# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label splashscreen:
    if renpy.emscripten:
            show screen adult_warning
            call screen adult_warning
    else:
        call splashscreen_intro

    return

label splashscreen_intro:
    camera at defaultColorblind:
        function tf_parallax
    $ renpy.movie_cutscene("video/4ls.webm")

    return

label main_menu:
    show screen main_menu
    with dotwipe_up
    call screen main_menu

    return

label gallery:
    show screen gallery(0)
    call screen gallery(0)
    
    return


label cinema:
    show screen cinema
    call screen cinema

    return

label mods:
    show screen mods
    call screen mods

    return

label act_op(svideo):
    python:
        video = "video/" + svideo

        if video not in persistent._watched_videos:
            config.skipping = False
            persistent._watched_videos.add(video)

    if svideo != "op_1.webm":
        scene white
        with Dissolve(2.0)

    pause 1.0
    $ renpy.movie_cutscene(video)
    pause 0.1

    return

label watch_gallery(images):
    $ i = 0
    $ processing = True

    while processing:
        scene black
        if is_seen(images[i]) or config.developer:
            show expression (images[i].image if isinstance(images[i], Trigger) else images[i])
        else:
            $ processing = False
            show gallery_locked
            show expression Text("{} further images locked!".format(len(images) - i), color="#000") at truecenter
        with dissolve
        pause

        if processing:
            $ i += 1
            $ processing = i < len(images)

    scene black
    
    jump gallery

label watch_video(video):
    $ renpy.music.set_volume(volume=0.0, delay=1.0)

    if video == "video/op_1.webm":
        scene black
    else:
        scene white
    with dissolve

    pause 1.0
    $ renpy.movie_cutscene(video, stop_music=False)
    pause 0.1

    $ renpy.music.set_volume(volume=1.0, delay=1.0)

    jump cinema

label timeskip:
    stop sound fadeout 2.0
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    pause 2.0

    play music music_timeskip

    show kslogo heart at Transform(xalign=0.5, yalign=0.5)
    with clockwipe

    scene black
    show kslogo words at Transform(xalign=0.5, yalign=0.5)
    with clockwipe

    pause 2.0

    stop music fadeout 2.0

    scene black
    with clockwipe

    pause 2.0

    return

label start:
    stop music fadeout 1.0

    scene black
    with config.game_main_transition
    pause 2.0

    call a1_monday
    call a1_tuesday
    call a1_wednesday
    call a1_thursday
    call a1_friday
    call a1_saturday
    call a1_sunday


    if force_route == FR_EMI:
        call act_op("tc_act2_emi.webm")
        call a2_emi

        call act_op("tc_act3_emi.webm")
        call a3_emi

        if have_a_minute and talk_to_her_mom or let_misha_know:
            call act_op("tc_act4_emi.webm")
            call a4_emi
            $ credits_vid = "video/credits_emi.webm"
            # good ending
        else:
            # bad ending
            pass
    elif force_route == FR_HANAKO:
        call act_op("tc_act2_hanako.webm")
        call a2_hanako

        call act_op("tc_act3_hanako.webm")
        call a3_hanako

        call act_op("tc_act4_hanako.webm")
        call a4_hanako

        if go_to_the_city and agree_with_lilly:
            # good ending
            $ credits_vid = "video/credits_hanako.webm"
        elif go_to_the_city:
            # sad ending
            pass
        else:
            # rage ending
            pass
    elif force_route == FR_LILLY:
        call act_op("tc_act2_lilly.webm")
        call a2_lilly

        call act_op("tc_act3_lilly.webm")
        call a3_lilly

        call act_op("tc_act4_lilly.webm")
        call a4_lilly

        if want_true and address_it and mention_the_letter:
            # good ending
            $ credits_vid = "video/credits_lilly.webm"
        else:
            # bad ending
            pass
    elif force_route == FR_RIN:
        call act_op("tc_act2_rin.webm")
        call a2_rin

        call act_op("tc_act3_rin.webm")
        call a3_rin

        if not explain:
            call act_op("tc_act4_rin.webm")
            call a4_rin

            if is_true:
                # true ending
                pass
            else:
                # good ending
                $ credits_vid = "video/credits_rin.webm"
        else:
            # bad ending
            pass
    elif force_route == FR_SHIZU:
        call act_op("tc_act2_shizune.webm")
        call a2_shizune

        call act_op("tc_act3_shizune.webm")
        call a3_shizune

        call act_op("tc_act4_shizune.webm")
        call a4_shizune

        if refuse_misha:
            # good ending
            $ credits_vid = "video/credits_shizune.webm"
        else:
            # bad ending
            pass
    else:
        scene bloodred
        with Dissolve(4.0)

    call credits

    return

label replay_start:
    $ _in_replay = True

    stop music fadeout 1.0

    $ renpy.transition(dissolve)
    call expression _current_replay

    return

label credits:
    stop music
    stop ambient

    $ config.skipping = False
    $ config.allow_skipping = False

    scene black
    show credits mask
    with Dissolve(2.0)

    if credits_vid:
        play music music_credits noloop
        $ renpy.movie_cutscene(credits_vid, stop_music=False)
    else:
        play music music_musicbox volume 0.25 noloop

    show credits_final behind credits at Transform(xalign=0.5, yalign=0.0)
    with Dissolve(2.0)

    pause 1.0

    show credits_final behind credits:
        xalign 0.5 yalign 0.0
        acdc20_warp 60.0 yalign 1.0

    pause 60.0

    show expression Text("©MMXV Four Leaf Studios, Fleeting Heartbeat Studios", text_align=0.5, size=29) zorder 999 at Transform(xalign=0.5, yalign=0.605)
    with Dissolve(2.0)

    pause 5.0

    stop music fadeout 2.0
    scene black
    with Dissolve(2.0)

    pause 1.0

    $ config.allow_skipping = True

    return
