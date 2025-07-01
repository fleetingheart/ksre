#!/bin/bash
# Video Translation Processing Script
# Author: Nikolai "neparij" Laptev

python3 ./setup.py
source venv/bin/activate

#PREVIEW=${PREVIEW:-true}
PREVIEW=${PREVIEW:-false}

VIDEOS=$(cat <<EOF
#op_1
tc_act1
#tc_act2_hanako
#tc_act2_lilly
#tc_act2_rin
#tc_act2_shizune
#tc_act3_emi
#tc_act3_hanako
#tc_act3_lilly
tc_act3_rin
#tc_act3_shizune
#tc_act4_emi
#tc_act4_hanako
#tc_act4_lilly
#tc_act4_rin
#tc_act4_shizune
EOF
)

LANGUAGES=$(cat <<EOF
de
es
fr
it
jp
ru
zh_hans
EOF
)

log() {
    text="$1"
    printf "%s\n" "$text"
}

log_colored() {
    color="$1"
    text="$2"
    printf "\033[38;5;%sm %s \033[0m\n" "$color" "$text"
}

log_bold() {
    text="$1"
    printf "\033[1m%s\033[0m\n" "$text"
}

log_bold_colored() {
    color="$1"
    text="$2"
    printf "\033[1;38;5;%sm%s\033[0m\n" "$color" "$text"
}

if [[ "$PREVIEW" == "true" ]]; then
    log_bold_colored "196" "Running in preview mode. No actual processing will be done."
fi

for video in $VIDEOS; do
    if [[ "$video" == \#* ]]; then
        log_bold "Skipping video: $video"
        continue
    fi

    if [ ! -f "$video.yaml" ]; then
        log_bold_colored "196" "Video configuration file $video.yaml not found. Skipping."
        continue
    fi

    log_bold "Processing video: $video"
    rm -rf clean_frames
    if [[ "$PREVIEW" == "true" ]]; then
        python3 ./video_processor.py --output-dir clean_frames "${video}".yaml --preview
    else
        python3 ./video_processor.py --output-dir clean_frames "${video}".yaml
    fi

    for lang in $LANGUAGES; do
        if [[ "$lang" == \#* ]]; then
            log_bold "Skipping language: $lang"
            continue
        fi

        log_bold "Translating to language: $lang"
        rm -rf tl_frames
        if [[ "$PREVIEW" == "true" ]]; then
            python3 ./translation_processor.py --frames-dir clean_frames --temp-dir tl_frames --translation "$lang" "$video.yaml" --preview
        else
            python3 ./translation_processor.py --frames-dir clean_frames --temp-dir tl_frames --translation "$lang" "$video.yaml"
        fi
    done
done
