#!/usr/bin/env python3
"""Läsande hypotestest av misstänkta inköpspriser (workoutbrands.com). Inget skrivs i butiken, inga inköpspriser föreslås.
Användning: python3 -I analysera_inkop_wb.py <ut-katalog> <aktiva_A.ndjson> <aktiva_B.ndjson>"""
import sys,json,csv,statistics,collections,os,re
ut=sys.argv[1]; os.makedirs(ut,exist_ok=True)
P=[json.loads(l) for f in sys.argv[2:] for l in open(f)]
MOMS=1.25; FORMEL=None
def q(v,p): v=sorted(v); return v[min(len(v)-1,int(p*(len(v)-1)))]
rows=[]
for x in P:
    for i,v in enumerate(x['variants']['nodes']):
        try: pr=float(v['price'])
        except: continue
        uc=(v.get('inventoryItem') or {}).get('unitCost'); c=float(uc['amount']) if uc and uc.get('amount') not in(None,'') else None
        if pr<=0: continue
        m=None if not c or c<=0 else ((pr/MOMS)-c)/(pr/MOMS)
        rows.append(dict(pid=x['legacyResourceId'],titel=x['title'],vendor=x['vendor'],typ=x['productType'] or '(tom)',sku=v['sku'] or '',pris=pr,inkop=c,m=m,created=x['createdAt'][:4],tags=x['tags'],lager=v['inventoryQuantity'],jobb='price-change-job-active' in x['tags'],i=i))
ok=[r for r in rows if r['m'] is not None]
norm=[r for r in ok if 0.30<=r['m']<=0.90]   # "rimliga" (formelgruppen)
hog=[r for r in ok if r['m']>0.90]; under=[r for r in ok if r['m']<0]; saknas=[r for r in rows if r['m'] is None]
R={"varianter_totalt":len(rows),"med_inkop":len(ok),"rimliga_30_90":len(norm),"over_90":len(hog),"under_inkop":len(under),"saknar_inkop":len(saknas),"mellan_0_30":len([r for r in ok if 0<=r['m']<0.30])}
# 1) kvot pris/inkop: rimlig grupp vs misstänkt grupp
kv=lambda g:[r['pris']/r['inkop'] for r in g]
R["kvot_rimliga"]={"median":round(statistics.median(kv(norm)),2),"q1":round(q(kv(norm),.25),2),"q3":round(q(kv(norm),.75),2)}
R["kvot_over_90"]={"median":round(statistics.median(kv(hog)),2),"q1":round(q(kv(hog),.25),2),"q3":round(q(kv(hog),.75),2)}
# 2) hypotes: inköp i annan enhet. Implicit faktor k = (pris/1,25)/(inkop*(1-0,607)) om formelmarginal 60,7 % gäller i riktiga enheter
FM=statistics.median([r['m'] for r in norm])
R["formelmarginal_median_rimliga"]=round(FM,4)
k=[(r['pris']/MOMS)/(r['inkop']*(1-FM)) for r in hog]
R["implicit_faktor_k_over_90"]={"median":round(statistics.median(k),2),"q1":round(q(k,.25),2),"q3":round(q(k,.75),2),"p10":round(q(k,.1),2),"p90":round(q(k,.9),2)}
# histogram av k (avrundat), för att se om de samlas kring ett fast tal
hist=collections.Counter(round(x) for x in k); R["faktor_k_histogram_topp"]=hist.most_common(12)
# andel k mellan 10 och 12 (EUR/SEK 2026 troligen ~10,5–11,5), mellan 9 och 13
R["andel_k_10_12"]=round(sum(1 for x in k if 10<=x<=12)/len(k),3); R["andel_k_9_13"]=round(sum(1 for x in k if 9<=x<=13)/len(k),3)
# 3) per vendor / typ: andel misstänkta och kvotens median
def grp(key):
    d=collections.defaultdict(lambda:[0,0,0,[],[]])
    for r in ok:
        g=d[r[key]]; g[0]+=1
        if r['m']>0.90: g[1]+=1; g[3].append(r['pris']/r['inkop']); g[4].append((r['pris']/MOMS)/(r['inkop']*(1-FM)))
        if r['m']<0: g[2]+=1
    return d
for key,fn in (("vendor","per_vendor.csv"),("typ","per_produkttyp.csv")):
    w=csv.writer(open(ut+"/inkop_"+fn,"w",newline="")); w.writerow([key,"varianter_med_inkop","over_90","andel_over_90","under_inkop","kvot_median_over_90","faktor_k_median_over_90"])
    for kx,g in sorted(grp(key).items(),key=lambda a:-a[1][1]):
        w.writerow([kx,g[0],g[1],round(g[1]/g[0],3),g[2],round(statistics.median(g[3]),2) if g[3] else "",round(statistics.median(g[4]),2) if g[4] else ""])
