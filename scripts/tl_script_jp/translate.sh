#!/bin/sh
# Author: Nikolai "neparij" Laptev
# Date: 2025-06-23
# Last update: 2025-06-25
# Purpose: This script processes and prepares translation files for the Katawa Shoujo Re-Engineered project,
#          including merging, extracting, and applying translations to the game scripts.
#          Currently it uses for Japanese translation only
#          Check the README.md for instructions


KS_ORIGINAL_GAME_PATH="$(pwd)/sources/game" # This is a path to the original decompiled rpy files
KS_ORIGINAL_GAME_R18_PATH="$(pwd)/sources/r18-game" # This is a path to the original decompiled rpy files (R18 patch)
KS_RE_GAME_PATH="$(cd "$(dirname "../../")" && pwd)/game" # This is a path to the Re-Engineered game files
PYTHON="python3"


# We need to have a groups beacause original KS scripts at sunday is ended before it is started in Re-Engineered version.
# They are using parts from Act2 for each girl <3
SCRIPT_GROUPS="
script-a1-monday
script-a1-tuesday
script-a1-wednesday
script-a1-thursday
script-a1-friday
script-a1-saturday
script-a1-sunday script-a2-emi script-a2-hanako script-a2-lilly script-a2-rin script-a2-shizune
script-a3-emi
script-a3-hanako
script-a3-lilly
script-a3-rin
script-a3-shizune
script-a4-emi
script-a4-hanako
script-a4-lilly
script-a4-rin
script-a4-shizune
"

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

