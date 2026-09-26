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
    build.classify("/fastlane/**", None)
    build.classify("/flatpak/**", None)
    build.classify("/steamdeck/*.*", None)
    build.classify("/.woodpecker/*.*", None)
    build.classify("/scripts/**", None)
    build.classify("/renconstruct/*.*", None)
    build.classify("**/caddy.conf.template", None)
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

    import os

    KSRE_STORE = "KSRE_STORE" in os.environ

    NSFW_BUILD_PATTERNS = [
        "game/event/emi_grinding/**",
        "game/event/emi_shed/**",
        "game/event/lilly_afterbath/**",
        "game/event/lilly_bath/**",
        "game/event/lilly_cowgirl/**",
        "game/event/lilly_handjob/**",
        "game/event/rin_h/**",
        "game/event/rin_h2/**",
        "game/event/shizune_hcg_tied/**",
        "game/event/shizu_undressing/**",
        "game/event/emi_miss_*.png",
        "game/event/emi_ending_*.png",
        "game/event/rin_high_frown.png",
        "game/event/rin_high_grin.png",
        "game/event/rin_high_grinwide.png",
        "game/event/rin_high_oneeye.png",
        "game/event/rin_high_open.png",
        "game/event/rin_high_smile.png",
        "game/event/rin_relief_*.png",
        "game/event/lilly_masturbate*.png",
        "game/event/hanako_bed_*.png",
        "game/event/hanako_missionary_*.png",
        "game/event/shizu_pushdown.png",
        "game/event/shizu_straddle_*.png",
        "game/event/shizu_table_*.png",
        "game/event/misha_naked.png",
        "game/event/misha_sex_*.png",
        "game/event/thumb/emi_grinding.jpg",
        "game/event/thumb/emi_shed.jpg",
        "game/event/thumb/emi_miss.jpg",
        "game/event/thumb/hanako_bed.jpg",
        "game/event/thumb/hanako_missionary.jpg",
        "game/event/thumb/lilly_handjob.jpg",
        "game/event/thumb/lilly_cowgirl.jpg",
        "game/event/thumb/lilly_bath.jpg",
        "game/event/thumb/lilly_afterbath.jpg",
        "game/event/thumb/lilly_masturbate.jpg",
        "game/event/thumb/rin_relief.jpg",
        "game/event/thumb/rin_h.jpg",
        "game/event/thumb/rin_h2.jpg",
        "game/event/thumb/shizune_tied.jpg",
        "game/event/thumb/shizu_undressing.jpg",
        "game/event/thumb/shizu_pushdown.jpg",
        "game/event/thumb/shizu_straddle.jpg",
        "game/event/thumb/shizu_table.jpg",
        "game/event/thumb/misha_naked.jpg",
        "game/event/thumb/misha_sex.jpg",
        "game/sprites/eminude/**",
        "game/sprites/rinpan/**",
        "game/sprites/hanagown/**stock**",
        "game/sprites/lilly/**_nak**",
        "game/sprites/shizu/**_nak**",
    ]

    for nsfw_pattern in NSFW_BUILD_PATTERNS:
        build.classify(nsfw_pattern, "nsfw")

    build.archive("nsfw", "nsfw_patch" if KSRE_STORE else "all")

    if KSRE_STORE:
        build.package("nsfw_patch", "zip", "nsfw_patch", description="18+ content patch", update=False, dlc=True, hidden=True)

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
