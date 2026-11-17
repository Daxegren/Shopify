#!/usr/bin/env python3
"""Fullständig återläsning av skrivna texter i BEST OF SPORTS. ENDAST LÄSNING mot Shopify (nodes(ids), högst 10 per anrop).

Underkommandon:
  las --cache FIL [--prov N]   läser live till en lokal cachefil (JSON, aldrig i repot, aldrig nycklar) och skriver tid/rate limit
  klassa --cache FIL --ut KAT  jämför live mot senast avsedd text och klassar varje avvikelse; skriver CSV och sammanfattningsdata
Senast avsedd text = den senaste skrivfilen per produkt i rapporter/facit-bos-2026-10-31/vag2_skriv/. Ordningen mellan skrivfiler
styrs av resultatfilernas tidsstämplar (rapporter/shopify-original-*/*_resultat_*.json); saknas tidsstämpel markeras ordningen
som osäker i stället för att gissas. Skriver aldrig till Shopify. Nycklar läses bara ur miljön och maskeras.
"""
import collections, csv, glob, json, os, re, sys, time

HAR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HAR)
import shopify_api as api  # noqa: E402

ROT = os.path.abspath(os.path.join(HAR, '..', '..'))
SKRIV = os.path.join(ROT, 'rapporter', 'facit-bos-2026-10-31', 'vag2_skriv')
NORM = ' (enligt tillverkaren)'
PROFIL = os.path.join(ROT, 'shopify-sync', 'config', 'butiksprofil-bestofsports.json')
SLUT_UTRULLNING = '2026-11-08T23:59:59Z'  # beslutsloggen 2026-11-08: utrullningen avslutas


def sid(x):
    return re.sub(r'\D', '', str(x))


# ---------- avsedda texter ----------
def resultatdatum():
    """skrivfilsnamn -> senaste tidsstämpel i resultatfiler; id -> lista (datum, resultatfil) för registrerade skrivningar."""
    per_fil, per_id = {}, collections.defaultdict(list)
    for f in glob.glob(os.path.join(ROT, 'rapporter', 'shopify-original-*', '*resultat*.json')):
        b = os.path.basename(f)
        m = re.match(r'(.+?)_resultat', b)
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        if not (isinstance(d, dict) and d.get('datum') and m):
            continue
        per_fil[m.group(1) + '.json'] = max(per_fil.get(m.group(1) + '.json', ''), d['datum'])
        for k, v in d.items():
            if k in ('avvikelser', 'hoppade_over') or not isinstance(v, list):
                continue
            for i in v:
                if isinstance(i, (str, int)) and len(sid(i)) >= 12:
                    per_id[sid(i)].append((d['datum'], b))
    return per_fil, per_id


def kandidater():
    """id -> lista av (filnamn, post, datum_eller_None) i stigande ordning; sist = senast avsedd."""
    per_fil, _ = resultatdatum()
    kand = collections.defaultdict(list)
    for f in sorted(set(glob.glob(os.path.join(SKRIV, '*skriv*.json')))):
        b = os.path.basename(f)
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        for p in d:
            if isinstance(p, dict) and 'html' in p and 'id' in p:
                kand[str(p['id'])].append((b, p, per_fil.get(b)))
    ut, osakra = {}, set()
    for i, lst in kand.items():
        # med datum först (stigande), utan datum efter korr/längre namn (mindre säkert); osäker om flera kandidater saknar datum
        # rättningsfiler (korr) skrivs efter ursprungsfilerna; därefter datum; saknas datum gäller namnets längd (…_resten_1 efter …_resten)
        nyckel = lambda t: ('korr' in t[0], t[2] is not None, t[2] or '', len(t[0]), t[0])
        lst.sort(key=nyckel)
        texter = {json.dumps(falt_skriv(t[1]), sort_keys=True) for t in lst}
        if len(texter) > 1 and any(t[2] is None and 'korr' not in t[0] for t in lst):
            osakra.add(i)
        ut[i] = lst
    return ut, osakra


