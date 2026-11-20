import csv, json, tempfile, unittest
import kollektion_oversattning_skriv as K
from kon_fyll_target_gender import Stopp


class Fake:
    def __init__(self, kalla, befintlig=None, trasig=False):
        self.kalla = kalla; self.tr = dict(befintlig or {}); self.trasig = trasig; self.reg = []

    def graphql(self, q, v=None):
        if "currentAppInstallation" in q:
            return {"currentAppInstallation": {"accessScopes": [{"handle": h} for h in getattr(self, "scopes", ["write_translations"])]}}
        if "translationsRegister" in q:
            for t in v["t"]:
                self.reg.append(t)
                self.tr[(t["locale"], t["key"])] = "?" if self.trasig else t["value"]
            return {"translationsRegister": {"userErrors": []}}
        l = v["l"]
        return {"translatableResource": {"translatableContent": [{"key": k, "value": s, "digest": "dig-" + k} for k, s in self.kalla.items()],
                                         "translations": [{"key": k, "value": val, "outdated": False} for (loc, k), val in self.tr.items() if loc == l]}}


def fil(rader):
    f = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8", newline="")
    w = csv.DictWriter(f, fieldnames=["handle", "kollektion_id", "locale", "key", "svenska", "oversattning", "godkand"], delimiter=";")
    w.writeheader(); w.writerows(rader); f.close(); return f.name


def rad(loc="da", key="meta_title", sv="Svensk titel", ov="Dansk titel", g="ja"):
    return {"handle": "h", "kollektion_id": "1", "locale": loc, "key": key, "svenska": sv, "oversattning": ov, "godkand": g}


ST = {"meta_title": "Svensk titel", "meta_description": "Svensk beskrivning"}


class T(unittest.TestCase):
    def test_torrkorning_skriver_inget(self):
        k = Fake(ST)
        self.assertEqual(K.skriv(k, fil([rad()]), tempfile.mktemp(), kor=False, logg=lambda *a: None), (1, 0)); self.assertEqual(k.reg, [])

    def test_skriver_med_live_digest_och_laser_tillbaka(self):
        k = Fake(ST)
        self.assertEqual(K.skriv(k, fil([rad(), rad(g="")]), tempfile.mktemp(), kor=True, logg=lambda *a: None), (1, 1))
        self.assertEqual(k.reg[0]["translatableContentDigest"], "dig-meta_title")

    def test_skriver_inte_over_befintlig_oversattning(self):
        k = Fake(ST, befintlig={("da", "meta_title"): "Finns redan"})
        self.assertEqual(K.skriv(k, fil([rad()]), tempfile.mktemp(), kor=True, logg=lambda *a: None), (1, 0)); self.assertEqual(k.reg, [])

    def test_hoppar_over_nar_kallan_andrats(self):
        k = Fake({"meta_title": "Ny svensk titel", "meta_description": "x"})
        self.assertEqual(K.skriv(k, fil([rad()]), tempfile.mktemp(), kor=True, logg=lambda *a: None), (1, 0)); self.assertEqual(k.reg, [])

    def test_stoppar_vid_avvikande_aterlasning_och_ogiltiga_rader(self):
        with self.assertRaises(Stopp):
            K.skriv(Fake(ST, trasig=True), fil([rad()]), tempfile.mktemp(), kor=True, logg=lambda *a: None)
        for r in (rad(ov="x" * 61), rad(loc="sv"), rad(key="title"), rad(ov="")):
            with self.assertRaises(Stopp):
                K.skriv(Fake(ST), fil([r]), tempfile.mktemp(), kor=True, logg=lambda *a: None)


    def test_stoppar_utan_behorighet(self):
        k = Fake(ST)
        k.scopes = ["read_products"]
        with self.assertRaises(Stopp):
            K.skriv(k, fil([rad()]), tempfile.mktemp(), kor=True, logg=lambda *a: None)
        self.assertEqual(k.reg, [])


if __name__ == "__main__":
    unittest.main()
