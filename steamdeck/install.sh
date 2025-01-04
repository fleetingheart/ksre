#!/bin/bash
# Copyright (c) 2025 Fleeting Heartbeat Studios
# Licensed under MPL 2.0 license.

KDIALOG=$(which kdialog)
CURL=$(which curl)

if [ ! -f ${KDIALOG} ]; then
    echo "This script requires kdialog. Please install it."
    
    exit 1
fi

if [ ! -f ${CURL} ]; then
    echo "This script requires curl. Please install it."
    
    exit 1
fi

title="Katawa Shoujo: Re-Engineered"

# Asking user to continue.
if !(kdialog --title="${title}" --yesno \
    "Welcome to the Katawa Shoujo: Re-Engineered Steam Deck installer!\nAre you ready to install the game?")
then
    kdialog --title="${title}" --sorry "Installation aborted."

    exit
fi

mkdir /tmp/ksre-installer
cd /tmp/ksre-installer
curl -o installer.sh "https://codeberg.org/fhs/katawa-shoujo-re-engineered/raw/branch/master/steamdeck/installer.sh"
curl -o shortcuts.py "https://codeberg.org/fhs/katawa-shoujo-re-engineered/raw/branch/master/steamdeck/shortcuts.py"
chmod +x installer.sh
./installer.sh
