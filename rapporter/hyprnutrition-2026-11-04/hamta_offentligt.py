import json, urllib.request, time, sys
B="https://www.hyprnutrition.se"
def get(u):
    r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 (onboarding-lasning)"})
    return urllib.request.urlopen(r,timeout=30).read().decode()
for kind in ("products","collections"):
    out=[];p=1
    while True:
        try: d=json.loads(get(f"{B}/{kind}.json?limit=250&page={p}"))[kind]
        except Exception as e: print(kind,"fel",e); break
        if not d: break
        out+=d;p+=1;time.sleep(1)
        if len(d)<250: break
    json.dump(out,open(f"offentlig_{kind}.json","w"),ensure_ascii=False)
    print(kind,len(out))
for n,u in (("sitemap","/sitemap.xml"),("robots","/robots.txt"),("agents","/agents.md"),("llms","/llms.txt"),("start","/")):
    try: open(f"offentlig_{n}.txt","w").write(get(B+u)); print(n,"ok")
    except Exception as e: print(n,"fel",e)
