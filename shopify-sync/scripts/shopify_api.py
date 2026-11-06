#!/usr/bin/env python3
"""Litet bibliotek för Shopify Admin API (GraphQL) med client credentials-flödet.

Säkerhet: Klient-ID och Klienthemlighet läses bara ur miljövariabler (namnen anges av anroparen),
åtkomstnyckeln hålls bara i minnet (aldrig på disk) och alla felutskrifter maskeras med `maska()`.

Innehåll:
  ShopifyKlient      token i minnet, graphql() med återförsök vid rate limit och serverfel
  hamta_produkter    läser produkter via nodes(ids) i delar
  spara_fore         sparar komplett före-fil (id, title, handle, status, tags, seo, descriptionHtml)
  uppdatera_seo      productUpdate med seo{title description}, alltid båda fälten
  jamfor_efter       jämför återläst produkt mot förväntat läge, tecken för tecken
Tester utan nätverk: shopify-sync/scripts/test_shopify_api.py
"""
import json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

BUTIK = '6f2e53-67.myshopify.com'
API_VERSION = os.environ.get('SHOPIFY_API_VERSION', '2026-07')

PRODUKTFALT = '''id title handle status tags updatedAt
  seo { title description }
  descriptionHtml'''


class ShopifyFel(Exception):
    pass


# Namn (inte värden) på miljövariabler som en profil har pekat ut; maskas utöver SHOPIFY_CLIENT_*.
_EXTRA_HEMLIGA_VARIABLER = set()


def _hemligheter(extra=()):
    namn = {k for k in os.environ if k.startswith('SHOPIFY_CLIENT_')} | {k for k in _EXTRA_HEMLIGA_VARIABLER if k in os.environ}
    vals = [os.environ.get(k) for k in namn]
    return [v for v in list(vals) + list(extra) if v and len(v) >= 6]


def maska(text, extra=()):
    """Tar bort alla kända hemligheter och allt som liknar en åtkomstnyckel ur en text."""
    text = str(text)
    for h in _hemligheter(extra):
        text = text.replace(h, '***')
    return re.sub(r'\b(shp[a-z]{1,3}_[A-Za-z0-9]{8,})\b', '***', text)


def _http_transport(url, headers, body, timeout=60):
    """Standardtransport. Returnerar (status, svarshuvuden, text). Kastar inte vid HTTP-fel."""
    req = urllib.request.Request(url, data=body, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, dict(r.headers), r.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers or {}), e.read().decode('utf-8', 'replace')


class ShopifyKlient:
    def __init__(self, butik=BUTIK, id_var='SHOPIFY_CLIENT_ID_BOS', secret_var='SHOPIFY_CLIENT_SECRET_BOS',
                 transport=None, sleep=time.sleep, klocka=time.time, max_forsok=6):
        self.butik, self.id_var, self.secret_var = butik, id_var, secret_var
        _EXTRA_HEMLIGA_VARIABLER.update((id_var, secret_var))
        self._transport, self._sleep, self._klocka, self.max_forsok = transport or _http_transport, sleep, klocka, max_forsok
        self._token = None
        self._giltig_till = 0
        self.antal_anrop = 0

    # --- token (bara i minnet) ---
    def token(self):
        if self._token and self._klocka() < self._giltig_till - 300:
            return self._token
        cid, sec = os.environ.get(self.id_var), os.environ.get(self.secret_var)
        if not cid or not sec:
            raise ShopifyFel(f'Miljövariablerna {self.id_var} och {self.secret_var} måste finnas.')
        body = urllib.parse.urlencode({'grant_type': 'client_credentials', 'client_id': cid, 'client_secret': sec}).encode()
        status, _, text = self._transport(f'https://{self.butik}/admin/oauth/access_token',
                                          {'Content-Type': 'application/x-www-form-urlencoded'}, body)
        if status != 200:
            raise ShopifyFel(maska(f'Token-anrop misslyckades: HTTP {status}: {text[:300]}'))
        d = json.loads(text)
        if 'access_token' not in d:
            raise ShopifyFel('Token-svaret saknar access_token (fält: %s)' % sorted(d))
        self._token = d['access_token']
        self._giltig_till = self._klocka() + int(d.get('expires_in', 3600))
        return self._token

    # --- GraphQL med återförsök ---
    def graphql(self, query, variabler=None):
        body = json.dumps({'query': query, 'variables': variabler or {}}, ensure_ascii=True).encode()
        for forsok in range(1, self.max_forsok + 1):
            headers = {'Content-Type': 'application/json', 'X-Shopify-Access-Token': self.token()}
            status, h, text = self._transport(f'https://{self.butik}/admin/api/{API_VERSION}/graphql.json', headers, body)
            self.antal_anrop += 1
            paus = min(2 ** forsok, 30)
            if status == 401:  # token ogiltig: hämta ny en gång
                if forsok == 1:
                    self._token = None
                    continue
                raise ShopifyFel(maska(f'HTTP 401 efter ny token: {text[:300]}'))
            if status == 429 or status >= 500:
                paus = max(paus, float({k.lower(): v for k, v in h.items()}.get('retry-after', 0) or 0))
                self._sleep(paus)
                continue
            if status != 200:
                raise ShopifyFel(maska(f'HTTP {status}: {text[:300]}'))
            d = json.loads(text)
            fel = d.get('errors') or []
            if fel:
                if any((e.get('extensions') or {}).get('code') == 'THROTTLED' for e in fel if isinstance(e, dict)):
                    self._sleep(paus)
                    continue
                raise ShopifyFel(maska('GraphQL-fel: ' + json.dumps(fel, ensure_ascii=False)[:500]))
            # proaktiv paus när kostnadsbudgeten tar slut
            ts = ((d.get('extensions') or {}).get('cost') or {}).get('throttleStatus') or {}
            if ts and ts.get('currentlyAvailable', 1000) < 100:
                self._sleep(max(1.0, (100 - ts['currentlyAvailable']) / max(ts.get('restoreRate', 50), 1)))
            return d['data']
        raise ShopifyFel(f'Gav upp efter {self.max_forsok} försök (rate limit eller serverfel).')


