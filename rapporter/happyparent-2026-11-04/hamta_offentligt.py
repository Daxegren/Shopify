"""Hämtar offentliga data från happyparent.store (bara läsning): products.json, collections.json, sitemaps.
Användning: python3 -I hamta_offentligt.py <utkatalog>"""
import json, sys, time, urllib.request, urllib.error, re, os
BAS = "https://www.happyparent.store"
ut = sys.argv[1]
def get(u):
    for i in range(4):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (compatible; onboarding-readonly)"}), timeout=40)
            return r.status, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 429: time.sleep(5 * (i + 1)); continue
            return e.code, ""
        except Exception as e:
            time.sleep(2)
    return 0, ""
def sida(path, nyckel, fil):
    alla, p = [], 1
    while True:
        s, t = get(f"{BAS}/{path}.json?limit=250&page={p}")
        if s != 200: print(path, "status", s); break
        d = json.loads(t).get(nyckel, [])
        if not d: break
        alla += d; p += 1; time.sleep(0.5)
    json.dump(alla, open(os.path.join(ut, fil), "w"), ensure_ascii=False)
    print(path, len(alla))
sida("products", "products", "products.json")
sida("collections", "collections", "collections.json")
