#!/usr/bin/env python3
# https://stackoverflow.com/a/79296718
# Licensed under CC-BY-SA 4.0

import re
import sys
from pathlib import Path
from typing import List, Tuple

def get_shortcut_id(appid: int):
    return (appid << 32) | 0x02000000

def get_non_steam_games(steam_config_path) -> List[Tuple[str, str, str, str]]:
    shortcut_path = steam_config_path / 'shortcuts.vdf'
    if not shortcut_path.is_file():
        print(f"No non-steam games shortcut file found at {shortcut_path}. Assuming no non-steam games are installed.")
        return []
    shortcut_bytes = shortcut_path.read_bytes()

    # Using regex to extract the shortcut information, rather than parsing it based on
    # the binary format
    game_pattern = re.compile(b"\x00\x02appid\x00(.{4})\x01appname\x00([^\x08]+?)\x00\x01exe\x00([^\x08]+?)\x00\x01.+?\x00tags\x00(?:\x01([^\x08]+?)|)\x08\x08", flags=re.DOTALL | re.IGNORECASE)
    games = []
    for game_match in game_pattern.findall(shortcut_bytes):
        id = int.from_bytes(game_match[0], byteorder='little', signed=False)
        name = game_match[1].decode('utf-8')
        target = game_match[2].decode('utf-8')
        games.append((name, target, str(id), str(get_shortcut_id(id))))

    return games

for id, dir in enumerate(sys.argv[1:]):
    for game in get_non_steam_games(Path(dir)):
        print(game)
