import os
import copy
import json
import datetime
import re

class TranslationEntry:
    def __init__(self, file: str, linenum: int, lang: str, key: str | None, origtext: str, text: str):
        self.file = file
        self.linenum = linenum
        self.lang = lang
        self.key = key
        self.origtext = origtext
        self.text = text

    def __str__(self):
        return f"<{self.file}:{self.linenum}> {self.lang} {self.key}: ({self.origtext}) {self.text}"

    def is_keyless(self):
        return self.key is None

class TranslationMapping:
    def __init__(self, old: str, new: str):
        self.old = old
        self.new = new

    def __str__(self):
        return f"{self.old} -> {self.new}"

    def to_json(self) -> dict:
        return {"old": self.old, "new": self.new}

    @staticmethod
    def from_json(obj):
        if "old" in obj and "new" in obj:
            return TranslationMapping(obj["old"], obj["new"])
        raise Exception(f"Invalid translation mapping: {obj}")

class TranslationMappings:
    def __init__(self, mappings: list[TranslationMapping]):
        self.mappings = mappings
        self.old2new = {}
        self.new2old = {}
        self._update_maps(mappings)

    def _update_maps(self, mappings):
        for mapping in mappings:
            self.old2new[mapping.old] = mapping.new
            self.new2old[mapping.new] = mapping.old

    def merge(self, other):
        self.mappings.extend(other.mappings)
        self._update_maps(other.mappings)

    def get_old_key(self, new_key: str) -> str:
        return self.new2old[new_key]

    def has_old_key(self, new_key: str) -> bool:
        return new_key in self.new2old

    def get_new_key(self, old_key: str) -> str:
        return self.old2new[old_key]

    def has_new_key(self, old_key: str) -> bool:
        return old_key in self.old2new

    def to_json(self) -> dict:
        mappings = []
        for mapping in self.mappings:
            mappings.append(mapping.to_json())
        return mappings

    @staticmethod
    def from_json(obj):
        mappings = []
        if type(obj) is list:
            for mapping_obj in obj:
                mappings.append(TranslationMapping.from_json(mapping_obj))
        return TranslationMappings(mappings)

def make_parent_dirs(filepath: str) -> None:
    parentdir = os.path.dirname(filepath)
    if not os.path.exists(parentdir):
        os.makedirs(parentdir)

def read_translation_entries(path: str) -> list[TranslationEntry]:
    entries = []
    with open(path, "r", encoding="utf-8-sig") as infile:
        curr_linenum = 0
        file = ""
        linenum = 0
        lang = ""
        key = ""
        origtext = ""
        text = ""
        for line in infile.readlines():
            curr_linenum += 1
            line = line.rstrip("\n\r")
            if line.startswith("# game/"):
                file = line[2:line.index(":")]
                linenum = int(line[line.index(":")+1:])
            elif line.startswith("translate "):
                lang = line[10:line.rfind(" ")]
                key = line[line.rfind(" ")+1:-1]
            elif line.startswith("    "):
                if line.startswith("    # "):
                    if key == "strings":
                        file = line[6:line.index(":")]
                        linenum = int(line[line.index(":")+1:])
                    else:
                        origtext = line[6:]
                else:
                    if line.startswith("    old "):
                        origtext = line[8:]
                    elif line.startswith("    new "):
                        text = line[8:]
                    elif key != "strings":
                        text = line[4:]
                    else:
                        print(f"WARN: Malformed line? [{path}:{curr_linenum}] {line}")
            elif line != "" and not line.startswith("# TODO: Translation updated at "):
                print(f"WARN: Malformed line? [{path}:{curr_linenum}] {line}")
            if text != "":
                if file == "" or linenum == 0 or lang == "" or key == "" or origtext == "":
                    print(f"WARN: Encountered text without requirements. [{path}:{curr_linenum}] {line}")
                else:
                    entry = TranslationEntry(file, linenum, lang, key if key != "strings" else None, origtext, text)
                    entries.append(entry)
                file = ""
                linenum = 0
                origtext = ""
                text = ""
                if key != "strings":
                    lang = ""
                    key = ""
    return entries

