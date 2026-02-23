import re
import sys
import json
from enum import Enum


class ModeType(Enum):
    NONE = -1
    OLD_NEW_PAIR = 0
    BLOCK = 1

def cleanup_key(key: str):
    return (key
            .strip()
            .replace("“", "'")
            .replace("”", "'")
            .replace("‘", "'")
            .replace("’", "'"))

# exp = re.compile(r"\A([a-zA-Z0-9_]* )?\"(.+)\"(.*)\Z")
# exp_com = re.compile(r"\A\#( [a-zA-Z0-9_]* )\"(.*)\Z")

exp_block = re.compile(r"\A\# (?P<original>(?:\"[a-zA-Z0-9_]+\" |[a-zA-Z0-9_]+ |)\"(?P<vspace>\{vspace=(?P<vspace_amount>[\d]+)\}|).*\")(?P<suffix>.*)\Z")
exp_code_block = re.compile(r"\A\# (?P<code>nvl .+)\Z")
dataset = json.load(open(sys.argv[1], "r", encoding="utf8"))
tl = open(sys.argv[2], "r", encoding="utf-8-sig").readlines()


MODE = ModeType.NONE
warnings = []
block = []
flags = []

for i in range(len(tl)):
    t = tl[i].strip()

    pre = "    "
    if "vspace=" in t:
        t = t.replace("{vspace=30}", "\\n")
        t = t.replace("{vspace=60}", "\\n\\n")
        t = t.replace("{vspace=90}", "\\n\\n\\n")
        t = t.replace("{vspace=120}", "\\n\\n\\n\\n")
        t = t.replace("{vspace=150}", "\\n\\n\\n\\n\\n")
        t = t.replace("{vspace=180}", "\\n\\n\\n\\n\\n\\n")
        t = t.replace("{vspace=210}", "\\n\\n\\n\\n\\n\\n\\n")
        t = t.replace("{vspace=240}", "\\n\\n\\n\\n\\n\\n\\n\\n")
        t = t.replace("{vspace=270}", "\\n\\n\\n\\n\\n\\n\\n\\n\\n")
        t = t.replace("{vspace=300}", "\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
        t = t.replace("{vspace=330}", "\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n")
    if t.startswith("# TODO"):
        # Skip TODOs
        continue
    # if t.startswith("new \"") or t.find("\"\"") != -1:
    #     # Skip NEW for now and empty strings
    #     continue

    if t.startswith("old \""):
        MODE = ModeType.OLD_NEW_PAIR
        new = dataset.get(cleanup_key(t[4:]))
        if new is None:
            warnings.append(f"Missing translation on line {i}: {tl[i]}")
            new = t[4:]
        tl[i+1] = f"{pre}new {new}\n"
    elif exp_block.match(t) is not None:
        MODE = ModeType.BLOCK
        original = exp_block.match(t).group("original")
        suffix = exp_block.match(t).group("suffix")
        vspace = exp_block.match(t).group("vspace")

        if vspace is not None and vspace != "":
            vspace_amount = int(exp_block.match(t).group("vspace_amount"))
            original = re.sub(r"\{vspace=\d+\}", "\\n" * (vspace_amount // 30), original)
        new = dataset.get(cleanup_key(original))
        if new is None:
            warnings.append(f"Missing translation on line {i}: {tl[i]}")
            new = original
        block.append(f"{pre}{new}{suffix}")
    elif exp_code_block.match(t) is not None:
        MODE = ModeType.BLOCK
        code = exp_code_block.match(t).group("code")
        block.append(f"{pre}{code}")
    else:
        MODE = ModeType.NONE
        if len(block) > 0:
            block_start = i
            for block_i in range(len(block)):
                tl[block_start + block_i] = f"{block[block_i]}\n"
        block.clear()

open("tl-" + sys.argv[2], "w", encoding="utf8").write("".join(tl))
# print("[i] Auto application complete.")
if len(warnings) != 0:
    print("[!] {} warnings found.".format(len(warnings)))
    for warn in warnings:
        print(warn)
    exit(1)
