#!/usr/bin/env python3
"""Avpublicerar tomma kollektioner från Webbshop (Workout Brands). Torrkörning som standard.

Bara kollektioner som står i listan (CSV, kolumnen handle) OCH har 0 produkter just nu OCH är publicerade på Webbshop.
Allt annat hoppas över med skäl. Bara Webbshop berörs; övriga kanaler lämnas orörda.
Sparar före-fil, skriver en i taget, läser tillbaka varje och stoppar vid första avvikelse.

Miljövariabler (skrivs i terminalen, aldrig i chatten): SHOPIFY_CLIENT_ID_WB, SHOPIFY_CLIENT_SECRET_WB
Behörighet: write_publications. Saknas den skriver Shopify det i felet.
  python3 wb_avpublicera.py --lista LISTA.csv --ut ~/wb_avpub                       (torrkörning: läser bara)
  python3 wb_avpublicera.py --lista LISTA.csv --ut ~/wb_avpub --skriv --max 1       (kanariefall: en kollektion)
  python3 wb_avpublicera.py --lista LISTA.csv --ut ~/wb_avpub --skriv               (resten)
  python3 wb_avpublicera.py --ut ~/wb_avpub --aterstall ~/wb_avpub/fore.json [--skriv]   (ångra: publicera igen)
"""
import argparse, csv, json, os, sys, time
from kon_fyll_target_gender import Klient, Stopp

WEBBSHOP_APP = "Webbshop"
PUBLIKATIONER = '''{ publications(first: 20) { nodes { id catalog { ... on AppCatalog { apps(first: 3) { nodes { title } } } } } } }'''
LAS = '''query($q:String!,$p:ID!){ collections(first:100, query:$q){ nodes { id handle title productsCount{count}
  publishedOnPublication(publicationId:$p) } } }'''
LAS_ID = '''query($id:ID!,$p:ID!){ collection(id:$id){ id handle productsCount{count} publishedOnPublication(publicationId:$p) } }'''
AVPUBLICERA = '''mutation($id:ID!,$i:[PublicationInput!]!){ publishableUnpublish(id:$id, input:$i){ userErrors{field message} } }'''
PUBLICERA = '''mutation($id:ID!,$i:[PublicationInput!]!){ publishablePublish(id:$id, input:$i){ userErrors{field message} } }'''


def hitta_webbshop(klient):
    for n in klient.graphql(PUBLIKATIONER)["publications"]["nodes"]:
        apps = ((n.get("catalog") or {}).get("apps") or {}).get("nodes") or []
        if any(a.get("title") == WEBBSHOP_APP for a in apps):
            return n["id"]
    raise Stopp("Hittade inte publikationen för Webbshop.")


def las_handles(sokvag):
    with open(sokvag, newline="", encoding="utf-8") as f:
        return [r["handle"].strip() for r in csv.DictReader(f, delimiter=";") if r.get("handle", "").strip()]


def las_kollektioner(klient, handles, pub):
    """handle -> {id, produkter, publicerad}. Hämtar i grupper så att sökfrågan inte blir för lång."""
    ut = {}
    for i in range(0, len(handles), 15):
        q = " OR ".join(f"handle:{h}" for h in handles[i:i + 15])
        for n in klient.graphql(LAS, {"q": q, "p": pub})["collections"]["nodes"]:
            ut[n["handle"]] = {"id": n["id"], "produkter": n["productsCount"]["count"], "publicerad": n["publishedOnPublication"]}
    return ut


def planera(handles, nu):
    att_gora, hoppas = [], []
    for h in handles:
        k = nu.get(h)
        if not k:
            hoppas.append((h, "finns inte i butiken"))
        elif k["produkter"] != 0:
            hoppas.append((h, f"har {k['produkter']} produkter"))
        elif not k["publicerad"]:
            hoppas.append((h, "är redan inte publicerad på Webbshop"))
        else:
            att_gora.append((h, k["id"]))
    return att_gora, hoppas


