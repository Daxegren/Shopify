#!/usr/bin/env python3
"""Sätter produktkategori på produkter som saknar den (Workout Brands), så att fältet "Avsett för" kan fyllas.

Två lägen:
  --forslag IN.csv UT.csv   LÄSER bara. IN = misslyckade_kon.csv (produkt_id;kategori;felmeddelande). UT får titel, märke,
                            produkttyp, nuvarande kategori och föreslagen kategori. David granskar och sätter godkand=ja.
  --skriv GODKAND.csv       Skriver bara rader med godkand=ja. Före-fil sparas, varje rad läses tillbaka, stopp vid
                            första avvikelse. Torrkörning om --skriv saknas (--kor). --max N för kanariefall.
Rör inte priser, taggar, texter, status eller spärrade produkter. Miljövariabler skrivs i terminalen, aldrig i chatten.
"""
import argparse, csv, json, sys
from kon_fyll_target_gender import Klient, Stopp, gid

KAT = {
    "kläder": ("gid://shopify/TaxonomyCategory/aa", "Kläder och accessoarer"),
    "keps": ("gid://shopify/TaxonomyCategory/aa-2-17-1", "Hattar > Baseballkeps"),
    "strumpor": ("gid://shopify/TaxonomyCategory/aa-1-18", "Klädsel > Strumpor"),
    "bälte": ("gid://shopify/TaxonomyCategory/aa-2-6", "Klädaccessoarer > Bälten"),
    "solglasögon": ("gid://shopify/TaxonomyCategory/aa-2-27", "Klädaccessoarer > Solglasögon"),
    "ryggsäck": ("gid://shopify/TaxonomyCategory/lb-1", "Resväskor och väskor > Ryggsäckar"),
}
INGEN = ("mug", "exercise book", "exercises book")
GRUPPER = [
    ("keps", ("keps", " cap", "snapback", "trucker", "visor", "dockercap", "driver")),
    ("strumpor", ("sock", "strumpor")),
    ("manuell", ("pouch", "hip bag")),
    ("bälte", ("belt", "bälte")),
    ("solglasögon", ("sunglasses", "solglas")),
    ("ryggsäck", ("ryggsäck", "backpack", "duffel")),
    ("manuell", ("beanie", "mössa", "necklace", "anklet", "halsband", "fotlänk", "scrunchie", "headband", "bandana",
                 "tote", "pouch", "hip bag", "sneakers", "highbridge", "väska", "tillbehör")),
    ("kläder", ("tee", "t-shirt", "hoodie", "hoody", "shorts", "tights", "jeans", "jacket", "jacka", "windrunner",
                "bomber", "vest", "väst", "tank", "top", "linne", "pants", "byxor", "sweat", "longsleeve", "crew", "dress",
                "klänning", "skirt", "kjol", "skjol", "cardigan", "shirt", "skjorta", "body", "bra ", "bh", "boxer",
                "kalsonger", "underkläder", "hipster", "thong", "bikini", "leggings", "trackpants", "poncho", "pullover",
                "jersey", "långärmad", "stickad", "cargo", "badbyxor", "tröja", "dry baggys", " ls")),
]


def klassa(titel, typ, marke=""):
    """Returnerar nyckel i KAT, 'ingen' (ska inte ha kategori/kön) eller 'manuell'."""
    t = f" {titel} {typ}".lower()
    if any(x in t for x in INGEN):
        return "ingen"
    if typ.strip().lower() == "keps":
        return "keps"
    for namn, ord_ in GRUPPER:
        if any(o in t for o in ord_):
            return namn
    return "manuell"


LASA = '''query($ids:[ID!]!){nodes(ids:$ids){... on Product{id title vendor productType status category{id fullName}}}}'''
SATT = '''mutation($p:ProductUpdateInput!){productUpdate(product:$p){product{id category{id}} userErrors{field message}}}'''


def forslag(klient, inn, ut):
    ids = [int(r["produkt_id"]) for r in csv.DictReader(open(inn, encoding="utf-8"), delimiter=";") if r["produkt_id"].isdigit()]
    rader = []
    for k in range(0, len(ids), 50):
        for n in klient.graphql(LASA, {"ids": [gid(i) for i in ids[k:k + 50]]})["nodes"]:
            if not n:
                continue
            nyckel = klassa(n["title"], n.get("productType") or "")
            kid, knamn = KAT.get(nyckel, ("", nyckel))
            rader.append({"produkt_id": n["id"].rsplit("/", 1)[1], "titel": n["title"], "marke": n["vendor"],
                          "produkttyp": n.get("productType") or "", "nuvarande": (n.get("category") or {}).get("fullName", ""),
                          "grupp": nyckel, "foreslagen": knamn, "kategori_id": kid, "godkand": ""})
    with open(ut, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rader[0]), delimiter=";")
        w.writeheader(); w.writerows(rader)
    return rader


def skriv(klient, godkand, fore_fil, max_n=None, kor=False, logg=print):
    rader = [r for r in csv.DictReader(open(godkand, encoding="utf-8"), delimiter=";")
             if r.get("godkand", "").strip().lower() == "ja" and r.get("kategori_id")]
    if max_n:
        rader = rader[:max_n]
    fore, klara = [], 0
    for r in rader:
        i = int(r["produkt_id"])
        n = klient.graphql(LASA, {"ids": [gid(i)]})["nodes"][0]
        if not n or n.get("status") != "ACTIVE":
            logg(f"hoppar över {i}: ej aktiv/saknas"); continue
        nu = (n.get("category") or {}).get("id")
        if nu == r["kategori_id"]:
            continue
        fore.append({"produkt_id": i, "tidigare": nu, "ny": r["kategori_id"]})
        if kor:
            fel = klient.graphql(SATT, {"p": {"id": gid(i), "category": r["kategori_id"]}})["productUpdate"]["userErrors"]
            if fel:
                raise Stopp(f"produkt {i}: {fel}")
            efter = klient.graphql(LASA, {"ids": [gid(i)]})["nodes"][0]["category"]
            if not efter or efter["id"] != r["kategori_id"]:
                raise Stopp(f"återläsning avviker för {i}")
            klara += 1
    json.dump(fore, open(fore_fil, "w"), indent=1)
    return len(rader), klara


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--forslag", nargs=2, metavar=("IN", "UT"))
    ap.add_argument("--skriv", metavar="GODKAND")
    ap.add_argument("--kor", action="store_true", help="skriv på riktigt (annars torrkörning)")
    ap.add_argument("--max", type=int)
    ap.add_argument("--fore-fil", default="fore_kategori.json")
    a = ap.parse_args()
    k = Klient()
    try:
        if a.forslag:
            r = forslag(k, *a.forslag)
            from collections import Counter
            print(Counter(x["grupp"] for x in r))
        elif a.skriv:
            print(skriv(k, a.skriv, a.fore_fil, a.max, a.kor))
        else:
            ap.print_help()
    except Stopp as e:
        sys.exit(f"STOPP: {e}")


if __name__ == "__main__":
    main()
