# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

init offset = -10

image bloodred = "#d00"
image white = "#FFF"
image pink = "#FF7FD4"
image darkgrey = "#0D0D0D"
image blind = "#0000007f"
image fw_blank = "#00000000"
image fw_flash = "#FFFFFF66"
image fw_screen = "#000000CC"

init python:
    def night(image):
        return Transform(image, matrixcolor=TintMatrix(Color(rgb=(0.6, 0.6, 0.7))) * SaturationMatrix(0.6))

    def sunset(image):
        return Transform(image, matrixcolor=TintMatrix(Color(rgb=(1.1, 0.95, 0.85))) * SaturationMatrix(1.2) * BrightnessMatrix(0.1))

    def rain(image):
        return Transform(image, matrixcolor=TintMatrix(Color(rgb=(0.95, 0.95, 1.0))) * SaturationMatrix(0.4) * BrightnessMatrix(-0.1))

    def sp_night(image):
        return Transform(image, matrixcolor=TintMatrix(Color(rgb=(0.9, 0.92, 1.0))) * BrightnessMatrix(-0.05))

    def sp_sunset(image):
        return Transform(image, matrixcolor=TintMatrix(Color(rgb=(1.02, 0.95, 0.9))) * SaturationMatrix(1.1) * BrightnessMatrix(0.05))

    def sp_rain(image):
        return Transform(image, matrixcolor=TintMatrix(Color(rgb=(0.96, 0.96, 1.0))) * SaturationMatrix(0.6) * BrightnessMatrix(-0.05))

    def past(image):
        return Transform(image, matrixcolor=TintMatrix(Color(rgb=(1.0, 0.94, 0.76))) * SaturationMatrix(0.15))

    def past_night(image):
        return Transform(image, matrixcolor=TintMatrix(Color(rgb=(0.6, 0.6, 0.7))) * TintMatrix(Color(rgb=(1.0, 0.94, 0.76))) * SaturationMatrix(0.6) * SaturationMatrix(0.15))

    def adult(image, use_null=False, sfw_alt=None):
        if sfw_alt is not None:
            alt = sfw_alt
        elif use_null:
            alt = "null"
        else:
            alt = "black"

        return ConditionSwitch(
            "persistent.hdisabled", alt,
            "True", image)

    def make_sprites(char, nude_if=None):
        prefix = "sprites/" + char + "/"

        for file in filter(lambda el: el.startswith(prefix), renpy.list_files()):
            base_name = file.rsplit("/", 1)[1].replace("_", " ", 1).removesuffix(".png")

            if nude_if and nude_if(base_name):
                renpy.image(base_name, adult(file, use_null=True))
                renpy.image(base_name + "_ss", adult(sp_sunset(file), use_null=True))
                renpy.image(base_name + "_ni", adult(sp_night(file), use_null=True))
                renpy.image(base_name + "_rn", adult(sp_rain(file), use_null=True))
            else:
                renpy.image(base_name, file)
                renpy.image(base_name + "_ss", sp_sunset(file))
                renpy.image(base_name + "_ni", sp_night(file))
                renpy.image(base_name + "_rn", sp_rain(file))

    for file in filter(lambda el: el.startswith("bgs/"), renpy.list_files()):
        base_name = "bg " + file.rsplit("/", 1)[1].removesuffix(".jpg")

        renpy.image(base_name, file)
        renpy.image(base_name + "_ss", sunset(file))
        renpy.image(base_name + "_ni", night(file))
        renpy.image(base_name + "_rn", rain(file))

    make_sprites("akira")
    make_sprites("emi")
    make_sprites("emicas")
    make_sprites("eminude", nude_if=lambda name: True)
    make_sprites("emiwheel")
    make_sprites("hanagown", nude_if=lambda name: "stock" in name)
    make_sprites("hanako")
    make_sprites("hideaki")
    make_sprites("jigoro")
    make_sprites("kenji")
    make_sprites("lilly", nude_if=lambda name: name.endswith("nak"))
    make_sprites("meiko")
    make_sprites("miki")
    make_sprites("misha")
    make_sprites("mishashort")
    make_sprites("muto")
    make_sprites("nomiya")
    make_sprites("nurse")
    make_sprites("rin")
    make_sprites("rinpan")
    make_sprites("sae")
    make_sprites("shizu", nude_if=lambda name: name.endswith("nak"))
    make_sprites("shizuyu")
    make_sprites("shopkeep")
    make_sprites("yuuko")
    make_sprites("yuukoshang")

    class Drugs(renpy.Displayable):
        drugs_wordlist = list(map(_, [
            "Disopyramide",
            "Warfarin",
            "Diltiazem",
            "Felodipine",
            "Propanolol",
            "Penbutolol",
            "Carteolol",
            "Procainamide",
            "Heparin",
            "Phenytoin",
            "Verapamil",
            "Quinidine",
            "Flecainide",
            "5mg/day",
            "400mg/day",
            "15ml/day",
            "100mg/day",
            "10ml/48hrs",
            "10ml/day",
            "200mg/12hrs",
            "50mg/12hrs",
            "500mg/48hrs",
            "125mg/12hrs",
            "25ml/day",
            "nightmares",
            "decreased concentration",
            "bradycardia",
            "clinical depression",
            "insomnia",
            "erectile dysfunction",
            "abnormal vision",
            "heart failure",
            "nausea",
            "dizziness",
            "hallucinations",
            "bronchospasm",
            "dyspnea",
            "fatigue",
            "hypotension",
            "heart block",
            "cold extremities",
            "diarrhea",
            "cardiac arrest",
            "ventricular fibrillation",
            "ataxia",
            "asthma"
        ]))

        def __init__(self, width, height):
            renpy.Displayable.__init__(self)

            self.fadeintime = 1.0
            self.framelength = 0.04

            self.width = width
            self.height = height

            self.progress = 0

            self.wordlist = self.drugs_wordlist * 5
            random.shuffle(self.wordlist)
            self.timeperword = 22.0 / len(self.wordlist)

            self.words = []

            for word in self.wordlist:
                thisword = object()
                thisword.payload = word
                thisword.position = (random.randint(0, self.width), random.randint(0, self.height))
                thisword.size = random.randint(30, 100)
                thisword.alpha = 0
                thisword.render = None
                self.words.append(thisword)

        def render(self, width, height, st, at):
            width = self.width
            height = self.height

            rv = renpy.Render(width, height)
            rv.fill((255, 255, 255, 255))

            self.progress = int(st / self.timeperword)

            for i, word in enumerate(self.words):
                if i > self.progress:
                    break

                if word.alpha < 255:
                    word.alpha = min(((st - i * self.timeperword) / self.fadeintime) * 255, 255)

                    if _preferences.language == "jp":
                        disp = Text(word.payload, size=word.size, color=(0, 0, 0, word.alpha), font="font/NotoSansJP-VariableFont_wght.ttf")
                    else:
                        disp = Text(word.payload, size=word.size, color=(0, 0, 0, word.alpha), font="font/gentium.ttf")

                    render = renpy.render(disp, width, height, st, at)

                    if word.alpha == 255:
                        word.render = render
                else:
                    render = word.render

                size = render.get_size()
                rv.blit(render, (word.position[0] - (size[0] / 2), word.position[1] - (size[1] / 2)))

            renpy.redraw(self, self.framelength)

            return rv

    def roofcomposite(comppath):
        return Composite(
            (1920, 1080),
            (0, 0), "event/rin_roof/rin_roof_boredom.png",
            (720, 300), comppath)

    def rin_trueend_comp(list_in):
        baselist = [(1920, 1080), (0, 0), "event/rin_trueend/rin_trueend_gone.png"]
        for item in list_in:
            baselist.append((0, 0))
            baselist.append("event/rin_trueend/rin_trueend_" + item + ".png")
        return Composite(*baselist)

    def rin_h_comp(im_in, is_close=False):
        closer = ""
        if is_close:
            closer = "_close"
        return Composite(
            (1920, 1080),
            (0, 0), "event/rin_h/rin_h_closed"+closer+".png",
            (0, 0), "event/rin_h/rin_h_"+im_in+closer+".png")

    def traincomposite(comppath):
        return Composite(
            (1920, 1080),
            (0, 0), "event/lilly_train/lilly_trainride_ni_norm.png",
            (0, 0), comppath)

    def silhouette(disp, color=0):
        return Transform(disp, matrixcolor=TintMatrix((color, color, color)))

    def rainAnim(my_offset=0.0, zoom=1.0, alpha=1.0):
        return rainAnim_tf(my_offset, zoom, alpha)

image null = Null()

image adult_warning_bg = Composite((1920, 1080), (0, 0), "gui/bg/main.png")
image main_menu_bg = DynamicDisplayable(main_menu_composer)
image config_bg = Frame("gui/bg/config.png")

image logo_credo = Composite((1920, 1080), (685, 340), "gui/logo/credo.png")
image logo_4ls = Composite((1920, 1080), (781, 432), "gui/logo/4ls-small.png")

image credits_text_good = Text(_("""
{image=gui/icons/flourish_left.png} {b}Writing{/b} {image=gui/icons/flourish_right.png}
Anonymous22
Aura
cpl_crud
Suriko
TheHivemind

{image=gui/icons/flourish_left.png} {b}Editing{/b} {image=gui/icons/flourish_right.png}
Kagami
Losstarot
Silentcook

{image=gui/icons/flourish_left.png} {b}Music{/b} {image=gui/icons/flourish_right.png}
Blue123
NicolArmarfi

{image=gui/icons/flourish_left.png} {b}Art{/b} {image=gui/icons/flourish_right.png}
gebyy-terar
Kamifish
moekki
pimmy
raemz
Raide

{image=gui/icons/flourish_left.png} {b}Additional Art{/b} {image=gui/icons/flourish_right.png}
climatic
Doomfest
yujovi

{image=gui/icons/flourish_left.png} {b}FMV Animation{/b} {image=gui/icons/flourish_right.png}
Mike Inel

{image=gui/icons/flourish_left.png} {b}Directing{/b} {image=gui/icons/flourish_right.png}
delta
Raide
yujovi

{image=gui/icons/flourish_left.png} {b}Engineering{/b} {image=gui/icons/flourish_right.png}
delta

{image=gui/icons/flourish_left.png} {b}Production{/b} {image=gui/icons/flourish_right.png}
cpl_crud
Suriko


{image=gui/icons/flourish_center.png}


{image=gui/icons/flourish_left.png} {b}Thanks{/b} {image=gui/icons/flourish_right.png}
Ambi07
abscess
Anonymous
Celiest
ContinualNaba
Dark_Mercury
DuaneMoody
Fink
frumplstlskn
Ismuth
Japesland
Juno
kekekeke
konflikti
Magaran
Mirage_GSM
OverCoat
Peorth
Petaru
silentkyon
skim
stirfriedweasel
Syureria
TcDohl
tottori
VCR

{image=gui/icons/flourish_left.png} {b}Special Thanks{/b} {image=gui/icons/flourish_right.png}
hir
PyTom
RAITA
replicated

{image=gui/icons/flourish_left.png} {b}Fleeting Heartbeat Studios{/b} {image=gui/icons/flourish_right.png}
Ikariya Biorante
LocalManLLC
Tovarish1
XPND.Dev
Tibix
Niomesan
hdkv
levev

{image=gui/icons/flourish_left.png} {b}Community Contributors{/b} {image=gui/icons/flourish_right.png}
whizvox
CloneWith
BridgetSystems
Dracoctix
LuK1337
ykhima
DrSimp
ZenMaruki
Valdemar «Vavan» Andrade
Nikolai «neparij» Laptev
"""), color="#ffffff", text_align=0.5, size=47, xalign=0.8)

