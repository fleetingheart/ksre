# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

init python:
    class LanguageInformation(python_object):
        def __init__(self, label=None, linux_voice=None, mac_voice=None):
            self.label = label
            self.linux_voice = linux_voice
            self.mac_voice = mac_voice

    languages = {
        None:      LanguageInformation(_("English"), "en-us", "Samantha"),
        "ru":      LanguageInformation(_("Russian"), "ru", "Milena"),
        "fr":      LanguageInformation(_("French"), "fr-fr", "Thomas"),
        "it":      LanguageInformation(_("Italian"), "it", "Alice"),
        "pt_br":   LanguageInformation(_("Brazilian Portuguese"), "pt-br", "Luciana"),
        "es":      LanguageInformation(_("Spanish"), "es", "Monica"),
        "de":      LanguageInformation(_("German"), "de", "Anna"),
        "jp":      LanguageInformation(_("Japanese"), "ja", "Kyoko"),
        "zh_hans": LanguageInformation(_("Simplified Chinese"), "cmn", "Tingting"),
        "zh_hant": LanguageInformation(_("Traditional Chinese"), "cmn", "Sinji"),
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
