import json,re,urllib.request,time,html
B="https://www.hyprnutrition.se"
def get(u):
    r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 (onboarding-lasning)"})
    try:
        x=urllib.request.urlopen(r,timeout=30);return x.status,x.read().decode("utf-8","replace"),x.geturl()
    except Exception as e: return getattr(e,"code",0),"",u
P=json.load(open("offentlig_products.json"))
# sitemap-sidor
urls=[]
for s in ("sitemap_products_1.xml?from=10547380748631&to=10980883628375","sitemap_pages_1.xml?from=134858932567&to=164630692183","sitemap_collections_1.xml?from=637962584407&to=681928425815","sitemap_blogs_1.xml","sitemap_articles_1.xml"):
    c,t,_=get(f"{B}/{s}");l=re.findall(r"<loc>([^<]+)",t);print(s.split('?')[0],c,len(l));urls+=l
json.dump(urls,open("sitemap_urls.json","w"),indent=1)
rows=[]
pages=[B+"/"]+[u for u in urls if "/products/" in u or "/collections/" in u or "/pages/" in u or "/blogs/" in u]
for u in pages:
    c,t,fu=get(u);time.sleep(.7)
    def f(p,fl=re.S|re.I):
        m=re.search(p,t,fl);return html.unescape(m.group(1)).strip() if m else None
    ld=re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>',t,re.S)
    types=[]
    for j in ld:
        try:
            d=json.loads(j);d=d if isinstance(d,list) else [d]
            types+=[x.get("@type") for x in d]
        except: types.append("ogiltig")
    imgs=re.findall(r"<img\b[^>]*>",t);noalt=[i for i in imgs if not re.search(r'alt="[^"]+"',i)]
    rows.append(dict(url=u,status=c,final=fu,title=f(r"<title[^>]*>(.*?)</title>"),meta=f(r'<meta name="description" content="([^"]*)"'),canon=f(r'<link rel="canonical" href="([^"]*)"'),
      h1=len(re.findall(r"<h1\b",t)),h1txt=f(r"<h1[^>]*>(.*?)</h1>"),ldtypes=types,imgs=len(imgs),noalt=len(noalt),hreflang=len(re.findall(r'hreflang=',t)),robots=f(r'<meta name="robots" content="([^"]*)"'),bytes=len(t)))
    print(c,u,rows[-1]["title"],"|",rows[-1]["ldtypes"])
json.dump(rows,open("sidgranskning.json","w"),ensure_ascii=False,indent=1)
