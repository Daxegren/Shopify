import json,glob,re,sys,collections
utl={}
for f in glob.glob('c_utlatande_*.json'):
    for x in json.load(open(f,encoding='utf-8')): utl[x['nr']]=x
drafts={}
for f in sorted(glob.glob('c_*_utkast.json')):
    for x in json.load(open(f,encoding='utf-8')): drafts[x['nr']]=x
HOLD={3191:'stegbräda bär kroppsvikt, maxbelastning saknas',3192:'stegbräda bär kroppsvikt, maxbelastning saknas',3257:'stegbräda bär kroppsvikt, maxbelastning saknas',3240:'balansbräda i trä, fallrisk',3087:'möjlig dubblett av 3001 (SKU 62010 mot GYM62010)'}
out=[];problem=[];saknar=[];holdl=[]
for nr,d in sorted(drafts.items()):
    u=utl.get(nr)
    if not u: saknar.append(nr); continue
    if u['dom'].startswith('UNDERK'): continue
    if nr in HOLD: holdl.append((nr,HOLD[nr])); continue
    x={k:d.get(k) for k in('id','nr','titel','seo_title','meta','html')}
    for fld,chs in (u.get('rattningar') or {}).items():
        base=re.sub(r'_\d+$','',fld.split()[0])
        if isinstance(chs,dict): chs=[chs]
        for ch in chs:
            fore,efter=ch['fore'],ch['efter']
            if base not in x or x[base] is None: problem.append((nr,fld,'fält saknas')); continue
            n=x[base].count(fore)
            if n!=1: problem.append((nr,fld,f'fore träffar {n} ggr')); continue
            x[base]=x[base].replace(fore,efter)
    out.append(x)
# kontroller
def cnt(k): return collections.Counter(o[k] for o in out if o[k])
for k in('titel','seo_title','meta'):
    for v,c in cnt(k).items():
        if c>1: problem.append((None,k,f'dubblett x{c}: {v[:60]}'))
for o in out:
    if len(o['titel'])>70 or o['titel'].count(',')>2: problem.append((o['nr'],'titel','längd/komma'))
    if o['seo_title'] and len(o['seo_title'])>43: problem.append((o['nr'],'seo_title','>43'))
    if o['meta'] and not 130<=len(o['meta'])<=155: problem.append((o['nr'],'meta',f"{len(o['meta'])} tecken"))
json.dump(out,open('c_skriv.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('skrivbara',len(out),'saknar utlåtande',saknar)
for p in problem: print(p)

json.dump({'hold':holdl},open('c_hold.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('hold',holdl)
