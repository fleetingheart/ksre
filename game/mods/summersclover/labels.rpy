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

    return
