#!/usr/bin/env python3
"""Lägger till EN tagg per rad i en CSV (kollektion;tagg_att_lagga_till;produkt_id;...). Rör inget annat.
Användning: taggar_lagg_till.py CSV --ut KATALOG (--dry-run | --kanarie | --rest | --aterstall) [--hoppa-over ID,ID]
Före-fil per produkt i KATALOG/fore/<id>.json (status, handle, taggar, varianternas pris/jämförpris). Efter varje skrivning: återläsning;
taggen ska ha tillkommit och allt annat (status, handle, titel, övriga taggar, pris) vara oförändrat. Stopp vid första avvikelse.
--kanarie: första kollektionen i filen (alla dess produkter). --rest: övriga i grupper om 5. --aterstall: tagsRemove för det som lagts till."""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shopify_api as s
Q = '''query($id:ID!){product(id:$id){id title handle status tags variants(first:100){nodes{id price compareAtPrice}}}}'''
ADD = '''mutation($id:ID!,$t:[String!]!){tagsAdd(id:$id,tags:$t){node{id} userErrors{field message}}}'''
REM = '''mutation($id:ID!,$t:[String!]!){tagsRemove(id:$id,tags:$t){node{id} userErrors{field message}}}'''
def las(k, pid): return k.graphql(Q, {'id': pid})['product']
def stil(p): return {'title': p['title'], 'handle': p['handle'], 'status': p['status'], 'v': [(v['id'], v['price'], v['compareAtPrice']) for v in p['variants']['nodes']]}
def main(a):
    rader = list(csv.DictReader(open(a[0], encoding='utf-8'), delimiter=';'))
    ut = a[a.index('--ut') + 1]; os.makedirs(os.path.join(ut, 'fore'), exist_ok=True)
    skip = set(a[a.index('--hoppa-over') + 1].split(',')) if '--hoppa-over' in a else set()
    rader = [r for r in rader if r['produkt_id'] not in skip]
    lage = next((x for x in ('--dry-run', '--kanarie', '--rest', '--aterstall') if x in a), None)
    if not lage: print('Ange läge'); return 2
    k = s.ShopifyKlient(); assert k.graphql('{shop{myshopifyDomain}}')['shop']['myshopifyDomain'] == s.BUTIK
    resf = os.path.join(ut, 'resultat.json'); res = json.load(open(resf)) if os.path.exists(resf) else {}
    kolls = list(dict.fromkeys(r['kollektion'] for r in rader))
    if lage == '--kanarie': rader = [r for r in rader if r['kollektion'] == kolls[0]]
    if lage == '--rest':
        if not os.path.exists(os.path.join(ut, 'kanarie_klar')): print('Kanarien först'); return 2
        rader = [r for r in rader if r['kollektion'] != kolls[0]]
    for r in rader:
        pid, tagg = r['produkt_id'], r['tagg_att_lagga_till']; p = las(k, pid)
        ff = os.path.join(ut, 'fore', pid.split('/')[-1] + '.json')
        if not os.path.exists(ff): json.dump(p, open(ff, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        fore = json.load(open(ff, encoding='utf-8'))
        if lage == '--dry-run':
            print(pid.split('/')[-1], 'redan' if tagg in p['tags'] else 'lägg till', '|', p['status'], '|', p['title'][:50]); continue
        if lage == '--aterstall':
            if res.get(pid, {}).get('lagd') and tagg in p['tags']:
                e = k.graphql(REM, {'id': pid, 't': [tagg]})['tagsRemove']
                print('återställd', pid.split('/')[-1], e['userErrors'] or 'ok'); res[pid]['aterstalld'] = True
            continue
        if p['status'] != 'ACTIVE' or stil(p) != stil(fore): print('STOPP: produkten har ändrats sedan före-filen', pid); return 1
        if tagg in p['tags']: print('redan', pid.split('/')[-1]); continue
        e = k.graphql(ADD, {'id': pid, 't': [tagg]})['tagsAdd']
        if e['userErrors']: print('STOPP userErrors', pid, e['userErrors']); return 1
        n = las(k, pid); ok = tagg in n['tags'] and sorted(set(n['tags']) - {tagg}) == sorted(fore['tags']) and stil(n) == stil(fore)
        res[pid] = {'tagg': tagg, 'lagd': True, 'verifierad': ok}; json.dump(res, open(resf, 'w'), indent=1)
        print(r['kollektion'], pid.split('/')[-1], 'verifierad' if ok else 'AVVIKELSE')
        if not ok: return 1
    if lage == '--kanarie': open(os.path.join(ut, 'kanarie_klar'), 'w').write('ok')
    if lage == '--aterstall': json.dump(res, open(resf, 'w'), indent=1)
    return 0
if __name__ == '__main__': sys.exit(main(sys.argv[1:]))
