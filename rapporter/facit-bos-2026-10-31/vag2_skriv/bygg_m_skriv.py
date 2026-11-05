import json,glob,re,collections,sys
# argument: namn  utkastfiler(komma)  utlatandefiler(komma)  utfil
namn,ut,ul,outf=sys.argv[1:5]
utl={}
for f in ul.split(','):
    for x in json.load(open(f,encoding='utf-8')): utl[x['nr']]=x
drafts={}
for f in ut.split(','):
    for x in json.load(open(f,encoding='utf-8')):
        if x.get('nr') is None: sys.exit(f'FEL: utkast utan nr i {f} (id {x.get("id")}); nr är nyckel och måste vara unikt')
for f in ut.split(','):
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
            x[base]=None if ch['efter'] is None and x[base]==ch['fore'] else x[base].replace(ch['fore'],ch['efter'] or '')
    out.append(x)
allx=[]
skip=set(sys.argv[5:])
for f in glob.glob('*skriv*.json'):
    if f==outf or f in skip or 'titlar' in f: continue
    try: z=json.load(open(f,encoding='utf-8'))
    except Exception: continue
    if isinstance(z,list): allx+=[o for o in z if isinstance(o,dict)]
for k in('titel','seo_title','meta'):
    c=collections.Counter(o[k] for o in out if o[k])
    for v,n in c.items():
        if n>1: prob.append((None,k,f'dubblett x{n}: {v[:50]}'))
    others={o.get(k) for o in allx if o.get('id') not in {x['id'] for x in out}}
    for o in out:
        if o[k] and o[k] in others: prob.append((o['nr'],k,'dubblett mot redan skrivet'))
for o in out:
    if len(o['titel'])>70: prob.append((o['nr'],'titel','>70'))
    if o['seo_title'] and len(o['seo_title'])>43: prob.append((o['nr'],'seo','>43'))
    if o['meta'] and not 70<=len(o['meta'])<=155: prob.append((o['nr'],'meta',len(o['meta'])))
json.dump(out,open(outf,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(namn,len(out),'skrivbara; saknar utlåtande:',saknar)
print(collections.Counter(utl[o['nr']]['dom'][:6] for o in out))
for p in prob: print(p)
