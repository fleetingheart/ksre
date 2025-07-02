#!/bin/bash
# Merge Playtime and custom font (jp,zh_hans)
# Author Sehaxe
fontforge -lang=ff -script merge.ff ../game/font/playtime.ttf ../game/font/VL-PGothic-Regular.ttf 1000 assets/jp.ttf
fontforge -lang=ff -script merge.ff ../game/font/playtime.ttf ../game/font/XiaolaiSC-Regular.ttf 1000 assets/zh_hans.ttf
rm -f temp-merge-font.ttf