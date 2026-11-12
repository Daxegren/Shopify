#!/usr/bin/env python3
"""Underlag för rensning 2 (F2): lastgränser utan "enligt tillverkaren" i BEST OF SPORTS.

LÄSER BARA repots egna filer (skrivfiler, utkast, spärrlista). Inget nätverk, ingen Shopify, inga nycklar.
Skriver: rapporter/rensning-2-underlag-<datum>.md och rapporter/facit-bos-2026-10-31/vag2_skriv/rensning2_forslag.json
(+ en temporär kontrollfil i --tmp som skrivfil_kontroll.py läser).

Senast skrivna version per produkt = senaste skrivfilen (korrigeringar och k_skriv_rens2 väger tyngre än originalen),
med metarensning 1 och 3 samt kort_meta påförda. Det är repots bild; live kan avvika (kräver live-klassning före skrivning).
Användning: rensning2_underlag.py [--datum ÅÅÅÅ-MM-DD] [--tmp KATALOG]
"""
import collections, csv, datetime, glob, json, os, re, subprocess, sys

HAR = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.abspath(os.path.join(HAR, '..', '..'))
V = os.path.join(ROT, 'rapporter', 'facit-bos-2026-10-31', 'vag2_skriv') + os.sep
sys.path.insert(0, HAR)
from skrivfil_kontroll import las_sparr, las_profil  # noqa: E402

FRAS = 'enligt tillverkaren'

# ---------------------------------------------------------------- inläsning
AGGREGAT = {'k_skriv.json', 'c_skriv.json', 'c_skriv_resten.json', 'k_skriv_3.json', 'b_skriv_13.json',
            'b_skriv_14.json', 'b_skriv.json', 'a_skriv.json'}


def skrivfiler():
    fs = [os.path.basename(f) for f in glob.glob(V + '*.json')]
    fs = [f for f in fs if 'skriv' in f and not re.search(r'utkast|_in\.|avvisade|utlatande|prompt|kandidat|test_', f)
          and f != 'kort_meta_skriv.json']

    def tier(f):
        if f in AGGREGAT: return 0
        if f == 'k_skriv_rens2.json': return 3
        if re.search(r'fix|rest\.|rest_|ok\.|korr|kanarie', f) and not f.startswith('c_skriv_resten'): return 2
        return 1
    return sorted(fs, key=lambda f: (tier(f), f))


def bygg():
    cur, src = {}, {}
    for f in skrivfiler():
        d = json.load(open(V + f, encoding='utf-8'))
        if not isinstance(d, list) or not d or 'html' not in d[0]:
            continue
        for x in d:
            cur[str(x['id'])] = x; src[str(x['id'])] = f
    ov = {}
    for f in ('kort_meta_skriv.json', 'meta_rensning.json', 'meta_rensning3.json'):
        for x in json.load(open(V + f, encoding='utf-8')):
            m = x.get('meta_ny', x.get('meta'))
            if m is not None:
                ov[str(x['id'])] = m
    for i, m in ov.items():
        if i in cur:
            cur[i] = dict(cur[i]); cur[i]['meta'] = m
    return cur, src


def utkastindex():
    idx = collections.defaultdict(list)
    for f in sorted(glob.glob(V + '*.json')):
        b = os.path.basename(f)
        if re.search(r'utkast|_in\.json|avvisade', b):
            try: d = json.load(open(f, encoding='utf-8'))
            except Exception: continue
            if isinstance(d, list):
                for x in d:
                    if isinstance(x, dict) and 'id' in x: idx[str(x['id'])].append((b, x))
    return idx


def arkiverade():
    ids = set()
    p = os.path.join(ROT, 'rapporter', 'arkiverade-av-synk-2026-11-06.md')
    if os.path.exists(p):
        for rad in open(p, encoding='utf-8'):
            m = re.search(r'\|\s*(\d{13,})\s*\|\s*$', rad)
            if m: ids.add(m.group(1))
    return ids


# ---------------------------------------------------------------- detektering
STD = re.compile(r'<h2>Leverans, retur och garanti</h2>.*', re.S)
TERM = re.compile(r'(?<![\wåäö])(användarvikt\w*|kroppsvikt\w*|lastgräns\w*|lastkapacitet\w*|maxlast\w*|'
                  r'max(?:imal|imum)?\.?\s*(?:vikt|last|belastning|kapacitet)\w*|maxbelastning\w*|belastning\w*|belastbar\w*|'
                  r'bärkraft\w*|bärförmåga\w*|bärkapacitet\w*|bärighet\w*|driftsvikt\w*|tål\w*|bär upp|bär(?:a|er)?\b|klarar)', re.I)
KGV = re.compile(r'(\d+(?:[.,]\d+)?)\s*(kg|ton)\b', re.I)
EJ_LAST = re.compile(r'(ökar kroppsvikten|viktväst|plug-in|vikter från|kan varieras|öka belastningen|belastningen kan justeras|'
                     r'med 1 kg i taget|Utökning:|Viktskivor|motstånd)', re.I)


def segment(x):
    segs = [('titel', x.get('titel') or ''), ('seo_title', x.get('seo_title') or ''), ('meta', x.get('meta') or '')]
    html = x.get('html') or ''
    h = STD.sub('', html)
    faq = re.search(r'<h2>Vanliga frågor</h2>.*', html, re.S)
    if faq: h += faq.group(0)
    for li in re.findall(r'<li>(.*?)</li>', h, re.S):
        segs.append(('li', re.sub('<[^>]+>', '', li).strip()))
    for p in re.findall(r'<(?:p|h3)>(.*?)</(?:p|h3)>', h, re.S):
        for s in re.split(r'(?<=[.!?])\s+', re.sub('<[^>]+>', '', p).strip()):
            if s: segs.append(('p', s))
    return segs


