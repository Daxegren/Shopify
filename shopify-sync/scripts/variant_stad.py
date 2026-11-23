#!/usr/bin/env python3
"""Byter variantnamn (alternativvärde) och vid behov SKU på angivna varianter. Rör aldrig pris, lager, status, taggar eller titel.
Plan (JSON): [{"produkt_id": "...", "varianter": [{"fran_sku": "..", "fran_namn": "..", "ny_sku": ".."|null, "nytt_namn": ".."}]}]
En variant identifieras av (SKU, nuvarande namn). Före-fil per produkt i KATALOG/fore/. Återläsning: nytt namn/SKU på rätt variant och allt annat
(id-ordning, pris, jämförpris, lager, status, titel, taggar) oförändrat. Stopp vid första avvikelse.
Användning: variant_stad.py PLAN.json --ut KATALOG (--dry-run | --kanarie | --rest | --aterstall)  (kanarie = första produkten, rest = övriga)"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shopify_api as s
Q = '''query($id:ID!){product(id:$id){id title status tags options{name} variants(first:100){nodes{id title sku price compareAtPrice inventoryQuantity inventoryPolicy selectedOptions{name value}}}}}'''
M = '''mutation($p:ID!,$v:[ProductVariantsBulkInput!]!){productVariantsBulkUpdate(productId:$p,variants:$v){productVariants{id} userErrors{field message}}}'''
def las(k, pid): return k.graphql(Q, {'id': pid})['product']
def stabil(p): return {'title': p['title'], 'status': p['status'], 'tags': sorted(p['tags']), 'v': {v['id']: (v['price'], v['compareAtPrice'], v['inventoryQuantity'], v['inventoryPolicy']) for v in p['variants']['nodes']}}
def hitta(p, sku, namn):
    c = [v for v in p['variants']['nodes'] if (v['sku'] or '') == sku and v['title'] == namn]
    return c[0] if len(c) == 1 else None
def main(a):
    plan = json.load(open(a[0], encoding='utf-8')); ut = a[a.index('--ut') + 1]; os.makedirs(os.path.join(ut, 'fore'), exist_ok=True)
    lage = next((x for x in ('--dry-run', '--kanarie', '--rest', '--aterstall') if x in a), None)
    if not lage: print('Ange läge'); return 2
    k = s.ShopifyKlient(); assert k.graphql('{shop{myshopifyDomain}}')['shop']['myshopifyDomain'] == s.BUTIK
    if lage == '--kanarie': plan = plan[:1]
    if lage == '--rest':
        if not os.path.exists(os.path.join(ut, 'kanarie_klar')): print('Kanarien först'); return 2
        plan = plan[1:]
    for pr in plan:
        pid = pr['produkt_id']; p = las(k, pid); ff = os.path.join(ut, 'fore', pid.split('/')[-1] + '.json')
        if not os.path.exists(ff): json.dump(p, open(ff, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        fore = json.load(open(ff, encoding='utf-8')); opt = p['options'][0]['name']
        upd, ok_plan = [], True
        for v in pr['varianter']:
            if lage == '--aterstall':
                cur = hitta(p, v['ny_sku'] or v['fran_sku'], v['nytt_namn'])
                if not cur: print('SAKNAS (återställ)', pid, v); ok_plan = False; continue
                upd.append({'id': cur['id'], 'optionValues': [{'optionName': opt, 'name': v['fran_namn']}], 'inventoryItem': {'sku': v['fran_sku']}}); continue
            cur = hitta(p, v['fran_sku'], v['fran_namn'])
            if not cur:
                if hitta(p, v['ny_sku'] or v['fran_sku'], v['nytt_namn']): print('redan klar', pid.split('/')[-1], v['nytt_namn']); continue
                print('STOPP: hittar inte', pid, v); return 1
            u = {'id': cur['id'], 'optionValues': [{'optionName': opt, 'name': v['nytt_namn']}]}
            if v.get('ny_sku'): u['inventoryItem'] = {'sku': v['ny_sku']}
            upd.append(u)
        if lage == '--dry-run': print(pid.split('/')[-1], [(x['optionValues'][0]['name'], x.get('inventoryItem')) for x in upd]); continue
        if not ok_plan: return 1
        if stabil(p) != stabil(fore): print('STOPP: produkten har ändrats sedan före-filen (pris, lager, status, titel eller taggar)', pid); return 1
        if not upd: continue
        r = k.graphql(M, {'p': pid, 'v': upd})['productVariantsBulkUpdate']
        if r['userErrors']: print('STOPP userErrors', pid, r['userErrors']); return 1
        n = las(k, pid); fel = []
        if stabil(n) != stabil(fore): fel.append('pris/lager/status/titel/taggar ändrade')
        for u in upd:
            nv = next((x for x in n['variants']['nodes'] if x['id'] == u['id']), None)
            if not nv or nv['title'] != u['optionValues'][0]['name'] or ('inventoryItem' in u and nv['sku'] != u['inventoryItem']['sku']): fel.append('namn/SKU ej som avsett ' + u['id'])
        print(pid.split('/')[-1], 'verifierad' if not fel else 'AVVIKELSE ' + str(fel))
        if fel: return 1
    if lage == '--kanarie': open(os.path.join(ut, 'kanarie_klar'), 'w').write('ok')
    return 0
if __name__ == '__main__': sys.exit(main(sys.argv[1:]))
