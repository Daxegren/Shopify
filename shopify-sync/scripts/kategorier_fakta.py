#!/usr/bin/env python3
"""Faktaunderlag per kollektion ur kollektionens egna produkter (BARA LÄSNING).
Indata: kollektioner.json från kategorier_inventera.py. Ut: faktaunderlag.json.
Räknar bara ACTIVE-produkter; 'koopbara' = aktiva med lager > 0 (eller utan lagerspårning)."""
import json, os, sys, collections, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shopify_api as s

Q = '''query($id:ID!,$after:String){collection(id:$id){products(first:250, after:$after){pageInfo{hasNextPage endCursor}
 nodes{id title vendor productType status tracksInventory totalInventory
  priceRangeV2{minVariantPrice{amount} maxVariantPrice{amount}}}}}}'''

def fakta(prods):
    akt = [p for p in prods if p['status'] == 'ACTIVE']
    kop = [p for p in akt if (p['totalInventory'] or 0) > 0 or not p['tracksInventory']]
    def top(lst, f, n=12):
        return collections.Counter(f(p) for p in lst if f(p)).most_common(n)
    priser = [float(p['priceRangeV2']['minVariantPrice']['amount']) for p in kop]
    return {'totalt': len(prods), 'aktiva': len(akt), 'koopbara': len(kop),
            'marken': top(kop, lambda p: p['vendor']), 'typer': top(kop, lambda p: p['productType']),
            'pris_min': min(priser) if priser else None, 'pris_max': max(priser) if priser else None,
            'pris_median': statistics.median(priser) if priser else None}

def main(mapp):
    k = s.ShopifyKlient()
    assert k.graphql('{shop{myshopifyDomain}}')['shop']['myshopifyDomain'] == s.BUTIK
    kol = json.load(open(os.path.join(mapp, 'kollektioner.json'), encoding='utf-8'))['kollektioner']
    ut = {}
    for i, c in enumerate(kol):
        if c['antal_produkter'] == 0:
            ut[c['id']] = fakta([]); continue
        prods, after = [], None
        while True:
            d = k.graphql(Q, {'id': c['id'], 'after': after})['collection']['products']
            prods += d['nodes']
            if not d['pageInfo']['hasNextPage']: break
            after = d['pageInfo']['endCursor']
        ut[c['id']] = fakta(prods)
        if i % 25 == 0: print(i, c['handle'], len(prods), flush=True)
    json.dump(ut, open(os.path.join(mapp, 'faktaunderlag.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('klart', k.antal_anrop, 'anrop')

if __name__ == '__main__':
    main(sys.argv[1])
