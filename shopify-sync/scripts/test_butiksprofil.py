#!/usr/bin/env python3
"""Tester utan nätverk för butiksval via butiksprofil (butiksprofil.py och skripten som använder den).
Körning: python3 -I shopify-sync/scripts/test_butiksprofil.py
Inga hemligheter läses; miljövariabler som sätts här har påhittade värden och städas efter varje test.
"""
import contextlib, copy, io, json, os, sys, tempfile, unittest

HAR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HAR)
import butiksprofil as bp
import shopify_api as api
import shopify_meta_rensning as rens
import status_uppdatera as status
import mutation_fran_skrivfil as mutskriv
import mat_utbyte

ALPHA = {
    'butik': 'alphazoo.se',
    'myshopify': 'alpha-zoo-test.myshopify.com',
    'butiksnamn': 'Alpha Zoo',
    'api': {'klient_id_var': 'ALPHA_ID_TEST', 'klient_hemlighet_var': 'ALPHA_SECRET_TEST'},
    'gransvarden': {'seo_suffix': ' – Alpha Zoo'},
    'klartagg': 'texter-klara',
    'sparrlista': 'shopify-sync/config/sparrlista-alphazoo.json',
    'arbetskatalog': 'rapporter/alphazoo/skriv',
    'granskningskatalog': 'rapporter/alphazoo/granskning',
    'filprefix': ['a', 'b'],
    'statusfil': 'shopify-sync/status/alphazoo-textutrullning.md',
}


def skriv_json(katalog, namn, data):
    p = os.path.join(katalog, namn)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    return p


class TestFallbackBos(unittest.TestCase):
    def test_standardprofil_ger_bos_varden(self):
        p = bp.las_butiksprofil()
        self.assertTrue(p['ar_standardprofil'])
        self.assertEqual(p['myshopify'], '6f2e53-67.myshopify.com')
        self.assertEqual((p['klient_id_var'], p['klient_hemlighet_var']), ('SHOPIFY_CLIENT_ID_BOS', 'SHOPIFY_CLIENT_SECRET_BOS'))
        self.assertEqual(p['seo_suffix'], ' – BEST OF SPORTS')
        self.assertEqual(p['filprefix'], ['f', 'g', 'h'])
        self.assertEqual(p['statusfil'], 'shopify-sync/status/bestofsports-textutrullning.md')
        self.assertEqual(p['arbetskatalog'], 'rapporter/facit-bos-2026-10-31/vag2_skriv')
        self.assertEqual(p['klartagg'], 'texter-klara')
        self.assertEqual(p['ersatta_batcher'], ['f_%d' % i for i in range(16, 26)])
        self.assertEqual(p['delade_skrivfiler'], ['f_14', 'f_15'])

    def test_bos_profilen_har_inte_fatt_nya_falt(self):
        """BOS-profilen ska fungera utan de nya fälten (Davids krav: den ändras inte)."""
        with open(bp.STANDARD_PROFIL, encoding='utf-8') as f:
            raa = json.load(f)
        for nytt in ('api', 'butiksnamn', 'arbetskatalog', 'granskningskatalog', 'filprefix', 'statusfil', 'ersatta_batcher'):
            self.assertNotIn(nytt, raa)

    def test_minimal_bos_profil_faller_tillbaka(self):
        for raa in ({'myshopify': bp.BOS_MYSHOPIFY}, {'butik': 'bestofsports.se'}, {}):
            p = bp.tolka_profil(raa)
            self.assertTrue(p['ar_standardprofil'])
            for k, v in bp.BOS_STANDARD.items():
                self.assertEqual(p[k], v, k)

    def test_delvis_overstyrning_i_bos_profil(self):
        p = bp.tolka_profil({'myshopify': bp.BOS_MYSHOPIFY, 'klartagg': 'klar', 'filprefix': ['k']})
        self.assertEqual(p['klartagg'], 'klar')
        self.assertEqual(p['filprefix'], ['k'])
        self.assertEqual(p['klient_id_var'], 'SHOPIFY_CLIENT_ID_BOS')


