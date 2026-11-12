#!/usr/bin/env python3
"""Våg 2: prioritering efter sökdata och strukturlista (BARA LÄSNING av lokala filer, inget nätverk, inget till Shopify).

Slår ihop kategorilistan (prioritering.csv, kollektioner.csv, overlappande.json) med Search Console-filen
(kolumner: handle, klick, visningar, position) och skriver två förslagsfiler. Inget ändras i någon butik.

1. Rangordning av kollektioner för text (våg 2). Potential = visningar x närhet till position 10-30.
   Närhet: 1,0 på position 10-30; över 30 minskar den linjärt till 0 vid position 80; under 10 är den 0,3
   (sidan ligger redan högt, mindre att vinna). Utesluts: kategorier utanför utrullningen (klass 6 i
   prioritering.csv, samt handles med orden i --uteslut-ord, normalt junior/barn), kollektioner med färre
   än 5 köpbara produkter (standarden, avsnitt 5) och dubbletter/överlappande (avgör struktur först).
2. Strukturlista: tomma (0 köpbara), 1-4 köpbara och överlappande kollektioner sorterade efter visningar, med
   förslag (behåll / slå ihop / omdirigera / ta bort). Många visningar men 0 köpbara = "omdirigeras, tas inte bort".
   Förslagen är underlag; beslutet är Davids.

Användning:
  kategorier_vag2.py --mapp rapporter/bos-kategorier-2026-11-04 --gsc rapporter/gsc-bestofsports-2026-11-12/kollektioner.csv \
      --ut rapporter/bos-kategorier-2026-11-04 [--min-visningar 500]
"""
import argparse, csv, json, os, re, sys

UTESLUT_ORD = ('junior', 'barn')          # barn/junior ligger utanför utrullningen (butiksprofilen)
SKYDDADE = {'frontpage', 'all', 'alla-produkter-best-of-sports'}   # systemkollektioner: tas aldrig upp för borttagning
MIN_KOOPBARA_TEXT = 5
OMDIRIGERA_FRAN_VISNINGAR = 500


def tal(s):
    """Läser svenska och engelska tal ('1 234', '1\xa0234', '45,3', '45.3'). Tomt blir 0."""
    s = (s or '').strip().replace('\xa0', '').replace(' ', '')
    if not s:
        return 0.0
    if ',' in s and '.' in s:
        s = s.replace('.', '').replace(',', '.')
    else:
        s = s.replace(',', '.')
    return float(s)


def handle_av(s):
    """'https://x.se/collections/abc?x=1' -> 'abc'. Ren handle lämnas oförändrad."""
    s = (s or '').strip()
    m = re.search(r'/collections/([^/?#]+)', s)
    return (m.group(1) if m else s.strip('/')).lower()


def lasa_gsc(sokvag):
    ut = {}
    with open(sokvag, encoding='utf-8-sig', newline='') as f:
        for r in csv.DictReader(f):
            h = handle_av(r.get('handle'))
            if not h:
                continue
            v = ut.setdefault(h, {'klick': 0.0, 'visningar': 0.0, 'pos_x_vis': 0.0})
            vis = tal(r.get('visningar'))
            v['klick'] += tal(r.get('klick')); v['visningar'] += vis; v['pos_x_vis'] += tal(r.get('position')) * vis
    for h, v in ut.items():   # viktad snittposition om samma handle förekommer flera gånger
        v['position'] = round(v['pos_x_vis'] / v['visningar'], 1) if v['visningar'] else 0.0
        del v['pos_x_vis']
    return ut


def narhet(pos):
    if pos <= 0:
        return 0.0
    if pos < 10:
        return 0.3
    if pos <= 30:
        return 1.0
    return max(0.0, 1.0 - (pos - 30) / 50.0)


def potential(visningar, pos):
    return round(visningar * narhet(pos))


def utanfor(handle, klass, uteslut_ord=UTESLUT_ORD):
    return klass.strip().startswith('6') or any(o in handle for o in uteslut_ord)


