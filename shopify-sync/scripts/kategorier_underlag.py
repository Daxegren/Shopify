#!/usr/bin/env python3
"""Faktaunderlag med kod ur kollektionens egna produkter (BARA LÄSNING).
Användning: kategorier_underlag.py <mapp med kollektioner.json> <handle>... 
Skriver <mapp>/underlag/<handle>.json. Språkmodellen får skriva text bara av dessa uppgifter."""
import json, os, re, sys, collections, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shopify_api as s

Q = '''query($id:ID!,$after:String){collection(id:$id){products(first:250, after:$after){pageInfo{hasNextPage endCursor}
 nodes{id title vendor status tags tracksInventory totalInventory
  priceRangeV2{minVariantPrice{amount} maxVariantPrice{amount}}}}}}'''
KG = re.compile(r'(\d+(?:[.,]\d+)?)\s?kg\b', re.I)

HUVUD = {  # regex mot titelns två första ord (gemener): vad som räknas som kategorins huvudprodukter
    # (tillbehör har typordet först i titeln: "Cykelsadel ... för Motionscykel", "Golvskydd ... Kettlebell")
    'motionscykel': r'motionscykel|spinningcykel|träningscykel', 'lopband': r'löpband(?!s)', 'roddmaskin': r'roddmaskin',
    'crosstrainer': r'crosstrainer', 'hantlar': r'hantel|hantlar', 'kettlebell': r'kettlebell|sangpomm', 'cykellas': r'lås',
    'elcyklar': r'elcykel|el-lastcykel', 'tunturi': r'', 'sparkcykel': r'^(?!.*(?:barn|sticker|klistermärke))(?=.*(sparkcykel(?!hjul|stöd)|scooter(?!hjul|stick)))'}

# Tillägg 2026-11-17 (andra granskningen, lärdom 2026-11-12): produkter vars typord står senare i titeln eller på engelska
# ("Pro Chrome Hantel 0,5kg", "Quick-Lock Dumbbell", "Treadmill ...", "Electric bike ...") räknas med via regex mot HELA titeln.
# EXKLUDERA tar bort tillbehör som annars räknas som huvudprodukter (hantelställ, hantelstänger, hantellås) först i titeln.
EXTRA_HELA_TITELN = {'sparkcykel': r'\bscooter\b', 'hantlar': r'hantel|dumbbell', 'lopband': r'treadmill(?!.*(lubric|oil|spray|olja))', 'elcyklar': r'electric (cargo )?bike',
                     'cykellas': r'\b(cable|frame|chain) lock\b'}
EXKLUDERA = {'hantlar': r'ställ|stång|stäng|rack|tower|hållare|^skivstång\b|^hyllplan', 'cykellas': r'hantellås|skivstångslås|collar',
             'elcyklar': r'baklykta|lykta|skydd för|hjälm', 'sparkcykel': r'hjul|wheel|holder|sticker|snow|snö|grip|tejp|stöd|stand\b|pad\b'}
EXKLUDERA_HELA = {'hantlar': r'dumbbell (bar|stand|rack|tower)', 'sparkcykel': r'(scooter|sparkcykel)\s?(wheel|holder|hjul|sticker)|wheel|holder|sticker'}
HUVUD_V2 = {'hantlar': r'hantel|hantlar|dumbbell', 'cykellas': r'(?<!hantel)lås'}

