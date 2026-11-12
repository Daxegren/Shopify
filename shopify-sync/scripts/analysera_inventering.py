#!/usr/bin/env python3
"""Analyserar en inventering (alla_produkter.json från inventera_bos.py) mot spärrlistan och batchfilerna. BARA LÄSNING av repots filer.

Skriver siffror.json, aktiva_utan_text.csv och luckor_skrivna.csv i inventeringskatalogen (skrivs aldrig över).
Grupper för aktiva produkter utan texter-klara (första träffen gäller):
  A/B/C  aktiv spärr (utanför tills vidare / titeldubblett / tidigare avvisad), efter undantagsfilen
  D      avvisad i någon batch (*_avvisade.json) men inte i spärrlistan; skälet sorteras på ord (ungefärligt)
  F      aldrig bearbetad (id finns i ingen batchfil)
Användning: analysera_inventering.py INVENTERINGSKATALOG [--jamfor ANNAN_INVENTERING.json]
"""
import collections, csv, glob, json, os, re, sys

HAR = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.abspath(os.path.join(HAR, '..', '..'))
SKRIV = os.path.join(ROT, 'rapporter', 'facit-bos-2026-10-31', 'vag2_skriv')
sid = lambda x: re.sub(r'\D', '', str(x))
RISK = r'hjälm|lås|belysning|lampa|broms|däck|kedja|pakethållare|trampolin|stödben|korg|barn|junior|kids|kosttillskott|massage|akupressur|vibrations|rullskridsk'
KATEGORIER = {'isbroddar': r'isbrodd', 'rullskridskor': r'rullskridsk', 'akupressur': r'akupressur', 'vibrationsplattor': r'vibrationsplatt',
              'kroppsanalysvågar': r'kroppsanalys|analysvåg|kroppsvåg|bioimpedans', 'massagestolar': r'massagestol',
              'barn (brett nyckelord)': r'\bbarn|junior|\bkids|bebis|baby', 'kosttillskott': r'kosttillskott|melatonin|protein'}
SKAL = [('dubblett', 'dubblett|samma artikel|exakt samma'), ('olika pris/artiklar', 'olika pris|olika artikl|varianter|blandar|olika vikt|olika modell|olika storlek'),
        ('barn', 'barn|junior'), ('massage/akupressur/rehab', 'massage|akupressur|rehab|knästöd|nackdrag'),
        ('kosttillskott', 'kosttillskott|melatonin|protein|kapslar|vitamin'),
        ('säkerhetsprodukt', 'säkerhet|broms|hjälm|lås|belysning|däck|kedja|bärande|lastgräns|stödben|korg|pakethållare|trampolin'),
        ('tunn/tom/motsägande källa', 'tunn|tom källa|motsäg|saknar källa|källa saknas|ingen källa|oklar'), ('elektronik', 'elektronik|batteri|laddare|display')]


def kat(skal):
    s = skal.lower()
    return next((k for k, pat in SKAL if re.search(pat, s)), 'övrigt')


def lasa_spar(cfg):
    mangd, und = {}, set()
    for s in cfg['sparrar']:
        ids = {sid(r[s['idkolumn']]) for r in csv.DictReader(open(os.path.join(ROT, s['idfil']), encoding='utf-8'))}
        if s.get('typ') == 'undantag':
            if s['aktiv']: und |= ids
        elif s['aktiv']:
            mangd[s['namn']] = ids
    return mangd, und


def batchfiler():
    bearbetade, avvisade = set(), {}
    for f in glob.glob(os.path.join(SKRIV, '*.json')):
        try: d = json.load(open(f, encoding='utf-8'))
        except Exception: continue
        if not isinstance(d, list): continue
        for x in d:
            if isinstance(x, dict) and 'id' in x:
                i = sid(x['id']); bearbetade.add(i)
                if 'avvisade' in os.path.basename(f): avvisade[i] = x.get('skäl') or x.get('skal') or ''
    return bearbetade, avvisade


