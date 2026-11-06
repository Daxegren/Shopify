#!/usr/bin/env python3
"""Omkontroll av arkiverade produkter mot Velomarkets katalog. ENDAST LÄSNING (GET). Ändrar inget i Shopify eller Lovable.

Körs i Google Cloud Shell (Python 3, bara standardbiblioteket).
  export VELOMARKET_API_KEY='...'            # nyckeln sätts bara i ditt eget skal, aldrig i någon fil
  python3 omkontroll.py kontrollera  sku-lista.csv  ut1.csv     # körning 1
  (vänta minst 10 minuter)
  python3 omkontroll.py kontrollera  sku-lista.csv  ut2.csv     # körning 2
  python3 omkontroll.py sammanfatta  ut1.csv ut2.csv  resultat.csv

sku-lista.csv måste ha en kolumn som heter sku (gärna även velo_product_id och namn).
Klasser: FINNS_MED_LAGER, FINNS_UTAN_LAGER, BORTTAGEN (404 på både SKU och id i båda körningarna), OSAKER.
"""
import csv, json, os, sys, time, urllib.error, urllib.parse, urllib.request

BASE = 'https://b2b.velomarket.ee/api/v1/reseller'
PAUS = 0.6  # sekunder mellan anrop, för att vara snäll mot API:t


def hamta(path, nyckel):
    req = urllib.request.Request(BASE + path, headers={'Authorization': 'Bearer ' + nyckel, 'Accept': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read().decode('utf-8') or 'null')
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception:
        return 0, None  # nätverksfel/timeout räknas som osäkert


def produkt_ur_svar(data):
    if isinstance(data, dict):
        for k in ('data', 'product'):
            if isinstance(data.get(k), dict):
                return data[k]
        return data
    return None


def kontrollera_en(sku, vpid, nyckel):
    """Returnerar (utfall_sku, utfall_id, lager) där utfall är FINNS, 404 eller FEL."""
    def slag(status, data):
        if status == 200 and produkt_ur_svar(data):
            return 'FINNS'
        if status == 404:
            return '404'
        return 'FEL'
    s1, d1 = (hamta('/products/' + urllib.parse.quote(sku, safe=''), nyckel) if sku else (0, None))
    time.sleep(PAUS)
    s2, d2 = (hamta('/products/' + urllib.parse.quote(str(vpid), safe=''), nyckel) if vpid else (0, None))
    time.sleep(PAUS)
    u1 = slag(s1, d1) if sku else 'SAKNAS'
    u2 = slag(s2, d2) if vpid else 'SAKNAS'
    p = produkt_ur_svar(d1) if u1 == 'FINNS' else (produkt_ur_svar(d2) if u2 == 'FINNS' else None)
    lager = None
    if p is not None:
        v = p.get('stock', p.get('quantity'))
        try:
            lager = int(v)
        except (TypeError, ValueError):
            lager = None
    return u1, u2, lager


def klassa(rader):
    """rader: lista med (utfall_sku, utfall_id, lager) per körning. Samma svar i alla körningar krävs."""
    if any(u1 == 'FEL' or u2 == 'FEL' for u1, u2, _ in rader):
        return 'OSAKER'
    finns = [(u1 == 'FINNS' or u2 == 'FINNS') for u1, u2, _ in rader]
    if all(finns):
        lagr = [l for _, _, l in rader]
        if any(l is None for l in lagr):
            return 'OSAKER'
        return 'FINNS_MED_LAGER' if all(l > 0 for l in lagr) else ('FINNS_UTAN_LAGER' if all(l <= 0 for l in lagr) else 'OSAKER')
    if not any(finns) and all((u1 in ('404', 'SAKNAS') and u2 in ('404', 'SAKNAS')) and ('404' in (u1, u2)) for u1, u2, _ in rader):
        return 'BORTTAGEN'
    return 'OSAKER'


def kontrollera(inf, utf):
    nyckel = os.environ.get('VELOMARKET_API_KEY')
    if not nyckel:
        sys.exit('Sätt VELOMARKET_API_KEY i ditt skal först.')
    rader = list(csv.DictReader(open(inf, encoding='utf-8-sig')))
    if not rader or 'sku' not in rader[0]:
        sys.exit('Filen måste ha en kolumn som heter sku.')
    klart = {}
    if os.path.exists(utf):  # återuppta efter avbrott
        klart = {r['sku']: r for r in csv.DictReader(open(utf, encoding='utf-8'))}
    with open(utf, 'a' if klart else 'w', newline='', encoding='utf-8') as o:
        w = csv.writer(o)
        if not klart:
            w.writerow(['sku', 'velo_product_id', 'namn', 'utfall_sku', 'utfall_id', 'lager', 'tid'])
        n = 0
        for r in rader:
            sku = (r.get('sku') or '').strip()
            if not sku or sku in klart:
                continue
            vpid = (r.get('velo_product_id') or '').strip()
            u1, u2, lager = kontrollera_en(sku, vpid, nyckel)
            w.writerow([sku, vpid, r.get('namn', ''), u1, u2, '' if lager is None else lager, time.strftime('%Y-%m-%d %H:%M:%S')])
            o.flush(); n += 1
            if n % 25 == 0:
                print(f'{n} kontrollerade...', flush=True); time.sleep(5)  # paus mellan omgångar
    print('Klart:', utf)


def sammanfatta(filer, utf):
    per = {}
    for f in filer:
        for r in csv.DictReader(open(f, encoding='utf-8')):
            lager = int(r['lager']) if r['lager'] != '' else None
            per.setdefault(r['sku'], {'namn': r['namn'], 'vpid': r['velo_product_id'], 'k': []})['k'].append((r['utfall_sku'], r['utfall_id'], lager))
    antal = {}
    with open(utf, 'w', newline='', encoding='utf-8') as o:
        w = csv.writer(o); w.writerow(['sku', 'velo_product_id', 'namn', 'klass', 'lager_velomarket'])
        for sku, d in per.items():
            k = klassa(d['k']) if len(d['k']) >= len(filer) else 'OSAKER'
            antal[k] = antal.get(k, 0) + 1
            lagr = [l for _, _, l in d['k'] if l is not None]
            w.writerow([sku, d['vpid'], d['namn'], k, max(lagr) if lagr else ''])
    print(antal); print('Skrev', utf)


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) == 3 and a[0] == 'kontrollera':
        kontrollera(a[1], a[2])
    elif len(a) >= 4 and a[0] == 'sammanfatta':
        sammanfatta(a[1:-1], a[-1])
    else:
        print(__doc__)
