#!/usr/bin/env python3
"""Läsande urval av publiceringskandidater för Workout Brands (inget skrivs i butiken).

Indata: JSON-filer från live-läsning (nodes(ids) med fälten id, handle, title, vendor, productType, tags, status,
totalInventory, mediaCount, variantsCount, description(truncateAt:200), resourcePublications, variants).
Kriterier (alla ska gälla för att inkluderas): status ACTIVE; inte publicerad i någon av de sex synliga publikationerna;
totalInventory > 0; minst en bild; varje variant har unitCost > 0; varje variants pris mellan 20 och 5 000 kr;
ingen variant under inköpspris efter korrigering (marginal med unitCost som den står över 90 % => inköp = unitCost x 11);
inte outlet (vendor eller tagg) och inte Out of stock (vendor eller produkttyp).

Användning: publicering_kandidater_wb.py <katalog-med-json> <ut-katalog>
"""
import sys, os, glob, json, csv, collections

SEX = {"93969055958", "94924406998", "96542359766", "96587284694", "192812089672", "194698805576"}
MOMS = 1.25
KURS = 11.0
PRISJOBB = "price-change-job-active"
KIDS_ORD = ("kids", "barn", "junior")


def marg(pris, ink):
    netto = pris / MOMS
    return (netto - ink) / netto if netto > 0 else None


def orsaker(p):
    o = []
    if p["status"] != "ACTIVE":
        o.append("inte aktiv")
    pubs = {x["publication"]["id"].split("/")[-1] for x in p["resourcePublications"]["nodes"] if x["isPublished"]}
    if pubs & SEX:
        o.append("redan publicerad")
    if (p["totalInventory"] or 0) <= 0:
        o.append("lager 0")
    if (p["mediaCount"]["count"] or 0) < 1:
        o.append("saknar bild")
    vs = p["variants"]["nodes"]
    if len(vs) < p["variantsCount"]["count"]:
        o.append("variantlista ofullständig")
    if any(not (v.get("inventoryItem") or {}).get("unitCost") or float(v["inventoryItem"]["unitCost"]["amount"] or 0) <= 0 for v in vs):
        o.append("variant saknar inköpspris")
    if any(float(v["price"]) < 20 or float(v["price"]) > 5000 for v in vs):
        o.append("pris utanför 20-5000")
    under = False
    for v in vs:
        uc = (v.get("inventoryItem") or {}).get("unitCost")
        if not uc or not uc.get("amount") or float(uc["amount"]) <= 0:
            continue
        ink = float(uc["amount"]); pris = float(v["price"]); jmf = float(v["compareAtPrice"]) if v.get("compareAtPrice") else 0.0
        ordn = jmf if jmf > pris else pris
        m = marg(ordn, ink)
        ink_k = ink * KURS if (m is not None and m > 0.90) else ink
        if pris / MOMS < ink_k:
            under = True
    if under:
        o.append("variant under inköpspris")
    tl = [t.lower() for t in (p["tags"] or [])]
    if "outlet" in (p["vendor"] or "").lower() or any("outlet" in t for t in tl):
        o.append("outlet")
    if (p["vendor"] or "") == "Out of stock" or (p["productType"] or "") == "Out of stock":
        o.append("Out of stock")
    return o


def barn(p):
    t = (p["vendor"] or "").lower() + " " + (p["title"] or "").lower() + " " + (p["productType"] or "").lower() + " " + " ".join(t.lower() for t in (p["tags"] or []))
    return any(k in t for k in KIDS_ORD)


