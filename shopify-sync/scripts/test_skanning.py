import os, tempfile, unittest
import skanning_paket as P
import skanning_shopify as S


def skriv(d, namn, rader):
    with open(os.path.join(d, namn), "w", encoding="utf-8") as f:
        f.write("\n".join(";".join(map(str, r)) for r in rader) + "\n")


class T(unittest.TestCase):
    def test_shopify_fynd_och_rapport(self):
        d = tempfile.mkdtemp()
        skriv(d, "produkter.csv", [["id", "handle", "titel", "status", "marke", "produkttyp", "kategori", "taggar", "seo_titel", "seo_beskrivning", "kon_varde", "beskrivning_tecken", "antal_bilder", "bilder_utan_alt"],
                                   [1, "a", "Tee", "ACTIVE", "V", "T", "Okategoriserat", "", "", "", "", 50, 4, 4],
                                   [2, "b", "Tee", "ACTIVE", "V", "T", "Kläder", "", "T" * 70, "", "[1]", 500, 2, 0],
                                   [3, "c", "Hoodie", "DRAFT", "V", "T", "Kläder", "", "", "", "", 500, 2, 2]])
        skriv(d, "kollektioner.csv", [["id", "handle", "titel", "seo_titel", "seo_beskrivning", "antal_produkter", "beskrivning_tecken"],
                                      [1, "tom", "Tom", "", "", 0, 10], [2, "full", "Full", "T", "B", 5, 500]])
        skriv(d, "oversattning_sammanfattning.csv", [["sprak", "typ", "nyckel", "finns_i_kalla", "oversatt", "foraldrad"],
                                                    ["en", "PRODUCT", "title", 3, 3, 1], ["is", "PRODUCT", "title", 3, 1, 0]])
        fl, kallor, anm = S.analysera(d)
        di = {f["id"]: f for f in fl}
        self.assertEqual((di["alt_text"]["antal"], di["alt_text"]["av"]), (4, 6))   # bara aktiva produkter
        self.assertEqual(di["utan_kategori"]["antal"], 1)
        self.assertEqual(di["tomma_kollektioner"]["antal"], 1)
        self.assertEqual(di["utan_kon"]["antal"], 1)
        self.assertEqual(di["dubblettitlar"]["antal"], 2)
        self.assertEqual(di["seo_titel_lang"]["antal"], 1)
        md = P.rapport_md("Test", "2026-11-19", kallor, fl, anm)
        self.assertIn("P1. Katalogstädning", md); self.assertIn("P2.", md)
        self.assertIn("alt_text", P.till_csv(fl))

    def test_sortering_brist_foerst(self):
        a = P.fynd("a", "x", "A", 1, 10, "VARNING", "P4", "x", "x"); b = P.fynd("b", "x", "B", 1, 10, "BRIST", "P3", "x", "x")
        self.assertEqual([f["id"] for f in P.sortera([a, b])], ["b", "a"])


if __name__ == "__main__":
    unittest.main()