image credits_text = Text(_("""
{image=gui/icons/flourish_left.png} {b}Writing{/b} {image=gui/icons/flourish_right.png}
Anonymous22
Aura
cpl_crud
Suriko
TheHivemind

{image=gui/icons/flourish_left.png} {b}Editing{/b} {image=gui/icons/flourish_right.png}
Kagami
Losstarot
Silentcook

{image=gui/icons/flourish_left.png} {b}Music{/b} {image=gui/icons/flourish_right.png}
Blue123
NicolArmarfi

{image=gui/icons/flourish_left.png} {b}Art{/b} {image=gui/icons/flourish_right.png}
gebyy-terar
Kamifish
moekki
pimmy
raemz
Raide

{image=gui/icons/flourish_left.png} {b}Additional Art{/b} {image=gui/icons/flourish_right.png}
climatic
Doomfest
yujovi

{image=gui/icons/flourish_left.png} {b}FMV Animation{/b} {image=gui/icons/flourish_right.png}
Mike Inel

{image=gui/icons/flourish_left.png} {b}Directing{/b} {image=gui/icons/flourish_right.png}
delta
Raide
yujovi

{image=gui/icons/flourish_left.png} {b}Engineering{/b} {image=gui/icons/flourish_right.png}
delta

{image=gui/icons/flourish_left.png} {b}Production{/b} {image=gui/icons/flourish_right.png}
cpl_crud
Suriko


{image=gui/icons/flourish_center.png}


{image=gui/icons/flourish_left.png} {b}Thanks{/b} {image=gui/icons/flourish_right.png}
Ambi07
abscess
Anonymous
Celiest
ContinualNaba
Dark_Mercury
DuaneMoody
Fink
frumplstlskn
Ismuth
Japesland
Juno
kekekeke
konflikti
Magaran
Mirage_GSM
OverCoat
Peorth
Petaru
silentkyon
skim
stirfriedweasel
Syureria
TcDohl
tottori
VCR

{image=gui/icons/flourish_left.png} {b}Special Thanks{/b} {image=gui/icons/flourish_right.png}
hir
PyTom
RAITA
replicated

{image=gui/icons/flourish_left.png} {b}Fleeting Heartbeat Studios{/b} {image=gui/icons/flourish_right.png}
Ikariya Biorante
LocalManLLC
Tovarish1
XPND.Dev
Tibix
Niomesan
hdkv
levev

{image=gui/icons/flourish_left.png} {b}Community Contributors{/b} {image=gui/icons/flourish_right.png}
whizvox
CloneWith
BridgetSystems
Dracoctix
LuK1337
ykhima
DrSimp
ZenMaruki
Nikolai «neparij» Laptev
"""), color="#ffffff", text_align=0.5, size=47, xalign=0.5)

image emi credits = Movie(play="video/credits_emi.mkv", loop=False)
image hanako credits = Movie(play="video/credits_hanako.mkv", loop=False)
image lilly credits = Movie(play="video/credits_lilly.mkv", loop=False)
image rin credits = Movie(play="video/credits_rin.mkv", loop=False)
image shizune credits = Movie(play="video/credits_shizune.mkv", loop=False)

image credits_final = VBox("logo_credo", "credits_text", "logo_4ls")
image credits_final_good = VBox("logo_credo", "credits_text_good", "logo_4ls")

image button_scribble = "gui/button/scribble.png"
image button_scribble_op:
    "button_scribble"
    matrixcolor OpacityMatrix(0.4)

image button_del = "gui/button/del.png"
image button_del_op:
    "button_del"
    matrixcolor OpacityMatrix(0.4)

image button_return = "gui/button/return.png"
image button_return_op:
    "button_return"
    matrixcolor OpacityMatrix(0.4)

image button_locked_track = "gui/button/locked-track.png"
image button_locked_track_op:
    "button_locked_track"
    matrixcolor OpacityMatrix(0.4)

image button_cg_locked = "gui/button/cg-locked.png"
image button_cg_locked_op:
    "button_cg_locked"
    matrixcolor OpacityMatrix(0.4)
image button_cg_locked_lop:
    "button_cg_locked"
    matrixcolor OpacityMatrix(0.1)

image icon_skip = "gui/icons/skip.png"
image icon_circle = "gui/icons/circle.png"
image icon_ctc:
    "gui/icons/ctc.png"
    xysize (42, 42) anchor (0.5, 0.5) pos (0.925, 0.955)
    block:
        function tf_blinking
        repeat

image icon_emi = "gui/icons/emi.png"
image icon_emi_colored = "gui/icons/emi-c.png"
image icon_rin = "gui/icons/rin.png"
image icon_rin_colored = "gui/icons/rin-c.png"
image icon_hanako = "gui/icons/hanako.png"
image icon_hanako_colored = "gui/icons/hanako-c.png"
image icon_lilly = "gui/icons/lilly.png"
image icon_lilly_colored = "gui/icons/lilly-c.png"
image icon_shizune = "gui/icons/shizune.png"
image icon_shizune_colored = "gui/icons/shizune-c.png"

image logo_large = "gui/logo/large.png"

image gallery_locked = "gui/bg/gallery-locked.png"

image fireworks = Composite(
    (1920, 1080),
    (0, 0), fw_constructor("vfx/fw1.png"),
    (0, 0), fw_constructor("vfx/fw2.png"),
    (0, 0), fw_constructor("vfx/fw3.png"),
    (0, 0), fw_constructor("vfx/fw4.png"),
    (0, 0), fw_constructor("vfx/fw5.png"),
    (0, 0), fw_constructor("vfx/fw6.png"),
    (0, 0), fw_constructor("vfx/fw7.png"),
    (0, 0), fw_constructor("vfx/fw8.png"),
    (0, 0), fw_constructor("vfx/fw9.png"))

image fireshine = Composite(
    (1920, 1080),
    (0, 0), fw_constructor_nosparkle(Solid("#FF000009")),
    (0, 0), fw_constructor_nosparkle(Solid("#00FF0009")),
    (0, 0), fw_constructor_nosparkle(Solid("#0000FF09")),
    (0, 0), fw_constructor_nosparkle(Solid("#CC00CC09")),
    (0, 0), fw_constructor_nosparkle(Solid("#CCCC0009")),
    (0, 0), fw_constructor_nosparkle(Solid("#0000CC09")))

image drugs = Drugs(config.screen_width * 2, config.screen_height)

image completionbonus = Transform("event/completionbonus.png", size=(1920, 1080), fit="contain")

image heartattack = "vfx/heart_attack.png"
image heartattack alpha = Transform("heartattack", alpha=0.3)
image heartattack residual = Transform("heartattack", alpha=0.17)

image emigymbouncecomp = Composite(
    (531, 1134),
    (0, 0), "sprites/emi/emi_basic_grin_gym.png",
    (0, 1080), "vfx/emi_gym_30pxlegs.png")

image emigymclosedbouncecomp = Composite(
    (531, 1134),
    (0, 0), "sprites/emi/emi_basic_closedgrin_gym.png",
    (0, 1080), "vfx/emi_gym_30pxlegs.png")

image emigymconcentratebouncecomp = Composite(
    (531, 1134),
    (0, 0), "sprites/emi/emi_basic_concentrate_gym.png",
    (0, 1080), "vfx/emi_gym_30pxlegs.png")

image emiannoyedbouncecomp = Composite(
    (531, 1188),
    (0, 0), "sprites/emi/emi_basic_annoyed.png",
    (0, 1080), "vfx/emi_uni_60pxlegs.png")

image emihappybouncecomp = Composite(
    (531, 1134),
    (0, 0), "sprites/emi/emi_basic_closedhappy.png",
    (0, 1080), "vfx/emi_uni_60pxlegs.png")

image emi annoyedbounce = At("emiannoyedbouncecomp", fourbounce60)
image emi gymbounce = At("emigymbouncecomp", fourbounce30)
image emi gymconcentratebounce = At("emigymconcentratebouncecomp", fourbounce30)
image emi gymbounceclosed = At("emigymclosedbouncecomp", fourbounce30)
image emi gymbounce_once = At("emigymclosedbouncecomp", onebounce)
image emi happybounce = At("emihappybouncecomp", fourbounce30)

image emi blur = "vfx/emi_blur.png"

image bg school_track_fb = past("bgs/school_track.jpg")
image emi basic_closedhappy_gym_fb = past("sprites/emi/emi_basic_closedhappy_gym.png")
image emi basic_grin_gym_fb = past("sprites/emi/emi_basic_grin_gym.png")
image emi sad_grin_gym_fb = past("sprites/emi/emi_sad_grin_gym.png")
image emi excited_proud_gym_fb = past("sprites/emi/emi_excited_proud_gym.png")

image ev other_iwanako_start:
    "event/other_iwanako_nosnow.png"
    xalign 0.5 yalign 0.9 zoom 1.2
    acdc_warp 20.0 zoom 1.0 yalign 0.5

image ev other_iwanako = "event/other_iwanako_nosnow.png"
image evul other_iwanako = "event/other_iwanako.png"

image ev hisao_class_start = Transform("event/hisao_class.png", crop=(0, 0, 1920, 1080))

image ev hisao_class_move:
    "event/hisao_class.png"
    xalign 0.0
    acdc_warp 40.0 xalign 1.0

image ev hisao_class_end = Transform("event/hisao_class.png", crop=(960, 0, 1920, 1080))

image ev emi_knockeddown = "event/emi_knockeddown.png"

image ev emi_knockeddown_facepullout:
    "event/emi_knockeddown_large.png"
    size (1920, 1080) crop (2016, 90, 1920, 1080)
    easeout 10.0 crop (2016, 90, 2112, 1188)

image ev emi_knockeddown_largepullout:
    "event/emi_knockeddown.png"
    size (1920, 1080) crop (96, 54, 1728, 972)
    easein 10.0 crop (0, 0, 1920, 1080)

image ev emi_knockeddown_face = Transform("event/emi_knockeddown_large.png", crop=(2016, 90, 1920, 1080))

image ev emi_knockeddown_legs:
    size None crop None
    "event/emi_knockeddown_large.png"
    xpos 4700 ypos 2020 xanchor 4800 yanchor 3600
    ease 8.0 xpos 3800 ypos 1800

image ev emi_run_face = "event/emi_run_face.png"

image ev emi_run_face_ss = sunset("event/emi_run_face.png")

image ev emi_firstkiss = "event/emi_firstkiss.png"

image insert startpistol = "vfx/startpistol.png"

image ev emitrack_running = "event/emitrack_running.png"
image ev emitrack_blocks = "event/emitrack_blocks.png"
image ev emitrack_blocks_close = "event/emitrack_blocks_close.png"
image ev emitrack_blocks_close_grin = "event/emitrack_blocks_close_grin.png"
image ev emitrack_finishtop = "event/emitrack_finishtop.png"
image ev emitrack_finish = "event/emitrack_finish.png"

image ev emi_sleepy = "event/emi_sleepy.png"
image ev emi_sleepy_face = "event/emi_sleepy_face.png"
image ev emi_sleepy_legs = "event/emi_sleepy_legs.png"

