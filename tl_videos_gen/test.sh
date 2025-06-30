#!/bin/bash
# Video Translation Processing Script
# Author: Nikolai "neparij" Laptev

python3 ./setup.py
source venv/bin/activate

# Act 3 - Rin (preview)
#python3 ./video_processor.py --output-dir clean_frames tc_act3_rin.yaml --preview
#python3 ./translation_processor.py --frames-dir clean_frames --temp-dir tl_frames --translation ru tc_act3_rin.yaml --preview

# Act 3 - Rin
python3 ./video_processor.py --output-dir clean_frames tc_act3_rin.yaml
python3 ./translation_processor.py --frames-dir clean_frames --temp-dir tl_frames --translation it tc_act3_rin.yaml
python3 ./translation_processor.py --frames-dir clean_frames --temp-dir tl_frames --translation jp tc_act3_rin.yaml
python3 ./translation_processor.py --frames-dir clean_frames --temp-dir tl_frames --translation ru tc_act3_rin.yaml
