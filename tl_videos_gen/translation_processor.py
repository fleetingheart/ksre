#!/usr/bin/env python3
"""
Translation Processor for Video Frames
Adds animated text to video frames with interpolation support for position, color, and blur effects.
Then assembles the frames back into video with original audio.

Author: Nikolai "neparij" Laptev
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

def blocks_config_add_tl(config, lang, text, font, size, stroke=0):
    """Add translation entry for a static block in blocks configuration."""
    if 'translations' not in config:
        config['translations'] = {}

    if lang not in config['translations']:
        config['translations'][lang] = []

    config['translations'][lang].append({
        'text': text,
        'font': font,
        'size': size,
        'stroke': stroke
    })

def blocks_config_get_tl_or_default(values, lang):
    """Get translation value for a specific language or return default if not found."""
    if lang in values:
        return values[lang]
    elif 'default' in values:
        return values['default']
    else:
        print(f"Error: No translation found for language '{lang}' and no default specified")
        sys.exit(1)

def parse_as_blocks_config(config):
    config['segments'] = []
    config['translations'] = {}

    languages_list = config.get('langs', [])
    if len(languages_list) == 0:
        print("Error: No languages specified in configuration")
        sys.exit(1)

    fade_in_frames = config.get('fade_in_frames', 0)
    fade_out_frames = config.get('fade_out_frames', 0)
    blur_radius = config.get('blur_radius', 0)
    font_size = config.get('font_size', 24)

    if 'fonts' not in config or len(config['fonts']) <= 1 or 'default' not in config['fonts']:
        print(f"Error: No default font specified in configuration")
        sys.exit(1)

    for block in config.get('blocks', []):
        if 'type' not in block or 'position' not in block or 'timeline' not in block:
            print(f"Error: Each block must have 'type', 'position', and 'timeline' fields")
            sys.exit(1)

        if block['type'] == 'static':
            config['segments'].append({
                'align': block.get('align', 'center'),
                'start_frame': block['timeline'][0],
                'end_frame': block['timeline'][1],
                'position_from': [ block['position'][0] / 1920.0, block['position'][1] / 1080.0 ],
                'position_to': [ block['position'][0] / 1920.0, block['position'][1] / 1080.0 ],
                'colors': [
                    {
                        'start_frame': block['timeline'][0],
                        'end_frame': block['timeline'][0] + fade_in_frames,
                        'color_from': [255, 255, 255, 0],
                        'color_to': [255, 255, 255, 255]
                    },
                    {
                        'start_frame': block['timeline'][1] - fade_out_frames,
                        'end_frame': block['timeline'][1],
                        'color_from': [255, 255, 255, 255],
                        'color_to': [255, 255, 255, 0]
                    }
                ],
                'effects': [
                    {
                        'start_frame': block['timeline'][0],
                        'end_frame': block['timeline'][0] + fade_in_frames,
                        'blur_from': blur_radius,
                        'blur_to': 0
                    },
                    {
                        'start_frame': block['timeline'][1] - fade_out_frames,
                        'end_frame': block['timeline'][1],
                        'blur_from': 0,
                        'blur_to': blur_radius
                    }
                ]
            })
            for lang in languages_list:
                blocks_config_add_tl(config, lang,
                                     blocks_config_get_tl_or_default(block['values'], lang),
                                     blocks_config_get_tl_or_default(config['fonts'], lang),
                                     font_size,
                                     stroke=1)


        elif block['type'] == 'credits_block':
            items_idx = 0
            for item in block['items']:
                config['segments'].append({
                    'align': block.get('align', 'left'),
                    'start_frame': block['timeline'][0],
                    'end_frame': block['timeline'][1],
                    'position_from': [(4 + block['position'][0]) / 1920.0, (6 + block['position'][1]) / 1080.0] if items_idx == 0
                                else [(4 + (block['position'][0] - 60 + 10 * items_idx)) / 1920.0, (6 + (block['position'][1] + 15 + items_idx * 45)) / 1080.0],
                    'position_to':   [(4 + (block['position'][0] - 50)) / 1920.0, (6 + block['position'][1]) / 1080.0] if items_idx == 0
                                else [(4 + block['position'][0]) / 1920.0, (6 + (block['position'][1] + 15 + items_idx * 45)) / 1080.0],
                    'colors': [
                        {
                            'start_frame': block['timeline'][0],
                            'end_frame': block['timeline'][0] + fade_in_frames,
                            'color_from': [0, 0, 0, 0],
                            'color_to': [0, 0, 0, 64]
                        },
                        {
                            'start_frame': block['timeline'][1] - fade_out_frames,
                            'end_frame': block['timeline'][1],
                            'color_from': [0, 0, 0, 64],
                            'color_to': [0, 0, 0, 0]
                        }
                    ],
                    'effects': [
                        {
                            'start_frame': block['timeline'][0],
                            'end_frame': block['timeline'][0] + fade_in_frames,
                            'blur_from': font_size / 4 + blur_radius,
                            'blur_to': font_size / 4
                        },
                        {
                            'start_frame': block['timeline'][0] + fade_in_frames,
                            'end_frame': block['timeline'][1] - fade_out_frames,
                            'blur_from': font_size / 4,
                            'blur_to': font_size / 4
                        },
                        {
                            'start_frame': block['timeline'][1] - fade_out_frames,
                            'end_frame': block['timeline'][1],
                            'blur_from': font_size / 4,
                            'blur_to': font_size / 4 + blur_radius
                            # 'blur_to': 0
                        }
                    ]
                })
                config['segments'].append({
                    'align': block.get('align', 'left'),
                    'start_frame': block['timeline'][0],
                    'end_frame': block['timeline'][1],
                    'position_from': [block['position'][0] / 1920.0, block['position'][1] / 1080.0] if items_idx == 0
                    else [(block['position'][0] - 60 + 10 * items_idx) / 1920.0,
                          (block['position'][1] + 15 + items_idx * 45) / 1080.0],
                    'position_to': [(block['position'][0] - 50) / 1920.0,
                                    block['position'][1] / 1080.0] if items_idx == 0
                    else [block['position'][0] / 1920.0, (block['position'][1] + 15 + items_idx * 45) / 1080.0],
                    'colors': [
                        {
                            'start_frame': block['timeline'][0],
                            'end_frame': block['timeline'][0] + fade_in_frames,
                            'color_from': [255, 255, 255, 0],
                            'color_to': [255, 255, 255, 255]
                        },
                        {
                            'start_frame': block['timeline'][1] - fade_out_frames,
                            'end_frame': block['timeline'][1],
                            'color_from': [255, 255, 255, 255],
                            'color_to': [255, 255, 255, 0]
                        }
                    ],
                    'effects': [
                        {
                            'start_frame': block['timeline'][0],
                            'end_frame': block['timeline'][0] + fade_in_frames,
                            'blur_from': blur_radius,
                            'blur_to': 0
                        },
                        {
                            'start_frame': block['timeline'][1] - fade_out_frames,
                            'end_frame': block['timeline'][1],
                            'blur_from': 0,
                            'blur_to': blur_radius
                        }
                    ]
                })
                for lang in languages_list:
                    blocks_config_add_tl(config, lang,
                                         blocks_config_get_tl_or_default(item, lang),
                                         blocks_config_get_tl_or_default(config['fonts'], lang),
                                         font_size,
                                         stroke=(1 if items_idx == 0 else 0))
                    blocks_config_add_tl(config, lang,
                                         blocks_config_get_tl_or_default(item, lang),
                                         blocks_config_get_tl_or_default(config['fonts'], lang),
                                         font_size,
                                         stroke=(1 if items_idx == 0 else 0))
                items_idx += 1

        else:
            print(f"Error: Unsupported block type '{block['type']}' in configuration")
            sys.exit(1)

    del config['blocks']
    del config['langs']
    del config['fade_in_frames']
    del config['fade_out_frames']
    del config['blur_radius']
    del config['font_size']
    del config['fonts']

    # print(f"Configuration (stringified): {yaml.dump(config, allow_unicode=True)}")
    #
    # sys.exit(0)
    return config


def load_config(config_path, translation_lang=None):
    """Load configuration from YAML file and merge with selected translation."""
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)

        # Check for required multilingual format
        if 'translations' not in config:
            if 'blocks' in config:
                print("Found blocks configuration, converting to multilingual format...")
                config = parse_as_blocks_config(config)
            else:
                print("Error: Config must contain 'translations' section for multilingual support")
                sys.exit(1)

        if not translation_lang:
            available_langs = list(config['translations'].keys())
            print(f"Error: --translation parameter is required. Available translations: {', '.join(available_langs)}")
            sys.exit(1)

        if translation_lang not in config['translations']:
            available_langs = list(config['translations'].keys())
            print(f"Error: Translation '{translation_lang}' not found in config.")
            print(f"Available translations: {', '.join(available_langs)}")
            sys.exit(1)

        segments = config.get('segments', [])
        translations = config['translations'][translation_lang]

        # Validate segment count matches translation count
        if len(segments) != len(translations):
            print(
                f"Error: Segment count ({len(segments)}) doesn't match translation count ({len(translations)}) for language '{translation_lang}'")
            sys.exit(1)

        # Merge segments with translations
        merged_segments = []
        for i, segment in enumerate(segments):
            merged_segment = segment.copy()
            translation = translations[i]

            # Add translation-specific fields
            merged_segment['font'] = translation['font']
            merged_segment['size'] = translation['size']
            merged_segment['text'] = translation['text']
            # Optional stroke parameter
            if 'stroke' in translation:
                merged_segment['stroke'] = translation['stroke']

            merged_segments.append(merged_segment)

        # Update config
        config['segments'] = merged_segments

        # Handle output path template
        if 'output_template' in config:
            config['output'] = config['output_template'].format(lang=translation_lang)
            del config['output_template']

        # Remove translations section as it's no longer needed
        del config['translations']

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


def create_text_layer(text, font_path, font_size, color, position, frame_size, align='center', blur_radius=0,
                      stroke_width=0, preview_mode=False):
    """Create a text layer with specified properties."""
    # High quality supersampling for smooth animation, or no supersampling for preview
    supersample = 1 if preview_mode else 4

    # Get cached font
    font = get_cached_font(font_path, font_size * supersample)

    # Create a transparent layer for text at higher resolution
    high_res_size = (frame_size[0] * supersample, frame_size[1] * supersample)
    high_res_layer = Image.new('RGBA', high_res_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(high_res_layer)

    # Get text bounding box at high resolution (including stroke if present)
    if stroke_width > 0:
        stroke_width_scaled = stroke_width * supersample
        bbox = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width_scaled)
    else:
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
    elif align == 'right':
        x -= text_width
    # For 'left' alignment, no adjustment needed

    # Draw text at high resolution with float coordinates and optional stroke
    if stroke_width > 0:
        stroke_width_scaled = stroke_width * supersample
        draw.text((x, y), text, font=font, fill=color,
                  stroke_width=stroke_width_scaled, stroke_fill=color)
    else:
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
    frame_path, segments_config, frame_num, output_path, preview_mode = args

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

            # Create text layer with adjusted font size, stroke and blur for preview mode
            font_size = segment['size'] // 4 if preview_mode else segment['size']
            stroke_width = segment.get('stroke', 0)
            if preview_mode and stroke_width > 0:
                stroke_width = stroke_width / 4.0
            if preview_mode and blur_radius > 0:
                blur_radius = blur_radius / 4.0

            text_layer = create_text_layer(
                text=segment['text'],
                font_path=segment['font'],
                font_size=font_size,
                color=color,
                position=current_position,
                frame_size=frame_size,
                align=segment.get('align', 'center'),
                blur_radius=blur_radius,
                stroke_width=stroke_width,
                preview_mode=preview_mode
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


def process_frame(frame_path, segments_config, frame_num, output_path, preview_mode=False):
    """Process a single frame by adding text according to configuration."""
    return process_frame_task((frame_path, segments_config, frame_num, output_path, preview_mode))


def process_frames(config, frames_dir, output_dir, preview_mode=False):
    """Process all frames according to configuration."""
    print("Processing frames with text overlay...")
    if preview_mode:
        print("Preview mode: using 1/4 resolution and no supersampling")

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Clean output directory if it exists
    for file in output_dir.glob('frame_*.png'):
        try:
            file.unlink()
        except Exception as e:
            print(f"Error removing existing frame file {file}: {e}")

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
    supersample_multiplier = 1 if preview_mode else 4
    for segment in segments_config:
        # Adjust font size for preview mode
        actual_font_size = segment['size'] // 4 if preview_mode else segment['size']
        unique_fonts.add((segment['font'], actual_font_size * supersample_multiplier))

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
            frames_to_process.append((frame_file, segments_config, frame_num, output_path, preview_mode))
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
            # In preview mode, frames are already resized by FFmpeg, so just copy
            shutil.copy2(frame_file, output_path)

        with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
            for _ in executor.map(copy_task, frames_to_copy):
                copied += 1
                if copied % 100 == 0 or copied == len(frames_to_copy):
                    print(f"Copying: {copied}/{len(frames_to_copy)} frames")

    total_processed = text_processed + copied
    print(
        f"Processing completed. Total: {total_processed}/{total_frames}, Text processed: {text_processed}, Copied: {copied}")
    print(f"Font cache size: {len(_font_cache)} fonts loaded")


def get_video_info(video_path):
    """Get comprehensive video information including framerate and codecs."""
    defaults = {
        'framerate': 30,
        'video_codec': 'libvpx-vp9',
        'audio_codec': 'libopus',
        'pixel_format': 'yuv420p'
    }
    try:
        video_info = defaults

        cmd = [
            'ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_streams',
            str(video_path)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Warning: Could not get video info from {video_path}")
            return defaults

        import json
        data = json.loads(result.stdout)

        # Find video and audio streams
        for stream in data.get('streams', []):
            if stream.get('codec_type') == 'video':
                # Get framerate
                fps_str = stream.get('r_frame_rate', '30/1')
                if '/' in fps_str:
                    num, den = fps_str.split('/')
                    video_info['framerate'] = float(num) / float(den)
                else:
                    video_info['framerate'] = float(fps_str)

                # Get video codec
                codec_name = stream.get('codec_name', 'h264')
                if codec_name == 'h264':
                    video_info['video_codec'] = 'libx264'
                elif codec_name == 'h265' or codec_name == 'hevc':
                    video_info['video_codec'] = 'libx265'
                elif codec_name == 'vp9':
                    video_info['video_codec'] = 'libvpx-vp9'
                elif codec_name == 'vp8':
                    video_info['video_codec'] = 'libvpx'
                elif codec_name == 'av1':
                    video_info['video_codec'] = 'libaom-av1'
                else:
                    video_info['video_codec'] = codec_name

                # Get pixel format
                pix_fmt = stream.get('pix_fmt', 'yuv420p')
                video_info['pixel_format'] = pix_fmt

            elif stream.get('codec_type') == 'audio':
                # Get audio codec
                codec_name = stream.get('codec_name', 'aac')
                if codec_name == 'aac':
                    video_info['audio_codec'] = 'aac'
                elif codec_name == 'mp3':
                    video_info['audio_codec'] = 'mp3'
                elif codec_name == 'opus':
                    video_info['audio_codec'] = 'libopus'
                elif codec_name == 'vorbis':
                    video_info['audio_codec'] = 'libvorbis'
                elif codec_name == 'flac':
                    video_info['audio_codec'] = 'flac'
                else:
                    video_info['audio_codec'] = codec_name

        return video_info

    except Exception as e:
        print(f"Warning: Error getting video info: {e}, using defaults")
        return defaults


def get_video_framerate(video_path):
    """Get framerate of the source video (legacy function for compatibility)."""
    return get_video_info(video_path)['framerate']


def preview_video(frames_dir, audio_source, verbose=False):
    """Preview frames as video with audio using FFmpeg pipe to ffplay."""
    print(f"Starting preview with ffplay...")
    print(f"Audio source: {audio_source}")
    print("Press 'q' to quit preview, SPACE to pause/unpause")

    # Get comprehensive video information
    video_info = get_video_info(audio_source)
    print(f"Source video info:")
    print(f"  Framerate: {video_info['framerate']}fps")

    try:
        print("Opening preview window...")

        # Use FFmpeg to combine frames with audio and pipe to ffplay
        ffmpeg_cmd = [
            'ffmpeg',
            '-r', str(video_info['framerate']),  # Input framerate
            '-i', str(frames_dir / 'frame_%05d.png'),  # Input frames
            '-i', str(audio_source),  # Audio source
            '-map', '0:v',  # Use video from first input (frames)
            '-map', '1:a',  # Use audio from second input (original video)
            '-c:v', 'libx264',  # Video codec
            '-c:a', 'copy',  # Copy audio
            '-pix_fmt', 'yuv420p',  # Pixel format
            '-f', 'matroska',  # Container format for pipe
            '-'  # Output to stdout
        ]

        ffplay_cmd = [
            'ffplay',
            '-window_title', 'Preview - Press q to quit',
            '-'  # Read from stdin
        ]

        if not verbose:
            ffmpeg_cmd.insert(1, '-loglevel')
            ffmpeg_cmd.insert(2, 'error')
            ffplay_cmd.insert(1, '-loglevel')
            ffplay_cmd.insert(2, 'error')

        if verbose:
            print("FFmpeg command:", ' '.join(ffmpeg_cmd))
            print("ffplay command:", ' '.join(ffplay_cmd))

        # Create pipe between ffmpeg and ffplay
        ffmpeg_proc = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE)
        ffplay_proc = subprocess.Popen(ffplay_cmd, stdin=ffmpeg_proc.stdout)

        # Close ffmpeg stdout in parent to allow pipe to work properly
        ffmpeg_proc.stdout.close()

        # Wait for ffplay to finish
        ffplay_proc.wait()
        ffmpeg_proc.wait()

        if ffplay_proc.returncode != 0:
            print(f"Preview failed with return code {ffplay_proc.returncode}")
        else:
            print("Preview completed!")

    except KeyboardInterrupt:
        print("\nPreview interrupted by user")
    except Exception as e:
        print(f"Error starting preview: {e}")
        raise


def assemble_video(frames_dir, audio_source, output_path, verbose=False):
    """Assemble frames back into video with audio from source, preserving original codecs."""
    print(f"Assembling video from frames...")
    print(f"Audio source: {audio_source}")
    print(f"Output: {output_path}")

    # Get comprehensive video information
    video_info = get_video_info(audio_source)
    print(f"Source video info:")
    print(f"  Framerate: {video_info['framerate']}fps")
    print(f"  Video codec: {video_info['video_codec']}")
    print(f"  Audio codec: {video_info['audio_codec']}")
    print(f"  Pixel format: {video_info['pixel_format']}")

    # Ensure output directory exists
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Build FFmpeg command to preserve original codecs
    cmd = [
        'ffmpeg',
        '-r', str(video_info['framerate']),  # Input framerate
        '-i', str(frames_dir / 'frame_%05d.png'),  # Input frames
        '-i', str(audio_source),  # Audio source
        '-c:v', video_info['video_codec'],  # Use original video codec
        '-c:a', 'copy',  # Copy audio without re-encoding to preserve original codec
        '-pix_fmt', video_info['pixel_format'],  # Use original pixel format
        '-y',  # Overwrite output file
    ]

    # Add verbose flag if requested
    if verbose:
        cmd.insert(1, '-v')
        cmd.insert(2, 'verbose')
    else:
        cmd.insert(1, '-v')
        cmd.insert(2, 'info')  # Show some info but not too verbose

    # Add output path at the end
    cmd.append(str(output_path))

    # Special handling for different codecs
    if video_info['video_codec'] == 'libx264':
        # Add H.264 specific settings for quality
        cmd.insert(-1, '-crf')
        cmd.insert(-1, '23')  # Good quality/size balance
        cmd.insert(-1, '-preset')
        cmd.insert(-1, 'medium')  # Good speed/quality balance
    elif video_info['video_codec'] == 'libx265':
        # Add H.265 specific settings
        cmd.insert(-1, '-crf')
        cmd.insert(-1, '28')  # HEVC equivalent to H.264 CRF 23
        cmd.insert(-1, '-preset')
        cmd.insert(-1, 'medium')
    elif video_info['video_codec'] in ['libvpx-vp9', 'libvpx']:
        # VP8/VP9 settings
        cmd.insert(-1, '-crf')
        cmd.insert(-1, '30')
        cmd.insert(-1, '-b:v')
        cmd.insert(-1, '0')  # Use CRF mode

    try:
        print("Running FFmpeg with original codecs...")
        if verbose:
            print("FFmpeg command:", ' '.join(cmd))

        result = subprocess.run(cmd, capture_output=True, text=True)

        if verbose and result.stdout:
            print("FFmpeg stdout:")
            print(result.stdout)

        if result.returncode != 0:
            print(f"FFmpeg error (return code {result.returncode}):")
            print(result.stderr)

            # Fallback to H.264 if original codec fails
            print("Attempting fallback to H.264...")
            fallback_cmd = [
                'ffmpeg',
                '-v', 'info' if not verbose else 'verbose',
                '-r', str(video_info['framerate']),
                '-i', str(frames_dir / 'frame_%05d.png'),
                '-i', str(audio_source),
                '-c:v', 'libx264',
                '-crf', '23',
                '-preset', 'medium',
                '-c:a', 'copy',
                '-pix_fmt', 'yuv420p',
                '-y',
                str(output_path)
            ]

            fallback_result = subprocess.run(fallback_cmd, capture_output=True, text=True)
            if fallback_result.returncode != 0:
                print(f"Fallback also failed: {fallback_result.stderr}")
                sys.exit(1)
            else:
                print("Fallback to H.264 successful!")
        else:
            print("Video assembly completed successfully with original codecs!")

        if verbose and result.stderr:
            print("FFmpeg stderr:")
            print(result.stderr)

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
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Enable verbose FFmpeg output for debugging')
    parser.add_argument('--translation', '-t', required=True,
                        help='Translation language code (required)')
    parser.add_argument('--preview', action='store_true',
                        help='Generate preview at 1/4 resolution and play with FFmpeg')

    args = parser.parse_args()

    # Load configuration with translation support
    config = load_config(args.config, args.translation)

    # Check required fields
    required_fields = ['video', 'output']
    for field in required_fields:
        if field not in config:
            print(f"Error: '{field}' field missing in configuration")
            sys.exit(1)

    frames_dir = Path(args.frames_dir)
    temp_dir = Path(args.temp_dir)
    audio_source = Path(config['video'])
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
        process_frames(config, frames_dir, temp_dir, preview_mode=args.preview)

        if args.preview:
            # Show preview with FFmpeg SDL output
            preview_video(temp_dir, audio_source, verbose=args.verbose)
        else:
            # Assemble video with audio, preserving original codecs
            assemble_video(temp_dir, audio_source, output_path, verbose=args.verbose)

        # Clean up temporary frames if not specified otherwise
        if not args.keep_frames and not args.preview:
            print("Removing temporary frames...")
            shutil.rmtree(temp_dir, ignore_errors=True)

        if args.preview:
            print(f"Preview processing complete!")
        else:
            print(f"Translation processing complete! Output saved to: {output_path}")

    except KeyboardInterrupt:
        print("\nProcessing interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