image ev emi_bed_frown = "event/emi_bed_frown.png"
image ev emi_bed_happy = "event/emi_bed_happy.png"

image ev emi_bed_normal = "event/emi_bed_normal.png"
image ev emi_bed_smile = "event/emi_bed_smile.png"
image ev emi_bed_unsure = "event/emi_bed_unsure.png"

image ev emi_forehead = "event/emi_forehead.png"

image ev emi_sleep_cry = "event/emi_sleep_cry.png"
image ev emi_sleep_normal = "event/emi_sleep_normal.png"
image ev emi_sleep_unsure = "event/emi_sleep_unsure.png"
image ev emi_sleep_weep = "event/emi_sleep_weep.png"

image ev emi_parkback = "event/emi_parkback.png"
image ev emi_parkback_frown = "event/emi_parkback_frown.png"

image ev emi_ending_smile = adult("event/emi_ending_smile.png", sfw_alt="event/sfw/emi_ending_smile.png")
image ev emi_ending_serious = adult("event/emi_ending_serious.png", sfw_alt="event/sfw/emi_ending_serious.png")
image ev emi_ending_glad = adult("event/emi_ending_glad.png", sfw_alt="event/sfw/emi_ending_glad.png")

image ev picnic_normal:
    "event/picnic_normal.png"
    xalign 0.5

image ev picnic_rain:
    "event/picnic_rain.png"
    xalign 0.5

image ev emi_cry_down = "event/emi_cry_down.png"
image evul emi_cry_down:
    "event/emi_cry_down.png"
    zoom 0.8
image ev emi_grave = "event/emi_grave.png"

image evh emi_grinding_victorytall = "event/emi_grinding/emi_grinding_victorytall.png"
image evh emi_grinding_victory = "event/emi_grinding/emi_grinding_victory.png"
image evh emi_grinding_wink = "event/emi_grinding/emi_grinding_wink.png"
image evh emi_grinding_grin = "event/emi_grinding/emi_grinding_grin.png"
image evh emi_grinding_half_undress = adult("event/emi_grinding/emi_grinding_half_undress.png")
image evh emi_grinding_half_grin = adult("event/emi_grinding/emi_grinding_half_grin.png")
image evh emi_grinding_off_yawn = adult("event/emi_grinding/emi_grinding_off_yawn.png")
image evh emi_grinding_off_closesurprise = adult("event/emi_grinding/emi_grinding_off_closesurprise.png")
image evh emi_grinding_off_closearoused = adult("event/emi_grinding/emi_grinding_off_closearoused.png")
image evh emi_grinding_off_aroused = adult("event/emi_grinding/emi_grinding_off_aroused.png")
image evh emi_grinding_off_arousedclosed = adult("event/emi_grinding/emi_grinding_off_arousedclosed.png")
image evh emi_grinding_off_come = adult("event/emi_grinding/emi_grinding_off_come.png")
image evh emi_grinding_off_end = adult("event/emi_grinding/emi_grinding_off_end.png")

image evh emi_shed_base1 = adult("event/emi_shed/emi_shed_base1.png")
image evh emi_shed_base2 = adult("event/emi_shed/emi_shed_base2.png")
image evh emi_shed_base3 = adult("event/emi_shed/emi_shed_base3.png")
image evh emi_shed_base4 = adult("event/emi_shed/emi_shed_base4.png")

image evh_l emi_shed_up = adult("event/emi_shed/emi_shed_lhand_up.png")
image evh_l emi_shed_down = adult("event/emi_shed/emi_shed_lhand_down.png")

image evh_r emi_shed_up = adult("event/emi_shed/emi_shed_rhand_up.png")
image evh_r emi_shed_down = adult("event/emi_shed/emi_shed_rhand_down.png")

image hisao emi_shed_closed = adult("event/emi_shed/emi_shed_hisao_closed.png")
image hisao emi_shed_neutral = adult("event/emi_shed/emi_shed_hisao_neutral.png")
image hisao emi_shed_sweat = adult("event/emi_shed/emi_shed_hisao_sweat.png")

image emi emi_shed_closed = adult("event/emi_shed/emi_shed_emi_closed.png")
image emi emi_shed_grin = adult("event/emi_shed/emi_shed_emi_grin.png")
image emi emi_shed_hesitant = adult("event/emi_shed/emi_shed_emi_hesitant.png")
image emi emi_shed_shock = adult("event/emi_shed/emi_shed_emi_shock.png")

image evh emi_miss_closed = adult("event/emi_miss_closed.png")
image evh emi_miss_open = adult("event/emi_miss_open.png")

image prop rin_cigarette = "vfx/prop_rin_cigarette.png"
image prop rin_cigarette_close = "vfx/prop_rin_cigarette_close.png"

image ev rin_eating = "event/rin_eating.png"

image ev rin_eating_zoomout:
    "event/rin_eating.png"
    size (1920, 1080) crop (332, 0, 1536, 864)
    acdc_warp 10.0 crop (0, 0, 1920, 1080)

image ev rin_artclass1:
    "event/rin_artclass1.png"
    yalign 0.5 xalign 1.0

image ev rin_artclass2:
    "event/rin_artclass2.png"
    yalign 0.5 xalign 1.0

image ev rin_artclass3:
    "event/rin_artclass3.png"
    yalign 0.5 xalign 1.0

image ev rin_artclass4:
    "event/rin_artclass4.png"
    yalign 0.5 xalign 1.0
    0.5
    acdc_warp 10.0 xalign 0.0

image ev rin_wisp1:
    "event/rin_wisp1.png"
    truecenter
image ev rin_wisp2:
    "event/rin_wisp2.png"
    truecenter
image ev rin_wisp3:
    "event/rin_wisp3.png"
    truecenter
image ev rin_wisp4:
    "event/rin_wisp4.png"
    truecenter
image ev rin_wisp5:
    "event/rin_wisp5.png"
    truecenter
image ev rin_wisp_blurred:
    "event/rin_wisp_blurred.png"
    truecenter
image smoke focused = "event/rin_wisp_smoke_focused.png"
image smoke blurred = "event/rin_wisp_smoke_blurred.png"

image ovl rinbyhisao = "vfx/rinbyhisao.png"
image ovl hisaobyrin = "vfx/hisaobyrin.png"

image ev hisao_mirror = "event/hisao_mirror.png"
image ev hisao_mirror_800 = "event/hisao_mirror.png"

image ev busride = "event/busride.png"
image ev busride_ni = "event/busride_ni.png"

image ev rin_roof_boredom = "event/rin_roof/rin_roof_boredom.png"
image ev rin_roof_disgust = roofcomposite("event/rin_roof/rin_roof_disgust.png")
image ev rin_roof_doubt = roofcomposite("event/rin_roof/rin_roof_doubt.png")
image ev rin_roof_nonchalant = roofcomposite("event/rin_roof/rin_roof_nonchalant.png")
image ev rin_roof_surprised = roofcomposite("event/rin_roof/rin_roof_surprised.png")

image hisao rin_roof = "event/rin_roof/hisao_shadow.png"
image emi rin_roof = "event/rin_roof/emi_shadow.png"

image ev hisaobird_0 = "event/hisaobird/bird_0.png"
image ev hisaobird_1 = "event/hisaobird/bird_1.png"
image ev hisaobird_2 = "event/hisaobird/bird_2.png"
image ev hisaobird_3 = "event/hisaobird/bird_3.png"
image ev hisaobird_4 = "event/hisaobird/bird_4.png"
image ev hisaobird_5 = "event/hisaobird/bird_5.png"
image ev hisaobird_6 = "event/hisaobird/bird_6.png"
image ev hisaobird_7 = "event/hisaobird/bird_7.png"
image ev hisaobird_8 = "event/hisaobird/bird_8.png"
image ev hisaobird_9 = "event/hisaobird/bird_9.png"

image ev watch_black = "event/watch_black.png"
image ev watch_worn = "vfx/watch_worn.png"
image ev watch_worn_330 = night("vfx/watch_worn_330.png")
image bg watchhallway_blur = "vfx/watchhallway_blur.jpg"

image bg worrytree = "vfx/worrytree.jpg"
image bg worrytree_ss = sunset("vfx/worrytree.jpg")

image ev rin_painting_base = "event/rin_painting_base.png"
image ev rin_painting_reply = "event/rin_painting_reply.png"
image ev rin_painting_concerned = "event/rin_painting_concerned.png"
image ev rin_painting_foot = "event/rin_painting_foot.png"
image ev rin_painting_faceconcerned = "event/rin_painting_faceconcerned.png"

image ev hisao_letter_closed = "event/hisao_letter_closed.png"
image ev hisao_letter_open = "event/hisao_letter_open.png"
image ev hisao_letter_open_2 = "event/hisao_letter_open_2.png"

image ev rin_rain_away = "event/rin_rain_away.png"
image ev rin_rain_towards = "event/rin_rain_towards.png"
image ev rin_rain_away_close = "event/rin_rain_away_close.png"
image ev rin_rain_towards_close = "event/rin_rain_towards_close.png"

image ovl rin_rain_hisaotowards_close = Transform("event/rin_rain_towards_close.png", crop=(960, 0, 960, 2880))
image ovl rin_rain_hisaotowards = Transform("event/rin_rain_towards.png", crop=(960, 0, 960, 1080))

image rin basic_deadpan_superclose = "sprites/rin/superclose/rin_basic_deadpan_superclose.png"
image rin basic_deadpannormal_superclose = "sprites/rin/superclose/rin_basic_deadpannormal_superclose.png"
image rin basic_lucid_superclose = "sprites/rin/superclose/rin_basic_lucid_superclose.png"
image rin basic_crying_superclose_ss = sunset("sprites/rin/superclose/rin_basic_crying_superclose.png")
image rin relaxed_doubt_superclose = "sprites/rin/superclose/rin_relaxed_doubt_superclose.png"
image rin relaxed_sleepy_superclose = "sprites/rin/superclose/rin_relaxed_sleepy_superclose.png"
image rin relaxed_surprised_superclose = "sprites/rin/superclose/rin_relaxed_surprised_superclose.png"
image rin negative_crying_superclose = "sprites/rin/superclose/rin_negative_crying_superclose.png"
image rin negative_crying_superclose_ss = sunset("sprites/rin/superclose/rin_negative_crying_superclose.png")

image bg gallery_atelier_close = "vfx/gallery_atelier_close.jpg"
image rin back_cas_superclose = "sprites/rin/superclose/rin_back_cas_superclose.png"

image ev rin_kiss = "event/rin_kiss.png"

image ev rin_high_frown = adult("event/rin_high_frown.png", sfw_alt="event/sfw/rin_high_frown.png")
image ev rin_high_grin = adult("event/rin_high_grin.png", sfw_alt="event/sfw/rin_high_grin.png")
image ev rin_high_grinwide = adult("event/rin_high_grinwide.png", sfw_alt="event/sfw/rin_high_grinwide.png")
image ev rin_high_oneeye = adult("event/rin_high_oneeye.png", sfw_alt="event/sfw/rin_high_oneeye.png")
image ev rin_high_open = adult("event/rin_high_open.png", sfw_alt="event/sfw/rin_high_open.png")
image ev rin_high_sleep = "event/rin_high_sleep.png"
image ev rin_high_smile = adult("event/rin_high_smile.png", sfw_alt="event/sfw/rin_high_smile.png")

