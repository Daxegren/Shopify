import csv, json, os, tempfile, unittest
import kollektion_seo_skriv as K
from kon_fyll_target_gender import Stopp


class Fake:
    def __init__(self, samlingar, skadlig=False):
        self.s = samlingar; self.skadlig = skadlig; self.skrivna = []

    def graphql(self, q, v=None):
        if "collectionUpdate" in q:
            c = v["c"]; self.skrivna.append(c)
            kol = self.s[c["id"]]
            kol["seo"] = {"title": c["seo"]["title"], "description": None if self.skadlig else c["seo"]["description"]}
            return {"collectionUpdate": {"userErrors": []}}
        return {"collection": self.s.get(v["id"])}


def kol(h, st="", sd="", html="<p>text</p>"):
    return {"id": f"gid://shopify/Collection/{h}", "handle": f"h{h}", "title": f"T{h}", "descriptionHtml": html, "seo": {"title": st, "description": sd}}


def fil(rader):
    f = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8", newline="")
    w = csv.DictWriter(f, fieldnames=["handle", "kollektion_id", "seo_title_nu", "seo_title_forslag", "seo_description_nu", "seo_description_forslag", "godkand"], delimiter=";")
    w.writeheader(); w.writerows(rader); f.close(); return f.name


def rad(i, godkand="ja", nu_d="(saknas)"):
    return {"handle": f"h{i}", "kollektion_id": str(i), "seo_title_nu": "(saknas)", "seo_title_forslag": f"Titel {i}", "seo_description_nu": nu_d, "seo_description_forslag": f"Beskrivning {i}", "godkand": godkand}


class T(unittest.TestCase):
    def test_torrkorning_skriver_inget(self):
        k = Fake({"gid://shopify/Collection/1": kol(1)}); f = tempfile.mktemp()
        self.assertEqual(K.skriv(k, fil([rad(1)]), f, kor=False, logg=lambda *a: None), (1, 0))
        self.assertEqual(k.skrivna, []); self.assertEqual(len(json.load(open(f))), 1)

    def test_skriver_bara_godkanda_med_titel_och_beskrivning(self):
        k = Fake({"gid://shopify/Collection/1": kol(1), "gid://shopify/Collection/2": kol(2)})
        self.assertEqual(K.skriv(k, fil([rad(1), rad(2, godkand="")]), tempfile.mktemp(), kor=True, logg=lambda *a: None), (1, 1))
        self.assertEqual(k.skrivna[0]["seo"], {"title": "Titel 1", "description": "Beskrivning 1"})

    def test_hoppar_over_befintlig_titel_och_andrad_beskrivning(self):
        k = Fake({"gid://shopify/Collection/1": kol(1, st="Finns"), "gid://shopify/Collection/2": kol(2, sd="Annan")})
        self.assertEqual(K.skriv(k, fil([rad(1), rad(2)]), tempfile.mktemp(), kor=True, logg=lambda *a: None), (2, 0))
        self.assertEqual(k.skrivna, [])

    def test_behaller_befintlig_beskrivning(self):
        k = Fake({"gid://shopify/Collection/3": kol(3, sd="Gammal")})
        r = rad(3, nu_d="Gammal"); r["seo_description_forslag"] = "Gammal"
        self.assertEqual(K.skriv(k, fil([r]), tempfile.mktemp(), kor=True, logg=lambda *a: None), (1, 1))

    def test_stoppar_vid_avvikande_aterlasning(self):
        k = Fake({"gid://shopify/Collection/1": kol(1)}, skadlig=True)
        with self.assertRaises(Stopp):
            K.skriv(k, fil([rad(1)]), tempfile.mktemp(), kor=True, logg=lambda *a: None)

    def test_stoppar_vid_fel_adress_och_for_lang_titel(self):
        with self.assertRaises(Stopp):
            K.skriv(Fake({"gid://shopify/Collection/1": kol(9)}), fil([rad(1)]), tempfile.mktemp(), kor=True, logg=lambda *a: None)
        r = rad(1); r["seo_title_forslag"] = "x" * 61
        with self.assertRaises(Stopp):
            K.skriv(Fake({"gid://shopify/Collection/1": kol(1)}), fil([r]), tempfile.mktemp(), kor=True, logg=lambda *a: None)


if __name__ == "__main__":
    unittest.main()
