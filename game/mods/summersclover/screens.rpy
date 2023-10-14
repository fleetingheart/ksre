# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

screen summersclover():
    tag menu
    style_prefix "summersclover"

    if main_menu:
        add "main_menu_bg"

    add "blind"

    frame:
        style_suffix "interface"

        has vbox

        text _("Mods > Summer's Clover"):
            bold True
            size bold_size

        frame:
            has vbox

            vbox:
                textbutton _("Start") action Start("summersclover_start")

                textbutton _("Jukebox") action ShowMenu("summersclover_jukebox")

                textbutton _("Library")

                textbutton _("Gallery")

                textbutton _("About") action ShowMenu("summersclover_about")

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("mods")

screen summersclover_jukebox():
    tag menu
    style_prefix "jukebox"

    add "main_menu_bg"
    add "blind"

    frame:
        style_suffix "interface"

        has vbox

        spacing 6

        text _("Mods > Summer's Clover > Jukebox"):
            bold True
            size bold_size

        text __("Now playing") + ": " + get_track_name()

        frame:
            left_margin 12

            has hbox

            viewport id "jukebox_vp":
                mousewheel True
                draggable True
                xsize 715
                ysize 500

                has vbox

                for file, name in _tracks.items():
                    if file.startswith("mods/summersclover"):
                        if renpy.seen_audio(file) or config.developer:
                            textbutton name action Play("music", file)
                        else:
                            null height 1
                            image opacity("gui/button/locked-track.png")
                            null height 1

            null width 4

            vbar value YScrollValue("jukebox_vp") style "vslider"

        hbox:
            spacing 15

            if not renpy.android and not renpy.ios:
                bar value Preference("mixer music volume"):
                    yoffset -4

                text _("Vol.")

            textbutton _("Stop"):
                style "stop_button"
                action Stop("music", fadeout=0.25)

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("summersclover")

screen summersclover_about():
    tag menu
    style_prefix "summersclover_about"

    if main_menu:
        add "main_menu_bg"

    add "blind"

    frame:
        style_suffix "interface"
        xsize 1200

        has vbox

        text _("Mods > Summer's Clover > About"):
            bold True
            size bold_size

        frame:
            has vbox

            vbox:

                text _("Summer's Clover is a game modification to Katawa Shoujo, aimed to tell the story of Miki Miura, written by Suriko, in visual novel format.\n")

                text _("It was created before Four Leaf Studios changed policy on game mods and is known as the oldest mod of the game.\n")

                text _("The code of the port to Katawa Shoujo: Re-Engineered is licensed under MPL 2.0.\n")

                text _("Version: ") + str(summersclover.version)

                text _("Ported for Katawa Shoujo:Re-Engineered by Vladimir Hodakov and Fleeting Heartbeat Studios team.\n")

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("summersclover")
