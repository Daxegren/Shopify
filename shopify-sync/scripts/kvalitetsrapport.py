#!/usr/bin/env python3
"""Kvalitetsrapport för en körning av produkttextutrullning (butiksoberoende, helt offline).

Läser en körnings material enligt ett manifest (JSON) och skriver en läsbar rapport för en e-handlare:
omfattning, före/efter, tillämpade regler, kontrollresultat, granskning, återläsning, stickprov,
mätetal, avvisade produkter med skäl, beslut som kunden behöver ta och svagheter.

Skriptet gör inga nätverksanrop, läser inga miljövariabler och ändrar inga indatafiler.
Allt som skrivs ut passerar `rensa()` som tar bort e-postadresser, telefonnummer och allt som liknar nycklar.

Användning:
  python3 -I shopify-sync/scripts/kvalitetsrapport.py --manifest MANIFEST.json --ut RAPPORT.md [--html] [--datum ÅÅÅÅ-MM-DD]

Utan --ut skrivs Markdown till standard ut. Med --html skrivs även en fristående HTML-fil bredvid (samma namn, .html).
Manifestets format och indatafilernas form beskrivs i shopify-sync/docs/kundguide-kom-igang.md (bilaga) och i `MANIFEST_EXEMPEL` nedan.
Tester (utan nätverk): python3 -I shopify-sync/scripts/test_kvalitetsrapport.py
"""
import argparse, collections, csv, datetime, glob, hashlib, html as htmlmod, json, os, re, statistics, sys

HAR = os.path.dirname(os.path.abspath(__file__))
ROT_STANDARD = os.path.abspath(os.path.join(HAR, '..', '..'))

MANIFEST_EXEMPEL = {
    'namn': 'Min butik, första batchen',
    'butik': 'Min butik',
    'profil': 'shopify-sync/config/butiksprofil-minbutik.json',
    'sparrlista': 'shopify-sync/config/sparrlista.json',
    'regelbok': 'shopify-sync/regler/regler-v1.md',
    'inventering': ['kors/*_in.json'],
    'utkast': ['kors/*_utkast.json'],
    'avvisade': ['kors/*_avvisade.json'],
    'utlatanden': ['kors/*utlatande*.json'],
    'skrivfiler': ['kors/*skriv*.json'],
    'korrigeringsmonster': 'korr',
    'fore': ['kors/original/*fore*.json'],
    'resultat': ['kors/original/*resultat*.json'],
    'skrivrapporter': [],
    'stickprov': ['kors/stickprov*.md', 'kors/stickprov*.json'],
    'oppna_fragor': 'shopify-sync/status/oppna_fragor.json',
    'efterkontroll': [],
    'totalt_i_butiken': {'antal': 0, 'kalla': ''},
    'exempel': {'antal': 5, 'fro': 'valfritt ord'},
}

# Kategorier för avvisade produkter: första träffande mönster vinner (ordningen är en del av metoden).
AVVISAD_KATEGORIER = [
    ('Redan arkiverad eller inte aktiv i butiken', r'archived|arkiverad|status\b|inte aktiv'),
    ('Spärrad eller utanför beslutad omfattning', r'spärr|utanför'),
    ('Barn och ungdom', r'barn|ungdom|junior'),
    ('Kosttillskott och hälsopåståenden', r'kosttillskott|tillskott|melatonin|hälsopåst'),
    ('Dubblett av annan annons', r'dubblett'),
    ('Flera varianter med olika pris eller artiklar', r'variant|olika pris|default title|flera storlek'),
    ('Lastgräns, bärande eller hängande del', r'lastgräns|maxvikt|bärande|hängande|belastning'),
    ('Säkerhet och skydd', r'hjälm|skydd|säkerhet|bromsdel'),
    ('Källan är tunn, trasig eller motsägelsefull', r'tunn|trasig|maskinöversatt|motsäg|saknar källa|otillräck|tom källa|ingen beskrivning|källan (är|saknar|har bara)'),
]
AVVISAD_ATGARD = {
    'Redan arkiverad eller inte aktiv i butiken': 'Avgör om produkten ska återaktiveras (kontrollera först varför den arkiverades) eller förbli arkiverad.',
    'Spärrad eller utanför beslutad omfattning': 'Ta ställning till om spärren ska ligga kvar eller hävas för hela kategorin.',
    'Barn och ungdom': 'Besluta vilka fakta som får skrivas och vilka underkategorier som alltid ska utebli (till exempel skyddsutrustning).',
    'Kosttillskott och hälsopåståenden': 'Besluta om texten får innehålla annat än produktfakta och användning, och vem som kontrollerar påståenden.',
    'Dubblett av annan annons': 'Besluta om dubbletterna ska slås ihop eller behållas som egna produkter.',
    'Flera varianter med olika pris eller artiklar': 'Dela upp varianterna i separata produkter eller be leverantören rätta datan; texten kan inte skrivas rätt förrän dess.',
    'Lastgräns, bärande eller hängande del': 'Besluta hur en saknad lastgräns ska uttryckas (till exempel "Ej känd") eller lämna produkten utan text.',
    'Säkerhet och skydd': 'Besluta om produkten ska skrivas med enbart fakta ur källan eller lämnas åt en människa.',
    'Källan är tunn, trasig eller motsägelsefull': 'Komplettera källan (tillverkarens sida, leverantör) eller godkänn en kort faktatext.',
    'Övrigt': 'Läs skälen i listan och avgör från fall till fall.',
}
RATTNING_ORSAKER = [
    ('Cirkulär eller svag inledning', r'cirkul|inledning'),
    ('"Enligt tillverkaren" saknas eller används fel', r'enligt tillverkaren|attribu'),
    ('Lastgräns eller maxvikt', r'lastgräns|maxvikt|belastning|användarvikt'),
    ('Uppgift saknar stöd i källan', r'källa|källan|stöd i|står inte'),
    ('Språk, stavning eller ordval', r'stav|grammat|ordval|böj|sammansättning|typord|ordföljd|språk'),
    ('Metabeskrivning', r'\bmeta\b|metabeskrivning'),
]
FORBJUDNA_STANDARD = [
    [r'här kallad', 'arbetsterm i kundtext'],
    [r'Vanliga frågor', 'kopierat FAQ-avsnitt'],
    [r'Om märket', 'kopierat "Om märket"-avsnitt'],
    [r'Maximum (operating|user) weight', 'engelsk maxviktsrad kvar'],
    [r'Load (capacity|range)', 'engelsk lastrad kvar'],
]
GRANSER_STANDARD = {'titel_max': 70, 'titel_max_komma': 2, 'seo_titel_max': 43, 'meta_min': 70, 'meta_max': 155}
KONTROLLNAMN = collections.OrderedDict([
    ('SPARRAD', 'Spärrad produkt har fått text'),
    ('SPARRAD_KAND', 'Spärrad produkt som redan redovisats som överträdelse'),
    ('TITEL_LANG', 'Titel längre än gränsen'),
    ('TITEL_KOMMA', 'Titel med för många kommatecken'),
    ('SEO_LANG', 'SEO-titel längre än gränsen'),
    ('META_LANGD', 'Metabeskrivning utanför tillåten längd'),
    ('META_SAKNAS', 'Metabeskrivning saknas'),
    ('BLOCK', 'Standardblocket (leverans, retur, garanti) saknar krävd rad'),
    ('VERSALER', 'Märke skrivet med versaler'),
    ('OSYNLIG', 'Osynligt tecken i texten'),
    ('ATTRIBUERING', '"Enligt tillverkaren" oftare än tillåtet'),
    ('FORBJUDET', 'Förbjudet uttryck i kundtext'),
    ('CIRKULAR', 'Cirkulär inledning ("X är en X")'),
    ('DUBBLETT_TITEL', 'Titeln används av flera produkter'),
    ('DUBBLETT_SEO', 'SEO-titeln används av flera produkter'),
    ('DUBBLETT_META', 'Metabeskrivningen används av flera produkter'),
])


