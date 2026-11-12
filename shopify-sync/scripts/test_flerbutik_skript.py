#!/usr/bin/env python3
"""Tester utan nätverk för --profil i shopify_skriv_texter, arkivera_dubbletter, nattkontroll, verifiera_skrivna
och profilstödet i skrivfil_kontroll. Falska klienter ersätter allt som annars pratar med Shopify.
Körning: python3 -I shopify-sync/scripts/test_flerbutik_skript.py   Inga hemligheter läses.
"""
import contextlib, copy, io, json, os, sys, tempfile, unittest
from unittest import mock

HAR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HAR)
import butiksprofil as bp
import shopify_api as api
import shopify_skriv_texter as st
import arkivera_dubbletter as ad
import nattkontroll as nk
import verifiera_skrivna as vs
import skrivfil_kontroll as sk
import regeltester
from test_butiksprofil import ALPHA, skriv_json

ALPHA2 = dict(copy.deepcopy(ALPHA), klartagg='klar-alpha', standardblock_krav=['Alpha-block', 'info@alphazoo.se'], marken=['Zoomark'],
              marken_varning_bara=[])
SIFFRA = 'gid://shopify/Product/'


def produkt(i, titel='T', html='<p>h</p>', tags=(), status='ACTIVE', meta='M', seo='S'):
    return {'id': SIFFRA + str(i), 'title': titel, 'handle': 'h%s' % i, 'status': status, 'tags': list(tags), 'updatedAt': 'x',
            'seo': {'title': seo, 'description': meta}, 'descriptionHtml': html}


class FalskKlient:
    """Ersätter ShopifyKlient: svarar på butiksfrågan och loggar vilken profil den skapades för."""
    skapade = []

    def __init__(self, profil):
        self.butik, self.antal_anrop, self.profil, self.mutationer = profil['myshopify'], 0, profil, []
        FalskKlient.skapade.append(self)

    def graphql(self, q, v=None):
        self.antal_anrop += 1
        if 'myshopifyDomain' in q:
            return {'shop': {'name': self.profil['butiksnamn'], 'myshopifyDomain': self.butik}}
        self.mutationer.append((q, v))
        raise AssertionError('oväntat anrop: ' + q[:60])


def kor(modul, argv, **kw):
    ut = io.StringIO()
    with contextlib.redirect_stdout(ut):
        try:
            kod = modul.main(argv)
        except SystemExit as e:
            kod = e.code
    return kod, ut.getvalue()


class Bas(unittest.TestCase):
    def setUp(self):
        FalskKlient.skapade = []
        self.d = tempfile.TemporaryDirectory(); self.addCleanup(self.d.cleanup)
        r = copy.deepcopy(ALPHA2)
        r['arbetskatalog'] = os.path.join(self.d.name, 'skriv')
        r['sparrlista'] = os.path.relpath(skriv_json(self.d.name, 'sparr.json', {'sparrar': []}), bp.ROT)
        self.profilfil = skriv_json(self.d.name, 'alpha.json', r)
        p = mock.patch.object(api, 'klient_fran_profil', side_effect=lambda profil, **kw: FalskKlient(profil))
        p.start(); self.addCleanup(p.stop)
        p = mock.patch.object(api, 'ShopifyKlient', side_effect=AssertionError('ShopifyKlient() utan profil får inte användas'))
        p.start(); self.addCleanup(p.stop)


class TestProfilfalt(unittest.TestCase):
    def test_pilotlista_bos_och_annan_butik(self):
        self.assertEqual(bp.las_butiksprofil()['pilotlista'], 'rapporter/bestofsports-pilot-20-produkter-2026-10-25.csv')
        self.assertIsNone(bp.tolka_profil(copy.deepcopy(ALPHA))['pilotlista'])  # ärvs inte från BOS
        self.assertEqual(bp.tolka_profil(dict(copy.deepcopy(ALPHA), pilotlista='x.csv'))['pilotlista'], 'x.csv')

    def test_butiksslug(self):
        self.assertEqual(bp.butiksslug({'butiksnamn': 'Alpha Zoo'}), 'alphazoo')
        self.assertEqual(bp.butiksslug({'butiksnamn': 'Bästa Öl'}), 'bastaol')
        with self.assertRaises(bp.ProfilFel):
            bp.butiksslug({'butiksnamn': ' – '})


