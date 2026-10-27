import os
HERE=os.path.dirname(os.path.abspath(__file__))
import csv,re,collections,json,random,statistics
SEED=20261027
live={}
for l in open(os.path.join(HERE,'indata_live_pris_seo_2026-10-27.txt')):
    a=l.split(); live[a[0]]=(int(a[1]),a[2])
r=list(csv.DictReader(open('/home/user/Shopify/rapporter/bos-produkter-titlar-beskrivningar-2026-10-25.csv')))
k={x['id']:x for x in r if x['ptype']=='Konditionsträning & Fitness' and x['id'] in live}
pilot=set(json.load(open('/home/user/Shopify/rapporter/shopify-original-2026-10-25/pilot-20-original.json')).keys())
EX=re.compile(r'protein|vitamin|kreatin|creatine|aminosyr|bcaa|koffein|caffeine|energi|fettförbr|tillskott|supplement|pre-?workout|massage|vibration|\bvåg\b|smart scale|hälsa|bränn|viktminsk|detox|rehab|smärta|sjukgymn|collagen|elektrolyt|akupunkt|akupress|terapi|reha|jõu|treening|inversi|ujumis|smartvåg|body screen',re.I)
def excl(i,x):
    z=[]
    if live[i][1]=='S': z.append('seo_satt')
    if i in pilot: z.append('pilot')
    if live[i][0]<=0: z.append('pris0')
    if int(x['inv'])<=0: z.append('lager<=0')
    if x['vendor']=='Trec': z.append('trec')
    if EX.search(x['title']) or EX.search(x['handle']): z.append('halsoord')
    if x['dlang'] not in ('sv','en'): z.append('dlang_'+x['dlang'])
    if int(x['desc_words'])<15: z.append('kortbeskr')
    return z
SUB=[('lopband',r'löpband|treadmill|gåband|walking'),('cykel',r'motionscykel|spinningcykel|minicykel|mini cykel|bike|cykel|cycle'),
('rodd',r'rodd|rowing'),('crosstrainer',r'crosstrainer|elliptical|cross trainer'),('bank',r'bänk|bench'),
('viktskivor',r'viktplatt|viktskiv|bumper|plates?\b|plate\b'),('hantlar',r'hantel|hantlar|dumbbell'),('kettlebell',r'kettlebell'),
('stang',r'lyftstång|skivstång|barbell|stång|fell'),('matta',r'matta|mat\b|golvmatta|flooring|yoga'),('boll',r'boll|ball'),
('handskar',r'handsk|glove'),('rack',r'rack|rig\b|cage|squat|tower|stall|station|multigym|power'),('band',r'band|tubing|stretch|rubber'),
('hopprep',r'hopprep|rope')]
def sub(t):
    for n,p in SUB:
        if re.search(p,t,re.I): return n
    return 'ovrigt'
def band(p):
    for lim,b in [(200,'B1<200'),(500,'B2 200-499'),(1500,'B3 500-1499'),(5000,'B4 1500-4999'),(15000,'B5 5000-14999')]:
        if p<lim: return b
    return 'B6>=15000'
pool=[]
for i,x in k.items():
    if not excl(i,x):
        p=live[i][0]; x=dict(x); x['price']=p; x['band']=band(p); x['sub']=sub(x['title']); x['vendor_g']=x['vendor']; pool.append(x)
rng=random.Random(SEED)
pool.sort(key=lambda x:int(x['id']))
left=pool[:]; pairs=[]
def run(keyf,level):
    global left
    g=collections.defaultdict(list)
    for x in left: g[keyf(x)].append(x)
    nl=[]
    for key in sorted(g):
        m=sorted(g[key],key=lambda x:int(x['id'])); rs=random.Random(f"{SEED}|{level}|{key}"); rs.shuffle(m)
        while len(m)>=2:
            a,b=m.pop(),m.pop()
            if rs.random()<0.5: a,b=b,a
            pairs.append((a,b,level))
        nl+=m
    left=nl
run(lambda x:(x['sub'],x['vendor'],x['band']),1)
run(lambda x:(x['sub'],x['band']),2)
run(lambda x:(x['vendor'],x['band']),3)
if __name__=="__main__":
    print('pool',len(pool),'pairs',len(pairs),'left',len(left), collections.Counter(l for _,_,l in pairs))
    T=[a for a,b,l in pairs]; K=[b for a,b,l in pairs]
    for nm,f in [('vendor',lambda x:x['vendor']),('sub',lambda x:x['sub']),('band',lambda x:x['band'])]:
        ct=collections.Counter(f(x) for x in T); ck=collections.Counter(f(x) for x in K)
        print(nm,{k_:(ct[k_],ck[k_]) for k_ in sorted(set(ct)|set(ck))})
    for nm,S in [('T',T),('K',K)]:
        ps=[x['price'] for x in S]; print(nm,len(S),'mean',round(statistics.mean(ps)),'median',statistics.median(ps),'desc median',statistics.median(int(x['desc_words']) for x in S))
    print(collections.Counter(x['sub'] for x in pool))