def klaim_i_segment(t):
    res = []
    for m in TERM.finditer(t):
        after = t[m.end():m.end() + 60]
        stop = re.search(r'\.\s|;', after)
        if stop: after = after[:stop.start()]
        v = KGV.search(after)
        if v and not re.search(r'(väger|svänghjul|produktvikt|totalvikt)', after[:v.start()], re.I):
            res.append((m.group(0).lower(), v.group(1).replace(',', '.') + v.group(2).lower(), m.end() + v.end())); continue
        before = t[max(0, m.start() - 30):m.start()]
        stop = list(re.finditer(r'\.\s|;', before))
        if stop: before = before[stop[-1].end():]
        v = list(KGV.finditer(before))
        if v and re.search(r'(för|till|upp till|max)\s*$', before[v[-1].end():], re.I | re.S):
            res.append((m.group(0).lower(), v[-1].group(1).replace(',', '.') + v[-1].group(2).lower(), m.end()))
    return res


def forekomster(x):
    """{värde: [{falt, text, fras, term, slut}]} för uppgifter som ser ut som lastgräns."""
    g = collections.defaultdict(list)
    for f, t in segment(x):
        seen = set()
        for term, val, slut in klaim_i_segment(t):
            if val in seen or EJ_LAST.search(t) and not re.search(r'(användarvikt|lastkapacitet|lastgräns|maxlast|maximal belastning)', t, re.I):
                continue
            seen.add(val)
            g[val].append({'falt': f, 'text': t, 'fras': FRAS in t.lower(), 'term': term, 'slut': slut})
    # säkerhetsnät: segment som har både samma kg-värde och frasen räknas som täckta förekomster (även om etiketten inte kändes igen)
    for f, t in segment(x):
        if FRAS not in t.lower(): continue
        for m in KGV.finditer(t):
            val = m.group(1).replace(',', '.') + m.group(2).lower()
            if val in g and not any(e['text'] == t and e['falt'] == f for e in g[val]):
                g[val].append({'falt': f, 'text': t, 'fras': True, 'term': 'fras-nära-värde', 'slut': m.end()})
    return g


# ---------------------------------------------------------------- källklass
def tal_re(val):
    n = re.match(r'(\d+(?:\.\d+)?)', val).group(1).replace('.', r'[.,]')
    return re.compile(r'(?<![\d.,])' + n + r'\s*(?:kg|kilo)\b', re.I)


SV_ETIKETT = re.compile(r'(användarvikt|belastning|lastkapacitet|lastgräns|maxvikt|maxlast|bärkapacitet|bärförmåga|'
                        r'kan bära|bär upp|maximal last|max\.? last|driftsvikt|last\b)', re.I)
EN_ORD = re.compile(r'\b(maximum|maximal user|user weight|load|capacity|weight limit|max\.? weight|operating weight|supports?)\b', re.I)


def kallklass(val, fakta, bekr, term):
    """Returnerar (klass, skäl). A+ = källan säger "enligt tillverkaren"; A = svensk ordagrann etikett+enhet (R4);
    B = osäker (engelsk/oklar källa, tolkad etikett, bara webbkälla eller värdet saknas i sparad källtext)."""
    tr = tal_re(val)
    finns = [m for m in tr.finditer(fakta or '')]
    bekr_txt = ' '.join(bekr) if isinstance(bekr, list) else str(bekr or '')
    webb = bool(re.search(r'https?://', bekr_txt)) and bool(re.search(r'(lastgräns|belastning|lastkapacitet|användarvikt|kg)', bekr_txt, re.I))
    if re.search(r'(tillverkarens egen (produkt)?sida|källa tillverkaren|tillverkarens sida|tillverkarens produktsida)', bekr_txt, re.I) and tal_re(val).search(bekr_txt):
        return 'A+', 'webbkälla på tillverkarens egen sida (regelbok v1.10); adress i att_bekrafta'
    if webb and tal_re(val).search(bekr_txt) and not (finns and any(SV_ETIKETT.search((fakta or '')[max(0, m.start() - 80):m.end() + 40]) and not EN_ORD.search((fakta or '')[max(0, m.start() - 80):m.end() + 40]) for m in finns)):
        return 'B', 'bara återförsäljarkälla (t.ex. bike-components, Rose Bikes); beslutet 2026-11-05 gör sådan lastgräns till "Ej känd"'
    if not finns:
        return 'B', ('värdet finns inte i sparad källtext; ' + ('webbkälla anges i att_bekrafta' if webb else 'ingen källa att styrka mot'))
    bästa = None
    for m in finns:
        fon = (fakta or '')[max(0, m.start() - 80):m.end() + 40]
        if FRAS in fon.lower():
            return 'A+', 'källtexten säger uttryckligen "enligt tillverkaren"'
        if SV_ETIKETT.search(fon) and not EN_ORD.search(fon):
            bästa = 'A'
        elif EN_ORD.search(fon) and bästa is None:
            bästa = 'EN'
    if bästa == 'A':
        return 'A', ('etiketten "driftsvikt" står ordagrant på svenska i källan (R4: texten tolkar den inte)' if 'driftsvikt' in term else 'svensk ordagrann etikett och enhet i leverantörens källtext (R4)') + ('; webbkälla anges också' if webb else '')
    if bästa == 'EN':
        return 'B', 'källan är engelsk eller maskinöversatt; översättning av etikett (R4: utelämna eller osäker)'
    return 'B', 'värdet står i källtexten men utan tydlig lastetikett'


