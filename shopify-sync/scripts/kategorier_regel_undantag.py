#!/usr/bin/env python3
"""Rättar en kollektions innehåll genom UNDANTAG för namngivna produkter (inga villkor raderas, inga produkter ändras).
Användning: kategorier_regel_undantag.py HANDLE REGEX --ut KATALOG (--analys | --dry-run | --skriv)
  REGEX    mot produkttiteln (gemener ignoreras); bara ACTIVE produkter i kollektionen undantas.
  --analys  skriver säkerhetskopia (kollektion, källa med villkor/undantag, alla medlemmar) och listar träffarna
  --skriv   lägger undantagen med collectionConditionsSourceUpdate(exclusion.selectionsToAdd), väntar in och kontrollerar:
            medlemmar efter = före minus undantagna; alla berörda produkters status, taggar och pris oförändrade; sidans fält oförändrade.
Ångra: collectionConditionsSourceUpdate med exclusion.selectionsToRemove för samma produkt-id (står i säkerhetskopian: 'undantas')."""
import json, os, re, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shopify_api as s
import kategorier_live as L

QK = '''query($id:ID!){collection(id:$id){id handle title ruleSet{appliedDisjunctively rules{column relation condition}}
 sources{__typename id title ... on CollectionConditionsSource{targetType
  inclusion{matchType conditions{__typename}} exclusion{matchType conditions{__typename} selections(first:250){nodes{product{id}}}}}}}}'''
QP = '''query($id:ID!,$a:String){collection(id:$id){products(first:250,after:$a){pageInfo{hasNextPage endCursor}
 nodes{id title status tags priceRangeV2{minVariantPrice{amount}}}}}}'''
MUT = '''mutation($i:CollectionUpdateConditionsSourceInput!){collectionConditionsSourceUpdate(input:$i){source{id} userErrors{field message}}}'''

def medlemmar(k, cid):
    ut, a = {}, None
    while True:
        d = k.graphql(QP, {'id': cid, 'a': a})['collection']['products']
        for p in d['nodes']: ut[p['id']] = {'title': p['title'], 'status': p['status'], 'tags': sorted(p['tags']), 'pris': p['priceRangeV2']['minVariantPrice']['amount']}
        if not d['pageInfo']['hasNextPage']: return ut
        a = d['pageInfo']['endCursor']

def main(argv):
    handle, rx = argv[0], re.compile(argv[1], re.I)
    ut = argv[argv.index('--ut') + 1]; os.makedirs(ut, exist_ok=True)
    lage = 'analys' if '--analys' in argv else 'dry' if '--dry-run' in argv else 'skriv' if '--skriv' in argv else None
    k = s.ShopifyKlient()
    assert k.graphql('{shop{myshopifyDomain}}')['shop']['myshopifyDomain'] == s.BUTIK
    cid = k.graphql('query($h:String!){collectionByHandle(handle:$h){id}}', {'h': handle})['collectionByHandle']['id']
    kol = k.graphql(QK, {'id': cid})['collection']; src = [x for x in kol['sources'] if x['__typename'] == 'CollectionConditionsSource']
    assert len(src) == 1, f'{len(src)} villkorskällor: stoppar'
    fore_m = medlemmar(k, cid); traff = {i: p for i, p in fore_m.items() if p['status'] == 'ACTIVE' and rx.search(p['title'])}
    fn = os.path.join(ut, handle + '.json')
    if not os.path.exists(fn):
        json.dump({'tid': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'kollektion': kol, 'faltoversikt': L.ovriga_falt(L.las(k, [cid])[0]), 'medlemmar_fore': fore_m, 'undantas': sorted(traff)}, open(fn, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{handle}: {len(fore_m)} medlemmar, {len(traff)} undantas (ACTIVE träffar), befintliga undantagsval: {len(src[0]["exclusion"]["selections"]["nodes"])}')
    for i, p in sorted(traff.items(), key=lambda x: x[1]['title']): print('  -', i.split('/')[-1], p['title'])
    if lage != 'skriv': return 0
    r = k.graphql(MUT, {'i': {'id': src[0]['id'], 'exclusion': {'selectionsToAdd': [{'productId': i} for i in traff]}}})['collectionConditionsSourceUpdate']
    if r['userErrors']: print('STOPP userErrors', r['userErrors']); return 1
    for forsok in range(8):
        time.sleep(5); efter = medlemmar(k, cid)
        if set(efter) == set(fore_m) - set(traff): break
    fel = []
    if set(efter) != set(fore_m) - set(traff): fel.append(f'medlemmar efter {len(efter)}, väntat {len(fore_m) - len(traff)}; skillnad {sorted(set(efter) ^ (set(fore_m) - set(traff)))[:5]}')
    ber = L.las  # produkter: jämför status/taggar/pris för alla före-medlemmar via nodes
    Q = 'query($ids:[ID!]!){nodes(ids:$ids){... on Product{id status tags priceRangeV2{minVariantPrice{amount}}}}}'
    ids = list(fore_m)
    for j in range(0, len(ids), 100):
        for p in k.graphql(Q, {'ids': ids[j:j + 100]})['nodes']:
            f = fore_m[p['id']]
            if (p['status'], sorted(p['tags']), p['priceRangeV2']['minVariantPrice']['amount']) != (f['status'], f['tags'], f['pris']): fel.append(f'produkt ändrad: {p["id"]}')
    fo = json.load(open(fn, encoding='utf-8'))['faltoversikt']; ef = L.ovriga_falt(L.las(k, [cid])[0])
    for key in ('handle', 'title', 'sortOrder', 'templateSuffix', 'image', 'ruleSet'):
        if fo[key] != ef[key]: fel.append(f'fält ändrat: {key}')
    json.dump({'efter_medlemmar': len(efter), 'fel': fel}, open(os.path.join(ut, handle + '_efter.json'), 'w'), ensure_ascii=False, indent=1)
    print('RESULTAT', 'OK' if not fel else fel, 'medlemmar efter', len(efter)); return 1 if fel else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
