init python:
    phi = Character("Philostrate", who_color="#CCCCCC")
    the = Character("Theseus", who_color="#CCCCCC")
    hip = Character("Hippolyta", color="#CCCCCC")
    lys = Character("Lysander", who_color="#CCCCCC")
    dem = Character("Demetrius", who_color="#CCCCCC")

    py = Character("Pyramus", who_color="#77654d")
    bo = Character("Bottom", kind=py)
    th = Character("Thisbe", who_color="#c7966d")
    wa = Character("Wall", who_color="#a7935e")
    mo = Character("Moon", who_color="#ff8a66")
    lio = Character("Lion", who_color="#d17079")

    pr = Character(kind=n)

    commentary = False

    style.say_dialogue.size = 20

    scene_names["pxt_real_start.pxt_start"] = _("pXt Start")

init:
    $ mods["pxt"] = "pXt"
    $ mods_with_menus["pxt"] = True

    image bg arcadia = "mods/pxt/arcadia.jpg"

    image curtains = "mods/pxt/curtains.jpg"

    image audience = "mods/pxt/audience.png"
    image philostrates = "mods/pxt/philostrates.png"

    image moon smile = "mods/pxt/sprites/01/01.png"
    image moon happy = "mods/pxt/sprites/01/02.png"
    image moon sad = "mods/pxt/sprites/01/03.png"
    image moon embarrassed = "mods/pxt/sprites/01/04.png"
    image moon blush = "mods/pxt/sprites/01/05.png"

    image lion happy = "mods/pxt/sprites/02/01.png"
    image lion smile = "mods/pxt/sprites/02/02.png"
    image lion shock = "mods/pxt/sprites/02/03.png"
    image lion embarrassed = "mods/pxt/sprites/02/04.png"
    image lion sad = "mods/pxt/sprites/02/05.png"

    image wall smile = "mods/pxt/sprites/03/01.png"
    image wall happy = "mods/pxt/sprites/03/02.png"
    image wall sad = "mods/pxt/sprites/03/03.png"
    image wall downtrodden = "mods/pxt/sprites/03/04.png"
    image wall embarrassed = "mods/pxt/sprites/03/05.png"

    image pyramus neutral = "mods/pxt/sprites/04/01.png"
    image pyramus happy = "mods/pxt/sprites/04/02.png"
    image pyramus angry = "mods/pxt/sprites/04/03.png"
    image pyramus embarrassed = "mods/pxt/sprites/04/04.png"
    image pyramus smile = "mods/pxt/sprites/04/05.png"

    image thisbe smile = "mods/pxt/sprites/05/01.png"
    image thisbe shock = "mods/pxt/sprites/05/02.png"
    image thisbe sad = "mods/pxt/sprites/05/03.png"
    image thisbe happy = "mods/pxt/sprites/05/04.png"
    image thisbe cry = "mods/pxt/sprites/05/05.png"
