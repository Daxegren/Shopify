#!/usr/bin/env python3
"""Läsande analys av katalogexport (ndjson från graphql_query) för workoutbrands.com. Inget skrivs i butiken.
Användning: python3 -I analysera_katalog_wb.py <ut-katalog> <fil1.ndjson> [fil2.ndjson ...]"""
import sys,json,re,statistics,collections,csv,html,os
ut=sys.argv[1]; os.makedirs(ut,exist_ok=True)
P={}
for f in sys.argv[2:]:
    for l in open(f):
        x=json.loads(l); P[x['id']]=x
P=list(P.values()); N=len(P); R={"produkter_analyserade":N}
MOMS=1.25
def txt(h): return re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",h or ""))).strip()
def q(v,p): v=sorted(v); return v[min(len(v)-1,int(p*(len(v)-1)))] if v else None
# --- status/vendor/typ/taggar
R["vendor_topp"]=collections.Counter(x['vendor'] for x in P).most_common(40)
R["vendor_antal"]=len({x['vendor'] for x in P})
R["typ_topp"]=collections.Counter(x['productType'] or '(tom)' for x in P).most_common(30)
R["typ_antal"]=len({x['productType'] for x in P}); R["typ_tom"]=sum(1 for x in P if not x['productType'])
tc=collections.Counter(t for x in P for t in x['tags']); R["tagg_antal"]=len(tc); R["tagg_topp"]=tc.most_common(40)
jobb=[(t,c) for t,c in tc.items() if re.search(r"job|price|pris|sale|rea|outlet|kampanj|campaign|discount|black|bf|sheet|wob|new|nyhet",t,re.I)]
R["tagg_pris_kampanj_import"]=sorted(jobb,key=lambda a:-a[1])[:40]
lc=collections.Counter(); 
for t in tc: lc[t.lower()]+=tc[t]
R["tagg_skiftlagesdubbletter"]=sum(1 for t in tc if t!=t.lower() and t.lower() in tc and t.lower()!=t)
# --- SEO
st=[x['seo']['title'] for x in P]; sm=[x['seo']['description'] for x in P]
R["seo_titel_saknas"]=sum(1 for v in st if not v); R["seo_meta_saknas"]=sum(1 for v in sm if not v)
R["seo_titel_over_70"]=sum(1 for v in st if v and len(v)>70); R["seo_meta_under_70"]=sum(1 for v in sm if v and len(v)<70); R["seo_meta_over_155"]=sum(1 for v in sm if v and len(v)>155)
R["seo_meta_median_tecken"]=statistics.median([len(v) for v in sm if v]) if any(sm) else None
R["seo_titel_slutar_med_suffix"]=sum(1 for v in st if v and v.endswith("| Workout Brands"))
R["titel_over_70"]=sum(1 for x in P if len(x['title'])>70)
# titlar
norm=lambda s:re.sub(r"[^a-z0-9åäö]+"," ",s.lower()).strip()
tcnt=collections.Counter(norm(x['title']) for x in P); R["dubbletitlar_grupper"]=sum(1 for v in tcnt.values() if v>1); R["dubbletitlar_produkter"]=sum(v for v in tcnt.values() if v>1)
sz=re.compile(r"[\s-](XXS|XS|S|M|L|XL|XXL|XXXL|3XL|4XL|5XL|\d{2}(?:[.,]\d)?)$",re.I)
R["titel_slutar_pa_storlek"]=sum(1 for x in P if sz.search(x['title'].strip()))
# --- varianter, priser, marginal
mar=[];under=[];over60=[];rea=0;fal=0;lag=0;nocost=0;varn=0;ratio_rea=[];prod_mar=[];prodrows=[]
for x in P:
    vs=x['variants']['nodes']; pm=[]
    for v in vs:
        varn+=1
        try: pr=float(v['price'])
        except: continue
        uc=(v.get('inventoryItem') or {}).get('unitCost'); c=float(uc['amount']) if uc and uc.get('amount') not in (None,'') else None
        ca=float(v['compareAtPrice']) if v.get('compareAtPrice') else None
        if ca is not None:
            if ca>pr: rea+=1; ratio_rea.append(1-pr/ca)
            elif ca==pr: fal+=1
        if not c or c<=0: nocost+=1; continue
        net=pr/MOMS; m=(net-c)/net if net>0 else None
        if m is None: continue
        mar.append(m); pm.append(m)
        if net<c: under.append((x['legacyResourceId'],x['title'],v['sku'],pr,c))
        if m>0.60: over60.append((x['legacyResourceId'],x['title'],v['sku'],pr,c,round(m,3)))
    if pm: prod_mar.append(statistics.median(pm)); prodrows.append((x['legacyResourceId'],x['title'],x['vendor'],round(statistics.median(pm),3)))
