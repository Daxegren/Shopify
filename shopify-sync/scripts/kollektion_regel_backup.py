#!/usr/bin/env python3
"""Sparar regel och medlemslista för en kollektion (bara läsning): kollektion_regel_backup.py HANDLE fore|efter
Skriver rapporter/shopify-original-2026-11-17/regel_<handle>_<fore|efter>.json. Nycklar läses ur miljön och skrivs aldrig ut."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shopify_api import ShopifyKlient, maska
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
def main(h, när):
    k = ShopifyKlient(); after = None; mem = []
    while True:
        r = k.graphql('query($h:String!,$a:String){ collectionByHandle(handle:$h){ id handle title sortOrder ruleSet{appliedDisjunctively rules{column relation condition}} products(first:100, after:$a){ pageInfo{hasNextPage endCursor} nodes{ id handle status totalInventory productType tags variants(first:50){nodes{id price compareAtPrice}} } } } }', {'h': h, 'a': after})['collectionByHandle']
        mem += r['products']['nodes']
        if not r['products']['pageInfo']['hasNextPage']: break
        after = r['products']['pageInfo']['endCursor']
    ut = {'kollektion': {x: r[x] for x in ('id', 'handle', 'title', 'sortOrder', 'ruleSet')}, 'antal_medlemmar': len(mem),
          'antal_koepbara': sum(1 for m in mem if m['status'] == 'ACTIVE' and (m['totalInventory'] or 0) > 0),
          'medlemmar': [[m['handle'], m['status'], m['totalInventory'], m['productType'], 'price-change-job-active' in m['tags'],
                         [[v['id'], v['price'], v['compareAtPrice']] for v in m['variants']['nodes']]] for m in mem]}
    fil = os.path.join(REPO, f'rapporter/shopify-original-2026-11-17/regel_{h}_{när}.json')
    json.dump(ut, open(fil, 'w'), ensure_ascii=False, indent=1)
    print(h, när, 'medlemmar', ut['antal_medlemmar'], 'köpbara', ut['antal_koepbara'], '->', os.path.relpath(fil, REPO))
if __name__ == '__main__':
    try: main(sys.argv[1], sys.argv[2])
    except Exception as e: print('FEL:', maska(e)); sys.exit(2)
