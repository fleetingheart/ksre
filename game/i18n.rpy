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

# Based off: https://github.com/Gouvernathor/renpy-TranslationTools
init python:
    from collections import defaultdict
    import itertools
    import os

    def sort_translates(languages=None, leave_backup=True):
        """
        Puts the orphan translations at the end of the file they're in, and (as a side-effect)
        orders the non-obsolete translations in the order of the dialogue they're translating.

        If `languages` is given, only the translations for these languages are sorted.
        `languages` can be a single language name or a list of language names.
        """

        set_all = set(renpy.known_languages())

        # checking languages
        if languages is None:
            languages = set_all
        else:
            if isinstance(languages, str):
                languages = {languages}
            languages = set(languages)

            unknowns = languages - set_all
            if unknowns:
                raise ValueError("languages contains unknown languages : {}".format(unknowns))

        dialogue = {} # identifier : (filename, linenumber)
        trans = {lang : defaultdict(list) for lang in languages} # language : filename : list of nodes
        transstring = defaultdict(list) # filename : list of "translate strings" nodes (which are actually init nodes)
        for nod in renpy.game.script.all_stmts:
            if isinstance(nod, (renpy.ast.Translate, renpy.ast.TranslateSay)):
                if nod.language is None:
                    dialogue[nod.identifier] = (nod.filename, nod.linenumber)
                elif nod.language in languages:
                    if f"/tl/{nod.language}/" in nod.filename:
                        trans[nod.language][nod.filename].append(nod)
            elif isinstance(nod, renpy.ast.Init) and all(isinstance(n, renpy.ast.TranslateString) for n in nod.block):
                if "/tl/" in nod.filename:
                    transstring[nod.filename].append(nod)
        dialogue = sorted(dialogue, key=dialogue.get) # list of all dialogue identifiers in the base game, in appearance order

        headermarker = object()
        stringsmarker = object()
        warning_comment = "\n# TODO: The following nodes are orphans, trying to translate an identifier that's not in the game.\n"
        for subdict in trans.values():
            for fn, nodlist in sorted(subdict.items()):
                long_fn = os.path.join(renpy.config.basedir, fn)
                has_orphans = False

                with open(long_fn, "r", encoding = "utf-8") as f:
                    lines = f.read().splitlines()

                boundaries = {} # linenumber : (language, identifier)
                for nod in itertools.chain(nodlist, transstring[fn]):
                    linenumber = nod.linenumber-1

                    if isinstance(nod, renpy.ast.TranslateSay):
                        while linenumber > 0 and not lines[linenumber].startswith("translate "):
                            linenumber -= 1

                    while lines[linenumber-1].startswith("#"):
                        linenumber -= 1

                    if isinstance(nod, (renpy.ast.Translate, renpy.ast.TranslateSay)):
                        boundaries[linenumber] = (nod.language, nod.identifier)
                        if (not has_orphans) and (nod.identifier not in dialogue):
                            has_orphans = True
                    else:
                        boundaries[linenumber] = ("", stringsmarker)

                if not has_orphans:
                    print("Skipping {} : no orphans".format(fn))
                    continue

                blocks = {} # (language, identifier) : block of lines
                block = []
                key = ("", headermarker)
                for linenumber, line in enumerate(lines):
                    if linenumber in boundaries:
                        if linenumber:
                            blocks[key] = "\n".join(block)
                        block = []
                        key = boundaries[linenumber]
                    block.append(line)
                blocks[key] = "\n".join(block)
                blocks["", warning_comment] = warning_comment

                def block_sort_function(key):
                    """
                    First the start of the file, then the good translate nodes,
                    then the strings, then the warning, then the orphan nodes.
                    """

                    (language, identifier), _block = key

                    index = 0
                    if identifier is headermarker:
                        group = 0
                    elif identifier is stringsmarker:
                        group = 2
                    elif identifier is warning_comment:
                        group = 3
                    elif identifier in dialogue:
                        group = 1
                        index = dialogue.index(identifier)
                    else:
                        group = 4

                    return (group, index, language)

                orderedblocks = [block for _key, block in sorted(blocks.items(), key=block_sort_function)]

                print("Writing sorted file {}".format(fn))

                if leave_backup:
                    with open(long_fn+".new", "w", encoding="utf-8") as f:
                        f.write("\n".join(orderedblocks))

                    try:
                        os.unlink(long_fn + ".bak")
                    except Exception:
                        pass

                    os.rename(long_fn, long_fn + ".bak")
                    os.rename(long_fn + ".new", long_fn)
                else:
                    with open(long_fn, "w", encoding="utf-8") as f:
                        f.write("\n".join(orderedblocks))
