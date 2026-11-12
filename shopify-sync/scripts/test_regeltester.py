#!/usr/bin/env python3
"""Enhetstester utan nätverk för regeltester.py, rattningstyper.py och kopplingen i skrivfil_kontroll.py.
Körning: python3 -I shopify-sync/scripts/test_regeltester.py
"""
import json, os, sys, tempfile, unittest

HAR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HAR)
import regeltester as rg
import rattningstyper as rt
import skrivfil_kontroll as sk

CFG = {
    'standardlage': 'varning', 'lage': {}, 'extra_marken': ['Giant'],
    'butiksord': {'scooter': 'sparkcykel'},
    'engelska_typord': ['power rack', 'half rack', 'foam roller', 'training belts?'],
    'kvalitetsord': ['slitstark', 'robust', 'skyddar', 'BPA-fri', 'UPF'],
}
BLOCK = '<h2>Leverans, retur och garanti</h2>'


def utkast(titel='Sparkcykel Soke City', seo='Sparkcykel Soke City', meta='Sparkcykeln väger 4 kg och har 200 mm hjul av PU, enligt tillverkaren.', html='<p>Soke City har hjul på 200 mm.</p>'):
    return {'nr': 1, 'id': '1', 'titel': titel, 'seo_title': seo, 'meta': meta, 'html': html}


def koder(x, cfg=CFG):
    return sorted({f.kod for _, f in rg.kontrollera_utkast(x, cfg)})


