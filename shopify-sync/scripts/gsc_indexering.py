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


def hamta(s, url, site, forsok=3):
    """Ett anrop med omförsök vid timeout/nätverksfel. Returnerar (status, svar eller text)."""
    for n in range(1, forsok + 1):
        try:
            r = s.post(API, json={"inspectionUrl": url, "siteUrl": site, "languageCode": "sv"}, timeout=60)
            return r.status_code, (r.json() if r.status_code == 200 else r.text)
        except Exception as e:  # timeout, nätverksfel
            if n == forsok:
                return 0, f"{type(e).__name__}: {e}"
            time.sleep(3 * n)


def las_klara(sokvag):
    if not os.path.exists(sokvag):
        return {}
    return {r["url"]: r for r in csv.DictReader(open(sokvag, encoding="utf-8"), delimiter=";") if r.get("verdict")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site")
    ap.add_argument("--ut")
    a = ap.parse_args()
    s = session()
    ut = os.path.expanduser(a.ut or f"~/gsc_indexering_{dt.date.today()}.csv")
    klara = las_klara(ut)
    if klara:
        print(f"Återupptar: {len(klara)} sidor är redan klara i {ut}")
    rader, fel_i_rad, lista = [], 0, urls()
    for n, (u, g) in enumerate(lista, 1):
        if u in klara:
            rader.append(klara[u]); continue
        status, svar = hamta(s, u, a.site)
        if status == 429:
            print("Kvoten är slut för i dag (429). Försök igen i morgon."); break
        if status != 200:
            fel_i_rad += 1
            print(f"Fel {status} för {u}: {str(svar)[:600]}"); rader.append(rad(u, g, {}))
            if fel_i_rad >= 3:
                skriv(ut, rader)
                sys.exit("STOPP: tre fel i rad. Det som är klart är sparat; kör samma kommando igen för att återuppta.")
            continue
        fel_i_rad = 0
        rader.append(rad(u, g, svar))
        if n % 10 == 0:
            print(f"  {n} av {len(lista)}")
            skriv(ut, rader)
        time.sleep(0.4)
    skriv(ut, rader)
    from collections import Counter
    print(Counter((r["grupp"], r["coverageState"]) for r in rader))
    print("KLART ->", ut)


def skriv(ut, rader):
    with open(ut, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=KOLUMNER, delimiter=";"); w.writeheader(); w.writerows(rader)


if __name__ == "__main__":
    main()
