import re,sys,json,urllib.request,html
def hamta(u):
    r=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(r,timeout=30) as f: return f.status,f.read().decode('utf-8','ignore'),f.geturl()
    except Exception as e: return getattr(e,'code',0),'',u
def analys(u):
    st,h,final=hamta(u); o={'url':u,'status':st,'slutadress':final}
    if not h: return o
    g=lambda p:(re.search(p,h,re.S|re.I) or [None,None])[1]
    o['title']=html.unescape((g(r'<title[^>]*>(.*?)</title>') or '').strip())
    o['meta']=html.unescape(g(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']') or g(r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']description["\']') or '')
    o['canonical']=g(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\'](.*?)["\']')
    o['robots']=g(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']')
    o['h1']=[re.sub(r'<[^>]+>','',x).strip() for x in re.findall(r'<h1[^>]*>(.*?)</h1>',h,re.S|re.I)]
    o['h2_antal']=len(re.findall(r'<h2[^>]*>',h,re.I))
    body=re.sub(r'<(script|style|noscript)[^>]*>.*?</\1>','',h,flags=re.S|re.I)
    body=re.sub(r'<(header|footer|nav)[^>]*>.*?</\1>','',body,flags=re.S|re.I)
    txt=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',body)))
    o['ord_synliga']=len(txt.split())
    o['jsonld']=sorted(set(re.findall(r'"@type"\s*:\s*"([A-Za-z]+)"',' '.join(re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>',h,re.S|re.I)))))
    o['faq_wrapper_tom']=bool(re.search(r'product-view__faq-wrapper"\s*>\s*</div>',h))
    o['faq_wrapper']='faq-wrapper' in h
    o['img']=len(re.findall(r'<img\b',h,re.I)); o['img_utan_alt']=len([x for x in re.findall(r'<img\b[^>]*>',h,re.I) if not re.search(r'alt=["\'][^"\']+["\']',x)])
    links=re.findall(r'<a\b[^>]+href=["\']([^"\']+)["\']',h,re.I)
    o['lankar_totalt']=len(links); o['lankar_med_param']=len([l for l in links if '_pos=' in l or '_psq=' in l])
    o['produktlankar']=len(set(l.split('?')[0] for l in links if '/products/' in l))
    o['hreflang']=len(re.findall(r'hreflang',h)); o['og_title']=bool(re.search(r'og:title',h))
    return o
if __name__=='__main__':
    res=[analys(u) for u in sys.argv[1:]]; json.dump(res,open('res.json','w'),ensure_ascii=False,indent=1)
    for o in res: print(json.dumps(o,ensure_ascii=False))
