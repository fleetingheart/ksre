# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

init python:
    def image_fullpath(name):
        return "mods/summersclover/images/" + name

transform show_lowres_fullscreen:
    xysize (1920, 1080)
    fit "contain"

image bg splash = show_lowres_fullscreen(image_fullpath("splash.jpg"))

image act1card = show_lowres_fullscreen(image_fullpath("act1card.png"))
image act1 = show_lowres_fullscreen(image_fullpath("act1.png"))
image neutral = show_lowres_fullscreen(image_fullpath("neutral.png"))
image act2suzu = show_lowres_fullscreen(image_fullpath("act2suzu.png"))
image  act2hisao =show_lowres_fullscreen(image_fullpath("act2hisao.png"))

define passingact = ImageDissolve(Composite((1920, 1080), (650, 300), image_fullpath("ui/tr-tcard-act1.png")), 3.0)
define passingactsuzu = ImageDissolve(show_lowres_fullscreen(image_fullpath("ui/tc-act2suzu.png")), 3.0)
define passingacthisao = ImageDissolve(show_lowres_fullscreen(image_fullpath("ui/tc-act2hisao.png")), 3.0)

   
