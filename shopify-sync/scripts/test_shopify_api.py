#!/usr/bin/env python3
"""Enhetstester utan nätverk för shopify_api.py och shopify_meta_rensning.py.
Körning: python3 -m unittest shopify-sync/scripts/test_shopify_api.py   (eller python3 shopify-sync/scripts/test_shopify_api.py)
"""
import json, os, sys, tempfile, unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shopify_api as api
import shopify_meta_rensning as rens

HEMLIGT_ID, HEMLIGT_SEC = 'testid_abcdef123456', 'testsecret_abcdef123456'


class FalskTransport:
    """Spelar upp förprogrammerade svar (status, text, huvuden) och loggar anropen."""
    def __init__(self, svar):
        self.svar, self.anrop = list(svar), []

    def __call__(self, url, headers, body, timeout=60):
        self.anrop.append((url, headers, body))
        s = self.svar.pop(0)
        return s[0], (s[2] if len(s) > 2 else {}), s[1]


TOKEN_OK = (200, json.dumps({'access_token': 'shpat_TESTTOKEN123456', 'expires_in': 86399, 'scope': 'write_products'}))


def gql(data=None, errors=None):
    return 200, json.dumps({'data': data, **({'errors': errors} if errors else {})})


def prod(i, meta, seo_title=None, **kw):
    p = {'id': f'gid://shopify/Product/{i}', 'title': 'Löpband X', 'handle': 'lopband-x', 'status': 'ACTIVE',
         'tags': ['a', 'b'], 'seo': {'title': seo_title, 'description': meta}, 'descriptionHtml': '<p>Text</p>'}
    p.update(kw)
    return p


class Bas(unittest.TestCase):
    def setUp(self):
        os.environ['SHOPIFY_CLIENT_ID_BOS'], os.environ['SHOPIFY_CLIENT_SECRET_BOS'] = HEMLIGT_ID, HEMLIGT_SEC
        self.pauser = []

    def klient(self, svar):
        t = FalskTransport(svar)
        return api.ShopifyKlient(transport=t, sleep=self.pauser.append, max_forsok=4), t


class TestKlient(Bas):
    def test_token_hamtas_en_gang_och_cachas_i_minnet(self):
        k, t = self.klient([TOKEN_OK, gql({'a': 1}), gql({'a': 2})])
        k.graphql('{a}'); k.graphql('{a}')
        self.assertEqual(sum('oauth/access_token' in u for u, _, _ in t.anrop), 1)
        self.assertEqual(t.anrop[1][1]['X-Shopify-Access-Token'], 'shpat_TESTTOKEN123456')

    def test_ny_token_nar_den_gar_ut(self):
        klocka = [1000.0]
        t = FalskTransport([TOKEN_OK, gql({}), TOKEN_OK, gql({})])
        k = api.ShopifyKlient(transport=t, sleep=lambda s: None, klocka=lambda: klocka[0])
        k.graphql('{a}'); klocka[0] += 86400; k.graphql('{a}')
        self.assertEqual(sum('oauth/access_token' in u for u, _, _ in t.anrop), 2)

    def test_hemligheter_skickas_bara_i_token_anropet(self):
        k, t = self.klient([TOKEN_OK, gql({})])
        k.graphql('{a}')
        self.assertIn(HEMLIGT_SEC.encode(), t.anrop[0][2])
        self.assertNotIn(HEMLIGT_SEC.encode(), t.anrop[1][2])

    def test_token_ingen_fil_pa_disk(self):
        with tempfile.TemporaryDirectory() as d:
            cwd = os.getcwd(); os.chdir(d)
            try:
                k, _ = self.klient([TOKEN_OK, gql({})]); k.graphql('{a}')
                self.assertEqual(os.listdir(d), [])
            finally:
                os.chdir(cwd)

    def test_fel_maskeras(self):
        k, _ = self.klient([(401, f'bad {HEMLIGT_SEC} shpat_ABCDEFGH12345678')])
        with self.assertRaises(api.ShopifyFel) as c:
            k.token()
        self.assertNotIn(HEMLIGT_SEC, str(c.exception)); self.assertNotIn('shpat_ABCDEFGH', str(c.exception))

    def test_saknade_miljovariabler(self):
        del os.environ['SHOPIFY_CLIENT_SECRET_BOS']
        k, _ = self.klient([])
        with self.assertRaises(api.ShopifyFel):
            k.token()

    def test_ateforsok_vid_throttled(self):
        thr = gql(None, [{'message': 'Throttled', 'extensions': {'code': 'THROTTLED'}}])
        k, t = self.klient([TOKEN_OK, thr, thr, gql({'ok': True})])
        self.assertEqual(k.graphql('{a}'), {'ok': True})
        self.assertEqual(len(self.pauser), 2)

    def test_ateforsok_vid_429_och_5xx_med_retry_after(self):
        k, _ = self.klient([TOKEN_OK, (429, 'x', {'Retry-After': '7'}), (503, 'x'), gql({'ok': 1})])
        self.assertEqual(k.graphql('{a}'), {'ok': 1})
        self.assertGreaterEqual(self.pauser[0], 7)

    def test_ger_upp_efter_max_forsok(self):
        k, _ = self.klient([TOKEN_OK] + [(503, 'x')] * 4)
        with self.assertRaises(api.ShopifyFel):
            k.graphql('{a}')

    def test_graphql_fel_kastas_utan_ateforsok(self):
        k, t = self.klient([TOKEN_OK, gql(None, [{'message': 'Field x does not exist'}])])
        with self.assertRaises(api.ShopifyFel):
            k.graphql('{x}')
        self.assertEqual(len(t.anrop), 2)

    def test_401_ger_ny_token_en_gang(self):
        k, t = self.klient([TOKEN_OK, (401, 'expired'), TOKEN_OK, gql({'a': 1})])
        self.assertEqual(k.graphql('{a}'), {'a': 1})


