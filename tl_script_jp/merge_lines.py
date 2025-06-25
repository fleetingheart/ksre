#!/usr/bin/env python3
# merge_dialogue_lines.py
import re
import sys
from pathlib import Path

# --- шаблоны ---------------------------------------------------------------
PAT_SPEAKER = re.compile(r'^(\w+)\s+"(.*)"\s*$')          # n "text"
PAT_ACTOR   = re.compile(r'^"([^"]+)"\s+"([^"]+)"\s*$')   # "actor1" "text"
PAT_QUOTE   = re.compile(r'^"([^"]+)"\s*$')               # "text"

def ends_with_colon_outside_quotes(line: str) -> bool:
    """
    Проверяет, заканчивается ли строка двоеточием вне кавычек.
    Например: '"text1":' — да; '"text1:"' — нет.
    """
    quote_count = line.count('"')
    return line.strip().endswith(':') and (quote_count % 2 == 0)

def classify(line: str):
    """
    Определяет тип строки и ключ для группировки.
    Возвращает кортеж (тип, key, text) или (None, None, None), если строка не подходит.
    typ  = "speaker" | "actor" | "quote"
    key  = идентификатор, по которому должны совпадать соседние строки
    text = содержимое кавычек
    """
    if m := PAT_SPEAKER.match(line):
        return "speaker", m.group(1), m.group(2)
    if m := PAT_ACTOR.match(line):
        return "actor",  m.group(1), m.group(2)
    if m := PAT_QUOTE.match(line):
        return "quote",  None,       m.group(1)
    return None, None, None


def merge_lines(lines):
    """
    Генератор, возвращающий преобразованные строки.
    """
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        if ends_with_colon_outside_quotes(line):
            yield line
            i += 1
            continue

        typ, key, text = classify(line)
        # Если строка не подходит под один из шаблонов — отдаём как есть
        if typ is None:
            yield line
            i += 1
            continue

        # Начинаем собирать блок из последовательных строк того же типа/ключа
        collected = [text]
        j = i + 1
        while j < n and lines[j].strip():         # пустая строка прерывает
            typ2, key2, text2 = classify(lines[j])
            if typ2 == typ and key2 == key:
                collected.append(text2)
                j += 1
            else:
                break

        # Формируем объединённую строку
        # joined_text = r'\n'.join(collected)
        joined_text = r' '.join(collected)

        if typ == "speaker":
            merged = f'{key} "{joined_text}"\n'
        elif typ == "actor":
            merged = f'"{key}" "{joined_text}"\n'
        else:  # quote
            merged = f'"{joined_text}"\n'

        yield merged
        i = j


def main(src_path: str, dst_path: str | None = None):
    path = Path(src_path)
    out_path = Path(dst_path) if dst_path else path.with_suffix(".merged.rpy")

    with path.open(encoding="utf-8-sig") as f:
        lines = f.readlines()

    merged_lines = list(merge_lines(lines))

    with out_path.open("w", encoding="utf-8", newline="") as f:
        f.writelines(merged_lines)

    print(f"Файл сохранён: {out_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: merge_dialogue_lines.py INPUT.rpy [OUTPUT.rpy]")
    main(*sys.argv[1:])