def extra_meta():
    """id -> lista av (källa, meta) från rensning 1/3 och kort_meta (äldre metaskrivningar utan beskrivning)."""
    ut = collections.defaultdict(list)
    for namn, falt, kalla in (('meta_rensning.json', 'meta_ny', 'rensning 1'), ('meta_rensning3.json', 'meta_ny', 'rensning 3'),
                              ('kort_meta_skriv.json', 'meta', 'kort meta')):
        try:
            for p in json.load(open(os.path.join(SKRIV, namn), encoding='utf-8')):
                ut[str(p['id'])].append((kalla, p.get(falt)))
        except Exception:
            pass
    return ut


def original_lagen():
    """id -> (titel, seo_title, meta, html) ur äldsta före-fil (leverantörens läge före våra skrivningar)."""
    ut = {}
    for f in sorted(glob.glob(os.path.join(ROT, 'rapporter', 'shopify-original-*', '**', '*fore*.json'), recursive=True)):
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        if isinstance(d, dict):
            d = d.get('data', d)
            d = d.get('nodes', d) if isinstance(d, dict) else d
            if isinstance(d, dict):
                d = [v for v in d.values() if isinstance(v, list)][:1] and [v for v in d.values() if isinstance(v, list)][0] or []
        for p in d if isinstance(d, list) else []:
            if isinstance(p, dict) and p.get('id') and 'descriptionHtml' in p and sid(p['id']) not in ut:
                s = p.get('seo') or {}
                ut[sid(p['id'])] = (p.get('title'), s.get('title') or p.get('title'), s.get('description'), p.get('descriptionHtml'))
    return ut


# ---------- läsning ----------
class SpelareTransport:
    """Omsluter transporten för att mäta tid, HTTP-status och Shopifys kostnads-/budgetfält. Loggar aldrig nycklar."""
    def __init__(self):
        self.lista = []
        self.inner = api._http_transport

    def __call__(self, url, headers, body, timeout=60):
        t0 = time.time()
        status, h, text = self.inner(url, headers, body, timeout)
        if 'graphql' in url:
            rec = {'t': round(time.time() - t0, 3), 'status': status}
            try:
                c = (json.loads(text).get('extensions') or {}).get('cost') or {}
                ts = c.get('throttleStatus') or {}
                rec.update(kostnad=c.get('actualQueryCost'), kvar=ts.get('currentlyAvailable'), max=ts.get('maximumAvailable'), aterstall=ts.get('restoreRate'))
            except Exception:
                pass
            self.lista.append(rec)
        return status, h, text


