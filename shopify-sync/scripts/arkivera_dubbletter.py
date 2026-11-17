#!/usr/bin/env python3
"""Hittar och arkiverar dubbletter i BEST OF SPORTS (ändrar BARA status till ARCHIVED).

En aktiv produkt utan taggen texter-klara (kandidat) är en dubblett om en aktiv, redan skriven produkt (behållare)
har ett gemensamt artikelnummer (SKU) och samma normaliserade titel-kärna. Kandidaten arkiveras bara om:
  - behållaren har texter-klara och är ACTIVE
  - behållaren har minst lika många bilder som kandidaten (Davids villkor: den som sparas har all info och alla bilder)
  - kandidatens artikelnummer är en delmängd av behållarens
  - kandidaten har inget lager (totalInventory == 0) eller högst lika mycket som... (annars hoppas den över)
  - kandidaten är inte pilotprodukt
Lägen: --dry-run (standard, skriver inget) och --kor (arkiverar, sparar före-fil, läser tillbaka).
Användning: arkivera_dubbletter.py [--dry-run | --kor] [--lista FIL] [--ut KATALOG] [--profil BUTIKSPROFIL.json]
Butik, miljövariabelnamn, klartagg och pilotlista läses ur butiksprofilen (standard: BEST OF SPORTS).
"""
import datetime, json, os, re, sys, csv

HAR = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.abspath(os.path.join(HAR, '..', '..'))
sys.path.insert(0, HAR)
import shopify_api as api  # noqa: E402
import butiksprofil  # noqa: E402

Q = '''query($c:String){products(first:100,after:$c,query:"status:active"){pageInfo{hasNextPage endCursor}
 nodes{id title handle createdAt tags status totalInventory mediaCount{count}
 variants(first:100){nodes{sku price}}}}}'''


def hamta_alla(klient):
    ut, c = [], None
    while True:
        d = klient.graphql(Q, {'c': c})['products']
        ut += d['nodes']
        if not d['pageInfo']['hasNextPage']:
            return ut
        c = d['pageInfo']['endCursor']


def norm(t):
    t = t.lower()
    t = re.sub(r'[^a-zåäö0-9]+', ' ', t)
    return ' '.join(w for w in t.split() if w not in ('cykel', 'tum'))


def skus(p):
    return {v['sku'] for v in p['variants']['nodes'] if v['sku']}


def hitta(produkter, pilot, klartagg='texter-klara'):
    klara = [p for p in produkter if klartagg in p['tags']]
    per_sku = {}
    for p in klara:
        for s in skus(p):
            per_sku.setdefault(s, []).append(p)
    ark, hoppar = [], []
    for p in produkter:
        if klartagg in p['tags'] or api.sifferid(p['id']) in pilot:
            continue
        ss = skus(p)
        if not ss:
            continue
        kand = {}
        for s in ss:
            for k in per_sku.get(s, []):
                kand[k['id']] = k
        for k in kand.values():
            if not ss <= skus(k):
                continue
            tc = set(norm(p['title']).split()) & set(norm(k['title']).split())
            if len(tc) < 3:
                continue
            skal = None
            if k['mediaCount']['count'] < p['mediaCount']['count']:
                skal = f'behållaren har färre bilder ({k["mediaCount"]["count"]} mot {p["mediaCount"]["count"]})'
            elif p['totalInventory'] and p['totalInventory'] > 0:
                skal = f'kandidaten har lager ({p["totalInventory"]} st)'
            (hoppar if skal else ark).append((p, k, skal))
            break
    return ark, hoppar


def main(argv=None):
    profil, a = butiksprofil.profil_fran_argv(argv if argv is not None else sys.argv[1:])
    kor = '--kor' in a
    ut = os.path.join(ROT, 'rapporter', f'shopify-original-{datetime.date.today().isoformat()}'
                      + ('' if profil['ar_standardprofil'] else '-' + butiksprofil.butiksslug(profil)))
    if '--ut' in a:
        i = a.index('--ut'); ut = a[i + 1]
    klient = api.klient_fran_profil(profil)
    print('Butik:', api.verifiera_butik(klient))
    pilotfil = butiksprofil.i_rot(profil, 'pilotlista')
    pilot = {r['produkt_id'] for r in csv.DictReader(open(pilotfil, encoding='utf-8'))} if pilotfil else set()
    produkter = hamta_alla(klient)
    ark, hoppar = hitta(produkter, pilot, profil['klartagg'])
    if '--lista' in a:  # begränsa till exakt de rader David godkänt
        gk = {(r['arkiveras'], r['behaller']) for r in json.load(open(a[a.index('--lista') + 1], encoding='utf-8'))}
        ark = [(p, k, s) for p, k, s in ark if (api.sifferid(p['id']), api.sifferid(k['id'])) in gk]
        if len(ark) != len(gk):
            print(f'STOPP: {len(ark)} av {len(gk)} godkända rader uppfyller villkoren nu'); return 1
    print(f'{len(produkter)} aktiva; {len(ark)} dubbletter att arkivera, {len(hoppar)} hoppas över')
    for p, k, s in hoppar:
        print(f'  HOPPAR {api.sifferid(p["id"])} -> {api.sifferid(k["id"])}: {s}')
    rader = [{'arkiveras': api.sifferid(p['id']), 'behaller': api.sifferid(k['id']), 'titel': p['title'][:60]} for p, k, _ in ark]
    os.makedirs(ut, exist_ok=True)
    json.dump(rader, open(os.path.join(ut, f'dubbletter_lista_{"kor" if kor else "dry"}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    if not kor:
        for r in rader[:200]:
            print(' ', r['arkiveras'], '->', r['behaller'], r['titel'])
        return 0
    ids = [r['arkiveras'] for r in rader] + [r['behaller'] for r in rader]
    fore = api.hamta_produkter(klient, ids)
    api.spara_fore(fore, os.path.join(ut, 'dubbletter3_fore.json'))
    fd = {api.sifferid(p['id']): p for p in fore}
    q = 'mutation($p:ProductUpdateInput!){productUpdate(product:$p){product{id status} userErrors{field message}}}'
    for s in range(0, len(rader), 4):
        del_ = rader[s:s + 4]
        for r in del_:
            d = klient.graphql(q, {'p': {'id': api.gid(r['arkiveras']), 'status': 'ARCHIVED'}})['productUpdate']
            if d['userErrors']:
                raise api.ShopifyFel(str(d['userErrors']))
        efter = api.hamta_produkter(klient, [r['arkiveras'] for r in del_] + [r['behaller'] for r in del_])
        for e in efter:
            i = api.sifferid(e['id']); f = fd[i]
            fel = [c for c in ('title', 'handle', 'descriptionHtml') if f[c] != e[c]] + (['tags'] if sorted(f['tags']) != sorted(e['tags']) else [])
            ok_status = e['status'] == ('ARCHIVED' if i in [r['arkiveras'] for r in del_] else 'ACTIVE')
            if fel or not ok_status:
                print('AVVIKELSE', i, fel, e['status']); return 1
    print(f'Arkiverade och verifierade: {len(rader)}')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (api.ShopifyFel, butiksprofil.ProfilFel) as e:
        print('FEL:', api.maska(e)); sys.exit(1)
