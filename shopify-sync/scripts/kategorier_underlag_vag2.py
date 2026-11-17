#!/usr/bin/env python3
"""Underlag för våg 2 (BARA LÄSNING): samma som kategorier_underlag.py men med typordsregex per kollektion (2026-11-17).
Användning: kategorier_underlag_vag2.py <mapp med kollektioner.json> <handle>...  -> <mapp>/underlag/<handle>.json"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shopify_api as s
import kategorier_underlag as ku
# Regex mot titelns två första ord (gemener). Tomt = alla köpbara räknas.
ku.HUVUD.update({'traningsmaskin': r'', 'herrcyklar': r'herrcykel|stadscykel', 'hybridcykel': r'hybridcykel(?!s)',
                 'traningsbank': r'träningsbänk', 'traningsutrustning-for-hemmagym': r'', 'grepptraning': r'', 'boxning': r'',
                 'racercykel': r'landsvägscykel(?!sadl)|racercykel|^cykel giant tcr', 'stankskarmar-cykel': r'skärm|stänk'})
ku.EXKLUDERA.update({'stankskarmar-cykel': r'fästklämma|fäste|förlängning|baklykta', 'racercykel': r'sadlar'})
if __name__ == '__main__':
    mapp, handles = sys.argv[1], sys.argv[2:]
    k = s.ShopifyKlient()
    assert k.graphql('{shop{myshopifyDomain}}')['shop']['myshopifyDomain'] == s.BUTIK
    kol = json.load(open(os.path.join(mapp, 'kollektioner.json'), encoding='utf-8'))['kollektioner']
    os.makedirs(os.path.join(mapp, 'underlag'), exist_ok=True)
    for h in handles:
        u = ku.bygg(h, kol, k)
        json.dump(u, open(os.path.join(mapp, 'underlag', h + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(h, u['antal_koopbara'], '/', u['antal_koopbara_alla'], u['marken'][:6], u['forsta_ord_i_titel'][:5])
