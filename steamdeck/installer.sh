#!/bin/bash
# Copyright (c) 2025 Fleeting Heartbeat Studios
# Licensed under MPL 2.0 license.

title="Katawa Shoujo: Re-Engineered"

installType=`kdialog --title "Installation Options" --radiolist "<div style='padding:20px; text-align:left'>
<font style='color:white'>Select your preferred installation method:</font><br><br>

<span style='font-size:14px; font-weight:bold'>1) Install with replacing existing Katawa Shoujo installation:</span><br>
<div style='padding-left:20px'>
    - It will have achievements support<br>
    - Will not auto-update<br>
    - You won't be able to play vanilla Steam release unless restored via Steam settings
</div><br>

<span style='font-size:14px; font-weight:bold'>2) Install as separate entity from FlatHub:</span><br>
<div style='padding-left:20px'>
    - It will auto-update<br>
    - Won't integrate with Steam achievements<br>
    - You will be able to play vanilla Steam release and KS:RE separately
</div></div>" \
"replace" "Install with replacing existing Katawa Shoujo installation" off \
"separate" "Install as separate entity from FlatHub" off \
--geometry 600x500+200+200`

if [[ "${installType}" == "separate" ]]; then
    # User agreed to installation separately.
    installProgress=`kdialog --title="${title}" --progressbar "${title}"`
    qdbus $installProgress Set "" value 1

    qdbus $installProgress setLabelText "Installing Katawa Shoujo: Re-Engineered from Flathub..."
    flatpak install --user --assumeyes sh.fhs.KatawaShoujoReEngineered || true

    if ! flatpak info "sh.fhs.KatawaShoujoReEngineered" >/dev/null 2>&1; then
        qdbus $installProgress close
        kdialog --title="${title}" --sorry "Installation failed."

        exit 1
    fi

    qdbus $installProgress Set "" value 80
    qdbus $installProgress setLabelText "Adding KS:RE as non-Steam game to Steam..."
    # Add-to-Steam shortcut (works only on Steam OS!)
    steamos-add-to-steam ~/.local/share/flatpak/exports/share/applications/sh.fhs.KatawaShoujoReEngineered.desktop
    sleep 10
    qdbus $installProgress Set "" value 100
    qdbus $installProgress close
elif [[ "${installType}" == "replace" ]]; then
    baseSteamPath="${HOME}/.local/share/Steam/steamapps/common"
    gameDir="Katawa Shoujo"

    if [ ! -d "${baseSteamPath}/${gameDir}" ]; then
        kdialog --title="${title}" --sorry "Installation aborted.\nEither the Steam release of KS is not installed or it is installed outside default Steam library directory."

        exit
    fi

    ksreReleaseURL="https://github.com/fleetingheart/ksre/releases/latest/download/KSRE-linux.tar.bz2"

    # User agreed to installation in-place.
    installProgress=`kdialog --title="${title}" --progressbar "${title}"`
    qdbus $installProgress Set "" value 1
    qdbus $installProgress setLabelText "Downloading Katawa Shoujo: Re-Engineered..."
    curl -L -o ksre.tar.bz2 "${ksreReleaseURL}"
    qdbus $installProgress Set "" value 50
    qdbus $installProgress setLabelText "Replacing Katawa Shoujo with the KS:RE installation..."
    tar -xf ksre.tar.bz2 -C "${baseSteamPath}/"
    mv "${baseSteamPath}/${gameDir}" "${baseSteamPath}/${gameDir}.$(date +%s)"
    ln -s "${baseSteamPath}/KSRE-linux/" "${baseSteamPath}/${gameDir}"
    mv "${baseSteamPath}/${gameDir}/Katawa Shoujo Re-Engineered.py" "${baseSteamPath}/${gameDir}/Katawa Shoujo.py"
    mv "${baseSteamPath}/${gameDir}/Katawa Shoujo Re-Engineered.sh" "${baseSteamPath}/${gameDir}/Katawa Shoujo.sh"
    mv "${baseSteamPath}/${gameDir}/lib/py3-linux-aarch64/Katawa Shoujo Re-Engineered" \
        "${baseSteamPath}/${gameDir}/lib/py3-linux-aarch64/Katawa Shoujo"
    mv "${baseSteamPath}/${gameDir}/lib/py3-linux-armv7l/Katawa Shoujo Re-Engineered" \
        "${baseSteamPath}/${gameDir}/lib/py3-linux-armv7l/Katawa Shoujo"
    mv "${baseSteamPath}/${gameDir}/lib/py3-linux-x86_64/Katawa Shoujo Re-Engineered" \
        "${baseSteamPath}/${gameDir}/lib/py3-linux-x86_64/Katawa Shoujo"
    rm ksre.tar.bz2
    qdbus $installProgress Set "" value 100
    qdbus $installProgress close

    kdialog --title="${title}" --msgbox "The game is installed. Don't forget to turn off Steam Cloud Saves before running it!"
