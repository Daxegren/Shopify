#!/usr/bin/env python3
"""Prisförslag (bara läsning): räknar formelpris per variant ur Shopifys egna uppgifter.

Formelpris = inköpspris / (1 - marginal) * moms, avrundat uppåt till närmaste ...9 (varor under 50 kr undantas
från taket på 50 % marginal men aldrig under inköpspris). Ordinarie pris = jämförpriset om det är högre än priset
(då pågår en rea), annars priset. Ändringar över ±25 % hålls kvar. Produkter med price-change-job-active markeras.
Skriver en CSV som David godkänner (kolumnen godkand) och som pris_skriv_fran_csv.py läser. Inget skrivs i butiken.

Användning:  python3 -I shopify-sync/scripts/pris_forslag.py --ut rapporter/prisforslag-2026-12-01.csv
"""
import argparse, csv, math, sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MOMS = 1.25
MARGINAL = 0.40
MAX_ANDRING = 0.25
GOLV, TAK = 0.30, 0.50
SMA_VAROR = 50.0
PRISJOBB = "price-change-job-active"

KOLUMNER = ["produkt_id", "variant_id", "sku", "titel", "pris_nu", "jamforpris", "ordinarie_pris", "inkop",
            "nytt_pris", "andring_pct", "riktning", "marginal_fore_pct", "marginal_efter_pct", "lager",
            "prisjobb", "rea", "hallen", "flagga", "godkand"]


def upp9(x):
    """Närmaste heltal som slutar på 9, uppåt (102,1 -> 109; 109 -> 109)."""
    return int(math.ceil((x - 9) / 10.0) * 10 + 9)


def formelpris(inkop, marginal=MARGINAL, moms=MOMS):
    return upp9(inkop / (1 - marginal) * moms)


def marginal_efter_moms(pris, inkop, moms=MOMS):
    if pris <= 0:
        return None
    netto = pris / moms
    return (netto - inkop) / netto


def bedom(pris_nu, jamforpris, inkop, tags, lager, moms=MOMS, marginal=MARGINAL, golv=GOLV, tak=TAK, tolerans=0.0):
    """Returnerar en dict med förslag och flaggor för en variant, eller None om inköpspris saknas."""
    if inkop is None or inkop <= 0 or pris_nu is None or pris_nu <= 0:
        return None
    rea = bool(jamforpris and jamforpris > pris_nu)
    ordinarie = jamforpris if rea else pris_nu
    nytt = formelpris(inkop, marginal, moms)
    m_efter = marginal_efter_moms(nytt, inkop, moms)
    m_fore = marginal_efter_moms(ordinarie, inkop, moms)
    andring = (nytt - ordinarie) / ordinarie
    flaggor = []
    hallen = False
    if nytt / moms < inkop:
        flaggor.append("UNDER_INKOP")
    if nytt >= SMA_VAROR and m_efter is not None and (m_efter < golv or m_efter > tak):
        flaggor.append("MARGINAL_UTANFOR_30_50")
    if abs(andring) > MAX_ANDRING:
        hallen = True
        flaggor.append("ANDRING_OVER_25")
    if m_fore is not None and m_fore > 0.80 and nytt < ordinarie:
        flaggor.append("KONTROLLERA_INKOP_ELLER_FORPACKNING")
    if nytt < 0.4 * ordinarie:
        flaggor.append("NYTT_UNDER_40_PCT_AV_NUVARANDE")
    if tolerans and m_fore is not None and abs(m_fore - marginal) <= tolerans and not rea:
        return None  # redan nära målmarginalen: ändras inte
    prisjobb = PRISJOBB in (tags or [])
    if prisjobb:
        flaggor.append("PRISJOBBSTAGG_SKRIVS_EJ")
    if rea:
        flaggor.append("REA_PAGAR_RAKNA_OM_EFTER_ATERSTALLNING")
    return {"rea": rea, "ordinarie": ordinarie, "nytt": nytt, "andring": andring, "m_fore": m_fore, "m_efter": m_efter,
            "hallen": hallen, "flaggor": flaggor, "prisjobb": prisjobb,
            "riktning": "upp" if nytt > ordinarie else ("ner" if nytt < ordinarie else "lika")}


