import json,glob,re,collections,sys
utl={}
for f in glob.glob('k_utlatande_1[0-9]_*.json'):
    for x in json.load(open(f,encoding='utf-8')): utl[x['nr']]=x
drafts={}
for f in sorted([f'k_{k}_utkast.json' for k in range(10,18)]):
    for x in json.load(open(f,encoding='utf-8')): drafts[x['nr']]=x
out=[];prob=[];saknar=[]
for nr,d in sorted(drafts.items()):
    u=utl.get(nr)
    if not u: saknar.append(nr); continue
    if u['dom'].startswith('UNDERK'): continue
    x={k:d.get(k) for k in('id','nr','titel','seo_title','meta','html')}
    for fld,chs in (u.get('rattningar') or {}).items():
        base=re.sub(r'_\d+$','',fld.split()[0])
        if isinstance(chs,dict): chs=[chs]
        for ch in chs:
            if base not in x or x[base] is None: prob.append((nr,fld,'fält saknas')); continue
            n=x[base].count(ch['fore'])
            if n!=1: prob.append((nr,fld,f'fore träffar {n}')); continue
            x[base]=x[base].replace(ch['fore'],ch['efter'])
    out.append(x)
allx=[]
for f in glob.glob('c_skriv_resten_[1-4].json')+['c_skriv_kanarie.json','a_skriv.json','a_skriv_titlar.json','b_skriv.json','b_skriv_hold_frisläppta.json','b_skriv_2.json','b_skriv_3.json','k_skriv_1.json','k_skriv_2.json']:
    z=json.load(open(f,encoding='utf-8')); allx+= z if isinstance(z,list) else []
for k in('titel','seo_title','meta'):
    c=collections.Counter(o[k] for o in out if o[k])
    for v,n in c.items():
        if n>1: prob.append((None,k,f'dubblett x{n}: {v[:50]}'))
    others={o.get(k) for o in allx}
    for o in out:
        if o[k] and o[k] in others: prob.append((o['nr'],k,'dubblett mot redan skrivet'))
for o in out:
    if len(o['titel'])>70: prob.append((o['nr'],'titel','>70'))
    if o['seo_title'] and len(o['seo_title'])>43: prob.append((o['nr'],'seo','>43'))
    if o['meta'] and not 130<=len(o['meta'])<=155: prob.append((o['nr'],'meta',len(o['meta'])))
json.dump(out,open('k_skriv_3.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out),'skrivbara; saknar utlåtande:',len(saknar))
print(collections.Counter(utl[o['nr']]['dom'] for o in out))
for p in prob: print(p)
