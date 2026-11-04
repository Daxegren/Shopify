#!/usr/bin/env python3
"""Mäter trend och regelfördelning i granskningsutlåtandena (kompletterar mat_utbyte.py).

Ordnar utlåtandena kronologiskt (första commit per fil), delar in dem i lika stora delar och
redovisar andel godkända direkt, rättningar per utkast samt vilka regler (R-koder ur regelboken)
som rättningarna hör till. Klassningen utgår från VAD som ändrades (före -> efter), inte från granskarens
motivering: ett stickprov visade att nyckelord i 'skal' träffar beskrivande text och ger låg precision.
Rättningarna är textfragment (inte hela fält), så längd och verb i metan kan inte avgöras här; typerna är grova och 'övrigt' redovisas. Användning: mat_regler.py [katalog] [--delar N]
"""
import json, glob, os, re, subprocess, sys, collections

TYPER = {  # typ: (närmaste regel, styrs idag av)
    'format (versaler/enheter/skiljetecken)': ('R8-R10', 'T'),
    'lastgräns/maxvikt ändrad': ('R4', 'G (delvis T)'),
    'påståendeord / enligt tillverkaren': ('R5', 'G (T för antal, R22 varnar)'),
    'meta: utfyllnad borttagen': ('R12', 'T (varning)'),
    'meta: innehåll ändrat': ('R11/R12', 'G/T'),
    'titel/SEO-titel: innehåll ändrat': ('R7/R12', 'G/T'),
    'uppgift struken (stöds inte av källan)': ('R1-R3', 'G'),
    'övrigt innehåll (språk, formulering, fakta)': ('R2/R11', 'G'),
}
LAST = re.compile(r'lastkapacitet|maxvikt|användarvikt|max\.? ?vikt|belastning|bär upp|driftsvikt|lastgräns', re.I)
PAAST = re.compile(r'slitstark|robust|halkfri|halkskydd|stödjer|skyddar|enligt tillverkaren|säker', re.I)

def norm(t): return re.sub(r'[\W_]+', '', (t or '').lower())

def andringstyp(fld, fore, efter):
    fore, efter = fore or '', efter or ''
    if fore and efter and norm(fore) == norm(efter): return 'format (versaler/enheter/skiljetecken)'
    if LAST.search(fore) or LAST.search(efter): return 'lastgräns/maxvikt ändrad'
    if bool(PAAST.search(fore)) != bool(PAAST.search(efter)): return 'påståendeord / enligt tillverkaren'
    if fld == 'meta':
        return 'meta: utfyllnad borttagen' if 'Finns hos' in fore else 'meta: innehåll ändrat'
    if fld in ('titel', 'seo_title'): return 'titel/SEO-titel: innehåll ändrat'
    if fore and (not efter or len(efter) < len(fore) * 0.6) and re.search(r'\d', fore): return 'uppgift struken (stöds inte av källan)'
    return 'övrigt innehåll (språk, formulering, fakta)'

def kronologi(kat):
    ut = subprocess.run(['git', 'log', '--reverse', '--diff-filter=A', '--name-only', '--format=@%ct', '--', kat],
                        capture_output=True, text=True).stdout.split('\n')
    order, t = {}, 0
    for l in ut:
        if l.startswith('@'): t = int(l[1:])
        elif l.strip() and 'utlatande' in l and l.endswith('.json') and l not in order: order[l] = t
    return order

def main():
    a = sys.argv[1:]
    delar = 4
    if '--delar' in a:
        k = a.index('--delar'); delar = int(a[k + 1]); del a[k:k + 2]
    kat = a[0] if a else 'rapporter/facit-bos-2026-10-31/vag2_skriv'
    order = kronologi(kat)
    filer = sorted(glob.glob(os.path.join(kat, '*utlatande*.json')), key=lambda p: (order.get(p, 1 << 60), p))
    poster = []
    for f in filer:
        try: d = json.load(open(f, encoding='utf-8'))
        except Exception: continue
        if isinstance(d, list):
            poster += [(f, x) for x in d if isinstance(x, dict) and x.get('dom')]
    n = len(poster)
    print(f'{len(filer)} utlåtandefiler, {n} bedömda utkast (kronologisk ordning efter första commit).\n')
    print('## Trend (lika stora delar i tidsordning)')
    print('| Del | Utkast | Godkända direkt | Rättas | Underkända | Fälträttningar per utkast |')
    print('|---|---|---|---|---|---|')
    steg = max(1, n // delar)
    for i in range(delar):
        s = poster[i * steg: (i + 1) * steg if i < delar - 1 else n]
        c = collections.Counter(x['dom'][:6] for _, x in s)
        ch = sum(len(v if isinstance(v, list) else [v]) for _, x in s for v in (x.get('rattningar') or {}).values())
        m = len(s) or 1
        print(f'| {i + 1} | {len(s)} | {c["GODKÄN"]} ({100 * c["GODKÄN"] // m} %) | {c["RÄTTA"]} ({100 * c["RÄTTA"] // m} %) | {c["UNDERK"]} ({100 * c["UNDERK"] // m} %) | {ch / m:.2f} |')
    print('\n## Rättningar per fält (antal enskilda ändringar)')
    fc = collections.Counter()
    for _, x in poster:
        for fld, v in (x.get('rattningar') or {}).items():
            fc[fld] += len(v if isinstance(v, list) else [v])
    for fld, v in fc.most_common(): print(f'- {fld}: {v}')
    print('\n## Typ av ändring (enskilda före -> efter-rättningar; första träffande typ i listan)')
    ct = collections.Counter(); utk = collections.defaultdict(set); ex = collections.defaultdict(list)
    for idx, (f, x) in enumerate(poster):
        for fld, v in (x.get('rattningar') or {}).items():
            for ch in (v if isinstance(v, list) else [v]):
                if not isinstance(ch, dict): continue
                t = andringstyp(fld, ch.get('fore'), ch.get('efter'))
                ct[t] += 1; utk[t].add(idx)
                if len(ex[t]) < 3: ex[t].append(f"{(ch.get('fore') or '')[:60]!r} -> {(ch.get('efter') or '')[:60]!r}")
    tot = sum(ct.values()) or 1
    print('| Typ | Närmaste regel | Styrs idag av | Ändringar | Andel | Utkast berörda |'); print('|---|---|---|---|---|---|')
    for t, v in ct.most_common():
        r, st = TYPER.get(t, ('-', '-'))
        print(f'| {t} | {r} | {st} | {v} | {100 * v // tot} % | {len(utk[t])} |')
    print('\n## Exempel per typ')
    for t, e in ex.items():
        print(f'- {t}:'); [print('   ', y) for y in e]

if __name__ == '__main__':
    main()