def bygg(handle, kol, k):
    c = next(x for x in kol if x['handle'] == handle)
    prods, after = [], None
    while True:
        d = k.graphql(Q, {'id': c['id'], 'after': after})['collection']['products']
        prods += d['nodes']
        if not d['pageInfo']['hasNextPage']: break
        after = d['pageInfo']['endCursor']
    kop_alla = [p for p in prods if p['status'] == 'ACTIVE' and ((p['totalInventory'] or 0) > 0 or not p['tracksInventory'])]
    rx = re.compile(HUVUD_V2.get(handle, HUVUD.get(handle, '')), re.I)
    ex = re.compile(EXKLUDERA[handle], re.I) if handle in EXKLUDERA else None
    extra = re.compile(EXTRA_HELA_TITELN[handle], re.I) if handle in EXTRA_HELA_TITELN else None
    def ar_huvud(p):
        t = p['title']
        if ex and ex.search(' '.join(t.split()[:2])): return False
        if handle in EXKLUDERA_HELA and re.search(EXKLUDERA_HELA[handle], t, re.I): return False
        return bool(rx.search(' '.join(t.split()[:2])) or (extra and extra.search(t)))
    kop = [p for p in kop_alla if ar_huvud(p)]
    ovriga = [p['title'] for p in kop_alla if not ar_huvud(p)]
    pris = [float(p['priceRangeV2']['minVariantPrice']['amount']) for p in kop]
    pris_pos = [x for x in pris if x > 0]
    ord1 = collections.Counter(p['title'].split()[0].lower() for p in kop if p['title'].split())
    kgs = sorted({float(m.replace(',', '.')) for p in kop for m in KG.findall(p['title'])})
    return {'handle': handle, 'id': c['id'], 'titel': c['title'], 'regel': [(r['column'], r['relation'], r['condition']) for r in (c['ruleSet'] or {}).get('rules', [])],
            'huvud_regex': HUVUD.get(handle, ''), 'antal_i_kollektionen': len(prods), 'antal_koopbara_alla': len(kop_alla), 'antal_koopbara': len(kop), 'antal_ovriga_koopbara': len(ovriga), 'exempel_ovriga': ovriga[:6], 'ovriga_titlar': sorted(ovriga), 'ovriga_med_pris': sorted([p['title'], float(p['priceRangeV2']['minVariantPrice']['amount'])] for p in kop_alla if p['title'] in set(ovriga)),
            'marken': collections.Counter(p['vendor'] for p in kop).most_common(),
            'forsta_ord_i_titel': ord1.most_common(10),
            'pris_min': min(pris_pos) if pris_pos else None, 'pris_max': max(pris_pos) if pris_pos else None,
            'pris_median': statistics.median(pris_pos) if pris_pos else None, 'antal_utan_pris_noll': len(pris) - len(pris_pos),
            'kg_i_titlar_min': kgs[0] if kgs else None, 'kg_i_titlar_max': kgs[-1] if kgs else None, 'antal_titlar_med_kg': sum(1 for p in kop if KG.search(p['title'])),
            'billigaste': [(p['title'], float(p['priceRangeV2']['minVariantPrice']['amount'])) for p in sorted(kop, key=lambda p: float(p['priceRangeV2']['minVariantPrice']['amount'])) if float(p['priceRangeV2']['minVariantPrice']['amount']) > 0][:4],
            'dyraste': [(p['title'], float(p['priceRangeV2']['minVariantPrice']['amount'])) for p in sorted(kop, key=lambda p: -float(p['priceRangeV2']['minVariantPrice']['amount']))[:3]],
            'alla_titlar': sorted(p['title'] for p in kop)}

def main(mapp, handles):
    k = s.ShopifyKlient()
    assert k.graphql('{shop{myshopifyDomain}}')['shop']['myshopifyDomain'] == s.BUTIK
    kol = json.load(open(os.path.join(mapp, 'kollektioner.json'), encoding='utf-8'))['kollektioner']
    os.makedirs(os.path.join(mapp, 'underlag'), exist_ok=True)
    for h in handles:
        u = bygg(h, kol, k)
        json.dump(u, open(os.path.join(mapp, 'underlag', h + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(h, u['antal_koopbara'], u['marken'][:4], u['forsta_ord_i_titel'][:4], u['pris_min'], u['pris_max'], u['antal_utan_pris_noll'], u['kg_i_titlar_min'], u['kg_i_titlar_max'])

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
