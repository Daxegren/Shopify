#!/usr/bin/env python3
"""Plattformsoberoende sajtskanning (läsande, publika sidor): hittar sidor via sitemap, hämtar ett urval och rapporterar fynd per paket.

Fungerar för vilken webbplats som helst (Shopify, WooCommerce, WordPress, egna system), eftersom den bara läser publik HTML.
Respekterar robots.txt, har paus mellan anrop och identifierar sig. Skanna bara sajter där ägaren har gett sitt godkännande för en
genomgång av den här omfattningen. Sidor som byggs av JavaScript visas som de levereras (utan rendering): fynd där kan bli fler än i
verkligheten, och det skrivs i rapporten.

  python3 sajtskanning.py --url https://exempel.se --ut ~/skanning-exempel [--max-sidor 150] [--paus 1.0]
Skriver sidor.csv, fynd.csv och rapport.md i --ut.
"""
from __future__ import annotations

import argparse
import csv
import random
import statistics
import sys
import time
import urllib.parse
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.robotparser import RobotFileParser

from onsite_kontroll import analyse_page, fetch, locs
from skanning_paket import fynd, rapport_md, till_csv

UA_NAMN = "SajtSkanning"


def sitemap_adresser(bas: str, robots_text: str) -> list[str]:
    rader = [l.split(":", 1)[1].strip() for l in robots_text.splitlines() if l.lower().startswith("sitemap:")]
    return rader or [bas.rstrip("/") + "/sitemap.xml"]


def hitta_sidor(bas: str, robots_text: str, max_nivaer: int = 2, tak: int = 20000):
    """Returnerar (sidor, sitemap_status) där sitemap_status är {adress: status}."""
    status, sidor, kö = {}, [], [(s, 0) for s in sitemap_adresser(bas, robots_text)]
    seda = set()
    while kö and len(sidor) < tak:
        adr, niv = kö.pop(0)
        if adr in seda:
            continue
        seda.add(adr)
        r = fetch(adr)
        status[adr] = r["status"]
        if r["status"] != 200:
            continue
        urls = locs(r["text"])
        barn = [u for u in urls if u.split("?")[0].endswith((".xml", ".xml.gz"))]
        if barn and niv < max_nivaer:
            kö += [(u, niv + 1) for u in barn]
        else:
            sidor += [u for u in urls if not u.split("?")[0].endswith((".xml", ".xml.gz"))]
    return sidor, status


def urval(sidor: list[str], bas: str, n: int, frö: int = 1) -> list[str]:
    start = bas.rstrip("/") + "/"
    unika = list(dict.fromkeys(sidor))
    rest = [u for u in unika if u.rstrip("/") != start.rstrip("/")]
    random.Random(frö).shuffle(rest)
    return [start] + rest[: max(0, n - 1)]


