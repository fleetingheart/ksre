# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

define audio_prefix = "mods/summersclover/audio/"

init python:
    def sc_music(filename, alias):
        fullpath = audio_prefix + "ost/" + filename + ".ogg"
        setattr(store, "music_" + alias, fullpath)
        store._tracks[fullpath] = filename.replace("_", " ")

    sc_music("Carefree_Days", "miki")

define sfx_tcard = audio_prefix + "sfx/tcard.ogg"
