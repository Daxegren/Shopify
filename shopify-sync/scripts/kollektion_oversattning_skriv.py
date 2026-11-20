#!/usr/bin/env python3
"""Registrerar översättningar av SEO-titel (meta_title) och SEO-beskrivning (meta_description) på kollektioner.

Indata (semikolon): handle; kollektion_id; locale; key; svenska; oversattning; godkand. Bara godkand=ja skrivs.
Skydd: (1) raden hoppas över om den svenska källtexten live skiljer sig från kolumnen 'svenska' (källan har ändrats),
(2) en befintlig översättning skrivs aldrig över, (3) digest hämtas live per fält, (4) varje översättning läses tillbaka.
Torrkörning om --kor saknas. --max N för kanarie. API-version 2026-10 om inget annat anges.
"""
import argparse, csv, json, os, sys
os.environ.setdefault("SHOPIFY_API_VERSION", "2026-10")
from kon_fyll_target_gender import Klient, Stopp

LASA = '''query($id:ID!,$l:String!){translatableResource(resourceId:$id){translatableContent{key value digest}
 translations(locale:$l){key value outdated}}}'''
SATT = '''mutation($id:ID!,$t:[TranslationInput!]!){translationsRegister(resourceId:$id,translations:$t){
 translations{key value} userErrors{field message}}}'''
TILLATNA = {"meta_title": 60, "meta_description": 160}


def behorighet(klient, krav):
    """Stoppar innan något skrivs om appen saknar en nödvändig behörighet (lärdom 2026-11-20)."""
    d = klient.graphql('{ currentAppInstallation { accessScopes { handle } } }')
    har = {s["handle"] for s in d["currentAppInstallation"]["accessScopes"]}
    saknas = sorted(set(krav) - har)
    if saknas:
        raise Stopp("appen saknar behörighet: " + ", ".join(saknas))


def skriv(klient, csv_fil, fore_fil, max_n=None, kor=False, logg=print):
    rader = [r for r in csv.DictReader(open(csv_fil, encoding="utf-8"), delimiter=";") if r.get("godkand", "").strip().lower() == "ja"]
    if max_n:
        rader = rader[:max_n]
    if kor:
        behorighet(klient, {"write_translations"})
    fore, klara = [], 0
    try:
        for r in rader:
            key, loc, v = r["key"], r["locale"], r["oversattning"].strip()
            if key not in TILLATNA or loc not in ("da", "no") or not v or len(v) > TILLATNA[key]:
                raise Stopp(f"{r['handle']} {loc} {key}: ogiltig rad (nyckel, språk, tom eller för lång text)")
            rid = f"gid://shopify/Collection/{r['kollektion_id']}"
            d = klient.graphql(LASA, {"id": rid, "l": loc})["translatableResource"]
            if not d:
                raise Stopp(f"{r['handle']}: resursen finns inte")
            kalla = next((c for c in d["translatableContent"] if c["key"] == key), None)
            if not kalla or (kalla["value"] or "").strip() != r["svenska"].strip():
                logg(f"hoppar över {r['handle']} {loc} {key}: svenska källtexten live skiljer sig från filen"); continue
            finns = next((t for t in d["translations"] if t["key"] == key and (t["value"] or "").strip()), None)
            if finns:
                logg(f"hoppar över {r['handle']} {loc} {key}: har redan översättning"); continue
            fore.append({"handle": r["handle"], "id": rid, "locale": loc, "key": key, "tidigare": None})
            if not kor:
                continue
            fel = klient.graphql(SATT, {"id": rid, "t": [{"locale": loc, "key": key, "value": v, "translatableContentDigest": kalla["digest"]}]})["translationsRegister"]["userErrors"]
            if fel:
                raise Stopp(f"{r['handle']} {loc} {key}: {fel}")
            efter = klient.graphql(LASA, {"id": rid, "l": loc})["translatableResource"]["translations"]
            if next((t["value"] for t in efter if t["key"] == key), None) != v:
                raise Stopp(f"återläsning avviker för {r['handle']} {loc} {key}")
            klara += 1
            logg(f"skrev {r['handle']} {loc} {key}")
    finally:
        json.dump(fore, open(fore_fil, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return len(rader), klara


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--kor", action="store_true")
    ap.add_argument("--max", type=int)
    ap.add_argument("--fore-fil", default="fore_oversattning.json")
    a = ap.parse_args()
    try:
        print(skriv(Klient(), a.csv, a.fore_fil, a.max, a.kor))
    except Stopp as e:
        sys.exit(f"STOPP: {e}")


if __name__ == "__main__":
    main()
