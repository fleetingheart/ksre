#!/usr/bin/env python3
"""
Setup script for video processor
Creates virtual environment and installs Python dependencies

Author: Nikolai "neparij" Laptev
"""

import subprocess
import sys
from pathlib import Path


def create_venv():
    """Create virtual environment."""
    venv_path = Path('venv')
    if venv_path.exists():
        print("Virtual environment already exists")
        return True

    print("Creating virtual environment...")
    try:
        subprocess.check_call([sys.executable, '-m', 'venv', 'venv'])
        print("Virtual environment created successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")
        return False


def get_venv_python():
    """Get path to Python executable in virtual environment."""
    return Path('venv/bin/python')


def install_dependencies():
    """Install required Python packages in virtual environment."""
    print("Installing Python dependencies in virtual environment...")

    venv_python = get_venv_python()
    if not venv_python.exists():
        print("Error: Virtual environment Python not found")
        return False

    try:
        subprocess.check_call([
            str(venv_python), '-m', 'pip', 'install', '-r', 'requirements.txt'
        ])
        print("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return False


def main():
    print("Video Processor Setup")
    print("=" * 50)

    # Check current directory
    if not Path('video_processor.py').exists():
        print("Error: video_processor.py not found in current directory")
        print("Please run this script from the tl_videos_gen directory")
        sys.exit(1)

    # Create virtual environment
    if not create_venv():
        print("Setup failed due to virtual environment creation error")
        sys.exit(1)

    # Install Python dependencies
    if not install_dependencies():
        print("Setup failed due to dependency installation error")
        sys.exit(1)

    print("\nSetup Summary:")
    print("=" * 50)
    print("✓ Virtual environment created")
    print("✓ Python dependencies installed")
    print("\n�� Setup complete!")


if __name__ == '__main__':
    main()