class TestAnnanButik(unittest.TestCase):
    def test_komplett_profil_laser_in(self):
        p = bp.tolka_profil(copy.deepcopy(ALPHA))
        self.assertFalse(p['ar_standardprofil'])
        self.assertEqual(p['myshopify'], 'alpha-zoo-test.myshopify.com')
        self.assertEqual(p['klient_id_var'], 'ALPHA_ID_TEST')
        self.assertEqual(p['seo_suffix'], ' – Alpha Zoo')
        self.assertEqual(p['filprefix'], ['a', 'b'])
        # valfria fält får neutrala värden, aldrig BOS-värden
        self.assertEqual(p['ersatta_batcher'], [])
        self.assertEqual(p['delade_skrivfiler'], [])
        self.assertIsNone(p['oppna_fragor'])
        self.assertEqual(p['statusgrupp'], 'Batcherna')

    def test_varje_obligatoriskt_falt_kravs(self):
        def utan(raa, nyckel):
            r = copy.deepcopy(raa)
            if nyckel in ('klient_id_var', 'klient_hemlighet_var'):
                del r['api'][nyckel]
            elif nyckel == 'seo_suffix':
                del r['gransvarden']['seo_suffix']
            else:
                del r[nyckel]
            return r
        for k in bp.OBLIGATORISKA:
            with self.assertRaises(bp.ProfilFel, msg=k) as c:
                bp.tolka_profil(utan(ALPHA, k))
            self.assertIn(k, str(c.exception))

    def test_platshallare_fran_mallen_avvisas(self):
        with open(os.path.join(bp.ROT, 'shopify-sync/config/butiksprofil-mall.json'), encoding='utf-8') as f:
            mall = json.load(f)
        with self.assertRaises(bp.ProfilFel):
            bp.tolka_profil(mall)
        r = copy.deepcopy(ALPHA); r['myshopify'] = '<butik>.myshopify.com'
        with self.assertRaises(bp.ProfilFel):
            bp.tolka_profil(r)

    def test_far_inte_anvanda_bos_miljovariabler(self):
        r = copy.deepcopy(ALPHA); r['api']['klient_id_var'] = 'SHOPIFY_CLIENT_ID_BOS'
        with self.assertRaises(bp.ProfilFel):
            bp.tolka_profil(r)
        r = copy.deepcopy(ALPHA); r['api']['klient_hemlighet_var'] = 'SHOPIFY_CLIENT_SECRET_BOS'
        with self.assertRaises(bp.ProfilFel):
            bp.tolka_profil(r)

    def test_bos_adress_pa_annan_butik_avvisas(self):
        r = copy.deepcopy(ALPHA); r['myshopify'] = bp.BOS_MYSHOPIFY
        with self.assertRaises(bp.ProfilFel):
            bp.tolka_profil(r)

    def test_annan_butik_utan_myshopify_faller_inte_tillbaka_pa_bos(self):
        r = copy.deepcopy(ALPHA); del r['myshopify']
        with self.assertRaises(bp.ProfilFel):
            bp.tolka_profil(r)

    def test_myshopify_maste_sluta_pa_myshopify_com(self):
        r = copy.deepcopy(ALPHA); r['myshopify'] = 'alphazoo.se'
        with self.assertRaises(bp.ProfilFel):
            bp.tolka_profil(r)

    def test_ogiltigt_filprefix(self):
        for fel in ([], 'a', ['a/b'], ['']):
            r = copy.deepcopy(ALPHA); r['filprefix'] = fel
            with self.assertRaises(bp.ProfilFel, msg=repr(fel)):
                bp.tolka_profil(r)


