# Translation automation script.

This script is designed to process and translate game scripts.
It automates the merging, extraction, and application of translations for Japanese (`JP`).

## Prerequisites

Before running the script, ensure the following dependencies are installed:

- **Python**: Required for running the helper scripts (`merge_lines.py`, `extract.py`, `concat.py`, `apply.py`).
- **Bash**: The script is written in Bash and requires a Unix-like environment.
- Ensure the following variables are set:
  - `KS_ORIGINAL_GAME_PATH`: Path to the original game scripts.
  - `KS_RE_GAME_PATH`: Path to the re-engineered game scripts.
  - `KS_ORIGINAL_GAME_R18_PATH`: Path to the R18 scripts (if applicable).
  - `PYTHON`: Path to the Python interpreter.
- Place the decompiled scripts from the original KS in the `sources/game` directory. You can use [unrpyc](https://github.com/CensoredUsername/unrpyc) to decompile the scripts.
- Place the decompiled R18 scripts in the `sources/r18-game` directory. You can unpack the `r18.rpa` file from original KS to get the rpyc files with the [unrpa](https://github.com/Lattyware/unrpa). Then just use the `unrpyc` 
- With the RenPy's interface — generate a new empty translation and place it in the `tl_template` directory.

## Usage

1. Place the script in the appropriate directory where it can access the required files and directories.
2. Ensure the `SCRIPT_GROUPS` variable is set with the list of script groups to process.
3. Run the script:

   ```bash
   ./translate.sh
   
4. Whenever you get the errors you can check the `new-process_orig.rpy` and `new-process_orig_jp.merged.rpy` files. So edit the original translated script to match the original untranslated script (`en`).
5. Have a nice day~!

## Workflow

The script follows these steps:
1. Merges script sequences to the one file. (optional)
2. Merges the lines of translations (Japanese can have multiple dialogue lines with a single new-line that should be processed as a single line with newline-break) (optional)
3. Extracts the translation lines from the merged file.
4. Compares the extracted translation lines to generate the JSON mapping file.
5. Applies the translations to the KS:RE translation files.