def rad(p, orsak=None):
    vs = p["variants"]["nodes"]; priser = [float(v["price"]) for v in vs]
    r = {"produkt_id": p["legacyResourceId"], "handle": p["handle"], "titel": p["title"], "vendor": p["vendor"], "typ": p["productType"],
         "lager": p["totalInventory"], "antal_bilder": p["mediaCount"]["count"], "antal_varianter": p["variantsCount"]["count"],
         "lagsta_pris": f"{min(priser):.2f}" if priser else "", "hogsta_pris": f"{max(priser):.2f}" if priser else "",
         "prisjobb": "ja" if PRISJOBB in (p["tags"] or []) else "nej", "beskrivning_finns": "ja" if (p.get("description") or "").strip() else "nej",
         "barn": "ja" if barn(p) else "nej", "tags_kort": ", ".join((p["tags"] or [])[:6])}
    if orsak is not None:
        r["orsak"] = "; ".join(orsak)
    return r


def main():
    ind, ut = sys.argv[1:3]
    os.makedirs(ut, exist_ok=True)
    prod = {}
    for f in sorted(glob.glob(os.path.join(ind, "p*.json"))):
        for n in json.load(open(f))["data"]["nodes"]:
            if n:
                prod[n["id"]] = n
    inkl, utes = [], []
    for p in prod.values():
        o = orsaker(p)
        (utes if o else inkl).append((p, o))
    inkl.sort(key=lambda x: -(x[0]["totalInventory"] or 0))
    utes.sort(key=lambda x: -(x[0]["totalInventory"] or 0))
    kol = ["produkt_id", "handle", "titel", "vendor", "typ", "lager", "antal_bilder", "antal_varianter", "lagsta_pris", "hogsta_pris", "prisjobb", "beskrivning_finns", "barn", "tags_kort"]
    with open(os.path.join(ut, "publicering_kandidater.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=kol, delimiter=";"); w.writeheader(); [w.writerow(rad(p)) for p, _ in inkl]
    with open(os.path.join(ut, "publicering_uteslutna.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=kol + ["orsak"], delimiter=";"); w.writeheader(); [w.writerow(rad(p, o)) for p, o in utes]
    s = {"lasta": len(prod), "inkluderade": len(inkl), "uteslutna": len(utes), "lagerenheter_inkl": sum(p["totalInventory"] or 0 for p, _ in inkl)}
    s["orsak_forsta"] = collections.Counter(o[0] for _, o in utes)
    s["orsak_alla"] = collections.Counter(x for _, o in utes for x in o)
    vc = collections.Counter(p["vendor"] for p, _ in inkl)
    s["vendor_topp10"] = [(v, n, sum(p["totalInventory"] or 0 for p, _ in inkl if p["vendor"] == v)) for v, n in vc.most_common(10)]
    s["prisjobb_inkl"] = sum(1 for p, _ in inkl if PRISJOBB in (p["tags"] or []))
    s["utan_beskrivning_inkl"] = sum(1 for p, _ in inkl if not (p.get("description") or "").strip())
    s["barn_inkl"] = sum(1 for p, _ in inkl if barn(p))
    # kanariegrupp: en per vendor, lager fallande, inga prisjobb, inga barn, minst en med beskrivning och 3 bilder
    kand = [p for p, _ in inkl if PRISJOBB not in (p["tags"] or []) and not barn(p) and (p["mediaCount"]["count"] or 0) >= 3 and (p.get("description") or "").strip()]
    kan, vend, typer = [], set(), collections.Counter()
    for p in kand:
        if p["vendor"] in vend or typer[p["productType"]] >= 2:
            continue
        kan.append(p); vend.add(p["vendor"]); typer[p["productType"]] += 1
        if len(kan) == 10:
            break
    # säkra minst 3 med lager över 50
    s["kanarie"] = [rad(p) for p in kan]
    s["kanarie_lager_over_50"] = sum(1 for p in kan if (p["totalInventory"] or 0) > 50)
    json.dump(s, open(os.path.join(ut, "publicering_sammanfattning.json"), "w"), ensure_ascii=False, indent=1, default=dict)
    print(json.dumps({k: v for k, v in s.items() if k != "kanarie"}, ensure_ascii=False, indent=1, default=dict))


if __name__ == "__main__":
    main()
