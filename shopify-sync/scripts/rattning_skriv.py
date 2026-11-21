#!/usr/bin/env python3
"""Rättning av SEO-titel, metabeskrivning och beskrivning på redan skrivna produkter via Admin API.

Indata: JSON-lista med id, fore_seo_title, fore_meta, fore_html, seo_title_ny, meta_ny, html_ny.
Varje produkt klassas mot live före skrivning:
  skriv     live == fore (SEO-titel, meta, beskrivning), inte spärrad, saknar taggen price-change-job-active
  klar      live == ny                          -> hoppas över
  avviker   något annat                         -> hoppas över och rapporteras
Lägen: --dry-run (skriver inget), --kanarie (3 första), --rest (övriga, delar om 4).
Skriver bara seo{title description} (alltid båda) och descriptionHtml. Efter varje del återläses allt:
title, handle, status, tags, priser och compareAtPrice ska vara OFÖRÄNDRADE, och SEO/beskrivning ska vara lika med ny text tecken för tecken.
Stopp vid första avvikelse (kod 1). Före- och resultatfil sparas i --ut (skrivs aldrig över).
Användning: rattning_skriv.py INFIL (--dry-run | --kanarie | --rest) --ut KATALOG [--profil BUTIKSPROFIL.json]
"""
import datetime, json, os, re, sys

HAR = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.abspath(os.path.join(HAR, '..', '..'))
sys.path.insert(0, HAR)
import shopify_api as api  # noqa: E402
import butiksprofil  # noqa: E402
from skrivfil_kontroll import las_sparr  # noqa: E402

LAS = 'price-change-job-active'
OSYNLIGA = re.compile('[­​‌‍⁠﻿]')
KANARIE, DEL = 3, 4
PRIS_Q = 'query($ids:[ID!]!){nodes(ids:$ids){... on Product{id variants(first:100){nodes{id price compareAtPrice}}}}}'
MUT = ('mutation($p:ProductUpdateInput!){productUpdate(product:$p){product{id} userErrors{field message}}}')


def priser(klient, ids):
    ut = {}
    for s in range(0, len(ids), 10):
        for n in klient.graphql(PRIS_Q, {'ids': [api.gid(i) for i in ids[s:s + 10]]})['nodes']:
            ut[api.sifferid(n['id'])] = sorted((v['id'], v['price'], v['compareAtPrice']) for v in n['variants']['nodes'])
    return ut


def klassa(w, live, sparr):
    """Ren funktion. Returnerar (klass, skäl)."""
    i = api.sifferid(w['id'])
    if i in sparr: return 'avviker', f'spärrad ({sparr[i][0]})'
    if live is None: return 'avviker', 'finns inte i butiken'
    if LAS in live['tags']: return 'avviker', f'har taggen {LAS}'
    if 'texter-klara' not in live['tags']: return 'avviker', 'saknar texter-klara'
    for k in ('seo_title_ny', 'meta_ny', 'html_ny'):
        if OSYNLIGA.search(w[k] or ''): return 'avviker', f'osynligt tecken i {k}'
    nu = (api.effektiv_seo_title(live), (live.get('seo') or {}).get('description') or '', live['descriptionHtml'])
    ny = (w['seo_title_ny'], w['meta_ny'], w['html_ny'])
    fore = (w['fore_seo_title'] or live['title'], w['fore_meta'] or '', w['fore_html'])
    if nu == ny: return 'klar', 'live är redan lika med ny text'
    if nu != fore: return 'avviker', 'live avviker från före-läget i indata'
    return 'skriv', 'live stämmer med före-läget'


def skriv(klient, w):
    seo_title = w['seo_title_ny']
    v = {'id': api.gid(w['id']), 'seo': {'title': seo_title, 'description': w['meta_ny']}}
    if w['html_ny'] != w['fore_html']:
        v['descriptionHtml'] = w['html_ny']
    fel = klient.graphql(MUT, {'p': v})['productUpdate']['userErrors']
    if fel: raise api.ShopifyFel('userErrors: ' + json.dumps(fel, ensure_ascii=False))


