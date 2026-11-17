#!/usr/bin/env python3
"""Struktur för kollektioner i BEST OF SPORTS: backup, mål-tabell, torrkörning och priskontroll (2026-11-17).

Bara läsning mot Admin API (nycklar ur miljön, aldrig utskrivna). Skriver inga ändringar i Shopify.

  python3 kategorier_struktur_underlag.py backup     # före-fil i rapporter/shopify-original-2026-11-17/
  python3 kategorier_struktur_underlag.py tabell     # mål-tabell (CSV) med kontroller live
  python3 kategorier_struktur_underlag.py pris NAMN  # prisögonblicksbild av produkterna i körklara källor
  python3 kategorier_struktur_underlag.py pris-jamfor FORE EFTER

Planen nedan är enda källan till vad som körs (KOR) och vad som väntar på Davids ja (VANTAR).
"""
import csv, hashlib, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shopify_api import ShopifyKlient, maska

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
GSC = os.path.join(REPO, 'rapporter/gsc-bestofsports-2026-11-12/kollektioner.csv')
UT_ORIG = os.path.join(REPO, 'rapporter/shopify-original-2026-11-17')
UT_RAPP = os.path.join(REPO, 'rapporter/bos-kategorier-2026-11-17')
WEBBSHOP = 'gid://shopify/Publication/164625875210'  # Online Store
PRIS_TAGG = 'price-change-job-active'

# (källa, mål, grupp, motivering)
KOR = [
    ('pwo-energipulver', 'pre-workout-pwo', 'pwo', 'Samma ämne. Målet har 4 102 visningar; källan ligger utanför topp 150 (högst 235).'),
    ('benmaskiner', 'traningsmaskin', 'ben', 'Överordnad kollektion med flest visningar i gruppen (3 192).'),
    ('benspark', 'traningsmaskin', 'ben', 'Samma som benmaskiner.'),
    ('bankpresspaket', 'traningsbank', 'bänk', 'Bänkpress hör till träningsbänk (3 432 visningar).'),
    ('situps-bank', 'traningsbank', 'bänk', 'Överordnad kollektion (3 432 visningar).'),
    ('stallbar-traningsbank', 'traningsbank', 'bänk', 'Överordnad kollektion (3 432 visningar).'),
    ('vevparti-cykel', 'cykelkedjor', 'cykel-drivlina', 'Drivlina; målet har flest visningar bland närliggande (1 443).'),
    ('klingor-och-kassett', 'cykelkedjor', 'cykel-drivlina', 'Drivlina; målet har flest visningar bland närliggande (1 443).'),
    ('cykeldatorer', 'cykeltillbehor', 'cykel-delar', 'Överordnad cykelkollektion (1 193 visningar).'),
    ('bromsar-cykel', 'cykeltillbehor', 'cykel-delar', 'Överordnad cykelkollektion (1 193 visningar).'),
    ('nav-cykel', 'cykeltillbehor', 'cykel-delar', 'Överordnad cykelkollektion (1 193 visningar).'),
    ('kettlebellpaket', 'kettlebell', 'kettlebell', 'Överordnad kollektion (1 884 visningar).'),
    ('skivstang-50-mm', 'skivstang', 'skivstång', 'Överordnad kollektion (387 visningar, källan 263).'),
    ('skivstangspaket', 'skivstangsset', 'överlapp', 'Överlappar skivstangsset (samma produkter); skivstangsset starkast (1 232 mot 1 209).'),
    ('cargobikes', 'ladcyklar', 'överlapp', 'Samma taggregel och samma 72 produkter; ladcyklar starkast (1 507 mot 321).'),
    ('aminosyror', 'aminosyror-1', 'överlapp', 'Samma produkter; aminosyror-1 starkast (258 mot högst 235).'),
    ('proteinpulver-1', 'proteinpulver', 'överlapp', 'Samma produkter; proteinpulver starkast (1 197 mot högst 235).'),
    ('solglasogon', 'cykelsolglasogon', 'överlapp', 'Samma 20 produkter; cykelsolglasogon starkast (2 526 mot högst 235).'),
]

