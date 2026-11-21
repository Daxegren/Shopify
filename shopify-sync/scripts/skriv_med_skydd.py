#!/usr/bin/env python3
"""Skriver en skrivfil via Admin API med extra skydd (David 2026-11-17). Skriver BARA title, seo och descriptionHtml samt taggen texter-klara.

Skydd utöver shopify_skriv_texter.py:
  - Produkter med taggen price-change-job-active hoppas över (klassas "avviker") och rörs aldrig. Taggen läses live före varje del;
    dyker den upp mellan klassning och skrivning, eller ändras en pris/jämförpris/status/handle/tagg, stoppas allt (kod 1).
  - Priser (varje variants price och compareAtPrice), lager (inventoryQuantity), status, handle och alla taggar läses före och efter varje del
    och måste vara oförändrade (taggen texter-klara undantagen, och bara efter verifierad text).
  - Före-fil (komplett, inklusive varianternas priser) sparas före skrivning; skrivs aldrig över.
Lägen: --dry-run (ingen skrivning), --kanarie (3 första), --rest (övriga, delar om högst 4). Efter varje del: återläsning och
jämförelse tecken för tecken. Stopp vid första avvikelse. Taggen texter-klara sätts sist och verifieras.
Användning: skriv_med_skydd.py SKRIVFIL (--dry-run | --kanarie | --rest) [--ut KATALOG] [--profil BUTIKSPROFIL.json]
Ångra: skriv tillbaka före-filen (title, seo, descriptionHtml) och ta bort texter-klara (se beslutsfilen).
"""
import datetime, json, os, sys

HAR = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.abspath(os.path.join(HAR, '..', '..'))
sys.path.insert(0, HAR)
import shopify_api as api  # noqa: E402
import butiksprofil  # noqa: E402
import shopify_skriv_texter as sk  # noqa: E402
from skrivfil_kontroll import las_sparr  # noqa: E402

SPARRTAGG = 'price-change-job-active'
DEL = 4
Q = '''query($ids:[ID!]!){nodes(ids:$ids){... on Product{id title handle status tags totalInventory updatedAt
 seo{title description} descriptionHtml
 variants(first:100){nodes{id sku price compareAtPrice inventoryQuantity}}}}}'''


class Stopp(Exception):
    pass


def las(klient, ids, n=10):
    ut = []
    for s in range(0, len(ids), n):
        ut.extend(klient.graphql(Q, {'ids': [api.gid(i) for i in ids[s:s + n]]})['nodes'])
    return ut


def prisbild(p):
    """Det som inte får ändras: varje variants id, pris, jämförpris och lagersaldo."""
    return sorted((v['id'], v['price'], v['compareAtPrice'], v['inventoryQuantity']) for v in p['variants']['nodes'])


def skyddsavvikelser(fore, efter, tagg_klar=False, klartagg='texter-klara'):
    fel = []
    if prisbild(fore) != prisbild(efter): fel.append('PRIS/JÄMFÖRPRIS/LAGER ändrat')
    if SPARRTAGG in (efter.get('tags') or []) and SPARRTAGG not in (fore.get('tags') or []): fel.append(f'taggen {SPARRTAGG} har tillkommit')
    if SPARRTAGG in (fore.get('tags') or []) and SPARRTAGG not in (efter.get('tags') or []): fel.append(f'taggen {SPARRTAGG} har försvunnit')
    for k in ('handle', 'status'):
        if fore.get(k) != efter.get(k): fel.append(f'{k} ändrad')
    return fel


def klassa_skydd(poster, live, sparr):
    skriv, klar, avviker = sk.klassa(poster, live, sparr)
    ok, extra = [], []
    for w in skriv:
        l = next(x for x in live if x and api.sifferid(x['id']) == api.sifferid(w['id']))
        (extra if SPARRTAGG in l['tags'] else ok).append(w)
    avviker += [(w, f'har taggen {SPARRTAGG} (rörs aldrig)') for w in extra]
    # redan lika texter men med prisjobbstaggen: inget ska göras alls
    rkl = []
    for w in klar:
        l = next(x for x in live if x and api.sifferid(x['id']) == api.sifferid(w['id']))
        (avviker.append((w, f'har taggen {SPARRTAGG} (rörs aldrig)')) if SPARRTAGG in l['tags'] else rkl.append(w))
    return ok, rkl, avviker