# ---------------------------------------------------------------- föreslagen text
def lagg_till(seg_falt, text, slut):
    """Minsta ändring: lägg frasen direkt efter måttet. Specifikationsrad: parentes (som rensning 2, 2026-11-04)."""
    m = re.compile(r'\s+(per \w+|vardera|totalt|var)\b').match(text, slut)
    if m: slut = m.end()
    if seg_falt == 'li' and re.match(r'^[^:]{1,45}: ', text):
        ny = text[:slut] + f' ({FRAS})' + text[slut:]
    elif seg_falt == 'li':
        ny = text[:slut] + f', {FRAS}' + text[slut:]
    else:
        ny = text[:slut] + f' {FRAS}' + text[slut:]
    return ny


def typord(titel):
    ord_ = (titel or '').split()
    hopp = {'hopfällbar', 'hopfällbart', 'liggande', 'vikbar', 'infällbar', 'infällbart', 'push'}
    while ord_ and ord_[0].lower().strip(',') in hopp and len(ord_) > 1:
        ord_ = ord_[1:]
    return (ord_[0].strip(',') if ord_ else '?')


GRUPP = {'Löpband': 'Löpband', 'Motionscykel': 'Motionscyklar (inkl. spinning)', 'Spinningcykel': 'Motionscyklar (inkl. spinning)',
         'Elcykel': 'Elcyklar och eltrehjulingar', 'El-lastcykel': 'Elcyklar och eltrehjulingar', 'Eltrehjuling': 'Elcyklar och eltrehjulingar',
         'Crosstrainer': 'Crosstrainers och roddmaskiner', 'Roddmaskin': 'Crosstrainers och roddmaskiner',
         'Träningsbänk': 'Bänkar, stationer och multigym', 'Träningsstation': 'Bänkar, stationer och multigym', 'Multigym': 'Bänkar, stationer och multigym',
         'Powerstation': 'Bänkar, stationer och multigym', 'Hemmagym': 'Bänkar, stationer och multigym',
         'Stuntsparkcykel': 'Sparkcyklar', 'Sparkcykel': 'Sparkcyklar', 'Tricksparkcykel': 'Sparkcyklar',
         'Pakethållare': 'Cykelbärare, korgar och stödben', 'Frampakethållare': 'Cykelbärare, korgar och stödben',
         'Frambagagebärare': 'Cykelbärare, korgar och stödben', 'Bagagehållare': 'Cykelbärare, korgar och stödben',
         'Frontbärare': 'Cykelbärare, korgar och stödben', 'Cykelkorg': 'Cykelbärare, korgar och stödben', 'Stödben': 'Cykelbärare, korgar och stödben',
         'Cykelväska': 'Cykelbärare, korgar och stödben',
         'Kabelhandtag': 'Stänger, handtag och tillbehör', 'Curlstång': 'Stänger, handtag och tillbehör', 'Hantelstång': 'Stänger, handtag och tillbehör',
         'Skivstång': 'Stänger, handtag och tillbehör', 'Roddhandtag': 'Stänger, handtag och tillbehör', 'Kabelstång': 'Stänger, handtag och tillbehör',
         'Tricepsstång': 'Stänger, handtag och tillbehör', 'Latsdragstång': 'Stänger, handtag och tillbehör', 'Skivstångspaket': 'Stänger, handtag och tillbehör'}


GRUPP_RE = [
    (r'^(boll|träningsboll|gymnastikboll|fitnessboll)', 'Bollar, balans och plyo'),
    (r'^(balans|plyo|step|stretchplatta|stabilitet)', 'Bollar, balans och plyo'),
    (r'^(parallettes|armhävning|sissy|maghjul|magtränare|magträning|träningsrulle|tricepsrep|up\b|ab\b|dips|väggfäste|upphängning|handtag|ankelband|vristband|gåband|farmers|lifting|kettlebell|bodypump|training|yogapaket|gymmattor|boxningssäck|trampolin|stepper)', 'Hemmaträning, stöd och handtag'),
    (r'^(rack|halvställ|smith|multipress|träningsställ|latsdrag|benspark|knäböj|kraftstation|hantelställ|viktställ|skivstångsställ|deadlift|bicepscurl|powerbänk|axelpress|träningsmaskin|stegmaskin|skiergometer|hybridtränare|olympiska)', 'Styrkemaskiner, ställ och racks'),
    (r'^(minicykel)', 'Motionscyklar (inkl. spinning)'),
    (r'^(framkorg|handväska|styrväska|mini-stöd|stöd\b|rattkälke)', 'Cykelbärare, korgar och stödben'),
]


def grupp(titel):
    t = typord(titel)
    if t in GRUPP: return GRUPP[t]
    for pat, g in GRUPP_RE:
        if re.search(pat, t, re.I): return g
    return 'Övrigt'


# ---------------------------------------------------------------- huvud
RADTYP_PRIO = {'li_etikett': 0, 'p': 1, 'meta': 2, 'li_passar': 3, 'titel': 4, 'seo_title': 5}


def radtyp_prio(f):
    if f['falt'] == 'li':
        return RADTYP_PRIO['li_etikett'] if re.match(r'^[^:]{1,45}: ', f['text']) else RADTYP_PRIO['li_passar']
    return RADTYP_PRIO[f['falt']]


