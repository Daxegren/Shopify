#!/usr/bin/env python3
"""Butiksoberoende, skrivskyddad inventering av en Shopify-butiks OFFENTLIGA produktdata (/products.json).
Hämtar bara publicerade produkter. Sparar råfil och sammanställning i angiven mapp. Ändrar inget.
Användning: python3 -I offentlig_inventering.py https://exempel.com <utmapp> [--paus 1.0]"""
import sys, json, time, re, collections, urllib.request, os

def hamta(url):
    req = urllib.request.Request(url, headers={"User-Agent": "produktdata-inventering/1.0"})
    for f in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            if f == 4: raise
            time.sleep(2 ** f)

def main():
    bas, ut = sys.argv[1].rstrip("/"), sys.argv[2]
    paus = float(sys.argv[sys.argv.index("--paus") + 1]) if "--paus" in sys.argv else 1.0
    os.makedirs(ut, exist_ok=True)
    alla, sida = [], 1
    while True:
        d = hamta(f"{bas}/products.json?limit=250&page={sida}")["products"]
        if not d: break
        alla += d; sida += 1; time.sleep(paus)
    with open(f"{ut}/produkter_offentliga.json", "w") as f:
        json.dump(alla, f, ensure_ascii=False)
    print("produkter:", len(alla))

if __name__ == "__main__":
    main()
