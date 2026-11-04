#!/usr/bin/env python3
"""Jämför live-läsning mot en skrivfil, tecken för tecken (R16).

Live-filen är en JSON-lista (eller {"data":{"nodes":[...]}} rakt från graphql nodes()) med
id (gid eller siffror), title, handle, status, tags, seo{title description}, descriptionHtml.
seo.title = null räknas som lika med titeln (Shopify lagrar så). Avslutar med kod 1 vid avvikelse.
Användning: jamfor_live.py <skrivfil> <livefil> [--fore <forefil>]
  --fore: kontrollerar också att handle och status är oförändrade mot före-filen.
"""
import json, sys, re

def lasnoder(p):
    d = json.load(open(p, encoding='utf-8'))
    if isinstance(d, dict):
        d = d.get('data', d)
        d = d.get('nodes', d) if isinstance(d, dict) else d
        if isinstance(d, dict):
            d = [v for v in d.values() if isinstance(v, list)][0]
    return [x for x in d if x]

def nid(x):
    return re.sub(r'\D', '', str(x.get('id')))

def main():
    a = sys.argv[1:]
    fore = None
    if '--fore' in a:
        k = a.index('--fore'); fore = {nid(x): x for x in lasnoder(a[k + 1])}; del a[k:k + 2]
    skriv = {str(x['id']): x for x in json.load(open(a[0], encoding='utf-8'))}
    live = {nid(x): x for x in lasnoder(a[1])}
    fel = 0
    for i, w in skriv.items():
        l = live.get(i)
        if not l:
            continue
        seo = l.get('seo') or {}
        kontroller = [
            ('titel', l.get('title'), w['titel']),
            ('seo.title', seo.get('title') or l.get('title'), w.get('seo_title') or w['titel']),
            ('seo.description', seo.get('description'), w.get('meta')),
            ('descriptionHtml', l.get('descriptionHtml'), w['html']),
        ]
        for namn, lv, wv in kontroller:
            if lv != wv:
                fel += 1
                print(f'AVVIKELSE {w["nr"]} ({i}) {namn}: live {len(lv or "")} tecken, skrivfil {len(wv or "")} tecken')
                for p, (c1, c2) in enumerate(zip(lv or '', wv or '')):
                    if c1 != c2:
                        print(f'   första skillnaden vid tecken {p}: live {lv[max(0,p-20):p+20]!r} / skrivfil {wv[max(0,p-20):p+20]!r}'); break
        if re.search(r'[­​ ﻿]', ''.join(str(l.get(k) or '') for k in ('title', 'descriptionHtml'))):
            fel += 1; print(f'AVVIKELSE {w["nr"]} ({i}): osynligt tecken i live')
        if 'texter-klara' not in (l.get('tags') or []):
            print(f'   obs {w["nr"]} ({i}): taggen texter-klara saknas ännu')
        if fore and i in fore:
            for k in ('handle', 'status'):
                if fore[i].get(k) and l.get(k) and fore[i][k] != l[k]:
                    fel += 1; print(f'AVVIKELSE {w["nr"]} ({i}): {k} ändrad {fore[i][k]} → {l[k]}')
    saknas = [i for i in skriv if i not in live]
    print(f'{len(skriv) - len(saknas)} av {len(skriv)} jämförda, {fel} avvikelser' + (f'; ej lästa: {len(saknas)}' if saknas else ''))
    sys.exit(1 if fel else 0)

if __name__ == '__main__':
    main()
