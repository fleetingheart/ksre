# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

init offset = -50

init python:
    def Dissolvemove(time, time_warp=_ease_time_warp):
        return ComposeTransition(
            Dissolve(time),
            before=MoveTransition(time, time_warp=time_warp, old=True),
            after=MoveTransition(time, time_warp=time_warp))

    class SoundTransition(renpy.display.transition.Transition):
        def __init__(self, sound, old_widget=None, new_widget=None, **properties):
            super(SoundTransition, self).__init__(0, **properties)

            self.sound = sound
            self.old_widget = old_widget
            self.new_widget = new_widget

        def render(self, width, height, st, at):
            renpy.sound.play(self.sound)
            return renpy.display.transition.null_render(self, width, height, st, at)

    def GenericWhiteout(rise, hold, fall):
        return MultipleTransition([
            False, partial(SoundTransition, "sfx/whiteout.ogg"),
            False, Fade(rise, hold, fall, color="#FFF"),
            True ])

    def scaled_runtime(length, expired):
        return min((float(expired) / float(length)), 1.0)

    def tremble_general(time, xpos, ypos, xanchor, yanchor, d, st, at):
        if not time:
            n = st - int(st)
        else:
            n = scaled_runtime(time, st)
        
        jitter = 0.0002 * random.randint(-1, 1)
        m = math.sin(n * math.pi * 40) * 0.001 + jitter
        d.xanchor = xanchor
        d.yanchor = yanchor
        d.xpos = xpos + m
        d.ypos = ypos + jitter

        return 0

    tf_centertremble = partial(tremble_general, False, 0.5, 1.0, 0.5, 1.0)

    def bounce_general(time, amplitude, num, d, st, at):
        n = scaled_runtime(time, st)
        m = math.fabs(math.sin(n * math.pi * num))

        max = amplitude * 1000
        d.yoffset = max - (m * max)

        return 0

    tf_fourbounce60 = partial(bounce_general, 2.1, 0.1, 4)

    tf_fourbounce30 = partial(bounce_general, 1.8, 0.04, 4)

    tf_onebounce = partial(bounce_general, 0.5, 0.04, 1)

    def l_hosp_out_f(trans, st, at):
        trans.yalign = 0.5
        trans.xalign = 0.5

        n = scaled_runtime(30.0, at)

        trans.zoom = (-acdc_warp(n) + 1.0) * 0.2 + 1.0

        return 0

    def restaurant_out_f(trans, st, at):
        trans.yalign = 0.5
        trans.xalign = 0.5

        n = scaled_runtime(20.0, at)

        trans.zoom = (-acdc_warp(n) + 1.0) * 0.266 + 1.0

        return 0

    def tf_train_shake(trans, st, at):
        trans.yalign = (math.sin(at / 2.0 % 2.0 * math.pi) + 1.0) / 2
        return 0

    def tf_leftrock(d, st, at):
        n = scaled_runtime(4.0, st)
        m = math.sin(n * math.pi * 8) * (1 - n)

        d.xpos = 0.3 + m * 0.05
        d.ypos = 1.0

        d.xanchor = 0.5
        d.yanchor = 0.9

        return 0

    def tf_slow_out(trans, st, at):
        trans.yalign = 0.5
        trans.xalign = 0.5

        n = scaled_runtime(60.0, at)

        trans.zoom = (-acdc_warp(n) + 1.0) * 0.2 + 0.8

        return 0

    def tf_slide_left(trans, st, at):
        trans.xalign = _ease_in_time_warp(scaled_runtime(6.0, at))

        return 0

    def generic_rotateloop(length, dir, has_zoom, trans, st, at):
        trans.yalign = 0.5
        trans.xalign = 0.5

        n = 0.0

        if has_zoom:
            n = scaled_runtime(60.0, at)

        trans.zoom = 0.834 + ((-acdc_warp(n) + 1.0) * 0.266)
        trans.rotate = 360 / (length / (at + 0.1)) * dir

        return 0

    def tf_wispturn(trans, st, at):
        return generic_rotateloop(180, 1, True, trans, st, at)

    def tf_smoketurn(trans, st, at):
        return generic_rotateloop(180, -1, False, trans, st, at)

    def tf_kenji_mg_out(trans, st, at):
        trans.xalign = 0.5
        trans.yalign = 0.5
        n = scaled_runtime(20.0, at)
        trans.zoom = 0.95 - (acdc_warp(n) * 0.15)
        return 0

    def tf_shizu_roof_in(trans, st, at):
        trans.xalign = 0.5
        trans.yalign = 1.0
        n = scaled_runtime(60.0, at)
        trans.zoom = 1.0 + (acdc_warp(n) * 0.2)
        return 0

    def tf_parallax(tf, st, tb):
        if persistent.parallax:
            _x, _y = renpy.get_mouse_pos()
            tf.zoom = 1.01
            tf.align = (float(_x) / config.screen_width, float(_y) / config.screen_height)
        else:
            tf.zoom = 1.0
        return 0

    def tf_blinking(tf, st, at):
        if persistent.blinking_arrow:
            if st >= 2.5:
                tf.alpha = 1
                return None
            elif st >= 1.5:
                tf.alpha = 0.25 + acdc_warp(st - 1.5) * 0.75
            elif st >= 1.25:
                tf.alpha = 0.25
                return 0.25
            elif st >= 0.25:
                tf.alpha = 1 - acdc_warp(st - 0.25) * 0.75
            else:
                tf.alpha = 1
                return 0.25
            return 0
        else:
            tf.alpha = 1
            return 1

    define.move_transitions("charamove", 1.0, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp)

    # HACK: Enable subpixel tranform property by default
    #       https://www.renpy.org/doc/html/atl.html#transform-property-subpixel
    setattr(renpy.display.transform.TransformState, "subpixel", True)

