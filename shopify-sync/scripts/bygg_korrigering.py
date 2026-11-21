#!/usr/bin/env python3
"""Bygger en skrivfil (id, nr, titel, seo_title, meta, html) ur live-läge + utkast med ersättningspar. ENDAST OFFLINE, ingen skrivning.

Indata: live-fil (lista med id, titel, seo_title, meta, html, tags) och en eller flera utkastfiler (lista med id, meta, seo_title, ersatt[{fore,efter}], anm).
Varje `fore` måste förekomma exakt en gång i html (annars avvisas produkten). För produkter med taggen "På beställning" läggs
leveranstidsmeningen till sist i fraktstycket om den saknas. Produkter som inte klarar kontrollerna hamnar i avvisade (med skäl).
Användning: bygg_korrigering.py LIVE.json UTKAST.json [UTKAST2.json ...] --ut SKRIVFIL.json --avvisade AVVISADE.json
"""
import json, re, sys

LEV = 'Beställningsvaror kan ta upp till en vecka längre.'
FRAKT = 'Se sidan Frakt för övriga länder.'


def bygg(live, utkast):
    ut, avvisade = [], []
    lv = {x['id']: x for x in live}
    for u in utkast:
        i = u['id']; x = lv.get(i)
        if not x:
            avvisade.append((i, 'saknas i live-filen')); continue
        html, meta, seo = x['html'], x['meta'], x['seo_title']
        andrad = False
        if u.get('anm') and not u.get('ersatt') and not u.get('meta'):
            avvisade.append((i, 'hoppad: ' + u['anm'])); continue
        fel = None
        for par in u.get('ersatt') or []:
            if html.count(par['fore']) != 1:
                fel = f'"fore" förekommer {html.count(par["fore"])} gånger: {par["fore"][:60]}'; break
            html = html.replace(par['fore'], par['efter']); andrad = True
        if fel:
            avvisade.append((i, fel)); continue
        if u.get('meta'):
            meta, andrad = u['meta'], True
        if u.get('seo_title'):
            seo, andrad = u['seo_title'], True
        if 'På beställning' in (x.get('tags') or []) and LEV not in html:
            if FRAKT not in html:
                avvisade.append((i, 'fraktstycket saknar förväntad mening; leveranstidsmening kunde inte läggas in')); continue
            html = html.replace(FRAKT, FRAKT + ' ' + LEV, 1); andrad = True
        if not andrad:
            avvisade.append((i, 'ingen ändring')); continue
        ut.append({'id': i, 'nr': i[-6:], 'titel': x['titel'], 'seo_title': seo, 'meta': meta, 'html': html})
    return ut, avvisade


def main(a):
    ut_f = a[a.index('--ut') + 1]; av_f = a[a.index('--avvisade') + 1]
    filer = [p for k, p in enumerate(a) if p.endswith('.json') and k > 0 and a[k - 1] not in ('--ut', '--avvisade')]
    live = json.load(open(a[0], encoding='utf-8'))
    utkast = [u for f in filer[:] if f != a[0] for u in json.load(open(f, encoding='utf-8'))]
    ut, av = bygg(live, utkast)
    json.dump(ut, open(ut_f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump([{'id': i, 'skal': s} for i, s in av], open(av_f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{len(ut)} produkter i skrivfilen, {len(av)} avvisade')
    for i, s in av:
        print('  avvisad', i, s[:100])


if __name__ == '__main__':
    main(sys.argv[1:])
