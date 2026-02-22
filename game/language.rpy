# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

init python:
    class LanguageInformation(python_object):
        def __init__(self, label=None, linux_voice=None, mac_voice=None, allow_fonts=True):
            self.label = label
            self.linux_voice = linux_voice
            self.mac_voice = mac_voice
            self.allow_fonts = allow_fonts

    languages = {
        None:      LanguageInformation(_("English"), "en-us", "Samantha", True),
        "ru":      LanguageInformation(_("Russian"), "ru", "Milena", True),
        "fr":      LanguageInformation(_("French"), "fr-fr", "Thomas", True),
        "it":      LanguageInformation(_("Italian"), "it", "Alice", True),
        "pt_br":   LanguageInformation(_("Brazilian Portuguese"), "pt-br", "Luciana", True),
        "es":      LanguageInformation(_("Spanish"), "es", "Monica", True),
        "de":      LanguageInformation(_("German"), "de", "Anna", True),
        "jp":      LanguageInformation(_("Japanese"), "ja", "Kyoko", False),
        "zh_hans": LanguageInformation(_("Simplified Chinese"), "cmn", "Tingting", False),
        "zh_hant": LanguageInformation(_("Traditional Chinese"), "cmn", "Sinji", False),
    }

    def update_tts_voice():
        lang = renpy.game.preferences.language
        info = languages.get(lang, languages[None])

        # Windows support is not here, because Windows sets the voice that is
        # used by Ren'Py system-wide, we can't control it reliably.
        if renpy.linux:
            renpy.config.tts_voice = info.linux_voice
        elif renpy.macintosh:
            renpy.config.tts_voice = info.mac_voice
