#!/usr/bin/env python3
"""Inventerar alla kollektioner i BEST OF SPORTS (BARA LÄSNING).
Sparar rapporter/bos-kategorier-<datum>/kollektioner.json. Använder shopify_api.ShopifyKlient
(token i minnet). Kontrollerar butiken (shop.myshopifyDomain) före och efter."""
import json, os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shopify_api as s

Q = '''query($after:String){collections(first:50, after:$after){pageInfo{hasNextPage endCursor}
 nodes{id title handle updatedAt sortOrder descriptionHtml
  seo{title description} image{url altText}
  ruleSet{appliedDisjunctively rules{column relation condition}}
  productsCount{count}
  da:translations(locale:"da"){key value} fi:translations(locale:"fi"){key value}
  sv:translations(locale:"sv"){key value}}}}'''

def main(ut):
    k = s.ShopifyKlient()
    shop = k.graphql('{shop{myshopifyDomain}}')['shop']['myshopifyDomain']
    assert shop == s.BUTIK, shop
    alla, after = [], None
    while True:
        d = k.graphql(Q, {'after': after})['collections']
        alla += d['nodes']
        if not d['pageInfo']['hasNextPage']: break
        after = d['pageInfo']['endCursor']
    for c in alla:
        c['antal_produkter'] = c.pop('productsCount')['count']
        c['typ'] = 'smart' if c['ruleSet'] else 'manuell'
        for l in ('sv', 'da', 'fi'):
            c[l] = {t['key']: t['value'] for t in c.pop(l)}
    os.makedirs(ut, exist_ok=True)
    with open(os.path.join(ut, 'kollektioner.json'), 'w', encoding='utf-8') as f:
        json.dump({'butik': shop, 'datum': datetime.date.today().isoformat(), 'kollektioner': alla}, f, ensure_ascii=False, indent=1)
    print(len(alla), 'kollektioner,', k.antal_anrop, 'anrop')

if __name__ == '__main__':
    main(sys.argv[1])