def tillampa(p, rader):
    """Tillämpar listan av {falt,radtyp,gammal,ny} på en kopia. Returnerar (ny_meta, ny_html, fel)."""
    meta, html, fel = p['x'].get('meta') or '', p['x'].get('html') or '', []
    for c in rader:
        if c['falt'] == 'meta':
            if meta.count(c['gammal']) != 1: fel.append('meta: raden hittas inte exakt en gång'); continue
            meta = meta.replace(c['gammal'], c['ny'])
        elif c['radtyp'] == 'li' and html.count('<li>' + c['gammal'] + '</li>') == 1:
            html = html.replace('<li>' + c['gammal'] + '</li>', '<li>' + c['ny'] + '</li>')
        elif c['radtyp'] == 'p' and html.count(c['gammal']) == 1:
            html = html.replace(c['gammal'], c['ny'])
        else:
            fel.append(f'beskrivning: raden hittas inte exakt en gång ({c["gammal"][:40]})')
    return meta, html, fel


def analysera():
    las_profil(os.path.join(ROT, 'shopify-sync/config/butiksprofil-bestofsports.json'))
    sparr = las_sparr(os.path.join(ROT, 'shopify-sync/config/sparrlista.json'))
    cur, src = bygg(); idx = utkastindex(); arkiv = arkiverade()
    prod = []
    for i, x in cur.items():
        g = forekomster(x)
        if not g: continue
        fk, bk = '', []
        for b, u in idx.get(i, []):
            if u.get('fakta'): fk, bk = u['fakta'], u.get('att_bekrafta') or []
        poster = []
        for val, fl in g.items():
            n = sum(1 for f in fl if f['fras'])
            klass, skal = kallklass(val, fk, bk, fl[0]['term'])
            poster.append({'varde': val, 'niva': 0 if n == len(fl) else (1 if n == 0 else 2), 'klass': klass, 'klass_skal': skal, 'f': fl,
                           'tidigare_fras': n > 0})
        p = {'id': i, 'x': x, 'fil': src[i], 'poster': poster, 'spar': (sparr.get(i) or [None])[0], 'arkiverad': i in arkiv,
             'grupp': grupp(x.get('titel')), 'forslag': [], 'alt_b': [], 'osakra': []}
        for po in poster:
            if po['niva'] == 0: continue
            saknar = [f for f in po['f'] if not f['fras']]
            saknar.sort(key=radtyp_prio)
            for k, f in enumerate(saknar):
                if f['falt'] in ('titel', 'seo_title'):
                    p['osakra'].append({'falt': f['falt'], 'radtyp': f['falt'], 'varde': po['varde'], 'niva': po['niva'], 'klass': po['klass'], 'gammal': f['text'],
                                        'skal': 'lastgräns i titel/SEO-titel; kräver omformulering (titeln är högst 70 tecken)'}); continue
                rec = {'falt': 'meta' if f['falt'] == 'meta' else 'beskrivning', 'radtyp': f['falt'], 'varde': po['varde'], 'niva': po['niva'], 'klass': po['klass'],
                       'gammal': f['text'], 'ny': lagg_till(f['falt'], f['text'], f['slut'])}
                if po['klass'] == 'B':
                    p['osakra'].append({**rec, 'skal': po['klass_skal']}); continue
                # nivå 1: exakt en förekomst per påstående enligt R5; övriga och hela nivå 2 = alt B (kräver beslut)
                (p['forslag'] if (po['niva'] == 1 and k == 0) else p['alt_b']).append(rec)
        if not (p['forslag'] or p['alt_b'] or p['osakra']): continue
        m1, h1, f1 = tillampa(p, p['forslag'])
        n_fras = len(re.findall(FRAS, h1, re.I))
        p['r5_fore'] = len(re.findall(FRAS, p['x'].get('html') or '', re.I))
        if p['forslag'] and n_fras > 2:
            # R5: högst två "enligt tillverkaren" per text. Förslaget skulle bryta mot det -> osäkert, kräver beslut
            for c in p['forslag']:
                p['osakra'].append({**c, 'skal': f'R5: texten har redan {p["r5_fore"]} "enligt tillverkaren" och skulle få {n_fras} (högst 2); en annan förekomst måste tas bort först'})
            p['forslag'] = []
            m1, h1, f1 = tillampa(p, [])
        m2, h2, f2 = tillampa(p, p['forslag'] + p['alt_b'])
        p['status'] = ('spärrad' if p['spar'] else 'arkiverad' if p['arkiverad'] else 'forslag' if p['forslag'] else
                       'osaker' if p['osakra'] else 'alt_b')
        p.update(meta_forslag=m1, html_forslag=h1, meta_alt_b=m2, html_alt_b=h2, fel=f1 + f2)
        prod.append(p)
    return cur, prod


def kontrollfiler(prod, tmp):
    """Skriver 'före'- och 'efter'-skrivfiler i skrivfilsformat (samma fält som skrivfilerna) och kör skrivfil_kontroll.kontrollera på dem."""
    import skrivfil_kontroll as K
    sparr = las_sparr(os.path.join(ROT, 'shopify-sync/config/sparrlista.json'))
    res = {}
    aktiva = [p for p in prod if p['status'] not in ('spärrad', 'arkiverad')]
    urval = {'forslag': [p for p in aktiva if p['forslag']], 'alt_b': [p for p in aktiva if p['forslag'] or p['alt_b']]}
    for namn, lista in urval.items():
        fore = [{k: p['x'].get(k) for k in ('id', 'nr', 'titel', 'seo_title', 'meta', 'html')} for p in lista]
        efter = [{**f, 'meta': (p['meta_forslag'] if namn == 'forslag' else p['meta_alt_b']),
                  'html': (p['html_forslag'] if namn == 'forslag' else p['html_alt_b'])} for f, p in zip(fore, lista)]
        fd = {}
        for etikett, d in (('fore', fore), ('efter', efter)):
            fil = os.path.join(tmp, f'rensning2_kontroll_{namn}_{etikett}.json')
            json.dump(d, open(fil, 'w', encoding='utf-8'), ensure_ascii=False)
            n, fel, varn = K.kontrollera(fil, sparr, False)
            fd[etikett] = (n, fel, varn)
            os.remove(fil)
        nya_fel = [m for m in fd['efter'][1] if m not in set(fd['fore'][1])]
        nya_varn = [m for m in fd['efter'][2] if m not in set(fd['fore'][2])]
        res[namn] = {'produkter': len(lista), 'fel_fore': len(fd['fore'][1]), 'fel_efter': len(fd['efter'][1]), 'nya_fel': nya_fel,
                     'varn_fore': len(fd['fore'][2]), 'varn_efter': len(fd['efter'][2]), 'nya_varningar': nya_varn}
    return res


