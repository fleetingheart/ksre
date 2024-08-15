#!/bin/bash
# Copyright (c) 2024 Fleeting Heartbeat Studios
# Licensed under MPL 2.0 license.

title="Katawa Shoujo: Re-Engineered"

# Asking user to continue.
if !(zenity --question --title="${title}" --text "Welcome to the Katawa Shoujo: Re-Engineered Steam Deck installer!\nAre you ready to install the game?")
then
    zenity --info --title="${title}" --text "Installation aborted."
    exit
fi


# User agreed to installation
( flatpak install -u -y sh.fhs.KatawaShoujoReEngineered ) | \
    zenity --progress --title="${title}" \
    --text "Installing Katawa Shoujo: Re-Engineered from Flathub..." \
    --auto-close --pulsate --no-cancel

# Add-to-Steam shortcut (works only on Steam OS!                                    )
steamos-add-to-steam ~/.local/share/flatpak/exports/share/applications/sh.fhs.KatawaShoujoReEngineered.desktop

artworks=("Shizune & Misha" "Lilly & Hanako (shy)" "Lilly & Hanako (curious)" "Emi & Rin " "Saki & Rika")

artwork=`zenity --list --hide-header --title="${title}" \
    --height 600 --width 600 \
    --text "Choose the Steam artwork" \
    --column="0" "${artworks[@]}"`

if [[ "${artwork}" == "" ]]
then
    artwork="Shizune & Misha"       
fi

echo $artwork