def klient_fran_profil(profil, **kw):
    """Skapar en klient för butiken i en butiksprofil (se butiksprofil.py). Läser inga miljövariabler här."""
    return ShopifyKlient(butik=profil['myshopify'], id_var=profil['klient_id_var'],
                         secret_var=profil['klient_hemlighet_var'], **kw)


def gid(i):
    i = str(i)
    return i if i.startswith('gid://') else f'gid://shopify/Product/{i}'


def sifferid(i):
    return re.sub(r'\D', '', str(i))


def hamta_produkter(klient, ids, del_storlek=10):
    """Returnerar en lista i samma ordning som ids; None för id som inte finns."""
    ids = [gid(i) for i in ids]
    ut = []
    q = 'query($ids:[ID!]!){nodes(ids:$ids){... on Product{%s}}}' % PRODUKTFALT
    for s in range(0, len(ids), del_storlek):
        ut.extend(klient.graphql(q, {'ids': ids[s:s + del_storlek]})['nodes'])
    return ut


def kontrollera_fore(produkter, ids):
    """R17: id-antal och inga tomma fält. Returnerar lista med fel (tom om allt stämmer)."""
    fel = []
    if len(produkter) != len(ids):
        fel.append(f'antal {len(produkter)} != {len(ids)}')
    for i, p in zip(ids, produkter):
        if not p:
            fel.append(f'{i}: produkten finns inte'); continue
        if sifferid(p['id']) != sifferid(i):
            fel.append(f'{i}: fel id i svaret')
        if p.get('descriptionHtml') is None or not p.get('title') or not p.get('handle'):
            fel.append(f'{i}: ofullständig post')
    return fel


def spara_fore(produkter, sokvag):
    """Sparar före-filen maskinellt. Skriver aldrig över en befintlig fil."""
    if os.path.exists(sokvag):
        raise ShopifyFel(f'{sokvag} finns redan; före-filer skrivs inte över.')
    os.makedirs(os.path.dirname(sokvag), exist_ok=True)
    with open(sokvag, 'w', encoding='utf-8') as f:
        json.dump(produkter, f, ensure_ascii=False, indent=1)
    return sokvag


def uppdatera_seo(klient, produkt_id, seo_title, seo_description):
    """productUpdate med seo{title description}, alltid båda fälten (lärdom 2026-11-01)."""
    if seo_title is None or seo_description is None:
        raise ShopifyFel('seo skickas alltid med både title och description.')
    q = ('mutation($p:ProductUpdateInput!){productUpdate(product:$p){product{id} userErrors{field message}}}')
    d = klient.graphql(q, {'p': {'id': gid(produkt_id), 'seo': {'title': seo_title, 'description': seo_description}}})
    fel = d['productUpdate']['userErrors']
    if fel:
        raise ShopifyFel('userErrors: ' + json.dumps(fel, ensure_ascii=False))
    return d['productUpdate']['product']['id']


def effektiv_seo_title(p):
    """Shopify lagrar seo.title som null när den är lika med titeln (lärdom 2026-10-31)."""
    return (p.get('seo') or {}).get('title') or p.get('title')


def jamfor_efter(fore, efter, forvantad_meta, forvantad_seo_title=None):
    """Jämför en återläst produkt mot före-läget. Endast seo.description får ha ändrats.
    Returnerar lista med avvikelser (tom om allt stämmer)."""
    fel = []
    if forvantad_seo_title is None:
        forvantad_seo_title = effektiv_seo_title(fore)
    for k in ('title', 'handle', 'status', 'descriptionHtml'):
        if fore.get(k) != efter.get(k):
            fel.append(f'{k} ändrad (före {len(fore.get(k) or "")} tecken, efter {len(efter.get(k) or "")} tecken)')
    if sorted(fore.get('tags') or []) != sorted(efter.get('tags') or []):
        fel.append('tags ändrade')
    if effektiv_seo_title(efter) != forvantad_seo_title:
        fel.append(f'seo.title avviker: {effektiv_seo_title(efter)!r} != {forvantad_seo_title!r}')
    ml = (efter.get('seo') or {}).get('description')
    if ml != forvantad_meta:
        p = next((n for n, (a, b) in enumerate(zip(ml or '', forvantad_meta or '')) if a != b), min(len(ml or ''), len(forvantad_meta or '')))
        fel.append(f'seo.description avviker vid tecken {p}: live {len(ml or "")} tecken, förväntat {len(forvantad_meta or "")} tecken')
    return fel


def verifiera_butik(klient, forvantad=None):
    """Stoppar om API-svaret inte kommer från förväntad butik (körs före varje skrivning).
    Förväntad butik är klientens egen adress (profilens myshopify) om inget annat anges."""
    forvantad = forvantad or klient.butik
    s = klient.graphql('{shop{name myshopifyDomain}}')['shop']
    if s['myshopifyDomain'] != forvantad:
        raise ShopifyFel(f'Fel butik: {s["myshopifyDomain"]} (väntade {forvantad}).')
    return s['name']
