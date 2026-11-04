#!/usr/bin/env python3
"""Läser tillbaka alla produkter i givna skrivfiler från butiken och jämför tecken för tecken (title, seo, descriptionHtml,
taggen texter-klara). Används dagen efter skrivning (nattsynk av leverantörsdata kan skriva över texter; lärdom 2026-10-30).
Användning: verifiera_skrivna.py SKRIVFIL [SKRIVFIL ...]   (kod 1 vid avvikelse). Skriver inget i Shopify."""
import json, os, sys
HAR = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HAR)
import shopify_api as api
from shopify_skriv_texter import jamfor_text

def main(filer):
    k = api.ShopifyKlient(); print('Butik:', api.verifiera_butik(k))
    tot = fel = 0
    for f in filer:
        poster = json.load(open(f, encoding='utf-8'))
        live = api.hamta_produkter(k, [w['id'] for w in poster], del_storlek=10)
        for w, l in zip(poster, live):
            tot += 1
            if not l: fel += 1; print(f'AVVIKELSE {os.path.basename(f)} {w["id"]}: finns inte'); continue
            NORM = ' (enligt tillverkaren)'  # rensning 2 (2026-11-04) lade till detta på lastgränsrader i redan skrivna texter
            w2 = dict(w, html=w['html'].replace(NORM, '')); l2 = dict(l, descriptionHtml=(l.get('descriptionHtml') or '').replace(NORM, ''))
            fe = jamfor_text(w2, l2, l2, tagg_klar=False)
            if 'texter-klara' not in (l.get('tags') or []): fe.append('taggen texter-klara saknas')
            fe = [x for x in fe if not x.startswith('taggar avviker')]
            if fe: fel += 1; print(f'AVVIKELSE {os.path.basename(f)} {w["id"]} ({w.get("nr")}): ' + '; '.join(fe))
    print(f'{tot} produkter lästa, {fel} med avvikelse'); return 1 if fel else 0

if __name__ == '__main__':
    try: sys.exit(main(sys.argv[1:]))
    except api.ShopifyFel as e: print('FEL:', api.maska(e)); sys.exit(1)
