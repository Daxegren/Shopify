#!/usr/bin/env python3
"""Läsande publik genomsökning av workoutbrands.com (BFS från startsidan). Högst ~2,5 anrop/s, följer robots.txt, neutralt user-agent.
Användning: python3 -I genomsok_wb.py <utkatalog> [max_kollektioner] [max_produkter] [max_ovrigt]"""
import sys,re,json,time,ssl,urllib.request,urllib.error,urllib.parse,collections
out=sys.argv[1]; MAXC=int(sys.argv[2]) if len(sys.argv)>2 else 700; MAXP=int(sys.argv[3]) if len(sys.argv)>3 else 400; MAXO=int(sys.argv[4]) if len(sys.argv)>4 else 60
BASE="https://workoutbrands.com"; UA="Mozilla/5.0 (compatible; SiteReviewBot/1.0; read-only)"
ctx=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
DIS=[r"^/admin",r"^/cart",r"^/checkout",r"^/orders",r"^/account",r"^/services",r"^/collections/.*sort_by",r"^/collections/.*\+",r".*\?.*(sort_by|filter\.|q=)"]
def allowed(path): return not any(re.match(p,path) for p in DIS)
def get(url):
    r=urllib.request.Request(url,headers={"User-Agent":UA,"Accept-Language":"sv"})
    try:
        with urllib.request.urlopen(r,timeout=25,context=ctx) as x: return x.status,x.read().decode("utf8","replace"),dict(x.headers)
    except urllib.error.HTTPError as e: return e.code,"",dict(e.headers)
    except Exception as e: return 0,str(e),{}
def kind(p):
    if p=="/" or p=="": return "home"
    if p.startswith("/collections/") and p.count("/")==2: return "collection"
    if p.startswith("/products/") and p.count("/")==2: return "product"
    if p.startswith("/pages/") or p.startswith("/blogs/"): return "other"
    return None
def parse(h):
    g=lambda rx:(re.search(rx,h,re.S|re.I) or [None,None])[1]
    d={"title":g(r"<title[^>]*>(.*?)</title>"),"meta":g(r'<meta[^>]+name="description"[^>]+content="([^"]*)"') or g(r'<meta[^>]+content="([^"]*)"[^>]+name="description"'),
       "canonical":g(r'<link[^>]+rel="canonical"[^>]+href="([^"]*)"'),"h1":len(re.findall(r"<h1[\s>]",h,re.I)),"robots":g(r'<meta[^>]+name="robots"[^>]+content="([^"]*)"'),
       "hreflang":len(re.findall(r'rel="alternate"[^>]+hreflang=',h)),"jsonld":sorted(set(re.findall(r'"@type"\s*:\s*"(\w+)"',h))),
       "images":len(re.findall(r"<img\b",h,re.I)),"img_no_alt":len(re.findall(r'<img\b(?![^>]*\balt=)[^>]*>',h,re.I)),"bytes":len(h),
       "next":bool(re.search(r'rel="next"',h)),"product_cards":len(set(re.findall(r'href="(?:/[a-z]{2}(?:-[A-Z]{2})?)?/collections/[^"/]+/products/([^"?#]+)|href="/products/([^"?#]+)',h)))}
    return d
def links(h):
    s=set()
    for m in re.findall(r'href="([^"#]+)"',h):
        u=urllib.parse.urljoin(BASE+"/",m); pu=urllib.parse.urlparse(u)
        if pu.netloc not in ("workoutbrands.com","www.workoutbrands.com"): continue
        p=pu.path.rstrip("/") or "/"
        p=re.sub(r"^/collections/([^/]+)/products/","/products/",p)
        s.add(p)
    return s
st,h,hd=get(BASE+"/"); print("start",st,len(h),flush=True)
pages={}; edges=collections.defaultdict(set); depth={"/":0}; queue=collections.deque(["/"]); cnt=collections.Counter(); t0=time.time(); r429=0
cap={"collection":MAXC,"product":MAXP,"other":MAXO,"home":1}
def visit(p):
    global r429
    time.sleep(0.7)
    st,h,hd=get(BASE+p)
    if st==429:
        r429+=1; print("429 vid",p,flush=True); time.sleep(60); st,h,hd=get(BASE+p)
        if st==429:
            pages[p]={'status':429,'kind':kind(p),'depth':depth.get(p)}; time.sleep(30); return False
    rec={"status":st,"kind":kind(p),"depth":depth.get(p)}
    if st==200: rec.update(parse(h)); L=links(h); edges[p]=L
    pages[p]=rec; return rec
visit("/")
for q in list(edges["/"]): pass
while queue and r429<6:
    p=queue.popleft()
    if p!="/" and p in pages: continue
    if p!="/":
        k=kind(p)
        if cnt[k]>=cap[k]: continue
        res=visit(p)
        if res is False: continue
        cnt[k]+=1
    for l in sorted(edges.get(p,[])):
        if l in pages or l in queue or kind(l) is None or not allowed(l): continue
        depth.setdefault(l,depth[p]+1); queue.append(l)
    if len(pages)%50==0: print(len(pages),dict(cnt),round(time.time()-t0),flush=True)
json.dump({"pages":pages,"edges":{k:sorted(v) for k,v in edges.items()},"r429":r429,"sek":round(time.time()-t0)},open(out+"/genomsokning.json","w"),ensure_ascii=False)
print("klart",len(pages),dict(cnt),r429)