class TestKontroller(unittest.TestCase):
    def test_rent_utkast_ger_inga_fynd(self):
        self.assertEqual(koder(utkast()), [])

    def test_decimalpunkt(self):
        self.assertIn('DECIMALPUNKT', koder(utkast(meta='Cykeln har 27.5 tum hjul och väger 14 kg.')))
        self.assertIn('DECIMALPUNKT', koder(utkast(html='<p>Mått 185x52.5 mm.</p>')))
        # modellnummer och versioner utan enhet ska inte larma
        self.assertNotIn('DECIMALPUNKT', koder(utkast(titel='Cardio Fit 2.0', meta='Modell 2.0 har skärm och väger 10 kg.')))
        self.assertNotIn('DECIMALPUNKT', koder(utkast(meta='Cykeln har 27,5 tum hjul och väger 14 kg.')))

    def test_tum_skarm(self):
        self.assertIn('TUM_SKARM', koder(utkast(meta='Motionscykel med 7 tum LED/LCD-skärm och 26 program.')))
        self.assertIn('TUM_SKARM', koder(utkast(html='<p>Löpband med 10,1 tum TFT-pekskärm.</p>')))
        self.assertNotIn('TUM_SKARM', koder(utkast(meta='Motionscykel med 7-tums LED/LCD-skärm och 26 program.')))
        self.assertNotIn('TUM_SKARM', koder(utkast(html='<ul><li>Skärm: 7 tum</li></ul>')))

    def test_tum_hjul(self):
        self.assertIn('TUM_HJUL', koder(utkast(meta='Cykeln har 26 tums hjul och 21 växlar.')))
        self.assertNotIn('TUM_HJUL', koder(utkast(meta='Cykeln har 26-tumshjul och 21 växlar.')))

    def test_apostrof(self):
        self.assertIn('APOSTROF', koder(utkast(titel="Barncykel S´COOL niXe")))
        self.assertNotIn('APOSTROF', koder(utkast(titel="Barncykel S'cool niXe")))

    def test_enhet_form(self):
        self.assertIn('ENHET_FORM', koder(utkast(meta='Pumpen når 120 PSI och motorn är på 3 HK.')))
        self.assertIn('ENHET_FORM', koder(utkast(meta='Motorn är på 3 hp och väger 20 kg.')))
        self.assertIn('ENHET_FORM', koder(utkast(html='<p>Längd 120 CM.</p>')))
        self.assertNotIn('ENHET_FORM', koder(utkast(meta='Pumpen når 120 psi och motorn är på 3 hk.')))

    def test_butiksord(self):
        self.assertIn('BUTIKSORD', koder(utkast(titel='Scooterhjul Union Dragon')))
        self.assertIn('BUTIKSORD', koder(utkast(html='<p>Dig som söker en hopfällbar scooter.</p>')))
        self.assertNotIn('BUTIKSORD', koder(utkast(titel='Sparkcykelhjul Union Dragon')))
        self.assertEqual(koder(utkast(titel='Scooterhjul Union Dragon'), dict(CFG, butiksord={})), [])

    def test_typord_fel_plats(self):
        self.assertIn('TYPORD_FEL_PLATS', koder(utkast(seo='Giant Cleanspring Dricksflaska')))
        self.assertIn('TYPORD_FEL_PLATS', koder(utkast(titel='Tunturi Cardio Fit D20')))
        self.assertNotIn('TYPORD_FEL_PLATS', koder(utkast(titel='Dricksflaska Giant Cleanspring')))

    def test_engelskt_typord(self):
        self.assertIn('ENGELSKT_TYPORD', koder(utkast(titel='Power Rack Tunturi RC20')))
        self.assertIn('ENGELSKT_TYPORD', koder(utkast(html='<p>Dig som vill ha en foam roller.</p>')))
        self.assertIn('ENGELSKT_TYPORD', koder(utkast(titel='Training Belts Toorx')))
        self.assertNotIn('ENGELSKT_TYPORD', koder(utkast(titel='Träningsställ Tunturi RC20')))

    def test_cirkular_typord(self):
        self.assertIn('CIRKULAR_TYPORD', koder(utkast(meta='Tunturi Hantelstång är en hantelstång på 180 cm i krom.')))
        self.assertIn('CIRKULAR_TYPORD', koder(utkast(html='<p>Gymstick Curlbar är en curlbar av metall.</p>')))
        self.assertNotIn('CIRKULAR_TYPORD', koder(utkast(meta='Tunturi Cardio Fit R25 är en roddmaskin med 8 motståndsnivåer och magnetbroms.')))
        self.assertNotIn('CIRKULAR_TYPORD', koder(utkast(meta='Tunturi Olympic Rubber Plate är en viktskiva i gummi på 10 kg.')))

    def test_kvalitetsord_utan_etv(self):
        self.assertIn('KVALITETSORD_UTAN_ETV', koder(utkast(meta='Flaskan är gjord av slitstark plast och rymmer 600 ml.')))
        self.assertIn('KVALITETSORD_UTAN_ETV', koder(utkast(html='<ul><li>Material: Robust plast</li></ul>')))
        self.assertIn('KVALITETSORD_UTAN_ETV', koder(utkast(html='<p>Handskarna har UPF-solskydd.</p>')))
        self.assertNotIn('KVALITETSORD_UTAN_ETV', koder(utkast(meta='Enligt tillverkaren är plasten slitstark. Flaskan rymmer 600 ml.')))
        self.assertNotIn('KVALITETSORD_UTAN_ETV', koder(utkast(html='<ul><li>Material: Robust plast, enligt tillverkaren</li></ul>')))

    def test_lastgrans_utan_etv(self):
        self.assertIn('LASTGRANS_UTAN_ETV', koder(utkast(html='<ul><li>Maximal användarvikt: 120 kg</li></ul>')))
        self.assertNotIn('LASTGRANS_UTAN_ETV', koder(utkast(html='<ul><li>Maximal användarvikt: 120 kg, enligt tillverkaren</li></ul>')))
        self.assertNotIn('LASTGRANS_UTAN_ETV', koder(utkast(html='<ul><li>Vikt: 12 kg</li></ul>')))

    def test_meta_utan_verb(self):
        self.assertIn('META_UTAN_VERB', koder(utkast(meta='Skivstångspaket med curlstång på 120 cm och viktskivor.')))
        self.assertNotIn('META_UTAN_VERB', koder(utkast(meta='Skivstångspaketet har en curlstång på 120 cm.')))


