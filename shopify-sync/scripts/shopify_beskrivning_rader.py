#!/usr/bin/env python3
"""Ändring av enstaka rader i produktbeskrivningen via Admin API (ändrar BARA descriptionHtml).

Indata: JSON-lista med id, nr, rader [{gammal, ny}], html_ny (t.ex. f2_indata_forslag_indata_skriv.json).
Varje produkt klassas live omedelbart före skrivning:
  skriv     live-HTML innehåller varje gammal rad exakt en gång och blir exakt html_ny efter ersättning -> skrivs
  klar      live-HTML == html_ny                                                                      -> redan gjord, hoppas över
  avviker   något annat, spärrad produkt, taggen price-change-job-active, eller finns inte               -> hoppas över och rapporteras
Lägen:
  --dry-run   läser och visar vad som skulle ändras; skriver inget i Shopify
  --kanarie   skriver de 3 första "skriv", läser tillbaka och jämför
  --rest      skriver övriga "skriv" i delar om 4, läser tillbaka och jämför efter varje del
Före varje skrivning läses varje variants pris och jämförpris; efter skrivning ska de vara oförändrade, liksom titel, handle,
status, taggar och SEO. Stopp vid första avvikelse (kod 1). Före-fil och resultatfil sparas i --ut.
Användning: shopify_beskrivning_rader.py INFIL (--dry-run | --kanarie | --rest) [--ut KATALOG] [--profil BUTIKSPROFIL.json]
"""
import datetime, json, os, sys

HAR = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.abspath(os.path.join(HAR, '..', '..'))
sys.path.insert(0, HAR)
import shopify_api as api  # noqa: E402
import butiksprofil  # noqa: E402
from skrivfil_kontroll import las_sparr  # noqa: E402

KANARIE_ANTAL = 3
DEL = 4
SKYDDSTAGG = 'price-change-job-active'
PRISFRAGA = 'query($ids:[ID!]!){nodes(ids:$ids){... on Product{id variants(first:100){nodes{id price compareAtPrice}}}}}'


def ersatt(html, rader):
    """Ren funktion. Returnerar ny HTML, eller None om någon rad inte finns exakt en gång."""
    for r in rader:
        if html.count(r['gammal']) != 1:
            return None
        html = html.replace(r['gammal'], r['ny'])
    return html


def klassa(poster, live, sparr):
    """Ren funktion (testbar utan nätverk). Returnerar (skriv, klar, avviker)."""
    skriv, klar, avviker = [], [], []
    for w, l in zip(poster, live):
        i = api.sifferid(w['id'])
        if i in sparr:
            avviker.append((w, f'spärrad ({sparr[i][0]})')); continue
        if l is None:
            avviker.append((w, 'finns inte i butiken')); continue
        if SKYDDSTAGG in (l.get('tags') or []):
            avviker.append((w, f'taggen {SKYDDSTAGG} (rörs inte)')); continue
        if not w.get('rader') or any(r['gammal'] == r['ny'] for r in w['rader']):
            avviker.append((w, 'ingen ändring i indata')); continue
        html = l.get('descriptionHtml') or ''
        if html == w['html_ny']:
            klar.append(w); continue
        ny = ersatt(html, w['rader'])
        if ny is None:
            avviker.append((w, 'live-texten avviker: någon gammal rad finns inte exakt en gång')); continue
        if ny != w['html_ny']:
            avviker.append((w, 'live-texten avviker från skrivfilen utanför de ändrade raderna')); continue
        skriv.append(w)
    return skriv, klar, avviker


def hamta_priser(klient, ids):
    """{siffer-id: [(variant-id, price, compareAtPrice), ...]} i stabil ordning."""
    ut = {}
    ids = [api.gid(i) for i in ids]
    for s in range(0, len(ids), 10):
        for n in klient.graphql(PRISFRAGA, {'ids': ids[s:s + 10]})['nodes']:
            if n:
                ut[api.sifferid(n['id'])] = sorted((v['id'], v['price'], v['compareAtPrice']) for v in n['variants']['nodes'])
    return ut


def uppdatera_beskrivning(klient, produkt_id, html):
    """productUpdate med bara descriptionHtml (seo, taggar, status m.m. skickas inte)."""
    q = 'mutation($p:ProductUpdateInput!){productUpdate(product:$p){product{id} userErrors{field message}}}'
    d = klient.graphql(q, {'p': {'id': api.gid(produkt_id), 'descriptionHtml': html}})
    fel = d['productUpdate']['userErrors']
    if fel:
        raise api.ShopifyFel('userErrors: ' + json.dumps(fel, ensure_ascii=False))
    return d['productUpdate']['product']['id']


