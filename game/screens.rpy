# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

screen skip_indicator():
    image "icon_skip":
        pos 1850, 35

screen say(who, what):
    style_prefix "say"

    vbox:
        style_suffix "vbox"
        
        if who and who.strip():
            window id "namebox":
                at colorblind(persistent.colorblind)
                style_suffix "namebox"
                text who id "who"
        else:
            null height 145

        window id "window":
            text what id "what"

screen doublespeak(c1, t1, c2, t2):
    style_prefix "doublespeak"

    frame id "namebox1":
        at colorblind(persistent.colorblind)
        style_suffix "namebox1"
        text ("{color=" + c1.who_args["color"] + "}" + renpy.translate_string(c1.name) + "{/color}") id "who1":
            size 40
            bold True

    frame id "window1":
        at colorblind(persistent.colorblind)
        style_suffix "window1"
        text t1 id "what1"

    frame id "namebox2":
        at colorblind(persistent.colorblind)
        style_suffix "namebox2"
        text ("{color=" + c2.who_args["color"] + "}" + renpy.translate_string(c2.name) + "{/color}") id "who2":
            size 40
            bold True

    frame id "window2":
        at colorblind(persistent.colorblind)
        style_suffix "window2"
        text t2 id "what2"

    image "icon_ctc" as ctc1:
        xpos 0.473
    image "icon_ctc" as ctc2:
        xpos 0.974

    key ["dismiss", "skip"] action Return()

    on "show" action If(renpy.is_skipping(), Return())

screen choice(items):
    style_prefix "choice"

    vbox:
        at colorblind(persistent.colorblind)
        for i in items:
            textbutton i.caption:
                if i.caption in persistent._seen_choices:
                    foreground "check_sl_fg_op_cb"
                    hover_foreground "check_sl_fg_cb"
                    action i.action
                else:
                    foreground "check_fg_op_cb"
                    hover_foreground "check_fg_cb"
                    action [AddToSet(persistent._seen_choices, i.caption), i.action, check_all_choices]

screen nvl(dialogue, items=None):
    window id "window":
        has vbox
        spacing 20
        at colorblind(persistent.colorblind)

        for d in dialogue:
            frame:
                has hbox

                if d.who is not None:
                    text d.who id d.who_id

                text d.what id d.what_id

screen confirm(message, yes_action, no_action=None, yes_text=None, no_text=None):
    modal True
    zorder 200
    style_prefix "confirm"

    add "blind"

    frame:
        style_suffix "interface"
        at colorblind(persistent.colorblind)

        has vbox

        hbox:
            null width 20
            text message
            null width 20

        null height 24

        hbox:
            spacing 40
            xalign 0.5

            textbutton (yes_text or _("Yes")) action [yes_action, Hide("confirm", transition=config.intra_transition)]
            textbutton (no_text or _("No")) action [(no_action or NullAction()), Hide("confirm", transition=config.intra_transition)]

        frame:
            ysize 1

            image "icon_hanako" xcenter -0.31 yoffset -128

    key "game_menu" action (no_action or Hide("confirm", transition=config.intra_transition))

screen game_menu():
    tag menu
    style_prefix "game_menu"

    default play_time = format_time(renpy.get_game_runtime())
    default scene_name = get_scene_name()
    default track_name = get_track_name()

    add "blind"

    frame:
        style_suffix "interface"
        at colorblind(persistent.colorblind)

        has vbox

        frame:
            ysize 1
            xcenter 0.525
            yoffset -128

            add "logo_large" zoom 0.25

        textbutton _("Return") action Return()

        textbutton _("History") action ShowMenu("history")

        textbutton _("Skip") action Skip()

        textbutton _("Auto") action Preference("auto-forward", "toggle")

        textbutton _("Options") action ShowMenu("prefs")

        textbutton _("Accessibility") action ShowMenu("accessibility")

        textbutton _("Saves") action ShowMenu("file_slots")

        if not renpy.emscripten:
            textbutton _("Mods") action ShowMenu("mods")

        textbutton _("Main menu") action MainMenu(True, False)

        if not renpy.android and not renpy.ios and not renpy.emscripten:
            textbutton _("Quit") action Quit(True)

    text (__("Playtime") + ": " + play_time):
        xalign 0.5
        text_align 0.5
        yanchor 0.0
        ypos 0.02

    text (__("Current scene") + ": " + scene_name + "\n"
        + __("Current track") + ": " + track_name):
        xalign 0.5
        yanchor 1.0
        ypos 0.98
        text_align 0.5

