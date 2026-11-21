#!/usr/bin/env python3
"""Läsande prisförslagstest för Workout Brands (inget skrivs i butiken).

Eurogruppen = varianter vars marginal med unitCost som den står (formel (pris/1,25 - inköp)/(pris/1,25), ordinarie
pris = jämförpris om det är högre än priset, annars priset) är över 90 %. För dem räknas inköp i kronor som
unitCost x kurs. Övriga räknas med unitCost som den står. Varianter utan inköpspris och varianter under inköpspris
(negativ marginal) redovisas separat och ingår inte i testet. Förslagen räknas med bedom() i pris_forslag.py
(marginal 0,60, golv 0,55, tak 0,65, tolerans 0,03).

Användning: prisforslag_test_wb.py <varianter.ndjson> <ut-katalog> [--kurs 11]
Indata (en variant per rad): produkt_id, variant_id, sku, vendor, tags, pris, jamforpris, inkop (unitCost som den står), lager
"""
import sys, os, csv, json, statistics, argparse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pris_forslag as pf

MARGINAL, GOLV, TAK, TOL = 0.60, 0.55, 0.65, 0.03
BINS = [("under 50", -9, .50), ("50-57", .50, .57), ("57-63", .57, .63), ("63-70", .63, .70), ("70-80", .70, .80), ("over 80", .80, 9)]


def bin_av(m):
    for namn, lo, hi in BINS:
        if lo <= m < hi:
            return namn
    return "over 80"


def klassa(v, kurs):
    """Returnerar (kategori, rad-dict eller None). kategori: euro/ovriga/saknas/under_inkop"""
    pris = v["pris"]; jmf = v["jamforpris"] or 0.0; ink = v["inkop"]
    if ink is None or ink <= 0 or pris is None or pris <= 0:
        return "saknas", None
    rea = bool(jmf and jmf > pris)
    ordn = jmf if rea else pris
    m_ou = pf.marginal_efter_moms(ordn, ink)
    if m_ou is not None and m_ou < 0:
        return "under_inkop", {"marginal_utan_korr": m_ou}
    euro = m_ou is not None and m_ou > 0.90
    ink_sek = ink * kurs if euro else ink
    m_nu = pf.marginal_efter_moms(ordn, ink_sek)
    b = pf.bedom(pris, jmf, ink_sek, v["tags"], v["lager"], marginal=MARGINAL, golv=GOLV, tak=TAK, tolerans=TOL)
    inom = m_nu is not None and abs(m_nu - MARGINAL) <= TOL and not rea
    if b is None:
        # inom toleransen (rörs inte) eller ogiltigt
        nytt, andr, ri, hallen, flag, prisjobb = None, None, "rors_ej", False, [], pf.PRISJOBB in v["tags"]
    else:
        nytt, andr, ri, hallen, flag, prisjobb = b["nytt"], b["andring"], b["riktning"], b["hallen"], b["flaggor"], b["prisjobb"]
    return ("euro" if euro else "ovriga"), {
        "rea": rea, "ordinarie": ordn, "ink_sek": ink_sek, "m_nu": m_nu, "nytt": nytt, "andring": andr,
        "riktning": ri, "hallen": hallen, "flagga": flag, "prisjobb": prisjobb, "inom": inom or (b is None)}


