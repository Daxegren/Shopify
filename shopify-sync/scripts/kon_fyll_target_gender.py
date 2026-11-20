#!/usr/bin/env python3
"""Fyller produktfältet shopify.target-gender ("Avsett för") från en godkänd mappningsfil. Torrkörning som standard.

Skriver bara det fältet. Rör inte priser, taggar, texter eller status. Hoppar över produkter som redan har ett annat
värde i fältet (om inte --overskriv), icke-aktiva produkter och produkter som inte finns. Före-fil sparas, varje grupp
läses tillbaka och körningen stoppar vid första avvikelse. Kan köras om: redan rätt värde hoppas över.

Miljövariabler (skrivs i terminalen, aldrig i chatten): SHOPIFY_CLIENT_ID_WB, SHOPIFY_CLIENT_SECRET_WB
  python3 kon_fyll_target_gender.py --csv kon_mapping.csv                      (torrkörning)
  python3 kon_fyll_target_gender.py --csv kon_mapping.csv --skriv --max 10 --fore-fil fore_kon.json   (kanariefall)
  python3 kon_fyll_target_gender.py --csv kon_mapping.csv --skriv --fore-fil fore_kon.json            (resten)
"""
import argparse, csv, json, os, sys, time, urllib.parse, urllib.request, urllib.error

BUTIK = os.environ.get("SHOPIFY_BUTIK", "doyou-se.myshopify.com")  # t.ex. gs-nordic-production.myshopify.com för Gorilla Sports
API = os.environ.get("SHOPIFY_API_VERSION", "2026-07")
VARDEN = {  # klass i mappningsfilen -> metaobjekt (Avsett för)
    "dam": ["gid://shopify/Metaobject/115133645128"],
    "herr": ["gid://shopify/Metaobject/115381502280"],
    "unisex": ["gid://shopify/Metaobject/115213959496"],
    "dam+herr": ["gid://shopify/Metaobject/115133645128", "gid://shopify/Metaobject/115381502280"],
}
LASA = '''query($ids:[ID!]!){nodes(ids:$ids){... on Product{id status tg:metafield(namespace:"shopify",key:"target-gender"){value}}}}'''
KAT = '''query($ids:[ID!]!){nodes(ids:$ids){... on Product{id title category{fullName}}}}'''
SKRIV = '''mutation($m:[MetafieldsSetInput!]!){metafieldsSet(metafields:$m){metafields{id key} userErrors{field message code}}}'''


class Stopp(Exception):
    pass