log_bold_colored "223" "Katawa Shoujo Translation Helper - JP"
log_bold_colored "223" ""
log_bold_colored "223" "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
log_bold_colored "223" "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⢛⣩⣥⣶⣶⣶⣦⣭⣙⠛⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⢛⣋⣭⣴⣶⣶⣶⣬⣭⣛⢿⣷⣤⠀⠀⠀⠀⠀⠀⠀"
log_bold_colored "223" "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⢋⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣍⠻⣿⣤⠀⠀⠀⠀⣠⣾⠿⣩⣶⣿⣿⣿⣿⣿⣿⢹⠾⣮⢿⣿⣿⣷⣝⠿⣶⡀⠀⠀⠀⠀"
log_bold_colored "223" "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⢿⣶⣴⣿⢛⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⠀⡿⣼⠖⠛⠉⣀⣽⣌⢿⣦⠀⠀⠀"
log_bold_colored "223" "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠟⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⢋⣾⠛⣶⡿⣛⣛⠿⣿⢋⡶⠛⠋⣉⠀⣴⢶⠀⣿⢱⣾⣿⣿⣷⢻⣿⠀⠀"
log_bold_colored "223" "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣭⣈⣆⠘⡟⣦⣤⡈⠛⣶⢩⣭⢹⠀⠘⠒⠿⢀⣿⣿⣛⣛⡿⣿⣷⢻⣷⠀"
log_bold_colored "223" "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢋⡞⢳⠹⢿⣿⣿⢿⣛⣛⠿⣿⣿⣾⠀⣿⢹⠀⢻⠙⣿⢀⡟⣭⣿⣿⠷⣩⡿⠉⣠⠖⠶⢶⣤⣤⣽⣼⣿⡆⣿⡄"
log_bold_colored "223" "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣿⠀⠉⣽⡶⠋⣀⣤⣤⠈⣦⡏⣿⢠⠏⣾⠛⢀⣿⠀⡿⣼⣿⣿⣇⣿⣤⠶⣫⣾⠿⢛⠻⣿⣿⣿⣿⣿⣿⣿⡇"
log_bold_colored "223" "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢸⣾⠛⣦⡿⠟⢿⣿⣿⣿⣿⢱⠛⢀⡆⠀⠀⣴⣫⣶⣿⣹⠀⡿⢸⣮⣭⣿⠖⣭⠟⢀⣾⣴⣿⣿⣿⣿⣿⣿⣿⣛⣤⣾⣿⣿⡿⢦⣙⢿⣿⡏⣿⡇"
log_bold_colored "223" "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢀⣿⠀⠛⠉⣀⣿⣽⣭⣽⡻⣷⣭⣽⠀⠀⢹⡜⣿⣛⡾⠁⣴⢣⣿⣿⣿⢰⣉⣤⠞⣭⣿⣿⣿⣿⣿⣿⡿⣵⣿⠿⣿⣿⣿⣿⣶⣾⣿⣿⣦⢀⣿⠀"
log_bold_colored "223" "⠀⠀⠀⠀⣿⠉⣇⣰⠶⣦⣀⠀⠀⢣⢿⣤⠀⢹⣏⣉⣤⣤⠶⠶⣋⣿⢁⡇⢠⢿⠀⢻⣾⣀⣴⣛⣾⣿⣿⢟⣭⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⣵⣿⣫⢟⣾⣭⢾⣛⢿⣤⣿⣾⣹⡿⣾⡿⠀"
log_bold_colored "223" "⠀⠀⢀⣴⠛⠀⢉⠙⣿⣦⣀⠛⣦⠀⣿⣄⣷⠈⣧⠶⣭⣽⣭⠶⠛⢙⡆⣝⣫⣷⣻⠞⣵⡿⣿⣿⣿⣿⡿⠸⣾⣤⡶⣛⣶⠻⣿⣿⣿⣯⣿⣫⠿⣴⣿⣿⣿⣽⣿⣿⣷⣽⢿⣴⢰⣿⠀⠀"
log_bold_colored "223" "⠀⠰⣏⣠⡿⠀⣿⢿⠀⣿⠈⢷⣴⠃⠈⣿⢻⠀⢿⢛⠶⢶⠶⢛⣯⣷⣿⣿⣿⡿⣵⣭⢛⣛⣩⠶⣶⢻⣼⢸⣻⠻⣇⡿⣼⢠⣿⣫⣿⢛⡿⣵⣿⣿⣿⣿⣿⣿⣿⣮⣿⣿⣿⢡⣿⠁⠀⠀"
log_bold_colored "223" "⠀⠀⠀⠀⢻⠀⣿⢸⠀⣼⠀⠀⠀⠀⠀⠀⢷⠻⠾⣱⣿⣿⣿⣿⣿⣿⢛⡶⣛⣭⣿⡘⢃⡘⣷⣿⢂⣦⣡⢷⣶⣻⢻⢩⣶⡿⣾⡿⣾⣭⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⢟⡿⣴⣿⠀⠀⠀⠀"
log_bold_colored "223" "⠀⠀⠀⠀⢸⡀⣿⠘⠿⠋⠀⠀⠀⠀⠀⠀⠀⠙⣿⠌⢩⣥⢛⣛⣿⢹⣨⣶⣶⣶⢂⣿⣸⢛⠾⣛⣩⣾⣿⣦⣙⣒⣛⣾⠟⣼⣿⣿⣮⢾⡛⣿⣿⣿⣿⣿⡿⣵⣿⣿⢋⣾⠟⠀⠀⠀⠀⠀"
log_bold_colored "223" "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣀⣰⢛⠻⣙⣿⢙⣿⣼⢸⢡⣘⣶⣝⣒⣛⣭⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣼⣿⣿⠿⡿⢿⣾⡻⣭⢿⣿⣿⣿⣿⢋⣾⡿⠀⠀⠀⠀⠀⠀⠀"
log_bold_colored "223" "⠀⠀⠀⠀⢀⣀⢀⡾⣶⡟⣭⢹⣄⣶⣻⢻⣰⢿⣦⣿⠛⠛⣬⣉⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠻⣿⡁⣀⢹⣿⣿⢻⣝⢿⢿⢉⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀"
log_bold_colored "223" "⠀⠀⠀⠀⢻⠹⢛⣾⣡⢧⢋⣦⣿⠶⠞⠛⠉⠀⠀⠀⠀⠀⠀⠛⣿⣬⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠻⣿⣿⣿⣿⣿⠾⣩⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
log_bold_colored "223" "⠀⠀⠀⠀⠀⣆⣿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⣝⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣙⠿⢛⣴⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
log_bold_colored "223" "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⣙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣥⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
log_bold_colored "223" "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣦⣙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣭⣾⠿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
log_bold_colored "223" "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣦⣙⢿⣿⣿⣿⠿⣩⣾⠿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
log_bold_colored "223" "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣶⣭⣾⠿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
log_bold_colored "223" ""