class TestProdukter(Bas):
    def test_hamta_i_delar_och_i_ordning(self):
        ids = [str(1000 + i) for i in range(25)]
        k, t = self.klient([TOKEN_OK, gql({'nodes': [prod(i, 'm') for i in ids[:10]]}), gql({'nodes': [prod(i, 'm') for i in ids[10:20]]}),
                            gql({'nodes': [prod(i, 'm') for i in ids[20:]]})])
        r = api.hamta_produkter(k, ids)
        self.assertEqual([api.sifferid(p['id']) for p in r], ids)

    def test_kontrollera_fore(self):
        self.assertEqual(api.kontrollera_fore([prod('1', 'm')], ['1']), [])
        self.assertTrue(api.kontrollera_fore([prod('1', 'm', descriptionHtml=None)], ['1']))
        self.assertTrue(api.kontrollera_fore([prod('1', 'm')], ['1', '2']))

    def test_spara_fore_skriver_inte_over(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'u', 'fore.json')
            api.spara_fore([prod('1', 'å ö ä')], p)
            self.assertEqual(json.load(open(p, encoding='utf-8'))[0]['seo']['description'], 'å ö ä')
            with self.assertRaises(api.ShopifyFel):
                api.spara_fore([], p)

    def test_uppdatera_seo_skickar_alltid_bada_falten(self):
        k, t = self.klient([TOKEN_OK, gql({'productUpdate': {'product': {'id': 'gid://shopify/Product/1'}, 'userErrors': []}})])
        api.uppdatera_seo(k, '1', 'Titel', 'Meta')
        v = json.loads(t.anrop[1][2])['variables']['p']
        self.assertEqual(v, {'id': 'gid://shopify/Product/1', 'seo': {'title': 'Titel', 'description': 'Meta'}})
        with self.assertRaises(api.ShopifyFel):
            api.uppdatera_seo(k, '1', None, 'Meta')

    def test_uppdatera_seo_userErrors(self):
        k, _ = self.klient([TOKEN_OK, gql({'productUpdate': {'product': None, 'userErrors': [{'field': ['seo'], 'message': 'fel'}]}})])
        with self.assertRaises(api.ShopifyFel):
            api.uppdatera_seo(k, '1', 'T', 'M')


