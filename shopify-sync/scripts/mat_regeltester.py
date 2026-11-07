#!/usr/bin/env python3
"""Mäter hur många av granskarnas rättningar som koden hade fångat, och hur många godkända utkast som larmas felaktigt.

Underlag: rapporter/facit-bos-2026-10-31/vag2_skriv/ (*_utkast.json och *utlatande*.json). Nätverksfri.
  mat_regeltester.py            skriver hela mätrapporten (markdown) till stdout
  mat_regeltester.py --typer    bara tabellen över rättningstyper
Kontrollerna är utformade på träningsdelen (utlåtandefiler b_, c_, f_, g_) och mäts även på provdelen (h_, k_),
som inte användes när mönstren valdes. Kör med python3 -I.
"""
import collections, importlib.util, json, os, re, sys, tempfile

HAR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HAR)
import rattningstyper as rt
import regeltester as rg

FA_TROSKEL = 2.0   # högst så många procent falsklarm bland godkända utkast, i båda delarna
MIN_TACKNING = 0.3  # och minst så många procent av rättningarna fångade i minst en del

# Befintliga kontroller i skrivfil_kontroll.py (svart låda): meddelandetext -> rättningstyper de är avsedda för
GAMLA = [
    ('FEL cirkulär inledning (X är en X)', r'^cirkulär inledning', ['cirkulär inledning']),
    ('VARN meta/första meningen börjar "Namn är en/ett"', r'^(meta|första meningen) börjar', ['cirkulär inledning', 'meta/inledning saknade verb']),
    ('VARN meta saknar verb (gamla)', r'^meta saknar verb', ['meta/inledning saknade verb']),
    ('FEL liten bokstav efter kolon', r'^liten bokstav efter kolon', ['versal/gemen efter kolon']),
    ('FEL märket i versaler', r'^märket .* versaler', ['ord/märke i VERSALER']),
    ('FEL FAQ-avsnitt kopierat', r'^FAQ-avsnitt', ['FAQ-avsnitt borttaget']),
    ('VARN utfyllnaden "Finns hos BEST OF SPORTS."', r'^meta slutar med utfyllnaden', ['utfyllnaden']),
    ('FEL stor bokstav efter bindestreck', r'^stor bokstav efter bindestreck', ['versal/gemen i titel']),
    ('VARN dubbla mellanslag', r'^dubbla mellanslag', ['bindestreck, mellanslag eller skiljetecken']),
]


# Handvalda exempel per typ (annars väljs automatiskt den kortaste rättningen)
EXEMPEL = {
    'ordval (enstaka ord byts)': 'scooterhjul → sparkcykelhjul; power rack → träningsställ',
    'typord/ordval bytt i titel': 'Scooterhjul Union Dragon → Sparkcykelhjul Union Dragon',
    'mening omskriven': 'den ska inte överskrida den rekommenderade dagliga mängden → den rekommenderade dagliga mängden ska inte överskridas',
    'mening/led borttaget': 'Enligt tillverkaren ger de ett säkert grepp även i regn. → (borttaget)',
    'bindestreck, mellanslag': '27.5×2.2 → 27,5×2,2',
    'specifikationsrad borttagen': '<li>Handtag: Bekvämt handtag</li> → (borttaget)',
    'cirkulär inledning': 'Selle Monte Grappa är ett kjolskydd i svart läder → Kjolskyddet från Selle Monte Grappa är i svart läder',
    'tal/mått/uppgift ändrat': 'lastgräns "1–10 kg" fyra gånger → en gång, "enligt tillverkaren"',
    'meta/inledning saknade verb': 'Skivstångspaket med curlstång på 120 cm → Skivstångspaket BASIC har en curlstång på 120 cm',
    '"enligt tillverkaren" tillagt': 'Sadeln har en ergonomisk design → Sadeln har enligt tillverkaren en ergonomisk design',
    'böjning/stavning/grammatik': 'pakväska → packväska',
    'FAQ-avsnitt borttaget': '<h2>Vanliga frågor</h2>… → (borttaget)',
    'titel/SEO-titel kompletterad': 'Sadel Liv Contact Comfort → Sadel Liv Contact Comfort Forward',
    '"enligt tillverkaren" borttaget': 'Skydd: Mot regn, smuts och damm, enligt tillverkaren → Skydd: Regn, smuts och damm',
    'målgruppsrad': '<li>Dig som vill ha handskar med UPF-solskydd</li> → (borttaget)',
    'versal/gemen efter kolon': 'Färg: blå → Färg: Blå',
    'versal/gemen i titel': 'Skivstång, 18 mm, justerbart → …, Justerbart',
    'tum-form': '27,5 tum → 27,5-tumshjul; 7 tum skärm → 7-tums skärm',
    'tal/mått/variant ändrat i titel': 'Giant TCR Advanced 2 PC, 700x25c → …, 700c',
    'versal/gemen i löptext': 'Orange → orange',
    'ord/märke i VERSALER': 'Träningsbänk TUNTURI CT40 → Träningsbänk Tunturi CT40',
    'utfyllnaden': '… Finns hos BEST OF SPORTS. → (borttaget)',
    'ord/märke → VERSALER': 'SOKE Evo → SOKE EVO',
    'enhet i versaler': '120 PSI → 120 psi; 3.0 HP → 3,0 hk',
}


