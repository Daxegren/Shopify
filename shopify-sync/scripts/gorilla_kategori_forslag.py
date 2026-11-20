#!/usr/bin/env python3
"""Läsande kategoriförslag för Gorilla Sports Nordics (inget skrivs).

Indata: produkter.csv från wb_export.py. Urval: aktiva produkter utan kategori ("Uncategorized") och
aktiva produkter i Shopifys gamla kategoriträd ("Exercise & Fitness", "Free Weights" osv. som inte finns i det nya).
Utdata: granskningsfil med förslag per produkt. Kategori-id:n och namn är kontrollerade mot Shopifys kategoriträd i butiken
(2026-11-20). Produkter där ingen regel passar får tomt förslag och säkerhet 'manuell'.
Användning: gorilla_kategori_forslag.py PRODUKTER.csv UT.csv
"""
import csv, re, sys

T = "gid://shopify/TaxonomyCategory/"
KAT = {  # id -> svenskt namn (kontrollerat mot butikens kategoriträd)
 "sg-2-24-2-1": "Sportartiklar > Fitness- och allmän träningsutrustning > Styrketräning > Fria vikter, hantlar och kettlebells > Hantlar",
 "sg-2-24-2-4": "Sportartiklar > Fitness- och allmän träningsutrustning > Styrketräning > Fria vikter, hantlar och kettlebells > Viktskivor",
 "sg-2-24-2-5": "Sportartiklar > Fitness- och allmän träningsutrustning > Styrketräning > Fria vikter, hantlar och kettlebells > Friviktsset",
 "sg-2-24-1-1": "Sportartiklar > Fitness- och allmän träningsutrustning > Styrketräning > Tillbehör till fria vikter > Skivor och tyngdlyftningsstänger",
 "sg-2-24-1": "Sportartiklar > Fitness- och allmän träningsutrustning > Styrketräning > Tillbehör till fria vikter",
 "sg-2-24-1-5": "Sportartiklar > Fitness- och allmän träningsutrustning > Styrketräning > Tillbehör till fria vikter > Skivstångskuddar",
 "sg-2-24-1-2-4": "Sportartiklar > Fitness- och allmän träningsutrustning > Styrketräning > Tillbehör till fria vikter > Ställ för hantlar och viktskivor > Viktskivsställ",
 "sg-2-24-1-2-5": "Sportartiklar > Fitness- och allmän träningsutrustning > Styrketräning > Tillbehör till fria vikter > Ställ för hantlar och viktskivor > Hantelställ",
 "sg-2-24-5-2": "Sportartiklar > Fitness- och allmän träningsutrustning > Styrketräning > Tillbehör till styrketräningsmaskiner och -bänkar > Användarnamn (Shopifys svenska översättning av 'Handles', handtag)",
 "sg-2-24-5-1": "Sportartiklar > Fitness- och allmän träningsutrustning > Styrketräning > Tillbehör till styrketräningsmaskiner och -bänkar > Kablar",
 "sg-2-24-4": "Sportartiklar > Fitness- och allmän träningsutrustning > Styrketräning > Träningshandskar och handstöd",
 "sg-2-9": "Sportartiklar > Fitness- och allmän träningsutrustning > Träningsmaskin och utrustning",
 "sg-2-7": "Sportartiklar > Fitness- och allmän träningsutrustning > Träningsbänkar",
 "sg-2-15-2": "Sportartiklar > Fitness- och allmän träningsutrustning > Medicinbollar > Medicinboll",
 "sg-2-4-3": "Sportartiklar > Fitness- och allmän träningsutrustning > Konditionsträning > Hopprep",
 "sg-2-6": "Sportartiklar > Fitness- och allmän träningsutrustning > Träningsband och -slingor",
 "sg-2-12": "Sportartiklar > Fitness- och allmän träningsutrustning > Skumgummirullar",
 "sg-2-17-3": "Sportartiklar > Fitness- och allmän träningsutrustning > Armhävningshandtag > Pull-up-stänger",
 "sg-2-17": "Sportartiklar > Fitness- och allmän träningsutrustning > Armhävningshandtag",
 "sg-2-29": "Sportartiklar > Fitness- och allmän träningsutrustning > Shakers",
 "sg-2-26": "Sportartiklar > Fitness- och allmän träningsutrustning > Yoga och pilates",
 "sg-2-2": "Sportartiklar > Fitness- och allmän träningsutrustning > Aerobics-brädor",
 "sg-1-4-2-4-3": "Sportartiklar > Idrott och sport > Boxning och kampsporter > Träningsutrustning för boxning och kampsporter > Sandsäckar och träningssäckar > Tunga sandsäckar och träningssäckar",
 "sg-1-4-1-5": "Sportartiklar > Idrott och sport > Boxning och kampsporter > Skyddsutrustning för boxning och kampsport > Handlindor för boxning",
 "sg-1-14-3": "Sportartiklar > Idrott och sport > Gymnastik > Gymnastikringar",
 "hb-3-11-8-2-3": "Skönhet och hälsa > Personlig vård > Massage och avslappning > Massageapparater > Verktyg för manuell massage > Massagebollar",
 "hg-11-3-11": "Hem och trädgård > Kök och matsal > Kärl för mat och dryck > Vattenflaskor",
}

