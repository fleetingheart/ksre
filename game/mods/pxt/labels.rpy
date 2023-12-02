label pxt:
    show screen pxt
    call screen pxt

    return

label pxt_start:
    stop music fadeout 1.0

    scene black
    with config.game_main_transition
    pause 2.0

    call pxt_real_start

    return