#!/usr/bin/env python3
"""Tester utan nätverk för skriv_med_skydd.py: prisjobbstagg, prisändring, tagg och normalflöde. Kör: python3 -I test_skriv_med_skydd.py"""
import copy, os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skriv_med_skydd as s  # noqa: E402


def prod(i, tags=(), pris='100.00'):
    return {'id': f'gid://shopify/Product/{i}', 'title': 'Gammal titel', 'handle': f'h{i}', 'status': 'ACTIVE', 'tags': list(tags), 'totalInventory': 3,
            'updatedAt': 'x', 'seo': {'title': None, 'description': None}, 'descriptionHtml': '<p>gammal</p>',
            'variants': {'nodes': [{'id': f'v{i}', 'sku': 'a', 'price': pris, 'compareAtPrice': None, 'inventoryQuantity': 3}]}}


def skrivpost(i):
    return {'id': str(i), 'nr': i, 'titel': 'Ny titel', 'seo_title': 'Ny seo', 'meta': 'M' * 80, 'html': '<p>ny</p>'}


class Fake:
    def __init__(self, prods, andra_pris_efter_skrivning=False, lagg_pcj_efter_skrivning=False):
        self.p = {s.api.sifferid(x['id']): x for x in prods}
        self.pris, self.pcj, self.antal_anrop = andra_pris_efter_skrivning, lagg_pcj_efter_skrivning, 0

    def graphql(self, q, v=None):
        self.antal_anrop += 1
        if 'nodes(ids' in q: return {'nodes': [copy.deepcopy(self.p[s.api.sifferid(i)]) for i in v['ids']]}
        if 'productUpdate' in q:
            x, pp = self.p[s.api.sifferid(v['p']['id'])], v['p']
            x['title'], x['descriptionHtml'], x['seo'] = pp['title'], pp['descriptionHtml'], pp['seo']
            if self.pris: x['variants']['nodes'][0]['price'] = '90.00'
            if self.pcj: x['tags'].append(s.SPARRTAGG)
            return {'productUpdate': {'product': {'id': pp['id']}, 'userErrors': []}}
        if 'tagsAdd' in q:
            self.p[s.api.sifferid(v['id'])]['tags'] += v['t']
            return {'tagsAdd': {'node': {'id': v['id']}, 'userErrors': []}}
        raise AssertionError(q)


class T(unittest.TestCase):
    def kor(self, f, ids):
        fore = {s.api.sifferid(x['id']): x for x in s.las(f, ids)}
        return s.kor_del(f, [skrivpost(i) for i in ids], fore, 'texter-klara'), fore

    def test_normalt(self):
        f = Fake([prod(1, ['Velomarket']), prod(2)])
        (ok, av), _ = self.kor(f, [1, 2])
        self.assertEqual((len(ok), av), (2, []))
        self.assertIn('texter-klara', f.p['1']['tags']); self.assertIn('Velomarket', f.p['1']['tags'])

    def test_prisandring_stoppar_och_taggar_inte(self):
        f = Fake([prod(1)], andra_pris_efter_skrivning=True)
        (ok, av), _ = self.kor(f, [1])
        self.assertEqual(ok, []); self.assertTrue(any('PRIS' in x for x in av[0][1]))
        self.assertNotIn('texter-klara', f.p['1']['tags'])

    def test_prisjobbstagg_efter_skrivning_stoppar(self):
        f = Fake([prod(1)], lagg_pcj_efter_skrivning=True)
        (ok, av), _ = self.kor(f, [1])
        self.assertEqual(ok, []); self.assertTrue(any('tillkommit' in x for x in av[0][1]))

    def test_prisjobbstagg_skippas_i_klassning(self):
        live = [prod(1, [s.SPARRTAGG]), prod(2)]
        skriv, klar, avv = s.klassa_skydd([skrivpost(1), skrivpost(2)], live, {})
        self.assertEqual([w['id'] for w in skriv], ['2']); self.assertEqual(len(avv), 1)

    def test_prisandring_fore_skrivning_stoppar(self):
        f = Fake([prod(1)])
        fore = {s.api.sifferid(x['id']): x for x in s.las(f, [1])}
        f.p['1']['variants']['nodes'][0]['compareAtPrice'] = '120.00'
        with self.assertRaises(s.Stopp): s.kor_del(f, [skrivpost(1)], fore, 'texter-klara')
        self.assertEqual(f.p['1']['title'], 'Gammal titel')


if __name__ == '__main__':
    unittest.main()
