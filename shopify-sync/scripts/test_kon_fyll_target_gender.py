import sys, os, json, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
import kon_fyll_target_gender as k

DAM = "gid://shopify/Metaobject/115133645128"; HERR = "gid://shopify/Metaobject/115381502280"


class Falsk:
    def __init__(self, produkter, daligt=False):
        self.p = produkter  # id -> {status, tg(list|None)}
        self.skrivna = []
        self.daligt = daligt
        self.sleep = lambda s: None

    def graphql(self, q, v=None):
        if "metafieldsSet" in q:
            for m in v["m"]:
                i = int(m["ownerId"].split("/")[-1]); self.skrivna.append(i)
                if not self.daligt:
                    self.p[i]["tg"] = json.loads(m["value"])
            return {"metafieldsSet": {"metafields": [], "userErrors": []}}
        out = []
        for g in v["ids"]:
            i = int(g.split("/")[-1]); p = self.p.get(i)
            out.append(None if not p else {"id": g, "status": p["status"], "tg": ({"value": json.dumps(p["tg"])} if p["tg"] else None)})
        return {"nodes": out}


def P(**kw):
    return {"status": "ACTIVE", "tg": None, **kw}


class T(unittest.TestCase):
    def test_torrkorning_skriver_inget(self):
        c = Falsk({1: P(), 2: P()})
        r = k.kor(c, {1: "dam", 2: "herr"}, logg=lambda *_: None)
        self.assertEqual(c.skrivna, []); self.assertEqual(r["att_skriva"], 2)

    def test_skriver_och_laser_tillbaka(self):
        c = Falsk({1: P(), 2: P(), 3: P()})
        with tempfile.TemporaryDirectory() as d:
            f = os.path.join(d, "fore.json")
            r = k.kor(c, {1: "dam", 2: "herr", 3: "dam+herr"}, skriv=True, fore_fil=f, logg=lambda *_: None)
            self.assertEqual(len(json.load(open(f))), 3)
        self.assertEqual(r["skrivna"], 3)
        self.assertEqual(sorted(c.p[3]["tg"]), sorted([DAM, HERR]))

    def test_max_begransar_kanarie(self):
        c = Falsk({i: P() for i in range(1, 31)})
        with tempfile.TemporaryDirectory() as d:
            r = k.kor(c, {i: "herr" for i in range(1, 31)}, skriv=True, max_n=10, fore_fil=os.path.join(d, "f.json"), logg=lambda *_: None)
        self.assertEqual(r["skrivna"], 10); self.assertEqual(len(c.skrivna), 10)

    def test_hoppar_redan_ratt_annat_varde_och_inaktiva(self):
        c = Falsk({1: P(tg=[DAM]), 2: P(tg=[HERR]), 3: P(status="DRAFT"), 4: P()})
        r = k.kor(c, {1: "dam", 2: "dam", 3: "dam", 4: "dam", 5: "dam"}, logg=lambda *_: None)
        self.assertEqual(r["att_skriva"], 1)
        self.assertEqual(r["hoppa"], {"redan_ratt": 1, "annat_varde": 1, "ej_aktiv_eller_saknas": 2})

    def test_overskriv_ersatter_annat_varde(self):
        c = Falsk({2: P(tg=[HERR])})
        with tempfile.TemporaryDirectory() as d:
            r = k.kor(c, {2: "dam"}, skriv=True, overskriv=True, fore_fil=os.path.join(d, "f.json"), logg=lambda *_: None)
        self.assertEqual(c.p[2]["tg"], [DAM])

    def test_stopp_vid_avvikande_aterlasning(self):
        c = Falsk({1: P()}, daligt=True)
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(k.Stopp):
                k.kor(c, {1: "dam"}, skriv=True, fore_fil=os.path.join(d, "f.json"), logg=lambda *_: None)

    def test_fore_fil_krävs(self):
        with self.assertRaises(k.Stopp):
            k.kor(Falsk({1: P()}), {1: "dam"}, skriv=True, logg=lambda *_: None)

    def test_okant_varde_i_csv(self):
        with tempfile.TemporaryDirectory() as d:
            f = os.path.join(d, "m.csv"); open(f, "w").write("produkt_id;varden\n1;kvinna\n")
            with self.assertRaises(k.Stopp):
                k.lasa_mappning(f)

    def test_mutationen_ber_inte_om_ogiltigt_falt(self):
        # Metafield saknar ownerId (felet som stoppade första körningen); id och key finns.
        self.assertNotIn("ownerId}", k.SKRIV.split("userErrors")[0].split("metafields{")[1])
        self.assertIn("id key", k.SKRIV)

    def test_omkorning_hoppar_det_som_ar_gjort(self):
        c = Falsk({1: P(), 2: P()})
        with tempfile.TemporaryDirectory() as d:
            k.kor(c, {1: "dam", 2: "herr"}, skriv=True, fore_fil=os.path.join(d, "f.json"), logg=lambda *_: None)
            r = k.kor(c, {1: "dam", 2: "herr"}, logg=lambda *_: None)
        self.assertEqual(r["att_skriva"], 0)


if __name__ == "__main__":
    unittest.main()
