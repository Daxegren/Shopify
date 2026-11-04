"""Läser ett urval offentliga sidor (bara GET) och sammanfattar titel, meta, H1, canonical, hreflang, JSON-LD, bilder/alt, länkar.
python3 -I genomlysning_offentlig.py <mapp>"""
import json,re,sys,urllib.request,html,time,collections
m=sys.argv[1];B="https://www.happyparent.store"
P=json.load(open(f'{m}/raw/products.json'));C=json.load(open(f'{m}/raw/collections.json'))
def get(u):
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 (compatible; onboarding-readonly)"}),timeout=40);return r.status,r.read().decode('utf-8','replace'),r.geturl()
    except urllib.error.HTTPError as e: return e.code,'',u
    except Exception as e: return 0,str(e),u
def an(u):
    s,h,fu=get(u);time.sleep(0.6)
    if s!=200: return dict(url=u,status=s)
    g=lambda r:(re.findall(r,h,re.S|re.I))
    ld=[]
    for b in g(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>'):
        try:
            j=json.loads(b);j=j if isinstance(j,list) else [j]
            for x in j: ld.append(x.get('@type') if isinstance(x,dict) else str(type(x)))
        except Exception: ld.append('OGILTIG_JSON')
    prod=[]
    for b in g(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>'):
        try:
            j=json.loads(b)
            for x in (j if isinstance(j,list) else [j]):
                if isinstance(x,dict) and x.get('@type')=='Product': prod.append({k:(str(v)[:120]) for k,v in x.items() if k in('name','brand','sku','gtin','gtin13','mpn','aggregateRating','review','offers','material','audience','additionalProperty','hasMerchantReturnPolicy')})
        except Exception: pass
    t=g(r'<title>(.*?)</title>')
    return dict(url=u,final=fu,status=s,bytes=len(h),title=html.unescape(t[0].strip()) if t else None,
      meta=(g(r'<meta[^>]+name="description"[^>]+content="(.*?)"') or [None])[0],
      h1=[html.unescape(re.sub('<[^>]+>','',x).strip()) for x in g(r'<h1[^>]*>(.*?)</h1>')][:4],
      canonical=(g(r'<link[^>]+rel="canonical"[^>]+href="(.*?)"') or [None])[0],
      hreflang=g(r'<link[^>]+hreflang="(.*?)"')[:12],robots=(g(r'<meta[^>]+name="robots"[^>]+content="(.*?)"') or [None])[0],
      og=bool(g(r'property="og:title"')),jsonld_types=ld,product_ld=prod[:1],
      imgs=len(g(r'<img\b')),imgs_empty_alt=len(g(r'<img\b(?![^>]*\balt="[^"]+")[^>]*>')),
      html_lang=(g(r'<html[^>]+lang="(.*?)"') or [None])[0],
      scripts=len(g(r'<script\b[^>]*src=')),inline_script_bytes=sum(len(x) for x in g(r'<script(?![^>]*src)[^>]*>(.*?)</script>')))
urls=[B+'/',B+'/en',B+'/da',B+'/fi']
import random;random.seed(1)
cols=[c for c in C if c['products_count']>0]
urls+=[f"{B}/collections/{c['handle']}" for c in sorted(cols,key=lambda c:-c['products_count'])[:3]+random.sample(cols,3)]
urls+=[f"{B}/products/{p['handle']}" for p in random.sample(P,8)]
urls+=[f"{B}/products/{[p for p in P if p['vendor']=='Urban Classics Kids'][0]['handle']}"]
for x in ['pages/contact','pages/om-oss','policies/shipping-policy','policies/refund-policy','policies/terms-of-service','policies/privacy-policy','agents.md','.well-known/ucp','llms.txt','sitemap_agentic_discovery.xml']: urls.append(f"{B}/{x}")
out=[an(u) for u in urls]
json.dump(out,open(f'{m}/genomlysning_sidor.json','w'),ensure_ascii=False,indent=1)
for o in out:
    print({k:v for k,v in o.items() if k in('url','status','title','meta','h1','canonical','jsonld_types','imgs','imgs_empty_alt','inline_script_bytes','scripts','bytes')})
