#!/usr/bin/env python3
"""Före/efter-kontroll av produktsidans brödsmula (bara läsning, inget skrivs till någon butik).

  # 1. Före-bild från den publika sidan (stickprov ur rådata från länkmätningen, högst 1 anrop/s, robots.txt följs)
  python3 -I shopify-sync/scripts/brodsmula_kontroll.py snapshot --bas https://bestofsports.se \
      --urval-fran rapporter/intern-lankning-bos-2026-11-12/ra-data --antal-per-hubb 8 --ut fore.json
  # 2. Efter-bild: sidor sparade från förhandsgranskningen av temakopian (Spara sida som, HTML) i en katalog,
  #    filnamn = produktens handle + .html
  python3 -I shopify-sync/scripts/brodsmula_kontroll.py fran-filer --katalog efter_html/ --ut efter.json
  # 3. Jämför
  python3 -I shopify-sync/scripts/brodsmula_kontroll.py jamfor fore.json efter.json

Förhandsgranskning av ett opublicerat tema (?preview_theme_id=) är spärrad i robots.txt och kräver inloggning,
så den hämtas aldrig av skriptet. Tester: scripts/test_brodsmula_kontroll.py.
"""
from __future__ import annotations

import argparse
import collections
import gzip
import json
import os
import random
import re
import sys
import time
from urllib.parse import urlsplit

HAR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HAR), "src"))
sys.path.insert(0, HAR)

from bs4 import BeautifulSoup  # noqa: E402

USER_AGENT = "LinkStructureMeasure/1.0 (read-only internal link measurement; no login)"
HUBBAR = ("/collections/varumarke", "/collections/cyklar", "/collections/konditionsutrustning",
          "/collections/gymutrustning", "/collections/kosttillskott", "/collections/ovrig-utrustning")


def extract(html: str | bytes, handle: str, status: int = 200) -> dict:
    """Plockar det som ska vara oförändrat eller förändras kontrollerat."""
    soup = BeautifulSoup(html, "lxml")
    nav = None
    for el in soup.find_all("nav"):
        if "custom-breadcrumb" in (el.get("class") or []) or "breadcrumb" in (el.get("aria-label") or "").lower():
            nav = el
            break
    crumbs = [(a.get("href", ""), a.get_text(" ", strip=True)) for a in nav.find_all("a")] if nav else []
    current = nav.find(class_="breadcrumb-current").get_text(" ", strip=True) if nav and nav.find(class_="breadcrumb-current") else None
    jsonld, jsonld_ok = [], True
    for sc in soup.find_all("script", type="application/ld+json"):
        txt = sc.get_text()
        try:
            data = json.loads(txt)
        except ValueError:
            jsonld_ok = False
            continue
        for item in (data if isinstance(data, list) else [data]):
            if isinstance(item, dict) and item.get("@type") == "BreadcrumbList":
                jsonld.append([(i.get("position"), i.get("name"), i.get("item")) for i in item.get("itemListElement", [])])
    if nav is not None:
        nav.extract()
    other_links = sorted({a["href"].split("?")[0] for a in soup.find_all("a", href=True)} - {""})
    canon = [l.get("href") for l in soup.find_all("link", rel=True) if "canonical" in [r.lower() for r in l.get("rel")]]
    return {"handle": handle, "status": status, "crumbs": crumbs, "current": current, "jsonld_breadcrumbs": jsonld,
            "jsonld_valid": jsonld_ok, "canonical_count": len(canon), "canonical": canon[:1], "h1_count": len(soup.find_all("h1")),
            "other_links": other_links}


def stratified_sample(ra_dir: str, per_hub: int, seed: int = 1) -> list[tuple[str, str]]:
    """Produkter per brödsmulans nuvarande huvudkategori ur rådata: [(handle, hubb)]."""
    opener = (lambda p: gzip.open(p + ".gz", "rt", encoding="utf-8")) if not os.path.exists(os.path.join(ra_dir, "sidor.jsonl")) else (lambda p: open(p, encoding="utf-8"))
    by_hub = collections.defaultdict(list)
    with opener(os.path.join(ra_dir, "sidor.jsonl")) as f:
        for line in f:
            r = json.loads(line)
            if r["status"] != 200 or not r["url"].startswith("/products/"):
                continue
            hubs = [l[0] for l in r["links"] if l[2] == "brodsmula" and l[0].startswith("/collections/")]
            if hubs:
                by_hub[hubs[0]].append(r["url"].split("/products/")[1])
    rng = random.Random(seed)
    out = []
    for hub in sorted(by_hub):
        hs = sorted(by_hub[hub])
        out += [(h, hub) for h in rng.sample(hs, min(per_hub, len(hs)))]
    return out


