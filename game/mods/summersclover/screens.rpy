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
                textbutton _("Start")

                textbutton _("Library")

                textbutton _("Gallery")

                textbutton _("About") action ShowMenu("summersclover_about")

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("mods")

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

                text _("It was created before 4LS changed policy on game mods and is known as the oldest mod of the game.\n")

                text _("The code of the port to Katawa Shoujo: Re-Engineered is licensed under MPL 2.0.\n")

                text _("Version: ") + str(summersclover.version)

                text _("Ported by Vladimir Hodakov.\n")

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("summersclover")
