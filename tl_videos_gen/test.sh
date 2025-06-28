#!/bin/bash

python3 ./setup.py
source venv/bin/activate

# Act 3 - Rin
#python3 ./video_processor.py --keep-frames --output-dir clean_frames tc_act3_rin.yaml
python3 ./video_processor.py --output-dir clean_frames tc_act3_rin.yaml
python3 ./text_processor.py --frames-dir clean_frames --output-dir tl_frames tc_act3_rin_jp.yaml
python3 ./text_processor.py --frames-dir clean_frames --output-dir tl_frames tc_act3_rin_it.yaml