def skanna(bas: str, max_sidor: int = 150, paus: float = 1.0, logg=print):
    """Returnerar (fynd, sidor, kallor, anmarkningar)."""
    bas = bas.rstrip("/")
    anm = []
    rob = fetch(bas + "/robots.txt")
    rp = RobotFileParser()
    rp.parse(rob["text"].splitlines() if rob["status"] == 200 else [])
    ut = []
    if not bas.startswith("https://"):
        ut.append(fynd("inte_https", "Teknik", "Sajten adresseras inte med https", 1, 1, "BRIST", "P3", "Flytta till https och omdirigera", "per sajt"))
    sidor_alla, sm_status = hitta_sidor(bas, rob["text"] if rob["status"] == 200 else "")
    if not any(s == 200 for s in sm_status.values()):
        ut.append(fynd("sitemap_saknas", "Indexering", "Ingen fungerande sitemap hittades", 1, 1, "BRIST", "P3", "Skapa och anmäl sitemap", "per sajt"))
    if rob["status"] == 200 and not rp.can_fetch(UA_NAMN, bas + "/"):
        ut.append(fynd("robots_blockerar", "Indexering", "robots.txt blockerar sajten för alla", 1, 1, "BRIST", "P3", "Rätta robots.txt", "per sajt"))
    mal = urval(sidor_alla, bas, max_sidor)
    logg(f"{len(sidor_alla)} sidor i sitemap, skannar {len(mal)}")
    sidor, hoppade, spar_stopp = [], 0, 0
    for i, u in enumerate(mal, 1):
        if not rp.can_fetch(UA_NAMN, u) and rob["status"] == 200:
            hoppade += 1
            continue
        r = fetch(u)
        rad = {"url": u, "slutlig_url": r["final"], "status": r["status"], "kedja": len(r["chain"]) - 1, "ms": r["ms"], "titel": "", "titel_tecken": 0,
               "beskrivning_tecken": 0, "h1_antal": 0, "canonical": "", "canonical_pekar_pa_sig": False, "canonical_annan_domän": False, "noindex": False,
               "bilder": 0, "bilder_utan_alt": 0, "bilder_tom_alt": 0, "ord": 0, "jsonld": 0, "jsonld_trasiga": 0, "og_bild": False, "html": False}
        ctype = (r.get("headers") or {}).get("content-type", "")
        if r["status"] == 200 and "html" in ctype.lower():
            a = analyse_page(r["text"], r["final"])
            rad.update({"titel": a["titel"], "titel_tecken": a["titel_tecken"], "beskrivning_tecken": a["beskrivning_tecken"], "h1_antal": a["h1_antal"],
                        "canonical": a["canonical"] or "", "canonical_pekar_pa_sig": a["canonical_pekar_pa_sig"], "canonical_annan_domän": a["canonical_annan_domän"],
                        "noindex": a["noindex"], "bilder": a["bilder"], "bilder_utan_alt": a["bilder_utan_alt"], "bilder_tom_alt": a["bilder_tom_alt"],
                        "ord": a["ord_main"], "jsonld": sum(a["jsonld_typer"].values()), "jsonld_trasiga": a["jsonld_trasiga"], "og_bild": a["og_bild"],
                        "html": True})
        sidor.append(rad)
        spar_stopp = spar_stopp + 1 if r["status"] in (429, 403) else 0
        if spar_stopp >= 3:  # bot-kontroll: försök aldrig ta dig förbi den (lärdom 2026-11-12), redovisa luckan
            anm.append(f"Skanningen avbröts efter {i} av {len(mal)} sidor: tre svar i rad med HTTP 429/403 (troligen bot-kontroll). Resterande sidor är inte skannade.")
            break
        if i % 25 == 0:
            logg(f"  {i} av {len(mal)}")
        time.sleep(paus)
    if hoppade:
        anm.append(f"{hoppade} sidor hoppades över eftersom robots.txt inte tillåter dem.")
    html = [s for s in sidor if s["html"]]
    n = len(html)
    ex = lambda lst: [s["url"] for s in lst[:3]]
    icke200 = [s for s in sidor if s["status"] != 200]
    ut.append(fynd("icke_200", "Indexering", "Sidor i sitemap som inte svarar 200", len(icke200), len(sidor), "BRIST", "P3", "Ta bort ur sitemap eller omdirigera", "per sida", ex(icke200)))
    kedja = [s for s in sidor if s["kedja"] > 1]
    ut.append(fynd("kedjor", "Indexering", "Sidor med omdirigeringskedja längre än ett steg", len(kedja), len(sidor), "VARNING", "P3", "Peka sitemap och länkar direkt på slutadressen", "per sida", ex(kedja)))
    om = [s for s in sidor if s["kedja"] >= 1 and s["status"] == 200]
    ut.append(fynd("omdirigerade_i_sitemap", "Indexering", "Sitemap-adresser som omdirigerar", len(om), len(sidor), "VARNING", "P3", "Lista slutadresser i sitemap", "per sida", ex(om)))
    if n:
        noi = [s for s in html if s["noindex"]]
        ut.append(fynd("noindex_i_sitemap", "Indexering", "Sidor med noindex som finns i sitemap", len(noi), n, "BRIST", "P3", "Ta bort noindex eller sidan ur sitemap", "per sida", ex(noi)))
        sakn = [s for s in html if not s["canonical"]]
        ut.append(fynd("canonical_saknas", "Canonical", "Sidor utan canonical", len(sakn), n, "VARNING", "P3", "Lägg till canonical", "per mall", ex(sakn)))
        ej = [s for s in html if s["canonical"] and not s["canonical_pekar_pa_sig"] and not s["canonical_annan_domän"]]
        ut.append(fynd("canonical_ej_sjalv", "Canonical", "Sidor vars canonical pekar på en annan sida", len(ej), n, "VARNING", "P3", "Kontrollera att det är avsiktligt", "per sida", ex(ej)))
        ann = [s for s in html if s["canonical_annan_domän"]]
        ut.append(fynd("canonical_annan_domän", "Canonical", "Sidor med canonical på annan domän", len(ann), n, "BRIST", "P3", "Rätta canonical", "per mall", ex(ann)))
        ut.append(fynd("titel_saknas", "Metadata", "Sidor utan titel", sum(1 for s in html if not s["titel"]), n, "BRIST", "P4", "Skriv titel", "per sida", ex([s for s in html if not s["titel"]])))
        ut.append(fynd("titel_lang", "Metadata", "Titlar över 60 tecken", sum(1 for s in html if s["titel_tecken"] > 60), n, "VARNING", "P4", "Korta titeln", "per sida"))
        ut.append(fynd("titel_kort", "Metadata", "Titlar under 15 tecken", sum(1 for s in html if 0 < s["titel_tecken"] < 15), n, "VARNING", "P4", "Skriv beskrivande titel", "per sida"))
        t = Counter(s["titel"] for s in html if s["titel"])
        dub = [k for k, v in t.items() if v > 1]
        ut.append(fynd("titel_dubbletter", "Metadata", "Sidor som delar titel med en annan sida (i urvalet)", sum(t[k] for k in dub), n, "VARNING", "P4", "Gör titlarna unika", "per sida", dub[:3]))
        ut.append(fynd("beskrivning_saknas", "Metadata", "Sidor utan metabeskrivning", sum(1 for s in html if s["beskrivning_tecken"] == 0), n, "BRIST", "P4", "Skriv metabeskrivning", "per sida"))
        ut.append(fynd("beskrivning_lang", "Metadata", "Metabeskrivningar över 160 tecken", sum(1 for s in html if s["beskrivning_tecken"] > 160), n, "VARNING", "P4", "Korta beskrivningen", "per sida"))
        h1 = [s for s in html if s["h1_antal"] != 1]
        ut.append(fynd("h1", "Struktur", "Sidor utan exakt en H1", len(h1), n, "VARNING", "P4", "Ge varje sida en H1", "per mall", ex(h1)))
        b = sum(s["bilder"] for s in html)
        bu = sum(s["bilder_utan_alt"] + s["bilder_tom_alt"] for s in html)
        ut.append(fynd("alt", "Bilder", "Bilder utan alt-text", bu, b, "VARNING", "P4", "Sätt alt-text", "per 1 000 bilder"))
        tunna = [s for s in html if s["ord"] < 150 and s["url"].rstrip("/") != bas]
        ut.append(fynd("tunt", "Innehåll", "Sidor med under 150 ord", len(tunna), n, "VARNING", "P4", "Utveckla innehållet eller slå ihop sidor", "per sida", ex(tunna)))
        ut.append(fynd("schema_saknas", "Schema", "Sidor utan strukturerad data (JSON-LD)", sum(1 for s in html if s["jsonld"] == 0), n, "VARNING", "P3", "Lägg till relevant schema", "per mall"))
        ut.append(fynd("schema_trasigt", "Schema", "Sidor med trasig JSON-LD", sum(1 for s in html if s["jsonld_trasiga"]), n, "BRIST", "P3", "Rätta schemat", "per mall"))
        ut.append(fynd("og_bild", "Delning", "Sidor utan delningsbild (og:image)", sum(1 for s in html if not s["og_bild"]), n, "VARNING", "P4", "Lägg till og:image", "per mall"))
        ms = [s["ms"] for s in html]
        med = int(statistics.median(ms)) if ms else 0
        ut.append(fynd("svarstid", "Hastighet", f"Median svarstid för HTML {med} ms (över 1 500 ms räknas som fynd)", 1 if med > 1500 else 0, 1, "VARNING", "P3",
                       "Undersök serversvar och cache", "per sajt"))
    anm += [f"Urval: {len(sidor)} av {len(sidor_alla)} sidor i sitemap (slumpmässigt, frö 1). Andelar gäller urvalet.",
            "Sidor hämtas som de levereras, utan JavaScript-rendering. Core Web Vitals och mobilvänlighet mäts inte här.",
            "Rapporten är ett underlag för bedömning, inte en slutsats: varje fynd bör granskas av en människa."]
    return [f for f in ut if f["antal"] > 0 or f["allvar"] == "INFO"], sidor, [f"publika sidor på {bas}"], anm