class TestJamfor(unittest.TestCase):
    def test_lika_ger_inga_avvikelser(self):
        self.assertEqual(api.jamfor_efter(prod('1', 'gammal'), prod('1', 'ny'), 'ny', 'Löpband X'), [])

    def test_seo_title_null_raknas_som_titeln(self):
        self.assertEqual(api.jamfor_efter(prod('1', 'g', None), prod('1', 'n', 'Löpband X'), 'n', 'Löpband X'), [])

    def test_ett_tecken_fel_i_meta_hittas(self):
        f = api.jamfor_efter(prod('1', 'g'), prod('1', 'nx'), 'ny', 'Löpband X')
        self.assertIn('vid tecken 1', f[0])

    def test_osynligt_tecken_hittas(self):
        self.assertTrue(api.jamfor_efter(prod('1', 'g'), prod('1', 'n­y'), 'ny', 'Löpband X'))

    def test_andrad_beskrivning_status_tagg_handle_titel(self):
        for k, v in (('descriptionHtml', '<p>annan</p>'), ('status', 'DRAFT'), ('tags', ['a']), ('handle', 'x'), ('title', 'Y')):
            self.assertTrue(api.jamfor_efter(prod('1', 'g'), prod('1', 'n', **{k: v}), 'n', 'Löpband X'), k)

    def test_taggordning_spelar_ingen_roll(self):
        self.assertEqual(api.jamfor_efter(prod('1', 'g'), prod('1', 'n', tags=['b', 'a']), 'n', 'Löpband X'), [])


class TestKlassa(unittest.TestCase):
    def w(self, i='1', gammal='A Finns hos BEST OF SPORTS.', ny='A', seo_title='Löpband X'):
        return {'id': i, 'nr': 1, 'seo_title': seo_title, 'meta_gammal': gammal, 'meta_ny': ny}

    def test_klassning(self):
        poster = [self.w('1'), self.w('2'), self.w('3'), self.w('4'), self.w('5'), self.w('6', seo_title='Annan')]
        live = [prod('1', 'A Finns hos BEST OF SPORTS.'), prod('2', 'A'), prod('3', 'Helt annan text'), None,
                prod('5', 'A Finns hos BEST OF SPORTS.'), prod('6', 'A Finns hos BEST OF SPORTS.')]
        skriv, klar, avviker = rens.klassa(poster, live, {'5': ('pilot-20', set())})
        self.assertEqual([w['id'] for w in skriv], ['1'])
        self.assertEqual([w['id'] for w in klar], ['2'])
        self.assertEqual(sorted(w['id'] for w, _ in avviker), ['3', '4', '5', '6'])


class TestSkrivTexter(unittest.TestCase):
    import shopify_skriv_texter as st
    W = {'id': '1', 'nr': 1, 'titel': 'Elcykel X', 'seo_title': 'Elcykel X', 'meta': 'Meta text som är tillräckligt lång.', 'html': '<p>Ny</p>'}

    def live(self, **kw):
        p = prod('1', 'Meta text som är tillräckligt lång.', title='Elcykel X', descriptionHtml='<p>Ny</p>', tags=['a'])
        p.update(kw); return p

    def test_lika_ger_inga_avvikelser(self):
        self.assertEqual(self.st.jamfor_text(self.W, self.live(), self.live()), [])

    def test_html_avvikelse_hittas(self):
        self.assertTrue(self.st.jamfor_text(self.W, self.live(), self.live(descriptionHtml='<p>Nx</p>')))

    def test_tagg_forvantas_bara_nar_tagg_klar(self):
        f = self.live(); e = self.live(tags=['a', 'texter-klara'])
        self.assertTrue(self.st.jamfor_text(self.W, f, e))
        self.assertEqual(self.st.jamfor_text(self.W, f, e, tagg_klar=True), [])

    def test_handle_och_status_far_inte_andras(self):
        f = self.live()
        self.assertEqual(len(self.st.jamfor_text(self.W, f, self.live(handle='x', status='DRAFT'))), 2)

    def test_klassning(self):
        poster = [dict(self.W, id=str(i)) for i in range(1, 6)]
        live = [self.live(descriptionHtml='<p>Gammal</p>'), self.live(), self.live(status='DRAFT', descriptionHtml='g'), None,
                self.live(descriptionHtml='g')]
        skriv, klar, avv = self.st.klassa(poster, live, {'5': ('pilot-20', set())})
        self.assertEqual([w['id'] for w in skriv], ['1']); self.assertEqual([w['id'] for w in klar], ['2'])
        self.assertEqual(sorted(w['id'] for w, _ in avv), ['3', '4', '5'])


if __name__ == '__main__':
    unittest.main(verbosity=1)
