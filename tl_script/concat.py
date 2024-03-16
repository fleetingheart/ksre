import os
import sys
import json

og = open(sys.argv[1], "r").readlines()
tl = open(sys.argv[2], "r").readlines()
assert len(og) == len(tl)

out = {}

for i in range(len(og)):
    out[og[i].strip()] = tl[i].strip()

json.dump(out, open(f"{os.path.splitext(sys.argv[1])[0]}.json", "w"), ensure_ascii=False, indent="\t")
