# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

init python:
    class LanguageInformation(python_object):
        def __init__(self,label=None, linux_voice=None):
            self.label = label
            self.linux_voice = linux_voice

    # How to add more languages:
    # 1. Generate a new language set by Ren'Py launcher
    # 2. Build a class with the information about the language's voices. 
    # The key of the dict is the name of the language folder.
    languages: dict[str | None, LanguageInformation] = {
        None:      LanguageInformation(_("English"), "en-us"),
        "ru":      LanguageInformation(_("Russian"), "ru"),
        "fr":      LanguageInformation(_("French"), "fr-fr"),
        "it":      LanguageInformation(_("Italian"), "it"),
        "pt_br":   LanguageInformation(_("Brazilian Portuguese"), "pt-br"),
        "es":      LanguageInformation(_("Spanish"), "es"),
        "de":      LanguageInformation(_("German"), "de"),
        "jp":      LanguageInformation(_("Japanese"), "ja"),
        "zh_hans": LanguageInformation(_("Simplified Chinese"), "cmn"),
        "zh_hant": LanguageInformation(_("Traditional Chinese"), "cmn"),
    }


    def update_tts_voice():
        lang = renpy.game.preferences.language
        info = languages.get(lang, languages[None])

        if renpy.linux:
            renpy.config.tts_voice = info.linux_voice
