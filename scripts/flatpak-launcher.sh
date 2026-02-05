#!/bin/sh

cp -R /app/ksre /var/tmp/ksre
cp -Rv ~/.renpy/sh.fhs.ksre/mods/* /var/tmp/ksre
/var/tmp/ksre/Katawa\ Shoujo\ Re-Engineered.sh
rm -rf /var/tmp/ksre
