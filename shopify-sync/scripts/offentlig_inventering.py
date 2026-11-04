#!/usr/bin/env python3
"""Offentlig, skrivskyddad inventering av en Shopify-butik via publika GET-adresser
(/products.json, /collections.json, /robots.txt, /sitemap.xml, /llms.txt). Ingen inloggning, inget skrivs.
Användning: python3 -I offentlig_inventering.py <basurl> <utkatalog> [--max-sidor N]
Sparar rådata som JSON i utkatalogen. Max ~1 anrop/sekund."""
import json, sys, time, urllib.request, urllib.error, os

UA = "Mozilla/5.0 (compatible; produktdata-genomlysning/1.0; las-endast)"

def hamta(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "sv"})
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.status, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and i < tries - 1:
                time.sleep(5 * (i + 1)); continue
            return e.code, ""
        except Exception as e:
            if i == tries - 1:
                return 0, str(e)
            time.sleep(3)
    return 0, ""

def main():
    bas = sys.argv[1].rstrip("/"); ut = sys.argv[2]
    maxs = int(sys.argv[sys.argv.index("--max-sidor") + 1]) if "--max-sidor" in sys.argv else 40
    os.makedirs(ut, exist_ok=True)
    prod = []
    for sida in range(1, maxs + 1):
        st, txt = hamta(f"{bas}/products.json?limit=250&page={sida}")
        time.sleep(1)
        if st != 200: print("products.json", sida, st); break
        d = json.loads(txt).get("products", [])
        if not d: break
        prod += d
    json.dump(prod, open(f"{ut}/products_public.json", "w"), ensure_ascii=False)
    kol = []
    for sida in range(1, 20):
        st, txt = hamta(f"{bas}/collections.json?limit=250&page={sida}")
        time.sleep(1)
        if st != 200: print("collections.json", sida, st); break
        d = json.loads(txt).get("collections", [])
        if not d: break
        kol += d
    json.dump(kol, open(f"{ut}/collections_public.json", "w"), ensure_ascii=False)
    for namn in ("robots.txt", "sitemap.xml", "llms.txt", ".well-known/ucp"):
        st, txt = hamta(f"{bas}/{namn}"); time.sleep(1)
        open(f"{ut}/{namn.replace('/', '_')}", "w").write(f"HTTP {st}\n{txt}")
    print(bas, "produkter", len(prod), "kollektioner", len(kol))
main()
