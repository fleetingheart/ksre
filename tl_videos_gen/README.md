# Video Translation Processing

Tools for adding translated text to videos with mask overlays and effects.

## Process

1. **Setup environment**:
   ```bash
   python3 setup.py
   source venv/bin/activate
   ```

2. **Process video with masks** (remove original text):
   ```bash
   python3 video_processor.py video_config_name.yaml --output-dir clean_frames
   ```

3. **Add translated text**:
   ```bash
   python3 translation_processor.py --frames-dir clean_frames --translation ru video_config_name.yaml
   ```

## Preview mode

For quick testing (1/4 resolution):
```bash
python3 video_processor.py video_config_name.yaml --preview
python3 translation_processor.py --translation ru video_config_name.yaml --preview
```

## Configuration

Each video needs its own YAML configuration file with two main sections:

### Masks (for video_processor.py)
```yaml
video: path/to/source_video.mkv
masks:
  - mask_from: path/to/start_mask.png
    mask_to: path/to/end_mask.png
    start_frame: 100
    end_frame: 200
```

Masks are interpolated from `mask_from` to `mask_to` across the frame range.

### Text & Translations (for translation_processor.py)
```yaml
video: path/to/source_video.mkv  # for audio
output_template: path/to/output_{lang}.mkv
segments:
  - align: center
    colors:
      - color_from: [255, 255, 255, 0]
        color_to: [255, 255, 255, 255]
        start_frame: 100
        end_frame: 120
    effects:
      - blur_from: 10
        blur_to: 0
        start_frame: 100
        end_frame: 120
    position_from: [0.5, 0.3]
    position_to: [0.5, 0.3]
    start_frame: 100
    end_frame: 200

translations:
  ru:
    - font: path/to/font.ttf
      size: 64
      text: "Русский текст"
  en:
    - font: path/to/font.ttf
      size: 64  
      text: "English text"
```

Detailed help: `--help` for each utility
