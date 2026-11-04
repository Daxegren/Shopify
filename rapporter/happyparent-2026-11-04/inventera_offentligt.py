"""Analyserar raw/products.json + collections.json (offentliga data). Skriver inventering.json och inventering_produkter.csv.
python3 -I inventera_offentligt.py <mapp>"""
import json,re,sys,csv,collections,html
m=sys.argv[1]
P=json.load(open(f'{m}/raw/products.json'));C=json.load(open(f'{m}/raw/collections.json'))
def text(h): return html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',h or ''))).strip()
RISK={
 'ce_mark':r'\bCE[- ]?(märk|mark|godkän|certifier)|\bCE\b',
 'en_norm':r'\bEN[ -]?\d{2,5}|EN71|EN ?71|ISO ?\d{3,5}|ASTM|OEKO|Öko-?Tex|GOTS',
 'sakerhet':r'säker|safe|ofarlig|giftfri|non-?toxic|BPA|ftalat|phthalat|blyfri|brandsäker|testad|certifierad|godkänd',
 'aldersgrans':r'(från|fr\.o\.m\.?|ab|över|under|upp till|ålder)\s*\d+\s*(år|mån|month|mdr|m\b)|\b\d+\+\s*(år|mån)?|\b\d+\s*[-–]\s*\d+\s*(år|mån)',
 'kvavning':r'kvävning|små delar|smådelar|svälj|choking|small parts',
 'halsa':r'utveckl|motorik|finmotorik|hjärnan|inlärning|syn(?:en|s)?\b|tand|tandsköt|tandlös|lindr|kolik|sömn|sover bättre|allergi|hypoallerg|antibakter|eksem|huden',
 'medicinskt':r'läk|terap|medicin|behandl|botar|förebygg',
 'montessori_pedagogik':r'montessori|pedagogisk|waldorf|steiner',
 'material':r'silikon|trä\b|bambu|bomull|ekologisk|organisk|naturgummi|plast|BPA',
 'spadbarn_sov':r'babynest|sovkudde|nackkudde|ligg(?:a|ning)|SIDS|plötslig|kudde|sovsäck|filt\b',
 'barnstol_fordon':r'barnstol|bilstol|barnvagn|bältes|skyddsbälte|hjälm|cykel|balans?cykel|sparkcykel',
 'batteri_magnet':r'batteri|knappcell|magnet',
 'enligt_tillverkaren':r'enligt tillverkaren',
}
rows=[];cnt=collections.Counter();ex=collections.defaultdict(list)
titles=collections.Counter(p['title'].strip().lower() for p in P)
bylen=[]
sv=re.compile(r'[åäöÅÄÖ]|\b(och|för|med|barn|till|som)\b',re.I)
en_title=0
for p in P:
    t=text(p['body_html']);L=len(t)
    flags=[k for k,r in RISK.items() if re.search(r,t+' '+p['title'],re.I)]
    for k in flags:
        cnt[k]+=1
        if len(ex[k])<4:
            mm=re.search(RISK[k],t+' '+p['title'],re.I);s=(t+' '+p['title']);i=mm.start();ex[k].append(f"{p['id']}: …{s[max(0,i-60):i+90]}…")
    eng=not sv.search(p['title'])
    rows.append(dict(id=p['id'],handle=p['handle'],title=p['title'],vendor=p['vendor'],type=p['product_type'] or '',n_var=len(p['variants']),n_img=len(p['images']),price_min=min(float(v['price']) for v in p['variants']),tags=';'.join(p['tags']),beskr_tecken=L,titel_tecken=len(p['title']),titel_ej_svensk=int(eng),dubblett_titel=int(titles[p['title'].strip().lower()]>1),flaggor=';'.join(flags),
      alla_slut=int(not any(v['available'] for v in p['variants'])),alt_saknas=sum(1 for i in p['images'] if not (i.get('alt') or '').strip()),published=p['published_at']))
with open(f'{m}/inventering_produkter.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
lens=sorted(r['beskr_tecken'] for r in rows)
out=dict(antal_produkter=len(P),
 vendor=collections.Counter(p['vendor'] for p in P).most_common(),
 product_type=collections.Counter(p['product_type'] or '(tom)' for p in P).most_common(),
 antal_taggar=len({t for p in P for t in p['tags']}),
 beskr_tomma=sum(1 for l in lens if l==0),beskr_under_150=sum(1 for l in lens if l<150),beskr_under_300=sum(1 for l in lens if l<300),median_beskr=lens[len(lens)//2],
 titel_over_70=sum(r['titel_tecken']>70 for r in rows),titel_ej_svensk=sum(r['titel_ej_svensk'] for r in rows),
 dubblett_titel_produkter=sum(r['dubblett_titel'] for r in rows),
 alla_slutsalda=sum(r['alla_slut'] for r in rows),med_flera_varianter=sum(r['n_var']>1 for r in rows),
 bilder_utan_alt=sum(r['alt_saknas'] for r in rows),produkter_med_alt_saknas=sum(1 for r in rows if r['alt_saknas']),utan_bild=sum(1 for r in rows if r['n_img']==0),
 riskflaggor=dict(cnt),riskexempel=ex,
 samlingar=len(C),tomma_samlingar=[c['handle'] for c in C if c['products_count']==0],
 samlingar_utan_beskrivning=sum(1 for c in C if not text(c.get('description'))),
 valuta_pris=dict(min=min(r['price_min'] for r in rows),max=max(r['price_min'] for r in rows)))
json.dump(out,open(f'{m}/inventering.json','w'),ensure_ascii=False,indent=1)
print(json.dumps({k:v for k,v in out.items() if k!='riskexempel'},ensure_ascii=False,indent=1))
