define config.steam_appid = "3068300"

init -9999 python:
    
    achdata = {
        "prologue_achieve",
        "emigood_achieve",
        "emibad_achieve",
        "lillygood_achieve",
        "lillyneutral_achieve",
        "hanakogood_achieve",
        "hanakobad_achieve",
        "hanakoneutral_achieve",
        "ringood_achieve",
        "rinbad_achieve",
        "rinneutral_achieve",
        "shizunegood_achieve",
        "shizunebad_achieve",
        "kenji_achieve",
        "fullcomplete_achieve",
        "act1emi_achieve",
        "act1shizune_achieve",
        "act1lilly_achieve",
        "act1rin_achieve",
        "act1hanako_achieve",
        "choice_achieve"
    }

    if persistent.ach is None:
        persistent.ach = []


init python:
    if config.steam_appid:
        achievement.sync()
        achievement.steam_position = "top left"

    
    def achcheck():
        
        if not config.steam_appid:
            return
        
        ids = list(achdata)
        for id in ids:
            if achievement.has(id):
                if not id in persistent.ach:
                    persistent.ach.append(id)

    
    achcheck()

    def ach(id):
        if id in persistent.ach:
            return
        if not (id in persistent.ach):
            persistent.ach.append(id)
        if config.steam_appid:
            achievement.grant(id)

    Ach = renpy.curry(ach)
    def achdel(id=None):
        if id in persistent.ach:
            persistent.ach.remove(id)
        elif id is None:
            persistent.ach = []