def main(a):
    if not a: print(__doc__); return 2
    kat_dir = a[0]; gammal = None
    if '--jamfor' in a: gammal = a[a.index('--jamfor') + 1]
    P = json.load(open(os.path.join(kat_dir, 'alla_produkter.json'), encoding='utf-8'))
    N = {sid(p['id']): p for p in P}
    klar = lambda p: 'texter-klara' in p['tags']
    txt = lambda p: (p['title'] + ' ' + (p['productType'] or '') + ' ' + ' '.join(p['tags'])).lower()
    S = {'totalt': len(P)}
    S['status'] = {s: {'totalt': sum(p['status'] == s for p in P), 'med_klara': sum(p['status'] == s and klar(p) for p in P),
                       'utan_klara': sum(p['status'] == s and not klar(p) for p in P)} for s in ('ACTIVE', 'DRAFT', 'ARCHIVED')}
    if gammal:
        O = {sid(p['id']): p for p in json.load(open(gammal, encoding='utf-8'))}
        S['jamfort_med'] = gammal
        S['nya_id'] = len(set(N) - set(O)); S['borta_id'] = len(set(O) - set(N))
        S['statusbyten'] = {f'{O[i]["status"]}>{N[i]["status"]}': 0 for i in N if i in O and O[i]['status'] != N[i]['status']}
        for i in N:
            if i in O and O[i]['status'] != N[i]['status']: S['statusbyten'][f'{O[i]["status"]}>{N[i]["status"]}'] += 1
    cfg = json.load(open(os.path.join(ROT, 'shopify-sync', 'config', 'sparrlista.json'), encoding='utf-8'))
    mangd, und = lasa_spar(cfg)
    eff = {k: v - und for k, v in mangd.items()}
    S['sparrar'] = {k: {'rå': len(mangd[k]), 'efter_undantag': len(eff[k]), 'status': dict(collections.Counter(N[i]['status'] for i in eff[k] if i in N)),
                        'med_klara': sum(klar(N[i]) for i in eff[k] if i in N)} for k in mangd}
    S['undantag_unika_id'] = len(und)
    bearbetade, avvisade = batchfiler()
    S['batchfiler'] = {'bearbetade_id': len(bearbetade), 'avvisade_id': len(avvisade)}
    ordning = ['pilot-20', 'utanfor-tills-vidare-2026-11-04', 'titeldubbletter-2026-11-04', 'tidigare-avvisade-2026-11-04']
    namn = {'utanfor-tills-vidare-2026-11-04': 'A spärr: utanför tills vidare', 'titeldubbletter-2026-11-04': 'B spärr: titeldubblett', 'tidigare-avvisade-2026-11-04': 'C spärr: tidigare avvisad'}
    klT = {p['title'].strip().lower() for p in P if p['status'] == 'ACTIVE' and klar(p)}
    rader, grp = [], collections.Counter()
    for p in P:
        if p['status'] != 'ACTIVE' or klar(p): continue
        i = sid(p['id']); g = next((namn[k] for k in ordning[1:] if i in eff[k]), None)
        if g: undergrupp = ''
        elif i in avvisade: g, undergrupp = 'D avvisad i batch (ej i spärrlistan)', kat(avvisade[i])
        elif i not in bearbetade:
            g = 'F aldrig bearbetad'
            lager = (p['totalInventory'] or 0) > 0
            undergrupp = ('titel lika med redan skriven aktiv produkt' if p['title'].strip().lower() in klT else
                          'riskord i titel/typ' if re.search(RISK, (p['title'] + ' ' + (p['productType'] or '')).lower()) else
                          'lager 0' if not lager else 'kandidat för ny omgång')
        else: g, undergrupp = 'E bearbetad men inte klar', ''
        grp[(g, undergrupp)] += 1
        rader.append([i, p['title'], p['productType'], p['totalInventory'], 'ja' if 'På beställning' in p['tags'] else '', g, undergrupp, (avvisade.get(i) or '')[:160]])
    S['aktiva_utan_klara'] = {'totalt': len(rader), 'grupper': {f'{g} / {u}' if u else g: n for (g, u), n in sorted(grp.items())}}
    S['kategorier_nyckelord'] = {}
    for k, pat in KATEGORIER.items():
        m = [p for p in P if re.search(pat, txt(p))]
        S['kategorier_nyckelord'][k] = {'alla': len(m), 'status': dict(collections.Counter(p['status'] for p in m)),
                                        'aktiva_med_klara': sum(p['status'] == 'ACTIVE' and klar(p) for p in m), 'aktiva_utan_klara': sum(p['status'] == 'ACTIVE' and not klar(p) for p in m)}
    ca = collections.Counter(p['title'].strip().lower() for p in P if p['status'] == 'ACTIVE'); call = collections.Counter(p['title'].strip().lower() for p in P)
    dd = [p for p in P if p['status'] == 'ACTIVE' and ca[p['title'].strip().lower()] > 1]
    S['titeldubbletter'] = {'alla_grupper': sum(n > 1 for n in call.values()), 'alla_produkter': sum(n for n in call.values() if n > 1),
                            'aktiva_grupper': sum(n > 1 for n in ca.values()), 'aktiva_produkter': len(dd), 'aktiva_med_klara': sum(klar(p) for p in dd), 'aktiva_utan_klara': sum(not klar(p) for p in dd)}
    def luckor(q):
        m = lambda f: sum(1 for p in q if f(p))
        return {'n': len(q), 'meta_saknas': m(lambda p: not (p['seo_description'] or '').strip()), 'meta_under_70': m(lambda p: 0 < len(p['seo_description'] or '') < 70),
                'meta_over_155': m(lambda p: len(p['seo_description'] or '') > 155), 'seo_titel_ej_satt_titeln_anvands': m(lambda p: not p['seo_title']),
                'seo_titel_over_60_tecken': m(lambda p: len(p['seo_title'] or '') > 60), 'titel_over_70': m(lambda p: len(p['title']) > 70),
                'standardblock_saknas': m(lambda p: not p['har_standardblock']), 'beskrivning_under_50_tecken': m(lambda p: p['html_tecken'] < 50),
                'pa_bestallning_utan_leveranstidsmening': m(lambda p: 'På beställning' in p['tags'] and not p['har_leveranstidsmening']),
                'leveranstidsmening_utan_tagg': m(lambda p: p['har_leveranstidsmening'] and 'På beställning' not in p['tags'])}
    S['luckor'] = {'aktiva_med_klara': luckor([p for p in P if p['status'] == 'ACTIVE' and klar(p)]),
                   'aktiva_utan_klara': luckor([p for p in P if p['status'] == 'ACTIVE' and not klar(p)]), 'alla': luckor(P)}
    luck = []
    for p in P:
        if not klar(p): continue
        f = [t for t, c in (('meta saknas', not (p['seo_description'] or '').strip()), ('meta under 70 tecken', 0 < len(p['seo_description'] or '') < 70),
                            ('meta över 155 tecken', len(p['seo_description'] or '') > 155), ('seo-titel över 60 tecken', len(p['seo_title'] or '') > 60),
                            ('På beställning utan leveranstidsmening', 'På beställning' in p['tags'] and not p['har_leveranstidsmening'])) if c]
        if f: luck.append([sid(p['id']), p['title'], p['status'], '; '.join(f)])
    S['luckor_skrivna_produkter'] = len(luck)
    for nm, hdr, rr in (('aktiva_utan_text.csv', ['produkt_id', 'titel', 'produkttyp', 'lager', 'pa_bestallning', 'grupp', 'undergrupp', 'avvisningsskal'], rader),
                        ('luckor_skrivna.csv', ['produkt_id', 'titel', 'status', 'lucka'], luck)):
        with open(os.path.join(kat_dir, nm), 'x', encoding='utf-8', newline='') as f:
            w = csv.writer(f); w.writerow(hdr); w.writerows(rr)
    json.dump(S, open(os.path.join(kat_dir, 'siffror.json'), 'x', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(S, ensure_ascii=False, indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
