# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

init offset = -25

define mobile_ts_add = 10

define bold_size = 38

style default:
    font "font/playtime.ttf"
    size 36 + mobile_ts_add * (renpy.android or renpy.ios)

style gui_text is default:
    size 42 + mobile_ts_add * (renpy.android or renpy.ios)
    color "#00000066"

style gui_button_text is gui_text:
    hover_color "#000"
    insensitive_color "#00000019"

style check_button is gui_button:
    foreground "check_fg_op"
    hover_foreground "check_fg"
    selected_foreground "check_sl_fg_op"
    selected_hover_foreground "check_sl_fg"

style check_button_text is gui_button_text:
    first_indent 40
    yoffset 5

style check_text is gui_text

style slider:
    xmaximum 400
    ymaximum 60
    left_gutter 20
    right_gutter 20
    thumb_offset -3
    base_bar opacity("gui/bar/horizontal_bar.png")
    hover_left_bar "gui/bar/horizontal_bar.png"
    thumb opacity("gui/bar/horizontal_thumb.png")
    hover_thumb "gui/bar/horizontal_thumb.png"

style slider_text is gui_text

style vslider:
    bar_vertical True
    bar_invert True
    xmaximum 48
    ymaximum 500
    top_gutter 30
    bottom_gutter 30
    thumb_offset -10
    base_bar opacity("gui/bar/vertical_bar.png")
    hover_base_bar "gui/bar/vertical_bar.png"
    thumb opacity("gui/bar/vertical_thumb.png")
    hover_thumb "gui/bar/vertical_thumb.png"

style say_namebox is frame:
    xpos 0.033
    ypos 0.745
    xsize 0.33
    ysize 0.135
    xpadding 20
    top_padding 10
    background Frame("gui/bg/namebox.png")

style say_window is frame:
    xalign 0.5
    yanchor 1.0
    ypos 0.99
    xsize 0.9
    ysize 0.185
    xpadding 40
    top_padding 10
    background Frame("gui/bg/saybox.png")

style say_dialogue is default:
    size 42 + (mobile_ts_add - 6) * (renpy.android or renpy.ios)

style doublespeak_namebox1 is say_namebox:
    xpos 0.008

style doublespeak_namebox2 is say_namebox:
    xpos 0.508

style doublespeak_window1 is say_window:
    xsize 0.46875
    xalign 0.05

style doublespeak_window2 is say_window:
    xsize 0.46875
    xalign 0.995

style choice_vbox is vbox:
    align (0.5, 0.4)
    spacing 20

style choice_button:
    background Frame("gui/button/choice.png")
    xysize (1126, 65)

style choice_button_text is gui_button_text:
    xalign 0.5
    yalign 0.5
    xsize 13
    layout "nobreak"

style return_button is gui_button:
    yalign 0.5
    xalign 1.0
    foreground "return_op"
    hover_foreground "return_"

style return_button_text is gui_button_text:
    first_indent 53
    yoffset -6

style interface_frame is frame:
    background "config_bg"
    xalign 0.5
    yalign 0.5
    xpadding 40
    ypadding 32

style confirm_interface is interface_frame:
    background Frame("gui/bg/popup.png")

style confirm_label:
    xminimum 337
    xalign 0.5
    yalign 0.5
    bottom_margin 30

style confirm_text is gui_text:
    text_align 0.5

style confirm_button is gui_button

style confirm_button_text is gui_button_text

style main_menu_vbox is vbox:
    xpos 0.075
    ypos 0.9
    yanchor 1.0
    spacing 12

style main_menu_button is gui_button

style main_menu_button_text is gui_button_text

style game_menu_interface is interface_frame:
    xpadding 40
    bottom_padding 40
    top_padding 72
    fit_first True

style game_menu_vbox is vbox:
    xalign 0.5
    yalign 0.56
    spacing 12

style game_menu_button is gui_button:
    xalign 0.5

style game_menu_button_text is gui_button_text:
    size 54 + mobile_ts_add * (renpy.android or renpy.ios)

style prefs_interface is interface_frame

style prefs_text is gui_text

style prefs_button is gui_button

style prefs_button_text is gui_button_text

style adult_warning_vbox is vbox:
    xalign 0.5
    yalign 0.5
    spacing 12

style adult_warning_text is gui_text

style adult_warning_button is gui_button

style adult_warning_button_text is gui_button_text

style test_button is gui_button:
    foreground "music_play_op"
    hover_foreground "music_play"
    top_margin 6

style test_button_text is gui_button_text:
    first_indent 54
    yoffset -6

style lang_button is gui_button:
    yalign 0.5
    foreground "language_op"
    hover_foreground "language"

style lang_button_text is gui_button_text:
    first_indent 54
    yoffset -6

style language_interface is interface_frame

style language_text is gui_text

style language_button is gui_button

style language_button_text is gui_button_text

style file_slots_interface is interface_frame

style file_slots_text is gui_text

style file_slots_button is gui_button

style file_slots_button_text is gui_button_text

style save_button is gui_button:
    foreground "star_op"
    hover_foreground "star"

style save_button_text is gui_button_text:
    first_indent 60

style extra_interface is interface_frame

style extra_text is gui_text

style extra_button is gui_button

style extra_button_text is gui_button_text

style jukebox_interface is interface_frame

style jukebox_text is gui_text

style jukebox_button is gui_button

style jukebox_button_text is gui_button_text

style stop_button is gui_button:
    foreground "music_stop_op"
    hover_foreground "music_stop"
    top_margin 5

style stop_button_text is gui_button_text:
    first_indent 54
    yoffset -4

style gallery_interface is interface_frame

style gallery_text is gui_text

style gallery_button is gui_button

style gallery_button_text is gui_button_text

style library_interface is interface_frame

style library_text is gui_text

style library_button is gui_button

style library_button_text is gui_button_text

style cinema_interface is interface_frame

style cinema_text is gui_text

style cinema_button is gui_button

style cinema_button_text is gui_button_text

style mods_interface is interface_frame

style mods_text is gui_text

style mods_button is gui_button

style mods_button_text is gui_button_text

style history_interface is interface_frame

style history_text is gui_text

style history_say is default:
    color "#00000066"

style note_frame:
    xalign 0.5
    yalign 0.5
    xpadding 45
    ypadding 60
    xsize 643
    yminimum 483
    background Frame("gui/bg/note.png", 0, 16, tile=True)

style note_text is default:
    color "#000244"
    layout "greedy"