screen main_menu():
    tag menu
    style_prefix "main_menu"

    add "main_menu_bg" at colorblind(persistent.colorblind)

    vbox:
        at colorblind(persistent.colorblind)
        textbutton _("Start") action Start()

        textbutton _("Saves") action ShowMenu("file_slots")

        textbutton _("Extras") action ShowMenu("extra")

        textbutton _("Options") action ShowMenu("prefs")

        textbutton _("Accessibility") action ShowMenu("accessibility")

        if not renpy.emscripten:
            textbutton _("Mods") action ShowMenu("mods")

        if not renpy.android and not renpy.ios and not renpy.emscripten:
            textbutton _("Quit") action Quit(False)

screen prefs():
    tag menu
    style_prefix "prefs"

    if main_menu:    
        add "main_menu_bg" at colorblind(persistent.colorblind)
    add "blind"

    frame:
        style_suffix "interface"
        at colorblind(persistent.colorblind)

        has vbox

        spacing 6

        text _("Options"):
            bold True
            size bold_size

        frame:
            left_margin 8
            size_group "prefs"

            has vbox

            spacing 6

            vbox:
                style_prefix "check"

                if renpy.emscripten:
                    if persistent.hdisabled:
                        text _("Adult content is disabled.")
                    else:
                        text _("Adult content is enabled.")
                else:
                    textbutton _("Disable adult content") action ToggleVariable("persistent.hdisabled", True, False)

                if not renpy.android and not renpy.ios:
                    textbutton _("Fullscreen mode") action Preference("display", "toggle")

                textbutton _("Skip unread text") action Preference("skip", "toggle")

                textbutton _("Skip after choices") action Preference("after choices", "toggle")

                if not renpy.emscripten:
                    textbutton _("Parallax") action ToggleVariable("persistent.parallax", True, False)

                if not renpy.android and not renpy.ios and not renpy.emscripten:
                    textbutton _("Discord activity") action ToggleVariable("persistent.discord", True, False)

                if not renpy.android and not renpy.ios:
                    textbutton _("Hardware cursor") action [
                        ToggleVariable("persistent.hardware_cursor", True, False),
                        Function(lambda: setattr(config, "mouse_displayable",
                            mouse if not persistent.hardware_cursor and not renpy.android and not renpy.ios else None
                        ))
                    ]

                textbutton _("Blinking arrow") action ToggleVariable("persistent.blinking_arrow", True, False)

                textbutton _("Disable expression transitions") action [ToggleVariable("persistent.charachange", { 'master': None }, { 'master' : Dissolve(0.5) }), ToggleVariable("persistent.charachangefast", { 'master': None }, { 'master' : Dissolve(0.2) })]

            vbox:
                style_prefix "slider"

                hbox:
                    bar value Preference("text speed")

                    null width 15

                    text _("Text speed")

                null height 3

                hbox:
                    bar value Preference("auto-forward time")

                    null width 15

                    text _("Auto mode delay")

                null height 3

                if config.has_music and not renpy.android and not renpy.ios:
                    hbox:
                        bar value Preference("mixer music volume")

                        null width 15

                        text _("Music volume")

                    null height 3

                if config.has_sound and not renpy.android and not renpy.ios:
                    hbox:
                        bar value Preference("mixer sfx volume")

                        null width 15

                        text _("SFX volume")

                        null width 15

                        textbutton _("Test"):
                            style "test_button"
                            action Play("sound", "sfx/slide.ogg")

            textbutton _("Language selection..."):
                style "lang_button"
                action ShowMenu("language")

            textbutton _("Return"):
                style "return_button"
                action If(main_menu, true=Return(), false=ShowMenu("game_menu"))

    key "game_menu" action If(main_menu, true=Return(), false=ShowMenu("game_menu"))