class TestArgumentOchFil(unittest.TestCase):
    def test_plocka_profilargument(self):
        self.assertEqual(bp.plocka_profilargument(['x.json', '--dry-run']), (None, ['x.json', '--dry-run']))
        self.assertEqual(bp.plocka_profilargument(['x.json', '--profil', 'p.json', '--rest']), ('p.json', ['x.json', '--rest']))
        for fel in (['--profil'], ['--profil', '--rest']):
            with self.assertRaises(bp.ProfilFel):
                bp.plocka_profilargument(fel)

    def test_utan_argument_ar_bos(self):
        p, rest = bp.profil_fran_argv(['a', 'b'])
        self.assertTrue(p['ar_standardprofil'])
        self.assertEqual(rest, ['a', 'b'])

    def test_fil_saknas_och_trasig_json(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(bp.ProfilFel):
                bp.las_butiksprofil(os.path.join(d, 'finns_inte.json'))
            trasig = os.path.join(d, 'trasig.json')
            with open(trasig, 'w') as f:
                f.write('{inte json')
            with self.assertRaises(bp.ProfilFel):
                bp.las_butiksprofil(trasig)

    def test_profil_fran_fil_och_relativ_sokvag(self):
        with tempfile.TemporaryDirectory() as d:
            p = bp.las_butiksprofil(skriv_json(d, 'alpha.json', ALPHA))
            self.assertEqual(p['sokvag'], os.path.join(os.path.realpath(d), 'alpha.json') if p['sokvag'].startswith(os.path.realpath(d)) else os.path.join(d, 'alpha.json'))
            self.assertEqual(p['butiksnamn'], 'Alpha Zoo')

    def test_i_rot(self):
        p = bp.tolka_profil(copy.deepcopy(ALPHA))
        self.assertEqual(bp.i_rot(p, 'statusfil'), os.path.join(bp.ROT, 'shopify-sync/status/alphazoo-textutrullning.md'))
        self.assertIsNone(bp.i_rot(p, 'oppna_fragor'))


class FalskTransport:
    def __init__(self, svar):
        self.svar, self.anrop = list(svar), []

    def __call__(self, url, headers, body, timeout=60):
        self.anrop.append((url, headers, body))
        s = self.svar.pop(0)
        return s[0], {}, s[1]


class TestKlientFranProfil(unittest.TestCase):
    def setUp(self):
        os.environ['ALPHA_ID_TEST'], os.environ['ALPHA_SECRET_TEST'] = 'alphaid_abcdef123456', 'alphasecret_abcdef123456'
        for k in ('SHOPIFY_CLIENT_ID_BOS', 'SHOPIFY_CLIENT_SECRET_BOS'):
            os.environ.pop(k, None)
        self.addCleanup(lambda: [os.environ.pop(k, None) for k in ('ALPHA_ID_TEST', 'ALPHA_SECRET_TEST')])

    def test_klienten_anvander_profilens_adress_och_variabler(self):
        t = FalskTransport([(200, json.dumps({'access_token': 'shpat_ALPHATOKEN123456', 'expires_in': 86399})),
                            (200, json.dumps({'data': {'shop': {'name': 'Alpha Zoo', 'myshopifyDomain': 'alpha-zoo-test.myshopify.com'}}}))])
        k = api.klient_fran_profil(bp.tolka_profil(copy.deepcopy(ALPHA)), transport=t, sleep=lambda s: None)
        self.assertEqual(api.verifiera_butik(k), 'Alpha Zoo')  # förväntad butik = profilens adress
        self.assertTrue(all('alpha-zoo-test.myshopify.com' in u for u, _, _ in t.anrop))
        self.assertFalse(any('6f2e53-67' in u for u, _, _ in t.anrop))
        self.assertIn(b'alphasecret_abcdef123456', t.anrop[0][2])  # hemligheten skickas bara i token-anropet
        self.assertNotIn(b'alphasecret_abcdef123456', t.anrop[1][2])

    def test_fel_butik_stoppar(self):
        t = FalskTransport([(200, json.dumps({'access_token': 'shpat_X123456789', 'expires_in': 86399})),
                            (200, json.dumps({'data': {'shop': {'name': 'BEST OF SPORTS', 'myshopifyDomain': bp.BOS_MYSHOPIFY}}}))])
        k = api.klient_fran_profil(bp.tolka_profil(copy.deepcopy(ALPHA)), transport=t, sleep=lambda s: None)
        with self.assertRaises(api.ShopifyFel):
            api.verifiera_butik(k)

    def test_bos_miljovariabler_anvands_inte_for_annan_butik(self):
        os.environ['SHOPIFY_CLIENT_ID_BOS'], os.environ['SHOPIFY_CLIENT_SECRET_BOS'] = 'bosid_abcdef123456', 'bossecret_abcdef123456'
        self.addCleanup(lambda: [os.environ.pop(k, None) for k in ('SHOPIFY_CLIENT_ID_BOS', 'SHOPIFY_CLIENT_SECRET_BOS')])
        t = FalskTransport([(200, json.dumps({'access_token': 'shpat_ALPHATOKEN123456', 'expires_in': 86399}))])
        k = api.klient_fran_profil(bp.tolka_profil(copy.deepcopy(ALPHA)), transport=t)
        k.token()
        self.assertNotIn(b'bossecret_abcdef123456', t.anrop[0][2])
        self.assertIn(b'alphasecret_abcdef123456', t.anrop[0][2])

    def test_saknad_variabel_for_profilens_namn(self):
        del os.environ['ALPHA_SECRET_TEST']
        k = api.klient_fran_profil(bp.tolka_profil(copy.deepcopy(ALPHA)), transport=FalskTransport([]))
        with self.assertRaises(api.ShopifyFel) as c:
            k.token()
        self.assertIn('ALPHA_SECRET_TEST', str(c.exception))

    def test_profilens_hemligheter_maskas(self):
        api.klient_fran_profil(bp.tolka_profil(copy.deepcopy(ALPHA)), transport=FalskTransport([]))
        ut = api.maska('fel alphasecret_abcdef123456 och alphaid_abcdef123456')
        self.assertNotIn('alphasecret_abcdef123456', ut)
        self.assertNotIn('alphaid_abcdef123456', ut)

    def test_standardklient_ar_oforandrad(self):
        k = api.ShopifyKlient(transport=FalskTransport([]))
        self.assertEqual((k.butik, k.id_var, k.secret_var), (api.BUTIK, 'SHOPIFY_CLIENT_ID_BOS', 'SHOPIFY_CLIENT_SECRET_BOS'))
        self.assertEqual(api.BUTIK, bp.BOS_MYSHOPIFY)


class TestMetaRensningProfil(unittest.TestCase):
    def test_ogiltig_profil_stoppar_innan_nagot_nat(self):
        with tempfile.TemporaryDirectory() as d:
            ofullstandig = copy.deepcopy(ALPHA); del ofullstandig['myshopify']
            pfil = skriv_json(d, 'p.json', ofullstandig)
            infil = skriv_json(d, 'in.json', [])
            with self.assertRaises(bp.ProfilFel):
                rens.main([infil, '--dry-run', '--profil', pfil])


class TestStatus(unittest.TestCase):
    def profil(self, d, **extra):
        raa = copy.deepcopy(ALPHA)
        raa.update(arbetskatalog=os.path.join(d, 'skriv'), granskningskatalog=os.path.join(d, 'gransk'),
                   statusfil=os.path.join(d, 'status.md'))
        raa.update(extra)
        return bp.tolka_profil(raa)

    def fyll(self, d):
        s = os.path.join(d, 'skriv')
        for namn, data in {
            'a_1_in.json': [{}, {}, {}], 'a_1_utkast.json': [{}, {}], 'a_1_avvisade.json': [{}],
            'a_utlatande_1.json': [{'dom': 'GODKÄND'}, {'dom': 'RÄTTAS'}], 'a_skriv_1.json': [{}, {}],
            'b_1_in.json': [{}], 'b_skriv_1.json': [{}],
            'b_2_in.json': [{}, {}], 'b_skriv_2ok.json': [{}], 'b_skriv_2rest.json': [{}],
            'a_9_in.json': [{}], 'a_x1_in.json': [{}],
        }.items():
            skriv_json(s, namn, data)
        os.makedirs(os.path.join(d, 'gransk'), exist_ok=True)
        with open(os.path.join(d, 'gransk', 'a_1_skrivrapport.md'), 'w') as f:
            f.write('x')

    def test_g_h_liknande_batcher_flera_prefix_och_ordning(self):
        with tempfile.TemporaryDirectory() as d:
            self.fyll(d)
            text, ut = status.bygg_status(self.profil(d), idag='2026-01-01')
            self.assertEqual(ut, os.path.join(d, 'status.md'))
            rader = [r.split('|')[1].strip() for r in text.splitlines() if r.startswith('| ') and r.split('|')[1].strip()[:2] in ('a_', 'b_')]
            self.assertEqual(rader, ['a_1', 'a_9', 'a_x1', 'b_1', 'b_2'])  # prefixordning, sedan nummer, x sist
            self.assertIn('# Textutrullning Alpha Zoo – status', text)
            self.assertIn('| a_1 | 3 | 2 | 1 | 1/1/0 | 2 | skriven |', text)
            self.assertIn('| b_1 | 1 |  | 0 |  | 1 | skrivfil |', text)
            self.assertIn('**Batcherna:** 2 produkter skrivna', text)
            self.assertIn('(2026-01-01)', text)

    def test_ersatta_och_delade(self):
        with tempfile.TemporaryDirectory() as d:
            self.fyll(d)
            text, _ = status.bygg_status(self.profil(d, ersatta_batcher=['a_9'], delade_skrivfiler=['b_2']), idag='x')
            self.assertNotIn('| a_9 |', text)
            self.assertIn('| b_2 | 2 |  | 0 |  | 2 | skrivfil |', text)  # ok + rest = 2

    def test_andra_prefix_ignoreras_och_bos_filer_rors_inte(self):
        with tempfile.TemporaryDirectory() as d:
            self.fyll(d)
            skriv_json(os.path.join(d, 'skriv'), 'f_1_in.json', [{}])
            text, _ = status.bygg_status(self.profil(d), idag='x')
            self.assertNotIn('| f_1 |', text)

    def test_oppna_fragor_per_butik(self):
        with tempfile.TemporaryDirectory() as d:
            self.fyll(d)
            fr = skriv_json(d, 'fr.json', [{'id': 'F1', 'datum': '2026-01-01', 'fraga': 'Vilket suffix?', 'status': 'oppen'},
                                          {'id': 'F2', 'datum': '2026-01-01', 'fraga': 'Klar', 'status': 'avklarad'}])
            text, _ = status.bygg_status(self.profil(d, oppna_fragor=fr), idag='x')
            self.assertIn('- F1 (2026-01-01): Vilket suffix?', text)
            self.assertNotIn('F2', text)
            text2, _ = status.bygg_status(self.profil(d), idag='x')  # ingen fil: inga BOS-frågor
            self.assertIn('- (inga)', text2)

    def test_bos_profilen_anvander_sina_ursprungliga_installningar(self):
        p = bp.las_butiksprofil()
        self.assertEqual(status.skrivfiler('/D', 'f', '14', set(p['delade_skrivfiler'])), ['/D/f_skriv_14ok.json', '/D/f_skriv_14rest.json'])
        self.assertEqual(status.skrivfiler('/D', 'g', '3', set(p['delade_skrivfiler'])), ['/D/g_skriv_3.json'])
        self.assertEqual(status.skrivfiler('/D', 'f', 'x1', set(p['delade_skrivfiler'])), ['/D/f_skriv_x1.json'])

    def test_main_med_fel_profil(self):
        ut = io.StringIO()
        with contextlib.redirect_stdout(ut):
            self.assertEqual(status.main(['--profil', '/finns/inte.json']), 1)
        self.assertIn('FEL:', ut.getvalue())


class TestMutationOchMatning(unittest.TestCase):
    def kor(self, modul, argv):
        gammal, ut = sys.argv, io.StringIO()
        sys.argv = ['x'] + argv
        try:
            with contextlib.redirect_stdout(ut):
                modul.main()
        finally:
            sys.argv = gammal
        return ut.getvalue()

    def test_klartagg_fran_profil_och_standard(self):
        with tempfile.TemporaryDirectory() as d:
            sk = skriv_json(d, 'skriv.json', [{'id': 7, 'titel': 'T', 'seo_title': 'S', 'meta': 'M', 'html': '<p>x</p>'}])
            self.assertIn('tags:["texter-klara"]', self.kor(mutskriv, [sk, '0', '1', '--tagga']))
            r = copy.deepcopy(ALPHA); r['klartagg'] = 'klar-alpha'
            pf = skriv_json(d, 'alpha.json', r)
            self.assertIn('tags:["klar-alpha"]', self.kor(mutskriv, [sk, '0', '1', '--tagga', '--profil', pf]))
            self.assertNotIn('--profil', self.kor(mutskriv, [sk, '0', '1', '--profil', pf]))

    def test_mat_utbyte_anvander_profilens_arbetskatalog(self):
        with tempfile.TemporaryDirectory() as d:
            skriv_json(os.path.join(d, 'skriv'), 'a_utlatande_1.json', [{'dom': 'GODKÄND'}, {'dom': 'UNDERKÄND'}])
            r = copy.deepcopy(ALPHA); r['arbetskatalog'] = os.path.join(d, 'skriv')
            pf = skriv_json(d, 'alpha.json', r)
            ut = self.kor(mat_utbyte, ['--profil', pf])
            self.assertIn('Totalt 2 utkast: 1 godkända', ut)
            # uttrycklig katalog går före profilen
            tom = os.path.join(d, 'tom'); os.makedirs(tom)
            self.assertIn('Totalt 0 utkast', self.kor(mat_utbyte, [tom, '--profil', pf]))


if __name__ == '__main__':
    unittest.main()
