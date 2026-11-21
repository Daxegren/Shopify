"""Läser byouunderwear.se offentligt (products.json, collections.json, robots, sitemap). Ändrar inget."""
import json, time, urllib.request, sys
B = "https://byouunderwear.se"
def get(path):
    for i in range(4):
        try:
            r = urllib.request.urlopen(urllib.request.Request(B+path, headers={"User-Agent":"Mozilla/5.0 (onboarding-lasning)"}), timeout=30)
            return r.read().decode("utf-8","replace")
        except Exception as e:
            time.sleep(2*(i+1)); err=e
    raise err
def pages(name, key):
    out=[]; p=1
    while True:
        d=json.loads(get(f"/{name}.json?limit=250&page={p}")).get(key,[])
        if not d: break
        out+=d; p+=1
        if len(d)<250: break
        time.sleep(1)
    return out
json.dump(pages("products","products"), open("produkter_publikt.json","w"), ensure_ascii=False)
json.dump(pages("collections","collections"), open("kollektioner_publikt.json","w"), ensure_ascii=False)
for n,p in [("robots.txt","/robots.txt"),("sitemap.xml","/sitemap.xml"),("agents.md","/agents.md"),("hem.html","/")]:
    try: open(n,"w").write(get(p))
    except Exception as e: print("fel",n,e)
