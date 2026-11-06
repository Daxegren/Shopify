#!/usr/bin/env python3
"""Daglig kontroll efter leverantörssynken: ligger våra texter, taggar och statusar kvar? ENDAST LÄSNING.

Bygger den senast avsedda texten per produkt ur alla skrivfiler (rättningsfiler `korr` väger tyngst) och jämför med butiken.
Rapporterar bara AVVIKELSER SOM ÄR NYA mot baslinjen (`--baslinje`), så att kända fall inte larmar varje dag.

Användning:
  nattkontroll.py                          # jämför mot baslinjen och skriv rapport
  nattkontroll.py --skapa-baslinje         # spara dagens läge som baslinje (görs efter att David godkänt läget)
Rapport: rapporter/nattkontroll/nattkontroll-ÅÅÅÅ-MM-DD.md och .csv. Kod 1 om nya avvikelser finns.
Skriv aldrig ut hemligheter. Ändrar inget i Shopify."""
import csv, glob, json, os, sys, time
HAR = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HAR)
import shopify_api as api
from shopify_skriv_texter import jamfor_text

ROT = os.path.abspath(os.path.join(HAR, '..', '..'))
SKRIV = os.path.join(ROT, 'rapporter', 'facit-bos-2026-10-31', 'vag2_skriv')
UT = os.path.join(ROT, 'rapporter', 'nattkontroll')
BASLINJE = os.path.join(UT, 'baslinje.json')
NORM = ' (enligt tillverkaren)'  # rensning 2 (2026-11-04) lade till detta på lastgränsrader


def avsedda():
    filer = list(dict.fromkeys(sorted(glob.glob(os.path.join(SKRIV, '*skriv*.json')))))
    nyckel = lambda f: (1 if 'korr' in os.path.basename(f) else 0, os.path.getmtime(f), os.path.basename(f))
    exp = {}
    for f in sorted(filer, key=nyckel):
        try: d = json.load(open(f, encoding='utf-8'))
        except Exception: continue
        for p in d:
            if isinstance(p, dict) and 'html' in p and 'id' in p:
                exp[str(p['id'])] = (p, os.path.basename(f))
    return exp


def kontrollera():
    exp = avsedda(); k = api.ShopifyKlient(); ids = list(exp); live = None
    for forsok in range(4):
        try: live = api.hamta_produkter(k, ids, del_storlek=10); break
        except Exception as e: print('nätverksfel, försöker igen:', type(e).__name__); time.sleep(5)
    if live is None: sys.exit('Kunde inte läsa butiken.')
    fynd = {}
    for i, l in zip(ids, live):
        w, fil = exp[i]
        if not l: fynd[i] = ('saknas', fil, w.get('nr'), ''); continue
        if l.get('status') != 'ACTIVE': fynd[i] = ('ej aktiv: ' + str(l.get('status')), fil, w.get('nr'), l.get('title', '')[:60]); continue
        w2 = dict(w, html=w['html'].replace(NORM, ''))
        l2 = dict(l, descriptionHtml=(l.get('descriptionHtml') or '').replace(NORM, ''))
        fe = [x for x in jamfor_text(w2, l2, l2, tagg_klar=False) if not x.startswith('taggar avviker')]
        if w.get('meta') is None: fe = [x for x in fe if not x.startswith('seo.description')]  # äldre skrivfiler saknade meta
        if 'texter-klara' not in (l.get('tags') or []): fe.append('taggen texter-klara saknas')
        if fe: fynd[i] = ('; '.join(fe)[:200], fil, w.get('nr'), l.get('title', '')[:60])
    return fynd, len(ids)


def main(a):
    os.makedirs(UT, exist_ok=True)
    fynd, n = kontrollera()
    if '--skapa-baslinje' in a:
        json.dump({'skapad': time.strftime('%Y-%m-%d %H:%M'), 'ids': sorted(fynd)}, open(BASLINJE, 'w'), indent=1)
        print(f'Baslinje sparad: {len(fynd)} kända avvikelser av {n} produkter.'); return 0
    bas = set(json.load(open(BASLINJE))['ids']) if os.path.exists(BASLINJE) else set()
    nya = {i: v for i, v in fynd.items() if i not in bas}
    atgardade = sorted(bas - set(fynd))
    dag = time.strftime('%Y-%m-%d')
    with open(os.path.join(UT, f'nattkontroll-{dag}.csv'), 'w', newline='', encoding='utf-8') as o:
        w = csv.writer(o); w.writerow(['produkt_id', 'nr', 'avvikelse', 'skrivfil', 'titel_live'])
        for i, (t, fil, nr, ti) in nya.items(): w.writerow([i, nr, t, fil, ti])
    rad = [f'# Nattkontroll {dag}', '', f'- Kontrollerade produkter: {n}', f'- Kända avvikelser (baslinjen): {len(bas)}', f'- **Nya avvikelser: {len(nya)}**', f'- Kända som nu är åtgärdade: {len(atgardade)}', '']
    typer = {}
    for t, *_ in nya.values(): typer[t.split(';')[0].split(' ')[0] + ' ' + (t.split(' ')[1] if ' ' in t else '')] = typer.get(t.split(';')[0].split(' ')[0] + ' ' + (t.split(' ')[1] if ' ' in t else ''), 0) + 1
    for t, c in sorted(typer.items(), key=lambda x: -x[1]): rad.append(f'- {c} st: {t.strip()}')
    open(os.path.join(UT, f'nattkontroll-{dag}.md'), 'w', encoding='utf-8').write('\n'.join(rad) + '\n')
    print('\n'.join(rad)); return 1 if nya else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
