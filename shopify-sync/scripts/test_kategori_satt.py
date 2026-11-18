import csv, json, os, tempfile, unittest
import kategori_satt as K


class Fake:
    def __init__(self):
        self.cat = {}
    def graphql(self, q, v=None):
        if "productUpdate" in q:
            i = v["p"]["id"]; self.cat[i] = v["p"]["category"]
            return {"productUpdate": {"userErrors": []}}
        return {"nodes": [{"id": i, "title": "x", "vendor": "v", "productType": "", "status": "ACTIVE",
                           "category": ({"id": self.cat[i], "fullName": "n"} if i in self.cat else None)} for i in v["ids"]]}


class T(unittest.TestCase):
    def test_klassa(self):
        for titel, typ, vänta in [
            ("110 Flexfit Fitted Snapback One Size", "Keps", "keps"), ("MSTRDS Letter Snapback", "Keps", "keps"),
            ("UC Daily Socks 3-Pack", "Strumpor", "strumpor"), ("UC Belts Trio", "Bälte", "bälte"),
            ("UC Sunglasses Lefkada 2-Pack", "Solglasögon", "solglasögon"), ("Ryggsäck Color Block One Size", "Ryggsäck", "ryggsäck"),
            ("UC Basic Tee 3-Pack", "T-shirt", "kläder"), ("UC Scuba Zip Hoodie", "Hoodie", "kläder"),
            ("UC High Waist Transparent Tech Mesh Tights", "Tights", "kläder"), ("Basic Trackpants - 2 Pack", "Mjukisbyxor", "kläder"),
            ("MT Lettered Coffee Mug", "Tillbehör", "ingen"), ("Pizza Art Exercise Book 2-Pack", "Tillbehör", "ingen"),
            ("MSTRDS Jersey Beanie Reversible", "Mössa", "manuell"), ("UC Big Classic Necklace 2-Pack", "Halsband", "manuell"),
            ("ZY Highbridge", "Sneakers", "manuell"), ("A Burger Tee heather grey XXL", "Men", "kläder"),
            ("UC Multicolor Bandana 3-Pack", "Bandana", "manuell"), ("BYOU Seamless Thong - Beige", "Underkläder", "kläder")]:
            self.assertEqual(K.klassa(titel, typ), vänta, titel)

    def test_skriv_bara_godkanda_och_kan_koras_om(self):
        d = tempfile.mkdtemp(); p = os.path.join(d, "g.csv")
        with open(p, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter=";"); w.writerow(["produkt_id", "kategori_id", "godkand"])
            w.writerow([1, "gid://shopify/TaxonomyCategory/aa", "ja"]); w.writerow([2, "gid://shopify/TaxonomyCategory/aa", ""])
        k = Fake()
        self.assertEqual(K.skriv(k, p, os.path.join(d, "f.json"), kor=True), (1, 1))
        self.assertEqual(list(k.cat), ["gid://shopify/Product/1"])
        self.assertEqual(K.skriv(k, p, os.path.join(d, "f.json"), kor=True), (1, 0))

    def test_torrkorning_skriver_inget(self):
        d = tempfile.mkdtemp(); p = os.path.join(d, "g.csv")
        open(p, "w", encoding="utf-8").write("produkt_id;kategori_id;godkand\n1;gid://shopify/TaxonomyCategory/aa;ja\n")
        k = Fake(); K.skriv(k, p, os.path.join(d, "f.json")); self.assertEqual(k.cat, {})


if __name__ == "__main__":
    unittest.main()
