# This simple file serves to show modding capabilites of KS:RE
# Enjoy creating!

init:
    # `mods["test_mod"]` is internal mod name, it must match with name of first label
    # `u"Test mod"` is external name, it will show user your in-game name of mod
    $ mods["test_mod"] = u"Test mod"
label test_mod:
    scene bg op_snowywoods
    show snow
    with Dissolve(2.0)
    show misha sign_smile
    with charachange
    mi "This is a success, Hicchan~!"
    show misha cross_laugh
    with charachange
    mi "Goodbye, Hicchan~! See you soon!"