def las(cache, prov=None, ids=None):
    exp, _ = kandidater()
    ids = ids or list(exp)
    mal = json.load(open(os.path.join(ROT, 'rapporter', 'inventering-bos-2026-11-12', 'alla_produkter.json'), encoding='utf-8'))
    klara = [sid(p['id']) for p in mal if 'texter-klara' in p['tags']]
    alla = list(dict.fromkeys(list(ids) + klara))  # skrivfilsprodukter först, därefter de med taggen men utan skrivfil
    if prov:
        alla = alla[:prov]
    sp = SpelareTransport()
    k = api.ShopifyKlient(transport=sp)
    print('Butik:', api.verifiera_butik(k))
    data = json.load(open(cache, encoding='utf-8')) if os.path.exists(cache) else {}
    kvar = [i for i in alla if i not in data]
    t0 = time.time()
    for s in range(0, len(kvar), 10):
        del_ = kvar[s:s + 10]
        res = api.hamta_produkter(k, del_, del_storlek=10)
        for i, p in zip(del_, res):
            data[i] = p
        if (s // 10) % 25 == 24 or s + 10 >= len(kvar):
            json.dump(data, open(cache, 'w', encoding='utf-8'), ensure_ascii=False)
            print(f'  {len(data)} av {len(alla)} lästa, {int(time.time() - t0)} s, {k.antal_anrop} anrop', flush=True)
    json.dump(data, open(cache, 'w', encoding='utf-8'), ensure_ascii=False)
    ts = [r['t'] for r in sp.lista]
    kv = [r['kvar'] for r in sp.lista if r.get('kvar') is not None]
    n429 = sum(1 for r in sp.lista if r['status'] == 429)
    rapport = {'produkter_lasta': len(data), 'anrop_graphql': len(sp.lista), 'anrop_inkl_token': k.antal_anrop, 'http_429': n429,
               'sek_totalt': round(time.time() - t0, 1), 'sek_per_anrop_medel': round(sum(ts) / max(len(ts), 1), 2),
               'sek_per_anrop_max': max(ts or [0]), 'kostnad_per_anrop_medel': round(sum((r.get('kostnad') or 0) for r in sp.lista) / max(len(sp.lista), 1), 1),
               'budget_max': next((r.get('max') for r in sp.lista if r.get('max')), None), 'budget_lagsta_kvar': min(kv) if kv else None,
               'aterstallning_per_s': next((r.get('aterstall') for r in sp.lista if r.get('aterstall')), None)}
    print(json.dumps(rapport, ensure_ascii=False))
    return rapport


# ---------- klassning ----------
def falt_live(l):
    s = l.get('seo') or {}
    return {'titel': l.get('title'), 'seo_title': s.get('title') or l.get('title'), 'meta': s.get('description'), 'html': l.get('descriptionHtml')}


def falt_skriv(w):
    return {'titel': w['titel'], 'seo_title': w.get('seo_title') or w['titel'], 'meta': w.get('meta'), 'html': w['html']}


def klassa_produkt(i, l, lst, osaker, emeta, orig, per_id):
    """Returnerar (klass, avvikelsetyp, detalj, avvikande_falt)."""
    fl = falt_live(l)
    fa = falt_skriv(lst[-1][1])
    senaste_fil = lst[-1][0]
    diff = [k for k in ('titel', 'seo_title', 'meta', 'html') if not (k == 'meta' and lst[-1][1].get('meta') is None) and fl[k] != fa[k]]
    if not diff:
        if osaker:
            return 'identisk', 'identisk (ordning mellan skrivfiler ej styrkt)', senaste_fil, []
        return 'identisk', 'identisk', senaste_fil, []
    # 0. Shopify lagrar & som &amp; i beskrivningen
    if diff == ['html'] and fl['html'] == re.sub(r'&(?!amp;|nbsp;|lt;|gt;|quot;|#)', '&amp;', fa['html']):
        return 'identisk', 'identisk (Shopify lagrar & som &amp;)', senaste_fil, []
    # 1. bara rensning 2 (tillägg eller borttagning av " (enligt tillverkaren)")
    if diff == ['html'] and fl['html'].replace(NORM, '') == fa['html'].replace(NORM, ''):
        return 'ersatt', 'ersatt: rensning 2 (enligt tillverkaren på lastgräns)', senaste_fil, diff
    # 2. meta ersatt av rensning 1/3 eller kort meta
    if set(diff) <= {'meta'}:
        for kalla, m in emeta.get(i, []):
            if m == fl['meta']:
                return 'ersatt', f'ersatt: {kalla} (metabeskrivning)', senaste_fil, diff
    # 3. matchar annan skrivfil för samma produkt (äldre eller yngre)
    for fil, p, _ in reversed(lst[:-1]):
        fb = falt_skriv(p)
        if all(fl[k] == fb[k] or (k == 'meta' and p.get('meta') is None) for k in fl) or (fl['html'].replace(NORM, '') == fb['html'].replace(NORM, '') and all(fl[k] == fb[k] for k in ('titel', 'seo_title', 'meta'))):
            return 'ersatt', f'ersatt: matchar annan skrivfil ({fil}), senast avsedd {senaste_fil}' + (' [ordning ej styrkt]' if osaker else ''), senaste_fil, diff
    # 4. hel text lika med fältvis kombination av kända skrivningar (t.ex. ny meta + äldre beskrivning)
    ok_kalla = {k: [f for f in (falt_skriv(p)[k] for _, p, _ in lst)] + ([m for _, m in emeta.get(i, [])] if k == 'meta' else []) for k in ('titel', 'seo_title', 'meta', 'html')}
    if all(fl[k] in ok_kalla[k] or (k == 'html' and any(fl[k].replace(NORM, '') == h.replace(NORM, '') for h in ok_kalla[k])) for k in diff):
        return 'ersatt', 'ersatt: fältvis lika med kända skrivningar (blandning av skrivfiler)', senaste_fil, diff
    # 5. återställd till leverantörens original (synken återställer text)
    o = orig.get(i)
    if o and all(fl[k] == o[n] for k, n in zip(diff, [('titel', 'seo_title', 'meta', 'html').index(x) for x in diff])):
        return 'synk', 'ändrad efteråt: återställd till leverantörens ursprungstext (trolig leverantörssynk)', senaste_fil, diff
    # 6. ändrad efter utrullningens slut av automatik (heuristik: uppdaterad efter 2026-11-08, 03:00–04:00 UTC)
    u = l.get('updatedAt') or ''
    if u > SLUT_UTRULLNING and u[11:13] == '03':
        return 'synk', 'ändrad efteråt: uppdaterad 03:00–04:00 UTC efter utrullningens slut (trolig synk, heuristik)', senaste_fil, diff
    return 'okand', 'avviker utan känd orsak', senaste_fil, diff


def forsta_skillnad(a, b):
    a, b = a or '', b or ''
    for p, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return p
    return min(len(a), len(b))


def klassa(cache, ut):
    data = json.load(open(cache, encoding='utf-8'))
    exp, osakra = kandidater()
    emeta, orig = extra_meta(), original_lagen()
    _, per_id = resultatdatum()
    os.makedirs(ut, exist_ok=True)
    rader, antal, exempel = [], collections.Counter(), []
    for i, lst in exp.items():
        l = data.get(i)
        if not l:
            rader.append([i, 'saknas i butiken', 'produkten finns inte', '', '', '', '', ''])
            antal['saknas'] += 1
            continue
        klass, typ, fil, diff = klassa_produkt(i, l, lst, i in osakra, emeta, orig, per_id)
        antal[klass] += 1
        tag = 'texter-klara' in (l.get('tags') or [])
        rader.append([i, {'identisk': 'identisk', 'ersatt': 'ersatt av senare omskrivning', 'synk': 'ändrad efteråt av synk/automatik',
                          'okand': 'avviker utan känd orsak'}[klass], typ, ','.join(diff), fil, l.get('status'), 'ja' if tag else 'nej', l.get('updatedAt')])
        if klass == 'okand' and len(exempel) < 400:
            fl, fa = falt_live(l), falt_skriv(lst[-1][1])
            exempel.append({'id': i, 'titel_live': l.get('title'), 'status': l.get('status'), 'updatedAt': l.get('updatedAt'), 'fil': fil,
                            'falt': {k: {'live_tecken': len(fl[k] or ''), 'avsedd_tecken': len(fa[k] or ''), 'forsta_skillnad': forsta_skillnad(fl[k], fa[k]),
                                         'live': (fl[k] or '')[max(0, forsta_skillnad(fl[k], fa[k]) - 40):forsta_skillnad(fl[k], fa[k]) + 60],
                                         'avsedd': (fa[k] or '')[max(0, forsta_skillnad(fl[k], fa[k]) - 40):forsta_skillnad(fl[k], fa[k]) + 60]} for k in diff}})
    with open(os.path.join(ut, 'aterlasning_skrivna.csv'), 'w', newline='', encoding='utf-8') as o:
        w = csv.writer(o)
        w.writerow(['produkt_id', 'status', 'avvikelsetyp', 'avvikande_falt', 'senast_avsedd_skrivfil', 'status_i_butiken', 'har_texter_klara', 'senast_andrad_utc'])
        w.writerows(rader)
    json.dump({'antal': dict(antal), 'osakra_ordning': len(osakra), 'flerfilsprodukter': sum(1 for v in exp.values() if len(v) > 1)},
              open(os.path.join(ut, 'siffror_klassning.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(exempel, open(os.path.join(os.environ.get('ATERLASNING_ARBETE', '/tmp'), 'okanda_detaljer.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    typer = collections.Counter(r[2].split(' (')[0] if r[1] != 'identisk' else r[2] for r in rader)
    print(dict(antal), '\n', typer.most_common(20))
    return rader


def utan_fil(cache, ut, arbete):
    """Produkter med taggen texter-klara men utan skrivfil: bedöms mot regelbokens kontroller (skrivfil_kontroll.py och regeltester.py)."""
    import skrivfil_kontroll as sk
    data = json.load(open(cache, encoding='utf-8'))
    exp, _ = kandidater()
    prof = json.load(open(PROFIL, encoding='utf-8'))
    sk.las_profil(PROFIL)
    sparr = sk.las_sparr(os.path.join(ROT, 'shopify-sync', 'config', 'sparrlista.json'))
    lev, levtagg = prof.get('leveranstidsmening') or '', prof.get('leveranstidstagg') or 'På beställning'
    ids = [i for i, p in data.items() if p and i not in exp and 'texter-klara' in (p.get('tags') or [])]
    rader, summa, utkast = [], collections.Counter(), []
    for i in ids:
        l = data[i]
        f = falt_live(l)
        x = {'id': i, 'nr': i[-6:], 'titel': f['titel'], 'seo_title': f['seo_title'], 'meta': f['meta'], 'html': f['html'] or ''}
        utkast.append(x)
    tmp = os.path.join(arbete, 'utan_fil_utkast.json')
    json.dump(utkast, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False)
    n, fel, varn = sk.kontrollera(tmp, sparr, False)
    rf, rv = sk.kontrollera_regeltester(tmp)
    per = collections.defaultdict(list)
    for m in fel + varn + rf + rv:
        mm = re.match(r'.*? \((\d+)\): (.*)', m)
        if mm:
            per[mm.group(1)].append(mm.group(2))
    for x in utkast:
        i = x['id']; l = data[i]; html = x['html']; flaggor = list(per.get(i, []))
        if not x['meta']:
            flaggor.append('saknad metabeskrivning')
        besta = levtagg in (l.get('tags') or [])
        if besta and lev and lev not in html:
            flaggor.append('På beställning utan leveranstidsmening')
        if lev and lev in html and not besta:
            flaggor.append('leveranstidsmening utan taggen På beställning')
        if len(re.findall(r'enligt tillverkaren', html, re.I)) > 2:
            flaggor.append('"enligt tillverkaren" fler än två gånger')
        if i in sparr:
            flaggor.append(f'spärrad produkt ({sparr[i][0]}) – förväntat, ingen åtgärd')
        for fl_ in set(re.sub(r'\[.*?\] i \w+: .*', lambda m_: m_.group(0)[:m_.group(0).index(']') + 1], g) for g in flaggor):
            summa[fl_[:70]] += 1
        rader.append([i, l.get('status'), l.get('title'), len(flaggor), ' | '.join(flaggor)[:700]])
    with open(os.path.join(ut, 'aterlasning_utan_skrivfil.csv'), 'w', newline='', encoding='utf-8') as o:
        w = csv.writer(o)
        w.writerow(['produkt_id', 'status_i_butiken', 'titel', 'antal_varningar', 'varningar'])
        w.writerows(rader)
    json.dump({'antal': len(rader), 'med_varning': sum(1 for r in rader if r[3]), 'status': dict(collections.Counter(r[1] for r in rader)),
               'varningstyper': dict(summa.most_common())}, open(os.path.join(ut, 'siffror_utan_skrivfil.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(rader), 'produkter,', sum(1 for r in rader if r[3]), 'med varning;', summa.most_common(15))


def main(a):
    if not a:
        print(__doc__); return 2
    def arg(n, d=None):
        return a[a.index(n) + 1] if n in a else d
    if a[0] == 'las':
        las(arg('--cache'), int(arg('--prov')) if arg('--prov') else None)
    elif a[0] == 'klassa':
        klassa(arg('--cache'), arg('--ut'))
    elif a[0] == 'utan-fil':
        utan_fil(arg('--cache'), arg('--ut'), os.environ.get('ATERLASNING_ARBETE', '/tmp'))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv[1:]))
    except api.ShopifyFel as e:
        print('FEL:', api.maska(e)); sys.exit(1)
