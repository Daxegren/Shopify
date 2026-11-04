#!/usr/bin/env python3
"""Genererar shopify-sync/status/bestofsports-textutrullning.md ur filerna i vag2_skriv.

Stegen per batch: in-fil → utkast → utlåtande → skrivfil → skrivrapport (= skriven i butiken).
Öppna frågor läses ur shopify-sync/status/oppna_fragor.json (underhålls för hand; poster tas aldrig bort, bara status ändras).
Användning: status_uppdatera.py
"""
import json, glob, os, re, datetime

ROT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
D = os.path.join(ROT, 'rapporter/facit-bos-2026-10-31/vag2_skriv')
G = os.path.join(ROT, 'rapporter/facit-bos-2026-10-31/granskning')
UT = os.path.join(ROT, 'shopify-sync/status/bestofsports-textutrullning.md')
FR = os.path.join(ROT, 'shopify-sync/status/oppna_fragor.json')


# f_16–f_25 ersattes 2026-11-04 av g_1–g_4 och h_1–h_7 (nya batcher efter att spärrade produkter hanterats)
ERSATTA = {('f', str(i)) for i in range(16, 26)}


def lad(p):
    try:
        return json.load(open(p, encoding='utf-8'))
    except Exception:
        return None


def n(p):
    d = lad(p)
    return len(d) if isinstance(d, list) else None


def batcher():
    nycklar = set()
    for p in glob.glob(os.path.join(D, '[fgh]_*_in.json')):
        m = re.match(r'([fgh])_(x?\d+)_in\.json', os.path.basename(p))
        if m and (m.group(1), m.group(2)) not in ERSATTA:
            nycklar.add((m.group(1), m.group(2)))
    ordning = {'f': 0, 'g': 1, 'h': 2}
    return sorted(nycklar, key=lambda t: (ordning[t[0]], int(t[1].lstrip('x') or 0) + (1000 if t[1].startswith('x') else 0)))


def main():
    rader, tot = [], dict(in_=0, skriven=0, avvisad=0)
    for pre, i in batcher():
        k = f'{pre}_{i}'
        inn = n(f'{D}/{k}_in.json')
        ut = n(f'{D}/{k}_utkast.json')
        av = n(f'{D}/{k}_avvisade.json') or 0
        utl = lad(f'{D}/{pre}_utlatande_{i}.json')
        dom = ''
        if isinstance(utl, list):
            dom = '/'.join(str(sum(1 for x in utl if str(x.get('dom', '')).startswith(p))) for p in ('GODK', 'RÄTTA', 'UNDERK'))
        # skrivfiler: huvudfil, men f_14/f_15 delas i ok+rest; fix-filer är delmängder
        filer = [f'{D}/{k.replace("_", "_skriv_")}.json'] if pre != 'f' else [f'{D}/f_skriv_{i}.json']
        if pre == 'f' and i in ('14', '15'):
            filer = [f'{D}/f_skriv_{i}ok.json', f'{D}/f_skriv_{i}rest.json']
        if pre == 'g': filer = [f'{D}/g_skriv_{i}.json']
        if pre == 'h': filer = [f'{D}/h_skriv_{i}.json']
        sk = sum(n(x) or 0 for x in filer)
        rapp = glob.glob(f'{G}/{k}_*skrivrapport.md') + glob.glob(f'{G}/{k}ok_*skrivrapport.md') + glob.glob(f'{G}/{k}rest_*skrivrapport.md')
        steg = 'in' if inn else ''
        if ut is not None: steg = 'utkast'
        if dom: steg = 'granskad'
        if sk: steg = 'skrivfil'
        if rapp: steg = 'skriven'
        rader.append((k, inn, ut, av, dom, sk, steg))
        tot['in_'] += inn or 0
        tot['avvisad'] += av
        if steg == 'skriven': tot['skriven'] += sk
    fr = lad(FR) or []
    rader_md = '\n'.join(f'| {k} | {inn} | {ut if ut is not None else ""} | {av} | {dom} | {sk or ""} | {steg} |' for k, inn, ut, av, dom, sk, steg in rader)
    oppna = [x for x in fr if x.get('status') != 'avklarad']
    fr_md = '\n'.join(f"- {x['id']} ({x['datum']}): {x['fraga']}" for x in oppna) or '- (inga)'
    text = f"""# Textutrullning BEST OF SPORTS – status

Genereras av `shopify-sync/scripts/status_uppdatera.py` ({datetime.date.today().isoformat()}). Redigera inte för hand; öppna frågor ligger i `oppna_fragor.json`.
Regler: `shopify-sync/regler/regler-v1.md`. Beslut: `shopify-sync/docs/BESLUTSLOGG.md`. Profil: `shopify-sync/config/butiksprofil-bestofsports.json`.

**Fitnessgruppen:** {tot['skriven']} produkter skrivna och verifierade i batcherna nedan (utöver tidigare vågor). Avvisade i batcherna: {tot['avvisad']}.

| Batch | Inventerade | Utkast | Avvisade | Dom (godk/rättas/underk) | Skrivfil | Steg |
|---|---|---|---|---|---|---|
{rader_md}

Steg: in → utkast → granskad → skrivfil → skriven (skrivrapport finns). f_x1 och fix-filer (f_*fix) ingår i huvudbatcherna.

## Öppna frågor till David
{fr_md}
"""
    os.makedirs(os.path.dirname(UT), exist_ok=True)
    open(UT, 'w', encoding='utf-8').write(text)
    print(text[:1500])


if __name__ == '__main__':
    main()