transform twoleft:
    xpos 0.3 xanchor 0.5 ypos 1.0 yanchor 1.0 alpha 1.0

transform tworight:
    xpos 0.7 xanchor 0.5 ypos 1.0 yanchor 1.0 alpha 1.0

transform closeleft:
    xpos 0.25 xanchor 0.5 ypos 1.0 yanchor 1.0 alpha 1.0

transform closeright:
    xpos 0.75 xanchor 0.5 ypos 1.0 yanchor 1.0 alpha 1.0

transform bgleft:
    xpos 0.45 xanchor 0.5 ypos 1.0 yanchor 1.0

transform bgright:
    xpos 0.55 xanchor 0.5 ypos 1.0 yanchor 1.0

transform fw_constructor(my_image):
    "fw_blank"
    choice 15:
        0.2
    choice:
        "fw_flash" with fw_dis_fast
        0.2
        choice:
            my_image with fw_dis_medium
            "fw_blank" with fw_dis_slow
            6.0
        choice:
            my_image with fw_dis_medium
            "fw_blank" with fw_sparkle_out
            6.0
    repeat

transform fw_constructor_nosparkle(my_image):
    "fw_blank"
    choice 15:
        0.2
    choice:
        "fw_flash" with fw_dis_fast
        0.2
        my_image with fw_dis_medium
        "fw_blank" with fw_dis_slow
        6.0
    repeat

transform centertremble:
    function tf_centertremble

transform fourbounce60:
    function tf_fourbounce60

transform fourbounce30:
    function tf_fourbounce30

transform onebounce:
    function tf_onebounce

transform l_hosp_out:
    function l_hosp_out_f

transform restaurant_out:
    function restaurant_out_f

transform train_shake:
    function tf_train_shake
    repeat

transform leftrock:
    function tf_leftrock

transform slow_out:
    function tf_slow_out
    repeat

transform slide_left:
    function tf_slide_left

transform wispturn:
    function tf_wispturn
    repeat

transform smoketurn:
    function tf_smoketurn
    repeat

transform kenji_mg_out:
    function tf_kenji_mg_out

transform shizu_roof_in:
    function tf_shizu_roof_in

transform hanako_fw_constructor(in_r, in_g, in_b):
    alpha 0.0
    "fw_blank"
    choice 15:
        0.2
    choice:
        parallel:
            linear 0.04 alpha 1.0
            linear 3.0 alpha 0.0
        parallel:
            "fw_flash" with fw_dis_fast
            0.05
            Transform("event/hanako_fw_flash.png", matrixcolor=TintMatrix((in_r, in_g, in_b))) with fw_dis_medium
            8.0
    repeat

transform rainAnim_tf(my_offset, my_zoom, my_alpha):
    xalign 0.5 yalign 1.0 zoom my_zoom alpha my_alpha
    "fw_blank"
    my_offset
    block:
        choice:
            "vfx/fx-rain-bg1.png" with rain_trans
            0.2
        choice:
            "vfx/fx-rain-bg2.png" with rain_trans
            0.2
        choice:
            "vfx/fx-rain-bg3.png" with rain_trans
            0.2
        choice:
            "vfx/fx-rain-bg4.png" with rain_trans
            0.2
        choice:
            "vfx/fx-rain-bg5.png" with rain_trans
            0.2
        choice:
            "vfx/fx-rain-bg6.png" with rain_trans
            0.2
        repeat

transform crowdgen(img1, img2, img3):
    img1
    block:
        1.0
        img2 with crowdtrans
        1.0
        img3 with crowdtrans
        1.0
        img1 with crowdtrans
        repeat

transform offscreenbottom:
    xalign 0.5 ypos 1.0

transform note_tf:
    xalign 0.5 yalign 1.0 alpha 0.0
    easein 0.5 yalign 0.5 alpha 1.0

    on hide:
        easeout 0.5 yalign 1.0 alpha 0.0

transform defaultColorblind:
    matrixcolor Matrix(persistent.colorblind or [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1])

# this is an ugly "hack" to get renpy to actuall refresh the filter real-time. The matrix parameter should always be `persistent.colorblind`
transform colorblind(matrix):
    matrixcolor Matrix(matrix or [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1])

transform rotateBy(rotation=0):
    delay 0.15
    ease(0.15) rotate rotation

define dotwipe_down = ImageDissolve(Tile("gui/trans/dots_col.png"), 0.5, 32, ramptype="mcube")
define dotwipe_up = ImageDissolve(Tile("gui/trans/dots_col.png"), 0.5, 32, ramptype="mcube", reverse=True)

