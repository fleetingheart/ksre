# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

init -100 python:
    import os

    NSFW_SPRITE_FILES = frozenset([
        "sprites/eminude/close/eminude_angry_close.png",
        "sprites/eminude/close/eminude_blush_close.png",
        "sprites/eminude/close/eminude_closedsmile_close.png",
        "sprites/eminude/close/eminude_evil_close.png",
        "sprites/eminude/close/eminude_frown_close.png",
        "sprites/eminude/close/eminude_grin_close.png",
        "sprites/eminude/close/eminude_happy_close.png",
        "sprites/eminude/close/eminude_neutral_close.png",
        "sprites/eminude/close/eminude_pout_close.png",
        "sprites/eminude/close/eminude_sad_close.png",
        "sprites/eminude/close/eminude_smile_close.png",
        "sprites/eminude/close/eminude_weaksmile_close.png",
        "sprites/eminude/close/eminude_wink_close.png",
        "sprites/eminude/eminude_awayfrown.png",
        "sprites/eminude/eminude_blush.png",
        "sprites/eminude/eminude_closedsmile.png",
        "sprites/eminude/eminude_evil.png",
        "sprites/eminude/eminude_frown.png",
        "sprites/eminude/eminude_grin.png",
        "sprites/eminude/eminude_happy.png",
        "sprites/eminude/eminude_neutral.png",
        "sprites/eminude/eminude_pout.png",
        "sprites/eminude/eminude_weaksmile.png",
        "sprites/eminude/eminude_wink.png",
        "sprites/hanagown/close/hanagown_stockworry_blush_close.png",
        "sprites/hanagown/hanagown_stockdistant_blush.png",
        "sprites/hanagown/hanagown_stocknormal_blush.png",
        "sprites/lilly/close/lilly_behind_listen_nak_close.png",
        "sprites/lilly/lilly_behind_emb_nak.png",
        "sprites/lilly/lilly_behind_giggle_nak.png",
        "sprites/lilly/lilly_behind_pout_nak.png",
        "sprites/lilly/lilly_behind_reminisce_nak.png",
        "sprites/lilly/lilly_behind_sleepy_nak.png",
        "sprites/lilly/lilly_behind_smile_nak.png",
        "sprites/lilly/lilly_behind_smileclosed_nak.png",
        "sprites/lilly/lilly_behind_weaksmile_nak.png",
        "sprites/rinpan/close/rinpan_basic_awayabsent_close.png",
        "sprites/rinpan/close/rinpan_basic_deadpan_close.png",
        "sprites/rinpan/close/rinpan_basic_deadpanamused_close.png",
        "sprites/rinpan/close/rinpan_basic_deadpancontemplation_close.png",
        "sprites/rinpan/close/rinpan_basic_deadpandelight_close.png",
        "sprites/rinpan/close/rinpan_basic_deadpanupset_close.png",
        "sprites/rinpan/close/rinpan_basic_lucid_close.png",
        "sprites/rinpan/close/rinpan_relaxed_boredom_close.png",
        "sprites/rinpan/close/rinpan_relaxed_doubt_close.png",
        "sprites/rinpan/close/rinpan_relaxed_nonchalant_close.png",
        "sprites/rinpan/close/rinpan_relaxed_sleepy_close.png",
        "sprites/rinpan/close/rinpan_relaxed_surprised_close.png",
        "sprites/rinpan/rinpan_basic_absent.png",
        "sprites/rinpan/rinpan_basic_amused.png",
        "sprites/rinpan/rinpan_basic_awayabsent.png",
        "sprites/rinpan/rinpan_basic_deadpan.png",
        "sprites/rinpan/rinpan_basic_deadpanamused.png",
        "sprites/rinpan/rinpan_basic_deadpancontemplation.png",
        "sprites/rinpan/rinpan_basic_deadpandelight.png",
        "sprites/rinpan/rinpan_basic_deadpannormal.png",
        "sprites/rinpan/rinpan_basic_deadpansurprised.png",
        "sprites/rinpan/rinpan_basic_deadpanupset.png",
        "sprites/rinpan/rinpan_basic_lucid.png",
        "sprites/rinpan/rinpan_basic_surprised.png",
        "sprites/rinpan/rinpan_basic_upset.png",
        "sprites/rinpan/rinpan_relaxed_boredom.png",
        "sprites/rinpan/rinpan_relaxed_doubt.png",
        "sprites/rinpan/rinpan_relaxed_nonchalant.png",
        "sprites/rinpan/rinpan_relaxed_sleepy.png",
        "sprites/rinpan/rinpan_relaxed_surprised.png",
        "sprites/shizu/shizu_behind_blank_nak.png",
        "sprites/shizu/shizu_behind_frown_nak.png",
        "sprites/shizu/shizu_behind_smile_nak.png",
        "sprites/shizu/shizu_behind_smilelow_nak.png",
    ])

    NSFW_PROBE_FILE = "sprites/eminude/eminude_neutral.png"

    class _NsfwState(object):
        ok = False
        status = "absent"
        restart_pending = False

    nsfw_state = _NsfwState()

    nsfw_boot_searchpath = tuple(config.searchpath)

    def nsfw_installed():
        return nsfw_state.ok

    def nsfw_patch_dir():
        if renpy.emscripten:
            return None
        return os.path.join(config.savedir, "game")

    def nsfw_script_dir():
        if renpy.emscripten:
            return None
        if renpy.android:
            if "ANDROID_PUBLIC" in os.environ:
                return os.path.join(os.environ["ANDROID_PUBLIC"], "game")
            return None
        return nsfw_patch_dir()

    def nsfw_dir_has_scripts(sdir):
        loose = (".rpy", ".rpyc", ".rpym", ".rpymc")
        try:
            for root, dirs, files in os.walk(sdir):
                dirs[:] = [d for d in dirs if not d.startswith(".")]
                for fn in files:
                    if fn.startswith("."):
                        continue
                    if fn.endswith(loose) or fn.endswith("_ren.py"):
                        return True
        except Exception:
            return False
        try:
            prefix = sdir + "/"
            for afn, index in renpy.loader.archives:
                if not afn.startswith(prefix):
                    continue
                for entry in index:
                    if entry.endswith((".rpyc", ".rpymc")):
                        return True
        except Exception:
            pass
        return False

    def nsfw_scripts_pending():
        sdir = nsfw_script_dir()
        if sdir is None:
            return False
        if sdir in nsfw_boot_searchpath:
            return False
        if not os.path.isdir(sdir):
            return False
        return nsfw_dir_has_scripts(sdir)

    def nsfw_prepare_scripts():
        if not nsfw_scripts_pending():
            return
        if not renpy.android:
            sdir = nsfw_script_dir()
            parts = [p for p in os.environ.get("RENPY_SEARCHPATH", "").split("::") if p]
            if sdir not in parts:
                parts.append(sdir)
                os.environ["RENPY_SEARCHPATH"] = "::".join(parts)
        nsfw_state.restart_pending = True

    def nsfw_remount():
        if renpy.emscripten:
            nsfw_state.ok = renpy.loadable(NSFW_PROBE_FILE)
            nsfw_state.status = "ok" if nsfw_state.ok else "absent"
            return nsfw_state.ok

        pdir = nsfw_patch_dir()
        if pdir is None:
            nsfw_state.ok = False
            return False

        try:
            os.makedirs(pdir, exist_ok=True)
        except Exception:
            pass

        if renpy.android and "ANDROID_PUBLIC" in os.environ:
            try:
                os.makedirs(os.path.join(os.environ["ANDROID_PUBLIC"], "game"), exist_ok=True)
            except Exception:
                pass

        try:
            for fn in os.listdir(config.savedir):
                src = os.path.join(config.savedir, fn)
                if fn.lower().endswith(".rpa") and os.path.isfile(src):
                    os.replace(src, os.path.join(pdir, fn))
        except Exception:
            pass

        if os.path.isdir(pdir) and pdir not in config.searchpath:
            config.searchpath.append(pdir)

        try:
            has_content = any(not e.name.startswith(".") for e in os.scandir(pdir))
        except Exception:
            has_content = False

        if has_content:
            try:
                renpy.loader.loadable_cache.clear()
                renpy.loader.archives.clear()
                renpy.loader.index_files()
            except Exception:
                nsfw_state.ok = False
                nsfw_state.status = "error"
                return False

        nsfw_state.ok = renpy.loadable(NSFW_PROBE_FILE)

        if nsfw_state.ok:
            nsfw_state.status = "ok"
        else:
            nsfw_state.status = "absent"
            try:
                if any(fn.endswith(".icloud") for fn in os.listdir(pdir)):
                    nsfw_state.status = "not_downloaded"
            except Exception:
                pass

        return nsfw_state.ok

    nsfw_remount()
    nsfw_prepare_scripts()

init 999 python:
    if not nsfw_installed():
        persistent.hdisabled = True
