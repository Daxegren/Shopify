#!/usr/bin/env python3
"""Skriver priser från en CSV som David godkänt (kolumnen godkand = ja). Standardläge är torrkörning.

Skydd: ingen skrivning före 2026-12-01 (prisspärr); live-priset och inköpspriset måste fortfarande vara exakt det
CSV:n byggdes på; produkter med price-change-job-active hoppas över (om inte --tillat-prisjobb); rader med pågående
rea hoppas över; före-fil sparas; de första --canary raderna skrivs och läses tillbaka innan resten; stopp vid första
avvikelse. Jämförpris tas bort bara om det är <= nytt pris. Inget annat fält rörs.

  python3 -I shopify-sync/scripts/pris_skriv_fran_csv.py --csv rapporter/prisforslag.csv              (torrkörning)
  python3 -I shopify-sync/scripts/pris_skriv_fran_csv.py --csv ... --skriv --canary 3 --fore-fil ...  (skriver)
"""
import argparse, csv, datetime, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SPARR_TOM = datetime.date(2026, 12, 1)
PRISJOBB = "price-change-job-active"

LASA = '''query($id:ID!){productVariant(id:$id){id price compareAtPrice product{id tags}
inventoryItem{unitCost{amount}}}}'''
SKRIV = '''mutation($p:ID!,$v:[ProductVariantsBulkInput!]!){productVariantsBulkUpdate(productId:$p,variants:$v){
productVariants{id price compareAtPrice} userErrors{field message}}}'''


class Stopp(Exception):
    pass


def lasa_csv(sokvag):
    with open(sokvag, newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f, delimiter=";")]


def godkanda(rader):
    return [r for r in rader if (r.get("godkand") or "").strip().lower() == "ja"]


def _pris(x):
    return None if x in (None, "") else round(float(x), 2)


def planera(klient, rad, tillat_prisjobb=False):
    """Läser live-läget och returnerar ('skriv', plan) eller ('hoppa', skäl). Stoppar vid avvikelse från CSV:n."""
    v = klient.graphql(LASA, {"id": f"gid://shopify/ProductVariant/{rad['variant_id']}"})["productVariant"]
    if not v:
        raise Stopp(f"variant {rad['variant_id']} finns inte")
    live_pris = _pris(v["price"])
    live_jmf = _pris(v["compareAtPrice"])
    uc = (v.get("inventoryItem") or {}).get("unitCost")
    live_inkop = _pris(uc["amount"]) if uc else None
    nytt = _pris(rad["nytt_pris"])
    if live_pris == nytt:
        return "hoppa", "redan rätt pris"
    if live_pris != _pris(rad["pris_nu"]):
        raise Stopp(f"variant {rad['variant_id']}: live-pris {live_pris} != CSV pris_nu {rad['pris_nu']}")
    if live_inkop != _pris(rad["inkop"]):
        raise Stopp(f"variant {rad['variant_id']}: inköpspris {live_inkop} != CSV {rad['inkop']}")
    if live_jmf and live_jmf > live_pris:
        return "hoppa", "rea pågår"
    if PRISJOBB in (v["product"].get("tags") or []) and not tillat_prisjobb:
        return "hoppa", "prisjobbstagg"
    jmf_ut = None if (live_jmf and live_jmf <= nytt) else live_jmf
    return "skriv", {"produkt": v["product"]["id"], "variant": v["id"], "fore_pris": live_pris, "fore_jmf": live_jmf,
                     "nytt": nytt, "jmf_ut": jmf_ut}


def skriv_en(klient, plan):
    vin = {"id": plan["variant"], "price": f"{plan['nytt']:.2f}", "compareAtPrice": None if plan["jmf_ut"] is None else f"{plan['jmf_ut']:.2f}"}
    d = klient.graphql(SKRIV, {"p": plan["produkt"], "v": [vin]})["productVariantsBulkUpdate"]
    if d["userErrors"]:
        raise Stopp(f"userErrors: {d['userErrors']}")
    # återläsning
    r = klient.graphql(LASA, {"id": plan["variant"]})["productVariant"]
    if _pris(r["price"]) != plan["nytt"] or _pris(r["compareAtPrice"]) != plan["jmf_ut"]:
        raise Stopp(f"återläsning avviker för {plan['variant']}: {r['price']}/{r['compareAtPrice']}")


def kor(klient, rader, skriv=False, canary=3, fore_fil=None, tillat_prisjobb=False, idag=None, logg=print):
    idag = idag or datetime.date.today()
    if skriv and idag < SPARR_TOM:
        raise Stopp(f"Prisspärr: ingen skrivning före {SPARR_TOM}")
    if skriv and not fore_fil:
        raise Stopp("--fore-fil krävs vid skrivning")
    planer, hoppade = [], []
    for r in godkanda(rader):
        tillst, x = planera(klient, r, tillat_prisjobb)
        (planer if tillst == "skriv" else hoppade).append((r, x))
    logg(f"godkända rader: {len(planer) + len(hoppade)}; att skriva: {len(planer)}; hoppas över: {len(hoppade)}")
    for r, skal in hoppade:
        logg(f"  hoppar {r['variant_id']} ({r['sku']}): {skal}")
    if not skriv:
        for r, p in planer:
            logg(f"  TORR {r['variant_id']} {p['fore_pris']} -> {p['nytt']} (jämförpris {p['fore_jmf']} -> {p['jmf_ut']})")
        return {"skrivna": 0, "hoppade": len(hoppade), "planerade": len(planer)}
    with open(fore_fil, "w", encoding="utf-8") as f:
        json.dump([p for _, p in planer], f, ensure_ascii=False, indent=1)
    n = 0
    for _, p in planer[:canary]:
        skriv_en(klient, p)
        n += 1
    logg(f"canary klar ({n} skrivna och återlästa)")
    for _, p in planer[canary:]:
        skriv_en(klient, p)
        n += 1
    logg(f"klart: {n} skrivna")
    return {"skrivna": n, "hoppade": len(hoppade), "planerade": len(planer)}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--skriv", action="store_true")
    ap.add_argument("--canary", type=int, default=3)
    ap.add_argument("--fore-fil")
    ap.add_argument("--tillat-prisjobb", action="store_true")
    ap.add_argument("--profil")
    a = ap.parse_args(argv)
    import shopify_api
    klient = shopify_api.klient_fran_profil(a.profil) if a.profil else shopify_api.ShopifyKlient()
    try:
        kor(klient, lasa_csv(a.csv), a.skriv, a.canary, a.fore_fil, a.tillat_prisjobb)
    except Stopp as e:
        print("STOPP:", e)
        sys.exit(2)


if __name__ == "__main__":
    main()
