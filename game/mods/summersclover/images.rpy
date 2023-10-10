# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

init python:
    def image_fullpath(name):
        return "mods/summersclover/images/" + name

transform show_lowres_fullscreen:
    xysize (1920, 1080)
    fit "contain"

image bg splash = show_lowres_fullscreen(image_fullpath("ui/splash.jpg"))

image act1card = show_lowres_fullscreen(image_fullpath("ui/act1card.png"))
image act1 = show_lowres_fullscreen(image_fullpath("ui/act1.png"))
image neutral = show_lowres_fullscreen(image_fullpath("ui/neutral.png"))
image act2suzu = show_lowres_fullscreen(image_fullpath("ui/act2suzu.png"))
image act2hisao =show_lowres_fullscreen(image_fullpath("ui/act2hisao.png"))

define passingact = ImageDissolve(Composite((1920, 1080), (650, 300), image_fullpath("ui/tr-tcard-act1.png")), 3.0)
define passingactsuzu = ImageDissolve(show_lowres_fullscreen(image_fullpath("ui/tc-act2suzu.png")), 3.0)
define passingacthisao = ImageDissolve(show_lowres_fullscreen(image_fullpath("ui/tc-act2hisao.png")), 3.0)

image kslogowords = image_fullpath("ui/kslogowords.png")
image kslogoheart = image_fullpath("ui/kslogoheart.png")
image solid_black = Solid("#000000")
define passingoftime = ImageDissolve(Composite((1920, 1080), (0, 0), image_fullpath("ui/tr-clockwipe.png")), 2.0)

image hisao_blank = show_lowres_fullscreen(image_fullpath("sprites/hisao_blank.png"))
image hisao_erm = show_lowres_fullscreen(image_fullpath("sprites/hisao_erm.png"))
image hisao_erm_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_erm_uniform.png"))
image hisao_talk_big = show_lowres_fullscreen(image_fullpath("sprites/hisao_talk_big.png"))
image hisao_talk_big_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_talk_big_uniform.png"))
image hisao_smile = show_lowres_fullscreen(image_fullpath("sprites/hisao_smile.png"))
image hisao_smile_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_smile_uniform.png"))
image hisao_wtf = show_lowres_fullscreen(image_fullpath("sprites/hisao_wtf.png"))
image hisao_wtf_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_wtf_uniform.png"))
image hisao_biggrin = show_lowres_fullscreen(image_fullpath("sprites/hisao_biggrin.png"))
image hisao_biggrin_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_biggrin_uniform.png"))
image hisao_disappoint = show_lowres_fullscreen(image_fullpath("sprites/hisao_disappoint.png"))
image hisao_disappoint_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_disappoint_uniform.png"))
image hisao_frown = show_lowres_fullscreen(image_fullpath("sprites/hisao_frown.png"))
image hisao_frown_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_frown_uniform.png"))
image hisao_heh = show_lowres_fullscreen(image_fullpath("sprites/hisao_heh.png"))
image hisao_heh_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_heh_uniform.png"))
image hisao_smile_teeth = show_lowres_fullscreen(image_fullpath("sprites/hisao_smile_teeth.png"))
image hisao_smile_teeth_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_smile_teeth_uniform.png"))
image hisao_talk_small = show_lowres_fullscreen(image_fullpath("sprites/hisao_talk_small.png"))
image hisao_talk_small_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_talk_small_uniform.png"))
image hisao_hmpf = show_lowres_fullscreen(image_fullpath("sprites/hisao_hmpf.png"))
image hisao_hmpf_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_hmpf_uniform.png"))
image hisao_closed = show_lowres_fullscreen(image_fullpath("sprites/hisao_closed.png"))
image hisao_closed_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_closed_uniform.png"))
image hisao_declare = show_lowres_fullscreen(image_fullpath("sprites/hisao_declare.png"))
image hisao_declare_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_declare_uniform.png"))
image hisao_blush = show_lowres_fullscreen(image_fullpath("sprites/hisao_blush.png"))
image hisao_blush_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_blush_uniform.png"))
image hisao_beach_blush = show_lowres_fullscreen(image_fullpath("sprites/hisao_beach_blush.png"))
image hisao_beach_frown = show_lowres_fullscreen(image_fullpath("sprites/hisao_beach_frown.png"))
image hisao_beach_smile = show_lowres_fullscreen(image_fullpath("sprites/hisao_beach_smile.png"))
image hisao_beach_erm = show_lowres_fullscreen(image_fullpath("sprites/hisao_beach_erm.png"))
image hisao_beach_disappoint = show_lowres_fullscreen(image_fullpath("sprites/hisao_beach_disappoint.png"))
image hisao_beach_talk = show_lowres_fullscreen(image_fullpath("sprites/hisao_beach_talk.png"))
image hisao_beach_grin = show_lowres_fullscreen(image_fullpath("sprites/hisao_beach_grin.png"))
image hisao_beach_declare = show_lowres_fullscreen(image_fullpath("sprites/hisao_beach_declare.png"))
image hisao_topless = show_lowres_fullscreen(image_fullpath("sprites/hisao_topless.png"))
image hisao_pale = show_lowres_fullscreen(image_fullpath("sprites/hisao_pale.png"))
image hisao_wtf_close = show_lowres_fullscreen(image_fullpath("sprites/hisao_wtf_close.png"))
image hisao_wtf_close_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_wtf_close_uniform.png"))
image hisao_erm_close = show_lowres_fullscreen(image_fullpath("sprites/hisao_erm_close.png"))
image hisao_erm_close_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_erm_close_uniform.png"))
image hisao_smile_close = show_lowres_fullscreen(image_fullpath("sprites/hisao_smile_close.png"))
image hisao_smile_close_u = show_lowres_fullscreen(image_fullpath("sprites/hisao_smile_close_uniform.png"))
image hisao_topless_smile = show_lowres_fullscreen(image_fullpath("sprites/hisao_topless_smile.png"))