def kontrollera(w, fore, efter, pris_fore, pris_efter):
    fel = []
    for k in ('title', 'handle', 'status'):
        if fore[k] != efter[k]: fel.append(f'{k} ändrad')
    if sorted(fore['tags']) != sorted(efter['tags']): fel.append('tags ändrade')
    if pris_fore != pris_efter: fel.append('pris eller jämförpris ändrat')
    if api.effektiv_seo_title(efter) != w['seo_title_ny']: fel.append('seo.title avviker från ny text')
    if ((efter.get('seo') or {}).get('description') or '') != w['meta_ny']: fel.append('seo.description avviker från ny text')
    if efter['descriptionHtml'] != w['html_ny']: fel.append('descriptionHtml avviker från ny text')
    return fel


def main(argv=None):
    profil, a = butiksprofil.profil_fran_argv(argv if argv is not None else sys.argv[1:])
    lage = next((x for x in ('--dry-run', '--kanarie', '--rest') if x in a), None)
    ut = None
    if '--ut' in a:
        k = a.index('--ut'); ut = a[k + 1]; del a[k:k + 2]
    filer = [x for x in a if not x.startswith('--')]
    if not lage or not ut or len(filer) != 1:
        print(__doc__); return 2
    poster = json.load(open(filer[0], encoding='utf-8'))
    namn = os.path.splitext(os.path.basename(filer[0]))[0]
    sparr = las_sparr(butiksprofil.i_rot(profil, 'sparrlista'))
    klient = api.klient_fran_profil(profil)
    print('Butik:', api.verifiera_butik(klient))
    ids = [w['id'] for w in poster]
    live = api.hamta_produkter(klient, ids)
    pris = priser(klient, ids)
    skriv_lista, klara, avviker = [], [], []
    for w, l in zip(poster, live):
        kl, skal = klassa(w, l, sparr)
        {'skriv': skriv_lista, 'klar': klara}.get(kl, avviker).append((w, skal) if kl == 'avviker' else w)
    print(f'{len(poster)} produkter: {len(skriv_lista)} att skriva, {len(klara)} redan klara, {len(avviker)} hoppas över')
    for w, skal in avviker: print(f'  HOPPAS ÖVER {w["id"]}: {skal}')
    valda = skriv_lista if lage in ('--dry-run', '--rest') else skriv_lista[:KANARIE]
    fore_per_id = {api.sifferid(l['id']): l for l in live if l}
    api.spara_fore([fore_per_id[api.sifferid(w['id'])] for w in valda], os.path.join(ut, f'{namn}_fore_{lage.strip("-")}.json'))
    if lage == '--dry-run':
        for w in valda:
            print(f'  SKULLE ÄNDRA {w["id"]}: meta {len(w["fore_meta"] or "")}->{len(w["meta_ny"])}, seo {len(w["fore_seo_title"] or "")}->{len(w["seo_title_ny"])}, html {len(w["fore_html"])}->{len(w["html_ny"])} tecken')
        return 0
    verifierade, avvikelser = [], []
    for s in range(0, len(valda), DEL):
        del_ = valda[s:s + DEL]
        for w in del_: skriv(klient, w)
        efter = api.hamta_produkter(klient, [w['id'] for w in del_])
        pe = priser(klient, [w['id'] for w in del_])
        for w, e in zip(del_, efter):
            i = api.sifferid(w['id'])
            fe = kontrollera(w, fore_per_id[i], e, pris[i], pe[i])
            (avvikelser if fe else verifierade).append((w['id'], fe))
        if avvikelser: break
    res = {'lage': lage, 'datum': datetime.datetime.now().isoformat(timespec='seconds'), 'skrivna_och_verifierade': [p for p, _ in verifierade],
           'avvikelser': [{'id': p, 'fel': f} for p, f in avvikelser], 'redan_klara': [w['id'] for w in klara],
           'hoppade_over': [{'id': w['id'], 'skal': s} for w, s in avviker], 'anrop': klient.antal_anrop}
    rf = os.path.join(ut, f'{namn}_resultat_{lage.strip("-")}.json')
    json.dump(res, open(rf, 'x', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'Skrivna och verifierade: {len(verifierade)} av {len(valda)}. Resultat: {os.path.relpath(rf, ROT)}')
    for p, f in avvikelser: print(f'  AVVIKELSE {p}: {"; ".join(f)}')
    if avvikelser: print('STOPP vid första avvikelse.'); return 1
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (api.ShopifyFel, butiksprofil.ProfilFel) as e:
        print('FEL:', api.maska(e)); sys.exit(1)
