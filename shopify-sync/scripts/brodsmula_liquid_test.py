#!/usr/bin/env python3
"""Kör temans verkliga Liquid-kod för brödsmulan (blocket 'type' i sections/main-product.liquid) mot alla produkter och
jämför med simuleringen i brodsmula_regel_sim.py. Kräver python-liquid (pip install python-liquid), inget nätverk, ingen skrivning.

  python3 -I shopify-sync/scripts/brodsmula_liquid_test.py --tema-fil <main-product.liquid> --regel v2 \
      --ra rapporter/intern-lankning-bos-2026-11-12/ra-data --meny shopify-sync/config/bos-main-menu-2026-11-13.json
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import sys

HAR = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("sim", os.path.join(HAR, "brodsmula_regel_sim.py"))
sim = importlib.util.module_from_spec(spec)
sys.modules["sim"] = sim
spec.loader.exec_module(sim)


def type_block(text: str) -> str:
    """Texten för blocket 'type' (från när-raden till nästa when/endcase)."""
    lines = text.split("\n")
    s = next(i for i, l in enumerate(lines) if "{%- when 'type' -%}" in l)
    e = next(i for i in range(s + 1, len(lines)) if re.search(r"\{%-?\s*(when|endcase)", lines[i]))
    return "\n".join(lines[s + 1:e])


def link_objects(tree: dict) -> list:
    def mk(handle, kids):
        return {"title": handle, "type": "collection_link", "url": f"/collections/{handle}", "object": {"handle": handle},
                "links": [mk(h, k) for h, k in kids.items()]}
    return [mk(h, k) for h, k in tree.items()]


def render(env_tmpl, links, collections: set, ptype="Cyklar", title="Testprodukt") -> list:
    out = env_tmpl.render({"linklists": {"main-menu": {"links": links}}, "routes": {"root_url": "/"}, "block": {"shopify_attributes": ""},
                           "product": {"collections": [{"handle": h} for h in sorted(collections)], "type": ptype, "title": title,
                                       "handle": "p", "url": "/products/p"}})
    nav = re.search(r"<nav class=\"custom-breadcrumb\".*?</nav>", out, re.S)
    if not nav:
        return None
    return re.findall(r'<a href="([^"]+)"', nav.group(0))


def main(argv=None):
    from liquid import Environment
    ap = argparse.ArgumentParser()
    ap.add_argument("--tema-fil", required=True)
    ap.add_argument("--regel", choices=["v1", "v2"], required=True)
    ap.add_argument("--ra", required=True)
    ap.add_argument("--meny", required=True)
    ap.add_argument("--max", type=int, default=0)
    ap.add_argument("--ut", default=None, help="skriv avvikelser som JSON")
    a = ap.parse_args(argv)
    tree = json.load(open(a.meny, encoding="utf-8"))
    member, titles = sim.load_membership(a.ra)
    tmpl = Environment().parse(type_block(open(a.tema_fil, encoding="utf-8").read()))
    links = link_objects(tree)
    rule = sim.rule_v1 if a.regel == "v1" else sim.rule_v2
    bad, n = [], 0
    for h in sorted(titles):
        if a.max and n >= a.max:
            break
        n += 1
        m = member.get(h, set())
        got = render(tmpl, links, m, ptype="", title=titles[h] or h)
        exp = rule(tree, m)
        # förväntad brödsmula: Hem, huvudgren (v1: första toppnivå som produkten tillhör; v2: valets egen), val
        main_v1 = next((t for t in tree if t in m), None)
        exp_main = (exp[0] if exp else main_v1)
        exp_links = ["/"] + ([f"/collections/{exp_main}"] if exp_main else []) + ([f"/collections/{exp[1]}"] if exp else [])
        got_cols = [g for g in (got or []) if not g.startswith("/search")]
        if got_cols != exp_links:
            bad.append({"produkt": h, "samlingar": sorted(m)[:8], "fick": got_cols, "forvantat": exp_links})
    print(f"{a.regel}: {n} produkter, {len(bad)} avvikelser mellan Liquid-koden och simuleringen")
    for b in bad[:15]:
        print("  ", b)
    if a.ut:
        json.dump(bad, open(a.ut, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