class TestSkrivTexter(Bas):
    W = {'id': '5', 'nr': 1, 'titel': 'Ny', 'seo_title': 'Ny S', 'meta': 'Ny meta', 'html': '<p>ny</p>'}

    def skrivfil(self):
        return skriv_json(self.d.name, 'a_skriv_1.json', [self.W])

    def test_klartagg_valbar_i_jamforelsen(self):
        l = produkt(5, 'Ny', '<p>ny</p>', tags=['klar-alpha'], meta='Ny meta', seo='Ny S')
        f = produkt(5, 'Ny', '<p>ny</p>', meta='Ny meta', seo='Ny S')
        self.assertEqual(st.jamfor_text(self.W, f, l, tagg_klar=True, klartagg='klar-alpha'), [])
        self.assertIn('taggar avviker från förväntat', st.jamfor_text(self.W, f, l, tagg_klar=True))  # BOS-taggen förväntas utan argument
        self.assertEqual(st.jamfor_text(self.W, f, produkt(5, 'Ny', '<p>ny</p>', ['texter-klara'], meta='Ny meta', seo='Ny S'), tagg_klar=True), [])

    def test_tagga_skickar_profilens_tagg(self):
        k = mock.Mock(); k.graphql.return_value = {'tagsAdd': {'userErrors': []}}
        st.tagga(k, '5', 'klar-alpha'); self.assertEqual(k.graphql.call_args[0][1]['t'], ['klar-alpha'])
        st.tagga(k, '5'); self.assertEqual(k.graphql.call_args[0][1]['t'], ['texter-klara'])

    def test_dry_run_med_profil_anvander_profilens_butik_sparr_och_utkatalog(self):
        ut = os.path.join(self.d.name, 'ut')
        with mock.patch.object(api, 'hamta_produkter', return_value=[produkt(5)]), mock.patch.object(api, 'kontrollera_fore', return_value=[]), \
                mock.patch.object(st, 'las_sparr', return_value={}) as sp:
            kod, text = kor(st, [self.skrivfil(), '--dry-run', '--ut', ut, '--profil', self.profilfil])
        self.assertEqual(kod, 0, text)
        self.assertIn('Butik: Alpha Zoo', text)
        self.assertEqual(FalskKlient.skapade[0].butik, 'alpha-zoo-test.myshopify.com')
        self.assertEqual(sp.call_args[0][0], os.path.join(bp.ROT, json.load(open(self.profilfil))['sparrlista']))
        self.assertNotIn('shopify-sync/config/sparrlista.json', sp.call_args[0][0].replace(self.d.name, ''))
        self.assertTrue(os.path.exists(os.path.join(ut, 'a_skriv_1_fore_dry-run.json')))

    def test_standardutkatalog_far_butiksnamn_for_annan_butik(self):
        with mock.patch.object(api, 'hamta_produkter', return_value=[produkt(5)]), mock.patch.object(api, 'kontrollera_fore', return_value=[]), \
                mock.patch.object(api, 'spara_fore') as sf:
            kor(st, [self.skrivfil(), '--dry-run', '--profil', self.profilfil])
        self.assertTrue(sf.call_args[0][1].split(os.sep)[-2].endswith('-alphazoo'), sf.call_args[0][1])

    def test_utan_profil_ar_bos_och_standardutkatalog_oforandrad(self):
        bos = bp.las_butiksprofil()
        with mock.patch.object(api, 'klient_fran_profil', side_effect=lambda p, **kw: FalskKlient(p)), \
                mock.patch.object(api, 'hamta_produkter', return_value=[produkt(5)]), mock.patch.object(api, 'kontrollera_fore', return_value=[]), \
                mock.patch.object(api, 'spara_fore') as sf:
            kod, text = kor(st, [self.skrivfil(), '--dry-run'])
        self.assertEqual(kod, 0, text)
        self.assertIn('Butik: BEST OF SPORTS', text)
        self.assertEqual(FalskKlient.skapade[0].butik, bos['myshopify'])
        self.assertRegex(os.path.basename(os.path.dirname(sf.call_args[0][1])), r'^shopify-original-\d{4}-\d\d-\d\d$')

    def test_felaktig_profil_stoppar_fore_anrop(self):
        for argv in (['--profil', '/finns/inte.json'], ['--profil']):
            with self.assertRaises(bp.ProfilFel):
                st.main([self.skrivfil(), '--dry-run'] + argv)
        self.assertEqual(FalskKlient.skapade, [])
        halv = skriv_json(self.d.name, 'halv.json', {'butik': 'x.se', 'myshopify': 'x.myshopify.com'})
        with self.assertRaises(bp.ProfilFel):
            st.main([self.skrivfil(), '--dry-run', '--profil', halv])
        self.assertEqual(FalskKlient.skapade, [])


