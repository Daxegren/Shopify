import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
import pris_forslag as p


class T(unittest.TestCase):
    def test_upp9(self):
        self.assertEqual(p.upp9(102.1), 109)
        self.assertEqual(p.upp9(109), 109)
        self.assertEqual(p.upp9(674.6), 679)
        self.assertEqual(p.upp9(89.01), 89 + 10)
        self.assertEqual(p.upp9(83.7), 89)

    def test_formelpris_axa(self):
        self.assertEqual(p.formelpris(323.8), 679)
        self.assertEqual(p.formelpris(49.0), 109)

    def test_marginal(self):
        self.assertAlmostEqual(p.marginal_efter_moms(679, 323.8), 0.404, places=2)

    def test_bedom_axa_stort_fel_halls(self):
        b = p.bedom(4805.10, 5339.0, 323.8, ["price-change-job-active"], 1)
        self.assertTrue(b["rea"])
        self.assertEqual(b["ordinarie"], 5339.0)
        self.assertEqual(b["nytt"], 679)
        self.assertTrue(b["hallen"])
        self.assertTrue(b["prisjobb"])
        self.assertIn("PRISJOBBSTAGG_SKRIVS_EJ", b["flaggor"])
        self.assertIn("ANDRING_OVER_25", b["flaggor"])

    def test_bedom_under_inkop_hojs(self):
        b = p.bedom(39.0, 39.0, 49.0, [], 226)
        self.assertEqual(b["nytt"], 109)
        self.assertEqual(b["riktning"], "upp")
        self.assertTrue(b["hallen"])  # +179 %

    def test_ingen_andring_vid_formelpris(self):
        b = p.bedom(679.0, 0, 323.8, [], 5)
        self.assertEqual(b["riktning"], "lika")
        self.assertEqual(b["flaggor"], [])

    def test_saknat_inkop(self):
        self.assertIsNone(p.bedom(100, 0, None, [], 1))
        self.assertIsNone(p.bedom(100, 0, 0, [], 1))

    def test_rea_flagga(self):
        b = p.bedom(899.1, 999.0, 400.0, [], 3)
        self.assertTrue(b["rea"])
        self.assertIn("REA_PAGAR_RAKNA_OM_EFTER_ATERSTALLNING", b["flaggor"])

    def test_forpackning_flagga(self):
        b = p.bedom(1659.0, 0, 138.2, [], 1)   # marginal över 80 % och nytt pris sjunker kraftigt
        self.assertIn("KONTROLLERA_INKOP_ELLER_FORPACKNING", b["flaggor"])

    def test_sma_varor_undantas_taket(self):
        b = p.bedom(9.0, 0, 0.33, [], 1)
        self.assertNotIn("MARGINAL_UTANFOR_30_50", b["flaggor"])

    def test_wb_malmarginal_60(self):
        # inköp 100: formelpris 60 % = ceil9(100/0.4*1.25=312.5) = 319
        self.assertEqual(p.formelpris(100, marginal=0.60), 319)
        b = p.bedom(499.0, 0, 100.0, [], 5, marginal=0.60, golv=0.55, tak=0.65)
        self.assertEqual(b["nytt"], 319)
        self.assertEqual(b["riktning"], "ner")
        self.assertTrue(b["hallen"])  # -36 % hålls kvar

    def test_tolerans_ror_inte_nara_malet(self):
        # pris 319 / inköp 100: marginal 60,2 %
        self.assertIsNone(p.bedom(319.0, 0, 100.0, [], 5, marginal=0.60, tolerans=0.03))
        self.assertIsNotNone(p.bedom(319.0, 0, 100.0, [], 5, marginal=0.60, tolerans=0.0))

    def test_rader_med_falsk_klient(self):
        class K:
            def graphql(self, q, v=None):
                return {"products": {"pageInfo": {"hasNextPage": False, "endCursor": None}, "nodes": [
                    {"legacyResourceId": "1", "title": "Lås", "tags": ["price-change-job-active"], "variants": {"nodes": [
                        {"legacyResourceId": "11", "sku": "S1", "price": "4805.10", "compareAtPrice": "5339.00",
                         "inventoryQuantity": 1, "inventoryItem": {"unitCost": {"amount": "323.80"}}}]}},
                    {"legacyResourceId": "2", "title": "Ok", "tags": [], "variants": {"nodes": [
                        {"legacyResourceId": "22", "sku": "S2", "price": "679.00", "compareAtPrice": None,
                         "inventoryQuantity": 5, "inventoryItem": {"unitCost": {"amount": "323.80"}}}]}}]}}
        rs = list(p.rader(K(), paus=0, logg=None))
        self.assertEqual(len(rs), 1)
        self.assertEqual(rs[0]["nytt_pris"], "679.00")
        self.assertEqual(rs[0]["prisjobb"], 1)
        self.assertEqual(rs[0]["hallen"], 1)


if __name__ == "__main__":
    unittest.main()
