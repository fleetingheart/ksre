import os
import pickle
import re
import sys
import zlib


def compile_pattern(pat):
    out = []
    i = 0
    while i < len(pat):
        if pat[i:i + 2] == "**":
            out.append(".*")
            i += 2
        elif pat[i] == "*":
            out.append("[^/]*")
            i += 1
        else:
            out.append(re.escape(pat[i]))
            i += 1
    return re.compile("".join(out) + r"\Z")


def main():
    project = sys.argv[1]
    out = sys.argv[2]

    src = open(os.path.join(project, "game", "options.rpy"), encoding="utf-8").read()
    block = re.search(r"NSFW_BUILD_PATTERNS = \[(.*?)\]", src, re.S).group(1)
    patterns = re.findall(r'"([^"]+)"', block)
    regexes = [compile_pattern(p) for p in patterns]

    names = []
    for root, dirs, files in os.walk(os.path.join(project, "game")):
        dirs.sort()
        for fn in sorted(files):
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, project).replace(os.sep, "/")
            if any(r.match(rel) for r in regexes):
                names.append((rel[len("game/"):], full))
    names.sort()

    key = 0x42424242
    index = {}
    with open(out, "wb") as f:
        f.write(b"RPA-3.0 XXXXXXXXXXXXXXXX XXXXXXXX\n")
        for name, path in names:
            with open(path, "rb") as df:
                data = df.read()
            f.write(b"Made with Ren'Py.")
            offset = f.tell()
            f.write(data)
            index[name] = [(offset ^ key, len(data) ^ key, b"")]
        indexoff = f.tell()
        f.write(zlib.compress(pickle.dumps(index, 2)))
        f.seek(0)
        f.write(b"RPA-3.0 %016x %08x\n" % (indexoff, key))

    print("%s: %d files" % (out, len(names)))
    if "sprites/eminude/eminude_neutral.png" not in index:
        print("probe file missing from archive", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
