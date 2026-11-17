#!/usr/bin/env python3
"""Läsande: hämtar live-källa (titel, typ, märke, taggar, beskrivning, SEO, varianter med SKU/EAN/pris/jämförpris/lager) för produkter.
BARA LÄSNING. Skriver aldrig över en befintlig utfil. Priser sparas bara som underlag (R3, prisjämförelse före/efter), aldrig i texter.
Användning: las_kallunderlag.py IDFIL.json UTFIL.json [--profil BUTIKSPROFIL.json]
  IDFIL: JSON-lista med produkt-id (siffror eller gid) eller objekt med fältet id.
"""
import json, os, sys
HAR = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HAR)
import shopify_api as api  # noqa: E402
import butiksprofil  # noqa: E402

Q = '''query($ids:[ID!]!){nodes(ids:$ids){... on Product{id title handle status vendor productType tags totalInventory updatedAt
 seo{title description} descriptionHtml
 variants(first:100){nodes{id title sku barcode price compareAtPrice inventoryQuantity selectedOptions{name value}}}}}}'''


def hamta(klient, ids, n=10):
    ut = []
    for s in range(0, len(ids), n):
        ut.extend(klient.graphql(Q, {'ids': [api.gid(i) for i in ids[s:s + n]]})['nodes'])
    return ut


def main():
    profil, a = butiksprofil.profil_fran_argv(sys.argv[1:])
    if len(a) != 2: print(__doc__); return 2
    ids = [x['id'] if isinstance(x, dict) else x for x in json.load(open(a[0], encoding='utf-8'))]
    if os.path.exists(a[1]): print(a[1], 'finns redan; skrivs inte över.'); return 1
    k = api.klient_fran_profil(profil)
    print('Butik:', api.verifiera_butik(k))
    P = hamta(k, ids)
    saknas = [i for i, p in zip(ids, P) if not p]
    json.dump([p for p in P if p], open(a[1], 'x', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{len([p for p in P if p])} av {len(ids)} lästa; saknas: {saknas}; anrop: {k.antal_anrop}')
    return 1 if saknas else 0


if __name__ == '__main__':
    try: sys.exit(main())
    except (api.ShopifyFel, butiksprofil.ProfilFel) as e: print('FEL:', api.maska(e)); sys.exit(1)