def compare(before: dict, after: dict, allow_hub_change: bool = False) -> dict:
    """Regler: sidan svarar 200, exakt en canonical, giltig JSON-LD, samma övriga länkar, samma sidnamn sist i brödsmulan,
    Hem och huvudkategori kvar i oförändrad ordning, och högst EN tillagd länk (till en kollektion)."""
    fel, info = [], []
    for h, b in before.items():
        a = after.get(h)
        if a is None:
            fel.append((h, "saknas i efter-bilden"))
            continue
        if a["status"] != 200:
            fel.append((h, f"status {a['status']}"))
        if a["canonical_count"] != 1:
            fel.append((h, f"{a['canonical_count']} canonical-taggar"))
        if not a["jsonld_valid"]:
            fel.append((h, "ogiltig JSON-LD"))
        if a["current"] != b["current"]:
            fel.append((h, f"produktnamn i brödsmulan ändrat: {b['current']!r} -> {a['current']!r}"))
        bc, ac = b["crumbs"], a["crumbs"]
        added = [c for c in ac if c not in bc]
        removed = [c for c in bc if c not in ac]
        hub_change = (allow_hub_change and 1 <= len(removed) <= 2 and all(x[0].startswith("/collections/") for x in removed)
                      and len(added) == 2 and all(x[0].startswith("/collections/") for x in added))
        if hub_change:
            info.append((h, f"huvudlänk byttes: {[x[0] for x in removed]} -> {[x[0] for x in added]}"))
        else:
            if removed:
                fel.append((h, f"länk borttagen ur brödsmulan: {removed}"))
            if len(added) > 1:
                fel.append((h, f"fler än en tillagd länk: {added}"))
            if added and not added[0][0].startswith("/collections/"):
                fel.append((h, f"tillagd länk pekar inte på en kollektion: {added[0]}"))
            if [c for c in ac if c in bc] != [c for c in bc if c in ac]:
                fel.append((h, "ordningen på befintliga länkar ändrad"))
        extra = set(a["other_links"]) - set(b["other_links"])
        missing = set(b["other_links"]) - set(a["other_links"])
        if missing:
            fel.append((h, f"{len(missing)} länkar utanför brödsmulan saknas efter ändringen, t.ex. {sorted(missing)[:3]}"))
        if extra and not added and not hub_change:
            info.append((h, f"{len(extra)} nya länkar utanför brödsmulan (kan vara slumpade rekommendationer)"))
        if a["h1_count"] != b["h1_count"]:
            fel.append((h, f"antal h1 ändrat {b['h1_count']} -> {a['h1_count']}"))
        if added and not hub_change:
            info.append((h, f"tillagd: {added[0][0]}"))
        # schemat ska innehålla minst lika många poster som före och sluta på samma produkt
        bj, aj = b["jsonld_breadcrumbs"], a["jsonld_breadcrumbs"]
        if bj and (not aj or len(aj[0]) < len(bj[0]) or aj[0][-1][1] != bj[0][-1][1]):
            fel.append((h, "BreadcrumbList i strukturerad data försämrad eller ändrad"))
    return {"antal": len(before), "fel": fel, "info": info, "ok": not fel}


def noise(a: dict, b: dict) -> list[str]:
    """Skillnader mellan två hämtningar av samma oförändrade sida (baslinje för slumpmässiga rekommendationer)."""
    return sorted(set(a["other_links"]) ^ set(b["other_links"]))