class TestArkivera(Bas):
    def p(self, i, tags, sku, titel='Stor sparkcykel rod xl', bilder=3, lager=0):
        return {'id': SIFFRA + str(i), 'title': titel, 'handle': 'h', 'createdAt': 'x', 'tags': tags, 'status': 'ACTIVE', 'totalInventory': lager,
                'mediaCount': {'count': bilder}, 'variants': {'nodes': [{'sku': sku, 'price': '1'}]}}

    def test_hitta_med_profilens_klartagg(self):
        lista = [self.p(1, ['klar-alpha'], 'S1'), self.p(2, [], 'S1')]
        ark, hoppar = ad.hitta(lista, set(), 'klar-alpha')
        self.assertEqual([api.sifferid(a[0]['id']) for a in ark], ['2'])
        self.assertEqual(ad.hitta(lista, set(), 'texter-klara'), ([], []))  # BOS-taggen finns inte i den här butiken
        self.assertEqual(len(ad.hitta([self.p(1, ['texter-klara'], 'S1'), self.p(2, [], 'S1')], set())[0]), 1)  # standard oförändrad

    def test_dry_run_anvander_profilen_och_ingen_bos_pilotlista(self):
        lista = [self.p(1, ['klar-alpha'], 'S1'), self.p(2, [], 'S1')]
        ut = os.path.join(self.d.name, 'ut')
        with mock.patch.object(ad, 'hamta_alla', return_value=lista), mock.patch('builtins.open', wraps=open) as op:
            kod, text = kor(ad, ['--dry-run', '--ut', ut, '--profil', self.profilfil])
        self.assertEqual(kod, 0, text)
        self.assertIn('Butik: Alpha Zoo', text)
        self.assertIn('1 dubbletter att arkivera', text)
        self.assertFalse(any('bestofsports-pilot' in str(c.args[0]) for c in op.call_args_list), 'BOS pilotlista lästes')
        self.assertEqual(FalskKlient.skapade[0].profil['myshopify'], 'alpha-zoo-test.myshopify.com')

    def test_dry_run_med_pilotlista_i_profil(self):
        lista = [self.p(1, ['klar-alpha'], 'S1'), self.p(2, [], 'S1')]
        csvf = os.path.join(self.d.name, 'pilot.csv'); open(csvf, 'w').write('produkt_id\n2\n')
        r = json.load(open(self.profilfil)); r['pilotlista'] = os.path.relpath(csvf, bp.ROT)
        pf = skriv_json(self.d.name, 'alpha_pilot.json', r)
        with mock.patch.object(ad, 'hamta_alla', return_value=lista):
            kod, text = kor(ad, ['--dry-run', '--ut', os.path.join(self.d.name, 'ut'), '--profil', pf])
        self.assertIn('0 dubbletter att arkivera', text)

    def test_felaktig_profil_stoppar_fore_anrop(self):
        with self.assertRaises(bp.ProfilFel):
            ad.main(['--dry-run', '--profil', '/finns/inte.json'])
        self.assertEqual(FalskKlient.skapade, [])