def find_line_numbers(filepath: str, text: str) -> list[int]:
    linenums = []
    with open(filepath, "r", encoding="utf-8-sig") as file:
        linenum = 0
        for line in file.readlines():
            line = line.strip()
            linenum += 1
            if line == text:
                linenums.append(linenum)
    return linenums

def find_matching_orphans(orphans: list[TranslationEntry], entry: TranslationEntry) -> list[TranslationEntry]:
    matches = []
    for orphan in orphans:
        if orphan.lang == entry.lang and orphan.origtext == entry.origtext and orphan.file == entry.file:
            matches.append(orphan)
    return matches

def find_matching_entries(entries: list[TranslationEntry], orphan: TranslationEntry, takenkeys: set) -> list[TranslationEntry]:
    matching = []
    for entry in entries:
        if entry.key not in takenkeys and entry.file == orphan.file and entry.lang == orphan.lang and entry.origtext == orphan.origtext:
            matching.append(entry)
    return matching

def map_broken_translations(entries: list[TranslationEntry]) -> TranslationMappings:
    orphans: list[TranslationEntry] = []
    result: list[TranslationEntry] = []
    takenkeys = set()
    mappings: list[TranslationMapping] = []
    # Find "orphan" translations. These are translations with an empty string, which Ren'Py will generate if no
    # translation is found for a particular string in a script. This only checks for keyed translations, since those
    # are the only ones that are broken when updating a script.
    for match in entries:
        if match.key is not None and match.text.endswith('""'):
            orphans.append(match)
        else:
            result.append(copy.copy(match))
    index = 0
    for orphan in orphans:
        index += 1
        all_matching = find_matching_entries(result, orphan, takenkeys)
        match: TranslationEntry = None
        if len(all_matching) == 0:
            print(f"WARN: Orphan has no matching entry - {orphan}")
        elif len(all_matching) == 1:
            match = all_matching[0]
        else:
            while match is None:
                print(f"Found multiple matching entries ({index}/{len(orphans)}):")
                print(f"Orphan: <{orphan.file}:{orphan.linenum}> {orphan.key}: {orphan.origtext}")
                for i, entry in enumerate(all_matching):
                    print(f"\t{i+1} - <{entry.file}:{entry.linenum}> {entry.key}")
                print("\t0 - Quit")
                try:
                    keep = int(input("Which one to replace? "))
                    if keep < 0 or keep > len(all_matching):
                        print("ERROR: Invalid selection")
                    elif keep == 0:
                        return
                    else:
                        match = all_matching[keep - 1]
                except ValueError:
                    print("ERROR: Invalid selection")
        if match is not None:
            takenkeys.add(match.key)
            mappings.append(TranslationMapping(match.key, orphan.key))
    return TranslationMappings(mappings)

def dump_translation_mappings(mappings: TranslationMappings, outpath: str) -> None:
    make_parent_dirs(outpath)
    with open(outpath, "w", encoding="utf-8-sig") as file:
        json.dump(mappings.to_json(), file, indent=2)

def load_translation_mappings(infile: str) -> TranslationMappings:
    with open(infile, "r", encoding="utf-8-sig") as file:
        mappings_obj = json.load(file)
        return TranslationMappings.from_json(mappings_obj)

def fix_translations(entries: list[TranslationEntry], mappings: TranslationMappings) -> list[TranslationEntry]:
    result = []
    for entry in entries:
        add = None
        if entry.is_keyless():
            add = entry
        elif mappings.has_new_key(entry.key):
            new_key = mappings.get_new_key(entry.key)
            newlinenum = entry.linenum
            for entry2 in entries:
                if entry2.key == new_key:
                    newlinenum = entry2.linenum
                    break
            add = TranslationEntry(entry.file, newlinenum, entry.lang, new_key, entry.origtext, entry.text)
        elif not mappings.has_old_key(entry.key):
            add = entry
        if add is not None:
            result.append(add)
    return result

