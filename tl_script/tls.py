import argparse
import os
import sys
from itertools import zip_longest

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(required=True)

parser_re = subparsers.add_parser("requals")
parser_re.add_argument("orig", help="original file compare with")
parser_re.add_argument("trans", help="translation file compare to")

parser_sr = subparsers.add_parser("strip")
parser_sr.add_argument("file", help="file remove empty lines in")

parser_tl = subparsers.add_parser("trans")
parser_tl.add_argument("orig", help="original file")
parser_tl.add_argument("trans", help="translation file")
parser_tl.add_argument("tl", help="renpy translations generated file")

parser_tll = subparsers.add_parser("translines")
parser_tll.add_argument("file", help="translation file update to")

args = parser.parse_args()

if sys.argv[1] == "requals":
	old_orig = "old-" + args.orig
	if os.path.exists(old_orig):
		os.remove(old_orig)
	os.rename(args.orig, old_orig)
	orig_lines = list(open(old_orig, "r", encoding="utf-8"))
	old_trans = "old-" + args.trans
	if os.path.exists(old_trans):
		os.remove(old_trans)
	os.rename(args.trans, old_trans)
	trans_lines = list(open(old_trans, "r", encoding="utf-8"))

	orig_new = open(args.orig, "w", encoding="utf-8")
	trans_new = open(args.trans, "w", encoding="utf-8")

	for lo, lt in zip_longest(orig_lines, trans_lines, fillvalue="\n"):
		if lo != lt and not (lo.startswith("label") and lt.startswith("label")):
			orig_new.write(lo)
			trans_new.write(lt)

	orig_new.close()
	trans_new.close()
elif sys.argv[1] == "strip":
	old_file = "old-" + args.file
	if os.path.exists(old_file):
		os.remove(old_file)
	os.rename(args.file, old_file)
	with open(old_file, "r", encoding="utf-8") as r:
		with open(args.file, "w", encoding="utf-8") as w:
			for line in r:
				if len(line.strip()) != 0:
					w.write(line)
elif sys.argv[1] == "trans":
	orig_lines = list(open(args.orig, "r", encoding="utf-8"))
	trans_lines = list(open(args.trans, "r", encoding="utf-8"))

	translates = []

	for ol, tl in zip(orig_lines, trans_lines):
		if tl != ol:
			translates.append((ol.strip(), tl.strip()))

	old_tl = "old-" + args.tl
	if os.path.exists(old_tl):
		os.remove(old_tl)
	os.rename(args.tl, old_tl)
	with open(old_tl, "r", encoding="utf-8") as r:
		with open(args.tl, "w", encoding="utf-8") as w:
			for l in r:
				stripped = l.strip()

				for i in range(len(translates)):
					if stripped.startswith(translates[i][0]):
						w.write("    " + translates[i][1] + "\n")
						translates.pop(i)
						break
				else:
					w.write(l)

	if len(translates):
		print("unused:\n")
		for tl in translates:
			print(tl[0] + "\n" + tl[1] + "\n")
elif sys.argv[1] == "translines":
	import env

	translates = env.translates

	old_file = "old-" + args.file
	if os.path.exists(old_file):
		os.remove(old_file)
	os.rename(args.file, old_file)
	with open(old_file, "r", encoding="utf-8") as r:
		with open(args.file, "w", encoding="utf-8") as w:
			for l in r:
				stripped = l.strip()

				for i in range(len(translates)):
					if stripped.startswith("new \"" + translates[i][0] + "\""):
						w.write("    new \"" + translates[i][1] + "\"\n")
						translates.pop(i)
						break
				else:
					w.write(l)

	if len(translates):
		print("unused:\n")
		for tl in translates:
			print(tl[0] + "\n" + tl[1] + "\n")
else:
	raise OSError("incorrect operation")