else
    kdialog --title="${title}" --sorry "Installation aborted."

    exit
fi

steamGameID=""
if [[ "${installType}" == "separate" ]]; then
    steamGameID=`python ./shortcuts.py ${HOME}/.local/share/Steam/userdata/*/config | grep "Katawa Shoujo: Re-Engineered" | cut -d "'" -f 6`
else
    steamGameID="3068300" # Vanilla KS Steam ID
fi

echo $steamGameID

artwork=`kdialog --title="${title}" --radiolist "Choose the Steam artwork" \
"shisha" "Shizune & Misha" off \
"hanashy" "Lilly & Hanako (shy)" off \
"hanacur" "Lilly & Hanako (curious)" off \
"lemon" "Emi & Rin" off \
"saki" "Saki & Rika" off`

if [[ "${artwork}" == "" ]]; then
    kdialog --title="${title}" --sorry "Installation aborted. The game installed without artwork.\nAssign artwork manually using SteamGridDB."

    exit
fi


artworkProgress=`kdialog --title="${title}" --progressbar "${title}"`
qdbus $artworkProgress Set "" value 1
qdbus $artworkProgress setLabelText "Downloading artwork..."

# The artwork is picked, time to download stuff!
curl -o "${steamGameID}p.png" "https://cdn2.steamgriddb.com/grid/e0bef5004dd56c6dd7b6019af66f2638.png"
qdbus $artworkProgress Set "" value 20

curl -o "${steamGameID}_logo.png" "https://codeberg.org/fhs/katawa-shoujo-re-engineered/raw/branch/master/game/gui/logo/large-heartonly.png"
qdbus $artworkProgress Set "" value 30

curl -o "${steamGameID}_hero.png" "https://cdn2.steamgriddb.com/hero/55e875a41fe6ef14540212235cf7d507.png"
qdbus $artworkProgress Set "" value 40

if [[ "${artwork}" == "shisha" ]]; then
    curl -o "${steamGameID}.png" "https://cdn2.steamgriddb.com/grid/5dd9b1b5acffc5a9064edee7e2904414.png"
elif [[ "${artwork}" == "hanashy" ]]; then
    curl -o "${steamGameID}.png" "https://cdn2.steamgriddb.com/grid/136d0b006683c59d520b9bdcad8216b2.png"
elif [[ "${artwork}" == "hanacur" ]]; then
    curl -o "${steamGameID}.png" "https://cdn2.steamgriddb.com/grid/223edfb2c306b101b2c435165a36fca5.png"
elif [[ "${artwork}" == "lemon" ]]; then
    curl -o "${steamGameID}.png" "https://cdn2.steamgriddb.com/grid/c7a3c595757b44e3104900cffaea9e68.png"
elif [[ "${artwork}" == "saki" ]]; then
    curl -o "${steamGameID}.png" "https://cdn2.steamgriddb.com/grid/a8e0e456885f13f7c01cdba8f434794b.png"
fi
qdbus $artworkProgress Set "" value 50

qdbus $artworkProgress setLabelText "Installing artwork..."

for steamDir in ${HOME}/.local/share/Steam/userdata/*; do
    mkdir "${steamDir}/config/grid" || true
    cp "${steamGameID}.png" "${steamDir}/config/grid/"
    cp "${steamGameID}p.png" "${steamDir}/config/grid/"
    cp "${steamGameID}_logo.png" "${steamDir}/config/grid/"
    cp "${steamGameID}_hero.png" "${steamDir}/config/grid/"
done

rm "${steamGameID}p.png"
rm "${steamGameID}_logo.png"
rm "${steamGameID}_hero.png"
rm "${steamGameID}.png"

qdbus $artworkProgress Set "" value 100
qdbus $artworkProgress close

kdialog --title="${title}" --msgbox "The game installed successfully. Return to Steam Gaming Mode to enjoy it."