def kor_del(klient, del_poster, fore, klartagg):
    """Läser före-läget på nytt, skriver, återläser, jämför text och skydd; taggar först efter ren jämförelse; verifierar igen."""
    ids = [w['id'] for w in del_poster]
    nu = {api.sifferid(p['id']): p for p in las(klient, ids)}
    for w in del_poster:
        n, f = nu[api.sifferid(w['id'])], fore[api.sifferid(w['id'])]
        fel = skyddsavvikelser(f, n)
        if fel: raise Stopp(f'{w["id"]} före skrivning: ' + '; '.join(fel))
        if SPARRTAGG in n['tags']: raise Stopp(f'{w["id"]} har {SPARRTAGG} före skrivning')
    avv = []
    for w in del_poster: sk.skriv_en(klient, w)
    efter = {api.sifferid(p['id']): p for p in las(klient, ids)}
    for w in del_poster:
        e, f = efter[api.sifferid(w['id'])], fore[api.sifferid(w['id'])]
        fe = sk.jamfor_text(w, f, e, klartagg=klartagg) + skyddsavvikelser(f, e)
        if fe: avv.append((w['id'], fe))
    if avv: return [], avv
    for w in del_poster: sk.tagga(klient, w['id'], klartagg)
    efter2 = {api.sifferid(p['id']): p for p in las(klient, ids)}
    for w in del_poster:
        e, f = efter2[api.sifferid(w['id'])], fore[api.sifferid(w['id'])]
        fe = sk.jamfor_text(w, f, e, tagg_klar=True, klartagg=klartagg) + skyddsavvikelser(f, e)
        if fe: avv.append((w['id'], fe))
    return ([] if avv else ids), avv


def main(argv=None):
    profil, a = butiksprofil.profil_fran_argv(argv if argv is not None else sys.argv[1:])
    lage = next((x for x in ('--dry-run', '--kanarie', '--rest') if x in a), None)
    ut = os.path.join(ROT, 'rapporter', f'shopify-original-{datetime.date.today().isoformat()}')
    if not profil['ar_standardprofil']: ut += '-' + butiksprofil.butiksslug(profil)
    if '--ut' in a: k = a.index('--ut'); ut = a[k + 1]; del a[k:k + 2]
    filer = [x for x in a if not x.startswith('--')]
    if not lage or len(filer) != 1: print(__doc__); return 2
    poster = json.load(open(filer[0], encoding='utf-8'))
    namn = os.path.splitext(os.path.basename(filer[0]))[0]
    sparr = las_sparr(butiksprofil.i_rot(profil, 'sparrlista'))
    klient = api.klient_fran_profil(profil)
    print('Butik:', api.verifiera_butik(klient))
    ids = [w['id'] for w in poster]
    live = las(klient, ids)
    fel = api.kontrollera_fore([l for l in live if l], [i for i, l in zip(ids, live) if l])
    if fel: print('Före-läget ofullständigt:', *fel[:5], sep='\n  '); return 1
    skriv, klar, avviker = klassa_skydd(poster, live, sparr)
    fore = {api.sifferid(l['id']): l for l in live if l}
    print(f'{len(poster)} produkter: {len(skriv)} att skriva, {len(klar)} redan lika, {len(avviker)} avvikande (hoppas över)')
    for w, s in avviker: print(f'  HOPPAS ÖVER {w["id"]} ({w.get("nr")}): {s}')
    valda = skriv[:sk.KANARIE_ANTAL] if lage == '--kanarie' else skriv
    fore_fil = os.path.join(ut, f'{namn}_fore_{lage.strip("-")}.json')
    api.spara_fore([fore[api.sifferid(w['id'])] for w in valda], fore_fil)
    print('Före-fil:', os.path.relpath(fore_fil, ROT), f'({len(valda)} produkter, med varianternas priser)')
    if lage == '--dry-run':
        for w in valda:
            l = fore[api.sifferid(w['id'])]
            print(f'  SKULLE SKRIVA {w["id"]} ({w["nr"]}): "{l["title"][:40]}" -> "{w["titel"][:40]}"; html {len(l["descriptionHtml"])} -> {len(w["html"])} tecken; '
                  f'{len(l["variants"]["nodes"])} varianter, taggar oförändrade utom {profil["klartagg"]}')
        return 0
    ok, avvik = [], []
    try:
        for s in range(0, len(valda), DEL):
            r, av = kor_del(klient, valda[s:s + DEL], fore, profil['klartagg'])
            ok += r; avvik += av
            if av: break
    except Stopp as e:
        avvik.append((str(e), ['STOPP före skrivning']))
    res = {'lage': lage, 'datum': datetime.datetime.now().isoformat(timespec='seconds'), 'skrivna_taggade_verifierade': ok,
           'avvikelser': [{'id': i, 'fel': f} for i, f in avvik], 'redan_lika': [w['id'] for w in klar],
           'hoppade_over': [{'id': w['id'], 'skal': s} for w, s in avviker], 'anrop': klient.antal_anrop}
    rf = os.path.join(ut, f'{namn}_resultat_{lage.strip("-")}.json')
    json.dump(res, open(rf, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'Skrivna, taggade och verifierade: {len(ok)} av {len(valda)}. Resultat: {os.path.relpath(rf, ROT)}')
    for i, f in avvik: print(f'  AVVIKELSE {i}: {"; ".join(f)}')
    if avvik: print('STOPP vid första avvikelse.'); return 1
    return 0


if __name__ == '__main__':
    try: sys.exit(main())
    except (api.ShopifyFel, butiksprofil.ProfilFel) as e: print('FEL:', api.maska(e)); sys.exit(1)
