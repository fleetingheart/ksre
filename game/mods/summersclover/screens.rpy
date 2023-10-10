# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

screen summersclover():
    tag menu
    style_prefix "summersclover"

    add "blind"
    if main_menu:
        add "main_menu_bg"

    frame:
        style_suffix "interface"

        has vbox

        text _("Mods > Summer's Clover"):
            bold True
            size bold_size

        frame:    
            textbutton _("About") action ShowMenu("summersclover_about")

        textbutton _("Return"):
            yoffset 5
            style "return_button"
            action ShowMenu("mods")

screen summersclover_about():
    tag menu
    style_prefix "summersclover"

    add "blind"
    if main_menu:
        add "main_menu_bg"

    frame:
        style_suffix "interface"

        has vbox

        text _("Mods > Summer's Clover > About"):
            bold True
            size bold_size

        frame:
            text _("About Summer's Clover")

        textbutton _("Return"):
            yoffset 5
            style "return_button"
            action ShowMenu("summersclover")
