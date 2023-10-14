# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label summersclover:
    show screen summersclover
    call screen summersclover

    return

label summersclover_start:
    stop music fadeout 1.0

    scene black
    with config.game_main_transition
    pause 2.0

    call summersclover_intro
    call summersclover_ch1
    call summersclover_ch2
    call summersclover_ch3

    return

label summersclover_timeskip:
    scene black with fadeslow

    stop sound fadeout 2.0
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    pause 2.0

    play music music_timeskip

    show kslogoheart at Transform(xalign=0.5, yalign=0.5, zoom=2.0)
    with clockwipe

    scene black
    show kslogowords at Transform(xalign=0.5, yalign=0.5, zoom=2.0)
    with clockwipe

    pause 2.0

    stop music fadeout 2.0

    scene black
    with clockwipe

    pause 2.0

    return
