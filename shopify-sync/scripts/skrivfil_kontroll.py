#!/usr/bin/env python3
"""Kontroll av skrivfiler (JSON-lista med id, nr, titel, seo_title, meta, html) innan något skrivs till Shopify.

Bygger på lärdomar i shopify-sync/docs/LARDOMAR.md. Avslutar med kod 1 om något FEL hittas.
Användning: skrivfil_kontroll.py FIL [FIL ...] [--sparr shopify-sync/config/sparrlista.json] [--tillat-kanda]
"""
import csv, json, re, sys, os, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import regeltester  # nya kontroller (läge per kontroll i shopify-sync/config/regeltester.json); börjar som varning

ROT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MARKEN = ['Hammer', 'Toorx', 'Tunturi', 'BH Fitness', 'Finnlo by Hammer', 'Gymstick', 'Christopeit', 'Kettler', 'Fluid', 'Union', 'Peltonen']
MARKEN_VARNING = ['Fluid']
FORBJUDET = [
    (r'här kallad', 'arbetsterm "här kallad" i kundtext'),
    (r'Vanliga frågor', 'FAQ-avsnitt kopierat från källa'),
    (r'Om märket', '"Om märket"-avsnitt från pilotens gamla text'),
    (r'Maximum (operating|user) weight', 'engelsk maxviktsrad kvar'),
    (r'Load (capacity|range)', 'engelsk lastrad kvar'),
]
BLOCK_KRAV = ['Leverans, retur och garanti', 'Frakt och leverans', 'Retur:', 'Reklamation:', 'Säljare:', 'info@bestofsports.se']


def las_profil(path):
    """Läser märken och standardblock ur butiksprofilen; faller tillbaka på standardvärdena ovan."""
    global MARKEN, MARKEN_VARNING, BLOCK_KRAV
    if path and os.path.exists(path):
        p = json.load(open(path, encoding='utf-8'))
        MARKEN = p.get('marken', MARKEN)
        MARKEN_VARNING = p.get('marken_varning_bara', MARKEN_VARNING)
        BLOCK_KRAV = p.get('standardblock_krav', BLOCK_KRAV)


def las_sparr(path):
    cfg = json.load(open(path, encoding='utf-8'))
    ut = {}
    undantag = set()
    for s in cfg['sparrar']:
        if not s.get('aktiv'):
            continue
        with open(os.path.join(ROT, s['idfil']), encoding='utf-8') as f:
            for r in csv.DictReader(f):
                if s.get('typ') == 'undantag':  # frisläpper enskilda id ur andra spärrar (beslut anges i posten)
                    undantag.add(str(r[s['idkolumn']]))
                else:
                    ut[str(r[s['idkolumn']])] = (s['namn'], set(s.get('kanda_overtradelser', [])))
    for i in undantag:
        ut.pop(i, None)
    return ut