def jamfor_beskrivning(fore, efter, html_ny, priser_fore, priser_efter):
    """Endast descriptionHtml får ha ändrats, och den ska vara exakt html_ny. Priser oförändrade."""
    fel = []
    for k in ('title', 'handle', 'status'):
        if fore.get(k) != efter.get(k):
            fel.append(f'{k} ändrad')
    if sorted(fore.get('tags') or []) != sorted(efter.get('tags') or []):
        fel.append('tags ändrade')
    if fore.get('seo') != efter.get('seo'):
        fel.append('seo ändrad')
    if efter.get('descriptionHtml') != html_ny:
        a, b = efter.get('descriptionHtml') or '', html_ny
        p = next((n for n, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
        fel.append(f'descriptionHtml avviker vid tecken {p}: live {len(a)} tecken, förväntat {len(b)} tecken')
    if priser_fore != priser_efter:
        fel.append('PRISER ÄNDRADE')
    return fel


def skriv_och_verifiera(klient, poster, fore_per_id, priser_fore):
    resultat = []
    for w in poster:
        uppdatera_beskrivning(klient, w['id'], w['html_ny'])
    efter = api.hamta_produkter(klient, [w['id'] for w in poster])
    priser_efter = hamta_priser(klient, [w['id'] for w in poster])
    for w, e in zip(poster, efter):
        i = api.sifferid(w['id'])
        resultat.append((w['id'], jamfor_beskrivning(fore_per_id[i], e, w['html_ny'], priser_fore.get(i), priser_efter.get(i))))
    return resultat


def main(argv=None):
    profil, a = butiksprofil.profil_fran_argv(argv if argv is not None else sys.argv[1:])
    lage = next((x for x in ('--dry-run', '--kanarie', '--rest') if x in a), None)
    ut = os.path.join(ROT, 'rapporter', f'shopify-original-{datetime.date.today().isoformat()}')
    if '--ut' in a:
        k = a.index('--ut'); ut = a[k + 1]; del a[k:k + 2]
    filer = [x for x in a if not x.startswith('--')]
    if not lage or len(filer) != 1:
        print(__doc__); return 2
    poster = json.load(open(filer[0], encoding='utf-8'))
    namn = os.path.splitext(os.path.basename(filer[0]))[0]
    sparr = las_sparr(butiksprofil.i_rot(profil, 'sparrlista'))

    klient = api.klient_fran_profil(profil)
    print('Butik:', api.verifiera_butik(klient))
    ids = [w['id'] for w in poster]
    live = api.hamta_produkter(klient, ids)
    fel = api.kontrollera_fore([l for l in live if l], [i for i, l in zip(ids, live) if l])
    if fel:
        print('Före-läget är ofullständigt:', *fel[:5], sep='\n  '); return 1
    skriv, klar, avviker = klassa(poster, live, sparr)
    fore_per_id = {api.sifferid(l['id']): l for l in live if l}
    print(f'{len(poster)} produkter: {len(skriv)} att skriva, {len(klar)} redan klara, {len(avviker)} avvikande (hoppas över)')
    for w, skal in avviker:
        print(f'  HOPPAS ÖVER {w["id"]} ({w.get("nr")}): {skal}')

    valda = skriv if lage != '--kanarie' else skriv[:KANARIE_ANTAL]
    fore_fil = os.path.join(ut, f'{namn}_fore_{lage.strip("-")}.json')
    api.spara_fore([fore_per_id[api.sifferid(w['id'])] for w in valda], fore_fil)
    priser_fore = hamta_priser(klient, [w['id'] for w in valda]) if valda else {}
    print('Före-fil:', os.path.relpath(fore_fil, ROT), f'({len(valda)} produkter)')

    if lage == '--dry-run':
        for w in valda:
            for r in w['rader']:
                print(f'  SKULLE ÄNDRA {w["id"]} ({w.get("nr")}): "{r["gammal"]}" -> "{r["ny"]}"')
        return 0

    verifierade, avvikelser = [], []
    for s in range(0, len(valda), DEL):
        for pid, fe in skriv_och_verifiera(klient, valda[s:s + DEL], fore_per_id, priser_fore):
            (avvikelser if fe else verifierade).append((pid, fe))
        if avvikelser:
            break
    res = {'lage': lage, 'datum': datetime.datetime.now().isoformat(timespec='seconds'),
           'skrivna_och_verifierade': [p for p, _ in verifierade], 'avvikelser': [{'id': p, 'fel': f} for p, f in avvikelser],
           'redan_klara': [w['id'] for w in klar], 'hoppade_over': [{'id': w['id'], 'skal': s} for w, s in avviker],
           'anrop': klient.antal_anrop}
    res_fil = os.path.join(ut, f'{namn}_resultat_{lage.strip("-")}.json')
    json.dump(res, open(res_fil, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'Skrivna och verifierade: {len(verifierade)} av {len(valda)}. Resultat: {os.path.relpath(res_fil, ROT)}')
    if avvikelser:
        for p, f in avvikelser:
            print(f'  AVVIKELSE {p}: {"; ".join(f)}')
        print('STOPP vid första avvikelse.'); return 1
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (api.ShopifyFel, butiksprofil.ProfilFel) as e:
        print('FEL:', api.maska(e)); sys.exit(1)
