#!/usr/bin/env python3
"""Live-klassning för rensning 2 (F2, "enligt tillverkaren" på maxvikt). BARA LÄSNING: skriver inget i Shopify.

Indata: JSON-lista med id, nr, rader [{gammal, ny}] (radens exakta text i en <li>, före och efter).
Varje produkt klassas mot live:
  skriv     varje gammal rad finns exakt en gång som <li>gammal</li> och ny rad saknas; R5 hålls efter ändringen
            (högst 2 "enligt tillverkaren" i hela texten: beskrivning + metabeskrivning); produkten är inte spärrad
  klar      alla nya rader finns redan i live
  avviker   något annat (spärrad, saknas, raden ändrad, för många "enligt tillverkaren" efter ändringen)
Skriver (nya filer, skrivs aldrig över): före-fil med live-läget, indatafil för en senare skrivning (bara "skriv"),
och en Markdown-rapport med före/efter per rad. Skrivningen själv görs inte här.
Användning: rensning2_klassning.py INFIL --ut KATALOG [--profil BUTIKSPROFIL.json]
"""
import datetime, json, os, sys

HAR = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.abspath(os.path.join(HAR, '..', '..'))
sys.path.insert(0, HAR)
import shopify_api as api  # noqa: E402
import butiksprofil  # noqa: E402
from skrivfil_kontroll import las_sparr  # noqa: E402

FRAS = 'enligt tillverkaren'


def antal_fras(p, html=None):
    html = p['descriptionHtml'] if html is None else html
    delar = [html, (p.get('seo') or {}).get('description') or '', p.get('title') or '', (p.get('seo') or {}).get('title') or '']
    return sum(d.lower().count(FRAS) for d in delar)


def klassa(post, live, sparr):
    """Ren funktion (testbar utan nätverk). Returnerar (klass, skäl, ny_html)."""
    i = api.sifferid(post['id'])
    if i in sparr:
        return 'avviker', f'spärrad ({sparr[i][0]})', None
    if live is None:
        return 'avviker', 'finns inte i butiken', None
    html = live['descriptionHtml']
    rader = post['rader']
    ny_klar = [r['ny'] in html for r in rader]
    if all(ny_klar):
        return 'klar', 'alla nya rader finns redan i live', None
    ny_html = html
    for r in rader:
        mal = f'<li>{r["gammal"]}</li>'
        n = ny_html.count(mal)
        if n != 1:
            return 'avviker', f'raden "{r["gammal"]}" finns {n} gånger som <li> i live (väntade 1)', None
        ny_html = ny_html.replace(mal, f'<li>{r["ny"]}</li>')
    efter = antal_fras(live, ny_html)
    if efter > 2:
        return 'avviker', f'R5: {efter} "enligt tillverkaren" i texten efter ändringen (högst 2)', None
    return 'skriv', f'live-raden stämmer; {antal_fras(live)} -> {efter} "enligt tillverkaren" i texten', ny_html


def main(argv=None):
    profil, a = butiksprofil.profil_fran_argv(argv if argv is not None else sys.argv[1:])
    ut = None
    if '--ut' in a:
        k = a.index('--ut'); ut = a[k + 1]; del a[k:k + 2]
    filer = [x for x in a if not x.startswith('--')]
    if not ut or len(filer) != 1:
        print(__doc__); return 2
    poster = json.load(open(filer[0], encoding='utf-8'))
    sparr = las_sparr(butiksprofil.i_rot(profil, 'sparrlista'))
    klient = api.klient_fran_profil(profil)
    print('Butik:', api.verifiera_butik(klient))
    live = api.hamta_produkter(klient, [w['id'] for w in poster])
    fel = api.kontrollera_fore([l for l in live if l], [w['id'] for w, l in zip(poster, live) if l])
    if fel:
        print('Före-läget är ofullständigt:', *fel[:5], sep='\n  '); return 1
    namn = os.path.splitext(os.path.basename(filer[0]))[0]
    api.spara_fore([l for l in live if l], os.path.join(ut, f'{namn}_live_fore.json'))
    skriv, md = [], []
    rader_md = ['| Nr | Titel | Status live | Klass | Skäl |', '|---|---|---|---|---|']
    for w, l in zip(poster, live):
        kl, skal, ny_html = klassa(w, l, sparr)
        rader_md.append(f'| {w["nr"]} | {(l or {}).get("title", "")} | {(l or {}).get("status", "")} | {kl} | {skal} |')
        for r in w['rader']:
            md.append(f'- **{w["nr"]}**: `{r["gammal"]}` -> `{r["ny"]}` ({kl})')
        if kl == 'skriv':
            skriv.append({'id': w['id'], 'nr': w['nr'], 'rader': w['rader'], 'html_fore_tecken': len(l['descriptionHtml']),
                          'html_ny': ny_html, 'seo_title': api.effektiv_seo_title(l),
                          'meta': (l.get('seo') or {}).get('description')})
    res = os.path.join(ut, f'{namn}_klassning.md')
    open(res, 'x', encoding='utf-8').write(
        f'# Live-klassning {datetime.date.today().isoformat()} (bara läsning)\n\n' + '\n'.join(rader_md) + '\n\n## Före och efter per rad\n\n' + '\n'.join(md) + '\n')
    inf = os.path.join(ut, f'{namn}_indata_skriv.json')
    json.dump(skriv, open(inf, 'x', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('\n'.join(rader_md)); print(f'\n{len(skriv)} av {len(poster)} att skriva. Filer: {os.path.relpath(res, ROT)}, {os.path.relpath(inf, ROT)}')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (api.ShopifyFel, butiksprofil.ProfilFel) as e:
        print('FEL:', api.maska(e)); sys.exit(1)
