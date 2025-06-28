#!/usr/bin/env python3
"""
Translation Processor for Video Frames
Adds animated text to video frames with interpolation support for position, color, and blur effects.
Then assembles the frames back into video with original audio.
"""

import os
import sys
import yaml
import shutil
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import argparse
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import multiprocessing


# Global font cache to avoid reloading fonts
_font_cache = {}


def load_config(config_path):
    """Load configuration from YAML file."""
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        print(f"Error loading configuration: {e}")
        sys.exit(1)


def get_frame_files(frames_dir):
    """Get sorted list of frame files."""
    frame_files = list(frames_dir.glob('frame_*.png'))
    return sorted(frame_files)


def get_cached_font(font_path, font_size):
    """Get font from cache or load and cache it."""
    cache_key = (font_path, font_size)
    if cache_key not in _font_cache:
        try:
            _font_cache[cache_key] = ImageFont.truetype(font_path, font_size)
        except (OSError, IOError):
            print(f"Warning: Could not load font {font_path}, using default")
            _font_cache[cache_key] = ImageFont.load_default()
    return _font_cache[cache_key]


def interpolate_value(value_from, value_to, alpha):
    """Interpolate between two values."""
    if isinstance(value_from, (list, tuple)) and isinstance(value_to, (list, tuple)):
        # Interpolate each component for lists/tuples (e.g., colors, positions)
        return [
            value_from[i] + (value_to[i] - value_from[i]) * alpha
            for i in range(len(value_from))
        ]
    else:
        # Interpolate single values (e.g., blur)
        return value_from + (value_to - value_from) * alpha


def get_interpolated_color(colors_config, frame_num):
    """Get interpolated color for specific frame."""
    # Find the exact range first
    for color_range in colors_config:
        start_frame = color_range['start_frame']
        end_frame = color_range['end_frame']
        
        if start_frame <= frame_num <= end_frame:
            if start_frame == end_frame:
                alpha = 0.0
            else:
                alpha = (frame_num - start_frame) / (end_frame - start_frame)
            
            color_from = color_range['color_from']
            color_to = color_range['color_to']
            
            interpolated = interpolate_value(color_from, color_to, alpha)
            return tuple(int(c) for c in interpolated)
    
    # If no exact range found, find the last applicable color
    # Sort ranges by start_frame to find the most recent one
    sorted_ranges = sorted(colors_config, key=lambda x: x['start_frame'])
    
    last_valid_color = None
    for color_range in sorted_ranges:
        if color_range['start_frame'] <= frame_num:
            # Use the end color of the most recent range that started before this frame
            last_valid_color = tuple(int(c) for c in color_range['color_to'])
        else:
            break
    
    if last_valid_color:
        return last_valid_color
    
    # If no valid color found, use the first color_from as default
    if colors_config:
        return tuple(int(c) for c in colors_config[0]['color_from'])
    
    return (0, 0, 0, 255)  # Default black only if no colors defined


def get_interpolated_effect(effects_config, effect_type, frame_num):
    """Get interpolated effect value for specific frame and effect type."""
    for effect_range in effects_config:
        if f'{effect_type}_from' not in effect_range:
            continue
            
        start_frame = effect_range['start_frame']
        end_frame = effect_range['end_frame']
        
        if start_frame <= frame_num <= end_frame:
            if start_frame == end_frame:
                alpha = 0.0
            else:
                alpha = (frame_num - start_frame) / (end_frame - start_frame)
            
            value_from = effect_range[f'{effect_type}_from']
            value_to = effect_range[f'{effect_type}_to']
            
            return interpolate_value(value_from, value_to, alpha)
    
    return 0  # Default value