def kontrollera(fil, sparr, tillat_kanda):
    d = json.load(open(fil, encoding='utf-8'))
    fel, varn = [], []
    c = {k: collections.Counter(x.get(k) for x in d if x.get(k)) for k in ('titel', 'seo_title', 'meta')}
    for x in d:
        nr, i = x.get('nr'), str(x.get('id'))
        f = lambda m: fel.append(f'{nr} ({i}): {m}')
        v = lambda m: varn.append(f'{nr} ({i}): {m}')
        if i in sparr:
            namn, kanda = sparr[i]
            if tillat_kanda and i in kanda:
                v(f'spärrad ({namn}) men känd överträdelse')
            else:
                f(f'SPÄRRAD produkt ({namn}) får inte skrivas')
        text = ' '.join(str(x.get(k) or '') for k in ('titel', 'seo_title', 'meta', 'html'))
        if re.search(r'driftsvikt', text, re.I):
            v('"driftsvikt": ok bara om det står ordagrant på svenska i produktens egen källa (alt A, 2026-11-04)')
        for pat, skal in FORBJUDET:
            if re.search(pat, text, re.I):
                f(skal)
        if re.search(r'\b\d+(,\d+)? tum (skärm|pekskärm|display)', text):
            f('"N tum skärm": skriv "N-tums skärm" i löptext (R10)')
        for m_ in re.finditer(r'\b([A-ZÅÄÖ][\wåäö-]+(?: [\wåäö-]+){0,3}) är (?:en|ett) \1\b', x.get('html') or '', re.I):
            f(f'cirkulär inledning: "{m_.group(0)[:50]}" (R11)'); break
        if re.search(r'&(?!amp;)', re.sub(r'&nbsp;|&amp;', '', text)):
            v('"&" i texten (skriv "och")')
        for m in MARKEN:
            for k in ('titel', 'seo_title'):
                if x.get(k) and re.search(r'\b' + re.escape(m.upper()) + r'\b', x[k]) and m.upper() != m:
                    (v if m in MARKEN_VARNING else f)(f'märket {m} i versaler i {k}')
        for rad in re.findall(r'<li>[^<:]{1,40}: ([a-zåäö]{3,})\b', x.get('html') or ''):
            f('liten bokstav efter kolon i specifikationsrad'); break
        for krav in BLOCK_KRAV:
            if krav not in (x.get('html') or ''):
                f(f'standardblocket saknar "{krav}"')
        t = x.get('titel') or ''
        if len(t) > 70: f('titel över 70 tecken')
        if t.count(',') > 2: v('titel har fler än 2 kommatecken')
        if x.get('seo_title') and len(x['seo_title']) > 43: f('seo-titel över 43 tecken')
        if x.get('meta') and not 70 <= len(x['meta']) <= 155: f(f'meta {len(x["meta"])} tecken (70–155)')
        if not x.get('meta'): v('meta saknas (null)')
        mt = x.get('meta') or ''
        if mt.endswith('Finns hos BEST OF SPORTS.') and len(mt) - len('Finns hos BEST OF SPORTS.') - 1 >= 70:
            v('meta slutar med utfyllnaden "Finns hos BEST OF SPORTS." fast den redan är över 70 tecken (R12); rensas i butiken när API-vägen finns')
        for k in ('titel', 'seo_title', 'meta'):
            if x.get(k) and c[k][x[k]] > 1:
                f(f'dubblett av {k} inom filen')
        if '  ' in text.replace('\n', ' ').replace('> <', '><'):
            v('dubbla mellanslag')
        if len(re.findall(r'enligt tillverkaren', x.get('html') or '', re.I)) > 2:
            f('"enligt tillverkaren" fler än 2 gånger i texten (R5)')
        if re.search(r'-Lastcykel|-Cykel\b', ' '.join(str(x.get(k) or '') for k in ('titel', 'seo_title'))):
            f('stor bokstav efter bindestreck i typordet ("El-lastcykel", inte "El-Lastcykel")')
        if x.get('meta') and not re.search(r'\b(är|har|ger|passar|finns|väger|mäter|består|används|kan|ingår|erbjuder|levereras|säljs|tillverkad|tillverkade|gör|hjälper|följer|innehåller|fungerar|rymmer|kommer|med)\b', x['meta'], re.I) or (x.get('meta') and re.match(r'^[A-ZÅÄÖ][\wåäö-]+(?: [\wåäö-]+){0,3} med ', x['meta']) and not re.search(r'\b(är|har|ger|passar|finns|väger|mäter|består|används|kan|ingår|erbjuder|säljs|innehåller|fungerar|rymmer)\b', x['meta'], re.I)):
            v('meta saknar verb (granskarfynd 31 av 37 rättningar i k_08b–d): börja inte med "Produkt med …"')
        for fld, txt in (('meta', x.get('meta') or ''), ('första meningen', re.sub(r'<[^>]+>', '', (re.search(r'<p>(.*?)</p>', x.get('html') or '', re.S) or [None, ''])[1]))):
            if re.match(r'^[A-ZÅÄÖ][^.,:;]{2,70}? är (?:en|ett) ', txt):
                v(f'{fld} börjar "Namn är en/ett typord" (cirkulär inledning, 30+ granskarrättningar): börja med vad produkten gör eller består av'); break
        if re.search(r'[­​ ﻿]', text):
            f('osynligt tecken (mjukt bindestreck, nollbredd, hårt mellanslag eller BOM)')
    return len(d), fel, varn


def kontrollera_regeltester(fil):
    """Nya kontroller (regeltester.py). Returnerar (fel, varningar) som textrader. Påverkar inte kontrollera() eller utgångskoden
    så länge alla kontroller står i läget varning (standard)."""
    cfg = regeltester.las_cfg()
    fel, varn = [], []
    with open(fil, encoding='utf-8') as fh:
        utkast = json.load(fh)
    for x in utkast:
        for lage, fy in regeltester.kontrollera_utkast(x, cfg):
            rad = f"{x.get('nr')} ({x.get('id')}): [{fy.kod}] i {fy.falt}: {fy.text}"
            (fel if lage == 'fel' else varn).append(rad)
    return fel, varn


def main():
    a = sys.argv[1:]
    sparr_path = os.path.join(ROT, 'shopify-sync/config/sparrlista.json')
    if '--sparr' in a:
        k = a.index('--sparr'); sparr_path = a[k + 1]; del a[k:k + 2]
    profil = os.path.join(ROT, 'shopify-sync/config/butiksprofil-bestofsports.json')
    if '--profil' in a:
        k = a.index('--profil'); profil = a[k + 1]; del a[k:k + 2]
    las_profil(profil)
    tillat = '--tillat-kanda' in a
    a = [x for x in a if x != '--tillat-kanda']
    sparr = las_sparr(sparr_path)
    totalfel = 0
    for fil in a:
        n, fel, varn = kontrollera(fil, sparr, tillat)
        print(f'{os.path.basename(fil)}: {n} produkter, {len(fel)} FEL, {len(varn)} varningar')
        for m in fel: print('  FEL  ', m)
        for m in varn[:5]: print('  varn ', m)
        totalfel += len(fel)
        rfel, rvarn = kontrollera_regeltester(fil)
        if rfel or rvarn:
            print(f'  regeltester: {len(rfel)} FEL, {len(rvarn)} varningar (varje kontroll: shopify-sync/scripts/regeltester.py)')
            for m in rfel: print('  FEL  ', m)
            for m in rvarn[:5]: print('  varn ', m)
        totalfel += len(rfel)
    sys.exit(1 if totalfel else 0)


if __name__ == '__main__':
    main()
