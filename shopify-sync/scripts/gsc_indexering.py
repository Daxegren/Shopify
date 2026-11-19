#!/usr/bin/env python3
"""Indexeringskontroll via Search Console URL Inspection API (bara läsning) för kollektionerna vi ändrat.

Skriver ~/gsc_indexering_<datum>.csv med en rad per sida: verdict, täckning, senaste genomsökning och om Googles canonical = vår.
Körs idag och om en vecka för jämförelse. Kvot: 2 000 anrop per dag och egendom; detta använder ca 45.
Inloggning: din Google-inloggning i Cloud Shell (samma som gsc_baslinje.py). Inga nycklar i filen.
  python3 gsc_indexering.py sc-domain:workoutbrands.com
"""
import argparse, csv, datetime as dt, os, sys, time

from gsc_export import session
from gsc_baslinje import ANDRADE, KONTROLL

API = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"
EXTRA = ["present-till-honom", "present-till-henne"]
BAS = "https://workoutbrands.com/collections/"
KOLUMNER = ["url", "grupp", "verdict", "coverageState", "indexingState", "pageFetchState", "robotsTxtState", "lastCrawlTime",
            "googleCanonical", "userCanonical", "canonical_samma"]


def rad(url, grupp, svar):
    i = (svar.get("inspectionResult") or {}).get("indexStatusResult") or {}
    g, u = i.get("googleCanonical", ""), i.get("userCanonical", "")
    return {"url": url, "grupp": grupp, "verdict": i.get("verdict", ""), "coverageState": i.get("coverageState", ""),
            "indexingState": i.get("indexingState", ""), "pageFetchState": i.get("pageFetchState", ""),
            "robotsTxtState": i.get("robotsTxtState", ""), "lastCrawlTime": (i.get("lastCrawlTime") or "")[:10],
            "googleCanonical": g, "userCanonical": u, "canonical_samma": ("ja" if g and g == u else ("nej" if g else ""))}


def urls():
    return [(BAS + h, "andrad") for h in ANDRADE + EXTRA] + [(BAS + h, "kontroll") for h in KONTROLL]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site")
    ap.add_argument("--ut")
    a = ap.parse_args()
    s = session()
    ut = os.path.expanduser(a.ut or f"~/gsc_indexering_{dt.date.today()}.csv")
    rader, fel_i_rad = [], 0
    for n, (u, g) in enumerate(urls(), 1):
        r = s.post(API, json={"inspectionUrl": u, "siteUrl": a.site, "languageCode": "sv"}, timeout=120)
        if r.status_code == 429:
            print("Kvoten är slut för i dag (429). Försök igen i morgon."); break
        if r.status_code != 200:
            fel_i_rad += 1
            print(f"Fel {r.status_code} för {u}: {r.text[:600]}"); rader.append(rad(u, g, {}))
            if fel_i_rad >= 3:
                sys.exit("STOPP: tre fel i rad, inget skrivs. Klistra in felmeddelandet ovan.")
            continue
        fel_i_rad = 0
        rader.append(rad(u, g, r.json()))
        if n % 10 == 0:
            print(f"  {n} av {len(urls())}")
        time.sleep(0.4)
    with open(ut, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=KOLUMNER, delimiter=";"); w.writeheader(); w.writerows(rader)
    from collections import Counter
    print(Counter((r["grupp"], r["coverageState"]) for r in rader))
    print("KLART ->", ut)


if __name__ == "__main__":
    main()