# (regel, regex mot "produkttyp | titel" i gemener, kategori-id, säkerhet) – första träff gäller
REGLER = [
 ("undantag", r"väggfäste|karbinhakar|ställ kabelhandtag", "", "manuell"),
 ("friviktsset", r"^skivstångspaket|skivstång.*hantlar|curlstång hantlar|starter paketet|curlstångspaket|skivstång & hantelset|bodypump", "sg-2-24-2-5", "medel"),
 ("kabelstång", r"kabelstång|draghandtag", "sg-2-24-5-2", "medel"),
 ("viktskivor", r"viktskiv|bumper plates|minivikt", "sg-2-24-2-4", "hög"),
 ("viktställ", r"viktställ", "sg-2-24-1-2-4", "hög"),
 ("hantelställ", r"hantelställ", "sg-2-24-1-2-5", "hög"),
 ("hantlar", r"\bhantlar\b|\bhantel \b|hexagonhantlar|hantlar - fasta|justerbara hantelset", "sg-2-24-2-1", "hög"),
 ("skivstångskudde", r"skivstångskudde", "sg-2-24-1-5", "hög"),
 ("stänger", r"curlstång|hantelstång|skivstänger", "sg-2-24-1-1", "hög"),
 ("kabel", r"kabel(set| latsdrag)|^[^|]*\|\s*kabel ", "sg-2-24-5-1", "medel"),
 ("kabelhandtag", r"kabelhandtag|kabelstång|roddhandtag|tricepsrep|tricepsstång|latsdrag kabelstång|v grepp|multihookbar|vristband|ankelband|crunch grepp|roddhantag|enhands", "sg-2-24-5-2", "medel"),
 ("pullup", r"chins & dips|chinsstång|pull up bar|pull-ups", "sg-2-17-3", "hög"),
 ("parallettes", r"parallette", "sg-2-17", "medel"),
 ("gummiband", r"gummiband|latexband|miniband|hip glute band|tower 2000", "sg-2-6", "hög"),
 ("foamroller", r"foam roller|pilates roller", "sg-2-12", "hög"),
 ("massageboll", r"massageboll", "hb-3-11-8-2-3", "hög"),
 ("hopprep", r"hopprep|speed rope", "sg-2-4-3", "hög"),
 ("medicinboll", r"medicinboll|wall ?ball", "sg-2-15-2", "medel"),
 ("shaker", r"shaker", "sg-2-29", "hög"),
 ("vattenflaska", r"vattenflaska", "hg-11-3-11", "medel"),
 ("träningshandskar", r"träningshandskar", "sg-2-24-4", "hög"),
 ("boxningsbandage", r"boxningsbandage|boxningslindor", "sg-1-4-1-5", "hög"),
 ("boxningssäck", r"boxningssäck|boxningsstation|boxningspaket", "sg-1-4-2-4-3", "medel"),
 ("stepbräda", r"step up", "sg-2-2", "medel"),
 ("yoga", r"yogapaket|yogabälte|yogaväska|yogamatt", "sg-2-26", "medel"),
 ("curlbänk", r"curlbänk", "sg-2-7", "medel"),
 ("gymringar", r"gymringar", "sg-1-14-3", "medel"),
 ("viktlås", r"viktlås|stjärnlås|jaw ?lock", "sg-2-24-1", "medel"),
 ("gympaket", r"gympaket|paket|hemmagym|crossfitpaket|hyroxpaket", "sg-2-9", "medel"),
]
GAMLA = ("Exercise & Fitness", "Free Weights")  # gammalt kategoriträd

def klassa(typ, titel):
    s = f"{typ} | {titel}".lower()
    for namn, rx, kid, sak in REGLER:
        if re.search(rx, s):
            return namn, kid, sak
    return "", "", "manuell"

def main(inn, ut):
    rows = list(csv.DictReader(open(inn, encoding="utf-8"), delimiter=";"))
    urval = [r for r in rows if r["status"] == "ACTIVE" and (r["kategori"] == "Uncategorized"
             or r["kategori"].startswith("Sporting Goods > Exercise & Fitness")
             or (not r["kategori"].startswith(("Sporting Goods > Fitness", "Sporting Goods > Athletics")) and r["kategori"] not in ("Uncategorized",)
                 and r["kategori"].split(" > ")[0] in ("Health & Beauty", "Toys & Games", "Apparel & Accessories", "Electronics")))]
    w = csv.writer(open(ut, "w", encoding="utf-8", newline=""), delimiter=";")
    w.writerow(["produkt_id", "handle", "titel", "produkttyp", "nuvarande_kategori", "grupp", "regel", "foreslagen_kategori_id", "foreslagen_kategori_namn", "sakerhet"])
    n = {}
    for r in sorted(urval, key=lambda r: (r["kategori"] != "Uncategorized", r["produkttyp"], r["titel"])):
        regel, kid, sak = klassa(r["produkttyp"], r["titel"])
        grupp = "utan kategori" if r["kategori"] == "Uncategorized" else "gammalt/avvikande kategoriträd"
        w.writerow([r["id"], r["handle"], r["titel"], r["produkttyp"], r["kategori"], grupp, regel, (T + kid) if kid else "", KAT.get(kid, ""), sak])
        n[(grupp, sak)] = n.get((grupp, sak), 0) + 1
    for k, v in sorted(n.items()): print(v, k)

if __name__ == "__main__":
    main(*sys.argv[1:3])
