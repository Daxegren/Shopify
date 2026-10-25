#!/usr/bin/env python3
"""Jämför genomlysningens kritiska omdirigeringsfynd med de omdirigeringar vi redan granskat (rapporter/redirects_granskade.csv).

Svarar på: hur många av de trasiga omdirigeringarna är redan åtgärdade i vår granskade fil (men inte i Shopify), och vilka är nya?

  gcloud storage cat gs://gorilla-sports-data-site-audit/audits/gorillasports-se/latest/findings.jsonl \
    | python3 scripts/redirect_jamforelse.py --granskade ../rapporter/redirects_granskade.csv

Bara läsning. Skriver en CSV med de nya (ogranskade) fynden till --ut (standard redirects_nya.csv)."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from urllib.parse import urlsplit, unquote

CHECKS = ("redirect_target_missing", "redirect_to_error")


def path_of(url: str) -> str:
    return unquote(urlsplit(url).path).rstrip("/") or "/"


def load_reviewed(path: str) -> dict[str, str]:
    out: dict[str, str] = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.reader(f):
            if len(row) >= 2 and row[0].startswith("/"):
                out[unquote(row[0]).rstrip("/") or "/"] = row[1]
    return out


def classify(findings: list[dict], reviewed: dict[str, str]) -> tuple[list[dict], list[dict]]:
    covered, new = [], []
    for f in findings:
        if f.get("check") not in CHECKS:
            continue
        src = path_of(f.get("url", ""))
        ev = f.get("evidence") or {}
        now = ev.get("target") or (ev.get("chain") or [""])[-1]
        item = {"kalla": src, "check": f["check"], "nuvarande_mal": now, "granskat_mal": reviewed.get(src, "")}
        (covered if src in reviewed else new).append(item)
    return covered, new


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--granskade", required=True)
    p.add_argument("--ut", default="redirects_nya.csv")
    args = p.parse_args(argv)
    findings = [json.loads(l) for l in sys.stdin if l.strip()]
    reviewed = load_reviewed(args.granskade)
    covered, new = classify(findings, reviewed)
    total = len(covered) + len(new)
    print(f"Kritiska omdirigeringsfynd: {total}. Redan i vår granskade fil: {len(covered)}. Nya (ogranskade): {len(new)}.")
    print("\nRedan granskade (källa, nuvarande mål i Shopify, vårt granskade mål):")
    for c in covered[:15]:
        print(f"  {c['kalla']}  ->  {c['nuvarande_mal']}   (granskat: {c['granskat_mal']})")
    if len(covered) > 15:
        print(f"  … och {len(covered) - 15} till")
    with open(args.ut, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["kalla", "check", "nuvarande_mal", "granskat_mal"])
        w.writeheader()
        w.writerows(new)
    print(f"\nNya fynd skrivna till {args.ut}. De första:")
    for c in new[:15]:
        print(f"  {c['kalla']}  ->  {c['nuvarande_mal']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
