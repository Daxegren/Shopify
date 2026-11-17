#!/usr/bin/env python3
"""Gemensam inläsning av butiksprofil för textutrullningens skript (butiksoberoende).

Skripten tar argumentet `--profil <sökväg>`. Utan argument används BEST OF SPORTS-profilen
(`shopify-sync/config/butiksprofil-bestofsports.json`), så att allt fungerar som förut.

Fält som profilen kan sätta (se `shopify-sync/config/butiksprofil-mall.json`):
  myshopify               butikens *.myshopify.com-adress (redan i BOS-profilen)
  butiksnamn              visningsnamn i rubriker och SEO-suffix, t.ex. "BEST OF SPORTS"
  api.klient_id_var       NAMNET på miljövariabeln för klient-id (värdet läses aldrig här)
  api.klient_hemlighet_var  NAMNET på miljövariabeln för klienthemligheten
  gransvarden.seo_suffix  SEO-suffix (redan i BOS-profilen)
  klartagg                taggen som sätts när texten är verifierad (redan i BOS-profilen)
  sparrlista              sökväg till spärrlistan (redan i BOS-profilen)
  regelbok, beslutslogg   sökvägar (redan i BOS-profilen)
  arbetskatalog           katalog med in-/utkast-/skrivfiler per batch
  granskningskatalog      katalog med skrivrapporter
  filprefix               lista med batchprefix i ordning, t.ex. ["f", "g", "h"]
  ersatta_batcher         batcher som inte ska räknas, t.ex. ["f_16", "f_17"]
  delade_skrivfiler       batcher vars skrivfil är delad i <batch>ok.json och <batch>rest.json
  statusfil               sökväg till den genererade statusfilen
  oppna_fragor            sökväg till öppna frågor (JSON), eller utelämnad
  statusgrupp             ordet i statusfilens sammanfattning ("Fitnessgruppen")
  pilotlista              CSV med pilotprodukter som arkivera_dubbletter.py aldrig arkiverar (kolumnen produkt_id);
                          utelämnad för en annan butik = ingen pilotlista

Fallback: saknas ett fält i BEST OF SPORTS-profilen gäller de värden som skripten hade före
flerbutiksändringen (`BOS_STANDARD`). En ANNAN butiks profil får aldrig falla tillbaka på BOS-värden
för butik, miljövariabler, filer eller status: där ger ett saknat obligatoriskt fält ett fel,
så att en ofullständig profil inte kan skriva till eller läsa fel butik.
"""
import json, os, re, sys

HAR = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.abspath(os.path.join(HAR, '..', '..'))
STANDARD_PROFIL = os.path.join(ROT, 'shopify-sync/config/butiksprofil-bestofsports.json')
BOS_MYSHOPIFY = '6f2e53-67.myshopify.com'

# Värdena som skripten hade hårdkodade för BEST OF SPORTS före 2026-11-06.
BOS_STANDARD = {
    'myshopify': BOS_MYSHOPIFY,
    'butiksnamn': 'BEST OF SPORTS',
    'klient_id_var': 'SHOPIFY_CLIENT_ID_BOS',
    'klient_hemlighet_var': 'SHOPIFY_CLIENT_SECRET_BOS',
    'seo_suffix': ' – BEST OF SPORTS',
    'klartagg': 'texter-klara',
    'sparrlista': 'shopify-sync/config/sparrlista.json',
    'regelbok': 'shopify-sync/regler/regler-v1.md',
    'beslutslogg': 'shopify-sync/docs/BESLUTSLOGG.md',
    'arbetskatalog': 'rapporter/facit-bos-2026-10-31/vag2_skriv',
    'granskningskatalog': 'rapporter/facit-bos-2026-10-31/granskning',
    'filprefix': ['f', 'g', 'h'],
    'ersatta_batcher': ['f_%d' % i for i in range(16, 26)],
    'delade_skrivfiler': ['f_14', 'f_15'],
    'statusfil': 'shopify-sync/status/bestofsports-textutrullning.md',
    'oppna_fragor': 'shopify-sync/status/oppna_fragor.json',
    'statusgrupp': 'Fitnessgruppen',
    'pilotlista': 'rapporter/bestofsports-pilot-20-produkter-2026-10-25.csv',
}

# Obligatoriska fält för en annan butik än BOS (inget får ärvas från BOS).
OBLIGATORISKA = ('myshopify', 'butiksnamn', 'klient_id_var', 'klient_hemlighet_var', 'seo_suffix', 'klartagg',
                 'sparrlista', 'arbetskatalog', 'granskningskatalog', 'filprefix', 'statusfil')
# Fält som får utelämnas för en annan butik (neutralt värde i stället för BOS-värde).
VALFRITT_NEUTRALT = {
    'regelbok': BOS_STANDARD['regelbok'],  # regelboken är gemensam för alla butiker
    'beslutslogg': BOS_STANDARD['beslutslogg'],
    'ersatta_batcher': [],
    'delade_skrivfiler': [],
    'oppna_fragor': None,
    'statusgrupp': 'Batcherna',
    'pilotlista': None,
}


class ProfilFel(Exception):
    pass