def cmd_snapshot(args):
    from site_audit.fetch import Fetcher
    from intern_lankning_mat import Robots
    base = args.bas.rstrip("/")
    f = Fetcher(USER_AGENT, 1.0)
    rb = f.fetch(base + "/robots.txt")
    robots = Robots(rb.body.decode("utf-8", "replace") if rb.status == 200 else "")
    if args.handles_fil:
        sample = [(h.strip(), "") for h in open(args.handles_fil, encoding="utf-8") if h.strip()]
    else:
        sample = stratified_sample(args.urval_fran, args.antal_per_hubb)
    snap, brus = {}, {}
    for i, (handle, hub) in enumerate(sample):
        path = "/products/" + handle
        if not robots.allowed(path):
            continue
        r = f.fetch(base + path)
        if r.status != 200:
            snap[handle] = {"handle": handle, "status": r.status, "crumbs": [], "current": None, "jsonld_breadcrumbs": [], "jsonld_valid": True,
                            "canonical_count": 0, "canonical": [], "h1_count": 0, "other_links": []}
            continue
        snap[handle] = dict(extract(r.body, handle), hubb=hub)
        if i < args.brus_antal:
            r2 = f.fetch(base + path)
            brus[handle] = noise(snap[handle], extract(r2.body, handle)) if r2.status == 200 else ["(andra hämtningen misslyckades)"]
    with open(args.ut, "w", encoding="utf-8") as fh:
        json.dump({"tid": time.strftime("%Y-%m-%d %H:%M:%S"), "bas": base, "sidor": snap, "brus": brus}, fh, ensure_ascii=False, indent=1)
    print(f"{len(snap)} sidor sparade i {args.ut}; sidor med slumpskillnader mellan två hämtningar: {sum(1 for v in brus.values() if v)} av {len(brus)}")
    return 0


def cmd_fran_filer(args):
    snap = {}
    for fn in sorted(os.listdir(args.katalog)):
        if fn.endswith(".html"):
            with open(os.path.join(args.katalog, fn), "rb") as fh:
                snap[fn[:-5]] = extract(fh.read(), fn[:-5])
    with open(args.ut, "w", encoding="utf-8") as fh:
        json.dump({"tid": time.strftime("%Y-%m-%d %H:%M:%S"), "bas": "filer", "sidor": snap, "brus": {}}, fh, ensure_ascii=False, indent=1)
    print(f"{len(snap)} sidor lästa från {args.katalog}")
    return 0


def cmd_jamfor(args):
    b = json.load(open(args.fore, encoding="utf-8"))
    a = json.load(open(args.efter, encoding="utf-8"))
    sub = {h: v for h, v in b["sidor"].items() if h in a["sidor"]} if args.bara_gemensamma else b["sidor"]
    res = compare(sub, a["sidor"], allow_hub_change=args.tillat_hubbbyte)
    print(f"Jämförde {res['antal']} sidor. Fel: {len(res['fel'])}. {'GODKÄND' if res['ok'] else 'EJ GODKÄND'}")
    for h, m in res["fel"]:
        print(f"  FEL  {h}: {m}")
    print(f"  Info: {len(res['info'])} noteringar (t.ex. {res['info'][:2]})")
    return 0 if res["ok"] else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("snapshot")
    s.add_argument("--bas", required=True)
    s.add_argument("--urval-fran", default=None)
    s.add_argument("--handles-fil", default=None, help="fil med en produkthandle per rad i stället för stratifierat urval")
    s.add_argument("--antal-per-hubb", type=int, default=8)
    s.add_argument("--brus-antal", type=int, default=6)
    s.add_argument("--ut", required=True)
    s.set_defaults(fn=cmd_snapshot)
    f = sub.add_parser("fran-filer")
    f.add_argument("--katalog", required=True)
    f.add_argument("--ut", required=True)
    f.set_defaults(fn=cmd_fran_filer)
    j = sub.add_parser("jamfor")
    j.add_argument("fore")
    j.add_argument("efter")
    j.add_argument("--tillat-hubbbyte", action="store_true", help="tillåt att ett byte av huvudlänk (en länk ut, två kollektionslänkar in) godkänns (regel v2)")
    j.add_argument("--bara-gemensamma", action="store_true", help="jämför bara sidor som finns i båda bilderna")
    j.set_defaults(fn=cmd_jamfor)
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