image ev dandelion = "vfx/dandelion.jpg"

image dandelion full = "vfx/dandelion_full.png"
image dandelion gone = "vfx/dandelion_gone.png"
image dandelionbg = "vfx/dandelionbg.jpg"

image ev rin_nap_close_hand = "event/rin_nap_close_hand.png"
image ev rin_nap_close_nohand = "event/rin_nap_close_nohand.png"
image ev rin_nap_close_tears = "event/rin_nap_close_tears.png"
image ev rin_nap_close_wind = "event/rin_nap_close_wind.png"
image ev rin_nap_close = "event/rin_nap_close.png"
image ev rin_nap_total_tears = "event/rin_nap_total_tears.png"
image ev rin_nap_total_wind = "event/rin_nap_total_wind.png"
image ev rin_nap_total = "event/rin_nap_total.png"

image ev rin_nap_total_awind:
    "ev rin_nap_total"
    block:
        0.2
        "ev rin_nap_total_wind" with Dissolve(0.4)
        0.2
        "ev rin_nap_total" with Dissolve(0.4)
        repeat

image ev rin_nap_close_awind:
    "ev rin_nap_close"
    block:
        0.2
        "ev rin_nap_close_wind" with Dissolve(0.4)
        0.2
        "ev rin_nap_close" with Dissolve(0.4)
        repeat

image ev rin_nap_total_awind_tears = Composite(
    (1920,1080),
    (0, 0), "ev rin_nap_total_awind",
    (0, 0), "ev rin_nap_total_tears")

image ev rin_nap_close_awind_tears = Composite(
    (1920, 1080),
    (0, 0), "ev rin_nap_close_awind",
    (0, 0), "ev rin_nap_close_tears")

image ev rin_masturbate_away = "event/rin_masturbate_away.png"
image ev rin_masturbate_surprise = "event/rin_masturbate_surprise.png"
image ev rin_masturbate_frown = "event/rin_masturbate_frown.png"
image ev rin_masturbate_doubt = "event/rin_masturbate_doubt.png"
image ev rin_masturbate_hug = "event/rin_masturbate_hug.png"

image ovl rin_galleryskylight = "event/rin_galleryskylight.png"

image ev rin_orange = "event/rin_orange.png"
image ev rin_orange_large = "event/rin_orange_large.png"

image evh rin_relief_up = adult("event/rin_relief_up.png")
image evh rin_relief_up_large = adult("event/rin_relief_up_large.png")
image evh rin_relief_down = adult("event/rin_relief_down.png")
image evh rin_relief_down_large = adult("event/rin_relief_down_large.png")

image ev rin_gallery:
    truecenter
    "event/rin_gallery.png"

image doodlewhite = Transform("vfx/rin_doodle.png", matrixcolor=BrightnessMatrix(1))

image ev rin_doodle:
    "doodlewhite"
    xalign 0.0 yalign 0.0
    parallel:
        acdc_warp 20.0 xalign 1.0 yalign 1.0
    parallel:
        1.0
        "vfx/rin_doodle.png" with ImageDissolve("vfx/rin_doodle_tr.png", 19.0, 32)

image ev rin_doodle_all:
    "vfx/rin_doodle.png"
    truecenter
    zoom 0.9
    easein 12.0 zoom 0.75

image bg misc_sky_rays = "bgs/misc_sky_rays.jpg"

image ev rin_trueend_gone = "event/rin_trueend/rin_trueend_gone.png"
image ev rin_trueend_gone_ni = night("event/rin_trueend/rin_trueend_gone.png")
image ev rin_trueend_normal = rin_trueend_comp(["normal"])
image ev rin_trueend_closed = rin_trueend_comp(["normal", "closed"])
image ev rin_trueend_sad = rin_trueend_comp(["normal", "sad"])
image ev rin_trueend_smile = rin_trueend_comp(["normal", "smile"])
image ev rin_trueend_weaksmile = rin_trueend_comp(["normal", "weaksmile"])
image ev rin_trueend_hug = rin_trueend_comp(["hug"])
image ev rin_trueend_hugclosed = rin_trueend_comp(["hug", "hugclosed"])

image ev rin_wet_pan_down = "event/rin_wet/rin_wet_pan_down.png"
image ev rin_wet_arms = "event/rin_wet/rin_wet_arms.png"
image ev rin_wet_face_up = "event/rin_wet/rin_wet_face_up.png"
image ev rin_wet_face_down = "event/rin_wet/rin_wet_face_down.png"
image ev rin_wet_towel_up = "event/rin_wet/rin_wet_towel_up.png"
image ev rin_wet_towel_down = "event/rin_wet/rin_wet_towel_down.png"
image ev rin_wet_towel_touch = "event/rin_wet/rin_wet_towel_touch.png"

image ev rin_pair_base = "event/rin_pair/rin_pair_base.png"
image ev rin_pair_base_clothes = Composite(
    (1920, 1080),
    (0, 0), "event/rin_pair/rin_pair_base.png",
    (0, 0), "event/rin_pair/rin_pair_hisao_clothes.png")

image rp_hisao normal = Solid("#00000000")
image rp_hisao frown = "event/rin_pair/rin_pair_hisao_frown.png"
image rp_hisao smile = "event/rin_pair/rin_pair_hisao_smile.png"
image rp_rin normal = Solid("#00000000")
image rp_rin closed = "event/rin_pair/rin_pair_rin_closed.png"
image rp_rin frown = "event/rin_pair/rin_pair_rin_frown.png"
image rp_rin smile = "event/rin_pair/rin_pair_rin_smile.png"
image rp_rin talk = "event/rin_pair/rin_pair_rin_talk.png"

image evh rin_h2_pan_surprise_base = Composite(
    (1920, 2160),
    (0, 0), "event/rin_h2/rin_h2_u_surprise.png",
    (0, 720), "event/rin_h2/rin_h2_l_pan.png")
image evh rin_h2_pan_surprise = adult("evh rin_h2_pan_surprise_base")

image evh rin_h2_pan_away_base = Composite(
    (1920, 2160),
    (0, 0), "event/rin_h2/rin_h2_u_away.png",
    (0, 720), "event/rin_h2/rin_h2_l_pan.png")
image evh rin_h2_pan_away = adult("evh rin_h2_pan_away_base")

image evh rin_h2_pan_closed_base = Composite(
    (1920, 2160),
    (0, 0), "event/rin_h2/rin_h2_u_closed.png",
    (0, 720), "event/rin_h2/rin_h2_l_pan.png")
image evh rin_h2_pan_closed = adult("evh rin_h2_pan_closed_base")

image evh rin_h2_nopan_closed_base = Composite(
    (1920, 2160),
    (0, 0), "event/rin_h2/rin_h2_u_closed.png",
    (0, 720), "event/rin_h2/rin_h2_l_nopan.png")
image evh rin_h2_nopan_closed = adult("evh rin_h2_nopan_closed_base")

image evh rin_h2_hisao_surprise_base = Composite(
    (1920, 2160),
    (0, 0), "event/rin_h2/rin_h2_u_surprise.png",
    (0, 720), "event/rin_h2/rin_h2_l_hisao.png")
image evh rin_h2_hisao_surprise = adult("evh rin_h2_hisao_surprise_base")

image evh rin_h2_hisao_away_base = Composite(
    (1920, 2160),
    (0, 0), "event/rin_h2/rin_h2_u_away.png",
    (0, 720), "event/rin_h2/rin_h2_l_hisao.png")
image evh rin_h2_hisao_away = adult("evh rin_h2_hisao_away_base")

image evh rin_h2_hisao_closed_base = Composite(
    (1920, 2160),
    (0, 0), "event/rin_h2/rin_h2_u_closed.png",
    (0, 720), "event/rin_h2/rin_h2_l_hisao.png")
image evh rin_h2_hisao_closed = adult("evh rin_h2_hisao_closed_base")

image evh rin_h_closed = adult("event/rin_h/rin_h_closed.png")
image evh rin_h_left = adult(rin_h_comp("left"))
image evh rin_h_normal = adult(rin_h_comp("normal"))
image evh rin_h_right = adult(rin_h_comp("right"))
image evh rin_h_strain = adult(rin_h_comp("strain"))

image evh rin_h_closed_close = adult("event/rin_h/rin_h_closed_close.png")
image evh rin_h_left_close = adult(rin_h_comp("left", True))
image evh rin_h_normal_close = adult(rin_h_comp("normal", True))
image evh rin_h_right_close = adult(rin_h_comp("right", True))
image evh rin_h_strain_close = adult(rin_h_comp("strain", True))

image ev rin_goodend_1 = Composite(
    (1920, 1080),
    (-240, 0), "event/rin_goodend/rin_goodend_base.png",
    (-240, 0), "event/rin_goodend/rin_goodend_1.png")
image ev rin_goodend_1b = Composite(
    (1920, 1080),
    (-240, 0), "event/rin_goodend/rin_goodend_base.png",
    (-240, 0), "event/rin_goodend/rin_goodend_1b.png")
image ev rin_goodend_2 = Composite(
    (1920, 1080),
    (-240, 0), "event/rin_goodend/rin_goodend_base.png",
    (-240, 0), "event/rin_goodend/rin_goodend_2.png")

image evbg rin_goodend_base = "event/rin_goodend/rin_goodend_base.png"
image rin goodend_1 = "event/rin_goodend/rin_goodend_1.png"
image rin goodend_1b = "event/rin_goodend/rin_goodend_1b.png"
image rin goodend_2 = "event/rin_goodend/rin_goodend_2.png"
image rin goodend_2_hires = "event/rin_goodend/rin_goodend_2_hires.png"
image evfg rin_goodend = "event/rin_goodend/rin_goodend_fg.png"

image ev lilly_tearoom = "event/lilly_tearoom.png"
image ev lilly_tearoom_open = "event/lilly_tearoom_open.png"

image ev lilly_crane = "event/lilly_crane.png"

image ev lilly_touch_uni = "event/lilly_touch_uni.png"
image ev lilly_touch_cas = sunset("event/lilly_touch_cas.png")
image ev lilly_touch_cheong = "event/lilly_touch_cheong.png"

image ev braille = "vfx/braille.jpg"
image ev icecream = "vfx/icecream.jpg"

image evfg lilly_sunsetwalk = sunset("event/lilly_sunsetwalk_fg.png")
image evbg lilly_sunsetwalk = "event/lilly_sunsetwalk_bg.png"

image ev lilly_bedroom = "event/lilly_bedroom.png"
image ev lilly_bedroom_large = "event/lilly_bedroom_large.png"

image ev lilly_hanako_hug = "event/lilly_hanako_hug.png"
image unlock_ev lilly_hanako_hug_end:
    "event/lilly_hanako_hug.png"
    xalign 0.5 yalign 1.0
    easein 6.0 yalign 0.0

image ev lilly_kissing = "event/lilly_kissing.png"

image ev lilly_sleeping = "event/lilly_sleeping.png"
image ev lilly_sleeping_smile = "event/lilly_sleeping_smile.png"

image train_scenery:
    "event/lilly_train/train_scenery.png"
    xalign 0.0
    linear 2.0 xalign 1.0
    repeat

image train_scenery_fg:
    "event/lilly_train/train_scenery_fg.png"
    offscreenright
    linear 0.3 offscreenleft
    4.0
    repeat