LASA = '''query($c:String){products(first:40,after:$c,query:"status:active"){pageInfo{hasNextPage endCursor}
nodes{legacyResourceId title tags variants(first:30){nodes{legacyResourceId sku price compareAtPrice inventoryQuantity
inventoryItem{unitCost{amount}}}}}}}'''


def hamta(klient, paus=0.4, logg=print):
    c = None
    n = 0
    while True:
        r = klient.graphql(LASA, {"c": c})
        d = r.get("products") or r["data"]["products"]
        for p in d["nodes"]:
            n += 1
            for v in p["variants"]["nodes"]:
                yield p, v
        if logg and n % 400 < 40:
            logg(f"lästa produkter: {n}")
        if not d["pageInfo"]["hasNextPage"]:
            break
        c = d["pageInfo"]["endCursor"]
        time.sleep(paus)


def rader(klient, marginal=MARGINAL, golv=GOLV, tak=TAK, tolerans=0.0, **kw):
    for p, v in hamta(klient, **kw):
        uc = (v.get("inventoryItem") or {}).get("unitCost")
        inkop = float(uc["amount"]) if uc and uc.get("amount") else None
        pris = float(v["price"])
        jmf = float(v["compareAtPrice"]) if v.get("compareAtPrice") else 0.0
        b = bedom(pris, jmf, inkop, p.get("tags") or [], v.get("inventoryQuantity"), marginal=marginal, golv=golv, tak=tak, tolerans=tolerans)
        if not b or b["nytt"] == pris and not b["rea"] and not b["flaggor"]:
            continue
        if b["riktning"] == "lika" and not b["flaggor"]:
            continue
        yield {"produkt_id": p["legacyResourceId"], "variant_id": v["legacyResourceId"], "sku": v.get("sku") or "",
               "titel": (p["title"] or "")[:70], "pris_nu": f"{pris:.2f}", "jamforpris": f"{jmf:.2f}" if jmf else "",
               "ordinarie_pris": f"{b['ordinarie']:.2f}", "inkop": f"{inkop:.2f}", "nytt_pris": f"{b['nytt']:.2f}",
               "andring_pct": f"{b['andring']*100:.1f}", "riktning": b["riktning"],
               "marginal_fore_pct": f"{b['m_fore']*100:.1f}", "marginal_efter_pct": f"{b['m_efter']*100:.1f}",
               "lager": v.get("inventoryQuantity"), "prisjobb": int(b["prisjobb"]), "rea": int(b["rea"]),
               "hallen": int(b["hallen"]), "flagga": "|".join(b["flaggor"]), "godkand": ""}


def sammanfatta(rs):
    from collections import Counter
    c = Counter()
    for r in rs:
        c["rader"] += 1
        c[r["riktning"]] += 1
        c["hallen"] += int(r["hallen"])
        c["rea"] += int(r["rea"])
        c["prisjobb"] += int(r["prisjobb"])
        if r["flagga"]:
            for f in r["flagga"].split("|"):
                c["flagga:" + f] += 1
    return c


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--ut", required=True)
    ap.add_argument("--profil", default=None, help="butiksprofil (standard: BEST OF SPORTS)")
    ap.add_argument("--marginal", type=float, default=MARGINAL, help="målmarginal efter moms (BOS 0.40, Workout Brands 0.60)")
    ap.add_argument("--golv", type=float, default=GOLV)
    ap.add_argument("--tak", type=float, default=TAK)
    ap.add_argument("--tolerans", type=float, default=0.0, help="rör inte varianter vars marginal redan ligger inom så många procentenheter (0.03 = 3 pp)")
    a = ap.parse_args(argv)
    from shopify_api import ShopifyKlient
    klient = ShopifyKlient() if not a.profil else __import__("shopify_api").klient_fran_profil(a.profil)
    rs = list(rader(klient, marginal=a.marginal, golv=a.golv, tak=a.tak, tolerans=a.tolerans))
    with open(a.ut, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=KOLUMNER, delimiter=";")
        w.writeheader()
        w.writerows(rs)
    for k, v in sorted(sammanfatta(rs).items()):
        print(f"{k}: {v}")
    print("CSV:", a.ut)


if __name__ == "__main__":
    main()