class TestNattkontrollOchVerifiera(Bas):
    def skriv(self, tagg_live):
        w = {'id': '5', 'nr': 1, 'titel': 'Ny', 'seo_title': 'Ny S', 'meta': 'Ny meta', 'html': '<p>ny</p>'}
        skriv_json(os.path.join(self.d.name, 'skriv'), 'a_skriv_1.json', [w])
        return [produkt(5, 'Ny', '<p>ny</p>', tags=tagg_live, meta='Ny meta', seo='Ny S')]

    def test_nattkontroll_laser_profilens_katalog_tagg_och_egen_baslinje(self):
        live = self.skriv(['texter-klara'])  # BOS-taggen räcker inte för Alpha
        ut = os.path.join(self.d.name, 'nk')
        with mock.patch.object(api, 'hamta_produkter', return_value=live), mock.patch.object(nk, 'UT', ut):
            kod, text = kor(nk, ['--profil', self.profilfil])
            self.assertEqual(kod, 1, text)
            self.assertIn('Kontrollerade produkter: 1', text)
            self.assertIn('Nya avvikelser: 1', text)
            self.assertTrue(os.path.isdir(os.path.join(ut, 'alphazoo')))
            self.assertFalse(os.path.exists(os.path.join(ut, 'baslinje.json')))
            kor(nk, ['--skapa-baslinje', '--profil', self.profilfil])
            self.assertTrue(os.path.exists(os.path.join(ut, 'alphazoo', 'baslinje.json')))
            self.assertFalse(os.path.exists(os.path.join(ut, 'baslinje.json')))  # delar inte baslinje med BOS
        csvrad = open(os.path.join(ut, 'alphazoo', 'nattkontroll-%s.csv' % __import__('time').strftime('%Y-%m-%d')), encoding='utf-8').read()
        self.assertIn('klar-alpha saknas', csvrad)
        live2 = self.skriv(['klar-alpha'])
        with mock.patch.object(api, 'hamta_produkter', return_value=live2), mock.patch.object(nk, 'UT', ut + '2'):
            kod, _ = kor(nk, ['--profil', self.profilfil])
        self.assertEqual(kod, 0)

    def test_nattkontroll_utan_profil_ar_bos_katalog(self):
        self.assertEqual(nk.avsedda.__defaults__[0], nk.SKRIV)
        self.assertTrue(nk.SKRIV.endswith(os.path.join('facit-bos-2026-10-31', 'vag2_skriv')))
        with mock.patch.object(nk, 'avsedda', return_value={}) as av, mock.patch.object(api, 'hamta_produkter', return_value=[]), \
                mock.patch.object(nk, 'UT', os.path.join(self.d.name, 'u')):
            kor(nk, [])
        self.assertEqual(av.call_args[0][0], os.path.join(bp.ROT, 'rapporter/facit-bos-2026-10-31/vag2_skriv'))

    def test_verifiera_skrivna_med_profil(self):
        self.skriv([])
        fil = os.path.join(self.d.name, 'skriv', 'a_skriv_1.json')
        with mock.patch.object(api, 'hamta_produkter', return_value=[produkt(5, 'Ny', '<p>ny</p>', ['klar-alpha'], meta='Ny meta', seo='Ny S')]):
            kod, text = kor(vs, ['--profil', self.profilfil, fil])
        self.assertEqual((kod, '1 produkter lästa, 0 med avvikelse' in text, 'Butik: Alpha Zoo' in text), (0, True, True), text)
        with mock.patch.object(api, 'hamta_produkter', return_value=[produkt(5, 'Ny', '<p>ny</p>', ['texter-klara'], meta='Ny meta', seo='Ny S')]):
            kod, text = kor(vs, ['--profil', self.profilfil, fil])
        self.assertEqual(kod, 1); self.assertIn('taggen klar-alpha saknas', text)

    def test_verifiera_skrivna_felaktig_profil(self):
        with self.assertRaises(bp.ProfilFel):
            vs.main(['--profil', '/finns/inte.json', 'x.json'])
        self.assertEqual(FalskKlient.skapade, [])