image evfg lilly_trainride = "event/lilly_train/lilly_trainride.png"
image evfg lilly_trainride_smiles = Composite(
    (1920, 1080),
    (0, 0), "event/lilly_train/lilly_trainride.png",
    (0, 0), "event/lilly_train/lilly_trainride_smile.png",
    (0, 0), "event/lilly_train/lilly_trainride_hanasmile.png")

image ev lilly_trainride = "event/lilly_train/lilly_trainride.png"
image ev lilly_trainride_smiles = "event/lilly_train/lilly_trainride_smiles.png"

image train_scenery_ni:
    "event/lilly_train/train_scenery_ni.png"
    xalign 0.0
    linear 2.0 xalign 1.0
    repeat

image train_scenery_fg_ni:
    "event/lilly_train/train_scenery_fg_ni.png"
    offscreenright
    linear 0.3 offscreenleft
    4.0
    repeat

image lilly_trainride_ni norm = "event/lilly_train/lilly_trainride_ni_norm.png"

image lilly_trainride_ni ara = traincomposite("event/lilly_train/lilly_trainride_ni_ara.png")
image lilly_trainride_ni opensmile = traincomposite("event/lilly_train/lilly_trainride_ni_opensmile.png")
image lilly_trainride_ni pout = traincomposite("event/lilly_train/lilly_trainride_ni_pout.png")
image lilly_trainride_ni smile = traincomposite("event/lilly_train/lilly_trainride_ni_smile.png")
image lilly_trainride_ni weaksmile = traincomposite("event/lilly_train/lilly_trainride_ni_weaksmile.png")

image ev lilly_trainride_ni = "event/lilly_train/lilly_trainride_ni.png"

image ev lilly_wheat_large = "event/lilly_wheat_large.png"
image ovl lilly_wheat_foreground = "event/lilly_wheat_foreground.png"

image unlock_ev lilly_wheat_close = Transform("event/lilly_wheat_large.png", crop=(420, 0, 1920, 1080))
image ev lilly_wheat_small = "event/lilly_wheat_small.png"

image ev lilly_restaurant_listen = "event/lilly_restaurant_listen.png"
image ev lilly_restaurant_sheepish = "event/lilly_restaurant_sheepish.png"

image evul lilly_restaurant_listen:
    "event/lilly_restaurant_listen.png"
    zoom 0.8
image evul lilly_restaurant_sheepish:
    "event/lilly_restaurant_sheepish.png"
    zoom 0.8

image ev lilly_restaurant_wine = "event/lilly_restaurant_wine.png"
image ev lilly_restaurant_eat = "event/lilly_restaurant_eat.png"
image ev lilly_restaurant_chew = "event/lilly_restaurant_chew.png"

image ev hisao_teacup = "event/hisao_teacup.png"
image evul hisao_teacup:
    "event/hisao_teacup.png"
    zoom 0.8

image ev akira_park = "event/akira_park.png"
image evul akira_park:
    "event/akira_park.png"
    zoom 0.8

image ev lilly_sheets = "event/lilly_sheets.png"

image ev lilly_hospitalwindow = "event/lilly_hospitalwindow.png"

image origami_hand = night("vfx/origami_hand.png")

image ev lilly_airport = "event/lilly_airport.png"
image ev lilly_airport_end = "event/lilly_airport_end.png"

image bg school_dormhisao_ni_fb = past("bgs/school_dormhisao_blurred_ni.jpg")
image origami_fb = past_night("vfx/origami_hand.png")
image bg shizu_houseext_lights_fb = past("bgs/shizu_houseext_lights.jpg")
image hideaki serious_up_fb = past_night("sprites/hideaki/hideaki_serious_up.png")
image bg hosp_ext_fb = past_night("bgs/hosp_ext.jpg")
image crowd_still1_fb = past_night("vfx/crowd1.png")
image crowd_still2_fb = past_night("vfx/crowd2.png")
image ev lilly_airport_end_fb = past("event/lilly_airport_end.png")

image unlock_ev lilly_hospital:
    "event/lilly_hospital.png"
    zoom 0.8
image ev lilly_hospital = "event/lilly_hospital.png"
image unlock_ev lilly_hospitalclosed:
    "event/lilly_hospitalclosed.png"
    zoom 0.8
image ev lilly_hospitalclosed = "event/lilly_hospitalclosed.png"

image unlock_ev lilly_goodend:
    "event/lilly_goodend.png"
    zoom 0.8
image ev lilly_goodend = "event/lilly_goodend.png"
image evbg lilly_goodend = "event/lilly_goodend_bg.png"
image evfg lilly_goodend = "event/lilly_goodend_fg.png"

image evhunlock lilly_handjob_chest_frown_small_base:
    "event/lilly_handjob/lilly_hcg_handjob_chest_frown.png"
    zoom 0.667
image evhunlock lilly_handjob_chest_frown_small = adult("evhunlock lilly_handjob_chest_frown_small_base")
image evhunlock lilly_handjob_chest_normal_small_base:
    "event/lilly_handjob/lilly_hcg_handjob_chest_normal.png"
    zoom 0.667
image evhunlock lilly_handjob_chest_normal_small = adult("evhunlock lilly_handjob_chest_normal_small_base")

image evh lilly_handjob_chest_frown = adult("event/lilly_handjob/lilly_hcg_handjob_chest_frown.png")
image evh lilly_handjob_chest_normal = adult("event/lilly_handjob/lilly_hcg_handjob_chest_normal.png")
image evh lilly_handjob_stroke_normopen = adult("event/lilly_handjob/lilly_hcg_handjob_stroke_normopen.png")

image evh lilly_handjob_stroke_flustopen_small = adult("event/lilly_handjob/lilly_hcg_handjob_stroke_flustopen_small.png")
image evh lilly_handjob_stroke_normopen_small = adult("event/lilly_handjob/lilly_hcg_handjob_stroke_normopen_small.png")
image evh lilly_handjob_stroke_normshut_small = adult("event/lilly_handjob/lilly_hcg_handjob_stroke_normshut_small.png")

image evh lilly_cowgirl_cry_small = adult("event/lilly_cowgirl/lilly_hcg_cowgirl_cry_small.png")
image evh lilly_cowgirl_frown_small = adult("event/lilly_cowgirl/lilly_hcg_cowgirl_frown_small.png")
image evh lilly_cowgirl_smile_small = adult("event/lilly_cowgirl/lilly_hcg_cowgirl_smile_small.png")
image evh lilly_cowgirl_strain_small = adult("event/lilly_cowgirl/lilly_hcg_cowgirl_strain_small.png")
image evh lilly_cowgirl_weaksmile_small = adult("event/lilly_cowgirl/lilly_hcg_cowgirl_weaksmile_small.png")

image evh lilly_bath_emb_small = adult("event/lilly_bath/lilly_hcg_bath_emb_small.png")
image evh lilly_bath_grab_small = adult("event/lilly_bath/lilly_hcg_bath_grab_small.png")
image evh lilly_bath_moan_small = adult("event/lilly_bath/lilly_hcg_bath_moan_small.png")
image evh lilly_bath_open_small = adult("event/lilly_bath/lilly_hcg_bath_open_small.png")
image evh lilly_bath_smile_small = adult("event/lilly_bath/lilly_hcg_bath_smile_small.png")

image evh lilly_afterbath_open_small = adult("event/lilly_afterbath/lilly_hcg_afterbath_open_small.png")
image evh lilly_afterbath_shut_small = adult("event/lilly_afterbath/lilly_hcg_afterbath_shut_small.png")

image evh lilly_masturbate = adult("event/lilly_masturbate.png")
image evh lilly_masturbate_come = adult("event/lilly_masturbate_come.png")
image evh lilly_masturbate_come_face = adult("event/lilly_masturbate_come_face.png")

image ev hana_library_read = sunset("event/hana_library_read.png")
image ev hana_library = sunset("event/hana_library.png")
image ev hana_library_gasp = sunset("event/hana_library_gasp.png")
image ev hana_library_smile = sunset("event/hana_library_smile.png")

image ev hana_library_read_std = "event/hana_library_read.png"
image ev hana_library_std = "event/hana_library.png"
image ev hana_library_gasp_std = "event/hana_library_gasp.png"
image ev hana_library_smile_std = "event/hana_library_smile.png"

image ev hanako_presents1 = "event/hanako_presents1.png"
image ev hanako_presents2 = "event/hanako_presents2.png"

image evbg hanako_breakdown = "event/hanako_breakdown/hanako_breakdown_bg.png"
image evfg hanako_breakdown_down = "event/hanako_breakdown/hanako_breakdown_down.png"
image evfg hanako_breakdown_up = Composite(
    (1920, 1080),
    (0, 0),"event/hanako_breakdown/hanako_breakdown_down.png",
    (1411, 141),"event/hanako_breakdown/hanako_breakdown_up.png")
image evfg hanako_breakdown_closed = Composite(
    (1920, 1080),
    (0, 0),"event/hanako_breakdown/hanako_breakdown_down.png",
    (1411, 141),"event/hanako_breakdown/hanako_breakdown_closed.png")

image evul hanako_breakdown_down = Composite(
    (1920, 1080),
    (0, 0), "event/hanako_breakdown/hanako_breakdown_bg.png",
    (0, 0),"event/hanako_breakdown/hanako_breakdown_down.png")
image evul hanako_breakdown_up = Composite(
    (1920, 1080),
    (0, 0), "event/hanako_breakdown/hanako_breakdown_bg.png",
    (0, 0),"event/hanako_breakdown/hanako_breakdown_down.png",
    (1411, 141),"event/hanako_breakdown/hanako_breakdown_up.png")
image evul hanako_breakdown_closed = Composite(
    (1920, 1080),
    (0, 0), "event/hanako_breakdown/hanako_breakdown_bg.png",
    (0, 0),"event/hanako_breakdown/hanako_breakdown_down.png",
    (1411, 141),"event/hanako_breakdown/hanako_breakdown_closed.png")

image ev hanako_crayon1 = "event/hanako_crayon1.png"
image ev hanako_crayon2 = "event/hanako_crayon2.png"

image ev hanako_cry_open = "event/hanako_cry_open.png"
image ev hanako_cry_closed = "event/hanako_cry_closed.png"
image ev hanako_cry_away = "event/hanako_cry_away.png"

image ev hanako_cry_closed_fb = past("event/hanako_cry_closed.png")

image hanako_door_base = "vfx/hanako_door_base.jpg"
image hanako_door_door = "vfx/hanako_door_door.jpg"

image ev hanako_billiards_break = "event/hanako_billiards_break.png"

image ev hanako_billiards_distant:
    "event/hanako_billiards_distant.png"

image ev hanako_billiards_distant_med:
    "event/hanako_billiards_distant.png"
    yanchor 0.0 ypos 0.0 xalign 1.0

image ev hanako_billiards_serious:
    "event/hanako_billiards_serious.png"

image ev hanako_billiards_serious_med:
    "event/hanako_billiards_serious.png"
    yanchor 0.0 ypos 0.0 xalign 1.0

image ev hanako_billiards_smile:
    "event/hanako_billiards_smile.png"

image ev hanako_billiards_smile_med:
    "event/hanako_billiards_smile.png"
    yanchor 0.0 ypos 0.0 xalign 1.0

image ev hanako_billiards_smile_close:
    "event/hanako_billiards_smile_close.png"