# (källa, föreslaget mål, orsak till att den väntar)
VANTAR = [
    ('tranings-t-shirt-dam', 'sportutrustning', 'Inga matchande produkter finns (4 T-shirt-produkter, alla utkast, lager 0, Gorilla Sports). Föreslaget mål är en svag matchning.'),
    ('tranings-t-shirt-herr', 'sportutrustning', 'Som tranings-t-shirt-dam.'),
    ('traningsbyxor-dam', 'sportutrustning', 'Klädkollektion; inget klädsortiment finns. Föreslaget mål är en svag matchning.'),
    ('traningsbyxor-herr', 'sportutrustning', 'Som traningsbyxor-dam.'),
    ('traningstroja-dam', 'sportutrustning', 'Som traningsbyxor-dam.'),
    ('traningstroja-herr', 'sportutrustning', 'Som traningsbyxor-dam.'),
    ('traningsshorts-dam', 'sportutrustning', 'Som traningsbyxor-dam.'),
    ('cykelreservdelar', 'cykeltillbehor', 'Föreslaget mål har färre visningar (1 193) än källan (1 780).'),
    ('slam-ball', 'traningsboll', 'Föreslaget mål har färre visningar (334) än källan (486).'),
    ('barnskidor', 'skidor', 'Föreslaget mål har färre visningar (467) än källan (534). Dessutom pekar en gammal omdirigering (konditionsutrustning-kopia) hit.'),
    ('trap-bar-hex-bar', 'skivstang', 'Föreslaget mål har färre visningar (387) än källan (723).'),
    ('barncyklar-8-12-ar-24', 'barncyklar', 'Målet saknas i topp 150 (högst 235) medan källan har 332 visningar.'),
    ('multigymspaket', 'traningsmaskin', 'Har nu 5 aktiva produkter (slutsålda). Sidan är inte tom.'),
    ('hantelset', 'hantlar', 'Har 5 aktiva produkter (slutsålda). Sidan är inte tom.'),
    ('ribbstol', 'hemmagym', 'Har 1 aktiv produkt (slutsåld) och svag matchning.'),
    ('vibrationsplatts', 'konditionsutrustning', 'Har 2 aktiva produkter (slutsålda) och svag matchning.'),
    ('kettler', '', 'Position 12,9 med 9 klick; inget lämpligt mål; märkessidor väntar.'),
    ('christopeit-sport-germany', '', 'Ska inte omdirigeras; samlingsregeln är fel (märke), position 11,9 med 4 klick.'),
    ('koner-hoga-och-laga', 'traningstillbehor', 'Manuell tom kollektion; svag matchning.'),
    ('produkter-for-crossfit', 'traningsutrustning-for-crossfit-kop-crossfit-utrustning', 'Målet är inte publicerat (0 kanaler).'),
    ('traningsutrustning-for-viktnedgang', 'konditionsutrustning', 'Ny sida med egen text (ändrad 2026-11-16) och 882 produkter; annan sökavsikt än målet.'),
    ('hopfallbar-gymutrustning', 'hopfallbara-cyklar', 'Annan sökavsikt (gym mot cykel); alla aktiva produkter är idag cyklar.'),
    ('viktpaket', 'gympaket-1', 'Varken källa eller mål finns i topp 150; starkaste sida kan inte avgöras utan gsc_export.'),
    ('varumarke', 'all', 'Systemsida (varumärkesindex, 5 030 produkter); slås inte ihop utan beslut.'),
    ('alla-produkter-best-of-sports', 'all', 'Systemsida (5 030 produkter); slås inte ihop utan beslut.'),
]


def gsc():
    d = {}
    with open(GSC, encoding='utf-8') as f:
        for r in csv.DictReader(f):
            d[r['handle']] = r
    return d


FRAG = '''id handle title updatedAt sortOrder templateSuffix descriptionHtml seo { title description }
  productsCount { count }
  ruleSet { appliedDisjunctively rules { column relation condition } }'''


