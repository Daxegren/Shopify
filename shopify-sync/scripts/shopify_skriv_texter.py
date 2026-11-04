#!/usr/bin/env python3
"""Skriver en skrivfil (id, nr, titel, seo_title, meta, html) via Admin API och sätter taggen texter-klara sist.

Per produkt klassas live-läget före skrivning:
  skriv    live skiljer sig från skrivfilen och produkten är ACTIVE            -> skrivs
  klar     title, seo och descriptionHtml är redan lika skrivfilen             -> bara taggen (om den saknas)
  avviker  ej ACTIVE, saknas, spärrad eller meta saknas i skrivfilen           -> hoppas över och rapporteras
Lägen: --dry-run (ingen skrivning), --kanarie (3 första "skriv"), --rest (övriga, delar om 4).
Efter varje del: återläsning och jämförelse tecken för tecken (title, seo.title, seo.description, descriptionHtml;
handle, status och befintliga taggar oförändrade). Stopp vid första avvikelse (kod 1). Taggen sätts först efter
verifierad återläsning och verifieras i sin tur. Före-fil (komplett) och resultatfil sparas i --ut.
Användning: shopify_skriv_texter.py SKRIVFIL (--dry-run | --kanarie | --rest) [--ut KATALOG]
"""
import datetime, json, os, sys

HAR = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.abspath(os.path.join(HAR, '..', '..'))
sys.path.insert(0, HAR)
import shopify_api as api  # noqa: E402
from skrivfil_kontroll import las_sparr  # noqa: E402

KLARTAGG = 'texter-klara'
KANARIE_ANTAL, DEL = 3, 4


def forvantat(w):
    return {'title': w['titel'], 'seo_title': w.get('seo_title') or w['titel'], 'meta': w['meta'], 'html': w['html']}


