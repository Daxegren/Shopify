#!/usr/bin/env python3
"""Läsande export ur Workout Brands (doyou-se). Skriver ingenting i butiken.

1) Bulkoperation: alla produkter och kollektioner (titel, status, taggar, kategori, SEO, könsfält, bilder utan alt-text).
2) Översättningstäckning per språk (title, body_html, meta_title, meta_description) för produkter och kollektioner.

Miljövariabler (skrivs i terminalen, aldrig i chatten): SHOPIFY_CLIENT_ID_WB, SHOPIFY_CLIENT_SECRET_WB
  python3 wb_export.py --ut ~/wb_export                     (allt)
  python3 wb_export.py --ut ~/wb_export --bara bulk         (bara steg 1)
  python3 wb_export.py --ut ~/wb_export --bara oversattning (bara steg 2; hoppar över språk som redan är klara)
"""
import argparse, csv, json, os, sys, time, urllib.request
from kon_fyll_target_gender import Klient, Stopp

BULK_PRODUKTER = '''{ products { edges { node { id handle title status vendor productType tags category{fullName} seo{title description} description
  tg: metafield(namespace:"shopify", key:"target-gender"){value}
  media { edges { node { ... on MediaImage { id alt } } } } } } } }'''
BULK_KOLLEKTIONER = '''{ collections { edges { node { id handle title seo{title description} description productsCount{count} } } } }'''
START = '''mutation($q:String!){bulkOperationRunQuery(query:$q){bulkOperation{id status} userErrors{field message}}}'''
STATUS = '''query($id:ID!){ node(id:$id){ ... on BulkOperation{ id status errorCode objectCount url } } }'''
SPRAK = '''{ shopLocales { locale primary published } }'''
OVS = '''query($t:TranslatableResourceType!,$loc:String!,$after:String){translatableResources(resourceType:$t,first:100,after:$after){
  pageInfo{hasNextPage endCursor} edges{node{resourceId translatableContent{key} translations(locale:$loc){key outdated}}}}}'''
NYCKLAR = ("title", "body_html", "meta_title", "meta_description")


def kor_bulk(k, fraga, fil, logg=print, vantetid=15):
    d = k.graphql(START, {"q": fraga})["bulkOperationRunQuery"]
    if d["userErrors"]:
        raise Stopp(f"bulk start: {d['userErrors']}")
    bid = d["bulkOperation"]["id"]
    while True:
        time.sleep(vantetid)
        s = k.graphql(STATUS, {"id": bid})["node"]
        logg(f"  bulk: {s['status']} {s.get('objectCount')}")
        if s["status"] == "COMPLETED":
            break
        if s["status"] in ("FAILED", "CANCELED", "EXPIRED"):
            raise Stopp(f"bulk misslyckades: {s}")
    if s.get("url"):
        urllib.request.urlretrieve(s["url"], fil)
    else:
        open(fil, "w").close()
    return fil


def las_jsonl(fil):
    rader = {}
    for rad in open(fil, encoding="utf-8"):
        o = json.loads(rad)
        if "__parentId" in o:
            rader.setdefault(o["__parentId"], {"barn": []})["barn"].append(o)
        else:
            rader.setdefault(o["id"], {"barn": []})["nod"] = o
    return [(v["nod"], v["barn"]) for v in rader.values() if "nod" in v]


def produkt_rad(n, barn):
    bilder = [b for b in barn if b.get("id", "").startswith("gid://shopify/MediaImage")]
    return {"id": n["id"].rsplit("/", 1)[1], "handle": n["handle"], "titel": n["title"], "status": n["status"], "marke": n["vendor"],
            "produkttyp": n["productType"], "kategori": (n.get("category") or {}).get("fullName", ""), "taggar": ",".join(n["tags"]),
            "seo_titel": (n.get("seo") or {}).get("title") or "", "seo_beskrivning": (n.get("seo") or {}).get("description") or "",
            "kon_varde": (n.get("tg") or {}).get("value") or "", "beskrivning_tecken": len(n.get("description") or ""),
            "antal_bilder": len(bilder), "bilder_utan_alt": sum(1 for b in bilder if not (b.get("alt") or "").strip())}


