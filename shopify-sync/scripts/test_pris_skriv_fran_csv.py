import sys, os, json, tempfile, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
import pris_skriv_fran_csv as s


class Falsk:
    def __init__(self, varianter):
        self.v = varianter  # id -> dict(price, jmf, inkop, tags)
        self.skrivna = []

    def graphql(self, q, v=None):
        if "productVariantsBulkUpdate" in q:
            x = v["v"][0]
            self.skrivna.append(x)
            vid = x["id"].split("/")[-1]
            self.v[vid]["price"] = x["price"]
            self.v[vid]["jmf"] = x["compareAtPrice"]
            return {"productVariantsBulkUpdate": {"productVariants": [], "userErrors": []}}
        vid = v["id"].split("/")[-1]
        d = self.v.get(vid)
        if not d:
            return {"productVariant": None}
        return {"productVariant": {"id": f"gid://shopify/ProductVariant/{vid}", "price": d["price"],
                                   "compareAtPrice": d["jmf"], "product": {"id": "gid://shopify/Product/1", "tags": d.get("tags", [])},
                                   "inventoryItem": {"unitCost": {"amount": d["inkop"]}}}}


def rad(vid, pris_nu, nytt, inkop, godkand="ja", sku="S"):
    return {"variant_id": vid, "sku": sku, "pris_nu": pris_nu, "nytt_pris": nytt, "inkop": inkop, "godkand": godkand}


IDAG_OK = datetime.date(2026, 12, 2)


class T(unittest.TestCase):
    def test_torrkorning_skriver_inget(self):
        k = Falsk({"1": {"price": "39.00", "jmf": None, "inkop": "49.00"}})
        r = s.kor(k, [rad("1", "39.00", "109.00", "49.00")], skriv=False, logg=lambda *_: None)
        self.assertEqual(k.skrivna, [])
        self.assertEqual(r["planerade"], 1)

    def test_sparr_fore_1_dec(self):
        k = Falsk({"1": {"price": "39.00", "jmf": None, "inkop": "49.00"}})
        with self.assertRaises(s.Stopp):
            s.kor(k, [rad("1", "39.00", "109.00", "49.00")], skriv=True, fore_fil="x", idag=datetime.date(2026, 11, 30), logg=lambda *_: None)
        self.assertEqual(k.skrivna, [])

    def test_skriver_godkand_och_rensar_jamforpris(self):
        k = Falsk({"1": {"price": "39.00", "jmf": "39.00", "inkop": "49.00"}})
        with tempfile.TemporaryDirectory() as d:
            f = os.path.join(d, "fore.json")
            r = s.kor(k, [rad("1", "39.00", "109.00", "49.00")], skriv=True, fore_fil=f, idag=IDAG_OK, logg=lambda *_: None)
            self.assertEqual(r["skrivna"], 1)
            self.assertEqual(json.load(open(f))[0]["fore_pris"], 39.0)
        self.assertEqual(k.skrivna[0]["price"], "109.00")
        self.assertIsNone(k.skrivna[0]["compareAtPrice"])

    def test_ej_godkand_skrivs_inte(self):
        k = Falsk({"1": {"price": "39.00", "jmf": None, "inkop": "49.00"}})
        r = s.kor(k, [rad("1", "39.00", "109.00", "49.00", godkand="")], skriv=True, fore_fil="x", idag=IDAG_OK, logg=lambda *_: None)
        self.assertEqual(k.skrivna, [])

    def test_stopp_om_livepris_andrats(self):
        k = Falsk({"1": {"price": "45.00", "jmf": None, "inkop": "49.00"}})
        with self.assertRaises(s.Stopp):
            s.kor(k, [rad("1", "39.00", "109.00", "49.00")], skriv=False, logg=lambda *_: None)

    def test_stopp_om_inkop_andrats(self):
        k = Falsk({"1": {"price": "39.00", "jmf": None, "inkop": "60.00"}})
        with self.assertRaises(s.Stopp):
            s.kor(k, [rad("1", "39.00", "109.00", "49.00")], skriv=False, logg=lambda *_: None)

    def test_prisjobb_hoppas_over(self):
        k = Falsk({"1": {"price": "39.00", "jmf": None, "inkop": "49.00", "tags": ["price-change-job-active"]}})
        r = s.kor(k, [rad("1", "39.00", "109.00", "49.00")], skriv=True, fore_fil="x", idag=IDAG_OK, logg=lambda *_: None)
        self.assertEqual(k.skrivna, [])
        self.assertEqual(r["hoppade"], 1)

    def test_rea_hoppas_over(self):
        k = Falsk({"1": {"price": "899.00", "jmf": "999.00", "inkop": "400.00"}})
        r = s.kor(k, [rad("1", "899.00", "679.00", "400.00")], skriv=True, fore_fil="x", idag=IDAG_OK, logg=lambda *_: None)
        self.assertEqual(k.skrivna, [])
        self.assertEqual(r["hoppade"], 1)

    def test_redan_ratt_pris_hoppas(self):
        k = Falsk({"1": {"price": "109.00", "jmf": None, "inkop": "49.00"}})
        r = s.kor(k, [rad("1", "39.00", "109.00", "49.00")], skriv=True, fore_fil="x", idag=IDAG_OK, logg=lambda *_: None)
        self.assertEqual(k.skrivna, [])

    def test_stopp_vid_avvikande_aterlasning(self):
        class Dalig(Falsk):
            def graphql(self, q, v=None):
                if "productVariantsBulkUpdate" in q:
                    return {"productVariantsBulkUpdate": {"productVariants": [], "userErrors": []}}  # skriver inget
                return super().graphql(q, v)
        k = Dalig({"1": {"price": "39.00", "jmf": None, "inkop": "49.00"}})
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(s.Stopp):
                s.kor(k, [rad("1", "39.00", "109.00", "49.00")], skriv=True, fore_fil=os.path.join(d, "f.json"), idag=IDAG_OK, logg=lambda *_: None)


if __name__ == "__main__":
    unittest.main()
