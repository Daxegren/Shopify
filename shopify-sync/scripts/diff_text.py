#!/usr/bin/env python3
"""Jämför två texter tecken för tecken och skriver ut bara det som skiljer. Används efter varje ändring i Shopify:
spara texten före ändringen i en fil, läs tillbaka texten efteråt och kontrollera att bara de godkända ändringarna finns kvar.

  python3 scripts/diff_text.py rapporter/shopify-original-2026-10-22/kollektion-spinningcykel.html nuvarande.html
"""

from __future__ import annotations

import difflib
import sys


def changes(before: str, after: str, width: int = 120) -> list[tuple[str, str, str]]:
    """Lista med (typ, före, efter) för alla avsnitt som skiljer. Typ är replace, delete eller insert."""
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, before, after, autojunk=False).get_opcodes():
        if tag != "equal":
            out.append((tag, before[i1:i2][:width], after[j1:j2][:width]))
    return out


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__)
        return 2
    a, b = (open(p, encoding="utf-8").read() for p in argv[1:])
    found = changes(a, b)
    for tag, x, y in found:
        print(f"{tag}: {x!r} -> {y!r}")
    print(f"{len(found)} avvikelser ({len(a)} -> {len(b)} tecken)")
    return 0 if not found else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
