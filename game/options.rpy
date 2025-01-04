# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

init python:
    build.directory_name = "KSRE"
    build.executable_name = "Katawa Shoujo Re-Engineered"

    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("videos", "all")
    build.archive("audio", "all")
    build.archive("fonts", "all")

    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
    build.classify("**.rpy", None)
    build.classify("**.rpym", None)
    build.classify("**.psd", None)
    build.classify("/tl_script/*.*", None)
    build.classify("/flatpak/*.*", None)
    build.classify("/steamdeck/*.*", None)
    build.classify("**/renconstruct.toml", None)
    build.classify("**/CONTRIBUTING.md", None)
    build.classify("**/_android-presplash.png", None)
    build.classify("/docs/*.*", None)
    build.classify("/.git/*.*", None)
    build.classify("**.sublime-project", None)
    build.classify("**.sublime-workspace", None)
    build.classify("/music/*.*", None)
    build.classify("script-regex.txt", None)
    build.classify("/game/10", None)
    build.classify("/game/cache/*.*", None)
    build.classify("**/.DS_Store", None)
    build.classify("**/*.keystore", None)
    build.classify("/game/.vscode/*.*", None)
    build.classify("**/dists", None)

    build.classify("game/**.wav", "audio android")
    build.classify("game/**.mp3", "audio android")
    build.classify("game/**.ogg", "audio android")
    build.classify("game/**.ttf", "fonts android")
    build.classify("game/**.otf", "fonts android")
    build.classify("game/**.jpg", "images android")
    build.classify("game/**.png", "images android")
    build.classify("game/**.rpyc", "scripts android")
    build.classify("game/**.rpymc", "scripts android")
    build.classify("game/**.mkv", "videos android")