def jamfor_text(w, fore, efter, tagg_klar=False):
    """Returnerar avvikelser mellan återläst produkt och skrivfilen."""
    f, fel = forvantat(w), []
    if efter.get('title') != f['title']: fel.append('title avviker')
    if api.effektiv_seo_title(efter) != f['seo_title']: fel.append('seo.title avviker')
    if (efter.get('seo') or {}).get('description') != f['meta']: fel.append('seo.description avviker')
    if efter.get('descriptionHtml') != f['html']:
        a, b = efter.get('descriptionHtml') or '', f['html']
        p = next((n for n, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
        fel.append(f'descriptionHtml avviker vid tecken {p} (live {len(a)}, skrivfil {len(b)} tecken)')
    for k in ('handle', 'status'):
        if fore.get(k) != efter.get(k): fel.append(f'{k} ändrad')
    forvantade_taggar = sorted(set(fore.get('tags') or []) | ({KLARTAGG} if tagg_klar else set()))
    if sorted(efter.get('tags') or []) != forvantade_taggar: fel.append('taggar avviker från förväntat')
    return fel


def klassa(poster, live, sparr):
    skriv, klar, avviker = [], [], []
    for w, l in zip(poster, live):
        if str(w['id']) in sparr: avviker.append((w, f'spärrad ({sparr[str(w["id"])][0]})')); continue
        if l is None: avviker.append((w, 'finns inte i butiken')); continue
        if not w.get('meta') or not w.get('html') or not w.get('titel'): avviker.append((w, 'skrivfilen saknar titel, meta eller html')); continue
        if l['status'] != 'ACTIVE': avviker.append((w, f'status {l["status"]}')); continue
        if not jamfor_text(w, l, l): klar.append(w)
        else: skriv.append(w)
    return skriv, klar, avviker


def skriv_en(klient, w):
    f = forvantat(w)
    q = 'mutation($p:ProductUpdateInput!){productUpdate(product:$p){product{id} userErrors{field message}}}'
    d = klient.graphql(q, {'p': {'id': api.gid(w['id']), 'title': f['title'], 'descriptionHtml': f['html'],
                                 'seo': {'title': f['seo_title'], 'description': f['meta']}}})['productUpdate']
    if d['userErrors']: raise api.ShopifyFel('userErrors: ' + json.dumps(d['userErrors'], ensure_ascii=False))


def tagga(klient, pid):
    d = klient.graphql('mutation($id:ID!,$t:[String!]!){tagsAdd(id:$id,tags:$t){node{id} userErrors{field message}}}',
                       {'id': api.gid(pid), 't': [KLARTAGG]})['tagsAdd']
    if d['userErrors']: raise api.ShopifyFel('userErrors: ' + json.dumps(d['userErrors'], ensure_ascii=False))


def kor_del(klient, del_poster, fore):
    """Skriv, återläs, jämför; tagga först efter ren jämförelse; återläs och jämför igen."""
    avv = []
    for w in del_poster: skriv_en(klient, w)
    efter = api.hamta_produkter(klient, [w['id'] for w in del_poster])
    rena = []
    for w, e in zip(del_poster, efter):
        fe = jamfor_text(w, fore[api.sifferid(w['id'])], e)
        (avv.append((w['id'], fe)) if fe else rena.append(w))
    if avv: return [], avv
    for w in rena: tagga(klient, w['id'])
    efter2 = api.hamta_produkter(klient, [w['id'] for w in rena])
    for w, e in zip(rena, efter2):
        fe = jamfor_text(w, fore[api.sifferid(w['id'])], e, tagg_klar=True)
        if fe: avv.append((w['id'], fe))
    return ([] if avv else [w['id'] for w in rena]), avv


def main(argv=None):
    a = list(argv if argv is not None else sys.argv[1:])
    lage = next((x for x in ('--dry-run', '--kanarie', '--rest') if x in a), None)
    ut = os.path.join(ROT, 'rapporter', f'shopify-original-{datetime.date.today().isoformat()}')
    if '--ut' in a: k = a.index('--ut'); ut = a[k + 1]; del a[k:k + 2]
    filer = [x for x in a if not x.startswith('--')]
    if not lage or len(filer) != 1: print(__doc__); return 2
    poster = json.load(open(filer[0], encoding='utf-8'))
    namn = os.path.splitext(os.path.basename(filer[0]))[0]
    sparr = las_sparr(os.path.join(ROT, 'shopify-sync/config/sparrlista.json'))
    klient = api.ShopifyKlient()
    ids = [w['id'] for w in poster]
    live = api.hamta_produkter(klient, ids)
    fel = api.kontrollera_fore([l for l in live if l], [i for i, l in zip(ids, live) if l])
    if fel: print('Före-läget ofullständigt:', *fel[:5], sep='\n  '); return 1
    skriv, klar, avviker = klassa(poster, live, sparr)
    fore = {api.sifferid(l['id']): l for l in live if l}
    print(f'{len(poster)} produkter: {len(skriv)} att skriva, {len(klar)} redan lika, {len(avviker)} avvikande (hoppas över)')
    for w, s in avviker: print(f'  HOPPAS ÖVER {w["id"]} ({w.get("nr")}): {s}')
    valda = skriv[:KANARIE_ANTAL] if lage == '--kanarie' else skriv
    fore_fil = os.path.join(ut, f'{namn}_fore_{lage.strip("-")}.json')
    api.spara_fore([fore[api.sifferid(w['id'])] for w in valda], fore_fil)
    print('Före-fil:', os.path.relpath(fore_fil, ROT), f'({len(valda)} produkter)')
    if lage == '--dry-run':
        for w in valda:
            l = fore[api.sifferid(w['id'])]
            print(f'  SKULLE SKRIVA {w["id"]} ({w["nr"]}): "{l["title"][:40]}" -> "{w["titel"][:40]}"; html {len(l["descriptionHtml"])} -> {len(w["html"])} tecken')
        return 0
    ok, avvik = [], []
    for s in range(0, len(valda), DEL):
        r, av = kor_del(klient, valda[s:s + DEL], fore)
        ok += r; avvik += av
        if av: break
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
    except api.ShopifyFel as e: print('FEL:', api.maska(e)); sys.exit(1)
