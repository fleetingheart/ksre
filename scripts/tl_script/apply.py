import re
import sys
import json

exp = re.compile(r"\A([a-zA-Z0-9_]* )?\"(.+)\"(.*)\Z")
dataset = json.load(open(sys.argv[1], "r"))
tl = open(sys.argv[2], "r").readlines()

for i in range(len(tl)):
    t = tl[i].strip()
    if exp.match(t) is None or t.startswith("old \""):
        continue

    if t.startswith("new \""):
        t = t[4:]
    if t.endswith(" nointeract"):
        t = t[:-11]

    new = dataset.get(t)

    if new is None:
        print("Failed to translate:")
        print(tl[i])
        continue

    tl[i] = tl[i].replace(t, new)

open("new-" + sys.argv[2], "w").write("".join(tl))
