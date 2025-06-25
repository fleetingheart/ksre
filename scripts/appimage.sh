#!/bin/bash

set -e

APP_DIR="build/appimage"
APP_IMAGE_TOOLKIT_URL="https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-$(uname -m).AppImage"
APPIMAGETOOL="appimagetool-$(uname -m).AppImage"
TARBALL="./dists/KSRE-linux.tar.bz2"
EXECUTABLE_FILE="KSRE-linux/Katawa Shoujo Re-Engineered.sh"


mkdir -p $APP_DIR/opt ./dists

wget -O ./build/$APPIMAGETOOL $APP_IMAGE_TOOLKIT_URL
chmod +x ./build/$APPIMAGETOOL

tar -xjf $TARBALL -C $APP_DIR/opt
chmod +x "${APP_DIR}/opt/${EXECUTABLE_FILE}"

echo "Creating AppRun script..."
cat << 'EOF' > $APP_DIR/AppRun
#!/bin/bash
exec "${APPDIR}/opt/KSRE-linux/Katawa Shoujo Re-Engineered.sh"
EOF
chmod +x $APP_DIR/AppRun

echo "Creating .desktop file..."
cat << EOF > $APP_DIR/sh.fhs.ksre.desktop
[Desktop Entry]
Name=Katawa Shoujo: Re-Engineered
Exec="opt/KSRE-linux/Katawa Shoujo Re-Engineered.sh"
Icon=icon
Type=Application
StartupWMClass=Katawa Shoujo Re-Engineered
Categories=Game;AdventureGame
EOF

cp flatpak/sh.fhs.ksre.svg $APP_DIR/icon.svg

echo "Compiling AppImage..."
ARCH=$(uname -m) ./build/$APPIMAGETOOL --appimage-extract-and-run $APP_DIR ./dists/sh.fhs.ksre-$(uname -m).AppImage

echo "AppImage creation completed!"
