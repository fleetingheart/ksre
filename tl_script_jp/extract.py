import re
import sys

exp_line = re.compile(r"\A([a-zA-Z0-9_]* )?\"(.+)\"(.*)\Z")
exp_doublespeak = re.compile(r"\A\$\s*doublespeak\s*\([a-zA-Z0-9_]+,\s*[a-zA-Z0-9_]+,\s*(?P<first>\".+?\")\s*(,\s*(?P<second>\".+\")|)\s*\)\Z")

prefix_ignore = [
    "\"emi basic_grin_rn\"",
    "\"emi invis\" with Dissolve",
    "\"rin basic_absent_rn\"",
    "\"ev hisao_letter_open_2\"",
    "\"rin relaxed_nonchalant_close_rn\""
]


def extract(path):
    old = open(path, "r").readlines()
    new = ""

    print(f"Not an actual text for '{path}':")
    for line in old:
        skip_line = False

        if line == "\n":
            continue

        for ignore in prefix_ignore:
            if line.strip().startswith(ignore):
                skip_line = True
                break
        if skip_line:
            continue

        if line.strip().startswith("$ written_note("):
            left_strip = 15
            if line.strip().startswith("$ written_note(u"):
                left_strip = 16
            if line.strip().endswith(", quiet=True)"):
                new += line.strip()[left_strip:-13] + "\n"
            else:
                new += line.strip()[left_strip:-1] + "\n"
        elif exp_doublespeak.match(line.strip()) is not None:
            match = exp_doublespeak.match(line.strip())
            new += f"{match.group('first').strip()}\n"
            if match.group('second') is not None:
                new += f"{match.group('second').strip()}\n"
            else:
                new += f"{match.group('first').strip()}\n"
        elif exp_line.match(line.strip()) is not None:
            line = line.replace(" with Dissolve(4.0)\n", "\n")
            line = line.replace(" with dissolve\n", "\n")
            line = line.replace(" with hpunch\n", "\n")
            line = line.replace(" with vpunch\n", "\n")
            if line.endswith(":\n"):
                new += line[:-2] + "\n"
            else:
                new += line
        # else:
        #     print(line.strip())

    open("new-" + path, "w", encoding="utf-8").write(new)

for file in sys.argv[1:]:
    extract(file)
    print()
