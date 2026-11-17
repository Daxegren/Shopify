#!/usr/bin/env python3
"""Läsande inventering av alla produkter i en butik (BARA LÄSNING, skriver inget i Shopify).

Sparar alla_produkter.json i given katalog (skrivs aldrig över): id, title, handle, status, vendor, productType, tags,
totalInventory, createdAt, updatedAt, seo_title, seo_description, html_tecken, har_standardblock, har_leveranstidsmening.
Själva beskrivningstexten sparas inte (storlek); standardblocket kontrolleras mot profilens `standardblock_krav`.
Användning: inventera_bos.py --ut KATALOG [--profil BUTIKSPROFIL.json] [--sida N]
"""
import json, os, sys, time

HAR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HAR)
import shopify_api as api  # noqa: E402
import butiksprofil  # noqa: E402

Q = '''query($after:String,$n:Int!){products(first:$n,after:$after,sortKey:ID){
 pageInfo{hasNextPage endCursor}
 nodes{id title handle status vendor productType tags totalInventory createdAt updatedAt
  seo{title description} descriptionHtml}}}'''


def kompakt(p, krav, lev):
    h = p.get('descriptionHtml') or ''
    seo = p.get('seo') or {}
    return {'id': p['id'], 'title': p['title'], 'handle': p['handle'], 'status': p['status'], 'vendor': p['vendor'],
            'productType': p['productType'], 'tags': p['tags'], 'totalInventory': p['totalInventory'],
            'createdAt': p['createdAt'], 'updatedAt': p['updatedAt'],
            'seo_title': seo.get('title'), 'seo_description': seo.get('description'),
            'html_tecken': len(h), 'har_standardblock': all(k in h for k in krav), 'har_leveranstidsmening': bool(lev) and lev in h}


def main(argv=None):
    profil, a = butiksprofil.profil_fran_argv(argv if argv is not None else sys.argv[1:])
    ut, sida = None, 50
    if '--ut' in a:
        k = a.index('--ut'); ut = a[k + 1]; del a[k:k + 2]
    if '--sida' in a:
        k = a.index('--sida'); sida = int(a[k + 1]); del a[k:k + 2]
    if not ut:
        print(__doc__); return 2
    fil = os.path.join(ut, 'alla_produkter.json')
    if os.path.exists(fil):
        print(fil, 'finns redan; skrivs inte över.'); return 1
    klient = api.klient_fran_profil(profil)
    print('Butik:', api.verifiera_butik(klient))
    # den normaliserade profilen innehåller inte kontrollfälten; läs dem ur profilfilen
    rå = json.load(open(os.path.join(butiksprofil.ROT, butiksprofil.relativ_sokvag(profil)), encoding='utf-8'))
    krav, lev = rå.get('standardblock_krav') or [], rå.get('leveranstidsmening')
    if not krav:
        print('FEL: profilen saknar standardblock_krav; kontrollen vore meningslös.'); return 1
    alla, after, t0 = [], None, time.time()
    while True:
        d = klient.graphql(Q, {'after': after, 'n': sida})['products']
        alla.extend(kompakt(p, krav, lev) for p in d['nodes'])
        if len(alla) % 500 < sida:
            print(f'  {len(alla)} lästa ({int(time.time() - t0)} s, {klient.antal_anrop} anrop)', flush=True)
        if not d['pageInfo']['hasNextPage']:
            break
        after = d['pageInfo']['endCursor']
    ids = [p['id'] for p in alla]
    assert len(ids) == len(set(ids)), 'dubbla id i inventeringen'
    os.makedirs(ut, exist_ok=True)
    json.dump(alla, open(fil, 'x', encoding='utf-8'), ensure_ascii=False)
    print(f'Klart: {len(alla)} produkter, {klient.antal_anrop} anrop, {int(time.time() - t0)} s. Sparad: {fil}')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (api.ShopifyFel, butiksprofil.ProfilFel) as e:
        print('FEL:', api.maska(e)); sys.exit(1)