def kort(t, n=60):
    t = re.sub(r'\s+', ' ', t or '').strip()
    return t if len(t) <= n else t[:n - 1].rstrip() + '…'


def cell(t):
    return (t or '').replace('|', '\\|')


def meta_ryms(p, c):
    return len(p['x'].get('meta') or '') - len(c['gammal']) + len(c['ny']) <= 155


def main(argv=None):
    a = list(argv if argv is not None else sys.argv[1:])
    datum = datetime.date.today().isoformat()
    tmp = '/tmp'
    if '--datum' in a: k = a.index('--datum'); datum = a[k + 1]; del a[k:k + 2]
    if '--tmp' in a: k = a.index('--tmp'); tmp = a[k + 1]; del a[k:k + 2]
    cur, prod = analysera()
    kf = kontrollfiler(prod, tmp)

    # alla produkter med lastuppgift (även de som redan är korrekta) för statistiken
    alla = []
    for i, x in cur.items():
        g = forekomster(x)
        if g: alla.append((i, x, g))
    niva_prod = collections.Counter()
    niva_klaim = collections.Counter()
    for i, x, g in alla:
        worst = 0
        for val, fl in g.items():
            n = sum(1 for f in fl if f['fras'])
            nv = 0 if n == len(fl) else (1 if n == 0 else 2)
            niva_klaim[nv] += 1; worst = max(worst, nv)
        niva_prod[worst] += 1
    forek_med = sum(1 for i, x, g in alla for fl in g.values() for f in fl if f['fras'])
    forek_utan = sum(1 for i, x, g in alla for fl in g.values() for f in fl if not f['fras'])

    # --- JSON (format som rensning 1 + utökade fält)
    ut = []
    for p in sorted(prod, key=lambda q: q['x']['nr']):
        x = p['x']
        rec = {'id': p['id'], 'nr': x['nr'], 'fil': p['fil'], 'titel': x.get('titel'), 'seo_title': x.get('seo_title'),
               'meta_gammal': x.get('meta'), 'meta_ny': p['meta_forslag'],
               'typ': p['grupp'], 'status': p['status'], 'kor': False,
               'forslag': [{k: c[k] for k in ('falt', 'radtyp', 'varde', 'klass', 'gammal', 'ny')} for c in p['forslag']],
               'alt_b': [{**{k: c[k] for k in ('falt', 'radtyp', 'varde', 'niva', 'klass', 'gammal', 'ny')},
                          'ryms': (meta_ryms(p, c) if c['falt'] == 'meta' else True)} for c in p['alt_b']],
               'osakra': [{k: c.get(k) for k in ('falt', 'radtyp', 'varde', 'niva', 'klass', 'gammal', 'ny', 'skal') if c.get(k) is not None} for c in p['osakra']],
               'notering': ('spärrad (' + p['spar'] + '): ändras inte' if p['spar'] else 'arkiverad av leverantörssynken: ändras inte' if p['arkiverad'] else '')}
        if p['alt_b']:
            rec['meta_ny_alt_b'] = p['meta_alt_b']
        ut.append(rec)
    jfil = os.path.join(V, 'rensning2_forslag.json')
    json.dump(ut, open(jfil, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    # --- siffror per produkttyp
    per = collections.defaultdict(lambda: collections.Counter())
    for i, x, g in alla:
        gr = grupp(x.get('titel'))
        per[gr]['med'] += 1
    st = {p['id']: p for p in prod}
    for p in prod:
        gr = p['grupp']
        if p['status'] in ('spärrad', 'arkiverad'): per[gr][p['status']] += 1; continue
        if p['forslag']: per[gr]['forslag'] += 1
        elif p['osakra']: per[gr]['osaker'] += 1
        elif p['alt_b']: per[gr]['alt_b'] += 1
    rader = []
    for gr in sorted(per, key=lambda g: -per[g]['med']):
        c = per[gr]
        rader.append(f"| {gr} | {c['med']} | {c['forslag']} | {c['osaker']} | {c['alt_b']} | {c['spärrad'] + c['arkiverad']} |")
    n_med = len(alla)

    md = []
    A = md.append
    A(f'# Rensning 2 – underlag: "enligt tillverkaren" på lastgränser (BEST OF SPORTS, {datum})\n')
    A('**Status: underlag och lista. Ingenting är skrivet till Shopify eller till någon butik.** Listan bygger på repots egna skrivfiler och utkast '
      '(`rapporter/facit-bos-2026-10-31/vag2_skriv/`), inte på live-läsning. Live kan avvika (nattsynken, manuella ändringar, arkivering). '
      'Ett live-klassningssteg (som i rensning 1: live-texten måste vara lika med "före"-texten, annars hoppas produkten över) krävs därför före all skrivning.\n')
    A('Frågan som underlaget hör till är F2 i `shopify-sync/status/oppna_fragor.json`: ska "enligt tillverkaren" stå på alla maxviktsuppgifter? '
      'Svaret antas inte här; beslutsfilen `rapporter/beslut-' + datum + '.md` ställer frågan.\n')
    A('## 1. Resultat i siffror\n')
    A('| Mått | Antal |\n|---|---|')
    A(f'| Skrivna texter i skrivfilerna (senaste version per produkt, metarensning 1 och 3 påförda) | {len(cur)} |')
    A(f'| Texter med maxvikt-/belastningsuppgift (lastgräns) | {n_med} |')
    A(f'| Lastgränsuppgifter (påståenden) i dessa texter | {sum(niva_klaim.values())} |')
    A(f'| – nivå 0: frasen "enligt tillverkaren" finns på minst en förekomst av påståendet (uppfyller R5 "en gång per påstående") | {niva_klaim[0]} |')
    A(f'| – nivå 2: frasen finns på en förekomst, men uppgiften upprepas utan frasen (oftast i metabeskrivningen, "Passar för" eller löptext) | {niva_klaim[2]} |')
    A(f'| – nivå 1: frasen saknas helt, på alla förekomster | {niva_klaim[1]} |')
    A(f'| Förekomster (rader/meningar) med lastgräns som saknar frasen | {forek_utan} av {forek_utan + forek_med} |')
    A(f'| Produkter där alla påståenden är på nivå 0 | {niva_prod[0]} |')
    A(f'| Produkter med nivå 2 som högsta nivå | {niva_prod[2]} |')
    A(f'| Produkter med nivå 1 (frasen saknas helt på minst ett påstående) | {niva_prod[1]} |')
    n_f = sum(1 for p in prod if p['status'] == 'forslag'); n_o = sum(1 for p in prod if p['osakra'] and not p['forslag'] and p['status'] not in ('spärrad', 'arkiverad'))
    A(f'| **Förslag enligt gällande regler (lista 1)** | **{n_f} produkter, {sum(len(p["forslag"]) for p in prod if p["status"] == "forslag")} rader** |')
    A(f'| **Osäkra, kräver Davids beslut (lista 2)** | **{sum(1 for p in prod if p["osakra"] and p["status"] not in ("spärrad", "arkiverad"))} produkter, {sum(len(p["osakra"]) for p in prod if p["status"] not in ("spärrad", "arkiverad"))} rader** |')
    A(f'| Spärrade eller arkiverade, ändras inte (lista 3) | {sum(1 for p in prod if p["status"] in ("spärrad", "arkiverad"))} produkter |')
    n_alt = [p for p in prod if p['alt_b'] and p['status'] not in ('spärrad', 'arkiverad')]
    A(f'| Alternativ B (lista 4): alla övriga förekomster utan frasen | {len(n_alt)} produkter, {sum(len(p["alt_b"]) for p in n_alt)} rader |')
    A('')
    A('**Läsning av siffrorna.** Rensning 2 den 4 november lade till frasen på specifikationsraderna i 178 texter, och texterna som skrevs efter det har frasen från start. '
      'Därför är den ursprungliga uppskattningen i F2 ("2 av 24 texter") inte längre rättvisande: i repots data saknar bara ' + str(niva_prod[1]) + ' av ' + str(n_med) +
      ' texter frasen helt. Det som återstår i stor skala är att uppgiften upprepas utan frasen i metabeskrivning, "Passar för" och löptext. '
      'Det är tillåtet enligt R5 (en gång per påstående) men är exakt vad F2 egentligen frågar om.\n')
    A('**Bakgrund: vad rensning 2 hoppade över den 4 november** (`rapporter/rensning2-lastgranser-2026-11-04/underlag.md`): 8797 och 10104 (skulle ge fler än två "enligt tillverkaren"), 3001 och 10349 (ingen specifikationsrad som kunde ändras automatiskt), 10348 (inte aktiv) och viktvästen 10604 (tillagd vikt, ingen lastgräns). '
      'Av dem är 8797 fortfarande öppen och redovisas i lista 1 (en rad i stället för två, så att R5 hålls). 10104 och 3001 redovisas i lista 2 (R5). 10349 har frasen i löptexten och saknar den bara på specifikationsraden (alt B). 10348 är spärrad. 10604 är ingen lastgräns.\n')
    A('## 2. Metod, nivåer och källklasser\n')
    A('- **Detektering:** för varje titel, SEO-titel, metabeskrivning, punkt i specifikation/"Passar för", löptextmening och FAQ-svar söks en lastetikett (användarvikt, maxlast, lastkapacitet, maximal belastning, lastgräns, maxvikt, bärförmåga, driftsvikt m.fl.) med ett kg-värde i samma mening. '
      'Inte lastgränser (enligt R4): viktväst med tillagd vikt, plug-in-vikter, motstånd, svänghjul, produktvikt, fyllnadsmängd. Kontrollerat med en andra sökning på "max", "upp till", "ton", "kilo": inga ytterligare lastgränser hittades.')
    A('- **Nivå:** per påstående (kg-värde): 0 = frasen finns på minst en förekomst; 1 = frasen saknas överallt; 2 = frasen finns på någon förekomst men inte alla.')
    A('- **Källklass A+:** produktens källtext säger själv "enligt tillverkaren" vid värdet. **A:** svensk ordagrann etikett och enhet i leverantörens källtext (regelbokens R4 och Davids beslut 2026-11-04, "Alt A"; samma grund som rensning 2 den 4 november använde). '
      '**B (osäker, kräver Davids beslut):** engelsk eller maskinöversatt källa, etiketten är en tolkning ("driftsvikt"), värdet står inte i sparad källtext, eller uppgiften kommer från en webbkälla som inte styrker att den är tillverkarens. För B föreslås ingen ändring.')
    A('- **Viktig tolkning att bekräfta:** ingen leverantörskälla säger ordagrant att uppgiften kommer från tillverkaren (utom A+). Jag har behandlat regelbokens definition (svensk ordagrann uppgift med etikett och enhet = tillverkarens uppgift) som tillräcklig för klass A. Läser David uppdraget strängare flyttas alla klass A till "osäker".')
    A('- **Förslagens utformning:** minsta ändring, frasen direkt efter måttet. Specifikationsrad: `(enligt tillverkaren)` i parentes (som i rensning 2). Metabeskrivning och löptext: ` enligt tillverkaren`. Punkt i "Passar för": `, enligt tillverkaren`. Inga utfyllnadsord.')
    A('- **Gällande regler (lista 1):** högst en förekomst per påstående (R5), högst två "enligt tillverkaren" per text, meta 70–155 tecken. Lastgräns i titel/SEO-titel föreslås inte (titeln är högst 70 tecken; kräver omformulering).')
    A('- **Alternativ B (lista 4):** frasen på varje återstående förekomst. Det strider mot R5 ("en gång per påstående", högst två per text) och kräver både ett ja på F2 i den formen och en ändring av R5. För metabeskrivningar anges om den nya metan ryms inom 155 tecken.\n')
    A('## 3. Antal per produkttyp\n')
    A('| Produkttyp | Texter med lastgräns | Förslag (lista 1) | Osäkra (lista 2) | Bara alt B (lista 4) | Spärrade/arkiverade |\n|---|---|---|---|---|---|')
    md.extend(rader)
    A('')
    A('Produkttyp = typordet först i titeln (gruppering enligt skriptet `shopify-sync/scripts/rensning2_underlag.py`).\n')

    # lista 1
    A('## 4. Lista 1 – förslag enligt gällande regler (före och efter)\n')
    A('Bara nivå 1 (frasen saknas helt), klass A eller A+, en förekomst per påstående. Längdgränser kontrollerade nedan.\n')
    A('| Nr | Titel | Rad | Före | Efter | Risk |\n|---|---|---|---|---|---|')
    for p in sorted(prod, key=lambda q: q['x']['nr']):
        if p['status'] != 'forslag': continue
        for c in p['forslag']:
            risk = 'Låg: svensk ordagrann etikett och enhet i källan; ändrar bara raden' + ('; metan ändras (längd ' + str(len(p['meta_forslag'])) + ' tecken)' if c['falt'] == 'meta' else '')
            A(f"| {p['x']['nr']} | {cell(kort(p['x']['titel'], 50))} | {c['radtyp']} | {cell(c['gammal'])} | {cell(c['ny'])} | {risk} |")
    A('')

    # lista 2
    A('## 5. Lista 2 – osäkra: kräver Davids beslut (ingen ändring föreslås)\n')
    A('| Nr | Titel | Rad | Text | Skäl |\n|---|---|---|---|---|')
    for p in sorted(prod, key=lambda q: q['x']['nr']):
        if p['status'] in ('spärrad', 'arkiverad'): continue
        for c in p['osakra']:
            A(f"| {p['x']['nr']} | {cell(kort(p['x']['titel'], 45))} | {c['radtyp']} | {cell(kort(c['gammal'], 110))} | {cell(c.get('skal'))} |")
    A('')
    A('Särskilt om etiketten "driftsvikt": BH Fitness 10071, 10074 och 10090 har "Maximal driftsvikt" ordagrant på svenska i källan och ligger därför i lista 1/alt B som klass A (R4: etiketten får stå, men får inte tolkas som användarvikt). 10069 har bara engelsk källa ("Maximum operating weight"); beslutsloggen 2026-11-04 ("Alt A") säger att driftsvikt utelämnas då. Texten kan alltså redan strida mot R4; det är ett separat fynd att ta ställning till, inte något som löses genom att lägga till frasen.\n')

    A('Särskilt om Hebie-stödbenen 32027–32029: texterna har redan "enligt tillverkaren" på lastgränsen 25 kg, men uppgiften bygger på återförsäljarsidor (bike-components, Rose Bikes) eftersom Hebies egen sida inte gick att läsa. Beslutet 2026-11-05 (Gymstick Performance Board och Power Rings) gjorde sådan lastgräns till "Ej känd". Det är ett separat fynd: samma princip kan kräva att de tre texterna ändras, inte kompletteras.\n')

    # lista 3
    A('## 6. Lista 3 – spärrade och arkiverade (ändras inte)\n')
    A('| Nr | Titel | Skäl | Rader som annars hade berörts |\n|---|---|---|---|')
    for p in sorted(prod, key=lambda q: q['x']['nr']):
        if p['status'] in ('spärrad', 'arkiverad'):
            sk = f"spärrad: {p['spar']}" if p['spar'] else 'arkiverad av leverantörssynken (Velomarket3)'
            A(f"| {p['x']['nr']} | {cell(kort(p['x']['titel'], 50))} | {sk} | {len(p['forslag']) + len(p['alt_b']) + len(p['osakra'])} |")
    A('')

    # lista 4
    A('## 7. Lista 4 – alternativ B: frasen på alla återstående förekomster (före och efter)\n')
    A('Gäller bara om David svarar ja på F2 i den vidaste formen och beslutar att R5 ändras. Kolumnen "Ryms" visar om ny meta blir högst 155 tecken. '
      'Efter ändring ger flera texter fler än två "enligt tillverkaren" (R5), se avsnitt 8.\n')
    grupper = collections.defaultdict(list)
    for p in sorted(prod, key=lambda q: q['x']['nr']):
        if p['status'] in ('spärrad', 'arkiverad') or not p['alt_b']: continue
        grupper[p['grupp']].append(p)
    for gr in sorted(grupper, key=lambda g: -len(grupper[g])):
        A(f'### {gr} ({len(grupper[gr])} produkter)\n')
        A('| Nr | Titel | Rad | Före | Efter | Ryms |\n|---|---|---|---|---|---|')
        for p in grupper[gr]:
            for c in p['alt_b']:
                r = ''
                if c['falt'] == 'meta':
                    n = len(p['x']['meta']) - len(c['gammal']) + len(c['ny'])
                    r = f"ja ({n})" if n <= 155 else f"nej ({n})"
                A(f"| {p['x']['nr']} | {cell(kort(p['x']['titel'], 40))} | {c['radtyp']} | {cell(c['gammal'])} | {cell(c['ny'])} | {r} |")
        A('')
    meta_alt = [(p, c) for p in n_alt for c in p['alt_b'] if c['falt'] == 'meta']
    ryms = sum(1 for p, c in meta_alt if meta_ryms(p, c))
    over2 = sum(1 for p in n_alt if len(re.findall(FRAS, p['html_alt_b'], re.I)) > 2)

    # kontroller
    A('## 8. Kontroller (`skrivfil_kontroll.py`, läsläge på kopior; inga filer i repot ändrades)\n')
    A('Kontrollerna kördes på en temporär skrivfil med "före"- och "efter"-text per produkt. Jämförelsen visar bara nya fel som förslaget orsakar.\n')
    A('| Förslag | Produkter | Fel före | Fel efter | Nya fel | Nya varningar |\n|---|---|---|---|---|---|')
    for namn, tx in (('forslag', 'Lista 1'), ('alt_b', 'Lista 1 + lista 4')):
        v = kf[namn]
        A(f"| {tx} | {v['produkter']} | {v['fel_fore']} | {v['fel_efter']} | {len(v['nya_fel'])} | {len(v['nya_varningar'])} |")
    A('')
    A(f"- Lista 1: nya fel {len(kf['forslag']['nya_fel'])}. Fel som redan fanns före ändringen räknas inte som förslagets.")
    nya_m = [m for m in kf['alt_b']['nya_fel'] if 'meta ' in m]
    nya_r5 = [m for m in kf['alt_b']['nya_fel'] if 'R5' in m]
    A(f"- Lista 4: {len(kf['alt_b']['nya_fel'])} nya fel: {len(nya_m)} metabeskrivningar över 155 tecken och {len(nya_r5)} texter med fler än två \"enligt tillverkaren\" (R5). "
      f"Av {len(meta_alt)} metaändringar ryms {ryms} inom 155 tecken; {len(meta_alt) - ryms} kräver att annan text i metan kortas (inte föreslaget här). "
      f"Totalt {over2} texter skulle få fler än två \"enligt tillverkaren\" i beskrivningen.\n")
    A('## 9. Risk\n')
    A('- **Källrisk:** frasen sätter tillverkarens namn på en uppgift. För klass A bygger det på regelbokens definition, inte på att leverantören skriver "tillverkaren". För klass B finns inget stöd, därför inga förslag.')
    A('- **Regelrisk (alt B):** frasen på varje förekomst bryter R5 och gör metabeskrivningar längre än 155 tecken; texten blir mer upprepande utan att bli mer informativ för kunden.')
    A('- **Läsbarhetsrisk:** "Maximal användarvikt är 130 kg enligt tillverkaren" i en metabeskrivning tar 20 tecken av 155 och pressar bort annat innehåll.')
    A('- **Datarisk:** listan bygger på repots filer. Texter kan ha ändrats live; därför live-klassning (live-raden måste vara exakt "före") och återläsning tecken för tecken efter skrivning, som i rensning 1 och 2.')
    A('- **Teknisk risk:** rensning 1:s skript (`shopify_meta_rensning.py`) hanterar bara `seo.description`. Radändringar i beskrivningen kräver samma väg som rensning 2 den 4 november (`shopify_skriv_texter.py` med skrivfil). Indatafilen innehåller raderna före/efter för exakt strängbyte (varje rad måste finnas exakt en gång).\n')
    A('## 10. Filer\n')
    A('- Indata (körs inte): `rapporter/facit-bos-2026-10-31/vag2_skriv/rensning2_forslag.json` – lista med rensning 1:s fält (`id`, `nr`, `fil`, `titel`, `seo_title`, `meta_gammal`, `meta_ny`) och utökade fält `typ`, `status`, `kor` (alltid false), `forslag`, `alt_b`, `osakra`, `meta_ny_alt_b`, `notering`. `meta_ny` är bara ändrad där en lista 1-ändring gäller metan; annars lika med `meta_gammal`.')
    A('- Skript som tar fram listan: `shopify-sync/scripts/rensning2_underlag.py` (läser bara repots filer; inget nätverk).')
    A('')
    mdfil = os.path.join(ROT, 'rapporter', f'rensning-2-underlag-{datum}.md')
    open(mdfil, 'w', encoding='utf-8').write('\n'.join(md))
    return {'md': mdfil, 'json': jfil, 'kf': kf, 'niva_prod': niva_prod, 'niva_klaim': niva_klaim, 'n_med': n_med, 'forek_utan': forek_utan,
            'forek_med': forek_med, 'ryms': ryms, 'meta_alt': len(meta_alt), 'over2': over2, 'prod': prod}


if __name__ == '__main__':
    r = main()
    print('Skrev', r['md'], r['json'])
    print('nivå (produkter):', dict(r['niva_prod']), 'nivå (påståenden):', dict(r['niva_klaim']), 'med lastgräns:', r['n_med'])
    print('förekomster utan fras:', r['forek_utan'], 'med fras:', r['forek_med'])
    for k, v in r['kf'].items():
        print(k, {a: (b if not isinstance(b, list) else len(b)) for a, b in v.items()})