image ev hanako_billiards_timid:
    "event/hanako_billiards_timid.png"

image ev hanako_billiards_timid_med:
    "event/hanako_billiards_timid.png"
    yanchor 0.0 ypos 0.0 xalign 1.0

image evul hanako_emptyclassroom = Transform(Composite(
    (1920, 1080),
    (0, 0), "event/hanako_emptyclassroom_bg.png",
    (0, 0), "event/hanako_emptyclassroom_fg.png"), zoom=0.8)

image evbg hanako_emptyclassroom = "event/hanako_emptyclassroom_bg.png"
image evfg hanako_emptyclassroom = "event/hanako_emptyclassroom_fg.png"

image ev hanako_dolls = "event/hanako_dolls.png"

image ev hanako_rage = "event/hanako_rage.png"
image ev hanako_rage_sad = "event/hanako_rage_sad.png"

image ev hanako_eye = "vfx/hanako_eye.jpg"

image ev hisao_scar_large = "event/hisao_scar_large.png"
image ev hisao_scar = "event/hisao_scar.png"

image ev hanako_scars_large = "event/hanako_scars_large.png"
image ev hanako_scars = "event/hanako_scars.png"

image evh hanako_bed_boobs_blush = adult("event/hanako_bed_boobs_blush.png")
image evh hanako_bed_boobs_glance = adult("event/hanako_bed_boobs_glance.png")
image evh hanako_bed_crotch_blush = adult("event/hanako_bed_crotch_blush.png")
image evh hanako_bed_crotch_glance = adult("event/hanako_bed_crotch_glance.png")

image evh hanako_missionary_underwear = adult("event/hanako_missionary_underwear.png")
image evh hanako_missionary_open = adult("event/hanako_missionary_open.png")
image evh hanako_missionary_closed = adult("event/hanako_missionary_closed.png")
image evh hanako_missionary_clench = adult("event/hanako_missionary_clench.png")

image ev hanako_after_worry = "event/hanako_after_worry.png"
image ev hanako_after_smile = "event/hanako_after_smile.png"

image ev hanako_park_alone = "event/hanako_park_alone.png"
image ev hanako_park_away = "event/hanako_park_away.png"
image ev hanako_park_closed = "event/hanako_park_closed.png"
image ev hanako_park_look = "event/hanako_park_look.png"

image ev hanako_goodend_close = "event/hanako_goodend_close.png"
image ev hanako_goodend_muffin = "event/hanako_goodend_muffin.png"
image ev hanako_goodend = "event/hanako_goodend.png"

image unlock_ev hanako_goodend_close:
    "event/hanako_goodend_close.png"
    zoom 0.8
image unlock_ev hanako_goodend_muffin:
    "event/hanako_goodend_muffin.png"
    zoom 0.8
image unlock_ev hanako_goodend:
    "event/hanako_goodend.png"
    xalign 0.5 yalign 0.0
    zoom 0.85

image ev shizu_shanghai = "event/shizu_shanghai.png"
image ev shizu_shanghai_boredlaugh = "event/shizu_shanghai_boredlaugh.png"
image ev shizu_shanghai_borednormal = "event/shizu_shanghai_borednormal.png"
image ev shizu_shanghai_normallaugh = "event/shizu_shanghai_normallaugh.png"
image ev shizu_shanghai_smirklaugh = "event/shizu_shanghai_smirklaugh.png"
image ev shizu_shanghai_smirknormal = "event/shizu_shanghai_smirknormal.png"

image ev shizuconfess_normal = "event/shizu_yukata/shizuconfess_normal.png"
image ev shizuconfess_smile = "event/shizu_yukata/shizuconfess_smile.png"
image ev shizuconfess_closed = "event/shizu_yukata/shizuconfess_closed.png"

image evbg kenji_glasses = "event/kenji_glasses/kenji_glasses_bg.png"
image evmg kenji_glasses_normal = "event/kenji_glasses/kenji_glasses_mg.png"
image evmg kenji_glasses_frown = Composite(
    (2400, 1800),
    (0, 0), "event/kenji_glasses/kenji_glasses_mg.png",
    (960, 456), "event/kenji_glasses/kenji_glasses_frown.png")
image evmg kenji_glasses_closed = Composite(
    (2400, 1800),
    (0, 0), "event/kenji_glasses/kenji_glasses_mg.png",
    (960, 456), "event/kenji_glasses/kenji_glasses_closed.png")
image evfg kenji_glasses = "event/kenji_glasses/kenji_glasses_fg.png"

image evul kenji_glasses_normal = Transform(Composite(
    (2400, 1800),
    (0, 0), "event/kenji_glasses/kenji_glasses_bg.png",
    (0, 0), "event/kenji_glasses/kenji_glasses_mg.png",
    (0, 0), "event/kenji_glasses/kenji_glasses_fg.png"), zoom=0.8, yalign=0.5)
image evul kenji_glasses_frown = Transform(Composite(
    (2400, 1800),
    (0, 0), "event/kenji_glasses/kenji_glasses_bg.png",
    (0, 0), "event/kenji_glasses/kenji_glasses_mg.png",
    (960, 456), "event/kenji_glasses/kenji_glasses_frown.png",
    (0, 0), "event/kenji_glasses/kenji_glasses_fg.png"), zoom=0.8, yalign=0.5)
image evul kenji_glasses_closed = Transform(Composite(
    (2400, 1800),
    (0, 0), "event/kenji_glasses/kenji_glasses_bg.png",
    (0, 0), "event/kenji_glasses/kenji_glasses_mg.png",
    (960, 456), "event/kenji_glasses/kenji_glasses_closed.png",
    (0, 0), "event/kenji_glasses/kenji_glasses_fg.png"), zoom=0.8, yalign=0.5)

image ev shizutanabata = "event/shizu_yukata/shizutanabata.png"

image ev shizu_flashback = "event/shizu_flashback.png"

image ev shizu_hands = "event/shizu_hands.png"

image ev shizune_car:
    "event/shizune_car.png"
    yalign 0.5 xalign 0.0
    easein 12.0 xalign 1.0

image ev shizu_fishing_sl = "event/shizu_fishing_sl.png"
image ev shizu_fishing_ah = "event/shizu_fishing_ah.png"

image ev shizu_couch = "event/shizu_couch.png"

image ev shizu_roof = "event/shizu_roof/shizu_roof.png"
image ev shizu_roof_towardsangry = Composite(
    (1920, 1080),
    (0, 0), "event/shizu_roof/shizu_roof.png",
    (0, 0), "event/shizu_roof/shizu_roof_towardsangry.png")
image ev shizu_roof_towardsnormal = Composite(
    (1920, 1080),
    (0, 0),  "event/shizu_roof/shizu_roof.png",
    (0, 0), "event/shizu_roof/shizu_roof_towardsnormal.png")
image ev shizu_roof_smile = Composite(
    (1920, 1080),
    (0, 0),  "event/shizu_roof/shizu_roof.png",
    (0, 0), "event/shizu_roof/shizu_roof_smile.png")

image ev shizu_roof2 = Composite(
    (1920, 1080),
    (0, 0), "event/shizu_roof/shizu_roof.png",
    (0, 0), "event/shizu_roof/shizu_roof_hisao2.png")
image ev shizu_roof2_towardsangry = Composite(
    (1920, 1080),
    (0, 0), "event/shizu_roof/shizu_roof.png",
    (0, 0), "event/shizu_roof/shizu_roof_hisao2.png",
    (0, 0), "event/shizu_roof/shizu_roof_towardsangry.png")
image ev shizu_roof2_towardsnormal = Composite(
    (1920, 1080),
    (0,0),  "event/shizu_roof/shizu_roof.png",
    (0, 0), "event/shizu_roof/shizu_roof_hisao2.png",
    (0, 0), "event/shizu_roof/shizu_roof_towardsnormal.png")
image ev shizu_roof2_smile = Composite(
    (1920, 1080),
    (0,0), "event/shizu_roof/shizu_roof.png",
    (0, 0), "event/shizu_roof/shizu_roof_hisao2.png",
    (0, 0), "event/shizu_roof/shizu_roof_smile.png")

image evh shizune_hcg_tied_blush_small = adult("event/shizune_hcg_tied/shizune_hcg_tied_blush_small.png")
image evh shizune_hcg_tied_blush = adult("event/shizune_hcg_tied/shizune_hcg_tied_blush.png")
image evh shizune_hcg_tied_close_small = adult("event/shizune_hcg_tied/shizune_hcg_tied_close_small.png")
image evh shizune_hcg_tied_close = adult("event/shizune_hcg_tied/shizune_hcg_tied_close.png")
image evh shizune_hcg_tied_kinky1_small = adult("event/shizune_hcg_tied/shizune_hcg_tied_kinky1_small.png")

image evh shizune_hcg_tied_kinky2_small = adult("event/shizune_hcg_tied/shizune_hcg_tied_kinky2_small.png")
image evh shizune_hcg_tied_kinky2 = adult("event/shizune_hcg_tied/shizune_hcg_tied_kinky2.png")
image evh shizune_hcg_tied_kinky3_small = adult("event/shizune_hcg_tied/shizune_hcg_tied_kinky3_small.png")

image evh shizune_hcg_tied_smile_small = adult("event/shizune_hcg_tied/shizune_hcg_tied_smile_small.png")

image evh shizune_hcg_tied_stare_small = adult("event/shizune_hcg_tied/shizune_hcg_tied_stare_small.png")
image evh shizune_hcg_tied_stare = adult("event/shizune_hcg_tied/shizune_hcg_tied_stare.png")

image evh_hi shizune_hcg_tied_hisao2_base = Composite(
    (3840, 2880),
    (2592, 696), "event/shizune_hcg_tied/shizune_hcg_tied_hisao2.png")
image evh_hi shizune_hcg_tied_hisao2 = adult("evh_hi shizune_hcg_tied_hisao2_base")

image evh_hi shizune_hcg_tied_hisao2_small_base = Composite(
    (1920, 1080),
    (1296, 224), "event/shizune_hcg_tied/shizune_hcg_tied_hisao2_small.png")
image evh_hi shizune_hcg_tied_hisao2_small = adult("evh_hi shizune_hcg_tied_hisao2_small_base")

image evhul shizune_hcg_tied_hisao2_small_base = Composite(
    (1920, 1080),
    (0, 0), "event/shizune_hcg_tied/shizune_hcg_tied_kinky3_small.png",
    (1296, 224),"event/shizune_hcg_tied/shizune_hcg_tied_hisao2_small.png")
image evhul shizune_hcg_tied_hisao2_small = adult("evhul shizune_hcg_tied_hisao2_small_base")

image evh shizu_undressing_clothed_stare = "event/shizu_undressing/shizu_undressing_clothed_stare.png"
image evh shizu_undressing_clothed_kiss = "event/shizu_undressing/shizu_undressing_clothed_kiss.png"
image evh shizu_undressing_clothed_blush = "event/shizu_undressing/shizu_undressing_clothed_blush.png"
image evh shizu_undressing_unclothed_blush = "event/shizu_undressing/shizu_undressing_unclothed_blush.png"
image evh shizu_undressing_unclothed_closed = "event/shizu_undressing/shizu_undressing_unclothed_closed.png"
image evh shizu_undressing_unclothed_kiss = "event/shizu_undressing/shizu_undressing_unclothed_kiss.png"
image evh shizu_undressing_unclothed_talk = "event/shizu_undressing/shizu_undressing_unclothed_talk.png"