def hamta(k, handle):
    r = k.graphql('query($h:String!){ collectionByHandle(handle:$h){ %s } }' % FRAG, {'h': handle})
    return r['collectionByHandle']


def produkter(k, coll_id, max_antal=400):
    ut, after = [], None
    while len(ut) < max_antal:
        r = k.graphql('''query($id:ID!,$a:String){ collection(id:$id){ products(first:100, after:$a){ pageInfo{hasNextPage endCursor}
          nodes{ id handle status totalInventory tags variants(first:50){ nodes{ id price compareAtPrice } } } } } }''',
                      {'id': coll_id, 'a': after})['collection']['products']
        ut += r['nodes']
        if not r['pageInfo']['hasNextPage']:
            break
        after = r['pageInfo']['endCursor']
    return ut


def kopbara(p):
    return [x for x in p if x['status'] == 'ACTIVE' and (x['totalInventory'] or 0) > 0]


# Appen saknar read_publications. Publicering i Online Store (kanal 164625875210) lästes live via Shopify MCP 2026-11-17
# (resourcePublicationsV2): alla kollektioner i planen utom crossfit-målet är publicerade där. Kontrolleras om via MCP före varje skrivning.
EJ_PUBLICERADE = {'traningsutrustning-for-crossfit-kop-crossfit-utrustning'}


def pa_webbshop(c):
    return c is not None and c['handle'] not in EJ_PUBLICERADE


def alla_handles():
    h = [a for a, *_ in KOR] + [b for _, b, *_ in KOR] + [a for a, *_ in VANTAR] + [b for _, b, _ in VANTAR if b]
    return sorted(set(h))


def backup(k):
    os.makedirs(UT_ORIG, exist_ok=True)
    ut = {'tagen': 'rapporter/shopify-original-2026-11-17/kollektioner_fore.json', 'butik': k.butik, 'kollektioner': {}}
    for h in alla_handles():
        c = hamta(k, h)
        if c is None:
            ut['kollektioner'][h] = None
            continue
        p = produkter(k, c['id'])
        c['produkter_handles_status_lager'] = [[x['handle'], x['status'], x['totalInventory']] for x in p]
        ut['kollektioner'][h] = c
    fil = os.path.join(UT_ORIG, 'kollektioner_fore.json')
    with open(fil, 'w', encoding='utf-8') as f:
        json.dump(ut, f, ensure_ascii=False, indent=1, sort_keys=True)
    print('Sparade', len(ut['kollektioner']), 'kollektioner i', os.path.relpath(fil, REPO), 'sha256', hashlib.sha256(open(fil, 'rb').read()).hexdigest()[:16])