# 4) samma produkt: blandas rimliga och misstänkta varianter?
bp=collections.defaultdict(list)
for r in ok: bp[r['pid']].append(r['m']>0.90)
mix=sum(1 for v in bp.values() if any(v) and not all(v)); alla=sum(1 for v in bp.values() if all(v)); inga=sum(1 for v in bp.values() if not any(v))
R["produkter_alla_varianter_over_90"]=alla; R["produkter_blandade"]=mix; R["produkter_inga_over_90"]=inga
# 5) samma SKU-prefix (modell) med olika nivå i olika produkter?
def pre(s): return s.rsplit('-',1)[0] if s.count('-')>=2 else s
sk=collections.defaultdict(lambda:[0,0])
for r in ok:
    sk[pre(r['sku'])][0]+=1; sk[pre(r['sku'])][1]+= r['m']>0.90
R["sku_modeller_blandade"]=sum(1 for a,b in sk.values() if 0<b<a); R["sku_modeller_totalt"]=len(sk)
# 6) korrelation med taggar/år/prisjobb/lager
def andel(f): 
    a=[r for r in ok if f(r)]; return (len(a),round(sum(1 for r in a if r['m']>0.9)/len(a),3)) if a else (0,None)
R["andel_over_90_per_skapandear"]={y:andel(lambda r,y=y:r['created']==y) for y in sorted({r['created'] for r in ok})}
R["andel_over_90_in_sheet"]=andel(lambda r:'in sheet' in r['tags']); R["andel_over_90_utan_in_sheet"]=andel(lambda r:'in sheet' not in r['tags'])
R["andel_over_90_prisjobb"]=andel(lambda r:r['jobb']); R["andel_over_90_ej_prisjobb"]=andel(lambda r:not r['jobb'])
R["andel_over_90_lager_0"]=andel(lambda r:(r['lager'] or 0)<=0); R["andel_over_90_lager_pos"]=andel(lambda r:(r['lager'] or 0)>0)
# 7) tio tydligaste exempel per vendor (störst pris/inkop-kvot), samt om samma SKU-modell har rimligt inköpspris på annan variant/produkt
rim_pre=collections.defaultdict(list)
for r in norm: rim_pre[pre(r['sku'])].append(r['inkop'])
w=csv.writer(open(ut+"/inkop_exempel_per_vendor.csv","w",newline="")); w.writerow(["vendor","produkt_id","titel","sku","pris_inkl_moms","inkop","marginal_efter_moms","kvot_pris_inkop","samma_skumodell_rimligt_inkop_finns","rimligt_inkop_exempel"])
bv=collections.defaultdict(list)
for r in hog+under: bv[r['vendor']].append(r)
for v,l in sorted(bv.items(),key=lambda a:-len(a[1])):
    seen=set();n=0
    for r in sorted(l,key=lambda r:-(r['pris']/r['inkop'])):
        if r['pid'] in seen: continue
        seen.add(r['pid']); n+=1
        ex=rim_pre.get(pre(r['sku']),[])
        w.writerow([v,r['pid'],r['titel'],r['sku'],r['pris'],r['inkop'],round(r['m'],3),round(r['pris']/r['inkop'],1),"ja" if ex else "nej",ex[0] if ex else ""])
        if n>=10: break
# 8) under inköp, lista + saknar
w=csv.writer(open(ut+"/inkop_under_inkop_141.csv","w",newline="")); w.writerow(["produkt_id","titel","vendor","typ","sku","pris_inkl_moms","inkop","marginal_efter_moms","prisjobb"])
for r in sorted(under,key=lambda r:r['m']): w.writerow([r['pid'],r['titel'],r['vendor'],r['typ'],r['sku'],r['pris'],r['inkop'],round(r['m'],3),r['jobb']])
w=csv.writer(open(ut+"/inkop_saknas_22.csv","w",newline="")); w.writerow(["produkt_id","titel","vendor","typ","sku","pris"])
for r in saknas: w.writerow([r['pid'],r['titel'],r['vendor'],r['typ'],r['sku'],r['pris']])
# under: vilken faktor löser dem? och sammanfattning
if under:
    R["under_inkop_kvot_median"]=round(statistics.median([r['pris']/MOMS/r['inkop'] for r in under]),3)
    R["under_inkop_vendor_topp"]=collections.Counter(r['vendor'] for r in under).most_common(8)
    R["under_inkop_prisjobb"]=sum(1 for r in under if r['jobb'])
R["saknas_vendor_topp"]=collections.Counter(r['vendor'] for r in saknas).most_common(8)
json.dump(R,open(ut+"/inkop_siffror.json","w"),ensure_ascii=False,indent=1)
print(json.dumps(R,ensure_ascii=False,indent=1))
