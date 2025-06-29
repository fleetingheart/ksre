#!/usr/bin/env python3
"""
Video Frame Processor with Mask Overlay
Processes video according to YAML configuration,
overlaying PNG masks on frames in specified ranges with interpolation support.
"""

import os
import sys
import yaml
import subprocess
import shutil
from pathlib import Path
from PIL import Image
import argparse


def load_config(config_path):
    """Load configuration from YAML file."""
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        print(f"Error loading configuration: {e}")
        sys.exit(1)


def extract_frames(video_path, frames_dir, verbose=False):
    """Extract all frames from video to frames/ directory."""
    print(f"Extracting frames from video: {video_path}")

    # Create frames directory
    frames_dir.mkdir(parents=True, exist_ok=True)

    # FFmpeg command to extract frames
    cmd = [
        'ffmpeg',
        '-v', 'verbose' if verbose else 'info',  # Add verbose control
        '-i', str(video_path),
        '-y',  # overwrite without confirmation
        str(frames_dir / 'frame_%05d.png')
    ]

    try:
        if verbose:
            print("FFmpeg command:", ' '.join(cmd))

        result = subprocess.run(cmd, capture_output=True, text=True)

        if verbose and result.stdout:
            print("FFmpeg stdout:")
            print(result.stdout)

        if result.returncode != 0:
            print(f"FFmpeg error (return code {result.returncode}):")
            print(result.stderr)
            sys.exit(1)

        print("Frames extracted successfully")

        if verbose and result.stderr:
            print("FFmpeg stderr:")
            print(result.stderr)

    except Exception as e:
        print(f"Error extracting frames: {e}")
        sys.exit(1)


def get_frame_count(frames_dir):
    """Get the number of extracted frames."""
    frame_files = list(frames_dir.glob('frame_*.png'))
    return len(frame_files)


def interpolate_masks(mask_from, mask_to, alpha):
    """Interpolate between two masks using alpha blending."""
    try:
        # Ensure both masks have the same size
        if mask_from.size != mask_to.size:
            mask_to = mask_to.resize(mask_from.size, Image.Resampling.LANCZOS)

        # Convert to RGBA if needed
        mask_from = mask_from.convert('RGBA')
        mask_to = mask_to.convert('RGBA')

        # Create interpolated mask
        interpolated = Image.blend(mask_from, mask_to, alpha)
        return interpolated

    except Exception as e:
        print(f"Error interpolating masks: {e}")
        return mask_from


def apply_interpolated_mask_to_frame(frame_path, mask_from_path, mask_to_path, alpha, output_path):
    """Apply interpolated mask to frame considering alpha channel."""
    try:
        # Load frame
        frame = Image.open(frame_path).convert('RGBA')

        # Load masks
        mask_from = Image.open(mask_from_path).convert('RGBA')
        mask_to = Image.open(mask_to_path).convert('RGBA')

        # Resize masks to frame size if necessary
        if mask_from.size != frame.size:
            mask_from = mask_from.resize(frame.size, Image.Resampling.LANCZOS)
        if mask_to.size != frame.size:
            mask_to = mask_to.resize(frame.size, Image.Resampling.LANCZOS)

        # Interpolate between masks
        interpolated_mask = interpolate_masks(mask_from, mask_to, alpha)

        # Overlay interpolated mask on top of frame
        result = Image.alpha_composite(frame, interpolated_mask)

        # Save result
        result.save(output_path, 'PNG')

    except Exception as e:
        print(f"Error applying interpolated mask to {frame_path}: {e}")
        # In case of error, copy original frame
        shutil.copy2(frame_path, output_path)


def apply_mask_to_frame(frame_path, mask_path, output_path):
    """Apply single mask to frame considering alpha channel."""
    try:
        # Load frame and mask
        frame = Image.open(frame_path).convert('RGBA')
        mask = Image.open(mask_path).convert('RGBA')

        # Resize mask to frame size if necessary
        if mask.size != frame.size:
            mask = mask.resize(frame.size, Image.Resampling.LANCZOS)

        # Overlay mask on top of frame
        result = Image.alpha_composite(frame, mask)

        # Save result
        result.save(output_path, 'PNG')

    except Exception as e:
        print(f"Error applying mask to {frame_path}: {e}")
        # In case of error, copy original frame
        shutil.copy2(frame_path, output_path)