image evh shizu_pushdown = adult("event/shizu_pushdown.png")

image evh shizu_straddle_open_base:
    "event/shizu_straddle_open.png"
    xalign 0.7 yalign 1.0
    easein 16.0 xalign 0.0 yalign 0.0
image evh shizu_straddle_open = adult("evh shizu_straddle_open_base")

image evh shizu_straddle_tease = adult("event/shizu_straddle_tease.png")
image evh shizu_straddle_closed = adult("event/shizu_straddle_closed.png")
image evh shizu_straddle_smile = adult("event/shizu_straddle_smile.png")
image evh shizu_straddle_come = adult("event/shizu_straddle_come.png")

image evh shizu_table_smile = adult("event/shizu_table_smile.png")
image evh shizu_table_normal = adult("event/shizu_table_normal.png")
image evh shizu_table_comeopen = adult("event/shizu_table_comeopen.png")
image evh shizu_table_comeclosed = adult("event/shizu_table_comeclosed.png")

image ev misha_sad = "event/misha_sad.png"

image ev misha_nightclass = "event/misha_nightclass.png"
image ovl misha_nightclass_aperture = "vfx/misha_nightclass_aperture.png"

image evh misha_naked = adult("event/misha_naked.png")
image evh misha_sex_aside = adult("event/misha_sex_aside.png")
image evh misha_sex_closed = adult("event/misha_sex_closed.png")

image ev misha_roof_normal:
    "event/misha_roof_normal.png"
    xalign 0.5 yalign 0.0
image ev misha_roof_angry = "event/misha_roof_angry.png"
image ev misha_roof_closed = "event/misha_roof_closed.png"
image ev misha_roof_sad = "event/misha_roof_sad.png"

image aoi_keiko = sunset("vfx/aoi_keiko.png")

image ev shizu_goodend:
    "event/shizu_goodend.png"
    xalign 0.5 yalign 0.85

image ev shizu_goodend_pan:
    "event/shizu_goodend.png"
    xalign 0.5 yalign 0.85
    0.5
    acdc_warp 15.0 yalign 0.0

image ev shizu_badend = "event/shizu_badend.png"

image ev showdown = "event/lilly_shizu_showdown.png"
image ev showdown_large = "event/lilly_shizu_showdown_large.png"
image ev showdown_lilly = Transform("event/lilly_shizu_showdown_large.png", crop=(672, 240, 1920, 1080))
image ev showdown_shizu = Transform("event/lilly_shizu_showdown_large.png", crop=(3360, 384, 1920, 1080))

image showdown_lilly_slice = Transform("event/lilly_shizu_showdown_large.png", crop=(1296, 468, 1920, 538))
image showdown_shizu_slice = Transform("event/lilly_shizu_showdown_large.png", crop=(2784, 576, 1920, 538))

image ev kenji_rooftop = "event/kenji_rooftop.png"
image ev kenji_rooftop_large = "event/kenji_rooftop_large.png"
image ev kenji_rooftop_kenji = Transform("event/kenji_rooftop_large.png", crop=(1058, 677, 1920, 1080))

image bg tearoom_lillyhisao_noon = "event/Lilly_supercg/tearoom_lillyhisao_noon.png"
image bg tearoom_lillyhisao_sunset = "event/Lilly_supercg/tearoom_lillyhisao_sunset.png"

image tearoom_hisao calm = "event/Lilly_supercg/tearoom_hisao_calm.png"
image tearoom_hisao oops = "event/Lilly_supercg/tearoom_hisao_oops.png"
image tearoom_hisao outside = "event/Lilly_supercg/tearoom_hisao_outside.png"
image tearoom_hisao relief = "event/Lilly_supercg/tearoom_hisao_relief.png"
image tearoom_hisao sigh = "event/Lilly_supercg/tearoom_hisao_sigh.png"
image tearoom_hisao smile = "event/Lilly_supercg/tearoom_hisao_smile.png"
image tearoom_hisao think = "event/Lilly_supercg/tearoom_hisao_think.png"
image tearoom_hisao thinkclosed = "event/Lilly_supercg/tearoom_hisao_thinkclosed.png"
image tearoom_hisao unsure = "event/Lilly_supercg/tearoom_hisao_unsure.png"

image tearoom_lilly ara = "event/Lilly_supercg/tearoom_lilly_ara.png"
image tearoom_lilly giggle = "event/Lilly_supercg/tearoom_lilly_giggle.png"
image tearoom_lilly smileclosed = "event/Lilly_supercg/tearoom_lilly_smileclosed.png"
image tearoom_lilly thinking = "event/Lilly_supercg/tearoom_lilly_thinking.png"
image tearoom_lilly weaksmile = "event/Lilly_supercg/tearoom_lilly_weaksmile.png"

image bg tearoom_everyone_noon = "event/Lilly_supercg/tearoom_everyone_noon.png"

image tearoom_hanae happy = "event/Lilly_supercg/tearoom_hanae_happy.png"
image tearoom_hanae open = "event/Lilly_supercg/tearoom_hanae_open.png"
image tearoom_hanae sad = "event/Lilly_supercg/tearoom_hanae_sad.png"
image tearoom_hanae shy = "event/Lilly_supercg/tearoom_hanae_shy.png"

image tearoom_lillye ara = "event/Lilly_supercg/tearoom_lillye_ara.png"
image tearoom_lillye giggle = "event/Lilly_supercg/tearoom_lillye_giggle.png"
image tearoom_lillye smileclosed = "event/Lilly_supercg/tearoom_lillye_smileclosed.png"
image tearoom_lillye thinking = "event/Lilly_supercg/tearoom_lillye_thinking.png"
image tearoom_lillye weaksmile = "event/Lilly_supercg/tearoom_lillye_weaksmile.png"
image tearoom_lillye smile = "event/Lilly_supercg/tearoom_lillye_smile.png"

image tearoom_hisaoe calm = "event/Lilly_supercg/tearoom_hisaoe_calm.png"
image tearoom_hisaoe outside = "event/Lilly_supercg/tearoom_hisaoe_outside.png"
image tearoom_hisaoe sigh = "event/Lilly_supercg/tearoom_hisaoe_sigh.png"
image tearoom_hisaoe thinkclosed = "event/Lilly_supercg/tearoom_hisaoe_thinkclosed.png"
image tearoom_hisaoe hoops = "event/Lilly_supercg/tearoom_hisaoe_hoops.png"
image tearoom_hisaoe hrelief = "event/Lilly_supercg/tearoom_hisaoe_hrelief.png"
image tearoom_hisaoe hsmile = "event/Lilly_supercg/tearoom_hisaoe_hsmile.png"
image tearoom_hisaoe hthink = "event/Lilly_supercg/tearoom_hisaoe_hthink.png"
image tearoom_hisaoe hunsure = "event/Lilly_supercg/tearoom_hisaoe_hunsure.png"
image tearoom_hisaoe loops = "event/Lilly_supercg/tearoom_hisaoe_loops.png"
image tearoom_hisaoe relief = "event/Lilly_supercg/tearoom_hisaoe_relief.png"
image tearoom_hisaoe lsmile = "event/Lilly_supercg/tearoom_hisaoe_lsmile.png"
image tearoom_hisaoe lthink = "event/Lilly_supercg/tearoom_hisaoe_lthink.png"
image tearoom_hisaoe lunsure = "event/Lilly_supercg/tearoom_hisaoe_lunsure.png"

image tearoom_chess = "event/Lilly_supercg/tearoom_chess.png"

image ev shizu_chess_large = "event/shizu_supercg/shizu_chess_large.png"
image ev shizu_chess_base = "event/shizu_supercg/shizu_chess_base.png"
image ev shizu_chess_base2 = "event/shizu_supercg/shizu_chess_base2.png"
image ev shizu_chess_base3 = "event/shizu_supercg/shizu_chess_base3.png"

image sc_shiz normal = Transform("event/shizu_supercg/shizu_chess_base3.png", crop=(960, 0, 960, 1080))

image kenji silhouette = silhouette("sprites/kenji/kenji_neutral.png")
image kenji silhouette_naked = silhouette("sprites/kenji/kenji_neutral_naked.png", 10)
image hanako silhouette = silhouette("sprites/hanako/hanako_basic_bashful.png")
image rin silhouette = silhouette("sprites/rin/rin_relaxed_surprised.png")

image shizuepiccomp = Composite(
    (2098,1555),
    (0, 0), sp_night("sprites/shizu/close/shizu_out_serious_close.png"),
    (3, 1080), sp_night("vfx/shizu_out_serious_legs.png"))

image shizuepiccomp_sil = Composite(
    (2098,1555),
    (0 ,0), silhouette("sprites/shizu/close/shizu_out_serious_close.png"),
    (3, 1080), silhouette("vfx/shizu_out_serious_legs.png"))

transform epictransform:
    xalign 0.5 yalign 0.0
    ease 2.0 zoom 0.1 ypos 1.235

image shizu epictransition:
    "shizuepiccomp"
    pause 0.2
    "shizuepiccomp_sil" with Dissolve(1.8)

image bg school_roof_ni_crop = Transform("bgs/school_roof_ni.jpg", crop=(200, 0, 1920, 1080))
image n_vignette = "vfx/narrowvignette.png"

image hisaowindow = "vfx/hisaowindow.png"

# same as style.say_dialogue.size and style.alive_text.size
image alivetext = renpy.ParameterizedText(xalign=0.5, yalign=0.5, size=42+(mobile_ts_add-6)*(renpy.android or renpy.ios), style="alive_text", drop_shadow=None, color="#666666")
image alivetext_j = renpy.ParameterizedText(xalign=0.5, yalign=0.5, size=42+(mobile_ts_add-6)*(renpy.android or renpy.ios), style="alive_text", drop_shadow=None, color="#666666")

image bg mural_start = "vfx/mural_start.jpg"
image bg mural_unfinished = "vfx/mural_unfinished.jpg"
image bg mural_part = "vfx/mural.jpg"
image mural all = "vfx/mural_wide.jpg"
image bg mural = "vfx/mural.jpg"
image bg mural_ss = sunset("vfx/mural.jpg")

image rin_exhibition_paintings = "vfx/rin_exhibition_paintings.jpg"
image rin_exhibition_sold = "vfx/rin_exhibition_sold.jpg"
image rin_exhibition_c = "vfx/rin_exhibition_c.jpg"

image rin_shadow basic:
    silhouette("sprites/rin/close/rin_basic_deadpan_close.png")
    alpha 0.7

image rin_shadow negative:
    silhouette("sprites/rin/close/rin_negative_spaciness_close.png")
    alpha 0.7

image nightsky rotation:
    "bgs/misc_sky_ni.jpg"
    xalign 0.5 yalign 0.5 rotate 0 zoom 1.5 alpha 0.0
    parallel:
        linear 40 rotate 360
        repeat
    parallel:
        linear 10 zoom 3.0
    parallel:
        linear 5.0 alpha 1.0

image cityscape zoom:
    "vfx/cityscape.png"
    xpos -0.25 ypos 1.0 xanchor 0.0 yanchor 0.0 zoom 1.5
    ease 2.0 xpos 0.0 ypos 1.0 xanchor 0.0 yanchor 1.0 zoom 1.0

image hill enter:
    "vfx/hillouette.png"
    xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.0
    ease 2.0 xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0

