#!/usr/bin/env python3
"""Skriver SEO-titel och SEO-beskrivning på kollektioner från en godkänd CSV.

Indata (semikolon): handle; kollektion_id; seo_title_nu; seo_title_forslag; seo_description_nu; seo_description_forslag; godkand.
Bara rader med godkand=ja skrivs. Reglerna (lärdomar 2026-11-01, -03 och 2026-11-19):
  * title och description skickas ALLTID tillsammans i seo (utelämnas description töms den).
  * Raden hoppas över om kollektionen redan har en SEO-titel, eller om SEO-beskrivningen live skiljer sig från seo_description_nu.
  * Före-värden sparas i före-filen. Efter varje skrivning läses titel, beskrivning, kollektionstitel, adress och
    sidtext (descriptionHtml) tillbaka; avvikelse stoppar körningen.
  * Torrkörning om --kor saknas. --max N för kanariekörning.
API-versionen är 2026-10 om inget annat anges (SHOPIFY_API_VERSION). Butiken styrs av SHOPIFY_BUTIK.
"""
import argparse, csv, json, os, sys
os.environ.setdefault("SHOPIFY_API_VERSION", "2026-10")
from kon_fyll_target_gender import Klient, Stopp

LASA = '''query($id:ID!){collection(id:$id){id handle title descriptionHtml seo{title description}}}'''
SATT = '''mutation($c:CollectionUpdateInput!){collectionUpdate(collection:$c){collection{id} userErrors{field message}}}'''


def tom(v):
    v = (v or "").strip()
    return "" if v == "(saknas)" else v


def gid(i):
    return f"gid://shopify/Collection/{i}"


def skriv(klient, csv_fil, fore_fil, max_n=None, kor=False, logg=print):
    rader = [r for r in csv.DictReader(open(csv_fil, encoding="utf-8"), delimiter=";")
             if r.get("godkand", "").strip().lower() == "ja"]
    if max_n:
        rader = rader[:max_n]
    fore, klara = [], 0
    try:
        for r in rader:
            ny_t, ny_d = r["seo_title_forslag"].strip(), r["seo_description_forslag"].strip()
            if not ny_t or not ny_d or len(ny_t) > 60 or len(ny_d) > 160:
                raise Stopp(f"{r['handle']}: titel/beskrivning saknas eller är för lång")
            nu = klient.graphql(LASA, {"id": gid(r["kollektion_id"])})["collection"]
            if not nu or nu["handle"] != r["handle"]:
                raise Stopp(f"{r['handle']}: kollektionen finns inte eller har annan adress ({nu and nu['handle']})")
            seo = nu.get("seo") or {}
            if tom(seo.get("title")):
                logg(f"hoppar över {r['handle']}: har redan SEO-titel"); continue
            if tom(seo.get("description")) != tom(r["seo_description_nu"]):
                logg(f"hoppar över {r['handle']}: SEO-beskrivningen live skiljer sig från filen"); continue
            fore.append({"handle": r["handle"], "id": nu["id"], "title": nu["title"], "descriptionHtml": nu["descriptionHtml"],
                         "seo_title": seo.get("title"), "seo_description": seo.get("description")})
            if not kor:
                continue
            fel = klient.graphql(SATT, {"c": {"id": nu["id"], "seo": {"title": ny_t, "description": ny_d}}})["collectionUpdate"]["userErrors"]
            if fel:
                raise Stopp(f"{r['handle']}: {fel}")
            efter = klient.graphql(LASA, {"id": nu["id"]})["collection"]
            s2 = efter.get("seo") or {}
            avvik = [k for k, v in (("seo.title", (s2.get("title") or "", ny_t)), ("seo.description", (s2.get("description") or "", ny_d)),
                                    ("title", (efter["title"], nu["title"])), ("handle", (efter["handle"], nu["handle"])),
                                    ("descriptionHtml", (efter["descriptionHtml"], nu["descriptionHtml"]))) if v[0] != v[1]]
            if avvik:
                raise Stopp(f"återläsning avviker för {r['handle']}: {avvik}")
            klara += 1
            logg(f"skrev {r['handle']}")
    finally:
        json.dump(fore, open(fore_fil, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return len(rader), klara


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--kor", action="store_true", help="skriv på riktigt (annars torrkörning)")
    ap.add_argument("--max", type=int)
    ap.add_argument("--fore-fil", default="fore_seo.json")
    a = ap.parse_args()
    try:
        print(skriv(Klient(), a.csv, a.fore_fil, a.max, a.kor))
    except Stopp as e:
        sys.exit(f"STOPP: {e}")


if __name__ == "__main__":
    main()
