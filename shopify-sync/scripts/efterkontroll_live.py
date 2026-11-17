#!/usr/bin/env python3
"""Efterkontroll på live-texter (BARA LÄSNING). Läser alla produkter med klartaggen och kör regelkontrollerna i kvalitetsrapport.py.
Skriver CSV med product-id, status, regelbrott, om produkten bär skyddstaggen och om den redan åtgärdats av annan session.
Användning: efterkontroll_live.py UTKATALOG [--redan-atgardade FIL.json ...]  (filer med id-listor, t.ex. korrigeringsfiler)"""
import csv, json, os, re, sys, collections
HAR = os.path.dirname(os.path.abspath(__file__)); ROT = os.path.abspath(os.path.join(HAR, '..', '..'))
sys.path.insert(0, HAR)
import shopify_api as api, butiksprofil, kvalitetsrapport as kv  # noqa: E402
from skrivfil_kontroll import las_sparr  # noqa: E402

SKYDD = 'price-change-job-active'
Q = '''query($c:String){products(first:50,after:$c,query:"tag:texter-klara"){pageInfo{hasNextPage endCursor}
 nodes{id title status tags seo{title description} descriptionHtml}}}'''


def hamta_alla(k):
    ut, c = [], None
    while True:
        d = k.graphql(Q, {'c': c})['products']
        ut += d['nodes']
        if not d['pageInfo']['hasNextPage']:
            return ut
        c = d['pageInfo']['endCursor']


def main(a):
    ut = a[0]; os.makedirs(ut, exist_ok=True)
    redan = set()
    for f in a[a.index('--redan-atgardade') + 1:] if '--redan-atgardade' in a else []:
        for x in json.load(open(f, encoding='utf-8')):
            redan.add(api.sifferid(x.get('id') or x.get('produkt_id')))
    profil, _ = butiksprofil.profil_fran_argv([])
    k = api.klient_fran_profil(profil)
    print('Butik:', api.verifiera_butik(k))
    prod = hamta_alla(k)
    sparr = las_sparr(butiksprofil.i_rot(profil, 'sparrlista'))
    sparr = {i: [(str(v[0]), False)] for i, v in sparr.items()}
    profil = json.load(open(os.path.join(ROT, 'shopify-sync', 'config', 'butiksprofil-bestofsports.json'), encoding='utf-8'))  # rå profil (har gransvarden)
    kr = profil.get('kvalitetsrapport') or {}
    forb = kr.get('forbjudna_uttryck', kv.FORBJUDNA_STANDARD)
    tillatna = profil.get('marken_versaler_tillatna') or {}
    rader, titlar = [], collections.defaultdict(list)
    for p in prod:
        i = api.sifferid(p['id'])
        d = {'id': i, 'titel': p['title'], 'seo_title': (p['seo'] or {}).get('title') or '', 'meta': (p['seo'] or {}).get('description') or '', 'html': p['descriptionHtml'] or ''}
        titlar[p['title']].append((i, p['status']))
        for kod, fork in kv.kontrollera_produkt(d, profil, sparr, tillatna, forb, int(kr.get('max_enligt_tillverkaren', 2)), kr.get('attribution_fras', 'enligt tillverkaren')):
            rader.append((i, p['status'], p['title'], kod, fork, SKYDD in p['tags']))
    for t, lst in titlar.items():
        akt = [x for x in lst if x[1] == 'ACTIVE']
        if len(akt) > 1:
            for i, s in akt:
                rader.append((i, s, t, 'DUBBLETT_TITEL_AKTIV', f'delas av {len(akt)} aktiva', next(SKYDD in q['tags'] for q in prod if api.sifferid(q['id']) == i)))
    with open(os.path.join(ut, 'efterkontroll_live.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(['produkt_id', 'status', 'titel', 'regelbrott', 'forklaring', 'bar_price_change_job_active', 'redan_atgardad_av_annan'])
        for r in rader:
            w.writerow(list(r) + [r[0] in redan])
    c = collections.Counter(r[3] for r in rader)
    print(len(prod), 'produkter lästa;', len(rader), 'fynd'); print(dict(c))
    print('allvarliga (CIRKULAR/FORBJUDET/DUBBLETT_TITEL*):', {kk: (sum(1 for r in rader if r[3] == kk), sum(1 for r in rader if r[3] == kk and not r[5] and r[0] not in redan)) for kk in c if kk in ('CIRKULAR', 'FORBJUDET') or kk.startswith('DUBBLETT_TITEL')})


if __name__ == '__main__':
    main(sys.argv[1:])
