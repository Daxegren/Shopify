#!/usr/bin/env python3
"""Skriver kollektionstexter (descriptionHtml + SEO-titel + SEO-beskrivning) i BEST OF SPORTS. Rör inget annat.
Användning: kategorier_skriv.py TEXTFIL.py FORE_LIVE.json --ut KATALOG (--dry-run | --kanarie | --rest) [--tillagg TILLAGG.json]
  TEXTFIL.py       handle -> (stycken, seo_titel, meta)   (samma format som pilot_texter_v2.py)
  FORE_LIVE.json   handle -> kollektionens live-fält när underlaget togs; descriptionHtml måste fortfarande vara lika live
  --tillagg        handle -> html som läggs EFTER de nya styckena (bevarade länkmeningar)
Läge: --dry-run (ingen skrivning), --kanarie (3 första), --rest (övriga, delar om 4). Före-fil per kollektion i KATALOG/<handle>.json.
Efter varje skrivning: återläsning och jämförelse tecken för tecken (descriptionHtml, seo.title, seo.description); övriga fält
(handle, titel, regler, sortering, mall, bild, antal) och kollektionens produkter (id, status, taggar, pris) ska vara oförändrade.
Stopp vid första avvikelse (kod 1). Mutationen är collectionUpdate(collection:{id,descriptionHtml,seo}) och ändrar inga produkter."""
import json, os, sys, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shopify_api as s
import kategorier_live as L

DEL, KANARIE = 4, 3
MUT = '''mutation($c:CollectionUpdateInput!){collectionUpdate(collection:$c){collection{id} userErrors{field message}}}'''
QP = '''query($id:ID!,$a:String){collection(id:$id){products(first:250,after:$a){pageInfo{hasNextPage endCursor}
 nodes{id status tags priceRangeV2{minVariantPrice{amount}}}}}}'''

def html_av(stycken): return ''.join(f'<p>{x}</p>' for x in stycken)

def produkter(k, cid):
    ut, a = {}, None
    while True:
        d = k.graphql(QP, {'id': cid, 'a': a})['collection']['products']
        for p in d['nodes']: ut[p['id']] = (p['status'], tuple(sorted(p['tags'])), p['priceRangeV2']['minVariantPrice']['amount'])
        if not d['pageInfo']['hasNextPage']: return ut
        a = d['pageInfo']['endCursor']

def lasa_texter(sokvag):
    spec = importlib.util.spec_from_file_location('t', sokvag); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.T

def main(argv):
    textfil, forefil = argv[0], argv[1]
    ut = argv[argv.index('--ut') + 1]; os.makedirs(ut, exist_ok=True)
    tillagg = json.load(open(argv[argv.index('--tillagg') + 1], encoding='utf-8')) if '--tillagg' in argv else {}
    lage = 'dry' if '--dry-run' in argv else 'kanarie' if '--kanarie' in argv else 'rest' if '--rest' in argv else None
    if not lage: print('Ange --dry-run, --kanarie eller --rest'); return 2
    T, fore = lasa_texter(textfil), json.load(open(forefil, encoding='utf-8'))
    k = s.ShopifyKlient()
    assert k.graphql('{shop{myshopifyDomain}}')['shop']['myshopifyDomain'] == s.BUTIK
    resf = os.path.join(ut, 'resultat.json')
    res = json.load(open(resf, encoding='utf-8')) if os.path.exists(resf) else {}
    live = {c['handle']: c for c in L.las(k, [fore[h]['id'] for h in T])}
    skriv, rapport = [], {}
    for h, (stycken, seo, meta) in T.items():
        c, mal = live[h], html_av(stycken) + tillagg.get(h, '')
        if c['id'] != fore[h]['id'] or c['handle'] != h: rapport[h] = 'AVVIKER: id/handle'; continue
        if res.get(h, {}).get('status') == 'verifierad': rapport[h] = 'redan skriven och verifierad' if (c['descriptionHtml'], c['seo']['title'], c['seo']['description']) == (mal, seo, meta) else 'AVVIKER: skriven kollektion har ändrats efter verifiering'; continue
        if c['descriptionHtml'] != fore[h]['descriptionHtml']: rapport[h] = 'AVVIKER: beskrivningen har ändrats live sedan underlaget togs'; continue
        if (c['descriptionHtml'], c['seo']['title'], c['seo']['description']) == (mal, seo, meta): rapport[h] = 'redan lika målet'; continue
        rapport[h] = 'skriv'; skriv.append(h)
    for h, r in rapport.items(): print(f'{h:14s} {r}')
    def spara_fore(h):   # före-fil: komplett live-läge före skrivning; skrivs bara om den saknas (originalet ska aldrig skrivas över)
        fn = os.path.join(ut, h + '.json')
        if not os.path.exists(fn):
            json.dump({'fore': live[h], 'produkter_fore': {a: list(b) for a, b in produkter(k, live[h]['id']).items()}},
                      open(fn, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for h in T: spara_fore(h)
    if lage == 'dry' or any(r.startswith('AVVIKER') for r in rapport.values()):
        json.dump(rapport, open(os.path.join(ut, 'torrkorning.json'), 'w'), ensure_ascii=False, indent=1)
        return 1 if any(r.startswith('AVVIKER') for r in rapport.values()) else 0
    del_ = skriv[:KANARIE] if lage == 'kanarie' else skriv
    if lage == 'rest' and not os.path.exists(os.path.join(ut, 'kanarie_klar')): print('Kanarien ska köras och verifieras först'); return 2
    for i in range(0, len(del_), DEL if lage == 'rest' else KANARIE):
        for h in del_[i:i + (DEL if lage == 'rest' else KANARIE)]:
            stycken, seo, meta = T[h]; mal = html_av(stycken) + tillagg.get(h, ''); c = live[h]
            spara_fore(h)
            pfore = produkter(k, c['id'])
            r = k.graphql(MUT, {'c': {'id': c['id'], 'descriptionHtml': mal, 'seo': {'title': seo, 'description': meta}}})['collectionUpdate']
            if r['userErrors']: print('STOPP userErrors', h, r['userErrors']); res[h] = {'status': 'fel'}; json.dump(res, open(resf, 'w'), indent=1); return 1
            e = L.las(k, [c['id']])[0]; fel = []
            if e['descriptionHtml'] != mal: fel.append('descriptionHtml')
            if e['seo']['title'] != seo: fel.append('seo.title')
            if e['seo']['description'] != meta: fel.append('seo.description')
            if L.ovriga_falt(e) != L.ovriga_falt(c): fel.append('övriga kollektionsfält ändrade')
            if produkter(k, c['id']) != pfore: fel.append('produkter (status/taggar/pris) ändrade')
            res[h] = {'status': 'verifierad' if not fel else 'AVVIKELSE', 'fel': fel}
            json.dump(res, open(resf, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            print(h, res[h])
            if fel: return 1
    if lage == 'kanarie': open(os.path.join(ut, 'kanarie_klar'), 'w').write('ok')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
