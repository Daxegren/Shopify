#!/usr/bin/env python3
"""Underlag med och utan produkter som har taggen price-change-job-active (BARA LÄSNING).
Användning: kategorier_underlag_ex_prisjobb.py <mapp med kollektioner.json> <handle>...
Skriver <mapp>/underlag/<handle>.json (alla produkter) och <mapp>/underlag_ex_prisjobb/<handle>.json (utan taggade)
samt <mapp>/prisjobb_jamforelse.json. Rör ingenting i butiken."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shopify_api as s
import kategorier_underlag as ku
TAGG = 'price-change-job-active'

class Filter:
    def __init__(self, k, ex): self.k, self.ex = k, ex
    def graphql(self, q, v=None):
        d = self.k.graphql(q, v)
        if self.ex:
            n = d['collection']['products']['nodes']
            d['collection']['products']['nodes'] = [p for p in n if TAGG not in (p.get('tags') or [])]
        return d

def main(mapp, handles):
    k = s.ShopifyKlient()
    assert k.graphql('{shop{myshopifyDomain}}')['shop']['myshopifyDomain'] == s.BUTIK
    kol = json.load(open(os.path.join(mapp, 'kollektioner.json'), encoding='utf-8'))['kollektioner']
    for sub in ('underlag', 'underlag_ex_prisjobb'): os.makedirs(os.path.join(mapp, sub), exist_ok=True)
    jam = {}
    for h in handles:
        a = ku.bygg(h, kol, Filter(k, False)); b = ku.bygg(h, kol, Filter(k, True))
        json.dump(a, open(os.path.join(mapp, 'underlag', h + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        json.dump(b, open(os.path.join(mapp, 'underlag_ex_prisjobb', h + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        jam[h] = {'alla': a['antal_koopbara'], 'utan_prisjobb': b['antal_koopbara'], 'marken_alla': a['marken'], 'marken_utan': b['marken'],
                  'kg_alla': [a['kg_i_titlar_min'], a['kg_i_titlar_max']], 'kg_utan': [b['kg_i_titlar_min'], b['kg_i_titlar_max']]}
        print(h, a['antal_koopbara'], b['antal_koopbara'], a['marken'][:5], flush=True)
    json.dump(jam, open(os.path.join(mapp, 'prisjobb_jamforelse.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