class Klient:
    def __init__(self, transport=None, sleep=time.sleep):
        self.t = transport or self._http
        self.sleep = sleep
        self.token = None

    @staticmethod
    def _http(url, headers, body):
        req = urllib.request.Request(url, data=body, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.status, r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode("utf-8", "replace")

    def hamta_token(self):
        # Alternativ 1: en färdig Admin API-token (äldre egen app): SHOPIFY_ADMIN_TOKEN. Alternativ 2: klient-id och hemlighet
        # (SHOPIFY_CLIENT_ID / SHOPIFY_CLIENT_SECRET, eller de gamla namnen med suffix _WB).
        fardig = os.environ.get("SHOPIFY_ADMIN_TOKEN")
        if fardig:
            self.token = fardig
            return
        cid = os.environ.get("SHOPIFY_CLIENT_ID") or os.environ.get("SHOPIFY_CLIENT_ID_WB")
        sec = os.environ.get("SHOPIFY_CLIENT_SECRET") or os.environ.get("SHOPIFY_CLIENT_SECRET_WB")
        if not cid or not sec:
            raise Stopp("SHOPIFY_CLIENT_ID och SHOPIFY_CLIENT_SECRET (eller SHOPIFY_ADMIN_TOKEN) måste vara satta i terminalen")
        body = urllib.parse.urlencode({"grant_type": "client_credentials", "client_id": cid, "client_secret": sec}).encode()
        st, txt = self.t(f"https://{BUTIK}/admin/oauth/access_token", {"Content-Type": "application/x-www-form-urlencoded"}, body)
        if st != 200 or "access_token" not in txt:
            raise Stopp(f"Token misslyckades: HTTP {st} {txt[:150]}")
        self.token = json.loads(txt)["access_token"]

    def graphql(self, q, v=None):
        if self.token is None:
            self.hamta_token()
        body = json.dumps({"query": q, "variables": v or {}}).encode()
        for forsok in range(1, 7):
            st, txt = self.t(f"https://{BUTIK}/admin/api/{API}/graphql.json",
                             {"Content-Type": "application/json", "X-Shopify-Access-Token": self.token}, body)
            if st == 401 and forsok == 1:
                self.token = None; self.hamta_token(); continue
            if st == 429 or st >= 500:
                self.sleep(min(2 ** forsok, 30)); continue
            if st != 200:
                raise Stopp(f"HTTP {st}: {txt[:200]}")
            d = json.loads(txt)
            if d.get("errors"):
                if any((e.get("extensions") or {}).get("code") == "THROTTLED" for e in d["errors"] if isinstance(e, dict)):
                    self.sleep(min(2 ** forsok, 30)); continue
                raise Stopp("GraphQL-fel: " + json.dumps(d["errors"], ensure_ascii=False)[:300])
            return d["data"]
        raise Stopp("Gav upp efter 6 försök")


def lasa_mappning(sokvag):
    ut = {}
    for r in csv.DictReader(open(sokvag, encoding="utf-8"), delimiter=";"):
        v = (r.get("varden") or "").strip().lower()
        if v not in VARDEN:
            raise Stopp(f"okänt värde '{v}' för produkt {r.get('produkt_id')}")
        ut[int(r["produkt_id"])] = v
    return ut


def gid(i):
    return f"gid://shopify/Product/{i}"


def onskat(v):
    return sorted(VARDEN[v])


def tolka(varde):
    if not varde:
        return None
    try:
        return sorted(json.loads(varde))
    except Exception:
        return ["?"]


def planera(klient, mapp, overskriv=False, logg=print):
    ids = list(mapp)
    skriv, hoppa = [], {"redan_ratt": 0, "annat_varde": 0, "ej_aktiv_eller_saknas": 0}
    fore = []
    for k in range(0, len(ids), 50):
        d = klient.graphql(LASA, {"ids": [gid(i) for i in ids[k:k + 50]]})["nodes"]
        for i, n in zip(ids[k:k + 50], d):
            if not n or n.get("status") != "ACTIVE":
                hoppa["ej_aktiv_eller_saknas"] += 1; continue
            nu = tolka((n.get("tg") or {}).get("value"))
            if nu == onskat(mapp[i]):
                hoppa["redan_ratt"] += 1; continue
            if nu is not None and not overskriv:
                hoppa["annat_varde"] += 1; continue
            skriv.append(i); fore.append({"produkt_id": i, "tidigare": nu})
        if (k // 50) % 20 == 0:
            logg(f"läst {min(k + 50, len(ids))} av {len(ids)}")
    return skriv, hoppa, fore


def _satt(klient, grupp, mapp):
    m = [{"ownerId": gid(i), "namespace": "shopify", "key": "target-gender", "type": "list.metaobject_reference",
          "value": json.dumps(VARDEN[mapp[i]])} for i in grupp]
    return klient.graphql(SKRIV, {"m": m})["metafieldsSet"]["userErrors"]


def _verifiera(klient, grupp, mapp):
    r = klient.graphql(LASA, {"ids": [gid(i) for i in grupp]})["nodes"]
    for i, n in zip(grupp, r):
        if tolka((n.get("tg") or {}).get("value")) != onskat(mapp[i]):
            raise Stopp(f"återläsning avviker för produkt {i}: {(n.get('tg') or {}).get('value')}")


def skriv_grupp(klient, grupp, mapp):
    """Skriver en grupp. Nekade produkter pekas ut av felindexen i svaret och skrivs inte; resten skrivs i ett anrop.
    Om svaret inte går att tolka provas varje produkt för sig. Returnerar lista (id, felmeddelande)."""
    fel = _satt(klient, grupp, mapp)
    if not fel:
        _verifiera(klient, grupp, mapp)
        return []
    dalig = {}
    for e in fel:
        f = e.get("field") or []
        if len(f) >= 2 and f[0] == "metafields" and str(f[1]).isdigit() and int(f[1]) < len(grupp):
            dalig[int(f[1])] = e["message"]
        else:
            dalig = None
            break
    misslyckade = []
    if dalig:
        misslyckade = [(grupp[ix], m) for ix, m in sorted(dalig.items())]
        rest = [i for ix, i in enumerate(grupp) if ix not in dalig]
        if not rest:
            return misslyckade
        if not _satt(klient, rest, mapp):
            _verifiera(klient, rest, mapp)
            return misslyckade
        grupp = rest
    ok = []
    for i in grupp:
        e = _satt(klient, [i], mapp)
        if e:
            misslyckade.append((i, "; ".join(x["message"] for x in e)))
        else:
            ok.append(i)
    if ok:
        _verifiera(klient, ok, mapp)
    return misslyckade


def kor(klient, mapp, skriv=False, max_n=0, fore_fil=None, overskriv=False, fel_fil=None, max_fel=50, logg=print):
    att, hoppa, fore = planera(klient, mapp, overskriv, logg)
    logg(f"att skriva: {len(att)}; hoppas över: {hoppa}")
    if not skriv:
        return {"skrivna": 0, "att_skriva": len(att), "hoppa": hoppa, "misslyckade": 0}
    if not fore_fil:
        raise Stopp("--fore-fil krävs vid skrivning")
    if max_n:
        att = att[:max_n]; fore = fore[:max_n]
    with open(fore_fil, "w", encoding="utf-8") as f:
        json.dump(fore, f)
    n, alla_fel = 0, []
    for k in range(0, len(att), 25):
        grupp = att[k:k + 25]
        fel = skriv_grupp(klient, grupp, mapp)
        alla_fel += fel
        n += len(grupp) - len(fel)
        if (k // 25) % 10 == 0:
            logg(f"försökt {k + len(grupp)} av {len(att)}; skrivna {n}; misslyckade {len(alla_fel)}")
        if len(alla_fel) > max_fel:
            logg(f"STOPP: fler än {max_fel} misslyckade")
            break
        klient.sleep(0.4)
    if alla_fel and fel_fil:
        kat = {}
        for k in range(0, len(alla_fel), 50):
            ids = [i for i, _ in alla_fel[k:k + 50]]
            for i, nod in zip(ids, klient.graphql(KAT, {"ids": [gid(x) for x in ids]})["nodes"]):
                kat[i] = ((nod or {}).get("category") or {}).get("fullName", "(ingen kategori)")
        with open(fel_fil, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f, delimiter=";"); w.writerow(["produkt_id", "kategori", "felmeddelande"])
            for i, m in alla_fel:
                w.writerow([i, kat.get(i, ""), m])
    logg(f"klart: {n} skrivna och återlästa, {len(alla_fel)} misslyckade" + (f" (se {fel_fil})" if alla_fel and fel_fil else ""))
    return {"skrivna": n, "att_skriva": len(att), "hoppa": hoppa, "misslyckade": len(alla_fel)}


NAMN = {v[0] if len(v) == 1 else "+".join(v): k for k, v in VARDEN.items()}
TITEL = '''query($ids:[ID!]!){nodes(ids:$ids){... on Product{id title vendor productType status tags tg:metafield(namespace:"shopify",key:"target-gender"){value}}}}'''


def lista_annat(klient, mapp, ut):
    """LÄSER bara. Skriver en CSV över produkter vars fält redan har ett värde som skiljer sig från mappningen."""
    ids, rader = list(mapp), []
    for k in range(0, len(ids), 50):
        for i, n in zip(ids[k:k + 50], klient.graphql(TITEL, {"ids": [gid(x) for x in ids[k:k + 50]]})["nodes"]):
            nu = tolka(((n or {}).get("tg") or {}).get("value"))
            if not n or nu is None or nu == onskat(mapp[i]):
                continue
            namn = "+".join(NAMN.get(g, g) for g in nu)
            rader.append({"produkt_id": i, "titel": n["title"], "marke": n["vendor"], "produkttyp": n["productType"],
                          "tagg_kon": ",".join(t for t in n["tags"] if t.lower() in ("men", "ladies", "unisex", "women", "kids")),
                          "nuvarande": namn, "mappning": mapp[i], "status": n["status"]})
    with open(ut, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["produkt_id", "titel", "marke", "produkttyp", "tagg_kon", "nuvarande", "mappning", "status"], delimiter=";")
        w.writeheader(); w.writerows(rader)
    return len(rader)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--skriv", action="store_true")
    ap.add_argument("--max", type=int, default=0)
    ap.add_argument("--fore-fil")
    ap.add_argument("--overskriv", action="store_true")
    ap.add_argument("--fel-fil", default="misslyckade_kon.csv")
    ap.add_argument("--max-fel", type=int, default=50)
    ap.add_argument("--lista-annat", metavar="UT", help="skriv CSV över produkter med annat värde (läser bara)")
    a = ap.parse_args()
    try:
        if a.lista_annat:
            print(lista_annat(Klient(), lasa_mappning(a.csv), a.lista_annat), "rader"); return
        kor(Klient(), lasa_mappning(a.csv), a.skriv, a.max, a.fore_fil, a.overskriv, a.fel_fil, a.max_fel)
    except Stopp as e:
        print("STOPP:", e); sys.exit(2)


if __name__ == "__main__":
    main()
