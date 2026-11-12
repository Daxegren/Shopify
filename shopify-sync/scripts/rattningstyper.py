#!/usr/bin/env python3
"""Läser granskarutlåtanden (vag2_skriv/*utlatande*.json) och sorterar varje enskild rättning (före/efter) efter typ.

Underlag för shopify-sync/scripts/mat_regeltester.py. Nätverksfri. Sorteringen är heuristisk (regler på före/efter-texten);
en rättning får exakt en typ. Typkoden F = format (bara tecken/skiljetecken/versaler), I = innehåll (ord, påståenden, grammatik).
"""
import collections, difflib, glob, json, os, re

ROT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
KAT = os.path.join(ROT, 'rapporter', 'facit-bos-2026-10-31', 'vag2_skriv')

VERB = r'\b(är|har|ger|passar|finns|väger|mäter|består|används|kan|ingår|erbjuder|levereras|säljs|tillverkad|tillverkade|gör|hjälper|följer|innehåller|fungerar|rymmer|kommer|med)\b'
KVALITETSORD = r'slitstark|slitstyrk|robust|hållbar|tålig|kvalitet|halkfri|halkskydd|stabil|säker|skyddar|skydd\b|stödjer|stöd för'
LASTORD = r'maxvikt|max\.? ?vikt|belastning|lastgräns|lastkapacitet|användarvikt|bärförmåga|klarar upp till'
EFFEKTORD = r'effekt|muskel|stärk|rehab|smärt|hälsa|lindr|förbättr|träningsresultat|ryggbesvär|återhämtning'


def norm(s):
    return re.sub(r'[\W_]+', '', (s or '').lower())


def faltnamn(k):
    return 'seo_title' if k.startswith('seo') else k.split()[0].split('_')[0]


def ordskillnad(f, e):
    """Returnerar (borttaget, tillagt, likhet) på ordnivå."""
    a = re.findall(r'\w+|[^\w\s]|\s+', f); b = re.findall(r'\w+|[^\w\s]|\s+', e)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    rem, add = [], []
    for t, i1, i2, j1, j2 in sm.get_opcodes():
        if t != 'equal':
            rem.append(''.join(a[i1:i2])); add.append(''.join(b[j1:j2]))
    return ' '.join(rem), ' '.join(add), sm.ratio()


def sortera(falt, fore, efter):
    """Returnerar (grupp, typ) för en rättning."""
    falt = faltnamn(falt); f = fore or ''; e = efter or ''
    R, A, ratio = ordskillnad(f, e)
    # --- format ---
    if re.search(r'\d(?:,\d)? tums?\b', f) and re.search(r'\d(?:,\d)?-tum', e):
        return 'F', 'tum-form (N tum → N-tums)'
    if '&' in f and '&' not in e:
        return 'F', '"&" → "och"'
    if norm(f) == norm(e):
        if f.lower() == e.lower():
            if re.search(r'\b(PSI|HK|HP|KG|CM|MM|KM/H)\b', f):
                return 'F', 'enhet i versaler (psi, hk, kg …)'
            if re.search(r'\b[A-ZÅÄÖ]{3,}\b', f) and not re.search(r'\b[A-ZÅÄÖ]{3,}\b', e):
                return 'F', 'ord/märke i VERSALER → normal skrivning'
            if re.search(r'\b[A-ZÅÄÖ]{3,}\b', e) and not re.search(r'\b[A-ZÅÄÖ]{3,}\b', f):
                return 'F', 'ord/märke → VERSALER'
            if re.search(r'(<li>[^<:]{1,40}:|/)\s*[a-zåäö]', f) or re.search(r'(<li>[^<:]{1,40}:|/)\s*[A-ZÅÄÖ]', e):
                return 'F', 'versal/gemen efter kolon eller snedstreck i specifikationsrad'
            if falt in ('titel', 'seo_title'):
                return 'F', 'versal/gemen i titel eller SEO-titel'
            return 'F', 'versal/gemen i löptext'
        return 'F', 'bindestreck, mellanslag eller skiljetecken'
    # --- borttagningar ---
    if not e.strip() or not A.strip():
        if re.search(r'Vanliga frågor|<h3>', f):
            return 'I', 'FAQ-avsnitt borttaget'
        if re.search(r'Finns hos BEST OF SPORTS', R):
            return 'I', 'utfyllnaden "Finns hos BEST OF SPORTS." borttagen'
        if re.search(r'Beställningsvaror kan ta upp till en vecka längre', R):
            return 'I', 'leveranstidsmening (R13) borttagen'
        if re.match(r'\s*<li>', f) or '<li>' in f[:6]:
            if re.search(r'Dig som|Lämplig för', f):
                return 'I', 'målgruppsrad ("Dig som …") borttagen'
            sub = _bort_typ(R + ' ' + f)
            return 'I', 'specifikationsrad borttagen' + sub
        return 'I', 'mening/led borttaget' + _bort_typ(R + ' ' + f)
    # --- tillägg ---
    if re.search(r'Beställningsvaror kan ta upp till en vecka längre', A) and 'Beställningsvaror' not in f:
        return 'I', 'leveranstidsmening (R13) tillagd'
    if re.search(r'enligt tillverkaren', A, re.I) and not re.search(r'enligt tillverkaren', R, re.I):
        return 'I', '"enligt tillverkaren" tillagt (R4/R5)'
    if re.search(r'enligt tillverkaren', R, re.I) and not re.search(r'enligt tillverkaren', A, re.I):
        return 'I', '"enligt tillverkaren" borttaget/omformulerat (R4/R5)'
    # --- omskrivningar ---
    if falt == 'meta' and re.search(VERB, e[:90], re.I) and not re.search(VERB, f, re.I):
        return 'I', 'meta/inledning saknade verb (R11)'
    if re.match(r'^(<p>)?[^.<]{0,80}? är (en|ett) ', f) and not re.match(r'^(<p>)?[^.<]{0,80}? är (en|ett) ', e) and falt in ('meta', 'html'):
        return 'I', 'cirkulär inledning "X är en/ett …" omskriven (R11)'
    if re.search(r'^[^.]{0,80} med ', f) and falt == 'meta' and re.search(r'\b(har|ger|innehåller|väger|mäter)\b', A):
        return 'I', 'meta/inledning saknade verb (R11)'
    ta = A.split(); tr = R.split()
    siffror_f = re.findall(r'\d+(?:[.,]\d+)?', f); siffror_e = re.findall(r'\d+(?:[.,]\d+)?', e)
    if falt in ('titel', 'seo_title'):
        if not R.strip() or (len(tr) == 0):
            return 'I', 'titel/SEO-titel kompletterad (ord tillagt)'
        if len(tr) <= 3 and len(ta) <= 4 and not re.search(r'\d', R + A):
            return 'I', 'typord/ordval bytt i titel eller SEO-titel (R7)'
        if re.search(r'\d', R + A):
            return 'I', 'tal/mått/variant ändrat i titel eller SEO-titel'
        return 'I', 'titel/SEO-titel omskriven'
    if sorted(siffror_f) != sorted(siffror_e):
        return 'I', 'tal/mått/uppgift ändrat'
    if len(tr) <= 3 and len(ta) <= 3:
        tf = f.split(); te = e.split()
        if re.fullmatch(r'\w+', R.strip() or 'x') and re.fullmatch(r'\w+', A.strip() or 'x') and difflib.SequenceMatcher(None, R, A).ratio() >= 0.7:
            return 'I', 'böjning/stavning/grammatik (ett ord)'
        if re.search(r'\b(en|ett)\b', R) and re.search(r'\b(en|ett)\b', A):
            return 'I', 'böjning/stavning/grammatik (ett ord)'
        return 'I', 'ordval (enstaka ord byts)'
    if len(ta) > 3 * max(len(tr), 1):
        return 'I', 'text tillagd/utökad'
    return 'I', 'mening omskriven'


