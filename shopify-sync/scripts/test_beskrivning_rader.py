#!/usr/bin/env python3
"""Nätverksfria tester för shopify_beskrivning_rader.py. Körning: python3 -I shopify-sync/scripts/test_beskrivning_rader.py"""
import os, sys, unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shopify_beskrivning_rader as b

RADER = [{'gammal': 'Maxvikt: 120 kg', 'ny': 'Maxvikt: 120 kg (enligt tillverkaren)'}]
FORE = '<ul><li>Maxvikt: 120 kg</li><li>Färg: Gul</li></ul>'
NY = '<ul><li>Maxvikt: 120 kg (enligt tillverkaren)</li><li>Färg: Gul</li></ul>'


def post(**kw):
    p = {'id': '111', 'nr': 1, 'rader': RADER, 'html_ny': NY}
    p.update(kw)
    return p


def live(html=FORE, tags=('a',), i='111'):
    return {'id': f'gid://shopify/Product/{i}', 'tags': list(tags), 'descriptionHtml': html, 'title': 'T', 'handle': 'h',
            'status': 'ACTIVE', 'seo': {'title': None, 'description': 'm'}}


class Klassa(unittest.TestCase):
    def test_skriv(self):
        s, k, a = b.klassa([post()], [live()], {})
        self.assertEqual((len(s), len(k), len(a)), (1, 0, 0))

    def test_redan_klar(self):
        s, k, a = b.klassa([post()], [live(NY)], {})
        self.assertEqual((len(s), len(k), len(a)), (0, 1, 0))

    def test_avviker_andrad_text(self):
        s, k, a = b.klassa([post()], [live(FORE.replace('Gul', 'Röd'))], {})
        self.assertEqual((len(s), len(k), len(a)), (0, 0, 1))

    def test_avviker_rad_saknas_eller_dubblett(self):
        self.assertEqual(len(b.klassa([post()], [live('<p>annat</p>')], {})[2]), 1)
        self.assertEqual(len(b.klassa([post()], [live(FORE + FORE)], {})[2]), 1)

    def test_skyddstagg_hoppas_over(self):
        s, k, a = b.klassa([post()], [live(tags=('price-change-job-active',))], {})
        self.assertEqual((len(s), len(a)), (0, 1))
        self.assertIn('price-change-job-active', a[0][1])

    def test_sparrad_och_saknad(self):
        self.assertEqual(len(b.klassa([post()], [live()], {'111': ('pilot',)})[2]), 1)
        self.assertEqual(len(b.klassa([post()], [None], {})[2]), 1)

    def test_ingen_andring(self):
        self.assertEqual(len(b.klassa([post(rader=[{'gammal': 'x', 'ny': 'x'}])], [live()], {})[2]), 1)


class Jamfor(unittest.TestCase):
    P = [('v1', '10.00', None)]

    def test_ok(self):
        self.assertEqual(b.jamfor_beskrivning(live(), live(NY), NY, self.P, self.P), [])

    def test_pris_andrad(self):
        self.assertIn('PRISER ÄNDRADE', b.jamfor_beskrivning(live(), live(NY), NY, self.P, [('v1', '9.00', None)]))

    def test_tagg_seo_html(self):
        e = live(NY, tags=('a', 'b'))
        self.assertIn('tags ändrade', b.jamfor_beskrivning(live(), e, NY, self.P, self.P))
        e = live(NY); e['seo'] = {'title': 'x', 'description': 'm'}
        self.assertIn('seo ändrad', b.jamfor_beskrivning(live(), e, NY, self.P, self.P))
        self.assertTrue(any('descriptionHtml avviker' in f for f in b.jamfor_beskrivning(live(), live(FORE), NY, self.P, self.P)))


class Mutation(unittest.TestCase):
    def test_skickar_bara_descriptionhtml(self):
        sparat = {}

        class K:
            def graphql(self, q, v):
                sparat.update(v)
                return {'productUpdate': {'product': {'id': 'x'}, 'userErrors': []}}
        b.uppdatera_beskrivning(K(), '111', NY)
        self.assertEqual(sorted(sparat['p']), ['descriptionHtml', 'id'])


class Indata(unittest.TestCase):
    def test_riktig_indata_ger_exakt_html_ny_vid_ersattning(self):
        import json
        fil = os.path.join(b.ROT, 'rapporter', 'shopify-original-2026-11-12', 'f2_indata_forslag_indata_skriv.json')
        fore = {api['id']: api for api in json.load(open(os.path.join(os.path.dirname(fil), 'f2_indata_forslag_live_fore.json'), encoding='utf-8'))}
        for w in json.load(open(fil, encoding='utf-8')):
            html = next(v for k, v in fore.items() if k.endswith(w['id']))['descriptionHtml']
            self.assertEqual(b.ersatt(html, w['rader']), w['html_ny'], w['nr'])


if __name__ == '__main__':
    unittest.main()
