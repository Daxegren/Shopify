#!/usr/bin/env python3
"""Genererar butikens statusfil (BEST OF SPORTS: shopify-sync/status/bestofsports-textutrullning.md)
ur batchfilerna i butikens arbetskatalog (BEST OF SPORTS: vag2_skriv).

Stegen per batch: in-fil → utkast → utlåtande → skrivfil → skrivrapport (= skriven i butiken).
Öppna frågor läses ur profilens `oppna_fragor` (underhålls för hand; poster tas aldrig bort, bara status ändras).
Batchprefix (f, g, h …), ersatta batcher, delade skrivfiler, kataloger och statusfil kommer från butiksprofilen.
Användning: status_uppdatera.py [--profil BUTIKSPROFIL.json]   (standard: BEST OF SPORTS)
"""
import json, glob, os, re, datetime, sys

HAR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HAR)
import butiksprofil  # noqa: E402

ROT = butiksprofil.ROT


def lad(p):
    try:
        with open(p, encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None


def n(p):
    d = lad(p)
    return len(d) if isinstance(d, list) else None


def batcher(D, prefix, ersatta):
    """Batchnycklar (prefix, nummer) i prefixens ordning. ersatta: mängd av 'f_16'-liknande namn."""
    nycklar = set()
    alt = '|'.join(re.escape(p) for p in prefix)
    for p in glob.glob(os.path.join(D, '*_in.json')):
        m = re.match(r'(%s)_(x?\d+)_in\.json' % alt, os.path.basename(p))
        if m and f'{m.group(1)}_{m.group(2)}' not in ersatta:
            nycklar.add((m.group(1), m.group(2)))
    ordning = {p: n for n, p in enumerate(prefix)}
    return sorted(nycklar, key=lambda t: (ordning[t[0]], int(t[1].lstrip('x') or 0) + (1000 if t[1].startswith('x') else 0)))


def skrivfiler(D, pre, i, delade):
    """Skrivfilerna för en batch: huvudfilen, eller <batch>ok + <batch>rest för delade batcher."""
    if f'{pre}_{i}' in delade:
        return [f'{D}/{pre}_skriv_{i}ok.json', f'{D}/{pre}_skriv_{i}rest.json']
    return [f'{D}/{pre}_skriv_{i}.json']


def bygg_status(profil, idag=None):
    """Returnerar (statustext, sökväg till statusfilen). Skriver ingenting."""
    D = butiksprofil.i_rot(profil, 'arbetskatalog')
    G = butiksprofil.i_rot(profil, 'granskningskatalog')
    UT = butiksprofil.i_rot(profil, 'statusfil')
    FR = butiksprofil.i_rot(profil, 'oppna_fragor')
    prefix = profil['filprefix']
    ersatta = set(profil.get('ersatta_batcher') or [])
    delade = set(profil.get('delade_skrivfiler') or [])
    rader, tot = [], dict(in_=0, skriven=0, avvisad=0)
    for pre, i in batcher(D, prefix, ersatta):
        k = f'{pre}_{i}'
        inn = n(f'{D}/{k}_in.json')
        ut = n(f'{D}/{k}_utkast.json')
        av = n(f'{D}/{k}_avvisade.json') or 0
        utl = lad(f'{D}/{pre}_utlatande_{i}.json')
        dom = ''
        if isinstance(utl, list):
            dom = '/'.join(str(sum(1 for x in utl if str(x.get('dom', '')).startswith(p))) for p in ('GODK', 'RÄTTA', 'UNDERK'))
        # skrivfiler: huvudfil, men delade batcher (profilen) har ok+rest; fix-filer är delmängder
        filer = skrivfiler(D, pre, i, delade)
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
    fr = (lad(FR) if FR else None) or []
    rader_md = '\n'.join(f'| {k} | {inn} | {ut if ut is not None else ""} | {av} | {dom} | {sk or ""} | {steg} |' for k, inn, ut, av, dom, sk, steg in rader)
    oppna = [x for x in fr if x.get('status') != 'avklarad']
    fr_md = '\n'.join(f"- {x['id']} ({x['datum']}): {x['fraga']}" for x in oppna) or '- (inga)'
    idag = idag or datetime.date.today().isoformat()
    fr_namn = os.path.basename(FR) if FR else 'oppna_fragor.json'
    text = f"""# Textutrullning {profil['butiksnamn']} – status

Genereras av `shopify-sync/scripts/status_uppdatera.py` ({idag}). Redigera inte för hand; öppna frågor ligger i `{fr_namn}`.
Regler: `{profil['regelbok']}`. Beslut: `{profil['beslutslogg']}`. Profil: `{butiksprofil.relativ_sokvag(profil)}`.

**{profil['statusgrupp']}:** {tot['skriven']} produkter skrivna och verifierade i batcherna nedan (utöver tidigare vågor). Avvisade i batcherna: {tot['avvisad']}.

| Batch | Inventerade | Utkast | Avvisade | Dom (godk/rättas/underk) | Skrivfil | Steg |
|---|---|---|---|---|---|---|
{rader_md}

Steg: in → utkast → granskad → skrivfil → skriven (skrivrapport finns). f_x1 och fix-filer (f_*fix) ingår i huvudbatcherna.

## Öppna frågor till David
{fr_md}
"""
    return text, UT


def main(argv=None):
    try:
        profil, rest = butiksprofil.profil_fran_argv(argv if argv is not None else sys.argv[1:])
    except butiksprofil.ProfilFel as e:
        print('FEL:', e); return 1
    if rest:
        print(__doc__); return 2
    text, UT = bygg_status(profil)
    os.makedirs(os.path.dirname(UT), exist_ok=True)
    open(UT, 'w', encoding='utf-8').write(text)
    print(text[:1500])
    return 0


if __name__ == '__main__':
    sys.exit(main())
