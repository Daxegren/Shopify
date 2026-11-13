#!/usr/bin/env python3
"""Simulerar brödsmulans kollektionsval (regel v1 = publicerad kod, regel v2 = förslag) över alla produkter i rådata
från länkmätningen. Bara läsning, inget nätverk, inget skrivs till Shopify.

  python3 -I shopify-sync/scripts/brodsmula_regel_sim.py --ra rapporter/intern-lankning-bos-2026-11-12/ra-data \
      --meny shopify-sync/config/bos-main-menu-2026-11-13.json --ut rapporter/intern-lankning-bos-2026-11-12/brodsmula-sim

Produktens kollektionstillhörighet härleds ur kollektionssidornas produktlistor (alla sidor i pagineringen). Det är en
approximation av medlemskapet i Shopify; v1 kontrolleras mot verkliga brödsmulor i före/efter-bilderna.
Tester: scripts/test_brodsmula_regel_sim.py.
"""
from __future__ import annotations

import argparse
import collections
import csv
import gzip
import json
import os
import re
import sys

BRAND_TOP = "varumarke"
# Menyposter som pekar på samma kollektion som en huvudgren (Gymtillbehör > "Tillbehör" -> ovrig-utrustning)
HUB_ALIAS = {"ovrig-utrustning", "tillbehor"}  # "tillbehor" = generisk samlingskollektion (Gymtillbehör), ger fel hubb för t.ex. cykeltillbehör


def flatten(tree: dict):
    """[(toppnivå, nivå, handle, förälder)] i menyordning."""
    out = []
    for top, kids in tree.items():
        for kid, grand in kids.items():
            out.append((top, 2, kid, top))
            for g in grand:
                out.append((top, 3, g, kid))
    return out


def rule_v1(tree: dict, member: set) -> tuple | None:
    """Publicerad kod: första toppnivå som produkten tillhör; sedan första barn som produkten tillhör och, under det barnet,
    första barnbarn som produkten tillhör. Ger (toppnivå, vald) eller None."""
    main = next((t for t in tree if t in member), None)
    if main is None:
        return None
    sub = None
    for child, grand in tree[main].items():
        if child in member:
            sub = child
            for g in grand:
                if g in member:
                    sub = g
                    break
            break
    return (main, sub) if sub else None


def rule_v2(tree: dict, member: set) -> tuple | None:
    """Förslag (konservativt): behåll v1 när den redan ger en ämneslänk. Annars sök ämneskollektioner i hela trädet (utanför
    Varumärken, och inte menyposter som pekar på en huvudgren); djupast först, därefter menyordning; hubben som visas blir
    valets egen toppnivå. Finns ingen ämneskollektion gäller v1 (varumärkeslänk bara när första huvudgrenen är Varumärken)."""
    r1 = rule_v1(tree, member)
    if r1 and r1[0] != BRAND_TOP:
        return r1
    hubs = set(tree)
    cands = [c for c in flatten(tree) if c[2] in member and c[0] != BRAND_TOP and c[2] not in hubs and c[2] not in HUB_ALIAS]
    if cands:
        best = max(enumerate(cands), key=lambda ic: (ic[1][1], -ic[0]))[1]
        return (best[0], best[2])
    return r1


def load_membership(ra_dir: str):
    """handle -> set(kollektionshandles) ur kollektionssidornas produktlistor; samt produkttitlar."""
    p = os.path.join(ra_dir, "sidor.jsonl")
    op = (lambda: open(p, encoding="utf-8")) if os.path.exists(p) else (lambda: gzip.open(p + ".gz", "rt", encoding="utf-8"))
    member = collections.defaultdict(set)
    titles, status = {}, {}
    with op() as f:
        for line in f:
            r = json.loads(line)
            u = r["url"]
            if u.startswith("/products/") and r["status"] == 200:
                titles[u[10:]] = r.get("h1") or r.get("title") or ""
                status[u[10:]] = True
            if r["type"] == "collection" and r["status"] == 200:
                col = u.split("?")[0].replace("/collections/", "")
                for l in r["links"]:
                    t = l[0].split("?")[0]
                    if l[2] in ("innehall",) and t.startswith("/products/"):
                        member[t[10:]].add(col)
    return member, titles