def _plocka(rå):
    """Plattar ut profilen till de nycklar som skripten använder (BOS_STANDARD:s nycklar)."""
    api = rå.get('api') or {}
    g = rå.get('gransvarden') or {}
    ut = {
        'myshopify': rå.get('myshopify'),
        'butiksnamn': rå.get('butiksnamn'),
        'klient_id_var': api.get('klient_id_var'),
        'klient_hemlighet_var': api.get('klient_hemlighet_var'),
        'seo_suffix': g.get('seo_suffix'),
        'klartagg': rå.get('klartagg'),
        'sparrlista': rå.get('sparrlista'),
        'regelbok': rå.get('regelbok'),
        'beslutslogg': rå.get('beslutslogg'),
        'arbetskatalog': rå.get('arbetskatalog'),
        'granskningskatalog': rå.get('granskningskatalog'),
        'filprefix': rå.get('filprefix'),
        'ersatta_batcher': rå.get('ersatta_batcher'),
        'delade_skrivfiler': rå.get('delade_skrivfiler'),
        'statusfil': rå.get('statusfil'),
        'oppna_fragor': rå.get('oppna_fragor'),
        'statusgrupp': rå.get('statusgrupp'),
        'pilotlista': rå.get('pilotlista'),
    }
    return ut


def _ar_platshallare(v):
    return isinstance(v, str) and (v.strip() == '' or '<' in v and '>' in v)


def tolka_profil(rå, sokvag=None):
    """Ren funktion (testbar utan filer). Returnerar en dict med alla nycklar i BOS_STANDARD plus 'sokvag'."""
    v = _plocka(rå)
    butik = rå.get('butik')
    if v['myshopify'] == BOS_MYSHOPIFY and butik not in (None, 'bestofsports.se'):
        raise ProfilFel('Profilen (%s) pekar på BEST OF SPORTS-butikens myshopify-adress men butiken är %r; rätta myshopify.'
                        % (sokvag or '(minnet)', butik))
    # BOS-profilen: egen myshopify, eller (äldre/ofullständig profil) ingen myshopify och butik bestofsports.se.
    ar_bos = v['myshopify'] == BOS_MYSHOPIFY or (v['myshopify'] is None and butik in (None, 'bestofsports.se'))
    ut = {}
    if ar_bos:
        for k, standard in BOS_STANDARD.items():
            ut[k] = v[k] if v[k] is not None else standard
    else:
        saknas = [k for k in OBLIGATORISKA if v[k] is None or v[k] == [] or _ar_platshallare(v[k])]
        if saknas:
            raise ProfilFel('Profilen %s saknar obligatoriska fält (får inte ärvas från BEST OF SPORTS): %s'
                            % (sokvag or '(minnet)', ', '.join(saknas)))
        for k in BOS_STANDARD:
            ut[k] = v[k] if v[k] is not None else VALFRITT_NEUTRALT.get(k)
        if ut['klient_id_var'] == BOS_STANDARD['klient_id_var'] or ut['klient_hemlighet_var'] == BOS_STANDARD['klient_hemlighet_var']:
            raise ProfilFel('Profilen använder BEST OF SPORTS miljövariabler; ge butiken egna variabelnamn.')
        if not str(ut['myshopify']).endswith('.myshopify.com'):
            raise ProfilFel('myshopify måste sluta på .myshopify.com (fick %r).' % ut['myshopify'])
        if not (isinstance(ut['filprefix'], list) and all(re.fullmatch(r'[A-Za-z0-9]+', str(p)) for p in ut['filprefix'])):
            raise ProfilFel('filprefix måste vara en lista med bokstäver/siffror.')
    ut['sokvag'] = sokvag
    ut['ar_standardprofil'] = ar_bos
    return ut


def las_butiksprofil(sokvag=None):
    """Läser en profilfil (standard: BEST OF SPORTS). Läser inga miljövariabler."""
    sokvag = os.path.abspath(sokvag or STANDARD_PROFIL)
    try:
        with open(sokvag, encoding='utf-8') as f:
            rå = json.load(f)
    except FileNotFoundError:
        raise ProfilFel('Profilfilen finns inte: %s' % sokvag)
    except ValueError as e:
        raise ProfilFel('Profilfilen är inte giltig JSON (%s): %s' % (sokvag, e))
    return tolka_profil(rå, sokvag)


def plocka_profilargument(argv):
    """Tar ut `--profil <sökväg>` ur en argumentlista. Returnerar (sökväg eller None, övriga argument)."""
    a = list(argv)
    if '--profil' not in a:
        return None, a
    k = a.index('--profil')
    if k + 1 >= len(a) or a[k + 1].startswith('--'):
        raise ProfilFel('--profil kräver en sökväg.')
    sokvag = a[k + 1]
    del a[k:k + 2]
    return sokvag, a


def profil_fran_argv(argv):
    """Returnerar (profil, övriga argument)."""
    sokvag, rest = plocka_profilargument(argv)
    return las_butiksprofil(sokvag), rest


def i_rot(profil, nyckel):
    """Absolut sökväg (under repots rot) för ett sökvägsfält i profilen, eller None."""
    v = profil.get(nyckel)
    return os.path.join(ROT, v) if v else None


def relativ_sokvag(profil):
    """Profilens sökväg relativt repots rot (för text i genererade filer)."""
    s = profil.get('sokvag')
    return os.path.relpath(s, ROT) if s else ''


def butiksslug(profil):
    """Kort ASCII-namn för butiken (för kataloger som inte får delas med andra butiker), t.ex. 'alphazoo'."""
    slug = re.sub(r'[^a-z0-9]+', '', str(profil.get('butiksnamn') or '').lower().replace('å', 'a').replace('ä', 'a').replace('ö', 'o'))
    if not slug:
        raise ProfilFel('Profilen har inget butiksnamn som kan bli ett katalognamn.')
    return slug


def las_ra_profil(profil):
    """Hela profilfilen som den står (för fält som inte plattas ut, t.ex. märken och standardblock). Läser bara filen."""
    with open(profil['sokvag'], encoding='utf-8') as f:
        return json.load(f)
