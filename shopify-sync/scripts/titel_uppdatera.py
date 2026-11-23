#!/usr/bin/env python3
"""Byter produkttitel enligt en CSV (handle;ny_titel). Rör inget annat: handle, status, taggar, varianter och pris återläses och jämförs.
Användning: titel_uppdatera.py CSV --ut KATALOG (--dry-run | --kanarie | --rest | --aterstall). Före-fil i KATALOG/fore/<handle>.json.
Kanarie = 3 första raderna; --rest = övriga i grupper om 5; --aterstall skriver tillbaka gamla titlar. Stopp vid första avvikelse."""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shopify_api as s
Q = '''query($h:String!){productByIdentifier(identifier:{handle:$h}){id title handle status tags variants(first:100){nodes{id sku price compareAtPrice title}}}}'''
M = '''mutation($p:ProductUpdateInput!){productUpdate(product:$p){product{id title handle} userErrors{field message}}}'''
def las(k, h): return k.graphql(Q, {'h': h})['productByIdentifier']
def stil(p): return {'handle': p['handle'], 'status': p['status'], 'tags': sorted(p['tags']), 'v': [(v['id'], v['sku'], v['title'], v['price'], v['compareAtPrice']) for v in p['variants']['nodes']]}
def main(a):
    rader = list(csv.DictReader(open(a[0], encoding='utf-8'), delimiter=';')); ut = a[a.index('--ut') + 1]; os.makedirs(os.path.join(ut, 'fore'), exist_ok=True)
    lage = next((x for x in ('--dry-run', '--kanarie', '--rest', '--aterstall') if x in a), None)
    if not lage: print('Ange läge'); return 2
    k = s.ShopifyKlient(); assert k.graphql('{shop{myshopifyDomain}}')['shop']['myshopifyDomain'] == s.BUTIK
    if lage == '--kanarie': rader = rader[:3]
    if lage == '--rest':
        if not os.path.exists(os.path.join(ut, 'kanarie_klar')): print('Kanarien först'); return 2
        rader = rader[3:]
    for r in rader:
        h, ny = r['handle'], r['ny_titel']; p = las(k, h)
        if not p: print('SAKNAS', h); return 1
        ff = os.path.join(ut, 'fore', h + '.json')
        if not os.path.exists(ff): json.dump(p, open(ff, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        fore = json.load(open(ff, encoding='utf-8'))
        mal = fore['title'] if lage == '--aterstall' else ny
        if lage == '--dry-run': print(('redan' if p['title'] == ny else 'byt'), '|', p['title'], '->', ny); continue
        if stil(p) != stil(fore): print('STOPP: produkten har ändrats sedan före-filen', h); return 1
        if p['title'] == mal: print('redan', h); continue
        e = k.graphql(M, {'p': {'id': p['id'], 'title': mal}})['productUpdate']
        if e['userErrors']: print('STOPP userErrors', h, e['userErrors']); return 1
        n = las(k, h); ok = n['title'] == mal and stil(n) == stil(fore)
        print(h[:50], 'verifierad' if ok else 'AVVIKELSE')
        if not ok: return 1
    if lage == '--kanarie': open(os.path.join(ut, 'kanarie_klar'), 'w').write('ok')
    return 0
if __name__ == '__main__': sys.exit(main(sys.argv[1:]))
