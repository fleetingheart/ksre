# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

init python:
    # fades
    fadeslow = Fade(0.7, 0.3, 0.7)

    # positioning stuff
    twoleft = Position(xanchor=0.5, xpos=0.3, yanchor=0.5, ypos=0.5)
    tworight = Position(xanchor=0.5, xpos=0.7, yanchor=0.5, ypos=0.5)

    oneleft = Position(xanchor=0.5, yanchor=0.5, xpos=0.4, ypos=0.5)
    oneright = Position(xanchor=0.5, xpos=0.6, yanchor=0.5, ypos=0.5)

    twoleftsit = Position(xanchor=0.5, yanchor=1.0, xpos=0.3, ypos=1.15)
    tworightsit = Position(xanchor=0.5, yanchor=1.0, xpos=0.7, ypos=1.15)
    leftsit = Position(xanchor=0.5, yanchor=1.0, xpos=0.15, ypos=1.15)
    rightsit = Position(xanchor=0.5, yanchor=1.0, xpos=0.85, ypos=1.15)
    centersit = Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.15)
    centersit2 = Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.07)
    centersitlow = Position(xanchor=0.5, yanchor=1.0, xpos=0.5, ypos=1.25)
    twoleftsitlow = Position(xanchor=0.5, yanchor=1.0, xpos=0.3, ypos=1.25)
    oneleftsitlow = Position(xanchor=0.5, yanchor=1.0, xpos=0.4, ypos=1.25)
    onerightsitlow = Position(xanchor=0.5, yanchor=1.0, xpos=0.6, ypos=1.25)
    tworightsitlow = Position(xanchor=0.5, yanchor=1.0, xpos=0.7, ypos=1.25)

    closeleft = Position(xanchor=0.5, xpos=0.25, yanchor=0.5, ypos=0.5)
    closeright = Position(xanchor=0.5, xpos=0.75, yanchor=0.5, ypos=0.5)
    closeleft2 = Position(xanchor=0.5, xpos=0.20,yanchor=0.5, ypos=0.5)

    rightedge = Position(xanchor=0.5, xpos=0.92, yanchor=0.5, ypos=0.5)
    leftoff = Position(xanchor=0.5, xpos=0.13, yanchor=0.5, ypos=0.5)
    centeroff = Position(xanchor=0.5, xpos=0.52, yanchor=0.5, ypos=0.5)

    twoleftoff = Position(xanchor=0.5, xpos=0.32, yanchor=0.5, ypos=0.5)
    tworightoff = Position(xanchor=0.5, xpos=0.68, yanchor=0.5, ypos=0.5)
    centeroff = Position(xanchor=0.5, xpos=0.52, yanchor=0.5, ypos=0.5)
    twocenteroff = Position(xanchor=0.5, xpos=0.39, yanchor=0.5, ypos=0.5)
    twocenteroff2 = Position(xanchor=0.5, xpos=0.41, yanchor=0.5, ypos=0.5)
    twocenteroff3 = Position(xanchor=0.5, xpos=0.59, yanchor=0.5, ypos=0.5)

    tworightstagger = Position(xanchor=0.5, xpos=0.6, yanchor=0.5, ypos=0.5)

    leftdoor = Position(xanchor=0.5, xpos=0.10, yanchor=0.5, ypos=0.5)
    leftdooropen = Position(xanchor=0.5, xpos=-0.1, yanchor=0.5, ypos=0.5)
    rightwallopen = Position(xanchor=0.5, xpos=0.85, yanchor=0.5, ypos=0.5)
    roomopen = Position(xanchor=0.5, xpos=0.45, yanchor=0.5, ypos=0.5)

    bgleft = Position(xanchor=0.5, xpos=0.4, yanchor=0.5, ypos=0.5)
    bgright = Position(xanchor=0.5, xpos=0.6, yanchor=0.5, ypos=0.5)

    leftoffsit = Position(xanchor=0.5, xpos=0.13, yanchor=1.0, ypos=1.15)
    rightedgesit = Position(xanchor=0.5, xpos=0.92, yanchor=1.0, ypos=1.15)

    oneleftsit = Position(xanchor=0.5, yanchor=1.0, xpos=0.4, ypos=1.15)
    onerightsit = Position(xanchor=0.5, yanchor=1.0, xpos=0.6, ypos=1.15)

    leftsitlow = Position(xanchor=0.5, yanchor=1.0, xpos=0.15, ypos=1.25)
    rightsitlow = Position(xanchor=0.5, yanchor=1.0, xpos=0.85, ypos=1.25)

    rightedgetsu = Position(xanchor=0.5, xpos=0.92, yanchor=0.45, ypos=0.5)
    tworighttsu = Position(xanchor=0.5, xpos=0.7, yanchor=0.45, ypos=0.5)
    leftoffmiyu = Position(xanchor=0.5, xpos=0.01, yanchor=0.17, ypos=0.5)

    # animations
    define.move_transitions("charamove", 1.0, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp)
    define.move_transitions("charamovefast", 0.5, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp)
    define.move_transitions('charamoveslow', 2.0, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp)
    def Dissolvemove(time, time_warp=_ease_time_warp):
        top = Dissolve(time)
        before = MoveTransition(time, factory=MoveFactory(time_warp=time_warp), old=True)
        after = MoveTransition(time, factory=MoveFactory(time_warp=time_warp))
        return ComposeTransition(top, before=before, after=after)

    dissolvecharamoveslowish = Dissolvemove(2.0)
    dissolvecharamove = Dissolvemove(1.0)
    dissolvecharamoveslow = Dissolvemove(3.0)
    dissolvecharamovefast = Dissolvemove(0.75)
    dissolvecharamovereallyfast = Dissolvemove(0.15)

    charachange = dissolve

    # music
    def audio_fullpath(name):
        return "mods/summersclover/audio/" + name

    def sc_music(filename, alias):
        fullpath = audio_fullpath("ost/" + filename + ".ogg")
        setattr(store, "music_" + alias, fullpath)
        store._tracks[fullpath] = filename.replace("_", " ")

    sc_music("Autumn", "suzu")
    sc_music("Carefree_Days", "miki")
    sc_music("Hit_Me_With_Your_Best_Shot", "best_shot")
    sc_music("Summer_Nights", "grease")

    # images
    def image_fullpath(name):
        return "mods/summersclover/images/" + name

define har = Character(_("Haru"),       who_color="#f9eaa0")
define suz = Character(_("Suzu"),       who_color="#72adee")
define yuk = Character(_("Yukio"),      who_color="#897cbf")
define jun = Character(_("Dad"),        who_color="#eb243b")
define mot = Character(_("Mrs Suzuki"), who_color="#ddddd3")
define dad = Character(_("Mr Suzuki"),  who_color="#f1f1f1") 
define tsu = Character(_("Tsubasa"),    who_color="#e94e77")
define yam = Character(_("Yamada"),     who_color="#ff8d7c") 
