#!/usr/bin/env python3
"""Search Console-baslinje för Workout Brands (bara läsning). Körs idag och igen om en vecka för jämförelse.

Skriver till --ut (standard ~/gsc_baslinje_<datum>/):
  vecka_sida.csv      sidor per vecka (16 veckor), alla sidor
  dag_totalt.csv      totalt per dag (90 dagar)
  land.csv, enhet.csv sista 28 dagarna
  sida_fraga_28d.csv  sida x sökfråga, sista 28 dagarna, för kollektionerna vi ändrat (grupp andrad) och kontrollgrupp
  info.json           datum för körningen och grupperna
Inloggning: din egen Google-inloggning i Cloud Shell (samma som gsc_export.py). Inga nycklar i filen.
  python3 gsc_baslinje.py sc-domain:workoutbrands.com
"""
import argparse, csv, datetime as dt, json, os, sys
from urllib.parse import quote

from gsc_export import session, API, PAGE

ANDRADE = ["astani-alla-produkter", "billiga-t-shirts-herr", "dangerous-dngrs-herr", "def-herr", "flexfit-keps", "gymvaska-1",
           "hoodie-oversized-herr", "kepsar", "klader-till-dop-dam", "linne-herr", "long-sleeve-man", "musee-mimmi-pigg-klader-herr-dam",
           "oversized-klader-herr", "relode", "rocawear-herr", "rocawear-herr-och-dam", "southpole-jeans", "starter-black-label-man",
           "streetwear-barn", "wob-alla-produkter", "yoga-pants", "hoodie-oversized-dam", "snapback-keps", "ryggsack", "mister-tee-hoodie-herr",
           "mj-gonzales-herr", "billiga-byxor-herr", "klader-till-examen-herr", "hoodie-kvinna", "klader-till-skolavslutning-dam",
           "kamouflage-klader-herr-1", "retroinspirerade-klader-herr", "lader-konstlader-jacka-man", "ecko-unltd-herr",
           "present-till-18-arig-kille", "hoodie-man"]
KONTROLL = ["klader-till-dop-herr", "cayler-sons-man", "klader-till-examen-dam", "thug-life-herr-och-dam", "turtleneck-dam"]


def veckor(slut, antal=16):
    """Lista (start, slut) med sjudagarsperioder bakåt från slut (inklusive), äldst först."""
    ut = []
    for i in range(antal):
        s = slut - dt.timedelta(days=7 * i + 6)
        e = slut - dt.timedelta(days=7 * i)
        ut.append((s, e))
    return ut[::-1]


def regex_for(handles):
    return "/collections/(" + "|".join(h.replace("-", "\\-") for h in handles) + ")(\\?.*)?$"


def hamta(s, site, dims, start, end, filt=None, tak=100000):
    rader, offset = [], 0
    while offset < tak:
        body = {"startDate": str(start), "endDate": str(end), "dimensions": dims, "rowLimit": PAGE, "startRow": offset, "dataState": "final"}
        if filt:
            body["dimensionFilterGroups"] = [{"filters": [filt]}]
        r = s.post(API.format(site=quote(site, safe="")), json=body, timeout=120)
        if r.status_code != 200:
            sys.exit(f"Fel {r.status_code} för {dims}: {r.text[:300]}")
        del_ = r.json().get("rows", [])
        rader += del_
        if len(del_) < PAGE:
            break
        offset += PAGE
    return rader


def skriv(sokvag, kolumner, rader):
    with open(sokvag, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(kolumner + ["klick", "visningar", "ctr", "position"])
        for pre, r in rader:
            w.writerow(list(pre) + list(r["keys"]) + [int(r["clicks"]), int(r["impressions"]), round(r["ctr"], 4), round(r["position"], 2)])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site")
    ap.add_argument("--ut")
    a = ap.parse_args()
    idag = dt.date.today()
    ut = os.path.expanduser(a.ut or f"~/gsc_baslinje_{idag}")
    os.makedirs(ut, exist_ok=True)
    s = session()
    slut = idag - dt.timedelta(days=3)
    print("Totalt per dag (90 dagar)")
    skriv(f"{ut}/dag_totalt.csv", ["datum"], [((), r) for r in hamta(s, a.site, ["date"], slut - dt.timedelta(days=89), slut)])
    print("Land och enhet (28 dagar)")
    d28 = slut - dt.timedelta(days=27)
    skriv(f"{ut}/land.csv", ["land"], [((), r) for r in hamta(s, a.site, ["country"], d28, slut)])
    skriv(f"{ut}/enhet.csv", ["enhet"], [((), r) for r in hamta(s, a.site, ["device"], d28, slut)])
    print("Sida x sökfråga för kollektionerna (28 dagar)")
    rader = []
    for grupp, hs in (("andrad", ANDRADE), ("kontroll", KONTROLL)):
        for r in hamta(s, a.site, ["page", "query"], d28, slut, {"dimension": "page", "operator": "includingRegex", "expression": regex_for(hs)}):
            rader.append(((grupp,), r))
    skriv(f"{ut}/sida_fraga_28d.csv", ["grupp", "sida", "fraga"], rader)
    print(f"  {len(rader)} rader")
    print("Sidor per vecka (16 veckor)")
    vr = []
    for st, en in veckor(slut):
        part = hamta(s, a.site, ["page"], st, en)
        print(f"  {st}..{en}: {len(part)} sidor")
        vr += [((str(st),), r) for r in part]
    skriv(f"{ut}/vecka_sida.csv", ["veckostart", "sida"], vr)
    json.dump({"kord": str(idag), "data_till": str(slut), "andrade_kollektioner": ANDRADE, "kontroll": KONTROLL,
               "andringar": "SEO-titlar 2026-11-18 och 2026-11-19, se ANDRINGSLOGG"}, open(f"{ut}/info.json", "w"), ensure_ascii=False, indent=1)
    print("KLART ->", ut)


if __name__ == "__main__":
    main()