def _bort_typ(t):
    if re.search(LASTORD, t, re.I): return ' – lastgräns/vikt'
    if re.search(EFFEKTORD, t, re.I): return ' – effekt/hälsa'
    if re.search(KVALITETSORD, t, re.I): return ' – säkerhet/kvalitet'
    return ''


def las_utlatanden(kat=KAT):
    ut = []
    for f in sorted(glob.glob(os.path.join(kat, '*utlatande*.json'))):
        b = os.path.basename(f)
        if b.startswith('test_'):  # test av Sonnet som granskare, inget facit
            continue
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        for x in d:
            if isinstance(x, dict):
                x['_utl'] = b; ut.append(x)
    return ut


def las_utkast(kat=KAT):
    u = collections.defaultdict(list)
    for f in sorted(glob.glob(os.path.join(kat, '*_utkast.json'))):
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        if isinstance(d, list):
            for x in d:
                if isinstance(x, dict) and x.get('id') is not None:
                    u[str(x['id'])].append((os.path.basename(f), x))
    return u


def hitta_utkast(x, utkast):
    """Utkastet som granskaren bedömde (samma id, helst i filen som utlåtandet anger; vid rättning: det där alla 'före' finns)."""
    kand = utkast.get(str(x.get('id')), [])
    if x.get('fil'):
        k2 = [c for c in kand if c[0] == x['fil']]
        kand = k2 or kand
    if len(kand) <= 1:
        return kand[0][1] if kand else None
    ratt = x.get('rattningar') or {}
    for _, d in kand:
        if all(ch.get('fore') in (d.get(faltnamn(k)) or '') for k, cs in ratt.items() for ch in (cs if isinstance(cs, list) else [cs])):
            return d
    return kand[0][1]


def rattningar(x):
    """Yield (fältnamn, fore, efter) för en RÄTTA-post."""
    for k, cs in (x.get('rattningar') or {}).items():
        for ch in (cs if isinstance(cs, list) else [cs]):
            if isinstance(ch, dict) and ch.get('fore') is not None:
                yield faltnamn(k), ch['fore'], ch.get('efter') or ''


if __name__ == '__main__':
    c = collections.Counter()
    for x in las_utlatanden():
        if str(x.get('dom', '')).startswith('RÄTTA'):
            for fa, fo, ef in rattningar(x):
                c[sortera(fa, fo, ef)] += 1
    for (g, t), n in c.most_common():
        print(n, g, t)