# ---------------------------------------------------------------- hjälpfunktioner

def sifferid(x):
    return re.sub(r'\D', '', str(x))


def tal(n):
    return f'{int(n):,}'.replace(',', ' ')


def proc(a, b, dec=0):
    if not b:
        return '–'
    if a and dec == 0 and 100.0 * a / b < 1:
        return '<1 %'
    return f'{100.0 * a / b:.{dec}f}'.replace('.', ',') + ' %'


def rensa(text):
    """Tar bort e-post, telefonnummer och allt som liknar nycklar. Körs på ALLT som skrivs ut."""
    t = str(text)
    t = re.sub(r'[\w.+-]+@[\w-]+(\.[\w-]+)+', '[e-postadress]', t)
    t = re.sub(r'\bshp[a-z]{1,3}_[A-Za-z0-9]{8,}\b', '[nyckel borttagen]', t)
    t = re.sub(r'(?i)(client[_ ]?secret|access[_ ]?token|api[_ ]?key)(\s*[:=]\s*)\S+', r'\1\2[borttagen]', t)
    t = re.sub(r'\b[A-Fa-f0-9]{32,}\b', '[nyckel borttagen]', t)
    t = re.sub(r'(?<![\w/])(\+\d{2}[ \d-]{8,}\d|0\d{1,3}[- ]\d{2,3}[ -]?\d{2}[ -]?\d{2})(?![\w/])', '[telefonnummer]', t)
    return t


def text_ur_html(h, block_start=None, maxlen=None):
    t = htmlmod.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'</(p|li|h\d|div)>', ' ', h or '')))
    t = re.sub(r'\s+', ' ', t).strip()
    if block_start and block_start in t:
        t = t.split(block_start)[0].strip()
    if maxlen and len(t) > maxlen:
        t = t[:maxlen].rsplit(' ', 1)[0] + ' …'
    return t