def sammanfatta(rs):
    """rs: lista av (variant, info). Returnerar dict med tal."""
    s = {"varianter": len(rs), "produkter": len({v["produkt_id"] for v, _ in rs})}
    s["bins"] = collections.Counter(bin_av(i["m_nu"]) for _, i in rs)
    s["inom_57_63"] = sum(1 for _, i in rs if i["inom"])
    prop = [(v, i) for v, i in rs if i["andring"] is not None]
    s["hojs"] = sum(1 for _, i in prop if i["riktning"] == "upp")
    s["sanks"] = sum(1 for _, i in prop if i["riktning"] == "ner")
    s["lika"] = sum(1 for _, i in prop if i["riktning"] == "lika")
    s["hallen"] = sum(1 for _, i in prop if i["hallen"])
    s["hallen_upp"] = sum(1 for _, i in prop if i["hallen"] and i["riktning"] == "upp")
    s["hallen_ner"] = sum(1 for _, i in prop if i["hallen"] and i["riktning"] == "ner")
    a = [i["andring"] * 100 for _, i in prop]
    a2 = [i["andring"] * 100 for _, i in prop if not i["hallen"]]
    s["median_andring"] = statistics.median(a) if a else None
    s["medel_andring"] = statistics.mean(a) if a else None
    s["median_andring_utan_hallna"] = statistics.median(a2) if a2 else None
    s["medel_andring_utan_hallna"] = statistics.mean(a2) if a2 else None
    s["prisjobb"] = sum(1 for v, i in rs if pf.PRISJOBB in v["tags"])
    s["rea"] = sum(1 for _, i in rs if i["rea"])
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("indata"); ap.add_argument("ut")
    ap.add_argument("--kurs", type=float, default=11.0)
    a = ap.parse_args()
    os.makedirs(a.ut, exist_ok=True)
    vs = [json.loads(l) for l in open(a.indata, encoding="utf-8")]
    res = {}
    for kurs in (a.kurs, 10.0, 12.0):
        by = collections.defaultdict(list); sep = collections.defaultdict(list)
        for v in vs:
            kat, info = klassa(v, kurs)
            if kat in ("euro", "ovriga"):
                by[kat].append((v, info))
            else:
                sep[kat].append(v)
        res[kurs] = (by, sep)
    by, sep = res[a.kurs]
    # variantfil
    kol = ["produkt_id", "variant_id", "sku", "vendor", "pris_nu", "jamforpris", "inkop_i_shopify", "inkop_sek_korrigerat", "grupp",
           "marginal_nu_pct", "nytt_pris", "andring_pct", "riktning", "hallen", "prisjobb", "rea", "flagga", "godkand"]
    with open(os.path.join(a.ut, "prisforslag_test_wb_11kr.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(kol)
        for grupp in ("euro", "ovriga"):
            for v, i in by[grupp]:
                w.writerow([v["produkt_id"], v["variant_id"], v["sku"] or "", v["vendor"], f"{v['pris']:.2f}",
                            f"{v['jamforpris']:.2f}" if v["jamforpris"] else "", f"{v['inkop']:.2f}", f"{i['ink_sek']:.2f}", grupp,
                            f"{i['m_nu']*100:.1f}", f"{i['nytt']:.2f}" if i["nytt"] else "",
                            f"{i['andring']*100:.1f}" if i["andring"] is not None else "", i["riktning"], int(i["hallen"]),
                            int(i["prisjobb"]), int(i["rea"]), "|".join(i["flagga"]), ""])
    with open(os.path.join(a.ut, "prisforslag_test_wb_utanfor_test.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(["produkt_id", "variant_id", "sku", "vendor", "pris_nu", "jamforpris", "inkop_i_shopify", "kategori"])
        for kat in ("saknas", "under_inkop"):
            for v in sep[kat]:
                w.writerow([v["produkt_id"], v["variant_id"], v["sku"] or "", v["vendor"], f"{v['pris']:.2f}" if v["pris"] is not None else "",
                            f"{v['jamforpris']:.2f}" if v["jamforpris"] else "", f"{v['inkop']:.2f}" if v["inkop"] is not None else "", kat])
    out = {"kurs": a.kurs, "totalt_varianter": len(vs), "totalt_produkter": len({v["produkt_id"] for v in vs}),
           "saknar_inkop": len(sep["saknas"]), "under_inkop": len(sep["under_inkop"])}
    out["grupper"] = {g: sammanfatta(by[g]) for g in ("euro", "ovriga")}
    # per vendor topp 15
    vc = collections.Counter(v["vendor"] for g in ("euro", "ovriga") for v, _ in by[g])
    out["vendor"] = {}
    for ven, _ in vc.most_common(15):
        tot = [(v, i) for g in ("euro", "ovriga") for v, i in by[g] if v["vendor"] == ven]
        eu = [(v, i) for v, i in by["euro"] if v["vendor"] == ven]
        d = sammanfatta(tot); d["euro_varianter"] = len(eu); out["vendor"][ven] = d
    # känslighet
    out["kanslighet"] = {}
    for kurs, (b2, _) in res.items():
        out["kanslighet"][str(kurs)] = {g: {k: sammanfatta(b2[g])[k] for k in ("varianter", "inom_57_63", "hojs", "sanks", "hallen")} for g in ("euro", "ovriga")}
    json.dump(out, open(os.path.join(a.ut, "prisforslag_test_wb_sammanfattning.json"), "w"), ensure_ascii=False, indent=1, default=dict)
    print(json.dumps(out, ensure_ascii=False, indent=1, default=dict)[:6000])


if __name__ == "__main__":
    main()
