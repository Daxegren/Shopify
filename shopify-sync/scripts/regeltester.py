#!/usr/bin/env python3
"""Regeltester: automatiska kontroller av återkommande granskningsfynd (utöver skrivfil_kontroll.py).

Varje kontroll tar ett utkast (dict med titel, seo_title, meta, html) och returnerar en lista fynd
(kod, fält, utdrag). Alla kontroller börjar i läget "varning": de stoppar ingenting. Läget per kontroll
styrs av shopify-sync/config/regeltester.json ("varning", "fel" eller "av"). Skrivfil_kontroll.py anropar
`kontrollera_utkast()` och skriver ut resultatet separat från de gamla kontrollerna.

Underlag och mätning: shopify-sync/status/regeltester-matning.md (skapas av mat_regeltester.py).
Nätverksfri. Körs med python3 -I (importera via sys.path.insert i anropande skript).
"""
import json, os, re, collections

HAR = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.abspath(os.path.join(HAR, '..', '..'))
CFG_SOKVAG = os.path.join(ROT, 'shopify-sync', 'config', 'regeltester.json')
PROFIL_SOKVAG = os.path.join(ROT, 'shopify-sync', 'config', 'butiksprofil-bestofsports.json')

Fynd = collections.namedtuple('Fynd', 'kod falt text')

STANDARD_CFG = {
    'standardlage': 'varning',
    'lage': {},
    'extra_marken': [],
    'butiksord': {},
    'engelska_typord': [],
    'kvalitetsord': [],
}


def las_cfg(sokvag=CFG_SOKVAG):
    cfg = json.loads(json.dumps(STANDARD_CFG))
    if sokvag and os.path.exists(sokvag):
        with open(sokvag, encoding='utf-8') as fh:
            cfg.update(json.load(fh))
    return cfg


def las_marken(sokvag=PROFIL_SOKVAG):
    if sokvag and os.path.exists(sokvag):
        with open(sokvag, encoding='utf-8') as fh:
            return json.load(fh).get('marken', [])
    return []


# ---------- hjälpfunktioner ----------

def text_utan_taggar(html):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html or '')).strip()


def enheter(html):
    """Delar html i meningar/rader: varje <li> är en enhet, löptext delas vid punkt."""
    ut = []
    for m in re.finditer(r'<li>(.*?)</li>', html or '', re.S):
        ut.append(text_utan_taggar(m.group(1)))
    rest = re.sub(r'<li>.*?</li>', ' ', html or '', flags=re.S)
    for stycke in re.split(r'</p>|</h\d>|<br\s*/?>', rest):
        t = text_utan_taggar(stycke)
        if t:
            ut.extend(s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-ZÅÄÖ])', t) if s.strip())
    return ut


def prosa_falt(x):
    """(fältnamn, text utan taggar) för meta och html."""
    return [('meta', x.get('meta') or ''), ('html', text_utan_taggar(x.get('html')))]


def alla_falt(x):
    return [(k, text_utan_taggar(x.get(k)) if k == 'html' else (x.get(k) or '')) for k in ('titel', 'seo_title', 'meta', 'html')]


# ---------- kontroller ----------
KONTROLLER = collections.OrderedDict()


def kontroll(kod, regel, beskrivning):
    def deko(fn):
        fn.kod, fn.regel, fn.beskrivning = kod, regel, beskrivning
        KONTROLLER[kod] = fn
        return fn
    return deko


ENHET_EFTER_TAL = r'(?=\s?(?:mm|cm|kg|g\b|tum|-tum|ml|l\b|W\b|Wh|V\b|Ah|km|kW|"|–|x\b|m\b))'


@kontroll('DECIMALPUNKT', 'R9', 'Decimalpunkt i stället för decimalkomma när talet följs av enhet (27.5 tum, 52.5 mm)')
def decimalpunkt(x, cfg):
    f = []
    for falt, t in alla_falt(x):
        m = re.search(r'(?:(?<=x)|(?<![\w.,/:-]))\d{1,3}\.[1-9]\d?' + ENHET_EFTER_TAL, t)
        if m:
            f.append(Fynd('DECIMALPUNKT', falt, m.group(0)))
    return f


