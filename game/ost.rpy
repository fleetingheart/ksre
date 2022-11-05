# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

init offset = -10

init python:
    _tracks = {}

    def ks_music(filename, alias):
        fullpath = "bgm/" + filename + ".ogg"
        setattr(store, "music_" + alias, fullpath)
        store._tracks[fullpath] = filename.replace("_", " ")

    ks_music("Afternoon", "tranquil")
    ks_music("Ah_Eh_I_Oh_You", "nurse")
    ks_music("Air_Guitar", "soothing")
    ks_music("Aria_de_l'Etoile", "twinkle")
    ks_music("Breathlessly", "moonlight")
    ks_music("Caged_Heart", "rain")
    ks_music("Cold_Iron", "tragic")
    ks_music("Comfort", "comfort")
    ks_music("Concord", "lilly")
    ks_music("Daylight", "daily")
    ks_music("Ease", "ease")
    ks_music("Everyday_Fantasy", "another")
    ks_music("Friendship", "friendship") 
    ks_music("Fripperies", "happiness")
    ks_music("Generic_Happy_Music", "comedy")
    ks_music("High_Tension", "tension")
    ks_music("Hokabi", "running")
    ks_music("Innocence", "innocence")
    ks_music("Letting_my_Heart_Speak", "heart")
    ks_music("Lullaby_of_Open_Eyes", "serene")
    ks_music("Moment_of_Decision", "drama")
    ks_music("Nocturne", "night")
    ks_music("Out_of_the_Loop", "kenji")
    ks_music("Painful_History", "hanako")
    ks_music("Parity", "rin")
    ks_music("Passing_of_Time", "timeskip")
    ks_music("Raindrops_and_Puddles", "dreamy")
    ks_music("Red_Velvet", "jazz")
    ks_music("Romance_in_Andante_II", "romance")
    ks_music("Romance_in_Andante", "credits")
    ks_music("Sarabande_from_BWV1010", "musicbox")
    ks_music("School_Days", "normal")
    ks_music("Shadow_of_the_Truth", "sadness")
    ks_music("Standing_Tall", "emi")
    ks_music("Stride", "pearly")
    ks_music("The_Student_Council", "shizune")
    ks_music("To_Become_One", "one")
    ks_music("Wiosna", "menus")

define sfx_tcard = "sfx/tcard.ogg"
define sfx_4lslogo = "sfx/4lsaudiologo.ogg"
define sfx_alarmclock = "sfx/alarm.ogg"
define sfx_normalbell = "sfx/carillon.ogg"
define sfx_warningbell = "sfx/chaimu.ogg"
define sfx_crunchydeath = "sfx/crunch.ogg"
define sfx_fireworks = "sfx/fireworks.ogg"
define sfx_rain = "sfx/rain.ogg"
define sfx_rustling = "sfx/rustling.ogg"
define sfx_impact = "sfx/wumph.ogg"
define sfx_impact2 = "sfx/wumph_2.ogg"
define sfx_heartfast = "sfx/heart_single_fast.ogg"
define sfx_heartslow = "sfx/heart_single_slow.ogg"
define sfx_heartstop = "sfx/heart_stop.ogg"

define sfx_emijogging = "sfx/emijogging.ogg"
define sfx_emirunning = "sfx/emirunning.ogg"
define sfx_emipacing = "sfx/emipacing.ogg"
define sfx_emisprinting = "sfx/emisprinting.ogg"

define sfx_startpistol = "sfx/startpistol.ogg"
define sfx_crowd_indoors = "sfx/crowd_indoors.ogg"
define sfx_crowd_outdoors = "sfx/crowd_outdoors.ogg"
define sfx_crowd_cheer = "sfx/crowd_cheer.ogg"
define sfx_doorknock = "sfx/doorknock.ogg"
define sfx_doorknock2 = "sfx/doorknock2.ogg"
define sfx_doorslam = "sfx/doorslam.ogg"
define sfx_doorclose = "sfx/doorclose.ogg"

define sfx_cicadas = "sfx/cicadas.ogg"
define sfx_scratch = "sfx/scratch.ogg"
define sfx_traffic = "sfx/traffic.ogg"
define sfx_rumble = "sfx/rumble.ogg"
define sfx_skid = "sfx/skid2.ogg"
define sfx_gymbounce = "sfx/emibounce.ogg"
define sfx_hammer = "sfx/hammer.ogg"
define sfx_birdstakeoff = "sfx/birdstakeoff.ogg"
define sfx_storebell = "sfx/storebell.ogg"
define sfx_thunder = "sfx/thunder.ogg"
define sfx_slide = "sfx/slide.ogg"
define sfx_slide2 = "sfx/slide2.ogg"
define sfx_draw = "sfx/sword_draw.ogg"
define sfx_shower = "sfx/shower.ogg"
define sfx_switch = "sfx/switch.ogg"
define sfx_pillow = "sfx/pillow.ogg"
define sfx_cellphone = "sfx/cellphone.ogg"
define sfx_door_creak = "sfx/door_creak.ogg"
define sfx_dooropen = "sfx/dooropen.ogg"
define sfx_dropglasses = "sfx/dropglasses.ogg"
define sfx_can = "sfx/can.ogg"
define sfx_stallbuilding = "sfx/stallbuilding.ogg"
define sfx_parkambience = "sfx/parkambience.ogg"
define sfx_trainint = "sfx/trainint.ogg"

define sfx_footsteps_hard = "sfx/footsteps_hard.ogg"
define sfx_footsteps_soft = "sfx/footsteps_soft.ogg"
define sfx_paper = "sfx/paper.ogg"
define sfx_paperruffling = "sfx/paperruffling.ogg"
define sfx_rooftop = "sfx/rooftop.ogg"
define sfx_lighter = "sfx/lighter.ogg"
define sfx_phone = "sfx/phone.ogg"
define sfx_hollowclick = "sfx/hollowclick.ogg"
define sfx_businterior = "sfx/businterior.ogg"
define sfx_teacup = "sfx/teacup.ogg"
define sfx_can_clatter = "sfx/can_clatter.ogg"
define sfx_snap = "sfx/snap.ogg"

define sfx_billiards_break = "sfx/billiards_break.ogg"
define sfx_billiards = "sfx/billiards.ogg"
define sfx_lock = "sfx/lock.ogg"
define sfx_dropstuff = "sfx/dropstuff.ogg"
define sfx_camera = "sfx/camera.ogg"

define sfx_time = "sfx/time.ogg"
define sfx_flash = "sfx/flash.ogg"
define sfx_whiteout = "sfx/whiteout.ogg"
