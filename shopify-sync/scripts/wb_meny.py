#!/usr/bin/env python3
"""Lägger till menylänkar i en meny i Workout Brands. Torrkörning som standard.

Läser hela menyn (med id på alla befintliga rader), sätter in nya rader efter en namngiven rad under en namngiven föräldrasökväg,
och skickar tillbaka HELA trädet med befintliga id:n bevarade. Sparar före-fil. Stoppar om föräldern eller raden inte hittas,
om en ny länk redan finns, eller om återläsningen inte stämmer (alla gamla rader kvar, nya på rätt plats).

Plan (JSON): [{"foralder": ["DAM", "KLÄDER"], "efter": "Jacka", "titel": "Vinterjacka", "url": "/collections/vinterjacka-kvinna", "collection_id": "gid://shopify/Collection/..."}]

Miljövariabler (skrivs i terminalen, aldrig i chatten): SHOPIFY_CLIENT_ID_WB, SHOPIFY_CLIENT_SECRET_WB
Behörighet: write_online_store_navigation (och read_online_store_navigation).
  python3 wb_meny.py --meny startsida-2-0-gymshark --plan plan.json --ut ~/wb_meny              (torrkörning)
  python3 wb_meny.py --meny startsida-2-0-gymshark --plan plan.json --ut ~/wb_meny --skriv
  python3 wb_meny.py --meny startsida-2-0-gymshark --ut ~/wb_meny --aterstall ~/wb_meny/fore_<meny>.json --skriv   (ångra)
"""
import argparse, copy, json, os, sys
from kon_fyll_target_gender import Klient, Stopp

FALT = "id title type resourceId tags url"
LAS = "query { menus(first: 50) { nodes { id handle title items { %s items { %s items { %s items { %s } } } } } } }" % ((FALT,) * 4)
SKRIV = """mutation($id:ID!,$t:String!,$i:[MenuItemUpdateInput!]!){ menuUpdate(id:$id, title:$t, items:$i){ menu{ id handle } userErrors{ field message } } }"""


def hamta_meny(klient, handle):
    for m in klient.graphql(LAS)["menus"]["nodes"]:
        if m["handle"] == handle:
            return m
    raise Stopp(f"Hittade ingen meny med handle {handle}.")


def till_input(items):
    """Läst träd -> MenuItemUpdateInput med id bevarade."""
    ut = []
    for it in items:
        d = {"title": it["title"], "type": it["type"], "tags": it.get("tags") or [],
             "items": till_input(it.get("items") or [])}
        if it.get("id"):  # nya rader saknar id och får ett av Shopify
            d["id"] = it["id"]
        if it.get("resourceId"):
            d["resourceId"] = it["resourceId"]
        if it.get("url"):
            d["url"] = it["url"]
        ut.append(d)
    return ut


def hitta_lista(items, sokvag):
    """Listan (items) under en föräldrasökväg av titlar."""
    lista = items
    for titel in sokvag:
        traffar = [x for x in lista if x["title"].strip() == titel]
        if len(traffar) != 1:
            raise Stopp(f"Föräldern {sokvag}: {len(traffar)} träffar på '{titel}' (väntade exakt 1).")
        lista = traffar[0]["items"]
    return lista


def lagg_till(items, plan):
    nytt = copy.deepcopy(items)
    for p in plan:
        lista = hitta_lista(nytt, p["foralder"])
        if any(x["title"].strip() == p["titel"] or x.get("url") == p["url"] for x in lista):
            raise Stopp(f"{p['foralder']}: '{p['titel']}' finns redan.")
        pos = [i for i, x in enumerate(lista) if x["title"].strip() == p["efter"]]
        if len(pos) != 1:
            raise Stopp(f"{p['foralder']}: {len(pos)} träffar på raden '{p['efter']}' (väntade exakt 1).")
        rad = {"title": p["titel"], "type": "COLLECTION", "resourceId": p["collection_id"], "tags": [], "items": []}
        lista.insert(pos[0] + 1, rad)
    return nytt


def rakna(items):
    return sum(1 + rakna(x.get("items") or []) for x in items)


def titlar(items, pre=""):
    for x in items:
        yield pre + x["title"]
        yield from titlar(x.get("items") or [], pre + x["title"] + " > ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--meny", required=True)
    ap.add_argument("--plan")
    ap.add_argument("--ut", required=True)
    ap.add_argument("--skriv", action="store_true")
    ap.add_argument("--aterstall")
    a = ap.parse_args()
    ut = os.path.expanduser(a.ut)
    os.makedirs(ut, exist_ok=True)
    klient = Klient()
    if klient.graphql("{shop{myshopifyDomain}}")["shop"]["myshopifyDomain"] != "doyou-se.myshopify.com":
        sys.exit("Fel butik. Avbryter.")
    meny = hamta_meny(klient, a.meny)
    fore_fil = os.path.join(ut, f"fore_{a.meny}.json")

    if a.aterstall:
        mal = json.load(open(os.path.expanduser(a.aterstall), encoding="utf-8"))["items"]
        nytt_trad = till_input(mal)
    else:
        if not a.plan:
            sys.exit("--plan saknas.")
        plan = json.load(open(os.path.expanduser(a.plan), encoding="utf-8"))
        nytt = lagg_till(meny["items"], plan)
        nytt_trad = till_input(nytt)
        gamla = set(titlar(meny["items"]))
        print(f"Meny '{a.meny}': {rakna(meny['items'])} rader nu, {rakna(nytt)} efter. Nya rader:")
        for t in titlar(nytt):
            if t not in gamla:
                print("  +", t)

    if not a.skriv:
        print("Torrkörning: inget skrivs. Lägg till --skriv.")
        return
    if not os.path.exists(fore_fil):
        json.dump(meny, open(fore_fil, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("Före-fil sparad:", fore_fil)
    svar = klient.graphql(SKRIV, {"id": meny["id"], "t": meny["title"], "i": nytt_trad})["menuUpdate"]
    if svar["userErrors"]:
        raise Stopp(f"menuUpdate: {svar['userErrors']}")
    efter = hamta_meny(klient, a.meny)
    if not a.aterstall:
        saknas = set(titlar(meny["items"])) - set(titlar(efter["items"]))
        if saknas:
            raise Stopp(f"Återläsning: rader saknas efter skrivningen: {sorted(saknas)[:5]}")
        if rakna(efter["items"]) != rakna(nytt):
            raise Stopp(f"Återläsning: {rakna(efter['items'])} rader, väntade {rakna(nytt)}.")
    print(f"KLART: {rakna(efter['items'])} rader i menyn. Ångra: --aterstall {fore_fil} --skriv")


if __name__ == "__main__":
    try:
        main()
    except Stopp as e:
        sys.exit(f"STOPP: {e}")
