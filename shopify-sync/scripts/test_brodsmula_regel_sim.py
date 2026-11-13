#!/usr/bin/env python3
"""Tester för brodsmula_regel_sim.py. Körning: python3 -I shopify-sync/scripts/test_brodsmula_regel_sim.py"""
import importlib.util, os, sys, unittest
HAR = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location("sim", os.path.join(HAR, "brodsmula_regel_sim.py"))
sim = importlib.util.module_from_spec(sp); sys.modules["sim"] = sim; sp.loader.exec_module(sim)

TREE = {"cyklar": {"elcyklar": {}, "cykeltillbehor": {"cykelbelysning": {}}},
        "gymutrustning": {"hemmagym": {"traningsbank": {}}, "fria-vikter": {"skivstang": {}}},
        "konditionsutrustning": {"motionscykel": {}},
        "kosttillskott": {"protein": {"proteinbars": {}}},
        "varumarke": {"giant": {}, "kona-1": {}}}


class V1(unittest.TestCase):
    def test_hittar_underkollektion_under_forsta_toppnivan(self):
        self.assertEqual(sim.rule_v1(TREE, {"cyklar", "elcyklar"}), ("cyklar", "elcyklar"))

    def test_djupaste_barnbarn(self):
        self.assertEqual(sim.rule_v1(TREE, {"gymutrustning", "hemmagym", "traningsbank"}), ("gymutrustning", "traningsbank"))

    def test_missar_om_toppnivan_saknas(self):      # träningsbänk men inte Gymutrustning: koden hamnar under Kondition
        self.assertIsNone(sim.rule_v1(TREE, {"konditionsutrustning", "traningsbank", "hemmagym"}))

    def test_missar_om_mellannivan_saknas(self):     # proteinbars men inte Protein
        self.assertIsNone(sim.rule_v1(TREE, {"kosttillskott", "proteinbars"}))

    def test_varumarke_ger_bara_varumarke_under_varumarke(self):
        self.assertEqual(sim.rule_v1(TREE, {"varumarke", "giant"}), ("varumarke", "giant"))


class V2(unittest.TestCase):
    def test_hittar_traningsbank_utan_gymutrustning(self):
        self.assertEqual(sim.rule_v2(TREE, {"konditionsutrustning", "traningsbank", "hemmagym"}), ("gymutrustning", "traningsbank"))

    def test_hittar_proteinbars_utan_protein(self):
        self.assertEqual(sim.rule_v2(TREE, {"kosttillskott", "proteinbars"}), ("kosttillskott", "proteinbars"))

    def test_amne_gar_fore_varumarke(self):
        self.assertEqual(sim.rule_v2(TREE, {"cyklar", "elcyklar", "giant", "varumarke"}), ("cyklar", "elcyklar"))

    def test_varumarke_ersatter_inte_amneshubb(self):   # cykel i Cyklar + Giant: ingen varumärkeslänk, som förut
        self.assertIsNone(sim.rule_v2(TREE, {"cyklar", "giant", "varumarke"}))

    def test_varumarke_visas_nar_forsta_huvudgrenen_ar_varumarke(self):
        self.assertEqual(sim.rule_v2(TREE, {"varumarke", "giant"}), ("varumarke", "giant"))

    def test_ingen_om_inget_matchar(self):
        self.assertIsNone(sim.rule_v2(TREE, {"cyklar", "alla-produkter"}))

    def test_behaller_v1_nar_den_redan_ger_amneslank(self):
        m = {"cyklar", "elcyklar", "konditionsutrustning", "motionscykel"}
        self.assertEqual(sim.rule_v2(TREE, m), sim.rule_v1(TREE, m))

    def test_menypost_som_pekar_pa_huvudgren_ignoreras(self):
        tree = {"gymutrustning": {"tillbehor": {"ovrig-utrustning": {}}}, "ovrig-utrustning": {"sportutrustning": {}}}
        self.assertEqual(sim.rule_v2(tree, {"ovrig-utrustning", "sportutrustning"}), ("ovrig-utrustning", "sportutrustning"))

    def test_djupast_forst_sedan_menyordning(self):
        self.assertEqual(sim.rule_v2(TREE, {"cykeltillbehor", "cykelbelysning", "elcyklar"}), ("cyklar", "cykelbelysning"))

    def test_v2_andrar_aldrig_en_befintlig_amneslank(self):
        for m in ({"cyklar", "elcyklar"}, {"gymutrustning", "hemmagym", "traningsbank"}, {"konditionsutrustning", "motionscykel", "traningsbank"}):
            r1 = sim.rule_v1(TREE, m)
            if r1 and r1[0] != "varumarke":
                self.assertEqual(sim.rule_v2(TREE, m), r1)

    def test_v2_hittar_minst_det_v1_hittar(self):
        for m in ({"cyklar", "elcyklar"}, {"gymutrustning", "hemmagym", "traningsbank"}, {"varumarke", "giant"}, {"konditionsutrustning", "motionscykel"}):
            if sim.rule_v1(TREE, m):
                self.assertIsNotNone(sim.rule_v2(TREE, m))
                self.assertEqual(sim.rule_v1(TREE, m)[1], sim.rule_v2(TREE, m)[1])


class Forslag(unittest.TestCase):
    def test_forslag_pa_ordstam(self):
        self.assertIn("skivstang", sim.suggest("Skivstång Hammer Maximum PRO", {"gymutrustning": {"fria-vikter": {"skivstang": {}}}}, ""))


if __name__ == "__main__":
    unittest.main(verbosity=1)
