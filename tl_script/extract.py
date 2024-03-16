import re
import sys

exp = re.compile(r"\A([a-zA-Z0-9_]* )?\"(.+)\"(.*)\Z")

def extract(path):
    old = open(path, "r").readlines()
    new = ""

    print(f"Not an actual text for '{path}':")
    for line in old:
        if line == "\n":
            continue
        if exp.match(line.strip()) is not None:
            new += line
        else:
            print(line.strip())

    open("new-" + path, "w", encoding="utf-8").write(new)

for file in sys.argv[1:]:
    extract(file)
    print()
