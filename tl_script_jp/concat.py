import os
import re
import sys
import json

og = open(sys.argv[1], "r").readlines()
tl = open(sys.argv[2], "r").readlines()

if len(og) != len(tl):
    print(f"Error: The number of original lines ({len(og)}) does not match the number of translated lines ({len(tl)}).")

    exp_block = re.compile(r"\A(?:(?P<actor>[a-zA-Z0-9_]+) \".*)|.*\Z")
    with open(sys.argv[1], "r") as og_f, open(sys.argv[2], "r") as tl_f:
        og_lines = og_f.readlines()
        tl_lines = tl_f.readlines()

        for i in range(min(len(og_lines), len(tl_lines))):
            og_match = exp_block.match(og_lines[i].strip())
            tl_match = exp_block.match(tl_lines[i].strip())

            if og_match and tl_match:
                og_actor = og_match.group("actor")
                tl_actor = tl_match.group("actor")
                if og_actor != tl_actor:
                    print(f"Line {i + 1}: Not mathching by actor check", flush=True)
                    sys.exit(1)
            else:
                print(f"Line {i + 1}: Not matching by regex check", flush=True)
                sys.exit(1)

    print("Check the input files for mismatched lines.", flush=True)
    sys.exit(1)

out = {}


def cleanup_key(key: str):
    return (key
            .strip()
            .replace("“", "'")
            .replace("”", "'")
            .replace("‘", "'")
            .replace("’", "'"))

for i in range(len(og)):
    out[cleanup_key(og[i])] = tl[i].strip()

json.dump(out, open(f"{os.path.splitext(sys.argv[1])[0]}.json", "w"), ensure_ascii=False, indent="\t")