screen language():
    tag menu
    style_prefix "language"

    if main_menu:    
        add "main_menu_bg" at colorblind(persistent.colorblind)
    add "blind"

    frame:
        style_suffix "interface"
        at colorblind(persistent.colorblind)
        
        has vbox

        spacing 6

        text _("Options > Language"):
            bold True
            size bold_size

        null

        frame:
            left_margin 26

            has vbox

            textbutton _("English") action Language(None)
            textbutton _("Russian") action Language("ru")
            textbutton _("French") action Language("fr")
            textbutton _("Italian") action Language("it")
            textbutton _("Spanish") action Language("es")
            textbutton _("German") action Language("de")
            textbutton _("Japanese") action Language("jp")
            textbutton _("Simplified Chinese") action Language("zh_hans")
            textbutton _("Traditional Chinese") action Language("zh_hant")

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("prefs")

    key "game_menu" action ShowMenu("prefs")

screen file_slots():
    tag menu
    style_prefix "file_slots"

    default save_hovered = False
    default local_saves_items = set()
    default local_dels_items = set()

    if main_menu:    
        add "main_menu_bg" at colorblind(persistent.colorblind)
    add "blind"

    frame:
        style_suffix "interface"
        at colorblind(persistent.colorblind)

        has vbox

        spacing 6

        text _("Saves"):
            bold True
            size bold_size

        frame:
            size_group "file_slots"

            has hbox

            viewport id "file_slots_vp":
                mousewheel True
                draggable True
                xysize 675, 500
                yinitial 1.0

                has vbox

                spacing 4

                for i, save in enumerate(renpy.list_saved_games(r'\d+')):
                    python:
                        if ";" in save[1]:
                            playtime, save_scene = save[1].split(";", 1)
                        else:
                            playtime = save[1]
                            save_scene = " "

                    hbox:
                        button:
                            xysize 637, 115
                            top_padding 6
                            hovered Function(local_saves_items.add, i)
                            unhovered Function(local_saves_items.remove, i)
                            if main_menu:
                                action [
                                    Function(setattr, config, "skipping", False),
                                    Function(setattr, config, "allow_skipping", True),
                                    Function(renpy.load, save[0])
                                ]
                            else:
                                action Show("confirm", config.intra_transition, _("Are you sure you want to\nload this save?"),
                                    [
                                        Function(setattr, config, "skipping", False),
                                        Function(setattr, config, "allow_skipping", True),
                                        Function(renpy.load, save[0])
                                    ]
                                )

                            if i in local_saves_items:
                                background "button_scribble"
                            else:
                                background "button_scribble_op"

                            has hbox

                            null width 8

                            image save[2]:
                                xysize 133, 101

                            null width 28

                            text (time.strftime("%b %d, %H:%M", time.localtime(save[3])) + " // "
                                + __("Playtime") + ": " + playtime + "\n"
                                + __("Scene") + ": " + get_scene_name(save_scene)):
                                size 30
                                if i in local_saves_items:
                                    color "#000"
                                else:
                                    color "#00000066"

                        button:
                            hovered Function(local_dels_items.add, i)
                            unhovered Function(local_dels_items.remove, i)
                            action Show("confirm", config.intra_transition, _("Are you sure you want to\ndelete this save?"), Function(renpy.unlink_save, save[0]))

                            if i in local_dels_items:
                                image "button_del"
                            else:
                                image "button_del_op"

            null width 60

            vbar value YScrollValue("file_slots_vp") style "vslider"

        textbutton _("Save"):
            style "save_button"
            action If(not (main_menu or _in_replay),
                true=Function(renpy.save, str(int(time.time() * 100000)), format_time(renpy.get_game_runtime()) + ";" + (current_scene or "")),
                false=None)

        textbutton _("Return"):
            yoffset 5
            style "return_button"
            action If(main_menu, true=Return(), false=ShowMenu("game_menu"))

    key "game_menu" action If(main_menu, true=Return(), false=ShowMenu("game_menu"))

