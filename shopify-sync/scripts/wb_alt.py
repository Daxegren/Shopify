#!/usr/bin/env python3
"""Sätter alt-text på produktbilder som saknar den (butik styrs av SHOPIFY_BUTIK, standard Workout Brands). Torrkörning som standard.

Bara aktiva produkter, bara bilder (MediaImage) med tom alt-text. Alt-text = produktens titel. Befintlig alt-text rörs aldrig.
Hämtar först alla aktiva produkter med bulkoperation, sparar före-fil (media-id, tidigare alt, ny alt), skriver i grupper om 20,
läser tillbaka varje grupp och stoppar vid första avvikelse. Kan köras om: bilder som redan har alt hoppas över.

Miljövariabler (skrivs i terminalen, aldrig i chatten): SHOPIFY_CLIENT_ID_WB, SHOPIFY_CLIENT_SECRET_WB
Behörighet: write_files (eller write_products). Saknas den skriver Shopify vilken.
  python3 wb_alt.py --ut ~/wb_alt                                  (torrkörning: räknar bara)
  python3 wb_alt.py --ut ~/wb_alt --skriv --max-produkter 10       (kanariefall)
  python3 wb_alt.py --ut ~/wb_alt --skriv                          (allt)
  python3 wb_alt.py --ut ~/wb_alt --utesluter-tagg price-change-job-active   (hoppa över produkter med taggen)
  python3 wb_alt.py --ut ~/wb_alt --aterstall ~/wb_alt/fore_alt.jsonl [--skriv]   (ångra: tom alt på de bilder vi skrev, bara om alt är oförändrad)
"""
import argparse, json, os, sys, time
from kon_fyll_target_gender import Klient, Stopp
from wb_export import kor_bulk, las_jsonl

BULK = '''{ products(query: "status:active") { edges { node { id title tags media { edges { node { ... on MediaImage { id alt } } } } } } } }'''
SKRIV = '''mutation($f:[FileUpdateInput!]!){fileUpdate(files:$f){files{id alt} userErrors{field message code}}}'''
LASA = '''query($ids:[ID!]!){nodes(ids:$ids){... on MediaImage{id alt}}}'''
GRUPP = 20


def att_gora(jsonl, uteslut_tagg=None):
    """[(media_id, ny_alt, produkt)] för bilder utan alt, och räkning. Produkter med taggen uteslut_tagg hoppas över."""
    ut, produkter, sedda = [], set(), set()
    for nod, barn in las_jsonl(jsonl):
        titel = (nod.get("title") or "").strip()
        if not titel:
            continue
        if uteslut_tagg and uteslut_tagg in (nod.get("tags") or []):
            continue
        for b in barn:
            if b.get("id", "").startswith("gid://shopify/MediaImage") and not (b.get("alt") or "").strip():
                if b["id"] in sedda:  # samma bild på flera produkter: första produktens titel gäller
                    continue
                sedda.add(b["id"])
                ut.append((b["id"], titel[:512], nod["id"]))
                produkter.add(nod["id"])
    return ut, len(produkter)


def skriv_grupp(k, grupp):
    fel = k.graphql(SKRIV, {"f": [{"id": i, "alt": a} for i, a, _ in grupp]})["fileUpdate"]["userErrors"]
    if fel:
        raise Stopp(f"fileUpdate: {fel[:3]}")
    r = k.graphql(LASA, {"ids": [i for i, _, _ in grupp]})["nodes"]
    for (i, a, _), n in zip(grupp, r):
        if not n or (n.get("alt") or "") != a:
            raise Stopp(f"återläsning avviker för {i}: {n}")


def kor(k, jobb, fore_fil, skriv=False, max_produkter=0, logg=print, sleep=time.sleep):
    if max_produkter:
        tillatna, valda = [], []
        for i, a, p in jobb:
            if p not in tillatna:
                if len(tillatna) >= max_produkter:
                    continue
                tillatna.append(p)
            valda.append((i, a, p))
        jobb = valda
    with open(fore_fil, "a", encoding="utf-8") as f:
        for i, a, p in jobb:
            f.write(json.dumps({"media_id": i, "produkt": p, "fore": None, "ny": a}, ensure_ascii=False) + "\n")
    skrivna = 0
    if skriv:
        for n in range(0, len(jobb), GRUPP):
            skriv_grupp(k, jobb[n:n + GRUPP]); skrivna += len(jobb[n:n + GRUPP])
            if (n // GRUPP) % 25 == 0:
                logg(f"  skrivna {skrivna} av {len(jobb)}")
            sleep(0.3)
    return len(jobb), skrivna


def aterstall(k, fore_fil, skriv=False, logg=print, sleep=time.sleep):
    """Ångra: sätter tom alt-text på bilder vi skrev, men bara om alt-texten fortfarande är exakt den vi skrev."""
    rader = {}
    for rad in open(fore_fil, encoding="utf-8"):
        if rad.strip():
            r = json.loads(rad); rader[r["media_id"]] = r["ny"]
    ids = list(rader)
    att, hoppar = [], 0
    for n in range(0, len(ids), GRUPP):
        for nod in k.graphql(LASA, {"ids": ids[n:n + GRUPP]})["nodes"]:
            if nod and (nod.get("alt") or "") == rader[nod["id"]]:
                att.append(nod["id"])
            else:
                hoppar += 1
    if skriv:
        for n in range(0, len(att), GRUPP):
            grupp = att[n:n + GRUPP]
            fel = k.graphql(SKRIV, {"f": [{"id": i, "alt": ""} for i in grupp]})["fileUpdate"]["userErrors"]
            if fel:
                raise Stopp(f"fileUpdate: {fel[:3]}")
            for nod in k.graphql(LASA, {"ids": grupp})["nodes"]:
                if (nod.get("alt") or "") != "":
                    raise Stopp(f"återläsning avviker för {nod['id']}")
            sleep(0.3)
    return len(att), hoppar


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ut", required=True)
    ap.add_argument("--skriv", action="store_true")
    ap.add_argument("--max-produkter", type=int, default=0)
    ap.add_argument("--utesluter-tagg", help="hoppa över produkter med den här taggen, t.ex. price-change-job-active")
    ap.add_argument("--aterstall", metavar="FORE_FIL", help="ångra en tidigare körning ur dess före-fil (tom alt, bara om oförändrad)")
    a = ap.parse_args()
    ut = os.path.expanduser(a.ut); os.makedirs(ut, exist_ok=True)
    k = Klient()
    try:
        if a.aterstall:
            n, h = aterstall(k, os.path.expanduser(a.aterstall), a.skriv)
            print(f"att ångra {n}, hoppar över {h} (alt ändrad sedan vi skrev eller bild borta)" + ("" if a.skriv else " (torrkörning)"))
            return
        print("Läser alla aktiva produkter (bulkoperation) ...")
        fil = kor_bulk(k, BULK, os.path.join(ut, "aktiva.jsonl"))
        jobb, antal_prod = att_gora(fil, a.utesluter_tagg)
        print(f"Bilder utan alt-text: {len(jobb)} på {antal_prod} produkter")
        n, s = kor(k, jobb, os.path.join(ut, "fore_alt.jsonl"), a.skriv, a.max_produkter)
        print(f"valda {n}, skrivna {s}" + ("" if a.skriv else " (torrkörning)"))
    except Stopp as e:
        print("STOPP:", e); sys.exit(2)


if __name__ == "__main__":
    main()