def process_frames(config, frames_dir, output_dir):
    """Process frames according to configuration."""
    print("Processing frames...")

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get total frame count
    total_frames = get_frame_count(frames_dir)
    if total_frames == 0:
        print("No frames found for processing")
        return

    print(f"Found frames: {total_frames}")

    # Create dictionary for segment information by frame number
    frame_segments = {}
    for segment in config.get('segments', []):
        start_frame = segment['start_frame']
        end_frame = segment['end_frame']

        # Check for new format (mask_from/mask_to) or old format (mask)
        if 'mask_from' in segment and 'mask_to' in segment:
            mask_from_path = segment['mask_from']
            mask_to_path = segment['mask_to']

            # Check if mask files exist
            if not os.path.exists(mask_from_path):
                print(f"Warning: mask_from file not found: {mask_from_path}")
                continue
            if not os.path.exists(mask_to_path):
                print(f"Warning: mask_to file not found: {mask_to_path}")
                continue

            # Store segment info for each frame in range
            for frame_num in range(start_frame, end_frame + 1):
                # Calculate interpolation alpha (0.0 to 1.0)
                if end_frame == start_frame:
                    alpha = 0.0
                else:
                    alpha = (frame_num - start_frame) / (end_frame - start_frame)

                frame_segments[frame_num] = {
                    'type': 'interpolated',
                    'mask_from': mask_from_path,
                    'mask_to': mask_to_path,
                    'alpha': alpha
                }

        elif 'mask' in segment:
            # Old format - single mask
            mask_path = segment['mask']

            if not os.path.exists(mask_path):
                print(f"Warning: mask file not found: {mask_path}")
                continue

            for frame_num in range(start_frame, end_frame + 1):
                frame_segments[frame_num] = {
                    'type': 'single',
                    'mask': mask_path
                }
        else:
            print(f"Warning: segment missing mask information: {segment}")

    # Process each frame
    processed = 0
    for frame_num in range(1, total_frames + 1):
        frame_filename = f'frame_{frame_num:05d}.png'
        frame_path = frames_dir / frame_filename
        output_path = output_dir / frame_filename

        if not frame_path.exists():
            continue

        if frame_num in frame_segments:
            segment_info = frame_segments[frame_num]

            if segment_info['type'] == 'interpolated':
                # Apply interpolated mask
                apply_interpolated_mask_to_frame(
                    frame_path,
                    segment_info['mask_from'],
                    segment_info['mask_to'],
                    segment_info['alpha'],
                    output_path
                )
            elif segment_info['type'] == 'single':
                # Apply single mask (backward compatibility)
                apply_mask_to_frame(frame_path, segment_info['mask'], output_path)
        else:
            # Just copy frame
            shutil.copy2(frame_path, output_path)

        processed += 1
        if processed % 100 == 0:
            print(f"Processed frames: {processed}/{total_frames}")

    print(f"Processing completed. Total frames: {processed}")


def main():
    parser = argparse.ArgumentParser(description='Video processing with mask overlay and interpolation')
    parser.add_argument('config', help='Path to YAML configuration file')
    parser.add_argument('--frames-dir', default='frames',
                        help='Directory for extracted frames (default: frames)')
    parser.add_argument('--output-dir', default='output',
                        help='Directory for output (default: output)')
    parser.add_argument('--keep-frames', action='store_true',
                        help='Keep extracted frames after processing')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Enable verbose FFmpeg output for debugging')

    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)

    # Check required fields
    if 'video' not in config:
        print("Error: 'video' field missing in configuration")
        sys.exit(1)

    video_path = Path(config['video'])
    if not video_path.exists():
        print(f"Error: video file not found: {video_path}")
        sys.exit(1)

    frames_dir = Path(args.frames_dir)
    output_dir = Path(args.output_dir)

    try:
        # Extract frames from video
        extract_frames(video_path, frames_dir, verbose=args.verbose)

        # Process frames
        process_frames(config, frames_dir, output_dir)

        # Remove temporary frames if not specified otherwise
        if not args.keep_frames:
            print("Removing temporary frames...")
            shutil.rmtree(frames_dir, ignore_errors=True)

        print(f"Done! Results saved to: {output_dir}")

    except KeyboardInterrupt:
        print("\nProcessing interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
