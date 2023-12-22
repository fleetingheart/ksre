screen pxt():
    tag menu
    style_prefix "pxt"

    if main_menu:
        add "main_menu_bg"

    add "blind"

    frame:
        style_suffix "interface"

        has vbox

        text _("Mods > pXt"):
            bold True
            size bold_size

        frame:
            has vbox

            vbox:
                textbutton _("Start") action Start("pxt_start")
            
            vbox:
                style_prefix "check"

                textbutton _("Commentary") action ToggleVariable("commentary", True, False)

            vbox:
                textbutton _("About") action ShowMenu("pxt_about")

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("mods")

screen pxt_about():
    tag menu
    style_prefix "pxt_about"

    if main_menu:
        add "main_menu_bg"

    add "blind"

    frame:
        style_suffix "interface"
        xsize 1200

        has vbox

        text _("Mods > pXt > About"):
            bold True
            size bold_size

        frame:
            has vbox

            vbox:

                text _("A short concept piece based around using only freely available resources for NaNoRenO by 4LS.\n")

                text _("Tells the love story of Pyramus and Thisbe, which is a part of Roman mythology.\n")

                text _("Port by Ikariya.\n")

        textbutton _("Return"):
            style "return_button"
            action ShowMenu("pxt")