def words(s: str) -> set:
    return {w[:6] for w in re.findall(r"[a-zåäö0-9]{4,}", s.lower())}


def suggest(title: str, tree: dict, top: str | None) -> str:
    """Grov förslagsgenerator: menykollektion vars namn delar ordstam med produkttiteln (heuristik, ska granskas)."""
    tw = words(title)
    best = []
    for t, lvl, h, parent in flatten(tree):
        if t == BRAND_TOP:
            continue
        hw = words(h.replace("-", " "))
        if hw and hw <= tw:
            best.append((lvl, h))
    return ", ".join(h for _, h in sorted(best, reverse=True)[:2])


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ra", required=True)
    ap.add_argument("--meny", required=True)
    ap.add_argument("--ut", required=True)
    ap.add_argument("--meny-fore", default=None, help="menyträd utan Hybridcykel, för att kontrollera v1 mot verkliga brödsmulor")
    ap.add_argument("--verklig", default=None, help="brodsmula-fore.json + efter-bild att kontrollera v1 mot")
    a = ap.parse_args(argv)
    tree = json.load(open(a.meny, encoding="utf-8"))
    member, titles = load_membership(a.ra)
    os.makedirs(a.ut, exist_ok=True)
    rows, cnt = [], collections.Counter()
    for h in sorted(titles):
        m = member.get(h, set())
        v1, v2 = rule_v1(tree, m), rule_v2(tree, m)
        hub = next((t for t in tree if t in m), "")
        k = ("v1_ja" if v1 else "v1_nej") + "/" + ("v2_ja" if v2 else "v2_nej")
        cnt[k] += 1
        rows.append({"produkt": h, "titel": titles[h], "huvudgren_idag": hub, "antal_kollektioner": len(m), "v1_valt": v1[1] if v1 else "", "v2_toppniva": v2[0] if v2 else "", "v2_valt": v2[1] if v2 else "",
                     "v2_ar_varumarke": bool(v2 and v2[0] == BRAND_TOP), "forslag_saknad_kollektion": "" if (v2 and v2[0] != BRAND_TOP) else suggest(titles[h], tree, hub)})
    with open(os.path.join(a.ut, "produkter.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter=";")
        w.writeheader()
        for r in rows:
            w.writerow({k: ("ja" if v is True else "nej" if v is False else v) for k, v in r.items()})
    topic_v1 = sum(1 for r in rows if r["v1_valt"])
    topic_v2 = sum(1 for r in rows if r["v2_valt"] and not r["v2_ar_varumarke"])
    brand_v2 = sum(1 for r in rows if r["v2_ar_varumarke"])
    none_v2 = sum(1 for r in rows if not r["v2_valt"])
    per_hub = collections.defaultdict(lambda: [0, 0, 0, 0])
    for r in rows:
        x = per_hub[r["huvudgren_idag"] or "(ingen)"]
        x[0] += 1
        x[1] += 1 if r["v1_valt"] else 0
        x[2] += 1 if (r["v2_valt"] and not r["v2_ar_varumarke"]) else 0
        x[3] += 1 if not r["v2_valt"] else 0
    res = {"produkter": len(rows), "v1_med_underkollektion": topic_v1, "v2_amneskollektion": topic_v2, "v2_bara_varumarke": brand_v2, "v2_ingen": none_v2,
           "per_huvudgren": {k: {"produkter": v[0], "v1": v[1], "v2_amne": v[2], "v2_ingen_eller_bara_varumarke": v[0] - v[2]} for k, v in sorted(per_hub.items())},
           "utan_medlemskap_i_nagon_kollektion_funnen": sum(1 for r in rows if r["antal_kollektioner"] == 0)}
    json.dump(res, open(os.path.join(a.ut, "sammanstallning.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(res, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