@kontroll('TUM_SKARM', 'R10', '"N tum skärm/display" ska skrivas "N-tums skärm" i löptext')
def tum_skarm(x, cfg):
    f = []
    mon = re.compile(r'\b\d+(?:,\d+)?\s+tums?\s+(?:\S+\s+){0,2}?\S*(?:skärm|display)\b', re.I)
    for falt, t in prosa_falt(x):
        m = mon.search(t)
        if m:
            f.append(Fynd('TUM_SKARM', falt, m.group(0)))
    return f


@kontroll('TUM_HJUL', 'R10', '"N tum(s) hjul/däck" ska skrivas "N-tumshjul" (granskarna är inte konsekventa, se mätningen)')
def tum_hjul(x, cfg):
    f = []
    mon = re.compile(r'\b\d+(?:,\d+)?\s+tums?\s+\S*(?:hjul|däck|fälg)\b', re.I)
    for falt, t in prosa_falt(x):
        m = mon.search(t)
        if m:
            f.append(Fynd('TUM_HJUL', falt, m.group(0)))
    return f


@kontroll('APOSTROF', 'R8', 'Accent (´) eller bakåtlutande apostrof i stället för vanlig apostrof (S\'cool)')
def apostrof(x, cfg):
    f = []
    for falt, t in alla_falt(x):
        m = re.search(r'\S*[´`]\S*', t)
        if m:
            f.append(Fynd('APOSTROF', falt, m.group(0)))
    return f


@kontroll('ENHET_FORM', 'R9', 'Enhet skriven fel: PSI/HK/KG/CM/MM i versaler eller "hp" (svenska: psi, hk, kg, cm, mm)')
def enhet_form(x, cfg):
    f = []
    for falt, t in alla_falt(x):
        m = re.search(r'\b(?:PSI|HK)\b|\b\d+(?:,\d+)?\s?(?:KG|CM|MM|Kg|Cm|Mm)\b|\bhp\b', t)
        if m:
            f.append(Fynd('ENHET_FORM', falt, m.group(0)))
    return f


@kontroll('BUTIKSORD', 'R7', 'Ord som butiken inte använder (se butiksord i config/regeltester.json, t.ex. scooter → sparkcykel)')
def butiksord(x, cfg):
    f = []
    ordlista = cfg.get('butiksord') or {}
    if not ordlista:
        return f
    mon = re.compile(r'\b\w*(?:' + '|'.join(re.escape(o) for o in ordlista) + r')\w*\b', re.I)
    for falt, t in alla_falt(x):
        m = mon.search(t)
        if m:
            f.append(Fynd('BUTIKSORD', falt, m.group(0)))
    return f


@kontroll('TYPORD_FEL_PLATS', 'R7', 'Titel eller SEO-titel börjar med märket i stället för typordet')
def typord_fel_plats(x, cfg):
    f = []
    marken = sorted(set(las_marken() + (cfg.get('extra_marken') or [])), key=len, reverse=True)
    for falt in ('titel', 'seo_title'):
        t = (x.get(falt) or '').strip()
        for m in marken:
            if t.lower().startswith(m.lower() + ' ') or t.lower() == m.lower():
                f.append(Fynd('TYPORD_FEL_PLATS', falt, t[:len(m)]))
                break
    return f


@kontroll('ENGELSKT_TYPORD', 'R7', 'Engelskt typord (se engelska_typord i config/regeltester.json) i titel, SEO-titel eller text')
def engelskt_typord(x, cfg):
    f = []
    ordlista = cfg.get('engelska_typord') or []
    if not ordlista:
        return f
    mon = re.compile(r'\b(?:' + '|'.join(ordlista) + r')\b', re.I)  # poster i engelska_typord är reguljära uttryck
    for falt, t in alla_falt(x):
        m = mon.search(t)
        if m:
            f.append(Fynd('ENGELSKT_TYPORD', falt, m.group(0)))
    return f


@kontroll('CIRKULAR_TYPORD', 'R11', 'Första meningen "Namn är en/ett typord" där typordet är samma ord som ett ord i namnet')
def cirkular_typord(x, cfg):
    f = []
    kallor = [('meta', x.get('meta') or '')]
    m1 = re.search(r'<p>(.*?)</p>', x.get('html') or '', re.S)
    if m1:
        kallor.append(('html', text_utan_taggar(m1.group(1))))
    for falt, t in kallor:
        m = re.match(r'^([A-ZÅÄÖ][^.,:;]{2,70}?) är (?:en|ett) ([\wåäöÅÄÖ-]+)', t)
        if not m:
            continue
        typ = m.group(2).lower()
        if any(len(n) >= 5 and n.lower() == typ for n in m.group(1).split()):
            f.append(Fynd('CIRKULAR_TYPORD', falt, m.group(0)))
    return f