screen extra():
    tag menu
    style_prefix "extra"

    default return_hovered = False
    default jukebox_hovered = False
    default gallery_hovered = False
    default library_hovered = False
    default cinema_hovered = False

    add "main_menu_bg" at colorblind(persistent.colorblind)
    add "blind"

    frame:
        style_suffix "interface"
        at colorblind(persistent.colorblind)

        has vbox

        spacing 6

        text _("Extras"):
            bold True
            size bold_size

        hbox:
            spacing 5

            button:
                yalign 1.0
                hovered SetScreenVariable("jukebox_hovered", True)
                unhovered SetScreenVariable("jukebox_hovered", False)
                action ShowMenu("jukebox")

                vbox:
                    if jukebox_hovered:
                        image "icon_lilly_colored":
                            xalign 0.5

                        text _("Jukebox"):
                            color "#000"
                            xalign 0.5
                    else:
                        image "icon_lilly":
                            xalign 0.5

                        text _("Jukebox"):
                            xalign 0.5

            button:
                yalign 1.0
                hovered SetScreenVariable("gallery_hovered", True)
                unhovered SetScreenVariable("gallery_hovered", False)
                action [Function(unlock_completion_bonus), ShowMenu("gallery")]

                vbox:
                    if gallery_hovered:
                        image "icon_rin_colored":
                            xalign 0.5

                        text _("Gallery"):
                            color "#000"
                            xalign 0.5
                    else:
                        image "icon_rin":
                            xalign 0.5

                        text _("Gallery"):
                            xalign 0.5

            button:
                yalign 1.0
                hovered SetScreenVariable("library_hovered", True)
                unhovered SetScreenVariable("library_hovered", False)
                action [SetVariable("completion_percentage", get_completion_percentage()), ShowMenu("library")]

                vbox:
                    if library_hovered:
                        image "icon_shizune_colored":
                            xalign 0.5

                        text _("Library"):
                            color "#000"
                            xalign 0.5
                    else:
                        image "icon_shizune":
                            xalign 0.5

                        text _("Library"):
                            xalign 0.5

            button:
                yalign 1.0
                hovered SetScreenVariable("cinema_hovered", True)
                unhovered SetScreenVariable("cinema_hovered", False)
                action ShowMenu("cinema")

                vbox:
                    if cinema_hovered:
                        image "icon_emi_colored":
                            xalign 0.5

                        text _("Cinema"):
                            color "#000"
                            xalign 0.5
                    else:
                        image "icon_emi":
                            xalign 0.5

                        text _("Cinema"):
                            xalign 0.5

        button:
            xalign 1.0
            action Return()
            hovered SetScreenVariable("return_hovered", True)
            unhovered SetScreenVariable("return_hovered", False)

            vbox:
                if return_hovered:
                    image "icon_hanako_colored":
                        xalign 0.5
                else:
                    image "icon_hanako":
                        xalign 0.5

                hbox:
                    if return_hovered:
                        image "button_return":
                            yoffset 5
                        null width 5
                        text _("Return"):
                            color "#000"
                    else:
                        image "button_return_op":
                            yoffset 5
                        null width 5
                        text _("Return")

        key "game_menu" action Return()

screen jukebox():
    tag menu
    style_prefix "jukebox"

    add "main_menu_bg" at colorblind(persistent.colorblind)
    add "blind"

    frame:
        style_suffix "interface"
        at colorblind(persistent.colorblind)
        
        has vbox

        spacing 6

        text _("Extras > Jukebox"):
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
                    if renpy.seen_audio(file) or config.developer:
                        textbutton name action Play("music", file)
                    else:
                        null height 1
                        image "button_locked_track_op"
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
            action ShowMenu("extra")

    key "game_menu" action ShowMenu("extra")