def tabell(k):
    g = gsc()
    rader = []
    live = {}

    def lev(h):
        if h not in live:
            c = hamta(k, h)
            live[h] = (c, produkter(k, c['id']) if c else [])
        return live[h]

    def v(h):
        r = g.get(h)
        return (r['visningar'], r['klick'], r['position']) if r else ('≤235 (utanför topp 150)', '', '')

    for kalla, mal, grupp, mot in KOR:
        sc, sp = lev(kalla)
        mc, mp = lev(mal)
        sh = {x['handle'] for x in kopbara(sp)}
        mh = {x['handle'] for x in mp}
        kontroller = {
            'källan_finns': sc is not None, 'källan_publicerad_webbshop': pa_webbshop(sc),
            'målet_finns': mc is not None, 'målet_publicerat_webbshop': pa_webbshop(mc),
            'mål_köpbara': len(kopbara(mp)),
            'källans_köpbara_finns_i_målet': sh <= mh,
            'källans_köpbara': len(sh),
        }
        ok = all([kontroller['källan_finns'], kontroller['källan_publicerad_webbshop'], kontroller['målet_finns'],
                  kontroller['målet_publicerat_webbshop'], kontroller['mål_köpbara'] > 0, kontroller['källans_köpbara_finns_i_målet']])
        rader.append({'beslut': 'körklar (väntar på avpublicering)' if ok else 'STOPP: kontroll misslyckades', 'källa': kalla, 'mål': mal, 'grupp': grupp,
                      'källa_visningar': v(kalla)[0], 'källa_position': v(kalla)[2], 'mål_visningar': v(mal)[0], 'mål_position': v(mal)[2],
                      'motivering': mot, **{kk: vv for kk, vv in kontroller.items()}})
    for kalla, mal, orsak in VANTAR:
        sc, sp = lev(kalla)
        mc = mp = None
        if mal:
            mc, mp = lev(mal)
        rader.append({'beslut': 'väntar på Davids ja', 'källa': kalla, 'mål': mal, 'grupp': '',
                      'källa_visningar': v(kalla)[0], 'källa_position': v(kalla)[2], 'mål_visningar': v(mal)[0] if mal else '', 'mål_position': v(mal)[2] if mal else '',
                      'motivering': orsak, 'källan_finns': sc is not None, 'källan_publicerad_webbshop': pa_webbshop(sc),
                      'målet_finns': (mc is not None) if mal else '', 'målet_publicerat_webbshop': pa_webbshop(mc) if mal else '',
                      'mål_köpbara': len(kopbara(mp)) if mal and mp is not None else '', 'källans_köpbara_finns_i_målet': '', 'källans_köpbara': len(kopbara(sp))})
    os.makedirs(UT_RAPP, exist_ok=True)
    fil = os.path.join(UT_RAPP, 'mal-tabell-2026-11-17.csv')
    with open(fil, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rader[0].keys()))
        w.writeheader()
        w.writerows(rader)
    print('Skrev', os.path.relpath(fil, REPO))
    for r in rader:
        print(f"{r['beslut'][:24]:24} {r['källa']:36} -> {r['mål']:28} källa {r['källa_visningar']!s:>8} mål {r['mål_visningar']!s:>8} köpbara mål {r['mål_köpbara']!s:>3} undermängd {r['källans_köpbara_finns_i_målet']}")


def pris(k, namn):
    ut = {}
    for kalla, mal, *_ in KOR:
        c = hamta(k, kalla)
        for p in produkter(k, c['id']):
            ut[p['handle']] = {'tagg_prisjobb': PRIS_TAGG in p['tags'], 'varianter': [[x['id'], x['price'], x['compareAtPrice']] for x in p['variants']['nodes']]}
    fil = os.path.join(UT_ORIG, f'pris_{namn}.json')
    os.makedirs(UT_ORIG, exist_ok=True)
    json.dump(ut, open(fil, 'w'), ensure_ascii=False, indent=1, sort_keys=True)
    print('Prisögonblicksbild:', len(ut), 'produkter,', sum(1 for v in ut.values() if v['tagg_prisjobb']), 'med prisjobb-taggen (rörs inte) ->', os.path.relpath(fil, REPO))


def pris_jamfor(a, b):
    fa, fb = json.load(open(os.path.join(UT_ORIG, f'pris_{a}.json'))), json.load(open(os.path.join(UT_ORIG, f'pris_{b}.json')))
    skillnad = [h for h in fa if fa[h] != fb.get(h)] + [h for h in fb if h not in fa]
    print('Produkter före/efter:', len(fa), len(fb), '| skillnader:', len(skillnad), skillnad[:10])
    return 0 if not skillnad else 1


if __name__ == '__main__':
    k = ShopifyKlient()
    try:
        cmd = sys.argv[1]
        if cmd == 'backup':
            backup(k)
        elif cmd == 'tabell':
            tabell(k)
        elif cmd == 'pris':
            pris(k, sys.argv[2])
        elif cmd == 'pris-jamfor':
            sys.exit(pris_jamfor(sys.argv[2], sys.argv[3]))
        else:
            print(__doc__)
    except Exception as e:  # maskera alltid
        print('FEL:', maska(e))
        sys.exit(2)