@kontroll('KVALITETSORD_UTAN_ETV', 'R5', 'Kvalitets-, säkerhets- eller effektord utan "enligt tillverkaren" i samma mening eller rad')
def kvalitetsord_utan_etv(x, cfg):
    f = []
    ordlista = cfg.get('kvalitetsord') or []
    if not ordlista:
        return f
    mon = re.compile(r'\b(?:' + '|'.join(ordlista) + r')\w*', re.I)
    for falt, enh in (('meta', [x.get('meta') or '']), ('html', enheter(x.get('html')))):
        for e in enh:
            m = mon.search(e)
            if m and not re.search(r'enligt tillverkaren', e, re.I):
                f.append(Fynd('KVALITETSORD_UTAN_ETV', falt, m.group(0)))
                break
    return f


LASTRAD = re.compile(r'(?:max(?:imal)?\.?\s*(?:användar|drift)?vikt\w*|maximal belastning|belastning\w*|lastkapacitet|lastgräns|användarvikt|bärförmåga)[^.<]{0,40}?\d+(?:,\d+)?\s?kg', re.I)


@kontroll('LASTGRANS_UTAN_ETV', 'R4', 'Lastgräns/maxvikt i kg utan "enligt tillverkaren" någonstans bland lastuppgifterna')
def lastgrans_utan_etv(x, cfg):
    f = []
    enh = [e for e in ([x.get('meta') or ''] + enheter(x.get('html'))) if LASTRAD.search(e)]
    if enh and not any(re.search(r'enligt tillverkaren', e, re.I) for e in enh):
        f.append(Fynd('LASTGRANS_UTAN_ETV', 'html', LASTRAD.search(enh[0]).group(0)))
    return f


VERBER = (r'(?:är|var|har|ger|passar|finns|väger|mäter|består|används|kan|ingår|erbjuder|levereras|säljs|tillverkad|tillverkade|tillverkas|gör|gjord|gjorda|gjort|hjälper|följer|innehåller|fungerar|rymmer|kommer|uppfyller|möjliggör|ersätter|bygger|sitter|fästs|monteras|justeras|räcker|gäller|behövs|visar|kräver|saknar|tål|klarar|håller|skyddar|ligger|bär|löper|rullar|lyser|laddas|tar|får|ska|bör|måste|vill|går|står|hänger|täcker|omger|fäster|avsedd|avsedda|utrustad|utrustade|försedd|försedda|stödjer|kopplas|öppnas|vikas|viks|fälls|blir|bildar|skapar|ökar|minskar|reglerar|styr|mäts|anges|syns|täcks|inkluderar|medföljer|skickas|erbjuds)')


@kontroll('META_UTAN_VERB', 'R11', 'Metabeskrivningens första mening saknar verb (bredare verblista än den gamla kontrollen)')
def meta_utan_verb(x, cfg):
    t = x.get('meta') or ''
    if not t:
        return []
    forsta = re.split(r'(?<=[.!?])\s', t)[0]
    if re.search(r'\b' + VERBER + r'\b', forsta, re.I):
        return []
    return [Fynd('META_UTAN_VERB', 'meta', forsta[:60])]


# ---------- körning ----------

def lage_for(kod, cfg):
    return (cfg.get('lage') or {}).get(kod, cfg.get('standardlage', 'varning'))


def kontrollera_utkast(x, cfg=None):
    """Returnerar lista av (läge, Fynd). Läge 'av' hoppas över."""
    cfg = cfg or las_cfg()
    ut = []
    for kod, fn in KONTROLLER.items():
        lage = lage_for(kod, cfg)
        if lage == 'av':
            continue
        for fy in fn(x, cfg):
            ut.append((lage, fy))
    return ut


if __name__ == '__main__':
    import sys
    for fil in sys.argv[1:]:
        for d in json.load(open(fil, encoding='utf-8')):
            for lage, fy in kontrollera_utkast(d):
                print(f"{d.get('nr')} ({d.get('id')}): [{lage}] {fy.kod} i {fy.falt}: {fy.text}")
