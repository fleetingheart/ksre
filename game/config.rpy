# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

init -501 python:
    gui.init(1920, 1080)

define config.developer = "auto"

define config.name = "Katawa Shoujo: Re-Engineered"
define config.version = "1.2.0"

define config.save_directory = config.name

define config.end_splash_transition = dotwipe_up

define config.enter_transition = dotwipe_down
define config.exit_transition = dotwipe_up

define config.enter_yesno_transition = dissolve
define config.exit_yesno_transition = dissolve

define config.main_game_transition = dotwipe_down
define config.game_main_transition = dotwipe_up

define config.intra_transition = dissolve

define config.window_show_transition = dissolve
define config.window_hide_transition = dissolve

define config.has_autosave = False
define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.main_menu_music = music_menus

define config.window_title = config.name
define config.window_icon = "gui/logo/window.png"

define config.predict_statements = 100

define config.rollback_enabled = True
define config.rollback_length = 256

define config.gestures = {
    "n": "game_menu",
    "s": "game_menu",
    "e": "rollback",
    "w": "rollforward"
}

define config.history_length = 250

default preferences.text_cps = 40

default persistent.hdisabled = False
default persistent.parallax = False
default persistent.discord = False
default persistent.hardware_cursor = False
default persistent.blinking_arrow = False

define mouse = MouseDisplayable("gui/icons/cursor.png", 0, 0)

define config.mouse_displayable = mouse if not persistent.hardware_cursor and not renpy.android and not renpy.ios else None

define _game_menu_screen = "game_menu"