define openeye = ImageDissolve("gui/trans/eyes.png", 2.0, 64, ramptype="cube")
define shuteye = ImageDissolve("gui/trans/eyes.png", 2.0, 64, ramptype="mcube", reverse=True)

define openeyefast = ImageDissolve("gui/trans/eyes.png", 0.5, 64, ramptype="cube")
define shuteyefast = ImageDissolve("gui/trans/eyes.png", 0.2, 64, ramptype="mcube", reverse=True)

define openeye_shock = ImageDissolve("gui/trans/openshock.png", 0.8, 64, ramptype="cube")

define whip_right = ImageDissolve(Tile("gui/trans/softwipe.png"), 0.3, 256, ramptype="mcube")
define whip_left = ImageDissolve(Tile("gui/trans/softwipe.png"), 0.3, 256, ramptype="mcube", reverse=True)

define flashback = ImageDissolve(Tile("gui/trans/flashback.png"), 2.0, 32)
define clockwipe = ImageDissolve(Tile("gui/trans/clockwipe.png"), 2.0, 8)

define delayblinds = ImageDissolve("gui/trans/delayblinds.png", 1.0)

define fw_dis_fast = Dissolve(0.04)
define fw_dis_medium = Dissolve(0.2)
define fw_dis_slow = Dissolve(3.0)
define fw_sparkle_out = ImageDissolve(Tile("gui/trans/pronoise.png"), 3.0, 32)

define letter_in = ImageDissolve(Tile("gui/trans/letter.png"), 1.0, 8, reverse=True)
define letter_out = ImageDissolve(Tile("gui/trans/letter.png"), 1.0, 8)

define hands_in = ImageDissolve("gui/trans/handsdissolve.png", 0.2, ramplen=256, reverse=True)
define hands_out = ImageDissolve("gui/trans/handsdissolve.png", 0.2, ramplen=256)

define softwipedown = ImageDissolve(Tile("gui/trans/wipeh.png"), 1.5, 16)
define softwipeup = ImageDissolve(Tile("gui/trans/wipeh.png"), 1.5, 16, reverse=True)

define silentflash = Fade(0.25, 0, 0.75, color="#FFF")
define flash = MultipleTransition([
    False, partial(SoundTransition, "sfx/flash.ogg"),
    False, silentflash,
    True ])

define silentwhiteout = Fade(1.0, 0.0, 1.0, color="#FFF")
define whiteout = GenericWhiteout(1.0, 0.0, 1.0)

define cameraflash = Fade(0.05, 0.1, 0.75, color="#FFF")
define cameraflashlong = Fade(0.05, 0.1, 4.0, color="#FFF")

define rain_trans = Dissolve(0.1)

define crowdtrans = Dissolve(0.3)

define delayed_dissolve = MultipleTransition([
    False, Dissolve(0.5),
    False, Dissolve(0.5),
    True ])

define delayblindsfade = MultipleTransition([
    False, partial(SoundTransition, "sfx/time.ogg"),
    False, delayblinds, Solid("#000"), delayblinds,
    True ])

define delayblindsfadesilent = MultipleTransition([
    False, delayblinds, Solid("#000"), delayblinds,
    True ])

define menueffect = dissolve

define charaenter = dissolve
define charaexit = dissolve

define characlose = dissolve
define charadistant = dissolve

define charachangealways = dissolve
define charachangeev = dissolve
define charachange = None # charachangealways (must be customizable)
define charachangefast = None # Dissolve(0.2) (must be customizable)

define charamovechange = Dissolvemove(2.0)

define charamovefast = MoveTransition(1.5,
    time_warp=_ease_time_warp,
    enter_time_warp=_ease_in_time_warp,
    leave_time_warp=_ease_out_time_warp)

define charamovefaster = MoveTransition(1.0,
    time_warp=_ease_time_warp,
    enter_time_warp=_ease_in_time_warp,
    leave_time_warp=_ease_out_time_warp)

define charamovechangefaster = Dissolvemove(1.0)

define charamovefastest = MoveTransition(0.5,
    time_warp=_ease_time_warp,
    enter_time_warp=_ease_in_time_warp,
    leave_time_warp=_ease_out_time_warp)

define charamovechangefastest = Dissolvemove(0.5)

define charamovecustom = partial(MoveTransition,
    time_warp=_ease_time_warp,
    enter_time_warp=_ease_in_time_warp,
    leave_time_warp=_ease_out_time_warp)

define locationchange = dissolve
define locationskip = Fade(0.5, 0, 0.5)

define shorttimeskip = delayblindsfade
define shorttimeskipsilent = delayblindsfadesilent

define trans_dandelion = CropMove(5.0, "wipeleft")

define easeout = MoveTransition(0.5, time_warp=_ease_out_time_warp)
define easein = MoveTransition(0.5, time_warp=_ease_in_time_warp)

define charamove_accel = MoveTransition(1.0, time_warp=_ease_out_time_warp)
define charamove_decel = MoveTransition(1.0, time_warp=_ease_in_time_warp)