def lasa_csv(sokvag):
    with open(sokvag, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def overlapp_grupper(lista):
    """handle -> (grupp, [övriga i gruppen]) ur overlappande.json (lista av listor)."""
    ut = {}
    for g in lista:
        for h in g:
            ut[h] = [x for x in g if x != h]
    return ut


def rangordna(prio, gsc, uteslut_ord=UTESLUT_ORD):
    """Rangordnar kollektioner för text. Returnerar (rangordnade, uteslutna) med orsak."""
    ranka, utes = [], []
    for r in prio:
        h = r['handle']; k = int(tal(r['koopbara'])); g = gsc.get(h, {'klick': 0, 'visningar': 0, 'position': 0})
        rad = dict(handle=h, titel=r['titel'], klass=r['klass'], koopbara=k, klick=int(g['klick']),
                   visningar=int(g['visningar']), position=g['position'], potential=potential(g['visningar'], g['position']))
        if r['klass'].startswith('1 '):
            utes.append({**rad, 'orsak': 'pilot (redan skriven som utkast)'}); continue
        if utanfor(h, r['klass'], uteslut_ord):
            utes.append({**rad, 'orsak': 'utanför utrullningen (profil: kosttillskott/barn m.fl.)'}); continue
        if r['klass'].startswith('4'):
            utes.append({**rad, 'orsak': 'överlappar annan kollektion (struktur först)'}); continue
        if k == 0:
            utes.append({**rad, 'orsak': 'inga köpbara produkter (struktur först)'}); continue
        if k < MIN_KOOPBARA_TEXT:
            utes.append({**rad, 'orsak': f'{k} köpbara (under {MIN_KOOPBARA_TEXT}, struktur först)'}); continue
        ranka.append(rad)
    ranka.sort(key=lambda x: (-x['potential'], -x['visningar'], -x['koopbara'], x['handle']))
    for i, x in enumerate(ranka, 1):
        x['rang'] = i
    return ranka, utes


def strukturforslag(kollektioner, overl, gsc, min_visningar=OMDIRIGERA_FRAN_VISNINGAR, uteslut_ord=UTESLUT_ORD, tak=None):
    """Förslag per tom, 1-4-köpbar eller överlappande kollektion. Ändrar ingenting.
    tak = lägsta antal visningar i Search Console-filen. Filen innehåller bara de översta kollektionerna, så en handle som saknas
    har inte noll visningar utan högst tak; det anges i skälet."""
    grp = overlapp_grupper(overl)
    k_av = {r['handle']: int(tal(r['koopbara'])) for r in kollektioner}
    def vis(h): return int(gsc.get(h, {}).get('visningar', 0))
    def klick(h): return int(gsc.get(h, {}).get('klick', 0))
    def basta(h):  # starkaste i gruppen (flest visningar, sedan flest köpbara)
        return sorted([h] + grp[h], key=lambda x: (-vis(x), -k_av.get(x, 0), x))[0]
    ut = []
    for r in kollektioner:
        h = r['handle']; k = k_av[h]; i_grupp = h in grp
        if k >= MIN_KOOPBARA_TEXT and not i_grupp:
            continue
        v, kl, pos = vis(h), klick(h), gsc.get(h, {}).get('position', 0.0)
        typ = 'tom' if k == 0 else ('1-4 köpbara' if k < MIN_KOOPBARA_TEXT else 'överlappande')
        if h in SKYDDADE:
            forslag, skal = 'behåll', 'systemkollektion (startsida/alla produkter), rörs inte'
        elif i_grupp and basta(h) != h:
            m = basta(h)
            forslag = 'slå ihop'
            skal = f'överlappar {", ".join(grp[h])}; starkast är {m} ({vis(m)} visningar). Omdirigera {h} dit, ta inte bort utan omdirigering' if v else \
                   f'överlappar {", ".join(grp[h])}; starkast är {m}. Inga visningar, kan tas bort efter kontroll av länkar'
            if not v and kl == 0 and k == 0:
                forslag = 'ta bort'
        elif i_grupp:
            forslag, skal = 'behåll', f'starkast av gruppen ({", ".join(grp[h])}); övriga slås ihop hit'
        elif k == 0 and v >= min_visningar:
            forslag, skal = 'omdirigera', f'{v} visningar men 0 köpbara: omdirigeras till närmaste kollektion, tas inte bort (mål väljs av David)'
        elif k == 0 and (kl > 0 or v > 0):
            forslag, skal = 'omdirigera', f'{v} visningar, {kl} klick, 0 köpbara: omdirigera hellre än ta bort (litet värde)'
        elif k == 0:
            forslag, skal = 'ta bort', 'tom och utan visningar eller klick i Search Console'
        elif v >= min_visningar:
            forslag, skal = 'behåll', f'{k} köpbara och {v} visningar: fyll på sortimentet eller slå ihop med närmaste större kollektion'
        elif v > 0:
            forslag, skal = 'slå ihop', f'{k} köpbara och bara {v} visningar: slå ihop med närmaste större kollektion och omdirigera'
        else:
            forslag, skal = 'ta bort', f'{k} köpbara och inga visningar: ta bort om ingen påfyllning planeras'
        if utanfor(h, '', uteslut_ord) and forslag in ('behåll',) and k > 0:
            skal += ' (ligger utanför utrullningen, ingen text)'
        if h not in gsc and tak is not None and forslag in ('ta bort', 'slå ihop', 'omdirigera'):
            skal += f' [saknas i sökdatafilen: högst {int(tak)} visningar, inte noll; kontrollera i Search Console före beslut]'
        ut.append(dict(handle=h, titel=r['titel'], typ=typ, koopbara=k, klick=kl, visningar=v, position=pos, forslag=forslag, skal=skal, i_gsc='ja' if h in gsc else 'nej'))
    ut.sort(key=lambda x: (-x['visningar'], x['handle']))
    return ut


def md_tabell(rader, kolumner):
    s = ['| ' + ' | '.join(k for k, _ in kolumner) + ' |', '|' + '---|' * len(kolumner)]
    for r in rader:
        s.append('| ' + ' | '.join(str(r[f]).replace('|', '/') for _, f in kolumner) + ' |')
    return '\n'.join(s)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--mapp', required=True, help='mapp med prioritering.csv, kollektioner.csv, overlappande.json')
    ap.add_argument('--gsc', required=True, help='CSV med handle, klick, visningar, position')
    ap.add_argument('--ut', required=True, help='mapp där vag2-prioritering.csv/.md och struktur-forslag.csv/.md skrivs')
    ap.add_argument('--min-visningar', type=int, default=OMDIRIGERA_FRAN_VISNINGAR)
    ap.add_argument('--uteslut-ord', default=','.join(UTESLUT_ORD))
    a = ap.parse_args(argv)
    uord = tuple(x for x in a.uteslut_ord.split(',') if x)
    gsc = lasa_gsc(a.gsc)
    prio = lasa_csv(os.path.join(a.mapp, 'prioritering.csv'))
    koll = lasa_csv(os.path.join(a.mapp, 'kollektioner.csv'))
    overl = json.load(open(os.path.join(a.mapp, 'overlappande.json'), encoding='utf-8'))
    ranka, utes = rangordna(prio, gsc, uord)
    tak = min((g['visningar'] for g in gsc.values()), default=None)
    struktur = strukturforslag(koll, overl, gsc, a.min_visningar, uord, tak)
    okanda = sorted(set(gsc) - {r['handle'] for r in prio})
    os.makedirs(a.ut, exist_ok=True)
    kol_r = [('Rang', 'rang'), ('Kollektion', 'handle'), ('Köpbara', 'koopbara'), ('Visningar', 'visningar'), ('Klick', 'klick'),
             ('Position', 'position'), ('Potential', 'potential')]
    with open(os.path.join(a.ut, 'vag2-prioritering.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(['rang', 'handle', 'titel', 'klass', 'koopbara', 'visningar', 'klick', 'position', 'potential'])
        for x in ranka:
            w.writerow([x['rang'], x['handle'], x['titel'], x['klass'], x['koopbara'], x['visningar'], x['klick'], x['position'], x['potential']])
    with open(os.path.join(a.ut, 'struktur-forslag.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(['handle', 'titel', 'typ', 'koopbara', 'visningar', 'klick', 'position', 'forslag', 'skal', 'i_gsc'])
        for x in struktur:
            w.writerow([x[k] for k in ('handle', 'titel', 'typ', 'koopbara', 'visningar', 'klick', 'position', 'forslag', 'skal', 'i_gsc')])
    ant = {}
    for x in struktur: ant[x['forslag']] = ant.get(x['forslag'], 0) + 1
    md = ['# Våg 2: rangordning efter sökdata (förslag, inget ändrat)', '',
          'Potential = visningar x närhet till position 10-30 (se skriptets huvud). Källa: Search Console, 12 månader. Beslutet är Davids.', '',
          f'Rangordnade för text: {len(ranka)}. Uteslutna: {len(utes)}. Handles i Search Console som saknas i kollektionslistan: {len(okanda)}.', '',
          md_tabell(ranka[:60], kol_r), '', '## Uteslutna med många visningar', '',
          md_tabell(sorted(utes, key=lambda x: -x['visningar'])[:25], kol_r[1:5] + [('Orsak', 'orsak')])]
    open(os.path.join(a.ut, 'vag2-prioritering.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    md2 = ['# Strukturlista sorterad efter visningar (förslag, inget ändrat)', '',
           f'{len(struktur)} kollektioner: ' + ', '.join(f'{v} {k}' for k, v in sorted(ant.items())) + '. Beslutet är Davids.', '',
           md_tabell(struktur, [('Kollektion', 'handle'), ('Typ', 'typ'), ('Köpbara', 'koopbara'), ('Visningar', 'visningar'),
                                ('Klick', 'klick'), ('Förslag', 'forslag'), ('Skäl', 'skal')])]
    open(os.path.join(a.ut, 'struktur-forslag.md'), 'w', encoding='utf-8').write('\n'.join(md2) + '\n')
    print(f'rangordnade {len(ranka)}, uteslutna {len(utes)}, struktur {len(struktur)} ({ant}), okända handles i GSC {len(okanda)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