def write_translation_file(entries: list[TranslationEntry], outpath: str) -> None:
    make_parent_dirs(outpath)
    with open(outpath, "w", encoding="utf-8-sig") as outfile:
        outfile.write(f"# Generated at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        keyless = []
        lang = None
        for entry in entries:
            if lang is None:
                lang = entry.lang
            if entry.is_keyless():
                keyless.append(entry)
            else:
                outfile.write("\n")
                outfile.write(f"# {entry.file}:{entry.linenum}\n")
                outfile.write(f"translate {entry.lang} {entry.key}:\n\n")
                outfile.write(f"    # {entry.origtext}\n")
                outfile.write(f"    {entry.text}\n")
        if len(keyless) > 0:
            outfile.write("\n")
            outfile.write(f"translate {lang} strings:\n")
            for entry in keyless:
                outfile.write("\n")
                outfile.write(f"    # {entry.file}:{entry.linenum}\n")
                outfile.write(f"    old {entry.origtext}\n")
                outfile.write(f"    new {entry.text}\n")

def find_all_languages(game_dir: str) -> list[str]:
    langs = []
    tl_dir = os.path.join(game_dir, "tl")
    for dir in os.listdir(tl_dir):
        langs.append(dir)
    return langs

def main(args):
    if len(args) < 2:
        print(f"USAGE: {__file__} <gamedir> [--lang <lang>] [--file <script>] [--use <lang>] [--noreplace] [--regen]")
        print("\t--lang <lang>: Examine a specific language")
        print("\t--file <script>: Only examine a specific script file (RegEx supported!)")
        print("\t--use <lang>: Apply a specific language's mappings to all affected languages")
        print("\t--noreplace: Do not replace any translation files, only generate mappings")
        print("\t--regen: Regenerate and ignore any preexisting mappings")
        print("Make sure this is only ran after generating translations in Ren'Py and selecting \"Generate empty strings for translations\"")
        return

    gamedir = args[1]
    i = 2
    langs = []
    scripts = []
    useother = None
    noreplace = False
    regen = False
    while i < len(args):
        if args[i] == "--lang" and i < len(args) - 1:
            langs.append(args[i + 1])
            i += 1
        elif args[i] == "--file" and i < len(args) - 1:
            scripts.append(args[i + 1])
            i += 1
        elif args[i] == "--use" and i < len(args) - 1:
            useother = args[i + 1]
            i += 1
        elif args[i] == "--noreplace":
            noreplace = True
        elif args[i] == "--regen":
            regen = True
        else:
            print(f"WARN: Unknown argument <{args[i]}>. Ignoring...")
        i += 1

    if len(langs) == 0:
        for dir in os.listdir(f"{gamedir}/tl"):
            langs.append(dir)

    allentries = {}
    for lang in langs:
        langdir = os.path.normpath(os.path.join(gamedir, "tl", lang))
        if os.path.exists(langdir):
            toscan = []
            for root, dirs, files in os.walk(langdir):
                for file in files:
                    filepath = os.path.join(root, file)
                    if len(scripts) == 0:
                        if filepath.endswith(".rpy"):
                            toscan.append(filepath)
                    else:
                        shouldadd = False
                        for script in scripts:
                            if re.search(script, filepath) is not None and filepath.endswith(".rpy"):
                                shouldadd = True
                                break
                        if shouldadd:
                            toscan.append(filepath)
            if len(toscan) > 0:
                files = {}
                for filepath in toscan:
                    print(f"Now reading <{filepath}>...")
                    files[filepath] = read_translation_entries(filepath)
                allentries[lang] = files
            else:
                print(f"ERROR: Could not find any files to scan in {langdir}")
        else:
            print(f"ERROR: Directory for language does not exist {langdir}")

    for lang, files in allentries.items():
        if useother is not None:
            mapfile = os.path.join("tmp", f"mappings-{useother}.json")
        else:
            mapfile = os.path.join("tmp", f"mappings-{lang}.json")
        mappings = TranslationMappings([])
        if not os.path.exists(mapfile) or regen:
            for filepath, entries in files.items():
                mappings.merge(map_broken_translations(entries))
            print(f"Writing translation mappings for {lang} to {mapfile}...")
            dump_translation_mappings(mappings, mapfile)
        else:
            print(f"Reading mappings file {mapfile}...")
            mappings.merge(load_translation_mappings(mapfile))
        if not noreplace:
            for filepath, entries in files.items():
                print(f"Writing fixed translation file to {filepath}...")
                write_translation_file(fix_translations(entries, mappings), filepath)

if __name__ == "__main__":
    import sys
    main(sys.argv)
