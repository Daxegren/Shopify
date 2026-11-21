"""Läser offentliga sidor på byouunderwear.se och sammanfattar SEO-element. Ändrar inget."""
import json,re,time,urllib.request,html
B="https://byouunderwear.se"
def get(path):
    r=urllib.request.urlopen(urllib.request.Request(B+path,headers={"User-Agent":"Mozilla/5.0 (onboarding-lasning)"}),timeout=30)
    return r.geturl(), r.read().decode("utf-8","replace")
prod=json.load(open("produkter_publikt.json")); col=json.load(open("kollektioner_publikt.json"))
paths=["/"]+[f"/collections/{c['handle']}" for c in col]+[f"/products/{p['handle']}" for p in prod]
paths+=["/policies/refund-policy","/policies/shipping-policy","/pages/kontakt","/pages/storleksguide","/da","/en","/fi","/de","/sitemap_agentic_discovery.xml"]
res=[]
for p in paths:
    try: u,h=get(p)
    except Exception as e: res.append({"path":p,"fel":str(e)}); time.sleep(1); continue
    t=re.search(r'<title[^>]*>(.*?)</title>',h,re.S)
    m=re.search(r'<meta[^>]+name="description"[^>]+content="([^"]*)"',h)
    can=re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]*)"',h)
    rob=re.findall(r'<meta[^>]+name="robots"[^>]+content="([^"]*)"',h)
    hre=re.findall(r'<link[^>]+rel="alternate"[^>]+hreflang="([^"]*)"',h)
    h1=[re.sub(r'<[^>]+>','',x).strip() for x in re.findall(r'<h1[^>]*>(.*?)</h1>',h,re.S)]
    h2=len(re.findall(r'<h2',h))
    ld=[]
    for b in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>',h,re.S):
        try:
            j=json.loads(b); ld+= j if isinstance(j,list) else [j]
        except Exception: ld.append({"@type":"UGILTIG"})
    types=[x.get("@type") for x in ld]
    imgs=re.findall(r'<img\b[^>]*>',h); noalt=sum(1 for i in imgs if not re.search(r'alt="[^"]+"',i))
    prodld=[x for x in ld if x.get("@type")=="Product"]
    pinfo=None
    if prodld:
        x=prodld[0]; o=x.get("offers"); o=o if isinstance(o,list) else [o] if o else []
        pinfo={"keys":sorted(x.keys()),"offers":len(o),"offer_keys":sorted(o[0].keys()) if o else [],"brand":x.get("brand"),"sku":x.get("sku"),"gtin":[k for k in x if k.startswith("gtin")],"rating":"aggregateRating" in x,"material":x.get("material"),"size":x.get("size")}
    res.append({"path":p,"final":u.replace(B,""),"len":len(h),"title":html.unescape(t.group(1).strip()) if t else None,"meta":html.unescape(m.group(1)) if m else None,"canonical":can,"robots":rob,"hreflang":hre,"h1":h1,"h2":h2,"ld_types":types,"product":pinfo,"imgs":len(imgs),"imgs_utan_alt":noalt,"jsonld_ogiltig":"UGILTIG" in types})
    time.sleep(0.7)
json.dump(res,open("sidor_genomlysning.json","w"),ensure_ascii=False,indent=1)
