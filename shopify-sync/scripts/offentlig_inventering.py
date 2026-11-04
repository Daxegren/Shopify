#!/usr/bin/env python3
"""Läs-bara-inventering via butikens publika /products.json (inga nycklar). Användning: offentlig_inventering.py <bas-url> <utfil.json>"""
import json, sys, time, urllib.request
bas, ut = sys.argv[1].rstrip("/"), sys.argv[2]
alla, sida = [], 1
while True:
    url = f"{bas}/products.json?limit=250&page={sida}"
    for forsok in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "produktdata-inventering/1.0"}), timeout=60) as r:
                data = json.load(r)["products"]; break
        except Exception as e:
            if forsok == 4: raise
            time.sleep(2 ** forsok)
    if not data: break
    alla += data; sida += 1; time.sleep(0.5)
json.dump(alla, open(ut, "w"), ensure_ascii=False)
print(len(alla), "produkter sparade i", ut)