def create_text_layer(text, font_path, font_size, color, position, frame_size, align='center', blur_radius=0):
    """Create a text layer with specified properties."""
    # High quality supersampling for smooth animation
    supersample = 4
    
    # Get cached font
    font = get_cached_font(font_path, font_size * supersample)
    
    # Create a transparent layer for text at higher resolution
    high_res_size = (frame_size[0] * supersample, frame_size[1] * supersample)
    high_res_layer = Image.new('RGBA', high_res_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(high_res_layer)
    
    # Get text bounding box at high resolution
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Calculate position based on relative coordinates and alignment at high resolution
    rel_x, rel_y = position
    x = rel_x * high_res_size[0]
    y = rel_y * high_res_size[1]
    
    # Adjust position based on alignment with float precision
    if align == 'center':
        x -= text_width / 2.0
        y -= text_height / 2.0
    elif align == 'right':
        x -= text_width
    # For 'left' alignment, no adjustment needed
    
    # Draw text at high resolution with float coordinates
    draw.text((x, y), text, font=font, fill=color)
    
    # Apply blur at high resolution if specified
    if blur_radius > 0:
        # Scale blur radius for high resolution
        high_res_blur = blur_radius * supersample
        high_res_layer = high_res_layer.filter(ImageFilter.GaussianBlur(radius=high_res_blur))
    
    # Downscale to target resolution with high-quality resampling
    text_layer = high_res_layer.resize(frame_size, Image.Resampling.LANCZOS)
    
    return text_layer


def process_frame_task(args):
    """Process a single frame - designed for multiprocessing."""
    frame_path, segments_config, frame_num, output_path = args
    
    try:
        # Load the frame
        frame = Image.open(frame_path).convert('RGBA')
        frame_size = frame.size
        
        # Process each text segment
        for segment in segments_config:
            start_frame = segment['start_frame']
            end_frame = segment['end_frame']
            
            # Skip if frame is outside segment range
            if not (start_frame <= frame_num <= end_frame):
                continue
            
            # Calculate position interpolation
            position_from = segment.get('position_from', [0.5, 0.5])
            position_to = segment.get('position_to', position_from)
            
            if start_frame == end_frame:
                position_alpha = 0.0
            else:
                position_alpha = (frame_num - start_frame) / (end_frame - start_frame)
            
            current_position = interpolate_value(position_from, position_to, position_alpha)
            
            # Get interpolated color
            color = get_interpolated_color(segment.get('colors', []), frame_num)
            
            # Get interpolated blur
            blur_radius = get_interpolated_effect(segment.get('effects', []), 'blur', frame_num)
            
            # Create text layer
            text_layer = create_text_layer(
                text=segment['text'],
                font_path=segment['font'],
                font_size=segment['size'],
                color=color,
                position=current_position,
                frame_size=frame_size,
                align=segment.get('align', 'center'),
                blur_radius=blur_radius
            )
            
            # Composite text layer onto frame
            frame = Image.alpha_composite(frame, text_layer)
        
        # Save processed frame with optimized settings
        frame.save(output_path, 'PNG', optimize=True)
        return True
        
    except Exception as e:
        print(f"Error processing frame {frame_path}: {e}")
        # In case of error, copy original frame
        shutil.copy2(frame_path, output_path)
        return False


def process_frame(frame_path, segments_config, frame_num, output_path):
    """Process a single frame by adding text according to configuration."""
    return process_frame_task((frame_path, segments_config, frame_num, output_path))


def process_frames(config, frames_dir, output_dir):
    """Process all frames according to configuration."""
    print("Processing frames with text overlay...")
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Get frame files
    frame_files = get_frame_files(frames_dir)
    if not frame_files:
        print("No frame files found in frames directory")
        return
    
    print(f"Found {len(frame_files)} frames")
    
    segments_config = config.get('segments', [])
    if not segments_config:
        print("No text segments found in configuration - copying all frames")
        # If no segments, just copy all frames using threading
        def copy_task(frame_file):
            output_path = output_dir / frame_file.name
            shutil.copy2(frame_file, output_path)
        
        with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
            list(executor.map(copy_task, frame_files))
        return
    
    # Pre-calculate which frames need text processing
    frames_with_text = set()
    for segment in segments_config:
        start_frame = segment['start_frame']
        end_frame = segment['end_frame']
        for frame_num in range(start_frame, end_frame + 1):
            frames_with_text.add(frame_num)
    
    print(f"Frames requiring text processing: {len(frames_with_text)}")
    print(f"Frames to copy unchanged: {len(frame_files) - len(frames_with_text)}")
    
    # Pre-load all fonts to cache
    print("Pre-loading fonts...")
    unique_fonts = set()
    for segment in segments_config:
        unique_fonts.add((segment['font'], segment['size'] * 4))  # 4x supersample
    
    for font_path, font_size in unique_fonts:
        get_cached_font(font_path, font_size)
    print(f"Loaded {len(unique_fonts)} unique fonts")
    
    # Separate frames for processing vs copying
    frames_to_process = []
    frames_to_copy = []
    
    for i, frame_file in enumerate(frame_files, 1):
        frame_num = i
        output_path = output_dir / frame_file.name
        
        if frame_num in frames_with_text:
            frames_to_process.append((frame_file, segments_config, frame_num, output_path))
        else:
            frames_to_copy.append((frame_file, output_path))
    
    processed = 0
    text_processed = 0
    copied = 0
    total_frames = len(frame_files)
    
    # Process text frames with threading (CPU-bound but PIL has GIL, so threading works well)
    if frames_to_process:
        print(f"Processing {len(frames_to_process)} frames with text...")
        with ThreadPoolExecutor(max_workers=min(16, multiprocessing.cpu_count())) as executor:
            for success in executor.map(process_frame_task, frames_to_process):
                text_processed += 1
                processed += 1
                if processed % 50 == 0 or processed == len(frames_to_process):
                    print(f"Text processing: {text_processed}/{len(frames_to_process)} frames")
    
    # Copy unchanged frames with threading
    if frames_to_copy:
        print(f"Copying {len(frames_to_copy)} unchanged frames...")
        def copy_task(args):
            frame_file, output_path = args
            shutil.copy2(frame_file, output_path)
        
        with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
            for _ in executor.map(copy_task, frames_to_copy):
                copied += 1
                if copied % 100 == 0 or copied == len(frames_to_copy):
                    print(f"Copying: {copied}/{len(frames_to_copy)} frames")
    
    total_processed = text_processed + copied
    print(f"Processing completed. Total: {total_processed}/{total_frames}, Text processed: {text_processed}, Copied: {copied}")
    print(f"Font cache size: {len(_font_cache)} fonts loaded")


def get_video_framerate(video_path):
    """Get framerate of the source video."""
    try:
        cmd = [
            'ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_streams',
            str(video_path)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Warning: Could not get framerate from {video_path}, using default 30fps")
            return 30
        
        import json
        data = json.loads(result.stdout)
        
        # Find video stream
        for stream in data.get('streams', []):
            if stream.get('codec_type') == 'video':
                fps_str = stream.get('r_frame_rate', '30/1')
                if '/' in fps_str:
                    num, den = fps_str.split('/')
                    return float(num) / float(den)
                else:
                    return float(fps_str)
        
        return 30  # Default fallback
        
    except Exception as e:
        print(f"Warning: Error getting framerate: {e}, using default 30fps")
        return 30


def assemble_video(frames_dir, audio_source, output_path):
    """Assemble frames back into video with audio from source."""
    print(f"Assembling video from frames...")
    print(f"Audio source: {audio_source}")
    print(f"Output: {output_path}")
    
    # Get framerate from source video
    framerate = get_video_framerate(audio_source)
    print(f"Using framerate: {framerate}fps")
    
    # Ensure output directory exists
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # FFmpeg command to create video with audio
    cmd = [
        'ffmpeg',
        '-r', str(framerate),  # Input framerate
        '-i', str(frames_dir / 'frame_%05d.png'),  # Input frames
        '-i', str(audio_source),  # Audio source
        '-c:v', 'libx264',  # Video codec
        '-c:a', 'copy',  # Copy audio without re-encoding
        '-pix_fmt', 'yuv420p',  # Pixel format for compatibility
        '-y',  # Overwrite output file
        str(output_path)
    ]
    
    try:
        print("Running FFmpeg...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"FFmpeg error: {result.stderr}")
            sys.exit(1)
        print("Video assembly completed successfully!")
    except Exception as e:
        print(f"Error assembling video: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description='Add animated text to video frames and assemble back to video')
    parser.add_argument('config', help='Path to YAML configuration file')
    parser.add_argument('--frames-dir', default='frames', 
                       help='Directory containing input frames (default: frames)')
    parser.add_argument('--temp-dir', default='temp_frames', 
                       help='Directory for temporary processed frames (default: temp_frames)')
    parser.add_argument('--keep-frames', action='store_true',
                       help='Keep processed frames after video assembly')
    
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    
    # Check required fields
    required_fields = ['audio_source', 'output']
    for field in required_fields:
        if field not in config:
            print(f"Error: '{field}' field missing in configuration")
            sys.exit(1)
    
    frames_dir = Path(args.frames_dir)
    temp_dir = Path(args.temp_dir)
    audio_source = Path(config['audio_source'])
    output_path = Path(config['output'])
    
    # Check if frames directory exists
    if not frames_dir.exists():
        print(f"Error: frames directory not found: {frames_dir}")
        sys.exit(1)
    
    # Check if audio source exists
    if not audio_source.exists():
        print(f"Error: audio source not found: {audio_source}")
        sys.exit(1)
    
    try:
        # Process frames with text overlay
        process_frames(config, frames_dir, temp_dir)
        
        # Assemble video with audio
        assemble_video(temp_dir, audio_source, output_path)
        
        # Clean up temporary frames if not specified otherwise
        if not args.keep_frames:
            print("Removing temporary frames...")
            shutil.rmtree(temp_dir, ignore_errors=True)
        
        print(f"Translation processing complete! Output saved to: {output_path}")
        
    except KeyboardInterrupt:
        print("\nProcessing interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main() 