screen gallery(page=0):
    tag menu
    style_prefix "gallery"

    default return_hovered = False
    default local_items = set()

    add "main_menu_bg" at colorblind(persistent.colorblind)
    add "blind"

    frame:
        style_suffix "interface"
        at colorblind(persistent.colorblind)

        has vbox

        spacing 12

        text _("Extras > Gallery"):
            bold True
            size bold_size

        frame:
            size_group "gallery"
        
            has grid 4 3

            for i in range(page * 12, (page + 1) * 12):
                if i > len(_gallery_images) - 1:
                    image "button_cg_locked_lop"
                elif is_seen(_gallery_images[i][int(_gallery_images[i][0].startswith("thumb/"))]) or config.developer:
                    python:
                        img = _gallery_images[i]
                        if img[0].startswith("thumb/"):
                            thumb = im.Scale("event/" + img[0], 200, 150)
                        else:
                            thumb = im.Scale(img[0], 200, 150)

                    button:
                        xysize 220, 170
                        hovered Function(local_items.add, i)
                        unhovered Function(local_items.remove, i)
                        if i is len(_gallery_images) - 1:
                            action [Function(ach, "fullcomplete_achieve"), Call("watch_gallery", img[1:] if img[0].startswith("thumb/") else img)]
                        else:
                            action Call("watch_gallery", img[1:] if img[0].startswith("thumb/") else img )

                        if i in local_items:
                            image Composite((220, 170),
                                                (0, 0), "button_cg_locked",
                                                (10, 10), thumb)
                        else:
                            image Composite((220, 170),
                                                (0, 0), "button_cg_locked_op",
                                                (10, 10), Transform(thumb, matrixcolor=SaturationMatrix(0)))
                else:
                    button:
                        xysize 220, 170

                        image "button_cg_locked_op"

        frame:
            size_group "gallery"

            has hbox

            spacing 10

            text _("Page:")

            for i in range((len(_gallery_images) - 1) // 12 + 1):
                textbutton str(i + 1):
                    xpadding 4
                    xmargin 2
                    text_size 42
                    text_color "#00000066"
                    text_hover_color "#000"
                    text_insensitive_color "#000"

                    if i != page:
                        action ShowMenu("gallery", i)

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("extra")

    key "game_menu" action ShowMenu("extra")

screen library(page=0):
    tag menu
    style_prefix "library"

    default current_desc = None

    add "main_menu_bg" at colorblind(persistent.colorblind)
    add "blind"

    frame:
        style_suffix "interface"
        at colorblind(persistent.colorblind)
        has vbox

        text _("Extras > Library"):
            bold True
            size bold_size

        null height 8

        frame:
            has hbox
            spacing 40

            for i, replay_collection in enumerate(replays):
                textbutton replay_collection[0]:
                    if page == i:
                        text_insensitive_color "#000"
                    else:
                        action ShowMenu("library", i)

        null height 5

        frame:
            left_margin 8

            has hbox

            viewport id "library_vp_" + str(page):
                mousewheel True
                draggable True
                xysize 705, 500

                vbox:
                    for replay_stack in replays[page][1]:
                        text replay_stack[0]

                        for replay in replay_stack[1]:
                            if renpy.seen_label(replay[1]) or config.developer:
                                textbutton replay[0]:
                                    left_margin 30
                                    action [
                                        SetVariable("_current_replay", replay[1]),
                                        SetVariable("current_scene", replay[1]),
                                        Start("replay_start") ]
                                    hovered SetScreenVariable("current_desc", replay[2])
                                    unhovered SetScreenVariable("current_desc", None)
                            else:
                                null height 1
                                hbox:
                                    null width 30
                                    image "button_locked_track_op"
                                null height 1

            null width 25

            vbar value YScrollValue("library_vp_" + str(page)) style "vslider"

        null height 16

        text __("Completion: [completion_percentage]")

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("extra")

    if current_desc:
        text current_desc:
            color "#fff"
            size 36
            xalign 0.5
            yalign 1.0

    key "game_menu" action ShowMenu("extra")

screen cinema():
    tag menu
    style_prefix "cinema"

    default local_items = set()

    add "main_menu_bg" at colorblind(persistent.colorblind)
    add "blind"

    frame:
        style_suffix "interface"
        at colorblind(persistent.colorblind)
        has vbox

        spacing 32

        text _("Extras > Cinema"):
            bold True
            size bold_size

        grid 3 2:
            spacing 30

            for i, video in enumerate(videos):
                button:
                    xysize 220, 170
                    hovered Function(local_items.add, i)
                    unhovered Function(local_items.remove, i)

                    if video in persistent._watched_videos or config.developer:
                        action Call("watch_video", video)

                        if i in local_items:
                            image "button_cg_locked"

                            image video.replace(".mkv", "_tn.jpg"):
                                align 0.5, 0.5
                        else:
                            image "button_cg_locked_op"

                            image video.replace(".mkv", "_tn.jpg"):
                                align 0.5, 0.5
                                matrixcolor SaturationMatrix(0)
                    else:
                        image "button_cg_locked_op"

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("extra")

    key "game_menu" action ShowMenu("extra")

screen history():
    tag menu
    predict False
    style_prefix "history"

    add "blind"

    frame:
        style_suffix "interface"
        at colorblind(persistent.colorblind)

        has vbox

        spacing 6

        text _("History"):
            bold True
            size bold_size

        frame:
            xsize 788
            ysize 520

            has hbox

            viewport id "history_vp":
                mousewheel True
                draggable True
                xsize 730
                ysize 500

                has vbox

                spacing 10

                null height 10

                for h in _history_list:
                    if h.who:
                        text h.who:
                            bold True

                    hbox:
                        if h.who:
                            null width 40

                        # fixing issue with "NameError: *dialogue text* not found" by ssh character
                        python:
                            entry = str(h.what)
                            if entry.startswith("[") and not entry.startswith("[["):
                                entry = "[" + entry

                        text entry:
                            style_suffix "say"

                null height 10

            null width 10

            vbar value YScrollValue("history_vp") style "vslider"

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("game_menu")

    key "game_menu" action ShowMenu("game_menu")

screen written_note(text, quiet=False, custom_background=None):
    modal True
    style_prefix "note"

    frame at note_tf, colorblind(persistent.colorblind):
        if custom_background:
            background custom_background

        text text

    key ["dismiss", "skip"] action Return()

    on "show" action [If(not quiet, Play("sound", sfx_paper)), If(renpy.is_skipping(), Return())]

screen accessibility():
    tag menu
    style_prefix "prefs"

    if main_menu:    
        add "main_menu_bg" at colorblind(persistent.colorblind)
    add "blind"

    frame:
        at colorblind(persistent.colorblind)
        style "interface_frame"

        has vbox

        text _("Accessibility"):
            bold True
            size bold_size

        null height 15

        frame:
            left_margin 8

            has vbox

            spacing 6

            text _("Fonts"):
                bold True
                size bold_size

            vbox:
                style_prefix "check"

                textbutton _("Default") action Preference("font transform", "none")

                # TODO: Do not allow "Deja Vu Sans" in current language is "jp"
                textbutton "DejaVu Sans" action Preference("font transform", "dejavusans")

                textbutton "OpenDyslexic" action Preference("font transform", "opendyslexic")

                textbutton _("High contrast") action Preference("high contrast text", "toggle")

            if not renpy.android and not renpy.ios and not renpy.emscripten:
                text _("Self-voicing"):
                    bold True
                    size bold_size

                vbox:
                    style_prefix "check"

                    textbutton (_("Enable")) action Preference("self voicing", "toggle")

                vbox:
                    style_prefix "slider"

                    hbox:
                        bar value Preference("self voicing volume drop")

                        null width 15

                        text _("Volume drop")

            text _("Mental health"):
                bold True
                size bold_size

            vbox:
                style_prefix "check"

                textbutton _("Skip hurtful adult scenes") action ToggleVariable("persistent.disable_disturbing_content", True, False)

            text _("Colorblind filter"):
                bold True
                size bold_size

            $ filterLookup = {
                "None": [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                "Deuteranopia": [0.43, 0.72, -0.15, 0.0, 0.34, 0.57, 0.09, 0.0, -0.02, 0.03, 1.00, 0.0, 0.0, 0.0, 0.0, 1.0],
                "Protanopia": [0.20, 0.99, -0.19, 0.0, 0.16, 0.79, 0.04, 0.0, 0.01, -0.01, 1.00, 0.0, 0.0, 0.0, 0.0, 1.0],
                "Tritanopia": [0.97, 0.11, -0.08, 0.0, 0.02, 0.82, 0.16, 0.0, -0.06, 0.88, 0.18, 0.0, 0.0, 0.0, 0.0, 1.0]
            }

            frame:
                xysize (100, 36)
                vbox:
                    hbox:
                        text ">" at rotateBy(90 if expanded else 0)
                        textbutton selected action ToggleVariable("expanded", True, False) at left


                    if expanded:
                            frame:
                                background "config_bg" at colorblind(persistent.colorblind)
                                if renpy.android or renpy.ios:
                                    xoffset 55
                                    yoffset -84
                                else:
                                    xoffset 43
                                    yoffset -71
                                xpadding 13
                                ypadding 13

                                vbox:
                                    spacing 6
                                    for item in filterLookup.keys():
                                        textbutton item action [ToggleVariable("persistent.colorblind", filterLookup[item], None), SetVariable("expanded", False), SetVariable("selected", item if item != "None" else "Options")]

            textbutton _("Return"):
                style "return_button"
                action [SetVariable("expanded", False), If(main_menu, true=Return(), false=ShowMenu("game_menu"))]

    key "game_menu" action If(main_menu, true=Return(), false=ShowMenu("game_menu"))

screen mods():
    tag menu
    style_prefix "mods"

    if main_menu:    
        add "main_menu_bg" at colorblind(persistent.colorblind)
    add "blind"

    frame:
        at colorblind(persistent.colorblind)
        style_suffix "interface"
        has vbox
        at colorblind(persistent.colorblind)

        spacing 6

        text _("Mods"):
            bold True
            size bold_size

        frame:
            size_group "mods"

            has hbox

            viewport id "mods_vp":
                mousewheel True
                draggable True
                xysize 675, 500

                has vbox

                spacing 4

                grid 1 len(mods)
                for lbl, name in sorted(mods.iteritems()):
                    textbutton name:
                        action If(lbl in mods_with_menus, true=ShowMenu(lbl), false=Start(lbl))

            null width 60

            vbar value YScrollValue("mods_vp") style "vslider"

        textbutton _("Return"):
            yoffset 5
            style "return_button"
            action If(main_menu, true=Return(), false=ShowMenu("game_menu"))

    key "game_menu" action If(main_menu, true=Return(), false=ShowMenu("game_menu"))

screen adult_warning():
    style_prefix "adult_warning"
    add "adult_warning_bg" at colorblind(persistent.colorblind)

    vbox:
        at colorblind(persistent.colorblind)
        
        text _("You must be 18+ to see adult content within this game.\nDo you meet these requirements?")
        text _("Note: answering \"No\" does NOT prevent you from playing the game.")
        text _("This question will not be shown again after you start playing.")

        hbox:
            spacing 40
            xalign 0.5

            textbutton _("Yes"):
                action [
                    SetVariable("persistent.hdisabled", False), 
                    Hide("adult_warning"),
                    Call("splashscreen_intro")
                ]
            textbutton _("No"):
                action [
                    SetVariable("persistent.hdisabled", True), 
                    Hide("adult_warning"),
                    Call("splashscreen_intro")
                ]

    on "show" action If(persistent.adult_warning_shown, true=Call("splashscreen_intro"), false=None)
    on "hide" action SetVariable("persistent.adult_warning_shown", True), 