R["varianter_i_urval(första 5/produkt)"]=varn; R["varianter_med_inkopspris"]=len(mar); R["varianter_utan_inkopspris"]=nocost
if mar:
    R["marginal_efter_moms"]={"median":round(q(mar,.5),3),"q1":round(q(mar,.25),3),"q3":round(q(mar,.75),3),"p10":round(q(mar,.1),3),"p90":round(q(mar,.9),3),"under_inkop":len(under),"over_60pct":len(over60),"under_20pct":sum(1 for m in mar if m<0.2),"mellan_30_50":sum(1 for m in mar if .3<=m<=.5)}
R["jamforpris_hogre_an_pris(rea)"]=rea; R["jamforpris_lika_med_pris(falskt)"]=fal
R["rea_djup_median"]=round(statistics.median(ratio_rea),3) if ratio_rea else None
R["jamforpris_lika_med_pris_per_vendor"]=None
# --- lager
R["totalInventory_0"]=sum(1 for x in P if (x.get('totalInventory') or 0)<=0); R["totalInventory_median"]=statistics.median([x.get('totalInventory') or 0 for x in P])
R["varianter_per_produkt_median"]=statistics.median([x['variantsCount']['count'] for x in P if x.get('variantsCount')])
R["bilder_0"]=sum(1 for x in P if (x.get('mediaCount') or {}).get('count',0)==0)
# --- text
SV=set("och att det som är en ett på för med av den har inte till kan om du vi ska när från eller den detta dessa också så mycket passar material design".split())
EN=set("the and with for this that your made from fit made of features comfortable perfect available".split())
wc=[];empty=0;circ=0;faq=0;om=0;amp=0;eng=0;mix=0;html_bad=0;nr=0;dup=collections.Counter();short=0;rowst=[]
for x in P:
    t=txt(x['descriptionHtml']); w=t.split(); wc.append(len(w))
    if not t: empty+=1; continue
    if len(w)<30: short+=1
    low=[a.strip(".,!?:;()").lower() for a in w]
    s=sum(1 for a in low if a in SV); e=sum(1 for a in low if a in EN)
    if e>s and e>=5: eng+=1
    elif e>=5 and s>=5: mix+=1
    ti=x['title'].lower()
    if re.search(r"vanliga frågor|faq",t,re.I): faq+=1
    if re.search(r"om (märket|varumärket)|about the brand|about us",t,re.I): om+=1
    if "&" in x['descriptionHtml'].replace("&amp;","").replace("&nbsp;",""): amp+=1
    if x['descriptionHtml'].count("<")!=x['descriptionHtml'].count(">") or len(re.findall(r"<(p|ul|li|strong|h\d)\b",x['descriptionHtml']))!=len(re.findall(r"</(p|ul|li|strong|h\d)>",x['descriptionHtml'])): html_bad+=1
    first=re.split(r"(?<=[.!?])\s",t,1)[0].lower(); m=re.match(r"^(.{3,60}?) (är|är en|är ett)\s+(en|ett)?\s*(.*)",first)
    if m and m.group(1)[:25] in ti: circ+=1
    dup[t[:200]]+=1
R["text_tom"]=empty; R["text_under_30_ord"]=short; R["text_ord_median"]=statistics.median(wc); R["text_ord_q1_q3"]=[q(wc,.25),q(wc,.75)]
R["text_mest_engelsk"]=eng; R["text_blandad_sv_en"]=mix; R["text_faq_eller_vanliga_fragor"]=faq; R["text_om_market"]=om; R["text_med_ampersand_i_html"]=amp; R["text_html_obalanserad"]=html_bad; R["text_cirkular_inledning(heur)"]=circ
R["text_identisk_inledning_grupper"]=sum(1 for v in dup.values() if v>1); R["text_identisk_inledning_produkter"]=sum(v for v in dup.values() if v>1)
# ---- urval: 300 spridda produkter för manuell textgranskning
import random; random.seed(7); smp=random.sample(P,min(300,N))
with open(ut+"/textprov_300.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["id","titel","vendor","typ","ord","seo_titel_len","seo_meta_len","borjan_av_text"])
    for x in smp: t=txt(x['descriptionHtml']); w.writerow([x['legacyResourceId'],x['title'],x['vendor'],x['productType'],len(t.split()),len(x['seo']['title'] or ''),len(x['seo']['description'] or ''),t[:160]])
with open(ut+"/under_inkop.csv","w",newline="") as f: w=csv.writer(f); w.writerow(["id","titel","sku","pris_inkl_moms","inkop"]); w.writerows(under)
with open(ut+"/marginal_over_60.csv","w",newline="") as f: w=csv.writer(f); w.writerow(["id","titel","sku","pris","inkop","marginal"]); w.writerows(over60)
json.dump(R,open(ut+"/katalog_siffror.json","w"),ensure_ascii=False,indent=1)
print(json.dumps(R,ensure_ascii=False,indent=1)[:6000])