class TestLage(unittest.TestCase):
    def test_lage_av_hoppar_over(self):
        cfg = dict(CFG, lage={'BUTIKSORD': 'av'})
        self.assertNotIn('BUTIKSORD', koder(utkast(titel='Scooterhjul Union'), cfg))

    def test_lage_fel_markeras(self):
        cfg = dict(CFG, lage={'BUTIKSORD': 'fel'})
        res = rg.kontrollera_utkast(utkast(titel='Scooterhjul Union'), cfg)
        self.assertEqual([l for l, f in res if f.kod == 'BUTIKSORD'], ['fel'])

    def test_standardlage_ar_varning(self):
        res = rg.kontrollera_utkast(utkast(titel='Scooterhjul Union'), CFG)
        self.assertTrue(res and all(l == 'varning' for l, _ in res))

    def test_config_i_repot_har_inga_fel_lagen(self):
        cfg = rg.las_cfg()
        self.assertEqual(cfg['standardlage'], 'varning')
        self.assertNotIn('fel', cfg['lage'].values(), 'inga nya kontroller får stå i läget fel utan Davids beslut')
        for kod in rg.KONTROLLER:
            self.assertIn(rg.lage_for(kod, cfg), ('varning', 'av'))


class TestKoppling(unittest.TestCase):
    """skrivfil_kontroll.py: nya kontroller som varning ändrar inte utgångskoden."""
    def skrivfil(self, titel):
        x = {'nr': 1, 'id': '1', 'titel': titel, 'seo_title': titel, 'meta': 'Sparkcykeln väger 4 kg och har 200 mm hjul av PU, enligt tillverkaren, och är hopfällbar.',
             'html': '<p>Soke City har hjul på 200 mm.</p>' + ''.join(f'<p>{b}</p>' for b in sk.BLOCK_KRAV)}
        f = os.path.join(tempfile.mkdtemp(prefix='rt_'), 'skriv.json')
        with open(f, 'w', encoding='utf-8') as fh:
            json.dump([x], fh, ensure_ascii=False)
        return f

    def test_varning_pavarkar_inte_fel(self):
        f = self.skrivfil('Scooterhjul Soke City')
        n, fel, varn = sk.kontrollera(f, {}, False)
        self.assertEqual(fel, [])
        rfel, rvarn = sk.kontrollera_regeltester(f)
        self.assertEqual(rfel, [])
        self.assertTrue(any('BUTIKSORD' in v for v in rvarn))

    def test_rent_utkast_ger_inga_regeltestfynd(self):
        f = self.skrivfil('Sparkcykel Soke City')
        self.assertEqual(sk.kontrollera_regeltester(f), ([], []))


class TestRattningstyper(unittest.TestCase):
    def typ(self, falt, fore, efter):
        return rt.sortera(falt, fore, efter)

    def test_format(self):
        self.assertEqual(self.typ('titel', 'Träningsbänk TUNTURI CT40', 'Träningsbänk Tunturi CT40')[0], 'F')
        self.assertIn('tum-form', self.typ('meta', 'har 7 tum LED-skärm', 'har 7-tums LED-skärm')[1])
        self.assertIn('enhet', self.typ('meta', 'når 120 PSI', 'når 120 psi')[1])
        self.assertIn('skiljetecken', self.typ('meta', 'mäter 52.5 mm', 'mäter 52,5 mm')[1])

    def test_innehall(self):
        self.assertEqual(self.typ('html', '<li>Handtag: Bekvämt handtag</li>', '')[0], 'I')
        self.assertIn('FAQ', self.typ('html', '<h2>Vanliga frågor</h2><h3>Går det?</h3><p>Ja.</p>', '')[1])
        self.assertIn('enligt tillverkaren', self.typ('meta', 'Strumporna är andningsaktiva.', 'Enligt tillverkaren andas de.')[1])
        self.assertIn('cirkulär', self.typ('html', '<p>Selle Monte Grappa är ett kjolskydd i svart läder</p>', '<p>Kjolskyddet från Selle Monte Grappa är i svart läder</p>')[1])

    def test_ordskillnad(self):
        rem, add, _ = rt.ordskillnad('Scooterhjul Union', 'Sparkcykelhjul Union')
        self.assertEqual((rem, add), ('Scooterhjul', 'Sparkcykelhjul'))

    def test_faltnamn(self):
        self.assertEqual(rt.faltnamn('html 2'), 'html')
        self.assertEqual(rt.faltnamn('seo_title'), 'seo_title')
        self.assertEqual(rt.faltnamn('html_3'), 'html')


if __name__ == '__main__':
    unittest.main(verbosity=1)