def kor(klient, pub, kolls, skriv, atgard, forvantat):
    """Skriver en kollektion i taget och läser tillbaka. Stoppar vid första avvikelse."""
    klar = 0
    for h, kid in kolls:
        if not skriv:
            continue
        # läs om precis före skrivning: får fortfarande inte ha produkter (vid avpublicering)
        nu = klient.graphql(LAS_ID, {"id": kid, "p": pub})["collection"]
        if forvantat is False and nu["productsCount"]["count"] != 0:
            raise Stopp(f"{h}: har fått produkter ({nu['productsCount']['count']}), stoppar.")
        svar = klient.graphql(atgard, {"id": kid, "i": [{"publicationId": pub}]})
        fel = list(svar.values())[0]["userErrors"]
        if fel:
            raise Stopp(f"{h}: {fel}")
        efter = klient.graphql(LAS_ID, {"id": kid, "p": pub})["collection"]
        if efter["publishedOnPublication"] != forvantat:
            raise Stopp(f"{h}: återläsning visar publicerad={efter['publishedOnPublication']}, väntade {forvantat}.")
        klar += 1
        print(f"  ok {h}")
        time.sleep(0.6)
    return klar


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lista", help="CSV med kolumnen handle (semikolonseparerad)")
    ap.add_argument("--ut", required=True)
    ap.add_argument("--skriv", action="store_true")
    ap.add_argument("--max", type=int, default=0, help="högst så här många kollektioner (kanariefall)")
    ap.add_argument("--aterstall", help="före-fil att publicera igen")
    a = ap.parse_args()
    ut = os.path.expanduser(a.ut)
    os.makedirs(ut, exist_ok=True)
    klient = Klient()
    butik = klient.graphql("{shop{myshopifyDomain}}")["shop"]["myshopifyDomain"]
    if butik != "doyou-se.myshopify.com":
        sys.exit(f"Fel butik: {butik}. Avbryter.")
    pub = hitta_webbshop(klient)

    if a.aterstall:
        fore = json.load(open(os.path.expanduser(a.aterstall), encoding="utf-8"))
        kolls = [(k["handle"], k["id"]) for k in fore["kollektioner"] if k["publicerad"]]
        print(f"Ångra: {len(kolls)} kollektioner publiceras igen på Webbshop. {'SKRIVER' if a.skriv else 'Torrkörning, inget skrivs.'}")
        n = kor(klient, pub, kolls, a.skriv, PUBLICERA, True)
        print(f"KLART, {n} återpublicerade.")
        return

    if not a.lista:
        sys.exit("--lista saknas.")
    handles = las_handles(os.path.expanduser(a.lista))
    nu = las_kollektioner(klient, handles, pub)
    att_gora, hoppas = planera(handles, nu)
    print(f"{len(handles)} i listan: {len(att_gora)} att avpublicera, {len(hoppas)} hoppas över.")
    for h, skal in hoppas:
        print(f"  hoppar {h}: {skal}")
    fore_fil = os.path.join(ut, "fore.json")
    if a.skriv and not os.path.exists(fore_fil):
        json.dump({"datum": time.strftime("%Y-%m-%d %H:%M"), "publikation": pub,
                   "kollektioner": [{"handle": h, "id": nu[h]["id"], "produkter": nu[h]["produkter"], "publicerad": nu[h]["publicerad"]}
                                    for h in handles if h in nu]}, open(fore_fil, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("Före-fil sparad:", fore_fil)
    if a.max:
        att_gora = att_gora[:a.max]
    if not a.skriv:
        print("Torrkörning: inget skrivs. Lägg till --skriv (börja med --max 1).")
        return
    n = kor(klient, pub, att_gora, True, AVPUBLICERA, False)
    print(f"KLART, {n} avpublicerade på Webbshop. Ångra: --aterstall {fore_fil} --skriv")


if __name__ == "__main__":
    try:
        main()
    except Stopp as e:
        sys.exit(f"STOPP: {e}")