def kollektion_rad(n, _barn):
    return {"id": n["id"].rsplit("/", 1)[1], "handle": n["handle"], "titel": n["title"], "seo_titel": (n.get("seo") or {}).get("title") or "",
            "seo_beskrivning": (n.get("seo") or {}).get("description") or "", "antal_produkter": (n.get("productsCount") or {}).get("count", ""),
            "beskrivning_tecken": len(n.get("description") or "")}


def skriv_csv(sokvag, rader):
    with open(sokvag, "w", encoding="utf-8", newline="") as f:
        if rader:
            w = csv.DictWriter(f, fieldnames=list(rader[0]), delimiter=";"); w.writeheader(); w.writerows(rader)


def tackning(noder):
    """noder: [(resourceId, {nyckel i källan}, {nyckel: outdated})] -> räkning per nyckel."""
    r = {k: {"finns_i_kalla": 0, "oversatt": 0, "foraldrad": 0} for k in NYCKLAR}
    for _, kalla, ovs in noder:
        for k in NYCKLAR:
            if k in kalla:
                r[k]["finns_i_kalla"] += 1
                if k in ovs:
                    r[k]["oversatt"] += 1
                    r[k]["foraldrad"] += 1 if ovs[k] else 0
    return r


def oversattning(k, locale, typ, logg=print):
    noder, after = [], None
    while True:
        d = k.graphql(OVS, {"t": typ, "loc": locale, "after": after})["translatableResources"]
        for e in d["edges"]:
            n = e["node"]
            noder.append((n["resourceId"], {c["key"] for c in n["translatableContent"]}, {t["key"]: t["outdated"] for t in n["translations"]}))
        if not d["pageInfo"]["hasNextPage"]:
            return noder
        after = d["pageInfo"]["endCursor"]
        if len(noder) % 1000 < 100:
            logg(f"    {typ} {locale}: {len(noder)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ut", required=True)
    ap.add_argument("--bara", choices=["bulk", "oversattning"])
    a = ap.parse_args()
    ut = os.path.expanduser(a.ut); os.makedirs(ut, exist_ok=True)
    k = Klient()
    try:
        if a.bara in (None, "bulk"):
            for namn, fraga, radfn in (("produkter", BULK_PRODUKTER, produkt_rad), ("kollektioner", BULK_KOLLEKTIONER, kollektion_rad)):
                print(f"Bulk: {namn}")
                fil = kor_bulk(k, fraga, os.path.join(ut, f"{namn}.jsonl"))
                rader = [radfn(n, b) for n, b in las_jsonl(fil)]
                skriv_csv(os.path.join(ut, f"{namn}.csv"), rader)
                print(f"  {len(rader)} rader -> {namn}.csv")
        if a.bara in (None, "oversattning"):
            sprak = [s["locale"] for s in k.graphql(SPRAK)["shopLocales"] if not s["primary"]]
            print("Språk:", ", ".join(sprak))
            sam = os.path.join(ut, "oversattning_sammanfattning.csv")
            rader = list(csv.DictReader(open(sam, encoding="utf-8"), delimiter=";")) if os.path.exists(sam) else []
            klara = {(r["sprak"], r["typ"]) for r in rader}
            for loc in sprak:
                for typ in ("PRODUCT", "COLLECTION"):
                    if (loc, typ) in klara:
                        continue
                    print(f"  {loc} {typ}")
                    t = tackning(oversattning(k, loc, typ))
                    for nyckel, v in t.items():
                        rader.append({"sprak": loc, "typ": typ, "nyckel": nyckel, **v})
                    skriv_csv(sam, rader)
        print("KLART ->", ut)
    except Stopp as e:
        print("STOPP:", e); sys.exit(2)


if __name__ == "__main__":
    main()