log_bold "Current configuration:"
log " - Original game path: $KS_ORIGINAL_GAME_PATH"
log " - Re-Engineered game path: $KS_RE_GAME_PATH"






# Translate definitions
log_bold "Processing definitions..."
cp "tl_template/definitions.rpy" ./process_definitions.rpy
"$PYTHON" definitions.py process_definitions.rpy
if [ $? -ne 0 ]; then
    log_colored "196" "Error: Failed to apply translation"
    log_colored "196" "       script name: process_definitions.rpy"
    exit 1
fi
cp tl-process_definitions.rpy "${KS_RE_GAME_PATH}/tl/jp/definitions.rpy"
echo "${KS_RE_GAME_PATH}/tl/jp/definitions.rpy"



# Translate scripts
log_bold "Processing scripts..."

echo "$SCRIPT_GROUPS" | while IFS= read -r SCRIPT_GROUP; do
    log_bold "Processing script group: $SCRIPT_GROUP"

    rm -f process_orig_jp.rpy
    rm -f process_orig.rpy
    touch process_orig_jp.rpy
    touch process_orig.rpy

    for SCRIPT_NAME in $SCRIPT_GROUP; do
      cat "${KS_ORIGINAL_GAME_PATH}/${SCRIPT_NAME}_JP.rpy" >> process_orig_jp.rpy
      cat "${KS_ORIGINAL_GAME_PATH}/${SCRIPT_NAME}.rpy" >> process_orig.rpy
      log " - Added script: $SCRIPT_NAME"

      if [ -f "${KS_ORIGINAL_GAME_R18_PATH}/r18-${SCRIPT_NAME}_JP.rpy" ]; then
        cat "${KS_ORIGINAL_GAME_R18_PATH}/r18-${SCRIPT_NAME}_JP.rpy" >> process_orig_jp.rpy
        cat "${KS_ORIGINAL_GAME_R18_PATH}/r18-${SCRIPT_NAME}.rpy" >> process_orig.rpy
        log " - Added R18 script: ${SCRIPT_NAME}_JP.rpy"
      fi
    done

    # Merge lines for JP translation
    "$PYTHON" merge_lines.py process_orig_jp.rpy process_orig_jp.merged.rpy

    # Extract the translation lines
    "$PYTHON" extract.py process_orig_jp.merged.rpy
    "$PYTHON" extract.py process_orig.rpy

    # Prepare the translation dictionary
    "$PYTHON" concat.py new-process_orig.rpy new-process_orig_jp.merged.rpy
    if [ $? -ne 0 ]; then
        log_colored "196" "Error: Failed to extract lines from process_orig_jp.merged.rpy or process_orig.rpy"
        exit 1
    fi

    for SCRIPT_NAME in $SCRIPT_GROUP; do
        log_bold "Processing script: $SCRIPT_NAME"

        # Copy KS:RE script file
        cp "${KS_RE_GAME_PATH}/${SCRIPT_NAME}.rpy" ./process_re.rpy

        # Copy empty KS:RE translation file
        cp "tl_template/${SCRIPT_NAME}.rpy" ./process_tl.rpy

        "$PYTHON" apply.py new-process_orig.json process_tl.rpy
        if [ $? -ne 0 ]; then
            log_colored "196" "Error: Failed to apply translation"
            log_colored "196" "       script name: ${SCRIPT_NAME}"
            exit 1
        fi

        cp tl-process_tl.rpy "${KS_RE_GAME_PATH}/tl/jp/${SCRIPT_NAME}.rpy"
        echo "${KS_RE_GAME_PATH}/tl/jp/${SCRIPT_NAME}.rpy"
    done
done


# Cleanup temporary files

rm -f process_orig.rpy
rm -f process_orig_jp.rpy
rm -f process_orig_jp.merged.rpy

rm -f new-process_orig.rpy
rm -f new-process_orig_jp.merged.rpy

rm -f process_re.rpy
rm -f process_tl.rpy
rm -f process_definitions.rpy
rm -f tl-process_tl.rpy
rm -f tl-process_definitions.rpy

rm -f new-process_orig.json


exit 0;