def las_json(sokvag, problem):
    try:
        with open(sokvag, encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:  # trasig eller saknad fil ska aldrig stoppa rapporten
        problem.append(f'Kunde inte läsa {os.path.basename(sokvag)}: {type(e).__name__}')
        return None


def las_text(sokvag, problem):
    try:
        with open(sokvag, encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        problem.append(f'Kunde inte läsa {os.path.basename(sokvag)}: {type(e).__name__}')
        return ''


def expandera(rot, monster, problem=None):
    """Glob-mönster (relativa mot rot) till sorterad, unik fillista."""
    if isinstance(monster, str):
        monster = [monster]
    ut = []
    for m in monster or []:
        sok = m if os.path.isabs(m) else os.path.join(rot, m)
        fynd = sorted(glob.glob(sok))
        if not fynd and problem is not None:
            problem.append(f'Inga filer matchar {m}')
        for f in fynd:
            if f not in ut and os.path.isfile(f):
                ut.append(f)
    return ut


def poster_ur(filer, problem, kraver=('id',)):
    ut = []
    for f in filer:
        d = las_json(f, problem)
        if isinstance(d, dict):
            d = d.get('data', d)
            d = d.get('nodes', d) if isinstance(d, dict) else d
        if not isinstance(d, list):
            continue
        for p in d:
            if isinstance(p, dict) and all(k in p for k in kraver):
                ut.append((f, p))
    return ut


# ---------------------------------------------------------------- profil, spärrlista, regelbok

def las_profil(sokvag, problem):
    p = las_json(sokvag, problem) if sokvag and os.path.exists(sokvag) else None
    if p is None:
        if sokvag:
            problem.append('Butiksprofilen saknas eller kunde inte läsas; standardgränser används.')
        p = {}
    g = dict(GRANSER_STANDARD)
    g.update(p.get('gransvarden') or {})
    p['gransvarden'] = g
    return p


def las_sparrar(rot, sokvag, problem):
    """Returnerar (id -> lista (spärrnamn, känd överträdelse)), lista över aktiva spärrar med antal id."""
    cfg = las_json(sokvag, problem) if sokvag and os.path.exists(sokvag) else None
    if not cfg:
        problem.append('Spärrlistan saknas; ingen spärrkontroll gjordes.')
        return {}, []
    ut, undantag, oversikt = {}, set(), []
    for s in cfg.get('sparrar', []):
        if not s.get('aktiv'):
            continue
        idfil = os.path.join(rot, s['idfil'])
        ids = []
        try:
            with open(idfil, encoding='utf-8') as f:
                ids = [sifferid(r[s['idkolumn']]) for r in csv.DictReader(f)]
        except Exception as e:
            problem.append(f'Spärrens idfil kunde inte läsas ({s.get("namn")}): {type(e).__name__}')
        if s.get('typ') == 'undantag':
            undantag.update(ids)
            oversikt.append({'namn': s.get('namn'), 'typ': 'undantag', 'antal': len(set(ids)), 'skal': s.get('skal', ''), 'beslut': s.get('beslut', '')})
            continue
        kanda = {sifferid(k) for k in s.get('kanda_overtradelser', [])}
        for i in ids:
            ut.setdefault(i, []).append((s.get('namn'), i in kanda))
        oversikt.append({'namn': s.get('namn'), 'typ': 'spärr', 'antal': len(set(ids)), 'skal': s.get('skal', ''), 'beslut': s.get('beslut', '')})
    for i in undantag:
        ut.pop(i, None)
    return ut, oversikt


def las_regelbok(sokvag, problem):
    """Plockar rader som '- R4 (T/G) text'. Första förekomsten av varje kod gäller; senare tillägg ignoreras här."""
    if not sokvag or not os.path.exists(sokvag):
        problem.append('Regelboken saknas; regeltabellen utelämnas.')
        return collections.OrderedDict()
    regler = collections.OrderedDict()
    for rad in las_text(sokvag, problem).splitlines():
        m = re.match(r'^\s*[-*]\s*(R\d+[a-z]?)\s*\(([TGM/]+)\)\s*(.*)$', rad)
        if m and m.group(1) not in regler:
            regler[m.group(1)] = (m.group(2), m.group(3).strip())
    return regler


# ---------------------------------------------------------------- slutlig text per produkt, kontroller

def stam(sokvag):
    return re.sub(r'_(resultat|fore)(_[a-z\-]+)?\.json$', '', os.path.basename(sokvag))


def ar_korr(filnamn, korr_monster):
    if isinstance(korr_monster, str):
        korr_monster = [korr_monster]
    return any(k and k in filnamn for k in (korr_monster or []))


def ordna_skrivfiler(filer, datum_per_stam, korr_monster='korr'):
    """Äldst först; rättningsfiler (filnamn med något av korr_monster) sist, så att de väger tyngst (som nattkontroll.py)."""
    def nyckel(f):
        b = os.path.basename(f)
        return (1 if ar_korr(b, korr_monster) else 0, datum_per_stam.get(b[:-5], ''), b)
    return sorted(filer, key=nyckel)


def slutlig_text(skrivfiler, datum_per_stam, korr_monster, problem):
    """Senast avsedda text per produkt. Returnerar (id -> (post, filnamn)), antal skrivfiler per id, id i rättningsfiler."""
    senast, antal_filer, korr_ids = {}, collections.Counter(), set()
    for f in ordna_skrivfiler(skrivfiler, datum_per_stam, korr_monster):
        d = las_json(f, problem)
        if not isinstance(d, list):
            continue
        sedda = set()
        for p in d:
            if isinstance(p, dict) and 'id' in p and 'html' in p:
                i = sifferid(p['id'])
                senast[i] = (p, os.path.basename(f))
                if i not in sedda:
                    antal_filer[i] += 1
                    sedda.add(i)
                if ar_korr(os.path.basename(f), korr_monster):
                    korr_ids.add(i)
    return senast, antal_filer, korr_ids


def kontrollera_produkt(p, profil, sparr, tillatna_versaler, forbjudna, max_attr, attr_fras):
    """Returnerar lista av (kontrollkod, förklaring). Rena funktioner av profilen, inget butiksspecifikt i koden."""
    g = profil['gransvarden']
    fynd = []
    i = sifferid(p.get('id'))
    titel, seo, meta, html = p.get('titel') or '', p.get('seo_title') or '', p.get('meta') or '', p.get('html') or ''
    for namn, kand in sparr.get(i, []):
        fynd.append(('SPARRAD_KAND' if kand else 'SPARRAD', namn))
    if len(titel) > g['titel_max']:
        fynd.append(('TITEL_LANG', f'{len(titel)} tecken (gräns {g["titel_max"]})'))
    kommatecken = len(re.findall(r'(?<!\d),|,(?!\d)', titel))  # decimalkomma (60,5) räknas inte
    if kommatecken > g['titel_max_komma']:
        fynd.append(('TITEL_KOMMA', f'{kommatecken} kommatecken'))
    if seo and len(seo) > g['seo_titel_max']:
        fynd.append(('SEO_LANG', f'{len(seo)} tecken (gräns {g["seo_titel_max"]})'))
    if meta and not g['meta_min'] <= len(meta) <= g['meta_max']:
        fynd.append(('META_LANGD', f'{len(meta)} tecken (tillåtet {g["meta_min"]}–{g["meta_max"]})'))
    if not meta:
        fynd.append(('META_SAKNAS', ''))
    for krav in profil.get('standardblock_krav', []):
        if krav not in html:
            fynd.append(('BLOCK', f'saknar "{krav}"'))
    for m in profil.get('marken', []):
        if m.upper() == m or m.upper() in (profil.get('marken_versaler_tillatna') or {}):
            continue
        for faltnamn, falt in (('titel', titel), ('SEO-titel', seo)):
            if falt and re.search(r'\b' + re.escape(m.upper()) + r'\b', falt) and m not in (profil.get('marken_varning_bara') or []):
                fynd.append(('VERSALER', f'{m} i {faltnamn}'))
    alltext = ' '.join([titel, seo, meta, html])
    if re.search('[­​‌‍ ﻿]', alltext):
        fynd.append(('OSYNLIG', 'mjukt bindestreck, nollbredd, hårt mellanslag eller BOM'))
    if len(re.findall(re.escape(attr_fras), html, re.I)) > max_attr:
        fynd.append(('ATTRIBUERING', f'fler än {max_attr} gånger'))
    for monster, skal in forbjudna:
        if re.search(monster, alltext, re.I):
            fynd.append(('FORBJUDET', skal))
    if re.search(r'\b([A-ZÅÄÖ][\wåäö-]+(?: [\wåäö-]+){0,3}) är (?:en|ett) \1\b', html, re.I):
        fynd.append(('CIRKULAR', ''))
    return fynd


def kontrollera_alla(senast, profil, sparr, forbjudna, max_attr, attr_fras):
    tillatna = profil.get('marken_versaler_tillatna') or {}
    per_kod = collections.OrderedDict((k, []) for k in KONTROLLNAMN)
    for i, (p, fil) in senast.items():
        for kod, forklaring in kontrollera_produkt(p, profil, sparr, tillatna, forbjudna, max_attr, attr_fras):
            per_kod[kod].append((i, p.get('nr'), forklaring))
    for kod, falt in (('DUBBLETT_TITEL', 'titel'), ('DUBBLETT_SEO', 'seo_title'), ('DUBBLETT_META', 'meta')):
        c = collections.Counter(p.get(falt) for p, _ in senast.values() if p.get(falt))
        for i, (p, fil) in senast.items():
            if p.get(falt) and c[p[falt]] > 1:
                per_kod[kod].append((i, p.get('nr'), f'delas med {c[p[falt]] - 1} till'))
    return per_kod


# ---------------------------------------------------------------- avvisade, utlåtanden, återläsning, stickprov

def klassa_avvisad(skal):
    """Kategorin vars ord förekommer tidigast i motiveringen (vid lika placering vinner listans ordning)."""
    bast = None
    for ordning, (namn, monster) in enumerate(AVVISAD_KATEGORIER):
        m = re.search(monster, skal or '', re.I)
        if m and (bast is None or (m.start(), ordning) < bast[0]):
            bast = ((m.start(), ordning), namn)
    return bast[1] if bast else 'Övrigt'


def normtext(s):
    return re.sub(r'[\W_]+', '', (s or '').lower())


def rattningstyp(fore, efter):
    """'format' om bara versaler, mellanslag eller skiljetecken ändras; annars 'innehåll' (som mat_utbyte.py)."""
    if fore is None or efter is None:
        return 'innehåll'
    return 'format' if normtext(fore) == normtext(efter) else 'innehåll'


def sammanfatta_utlatanden(poster):
    dom, falt, typer, orsaker, regelref = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
    unika = set()
    for fil, x in poster:
        d = str(x.get('dom', ''))[:6].upper()
        dom[d] += 1
        unika.add(sifferid(x.get('id')))
        for r in re.findall(r'\bR(\d+[a-z]?)\b', str(x.get('skal', ''))):
            regelref['R' + r] += 1
        if d.startswith('RÄTTA'):
            for fld, chs in (x.get('rattningar') or {}).items():
                falt['html' if str(fld).startswith('html') else 'meta' if str(fld).startswith('meta') else fld] += 1
                for ch in (chs if isinstance(chs, list) else [chs]):
                    if isinstance(ch, dict):
                        typer[rattningstyp(ch.get('fore'), ch.get('efter'))] += 1
            skal = str(x.get('skal', ''))
            orsaker[next((n for n, m in RATTNING_ORSAKER if re.search(m, skal, re.I)), 'Övrigt')] += 1
    return {'dom': dom, 'falt': falt, 'typer': typer, 'orsaker': orsaker, 'regelref': regelref, 'unika': len(unika)}


def tolka_resultat(sokvag, problem):
    d = las_json(sokvag, problem)
    if not isinstance(d, dict):
        return None
    skr = d.get('skrivna_taggade_verifierade', d.get('skrivna_och_verifierade', []))
    lika = d.get('redan_lika', d.get('redan_klara', []))
    return {'fil': os.path.basename(sokvag), 'stam': stam(sokvag), 'datum': str(d.get('datum', '')), 'lage': d.get('lage', ''),
            'skrivna': [sifferid(i) for i in skr], 'lika': [sifferid(i) for i in lika],
            'avvikelser': list(d.get('avvikelser', [])), 'hoppade': list(d.get('hoppade_over', [])), 'anrop': int(d.get('anrop', 0) or 0)}


def tolka_skrivrapport(text):
    m = re.search(r'(\d+) av (\d+)[^\n]{0,60}identiska', text) or re.search(r'identiska[^\n]{0,60}?(\d+) av (\d+)', text)
    return (int(m.group(1)), int(m.group(2))) if m else None


def tolka_stickprov(sokvag, problem):
    """JSON-sidovagn (rekommenderat): {"lasta":N,"jamforda":N,"avvikelser":N,"fynd":{"A":n,"B":n,"C":n},"skrivfiler":[...]}.
    Markdown-rapporter tolkas ungefärligt med textmönster och markeras som sådana."""
    namn = os.path.basename(sokvag)
    if sokvag.endswith('.json'):
        d = las_json(sokvag, problem)
        if not isinstance(d, dict):
            return None
        return {'fil': namn, 'rubrik': d.get('namn', namn), 'jamforda': d.get('jamforda'), 'lasta': d.get('lasta'), 'avvikelser': d.get('avvikelser'),
                'fynd': d.get('fynd'), 'nämnda': list(d.get('skrivfiler', [])), 'maskinlasbar': True}
    text = las_text(sokvag, problem)
    rubrik = next((r.lstrip('# ').strip() for r in text.splitlines() if r.startswith('#')), namn)
    lasta = None
    for rad in text.splitlines()[:120]:
        if re.search(r'läst|jämför|identisk|stämmer|live', rad, re.I):
            m = re.search(r'\b(\d+) av (\d+)\b', rad)
            if m:
                lasta = (int(m.group(1)), int(m.group(2)))
                break
    avv = None
    m = re.search(r'\b(\d+) avvikelse', text)
    if m:
        avv = int(m.group(1))
    elif re.search(r'(Ingen|Inga)[^\n]{0,30}avvikelse|\*\*Ingen\*\*|\b0 avvikelser', text, re.I):
        avv = 0
    fynd = collections.Counter(re.findall(r'\((A|B|C)[,)\s]', text))
    return {'fil': namn, 'rubrik': rubrik, 'jamforda': lasta[0] if lasta else None, 'lasta': lasta[1] if lasta else None, 'avvikelser': avv,
            'fynd': dict(fynd) if fynd else None, 'text': text, 'maskinlasbar': False}


def tolka_efterkontroll(text):
    ut = {}
    for nyckel, monster in (('kontrollerade produkter', r'Kontrollerade produkter:\s*(\d+)'), ('kända avvikelser (baslinje)', r'Kända avvikelser[^:]*:\s*(\d+)'),
                            ('nya avvikelser', r'Nya avvikelser:\s*\**\s*(\d+)')):
        m = re.search(monster, text)
        if m:
            ut[nyckel] = int(m.group(1))
    return ut


# ---------------------------------------------------------------- före/efter

def valj_original(fore_poster, senast, klartagg):
    """Första före-läget per produkt som är ett riktigt original: utan klartaggen och inte lika med slutlig text."""
    orig = {}
    for fil, n in fore_poster:
        i = sifferid(n.get('id'))
        if i not in senast or i in orig:
            continue
        if klartagg and klartagg in (n.get('tags') or []):
            continue
        p = senast[i][0]
        if n.get('title') == p.get('titel') and n.get('descriptionHtml') == p.get('html'):
            continue
        orig[i] = n
    return orig


def fore_efter_matt(orig, senast, profil):
    g = profil['gransvarden']
    block = (profil.get('standardblock_krav') or [None])[0]
    rader = []
    n = len(orig)
    if not n:
        return None
    def andel(f):
        return sum(1 for i in orig if f(orig[i], senast[i][0]))
    def median_len(f):
        v = [len(text_ur_html(f(orig[i], senast[i][0]), block)) for i in orig]
        return int(statistics.median(v)) if v else 0
    return {
        'n': n,
        'meta': (andel(lambda b, a: (b.get('seo') or {}).get('description')), andel(lambda b, a: a.get('meta'))),
        'seo': (andel(lambda b, a: len((b.get('seo') or {}).get('title') or b.get('title') or '') <= g['seo_titel_max']),
                andel(lambda b, a: len(a.get('seo_title') or a.get('titel') or '') <= g['seo_titel_max'])),
        'titel': (andel(lambda b, a: len(b.get('title') or '') <= g['titel_max']), andel(lambda b, a: len(a.get('titel') or '') <= g['titel_max'])),
        'block': (andel(lambda b, a: block and block in text_ur_html(b.get('descriptionHtml'))) if block else 0,
                  andel(lambda b, a: block and block in text_ur_html(a.get('html'))) if block else 0),
        'langd': (median_len(lambda b, a: b.get('descriptionHtml')), median_len(lambda b, a: a.get('html'))),
    }


def valj_exempel(orig, senast, antal, fro):
    ids = sorted(orig, key=lambda i: hashlib.sha1((str(fro) + i).encode()).hexdigest())
    return ids[:antal]


# ---------------------------------------------------------------- bygg rapport

def bygg_underlag(manifest, rot):
    """Läser allt material och räknar. Returnerar en dict som `skriv_markdown` renderar. Inga sidoeffekter."""
    problem = []
    m = manifest
    profil = las_profil(os.path.join(rot, m['profil']) if m.get('profil') else None, problem)
    sparr, sparr_oversikt = las_sparrar(rot, os.path.join(rot, m['sparrlista']) if m.get('sparrlista') else None, problem)
    regelbok = las_regelbok(os.path.join(rot, m['regelbok']) if m.get('regelbok') else None, problem)

    def hamta(nyckel):
        return expandera(rot, m.get(nyckel, []), problem)
    f_inv, f_utk, f_avv, f_utl = hamta('inventering'), hamta('utkast'), hamta('avvisade'), hamta('utlatanden')
    f_skr, f_fore, f_res = hamta('skrivfiler'), hamta('fore'), hamta('resultat')
    f_skrrapp, f_stick = hamta('skrivrapporter'), hamta('stickprov')

    resultat = [r for r in (tolka_resultat(f, problem) for f in f_res) if r]
    datum_per_stam = {}
    for r in resultat:
        if r['datum'] > datum_per_stam.get(r['stam'], ''):
            datum_per_stam[r['stam']] = r['datum']
    korr = m.get('korrigeringsmonster', 'korr')
    senast, antal_filer, korr_ids = slutlig_text(f_skr, datum_per_stam, korr, problem)

    inv_ids = {sifferid(p['id']) for _, p in poster_ur(f_inv, problem)}
    utkast_ids = {sifferid(p['id']) for _, p in poster_ur(f_utk, problem)}
    avvisade = collections.OrderedDict()
    for fil, p in poster_ur(f_avv, problem):
        avvisade[sifferid(p['id'])] = (p.get('nr'), p.get('skäl') or p.get('skal') or p.get('avvisningsskal') or p.get('orsak') or '', os.path.basename(fil))
    skrivna = set(senast)
    kvar_avvisade = {i: v for i, v in avvisade.items() if i not in skrivna}
    omprovade = [i for i in avvisade if i in skrivna]

    utl = poster_ur(f_utl, problem, kraver=('id', 'dom'))
    utl_sam = sammanfatta_utlatanden(utl)

    ver_ids, lika_ids, avv_resultat, hopp = set(), set(), [], 0
    for r in resultat:
        ver_ids.update(r['skrivna'])
        lika_ids.update(r['lika'])
        avv_resultat.extend((r['fil'], a) for a in r['avvikelser'])
        hopp += len(r['hoppade'])
    verifierade_skrivna = (ver_ids | lika_ids) & skrivna
    utan_maskinresultat = skrivna - verifierade_skrivna
    skrivrapport_tolkade = []
    for f in f_skrrapp:
        t = tolka_skrivrapport(las_text(f, problem))
        skrivrapport_tolkade.append((os.path.basename(f), t))

    stickprov = [s for s in (tolka_stickprov(f, problem) for f in f_stick) if s]
    kanda_stam = {os.path.basename(f)[:-5]: f for f in f_skr}
    for s in stickprov:
        namnda = set()
        kallor = s['nämnda'] if s.get('maskinlasbar') else re.findall(r'[\w\-]+_skriv[\w\-]*', s.get('text', ''))
        for st in kallor:
            st = re.sub(r'\.json$', '', st)
            if st in kanda_stam:
                namnda.add(st)
        ids = set()
        for st in namnda:
            d = las_json(kanda_stam[st], problem)
            if isinstance(d, list):
                ids.update(sifferid(p['id']) for p in d if isinstance(p, dict) and 'id' in p)
        s['ids'] = ids & skrivna
        s['nämnda_filer'] = sorted(namnda)
    stick_ids = set().union(*[s['ids'] for s in stickprov]) if stickprov else set()

    fore = poster_ur(f_fore, problem)
    orig = valj_original(fore, senast, profil.get('klartagg'))
    matt = fore_efter_matt(orig, senast, profil)
    ex_cfg = m.get('exempel') or {}
    exempel_ids = valj_exempel(orig, senast, int(ex_cfg.get('antal', 5)), ex_cfg.get('fro', 'kvalitetsrapport'))

    max_attr = int((profil.get('kvalitetsrapport') or {}).get('max_enligt_tillverkaren', 2))
    attr_fras = (profil.get('kvalitetsrapport') or {}).get('attribution_fras', 'enligt tillverkaren')
    forbjudna = (profil.get('kvalitetsrapport') or {}).get('forbjudna_uttryck', FORBJUDNA_STANDARD)
    kontroller = kontrollera_alla(senast, profil, sparr, forbjudna, max_attr, attr_fras)

    efter = []
    for f in expandera(rot, m.get('efterkontroll', []), problem):
        efter.append((os.path.basename(f), las_text(f, problem)))

    oppna = []
    if m.get('oppna_fragor'):
        sok = os.path.join(rot, m['oppna_fragor'])
        d = las_json(sok, problem) if os.path.exists(sok) else None
        if isinstance(d, list):
            oppna = [x for x in d if isinstance(x, dict) and x.get('status') != 'avklarad']

    regel_i_avvisade = collections.Counter()
    for v in avvisade.values():
        for r in re.findall(r'\bR(\d+[a-z]?)\b', v[1]):
            regel_i_avvisade['R' + r] += 1

    datum = sorted(d for d in datum_per_stam.values() if d)
    return {
        'manifest': m, 'profil': profil, 'problem': problem, 'regelbok': regelbok, 'sparr_oversikt': sparr_oversikt,
        'antal_filer': {'inventering': len(f_inv), 'utkast': len(f_utk), 'avvisade': len(f_avv), 'utlatanden': len(f_utl), 'skrivfiler': len(f_skr),
                        'fore': len(f_fore), 'resultat': len(f_res), 'skrivrapporter': len(f_skrrapp), 'stickprov': len(f_stick)},
        'inv_ids': inv_ids, 'utkast_ids': utkast_ids, 'skrivna': skrivna, 'avvisade': avvisade, 'kvar_avvisade': kvar_avvisade, 'omprovade': omprovade,
        'senast': senast, 'antal_filer_per_id': antal_filer, 'korr_ids': korr_ids,
        'utlatanden': utl_sam, 'n_utlatanden': len(utl), 'resultat': resultat, 'ver_ids': ver_ids, 'lika_ids': lika_ids,
        'verifierade_skrivna': verifierade_skrivna, 'utan_maskinresultat': utan_maskinresultat, 'avv_resultat': avv_resultat, 'hoppade': hopp,
        'skrivrapporter': skrivrapport_tolkade, 'stickprov': stickprov, 'stick_ids': stick_ids,
        'orig': orig, 'matt': matt, 'exempel_ids': exempel_ids, 'kontroller': kontroller, 'efter': efter, 'oppna': oppna,
        'regel_i_avvisade': regel_i_avvisade, 'period': (datum[0][:10], datum[-1][:10]) if datum else None,
        'max_attr': max_attr,
    }


def tabell(rubriker, rader):
    ut = ['| ' + ' | '.join(rubriker) + ' |', '|' + '---|' * len(rubriker)]
    for r in rader:
        ut.append('| ' + ' | '.join(str(c).replace('|', '/').replace('\n', ' ') for c in r) + ' |')
    return '\n'.join(ut)


def skriv_markdown(u, datum):
    m, profil = u['manifest'], u['profil']
    butik = m.get('butik', 'butiken')
    block = (profil.get('standardblock_krav') or [None])[0]
    n_skr = len(u['skrivna'])
    inventerade = len(u['inv_ids'] | u['utkast_ids'] | u['skrivna'] | set(u['avvisade']))
    ut = []
    P = ut.append
    P(f'# Kvalitetsrapport: {m.get("namn", butik)}')
    P('')
    P(f'*Butik: {butik}. Rapportdatum: {datum}.' + (f' Körningens resultatfiler är daterade {u["period"][0]} till {u["period"][1]}.' if u['period'] else '') + '*')
    P('')
    P('Rapporten är ett bevis, inte reklam: den visar vad som skrevs, vad som kontrollerades, hur ofta något behövde rättas och var det finns svagheter. '
      'Allt är uträknat ur körningens egna filer utan nätverksåtkomst; rapporten har inte tittat i butiken. Siffror som bara kan tolkas ungefärligt är markerade.')
    P('')

    # --- sammanfattning
    ud = u['utlatanden']
    n_dom = sum(ud['dom'].values())
    god, ratta, under = ud['dom'].get('GODKÄN', 0), ud['dom'].get('RÄTTA', 0), ud['dom'].get('UNDERK', 0)
    P('## Sammanfattning')
    P('')
    P(f'- **Omfattning:** {tal(n_skr)} produkter har fått ny text av totalt {tal(inventerade)} som ingick i körningen. '
      f'{tal(len(u["kvar_avvisade"]))} avvisades med skäl och väntar på beslut eller bättre underlag.')
    if n_dom:
        P(f'- **Granskning före skrivning:** {proc(god, n_dom)} av granskarnas utlåtanden godkände texten direkt, {proc(ratta, n_dom)} krävde rättning och {proc(under, n_dom)} underkändes.')
    P(f'- **Återläsning:** {tal(len(u["verifierade_skrivna"]))} av {tal(n_skr)} skrivna produkter har ett maskinläsbart resultat där butiken lästes tillbaka och jämfördes; '
      f'{tal(len(u["avv_resultat"]))} avvikelser registrerades. {tal(len(u["utan_maskinresultat"]))} produkter saknar maskinläsbart resultat (se Svagheter).')
    tot_fynd = sum(len(v) for k, v in u['kontroller'].items() if k not in ('META_SAKNAS', 'SPARRAD_KAND'))
    P(f'- **Regelkontroll i efterhand:** {tal(len([1 for k, v in u["kontroller"].items() if v and k not in ("META_SAKNAS", "SPARRAD_KAND")]))} av {len(KONTROLLNAMN) - 2} kontrolltyper gav fynd, sammanlagt {tal(tot_fynd)} fynd.')
    P(f'- **Vad kräver ditt beslut:** {tal(len(u["oppna"]))} öppna frågor och {len(set(klassa_avvisad(v[1]) for v in u["kvar_avvisade"].values()))} grupper av avvisade produkter (se avsnitt 9).')
    P('')

    # --- 1 omfattning
    P('## 1. Omfattning')
    P('')
    rader = [
        ('Produkter i körningen (unika)', tal(inventerade), 'Inventerade, utkastade, skrivna eller avvisade'),
        ('Skrivna (ny text i butiken)', tal(n_skr), f'{proc(n_skr, inventerade)} av körningen'),
        ('Avvisade och ännu inte skrivna', tal(len(u['kvar_avvisade'])), f'{proc(len(u["kvar_avvisade"]), inventerade)}; skäl i avsnitt 8'),
        ('Avvisade först, skrivna senare (omprövade)', tal(len(u['omprovade'])), 'Beslut eller regeländring gjorde att de kunde skrivas'),
        ('Varken skrivna eller avvisade', tal(max(0, inventerade - n_skr - len(u['kvar_avvisade']))), 'Väntar, hör till senare batcher eller ersatta batchar'),
    ]
    tb = m.get('totalt_i_butiken') or {}
    if tb.get('antal'):
        rader.append(('Aktiva produkter i butiken (uppgiven)', tal(tb['antal']), f'Källa: {tb.get("kalla", "manifestet")}'))
    P(tabell(['Mått', 'Antal', 'Kommentar'], rader))
    P('')
    P('Underlag: ' + ', '.join(f'{k} {v} filer' for k, v in u['antal_filer'].items() if v) + '.')
    P('')

    # --- 2 före/efter
    P('## 2. Före och efter')
    P('')
    mt = u['matt']
    if mt:
        n = mt['n']
        P(f'Jämförelsen gäller de {tal(n)} skrivna produkter där körningen sparade butikens ursprungliga läge före skrivning '
          f'(före-fil utan färdigtaggen och skild från slutlig text). Övriga {tal(n_skr - n)} saknar användbart före-läge i materialet.')
        P('')
        P(tabell(['Mått', 'Före', 'Efter'], [
            ('Har metabeskrivning', proc(mt['meta'][0], n), proc(mt['meta'][1], n)),
            ('SEO-titel inom längdgränsen (titeln används när SEO-titel saknas)', proc(mt['seo'][0], n), proc(mt['seo'][1], n)),
            ('Titel inom längdgränsen', proc(mt['titel'][0], n), proc(mt['titel'][1], n)),
            ('Har standardblocket' + (f' ("{block}")' if block else ''), proc(mt['block'][0], n), proc(mt['block'][1], n)),
            ('Median beskrivningslängd utan standardblock (tecken)', tal(mt['langd'][0]), tal(mt['langd'][1])),
        ]))
        P('')
        P('Mått som *inte* kan utläsas ur materialet: om texterna ger fler besök eller köp. Det kräver en separat mätning.')
    else:
        P('Inga användbara före-filer hittades, så före/efter-siffror kan inte räknas. (Före-filer sparas av skrivskripten före varje skrivning.)')
    P('')
    if u['exempel_ids']:
        P(f'### Exempel ({len(u["exempel_ids"])} av {tal(len(u["orig"]))}, slumpmässigt urval med fast frö, inte handplockat)')
        P('')
        for i in u['exempel_ids']:
            b, (a, fil) = u['orig'][i], u['senast'][i]
            P(f'**Produkt {a.get("nr") or i}** (skrivfil `{fil}`)')
            P('')
            P(tabell(['Fält', 'Före', 'Efter'], [
                ('Titel', rensa(b.get('title') or '–'), rensa(a.get('titel') or '–')),
                ('SEO-titel', rensa((b.get('seo') or {}).get('title') or '(ingen egen)'), rensa(a.get('seo_title') or '(ingen egen)')),
                ('Metabeskrivning', rensa((b.get('seo') or {}).get('description') or '–'), rensa(a.get('meta') or '–')),
                ('Beskrivning (början, utan standardblock)', rensa(text_ur_html(b.get('descriptionHtml'), block, 320) or '–'), rensa(text_ur_html(a.get('html'), block, 320) or '–')),
            ]))
            P('')

    # --- 3 regler
    P('## 3. Regler som tillämpats')
    P('')
    P('Reglerna är de som körningens regelbok anger. **T** = kontrolleras av skript, **G** = kontrolleras av en granskare, **M** = kräver mänskligt beslut. '
      'Kolumnerna visar hur ofta regelkoden nämns i granskarnas motiveringar respektive i skälen för avvisade produkter (det är en ungefärlig fingervisning om vilka regler som styrde mest, inte en fullständig räkning).')
    P('')
    if u['regelbok']:
        rr = []
        for kod, (typ, text) in u['regelbok'].items():
            rr.append((kod, typ, rensa(text[:150] + ('…' if len(text) > 150 else '')), ud['regelref'].get(kod, 0), u['regel_i_avvisade'].get(kod, 0)))
        P(tabell(['Regel', 'Typ', 'Innehåll (förkortat)', 'Nämnd i granskning', 'Nämnd i avvisade'], rr))
        P('')
    g = profil['gransvarden']
    P('Butiksprofilens gränsvärden: ' + f'titel högst {g["titel_max"]} tecken och högst {g["titel_max_komma"]} kommatecken, SEO-titel högst {g["seo_titel_max"]}, '
      f'metabeskrivning {g["meta_min"]}–{g["meta_max"]} tecken.')
    if profil.get('utanfor_tills_vidare'):
        P('')
        P('Kategorier som butiken valt att hålla utanför tills vidare: ' + '; '.join(profil['utanfor_tills_vidare']) + '.')
    P('')

    # --- 4 kontroller
    P('## 4. Kontrollresultat')
    P('')
    P(f'Kontrollerna kördes **i efterhand** på den senast avsedda texten för varje skriven produkt ({tal(n_skr)} st). '
      'De är desamma som skripten använder före skrivning, men en produkt kan ha skrivits under en äldre version av reglerna, så ett fynd här är inte alltid ett fel i processen. '
      'Ett fynd kan också vara ett medvetet, beslutat undantag; då anges det.')
    P('')
    kr = []
    for kod, namn in KONTROLLNAMN.items():
        f = u['kontroller'][kod]
        ex = ', '.join(str(x[1] or x[0]) for x in f[:5]) + (' …' if len(f) > 5 else '')
        kr.append((namn, tal(len(f)), proc(len(f), n_skr, 1), ex or '–'))
    P(tabell(['Kontroll', 'Produkter med fynd', 'Andel av skrivna', 'Exempel (nr eller id)'], kr))
    P('')
    P('"Metabeskrivning saknas" är en varning, inte ett fel: en kort sann beskrivning föredras framför utfyllnad, men en saknad meta är en förlorad möjlighet i sökresultaten.')
    P('')

    # --- 5 granskning
    P('## 5. Granskning före skrivning')
    P('')
    if n_dom:
        P(f'Ett utkast skrivs av en modell och granskas sedan av en andra, starkare modell som dömer GODKÄND, RÄTTA (med exakt före/efter) eller UNDERKÄND. '
          f'Underlaget är {tal(n_dom)} utlåtanden över {tal(ud["unika"])} unika produkter (en produkt kan ha granskats flera gånger, så siffrorna är per utlåtande).')
        P('')
        avv_dom = ud['dom'].get('AVVISA', 0)
        P(tabell(['Utfall', 'Antal', 'Andel'], [
            ('Godkänd direkt', tal(god), proc(god, n_dom)), ('Rättas före skrivning', tal(ratta), proc(ratta, n_dom)),
            ('Underkänd', tal(under), proc(under, n_dom)), ('Avvisad av granskaren', tal(avv_dom), proc(avv_dom, n_dom))]))
        P('')
        tf = ud['typer']
        nt = sum(tf.values())
        if nt:
            P(f'Av {tal(nt)} enskilda rättningar var {proc(tf.get("format", 0), nt)} rena formatändringar (versaler, mellanslag, skiljetecken) och {proc(tf.get("innehåll", 0), nt)} ändrade innehållet (ord, uppgifter eller betydelse). '
              'Det betyder att skriptkontroller av format inte räcker för att ersätta granskningen.')
            P('')
        if ud['falt']:
            P('Fält som rättades: ' + ', '.join(f'{k} ({tal(v)})' for k, v in ud['falt'].most_common()) + '.')
            P('')
        if ud['orsaker']:
            P('Vanligaste skälen till rättning (ordsökning i granskarens motivering, ungefärlig): ' + '; '.join(f'{k} ({tal(v)})' for k, v in ud['orsaker'].most_common()) + '.')
            P('')
    else:
        P('Inga maskinläsbara utlåtanden fanns i materialet.')
        P('')

    # --- 6 återläsning och stickprov
    P('## 6. Återläsning och stickprov')
    P('')
    ra = u['resultat']
    P(f'**Återläsning:** efter skrivning läser skriptet tillbaka varje produkt från butiken och jämför titel, SEO och beskrivning tecken för tecken mot skrivfilen. '
      f'Materialet har {tal(len(ra))} sådana resultatfiler med sammanlagt {tal(sum(r["anrop"] for r in ra))} anrop.')
    P('')
    P(tabell(['Mått', 'Antal'], [
        ('Skrivna, taggade och verifierade', tal(len(u['ver_ids']))),
        ('Redan lika vid körning (inget skrevs)', tal(len(u['lika_ids']))),
        ('Hoppade över', tal(u['hoppade'])),
        ('Avvikelser vid återläsning', tal(len(u['avv_resultat']))),
        ('Skrivna produkter utan maskinläsbart resultat', tal(len(u['utan_maskinresultat'])))]))
    P('')
    if u['avv_resultat']:
        P('Registrerade avvikelser (de första 10): ' + '; '.join(rensa(f'{f}: {a}')[:140] for f, a in u['avv_resultat'][:10]))
        P('')
    sr = u['skrivrapporter']
    tolkade = [(f, t) for f, t in sr if t]
    if sr:
        P(f'**Skrivrapporter (text):** {len(sr)} rapporter lästes; i {len(tolkade)} gick en uppgift av typen "N av M identiska" att utläsa automatiskt '
          f'({tal(sum(t[0] for _, t in tolkade))} av {tal(sum(t[1] for _, t in tolkade))} identiska). Det är ett textutdrag, inte en maskinell kontroll.')
        P('')
    st = u['stickprov']
    if st:
        P(f'**Stickprov:** ett stickprov är en separat, enbart läsande kontroll av en slumpad del av de skrivna produkterna, gjord av en annan modell än den som skrev. '
          f'Materialet har {len(st)} stickprovsrapporter.')
        P('')
        maskin = [s for s in st if s.get('maskinlasbar')]
        sj = [s for s in st if s['jamforda'] is not None and s['lasta'] is not None]
        sa = [s for s in st if s['avvikelser'] is not None]
        P(tabell(['Mått', 'Värde'], [
            ('Rapporter totalt / maskinläsbara (JSON)', f'{len(st)} / {len(maskin)}'),
            ('Rapporter där antal lästa kunde utläsas (ungefärligt ur text)', f'{len(sj)}'),
            ('Summa lästa produkter i dessa (kan innehålla dubbletter)', tal(sum(s['lasta'] for s in sj))),
            ('Rapporter med utläst avvikelseantal', f'{len(sa)}'),
            ('Summa avvikelser mot skrivfil i dessa', tal(sum(s['avvikelser'] for s in sa))),
            ('Skrivna produkter som ingår i nämnda skrivfiler', f'{tal(len(u["stick_ids"]))} av {tal(n_skr)} ({proc(len(u["stick_ids"]), n_skr)})')]))
        P('')
        P('Stickprovets *språkgranskning* gav fynd i klartext (kategori A = bör rättas före publik trafik, B = bör rättas, C = smaklig anmärkning). '
          'Dessa fynd är inte maskinläsbara i hela materialet, så de räknas inte här; läs rapporterna för detaljer:')
        P('')
        for s in st[:12]:
            P(f'- `{s["fil"]}`: {rensa(s["rubrik"])[:110]}' + (f' (lästa {s["jamforda"]} av {s["lasta"]}' + (f', avvikelser {s["avvikelser"]}' if s['avvikelser'] is not None else '') + ')' if s['jamforda'] is not None else ''))
        if len(st) > 12:
            P(f'- … och {len(st) - 12} till.')
        P('')
    else:
        P('Inga stickprovsrapporter fanns i materialet.')
        P('')

    # --- 7 mätetal
    P('## 7. Mätetal')
    P('')
    rattade = len(u['korr_ids'] & u['skrivna'])
    flera = sum(1 for i in u['skrivna'] if u['antal_filer_per_id'][i] > 1)
    P(tabell(['Mätetal', 'Värde', 'Hur det räknats'], [
        ('Andel godkända direkt', proc(god, n_dom), f'{tal(god)} av {tal(n_dom)} utlåtanden (inte per produkt)'),
        ('Andel som krävde rättning före skrivning', proc(ratta, n_dom), f'{tal(ratta)} av {tal(n_dom)} utlåtanden'),
        ('Rättningar efter skrivning', f'{tal(rattade)} produkter ({proc(rattade, n_skr, 1)} av skrivna)',
         'Produkter som finns i rättningsfiler (filnamn med "' + '" eller "'.join(([m['korrigeringsmonster']] if isinstance(m.get('korrigeringsmonster'), str) else m.get('korrigeringsmonster')) or ['korr']) + '"), det vill säga skrevs om efter fynd i stickprov eller kontroll'),
        ('Skrivna i mer än en skrivfil', f'{tal(flera)} produkter ({proc(flera, n_skr, 1)})', 'Rättning, omkörning eller delmängdsfil (till exempel kanarie); senaste versionen gäller'),
        ('Avvikelser vid återläsning', f'{tal(len(u["avv_resultat"]))} av {tal(len(u["ver_ids"]) + len(u["lika_ids"]))} återlästa', 'Från resultatfilerna; gäller bara produkter med maskinläsbart resultat'),
        ('Stickprovens täckning', proc(len(u['stick_ids']), n_skr), 'Övre gräns: alla produkter i de skrivfiler som stickproven nämner'),
        ('Produkter med någon kontrollvarning idag', proc(len({x[0] for k, v in u['kontroller'].items() if k not in ('META_SAKNAS', 'SPARRAD_KAND') for x in v}), n_skr, 1), 'Efterhandskontroll enligt avsnitt 4, utan varning om saknad meta')]))
    P('')

    # --- 8 avvisade
    P('## 8. Avvisade produkter och varför')
    P('')
    kv = u['kvar_avvisade']
    if kv:
        P(f'{tal(len(kv))} produkter avvisades och är inte skrivna. Att avvisa är ett resultat, inte ett misslyckande: det är bättre att inte skriva än att skriva något som inte stämmer med källan. '
          'Skälen är sorterade efter det ord som förekommer tidigast i den fria motiveringen (ungefärlig sortering).')
        P('')
        per = collections.OrderedDict()
        for i, (nr, skal, fil) in kv.items():
            per.setdefault(klassa_avvisad(skal), []).append((i, nr, skal))
        rader = []
        for k, v in sorted(per.items(), key=lambda kv_: -len(kv_[1])):
            rader.append((k, tal(len(v)), proc(len(v), len(kv)), rensa(v[0][2])[:140].replace('\n', ' ')))
        P(tabell(['Skäl (grupp)', 'Antal', 'Andel', 'Exempel på motivering'], rader))
        P('')
    else:
        P('Inga avvisade produkter fanns i materialet.')
        P('')

    # --- 9 beslut
    P('## 9. Vad som kräver ditt beslut')
    P('')
    if u['oppna']:
        P('**Öppna frågor (från körningens frågelista):**')
        P('')
        for x in u['oppna']:
            P(f'- {x.get("id", "")} ({x.get("datum", "")}): {rensa(x.get("fraga", ""))}')
        P('')
    if kv:
        P('**Grupper av avvisade produkter:**')
        P('')
        per = collections.Counter(klassa_avvisad(v[1]) for v in kv.values())
        P(tabell(['Grupp', 'Antal', 'Beslut som behövs'], [(k, tal(c), AVVISAD_ATGARD.get(k, AVVISAD_ATGARD['Övrigt'])) for k, c in per.most_common()]))
        P('')
    if u['sparr_oversikt']:
        P('**Aktiva spärrar (produkter som medvetet inte får skrivas):**')
        P('')
        P(tabell(['Spärr', 'Typ', 'Antal produkter', 'Skäl och beslut'], [(s['namn'], s['typ'], tal(s['antal']), rensa((s['skal'] + ' ' + s['beslut']).strip())[:200]) for s in u['sparr_oversikt']]))
        P('')
    if not (u['oppna'] or kv or u['sparr_oversikt']):
        P('Inga öppna beslut hittades i materialet.')
        P('')

    # --- efterkontroll
    if u['efter']:
        P('## 10. Läget efter skrivning')
        P('')
        for fil, text in u['efter']:
            e = tolka_efterkontroll(text)
            if e:
                P(f'- `{fil}`: ' + ', '.join(f'{k} {tal(v)}' for k, v in e.items()))
            else:
                arch = len(re.findall(r'\|\s*ARCHIVED\s*\|', text))
                P(f'- `{fil}`: ' + (f'{tal(arch)} produkter markerade ARCHIVED i listan' if arch else 'ingen siffra kunde utläsas'))
        P('')
        P('Siffrorna ovan kommer från separata kontroller som körts efter skrivningen (till exempel en daglig läsande kontroll). De visar om texterna ligger kvar, och fångar bland annat att andra system (till exempel leverantörens synk) ändrar eller arkiverar produkter efter att vi skrivit.')
        P('')

    # --- svagheter
    P('## Svagheter och osäkerheter')
    P('')
    sv = []
    if u['utan_maskinresultat']:
        sv.append(f'**Återläsning saknas i maskinläsbar form för {tal(len(u["utan_maskinresultat"]))} av {tal(n_skr)} skrivna produkter** ({proc(len(u["utan_maskinresultat"]), n_skr)}). '
                  'De skrevs innan skripten sparade resultatfiler; återläsningen dokumenterades då i text och gjordes delvis för hand. Det är sämre bevis än en maskinell jämförelse.')
    if kv:
        sv.append('Sorteringen av avvisade produkter och av rättningsorsaker bygger på ordsökning i fri text och är ungefärlig.')
    sv.append('"Godkända direkt" räknas per utlåtande, inte per produkt. En produkt som rättats och granskats på nytt räknas flera gånger.')
    if st:
        osakra = [s for s in st if not s.get('maskinlasbar')]
        sv.append(f'{len(osakra)} av {len(st)} stickprovsrapporter är skrivna som fri text; antal lästa och avvikelser är utlästa med textmönster och kan vara fel i enskilda fall. '
                  'Språkfynden (A/B/C) i stickproven är inte sammanräknade, så andelen produkter med kvarstående fynd är okänd.')
    sv.append('Stickprovens täckning är en övre gräns (alla produkter i nämnda skrivfiler), inte antalet faktiskt lästa produkter.')
    if rattade:
        sv.append(f'{tal(rattade)} skrivna produkter behövde skrivas om efter att fel hittats i stickprov eller kontroll. Det visar att granskning före skrivning inte fångar allt.')
    for k in ('SPARRAD',):
        if u['kontroller'][k]:
            n_sp = len(u['kontroller'][k])
            sv.append(f'**{tal(n_sp)} spärrad{"" if n_sp == 1 else "e"} produkt{"" if n_sp == 1 else "er"} har fått text** trots spärrlistan (se avsnitt 4), och överträdelsen är inte redovisad som känd i spärrlistan. Orsaken framgår inte av materialet och bör utredas.')
    if u['kontroller']['META_SAKNAS']:
        sv.append(f'{tal(len(u["kontroller"]["META_SAKNAS"]))} produkter saknar metabeskrivning i sin avsedda text (tunn källa), vilket är en kvarstående förlorad SEO-möjlighet.')
    if mt and mt['n'] < n_skr:
        sv.append(f'Före/efter-siffrorna bygger på {tal(mt["n"])} av {tal(n_skr)} produkter (de med bevarat original). De är inte representativa med säkerhet för resten.')
    sv.append('Rapporten visar att texterna följer reglerna och stämmer med butiken vid skrivtillfället. Den visar **inte** att uppgifterna i källan är sanna, att texterna säljer bättre eller att de ligger kvar i butiken idag; se avsnitt 10 om en efterkontroll finns.')
    sv.append('Regelkontrollerna i avsnitt 4 är skripttester av form och förbjudna uttryck. De kan inte avgöra om en sakuppgift är rätt; det är granskarens och stickprovets uppgift.')
    for p in u['problem'][:10]:
        sv.append(f'Materialfel: {rensa(p)}')
    for s in sv:
        P('- ' + s)
    P('')
    P('---')
    P(f'*Genererad av `kvalitetsrapport.py` (offline). Inga nycklar, kunduppgifter eller personuppgifter ingår; e-postadresser och telefonnummer maskeras automatiskt.*')
    return rensa('\n'.join(ut) + '\n')


# ---------------------------------------------------------------- HTML

def _inline(t):
    t = htmlmod.escape(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return t


def md_till_html(md, titel='Kvalitetsrapport'):
    ut, rader, i = [], md.splitlines(), 0
    while i < len(rader):
        r = rader[i]
        if r.startswith('|'):
            tab = []
            while i < len(rader) and rader[i].startswith('|'):
                tab.append(rader[i]); i += 1
            celler = lambda s: [c.strip() for c in s.strip().strip('|').split(' | ')] if ' | ' in s else [c.strip() for c in s.strip().strip('|').split('|')]
            ut.append('<div class="tab"><table><thead><tr>' + ''.join(f'<th>{_inline(c)}</th>' for c in celler(tab[0])) + '</tr></thead><tbody>')
            for t in tab[2:]:
                ut.append('<tr>' + ''.join(f'<td>{_inline(c)}</td>' for c in celler(t)) + '</tr>')
            ut.append('</tbody></table></div>')
            continue
        if r.startswith('#'):
            n = len(r) - len(r.lstrip('#'))
            ut.append(f'<h{n}>{_inline(r[n:].strip())}</h{n}>')
        elif r.startswith('- '):
            ut.append('<ul>')
            while i < len(rader) and rader[i].startswith('- '):
                ut.append(f'<li>{_inline(rader[i][2:])}</li>'); i += 1
            ut.append('</ul>')
            continue
        elif r.strip() == '---':
            ut.append('<hr>')
        elif r.strip():
            ut.append(f'<p>{_inline(r)}</p>')
        i += 1
    css = ('<style>:root{--bg:#fff;--fg:#1d2327;--mut:#5b6670;--line:#d7dde2;--acc:#0b5cab;--card:#f5f7f9}'
           '@media (prefers-color-scheme:dark){:root{--bg:#14181c;--fg:#e6eaee;--mut:#9aa6b2;--line:#2c353d;--acc:#6db1ff;--card:#1c2228}}'
           'body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,-apple-system,Segoe UI,sans-serif}'
           'main{max-width:960px;margin:0 auto;padding:24px 16px 64px}h1{font-size:1.7rem}h2{margin-top:2.2rem;border-bottom:1px solid var(--line);padding-bottom:.3rem}'
           'h3{margin-top:1.6rem}.tab{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:.92rem;margin:.6rem 0}'
           'th,td{border:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}th{background:var(--card)}'
           'code{background:var(--card);padding:1px 4px;border-radius:3px;font-size:.88em}a{color:var(--acc)}hr{border:0;border-top:1px solid var(--line)}'
           'em{color:var(--mut)}</style>')
    return ('<!doctype html><html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{htmlmod.escape(titel)}</title>{css}</head><body><main>' + '\n'.join(ut) + '</main></body></html>\n')


# ---------------------------------------------------------------- CLI

def kor(manifest_sokvag, rot=None, datum=None):
    rot = rot or ROT_STANDARD
    problem = []
    manifest = las_json(manifest_sokvag, problem)
    if not isinstance(manifest, dict):
        raise SystemExit('Manifestet kunde inte läsas: ' + '; '.join(problem))
    u = bygg_underlag(manifest, rot)
    return skriv_markdown(u, datum or datetime.date.today().isoformat()), u


def main(argv=None):
    ap = argparse.ArgumentParser(description='Genererar kvalitetsrapport (offline).')
    ap.add_argument('--manifest', required=True)
    ap.add_argument('--rot', default=ROT_STANDARD, help='Katalog som sökvägar i manifestet räknas från (standard: repots rot)')
    ap.add_argument('--ut', help='Markdown-fil att skriva (annars standard ut)')
    ap.add_argument('--html', action='store_true', help='Skriv även en fristående HTML-fil bredvid --ut')
    ap.add_argument('--datum', help='Rapportdatum ÅÅÅÅ-MM-DD (standard: idag)')
    a = ap.parse_args(argv)
    md, u = kor(a.manifest, a.rot, a.datum)
    if a.ut:
        os.makedirs(os.path.dirname(os.path.abspath(a.ut)), exist_ok=True)
        with open(a.ut, 'w', encoding='utf-8') as f:
            f.write(md)
        if a.html:
            with open(os.path.splitext(a.ut)[0] + '.html', 'w', encoding='utf-8') as f:
                f.write(md_till_html(md, u['manifest'].get('namn', 'Kvalitetsrapport')))
        print(f'Skrev {a.ut} ({len(md)} tecken, {len(u["skrivna"])} skrivna produkter, {len(u["problem"])} materialvarningar).')
    else:
        sys.stdout.write(md)


if __name__ == '__main__':
    main()