def skriv_ut(katalog: str, bas: str, fl, sidor, kallor, anm):
    ut = Path(katalog).expanduser(); ut.mkdir(parents=True, exist_ok=True)
    kol = ["url", "slutlig_url", "status", "kedja", "ms", "titel", "titel_tecken", "beskrivning_tecken", "h1_antal", "canonical", "canonical_pekar_pa_sig",
           "canonical_annan_domän", "noindex", "bilder", "bilder_utan_alt", "bilder_tom_alt", "ord", "jsonld", "jsonld_trasiga", "og_bild"]
    with open(ut / "sidor.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=kol, delimiter=";", extrasaction="ignore"); w.writeheader(); w.writerows(sidor)
    (ut / "fynd.csv").write_text(till_csv(fl), encoding="utf-8")
    (ut / "rapport.md").write_text(rapport_md(urllib.parse.urlparse(bas).netloc, date.today().isoformat(), kallor, fl, anm), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--ut", required=True)
    ap.add_argument("--max-sidor", type=int, default=150)
    ap.add_argument("--paus", type=float, default=1.0)
    a = ap.parse_args()
    fl, sidor, kallor, anm = skanna(a.url, a.max_sidor, a.paus)
    skriv_ut(a.ut, a.url, fl, sidor, kallor, anm)
    brist = sum(1 for f in fl if f["allvar"] == "BRIST")
    print(f"SAMMANFATTNING {a.url}: {brist} brister, {sum(1 for f in fl if f['allvar'] == 'VARNING')} varningar, {len(sidor)} sidor skannade. Rapport: {a.ut}/rapport.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