image hill pairtouch = "vfx/hillpair1.png"
image hill pairnotouch = "vfx/hillpair2.png"

image nightwash = "vfx/nightwash.png"

image noiseoverlay:
    Tile(Transform("vfx/noise1.png", alpha=0.1))
    pause 0.1
    Tile(Transform("vfx/noise2.png", alpha=0.1))
    pause 0.1
    Tile(Transform("vfx/noise3.png", alpha=0.1))
    pause 0.1
    repeat

image comic vfx1 = "vfx/comic_vfx1.png"
image comic vfx2 = "vfx/comic_vfx2.png"
image comic vfx3 = "vfx/comic_vfx3.png"
image comic vfx4 = "vfx/comic_vfx4.png"

image comic vfx1_ja = "vfx/comic_vfx1_ja.png"
image comic vfx2_ja = "vfx/comic_vfx2_ja.png"
image comic vfx3_ja = "vfx/comic_vfx3_ja.png"
image comic vfx4_ja = "vfx/comic_vfx4_ja.png"

image ev emi_bed_full = Composite(
    (1920, 2967),
    (0, 0), "event/emi_bed_normal_f.png",
    (0, 1335), "event/emi_bed_legs.png")

image passoutOP1:
    Solid("#0000")
    Solid("#000") with ImageDissolve("gui/trans/flashback.png", 6.0, 32)

image wine = "vfx/wine.png"
image musicbox open = "vfx/musicbox_open.png"
image musicbox closed = "vfx/musicbox_closed.png"
image boxstrip = "vfx/boxstrip.png"
image teaset = "vfx/teaset.png"
image stuffedcat = "vfx/stuffedcat.png"
image chessboard = "vfx/chessboard.png"
image shangpai = "vfx/shangpai.png"
image pills = "vfx/pills.png"
image pills_ni = sp_night("vfx/pills.png")
image invite = "vfx/invite.png"
image brailler = "vfx/brailler.png"
image sc_comp = "vfx/sc_comp.png"
image letter_insert = "vfx/letter_insert.png"
image letter_open_insert = "vfx/letter_open_insert.png"
image letter_open_insert_2 = "vfx/letter_open_insert_2.png"

image hanaphone = "vfx/hanaphone.png"
image phonestrap = "vfx/phonestrap.png"
image hanaphonestrap = "vfx/hanaphonestrap.png"

image kenjibox = "vfx/kenjibox.png"

image jigorocard = "vfx/jigorocard.png"

image stallphoto_insert = "vfx/stallphoto_insert.png"

image lilly superclose = "vfx/lilly_superclose.png"
image lilly superclose_ouch = "vfx/lilly_superclose_ouch.png"
image lilly superclose_shock = "vfx/lilly_superclose_shock.png"

image blanknote = "vfx/note_blur.png"

image lillyprop back_cane = "vfx/prop_lilly_back_cane.png"
image lillyprop back_cane_close = "vfx/prop_lilly_back_cane_close.png"
image lillyprop back_cane_ss = sp_sunset("vfx/prop_lilly_back_cane.png")
image lillyprop back_cane_ni = sp_night("vfx/prop_lilly_back_cane.png")

image bg gallery_atelier_bw = Transform("bgs/gallery_atelier.jpg", matrixcolor=SaturationMatrix(0))
image bg school_scienceroom_bw = Transform("bgs/school_scienceroom.jpg", matrixcolor=SaturationMatrix(0))
image bg school_library_bw = Transform("bgs/school_library.jpg", matrixcolor=SaturationMatrix(0))
image bg city_street4_bw = Transform("bgs/city_street4.jpg", matrixcolor=SaturationMatrix(0))
image bg city_street3_bw = Transform("bgs/city_street3.jpg", matrixcolor=SaturationMatrix(0))
image bg school_council_bw = Transform("bgs/school_council.jpg", matrixcolor=SaturationMatrix(0))
image bg school_dormhisao_bw = Transform("bgs/school_dormhisao.jpg", matrixcolor=SaturationMatrix(0))

image hanako_fw = Composite(
    (1920, 1080),
    (0, 0), hanako_fw_constructor(1.0, 1.0, 1.0),
    (0, 0), hanako_fw_constructor(1.1, 0.9, 0.9),
    (0, 0), hanako_fw_constructor(0.9, 1.1, 0.9),
    (0, 0), hanako_fw_constructor(0.9, 0.9, 1.1),
    (0, 0), hanako_fw_constructor(0.9, 1.05, 1.05),
    (0, 0), hanako_fw_constructor(1.05, 0.9, 1.05),
    (0, 0), hanako_fw_constructor(1.05, 1.05, 0.9))

image ev hanako_shanghaiwindow = "event/hanako_fw.png"

image bg school_library_yuuko_blurred = "vfx/school_library_yuuko_blurred.jpg"

image phone mobile = "vfx/mobile-sprite.png"

image rain normal = Composite(
    (1920, 1080),
    (0, 0), rainAnim(),
    (0, 0), rainAnim(my_offset=0.1, zoom=1.2))

image rain light = Composite(
    (1920, 1080),
    (0, 0), rainAnim(alpha=0.3),
    (0, 0), rainAnim(my_offset=0.1, zoom=1.2, alpha=0.3))

image rain medium = Composite(
    (1920, 1080),
    (0, 0), rainAnim(alpha=0.6),
    (0, 0), rainAnim(my_offset=0.1, zoom=1.2, alpha=0.6))

image crowd = crowdgen("vfx/crowd1.png","vfx/crowd2.png","vfx/crowd3.png")
image crowd_ss = crowdgen(sunset("vfx/crowd1.png"), sunset("vfx/crowd2.png"), sunset("vfx/crowd3.png"))
image crowd_ni = crowdgen(night("vfx/crowd1.png"), night("vfx/crowd2.png"), night("vfx/crowd3.png"))
image crowd_fb = crowdgen(past("vfx/crowd1.png"), past("vfx/crowd2.png"), past("vfx/crowd3.png"))
image crowd_ni_fb = crowdgen(past_night("vfx/crowd1.png"), past_night("vfx/crowd2.png"), past_night("vfx/crowd3.png"))

image letterbox = Composite(
    (1920, 1080),
    (0, 0), Solid("#000", ymaximum=75),
    (0, 525), Solid("#000", ymaximum=75))

image snowfg = SnowBlossom("vfx/snowflake.png", start=3.0, count=20, border=50, xspeed=(20, 50), yspeed=(216, 324), fast=True)
image snowbg = SnowBlossom(Transform("vfx/snowflake.png", size=(5, 5)), count=30, yspeed=(144, 216), start=3.0, border=50, xspeed=(20, 50), fast=True)
image snow = Composite(
    (1920, 1080),
    (0, 0), "snowbg",
    (0, 0), "snowfg")

image sakura = SnowBlossom(anim.Filmstrip("vfx/sakura.png", (20, 20), (2, 1), .25), xspeed=(150, 100), yspeed=(135, 270), count=80, fast=True)
image hospitalmask = "vfx/hospitalroommask_new.png"

image dandeliontbg = SnowBlossom(Transform("vfx/dandelion.png", size=(13, 16)), count=20, border=25, xspeed=(50, 100), yspeed=(-54, -18), start=8.0, fast=False, horizontal=True)
image dandeliontfg = SnowBlossom("vfx/dandelion.png", count=10, border=25, xspeed=(100, 200), yspeed=(-72, -27), start=8.0, fast=False, horizontal=True)
image dandelions thin = Composite(
    (1920, 1080),
    (0, 0), "dandeliontbg",
    (0, 0), "dandeliontfg")

image dandelionsbg thin = "dandeliontbg"
image dandelionsfg thin = "dandeliontfg"

image kslogo heart = "gui/logo/large-heartonly.png"
image kslogo words = "gui/logo/large.png"

image credits mask = "gui/bg/roll_mask.png"

image dandeliondbg = SnowBlossom(Transform("vfx/dandelion.png", size=(13, 16)), count=40, border=25, xspeed=(50, 100), yspeed=(-54, -18), start=8.0, fast=True, horizontal=True)
image dandeliondfg = SnowBlossom("vfx/dandelion.png", count=20, border=25, xspeed=(100, 200), yspeed=(-72, -27), start=8.0, fast=True, horizontal=True)
image dandelions dense = Composite(
    (1920, 1080),
    (0, 0), "dandeliondbg",
    (0, 0), "dandeliondfg")

image dandelionsbg dense = "dandeliondbg"
image dandelionsfg dense = "dandeliondfg"

image dandelions_blurbg = SnowBlossom(Transform("vfx/dandelion_blur.png", size=(13, 16)), count=40, border=25, xspeed=(50, 100), yspeed=(-54, -18), start=8.0, fast=True, horizontal=True)
image dandelions_blurfg = SnowBlossom("vfx/dandelion_blur.png", count=20, border=25, xspeed=(100, 200), yspeed=(-72, -27), start=8.0, fast=True, horizontal=True)

image steam:
    "vfx/steam1.png"
    1.5
    "vfx/steam2.png" with Dissolve(0.5)
    1.5
    "vfx/steam3.png" with Dissolve(0.5)
    1.5
    "vfx/steam1.png" with Dissolve(0.5)
    repeat

image steam2:
    "vfx/steam3.png"
    0.75
    "vfx/steam1.png" with Dissolve(0.5)
    1.5
    "vfx/steam2.png" with Dissolve(0.5)
    1.5
    "vfx/steam3.png" with Dissolve(0.5)
    0.75
    repeat

image check_fg_op = contrast_checker("gui/button/check_foreground.png", OpacityMatrix(0.4))
image check_fg = contrast_checker("gui/button/check_foreground.png")

image check_sl_fg_op = contrast_checker("gui/button/check_selected_foreground.png", OpacityMatrix(0.4))
image check_sl_fg = contrast_checker("gui/button/check_selected_foreground.png")

image check_fg_op_cb = VBox(Null(height=6+10*(renpy.android or renpy.ios)), HBox(Null(width=1060+270*(renpy.android or renpy.ios)), "check_fg_op"))
image check_fg_cb = VBox(Null(height=6+10*(renpy.android or renpy.ios)), HBox(Null(width=1060+270*(renpy.android or renpy.ios)), "check_fg"))

image check_sl_fg_op_cb = VBox(Null(height=6+10*(renpy.android or renpy.ios)), HBox(Null(width=1060+270*(renpy.android or renpy.ios)), "check_sl_fg_op"))
image check_sl_fg_cb = VBox(Null(height=6+10*(renpy.android or renpy.ios)), HBox(Null(width=1060+270*(renpy.android or renpy.ios)), "check_sl_fg"))

image return_op = contrast_checker("gui/button/return.png", OpacityMatrix(0.4))
image return_ = contrast_checker("gui/button/return.png")

image music_play_op = contrast_checker("gui/button/music-play.png", OpacityMatrix(0.4))
image music_play = contrast_checker("gui/button/music-play.png")

image language_op = contrast_checker("gui/button/language.png", OpacityMatrix(0.4))
image language = contrast_checker("gui/button/language.png")

image star_op = contrast_checker("gui/icons/star.png", OpacityMatrix(0.4))
image star = contrast_checker("gui/icons/star.png")

image music_stop_op = contrast_checker("gui/button/music-stop.png", OpacityMatrix(0.4))
image music_stop = contrast_checker("gui/button/music-stop.png")