class TestSkrivfilKontrollProfil(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.TemporaryDirectory(); self.addCleanup(self.d.cleanup)
        g = (list(sk.MARKEN), list(sk.MARKEN_VARNING), list(sk.BLOCK_KRAV), sk.BUTIKSNAMN, sk.SEO_SUFFIX, sk.REGELTEST_CFG, regeltester.PROFIL_SOKVAG)
        def aterstall():
            sk.MARKEN, sk.MARKEN_VARNING, sk.BLOCK_KRAV, sk.BUTIKSNAMN, sk.SEO_SUFFIX, sk.REGELTEST_CFG, regeltester.PROFIL_SOKVAG = g
        self.addCleanup(aterstall)

    def meta(self, namn):
        return 'Hundbädden är mjuk och tvättbar och ger din hund en plats att vila på, med rejäla kanter. Finns hos %s.' % namn

    def fil(self, namn, krav):
        x = {'nr': 1, 'id': '7', 'titel': 'Hundbädd Soft', 'seo_title': 'Hundbädd Soft', 'meta': self.meta(namn),
             'html': '<p>Hundbädden är mjuk.</p>' + ''.join('<p>%s</p>' % k for k in krav)}
        return skriv_json(self.d.name, 'skriv.json', [x])

    def test_bos_utan_argument_oforandrat(self):
        sk.las_profil(bp.STANDARD_PROFIL, strikt=True)
        self.assertEqual(sk.BUTIKSNAMN, 'BEST OF SPORTS')
        self.assertIn('info@bestofsports.se', sk.BLOCK_KRAV)
        self.assertIn('Maxxus', sk.MARKEN)
        n, fel, varn = sk.kontrollera(self.fil('BEST OF SPORTS', sk.BLOCK_KRAV), {}, False)
        self.assertTrue(any('Finns hos BEST OF SPORTS.' in v for v in varn))
        self.assertEqual(fel, [])

    def test_annan_butik_far_eget_namn_block_och_marken(self):
        pf = skriv_json(self.d.name, 'alpha.json', ALPHA2)
        sk.las_profil(pf, strikt=True)
        self.assertEqual((sk.BUTIKSNAMN, sk.SEO_SUFFIX), ('Alpha Zoo', ' – Alpha Zoo'))
        self.assertEqual(sk.BLOCK_KRAV, ['Alpha-block', 'info@alphazoo.se'])
        self.assertEqual(sk.MARKEN, ['Zoomark'])
        n, fel, varn = sk.kontrollera(self.fil('Alpha Zoo', sk.BLOCK_KRAV), {}, False)
        self.assertEqual(fel, [])
        self.assertTrue(any('Finns hos Alpha Zoo.' in v for v in varn))
        n, fel, varn = sk.kontrollera(self.fil('BEST OF SPORTS', sk.BLOCK_KRAV), {}, False)  # BOS-namnet är ingen utfyllnad här
        self.assertFalse(any('Finns hos' in v for v in varn))
        n, fel, _ = sk.kontrollera(self.fil('Alpha Zoo', ['Leverans, retur och garanti']), {}, False)
        self.assertTrue(any('saknar "Alpha-block"' in f for f in fel))
        self.assertFalse(any('bestofsports' in f for f in fel))

    def test_annan_butik_utan_standardblock_stoppas_och_ingen_marken_ärvs(self):
        r = copy.deepcopy(ALPHA2); del r['standardblock_krav']
        with self.assertRaises(bp.ProfilFel):
            sk.las_profil(skriv_json(self.d.name, 'a.json', r), strikt=True)
        r = copy.deepcopy(ALPHA2); del r['marken']; del r['marken_varning_bara']
        sk.las_profil(skriv_json(self.d.name, 'b.json', r), strikt=True)
        self.assertEqual((sk.MARKEN, sk.MARKEN_VARNING), ([], []))  # tomt, inte BOS-listan

    def test_annan_butik_regeltester_utan_bos_installningar(self):
        sk.las_profil(skriv_json(self.d.name, 'alpha.json', ALPHA2), strikt=True)
        self.assertIsNone(sk.REGELTEST_CFG)
        self.assertEqual(regeltester.las_marken(), ['Zoomark'])
        self.assertEqual(regeltester.las_cfg(sk.REGELTEST_CFG)['extra_marken'], [])  # BOS extra_marken ärvs inte
        sk.las_profil(bp.STANDARD_PROFIL, strikt=True)  # tillbaka till BOS
        self.assertEqual(sk.REGELTEST_CFG, regeltester.CFG_SOKVAG)
        self.assertIn('Maxxus', regeltester.las_marken())

    def test_profilfil_saknas(self):
        with self.assertRaises(bp.ProfilFel):
            sk.las_profil('/finns/inte.json', strikt=True)
        sk.las_profil('/finns/inte.json')  # äldre anrop utan strikt: BOS-värden, som förut

    def test_main_utgangskod_och_felmeddelande(self):
        gammal = sys.argv
        try:
            for arg, fraga in (('/finns/inte.json', 'FEL'),):
                sys.argv = ['x', '--profil', arg, 'a.json']
                with self.assertRaises(SystemExit) as c:
                    sk.main()
                self.assertIn(fraga, str(c.exception.code))
        finally:
            sys.argv = gammal


if __name__ == '__main__':
    unittest.main()
