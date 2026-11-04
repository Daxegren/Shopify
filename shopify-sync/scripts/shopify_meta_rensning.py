#!/usr/bin/env python3
"""Rensning av metabeskrivningar via Admin API (ändrar BARA seo.description).

Indata: JSON-lista med id, seo_title, meta_gammal, meta_ny (t.ex. meta_rensning.json).
Varje produkt klassas före skrivning mot live:
  skriv     live seo.description == meta_gammal och seo.title oförändrad  -> skrivs
  klar      live seo.description == meta_ny                               -> redan gjord, hoppas över
  avviker   något annat (eller spärrad produkt)                           -> hoppas över och rapporteras
Lägen:
  --dry-run   läser och visar vad som skulle ändras; skriver inget i Shopify
  --kanarie   skriver de 3 första "skriv", läser tillbaka och jämför
  --rest      skriver övriga "skriv" i delar om 4, läser tillbaka och jämför efter varje del
Stopp vid första avvikelse (kod 1). Före-fil och resultatfil sparas i --ut (standard rapporter/shopify-original-<datum>/).
Användning: shopify_meta_rensning.py INFIL (--dry-run | --kanarie | --rest) [--ut KATALOG]
"""
import datetime, json, os, sys

HAR = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.abspath(os.path.join(HAR, '..', '..'))
sys.path.insert(0, HAR)
import shopify_api as api  # noqa: E402
from skrivfil_kontroll import las_sparr  # noqa: E402

KANARIE_ANTAL = 3
DEL = 4


def klassa(poster, live, sparr):
    """Ren funktion (testbar utan nätverk). Returnerar (skriv, klar, avviker)."""
    skriv, klar, avviker = [], [], []
    for w, l in zip(poster, live):
        i = api.sifferid(w['id'])
        if i in sparr:
            avviker.append((w, f'spärrad ({sparr[i][0]})')); continue
        if l is None:
            avviker.append((w, 'finns inte i butiken')); continue
        if w['meta_gammal'] == w['meta_ny']:
            avviker.append((w, 'meta_gammal == meta_ny (ingenting att göra)')); continue
        ml = (l.get('seo') or {}).get('description')
        if ml == w['meta_ny']:
            klar.append(w); continue
        if ml != w['meta_gammal']:
            avviker.append((w, f'live-metan avviker från meta_gammal ({len(ml or "")} tecken)')); continue
        if api.effektiv_seo_title(l) != w['seo_title']:
            avviker.append((w, 'seo.title avviker från skrivfilen')); continue
        skriv.append(w)
    return skriv, klar, avviker


def skriv_och_verifiera(klient, poster, fore_per_id):
    """Skriver en del, läser tillbaka och jämför. Returnerar lista med (id, avvikelser)."""
    resultat = []
    for w in poster:
        api.uppdatera_seo(klient, w['id'], w['seo_title'], w['meta_ny'])
    efter = api.hamta_produkter(klient, [w['id'] for w in poster])
    for w, e in zip(poster, efter):
        f = fore_per_id[api.sifferid(w['id'])]
        resultat.append((w['id'], api.jamfor_efter(f, e, w['meta_ny'], w['seo_title'])))
    return resultat


def main(argv=None):
    a = list(argv if argv is not None else sys.argv[1:])
    lage = next((x for x in ('--dry-run', '--kanarie', '--rest') if x in a), None)
    ut = os.path.join(ROT, 'rapporter', f'shopify-original-{datetime.date.today().isoformat()}')
    if '--ut' in a:
        k = a.index('--ut'); ut = a[k + 1]; del a[k:k + 2]
    filer = [x for x in a if not x.startswith('--')]
    if not lage or len(filer) != 1:
        print(__doc__); return 2
    poster = json.load(open(filer[0], encoding='utf-8'))
    namn = os.path.splitext(os.path.basename(filer[0]))[0]
    sparr = las_sparr(os.path.join(ROT, 'shopify-sync/config/sparrlista.json'))

    klient = api.ShopifyKlient()
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

    valda = skriv if lage == '--dry-run' else skriv[:KANARIE_ANTAL] if lage == '--kanarie' else skriv
    # före-fil: komplett läge för det som körs (skrivs aldrig över)
    fore_fil = os.path.join(ut, f'{namn}_fore_{lage.strip("-")}.json')
    api.spara_fore([fore_per_id[api.sifferid(w['id'])] for w in valda] if valda else [], fore_fil)
    print('Före-fil:', os.path.relpath(fore_fil, ROT), f'({len(valda)} produkter)')

    if lage == '--dry-run':
        for w in valda:
            print(f'  SKULLE ÄNDRA {w["id"]} ({w.get("nr")}): "{w["meta_gammal"][-45:]}" -> "{w["meta_ny"][-45:]}" ({len(w["meta_gammal"])} -> {len(w["meta_ny"])} tecken)')
        return 0

    verifierade, avvikelser = [], []
    for s in range(0, len(valda), DEL):
        for pid, fe in skriv_och_verifiera(klient, valda[s:s + DEL], fore_per_id):
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
    except api.ShopifyFel as e:
        print('FEL:', api.maska(e)); sys.exit(1)
