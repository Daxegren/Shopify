#!/usr/bin/env python3
"""Mäter granskningsutbytet per batch ur utlåtande-filerna (JSON) i vag2_skriv.

För varje batch: antal godkända / rättas / underkända, och hur rättningarna fördelar sig på
'format' (bara versaler/gemener, mellanslag eller skiljetecken ändras: kan kontrolleras av skript)
och 'innehåll' (ord, uppgifter eller betydelse ändras: kräver granskare).
Användning: mat_utbyte.py [katalog] [--md]
"""
import json, glob, os, re, sys, collections

def norm(s):
    return re.sub(r'[\W_]+', '', (s or '').lower())

def typ(fore, efter):
    if efter is None or fore is None:
        return 'innehåll'
    if norm(fore) == norm(efter):
        return 'format'
    return 'innehåll'

def main():
    kat = next((a for a in sys.argv[1:] if not a.startswith('--')), 'rapporter/facit-bos-2026-10-31/vag2_skriv')
    rader, tot = [], collections.Counter()
    for f in sorted(glob.glob(os.path.join(kat, '*utlatande*.json')), key=lambda p: (re.sub(r'\d+', '', os.path.basename(p)), int(re.findall(r'\d+', os.path.basename(p))[0]) if re.findall(r'\d+', os.path.basename(p)) else 0)):
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        if not isinstance(d, list):
            continue
        c = collections.Counter(x.get('dom', '')[:6] for x in d if isinstance(x, dict))
        fmt = inn = 0
        ch_fmt = ch_inn = 0
        prod_med_inn = prod_bara_fmt = 0
        for x in d:
            if not isinstance(x, dict) or not str(x.get('dom', '')).startswith('RÄTTA'):
                continue
            t = set()
            for fld, chs in (x.get('rattningar') or {}).items():
                for ch in (chs if isinstance(chs, list) else [chs]):
                    tt = typ(ch.get('fore'), ch.get('efter'))
                    t.add(tt)
                    if tt == 'format': ch_fmt += 1
                    else: ch_inn += 1
            fmt += 'format' in t
            inn += 'innehåll' in t
            if 'innehåll' in t: prod_med_inn += 1
            else: prod_bara_fmt += 1
        n = len(d)
        rader.append((os.path.basename(f).replace('.json', ''), n, c.get('GODKÄN', 0), c.get('RÄTTA', 0), c.get('UNDERK', 0), prod_bara_fmt, prod_med_inn))
        for k, v in zip(('n', 'god', 'ratta', 'underk', 'bara_format', 'innehall'), rader[-1][1:]):
            tot[k] += v
        tot['ch_fmt'] += ch_fmt; tot['ch_inn'] += ch_inn
    md = '--md' in sys.argv
    hdr = ('Batch', 'Utkast', 'Godk.', 'Rättas', 'Underk.', 'Rättas bara format', 'Rättas innehåll')
    if md:
        print('| ' + ' | '.join(hdr) + ' |'); print('|' + '---|' * len(hdr))
        for r in rader: print('| ' + ' | '.join(map(str, r)) + ' |')
    else:
        for r in rader: print(*r, sep='\t')
    n = tot['n'] or 1
    print(f"\nTotalt {tot['n']} utkast: {tot['god']} godkända ({100*tot['god']//n} %), {tot['ratta']} rättas ({100*tot['ratta']//n} %), {tot['underk']} underkända.")
    if tot['ratta']:
        c_all = (tot['ch_fmt'] + tot['ch_inn']) or 1
        print(f"Räknat per enskild ändring: {tot['ch_fmt']} formatändringar ({100*tot['ch_fmt']//c_all} %) och {tot['ch_inn']} innehållsändringar ({100*tot['ch_inn']//c_all} %).")
        print(f"Av de som rättas: {tot['bara_format']} bara format ({100*tot['bara_format']//tot['ratta']} %), {tot['innehall']} med innehållsrättning ({100*tot['innehall']//tot['ratta']} %).")

if __name__ == '__main__':
    main()