def matchar_typ(typ, lista):
    return any(p in typ for p in lista)


def las_skrivfil_kontroll():
    sp = importlib.util.spec_from_file_location('skrivfil_kontroll', os.path.join(HAR, 'skrivfil_kontroll.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    m.las_profil(os.path.join(rt.ROT, 'shopify-sync/config/butiksprofil-bestofsports.json'))
    return m


def gamla_fynd(m, d, tmp):
    json.dump([d], open(tmp, 'w', encoding='utf-8'), ensure_ascii=False)
    _, fel, varn = m.kontrollera(tmp, {}, False)
    return [x.split(': ', 1)[1] for x in fel + varn]


def delmangd(namn):
    return 'prov' if namn[0] in 'hk' else 'träning'


def tacker(fynd, kod, falt, fore):
    """Nya kontroller: fyndet ligger i samma fält och dess utdrag överlappar texten granskaren ändrade."""
    for f in fynd:
        if f.kod != kod or f.falt != falt:
            continue
        a, b = (f.text or '').lower(), (fore or '').lower()
        if a and (a in b or b in a):
            return True
    return False


def bygg_material(cfg=None):
    """En post per unik bedömning (samma utkast med samma utfall räknas en gång)."""
    cfg = cfg or rg.las_cfg()
    sk = las_skrivfil_kontroll()
    tmp = os.path.join(tempfile.mkdtemp(prefix='regeltester_'), 'x.json')
    UT = rt.las_utkast()
    mat, sett = [], set()
    for x in rt.las_utlatanden():
        d = rt.hitta_utkast(x, UT)
        if d is None:
            continue
        dom = str(x.get('dom', ''))[:6]
        nyckel = (x.get('id'), dom, json.dumps([d.get(k) for k in ('titel', 'seo_title', 'meta', 'html')], ensure_ascii=False),
                  json.dumps(x.get('rattningar'), sort_keys=True, ensure_ascii=False))
        if nyckel in sett:
            continue
        sett.add(nyckel)
        alla = [f for l, f in rg.kontrollera_utkast(d, rg_alla(cfg))]       # alla kontroller, även de som är av
        aktiva = {f.kod for l, f in rg.kontrollera_utkast(d, cfg)}           # bara de som är på
        gamla = gamla_fynd(sk, d, tmp)
        ratt = []
        if dom == 'RÄTTA':
            for fa, fo, ef in rt.rattningar(x):
                typ = rt.sortera(fa, fo, ef)
                ratt.append({'falt': fa, 'fore': fo, 'efter': ef, 'grupp': typ[0], 'typ': typ[1],
                             'nya': {k for k in rg.KONTROLLER if tacker(alla, k, fa, fo)},
                             'gamla': {n for n, pat, typer in GAMLA if matchar_typ(typ[1], typer) and any(re.search(pat, g) for g in gamla)}})
        mat.append({'utl': x['_utl'], 'id': str(x.get('id')), 'dom': dom, 'del': delmangd(x['_utl']), 'utkast': d,
                    'ratt': ratt, 'alla': alla, 'aktiva': aktiva, 'gamla': gamla})
    return mat


def gamla_ok(mat):
    """Befintliga kontroller vars falsklarm bland godkända utkast ligger under tröskeln i båda delarna."""
    ok = set()
    for namn, pat, typer in GAMLA:
        bra = True
        for d in ('träning', 'prov'):
            god = [p for p in mat if p['dom'] == 'GODKÄN' and p['del'] == d]
            n = sum(1 for p in god if any(re.search(pat, g) for g in p['gamla']))
            if 100 * n / len(god) > FA_TROSKEL:
                bra = False
        if bra:
            ok.add(namn)
    return ok


def rg_alla(cfg):
    c = json.loads(json.dumps(cfg)); c['lage'] = {}; c['standardlage'] = 'varning'
    return c


def pct(n, d):
    return f'{n} av {d} ({100 * n / d:.1f} %)' if d else '0'


def utdrag(s, n=40):
    return re.sub(r'\s+', ' ', s or '')[:n].replace('|', '/')


def tabell_typer(mat, ok_gamla):
    c, prod, ex, grupp = collections.Counter(), collections.defaultdict(set), {}, {}
    nyfang, gamfang = collections.Counter(), collections.Counter()
    for p in mat:
        for r in p['ratt']:
            t = re.sub(r' – .*$', '', r['typ'])
            c[t] += 1; prod[t].add((p['utl'], p['id'])); grupp[t] = r['grupp']
            if len(r['fore'].strip()) >= 6 and r['fore'].strip() != r['efter'].strip() and (t not in ex or len(r['fore']) < len(ex[t]['fore'])):
                ex[t] = r
            ex.setdefault(t, r)
            aktiva = {k for k in r['nya'] if k in p['aktiva']}
            if aktiva: nyfang[t] += 1
            if r['gamla'] & ok_gamla: gamfang[t] += 1
    tot = sum(c.values())
    rader = ['| Typ | Grupp | Antal | Andel | Produkter | Exempel (före → efter) | Fångas av nya tester | Fångas av gamla tester (utan brusiga) |', '|---|---|---:|---:|---:|---|---:|---:|']
    for t, n in c.most_common():
        r = ex[t]
        e = next((v for k, v in EXEMPEL.items() if t.startswith(k)), f'{utdrag(r["fore"], 55)} → {utdrag(r["efter"], 55) or "(borttaget)"}')
        rader.append(f'| {t} | {r["grupp"]} | {n} | {100 * n / tot:.1f} % | {len(prod[t])} | `{e}` | {nyfang[t]} | {gamfang[t]} |')
    rader.append(f'| **Summa** | | **{tot}** | 100 % | {len({(p["utl"], p["id"]) for p in mat if p["ratt"]})} | | **{sum(nyfang.values())}** | **{sum(gamfang.values())}** |')
    return '\n'.join(rader), tot, c


def matning(mat, ok_gamla, cfg=None):
    cfg = cfg or rg.las_cfg()
    ut = []
    god = {d: [p for p in mat if p['dom'] == 'GODKÄN' and p['del'] == d] for d in ('träning', 'prov')}
    rat = {d: [p for p in mat if p['dom'] == 'RÄTTA' and p['del'] == d] for d in ('träning', 'prov')}
    nr = {d: sum(len(p['ratt']) for p in rat[d]) for d in rat}
    ut.append(f"Bedömningar efter borttagning av dubbletter: {len(mat)} (godkända {sum(len(v) for v in god.values())}, rättade {sum(len(v) for v in rat.values())}, övriga underkända/avvisade {len(mat) - sum(len(v) for v in god.values()) - sum(len(v) for v in rat.values())}). "
              f"Träningsdel (utlåtandefiler b_, c_, f_, g_): {len(god['träning'])} godkända, {len(rat['träning'])} rättade ({nr['träning']} enskilda rättningar). "
              f"Provdel (h_, k_): {len(god['prov'])} godkända, {len(rat['prov'])} rättade ({nr['prov']} enskilda rättningar).\n")
    ut.append(f'Tröskel för att en ny kontroll får vara på: högst {FA_TROSKEL:.0f} % falsklarm bland godkända utkast i både träningsdelen och provdelen, och minst {MIN_TACKNING} % av rättningarna fångade i minst en av delarna.\n')
    ut.append('### Nya kontroller (regeltester.py)\n')
    ut.append('| Kontroll | Regel | Läge nu | Fångar rättningar (träning) | Fångar rättningar (prov) | Falsklarm godkända (träning) | Falsklarm godkända (prov) | Larm på rättade utkast (prov) | Tröskel |')
    ut.append('|---|---|---|---:|---:|---:|---:|---:|---|')
    for kod, fn in rg.KONTROLLER.items():
        cell, fa_pct, tack = [], [], []
        for d in ('träning', 'prov'):
            n = sum(1 for p in rat[d] for r in p['ratt'] if kod in r['nya'])
            tack.append(100 * n / nr[d]); cell.append(pct(n, nr[d]))
        for d in ('träning', 'prov'):
            n = sum(1 for p in god[d] if any(f.kod == kod for f in p['alla']))
            fa_pct.append(100 * n / len(god[d])); cell.append(pct(n, len(god[d])))
        n = sum(1 for p in rat['prov'] if any(f.kod == kod for f in p['alla']))
        cell.append(pct(n, len(rat['prov'])))
        ok = max(fa_pct) <= FA_TROSKEL and max(tack) >= MIN_TACKNING
        lage = rg.lage_for(kod, cfg)
        ut.append(f'| `{kod}` | {fn.regel} | {lage} | ' + ' | '.join(cell) + f' | {"klarar" if ok else "klarar inte"} |')
    ut.append('\n### Befintliga kontroller i skrivfil_kontroll.py (oförändrade; svart låda)\n')
    ut.append('Täckning räknas på typnivå: kontrollen larmar på utkastet och rättningen är av den typ kontrollen är avsedd för. Falsklarm = larm på godkända utkast. '
              'Obs: i de senare batcherna (k_) kördes dessa kontroller redan före granskningen, så rättningar de hade fångat finns inte kvar i facit; täckningen är därför en underskattning.\n')
    ut.append('| Kontroll | Fångar rättningar (träning) | Fångar rättningar (prov) | Falsklarm godkända (träning) | Falsklarm godkända (prov) | Larm på rättade utkast (prov) |')
    ut.append('|---|---:|---:|---:|---:|---:|')
    for namn, pat, typer in GAMLA:
        def larm(p): return any(re.search(pat, g) for g in p['gamla'])
        cell = []
        for d in ('träning', 'prov'):
            cell.append(pct(sum(1 for p in rat[d] for r in p['ratt'] if namn in r['gamla']), nr[d]))
        for d in ('träning', 'prov'):
            cell.append(pct(sum(1 for p in god[d] if larm(p)), len(god[d])))
        cell.append(pct(sum(1 for p in rat['prov'] if larm(p)), len(rat['prov'])))
        ut.append(f'| {namn} | ' + ' | '.join(cell) + ' |')
    # ---- totalt ----
    ut.append('\n### Totalt: andel av granskarnas rättningar som koden hade fångat\n')
    ut.append('Nya tester = bara kontroller som är på (läge varning eller fel). Gamla tester = kontrollerna i tabellen ovan som själva klarar falsklarmströskeln (' + ', '.join(sorted(ok_gamla)) + '); de brusiga räknas inte med. Fångat = en kontroll larmar på rätt ställe (nya) eller av rätt typ (gamla).\n')
    ut.append('| Mått | Träning | Prov | Alla |')
    ut.append('|---|---:|---:|---:|')
    def tot(fn_ratt, fn_prod_min, fn_prod_alla):
        rader = []
        return rader
    def fang_ny(p, r): return any(k in p['aktiva'] and k in r['nya'] for k in r['nya'])
    def fang_gam(r): return bool(r['gamla'] & ok_gamla)
    def fang_bada(p, r): return fang_ny(p, r) or fang_gam(r)
    def rad(titel, fn):
        v = []
        for d in ('träning', 'prov'):
            v.append(fn([p for p in rat[d]]))
        v.append(fn(rat['träning'] + rat['prov']))
        ut.append(f'| {titel} | ' + ' | '.join(v) + ' |')
    rad('Rättningar fångade av nya tester', lambda L: pct(sum(1 for p in L for r in p['ratt'] if fang_ny(p, r)), sum(len(p['ratt']) for p in L)))
    rad('Rättningar fångade av gamla tester', lambda L: pct(sum(1 for p in L for r in p['ratt'] if fang_gam(r)), sum(len(p['ratt']) for p in L)))
    rad('Rättningar fångade av nya eller gamla', lambda L: pct(sum(1 for p in L for r in p['ratt'] if fang_bada(p, r)), sum(len(p['ratt']) for p in L)))
    rad('Rättade produkter där minst en rättning fångas (nya)', lambda L: pct(sum(1 for p in L if any(fang_ny(p, r) for r in p['ratt'])), len(L)))
    rad('Rättade produkter där alla rättningar fångas (nya)', lambda L: pct(sum(1 for p in L if p['ratt'] and all(fang_ny(p, r) for r in p['ratt'])), len(L)))
    rad('Rättade produkter där alla rättningar fångas (nya eller gamla)', lambda L: pct(sum(1 for p in L if p['ratt'] and all(fang_bada(p, r) for r in p['ratt'])), len(L)))
    v = []
    for d in ('träning', 'prov'):
        v.append(pct(sum(1 for p in god[d] if p['aktiva'] & {f.kod for f in p['alla']}), len(god[d])))
    v.append(pct(sum(1 for d in ('träning', 'prov') for p in god[d] if p['aktiva'] & {f.kod for f in p['alla']}), sum(len(god[d]) for d in god)))
    ut.append('| Godkända utkast som får minst ett larm från nya tester (falsklarm) | ' + ' | '.join(v) + ' |')
    return '\n'.join(ut)


if __name__ == '__main__':
    a = sys.argv[1:]
    cfg = rg.las_cfg()
    mat = bygg_material(cfg)
    if '--typer' in a:
        t, n, _ = tabell_typer([p for p in mat if p['ratt']], gamla_ok(mat))
        print(t)
    else:
        ok = gamla_ok(mat)
        print('## Rättningstyper\n'); t, n, _ = tabell_typer([p for p in mat if p['ratt']], ok); print(t)
        print('\n## Mätning\n'); print(matning(mat, ok, cfg))
