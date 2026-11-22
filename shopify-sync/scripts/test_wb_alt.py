import json, os, tempfile, unittest
import wb_alt as W


class Fake:
    def __init__(self):
        self.alt = {}
    def graphql(self, q, v=None):
        if "fileUpdate" in q:
            for f in v["f"]:
                self.alt[f["id"]] = f["alt"]
            return {"fileUpdate": {"userErrors": []}}
        return {"nodes": [{"id": i, "alt": self.alt.get(i)} for i in v["ids"]]}


def jsonl(rader):
    p = os.path.join(tempfile.mkdtemp(), "a.jsonl")
    open(p, "w").write("\n".join(json.dumps(r) for r in rader))
    return p


class T(unittest.TestCase):
    def test_bara_tom_alt_och_bilder(self):
        p = jsonl([{"id": "gid://shopify/Product/1", "title": "Tee Black"},
                   {"id": "gid://shopify/MediaImage/1", "alt": "", "__parentId": "gid://shopify/Product/1"},
                   {"id": "gid://shopify/MediaImage/2", "alt": "redan", "__parentId": "gid://shopify/Product/1"},
                   {"id": "gid://shopify/Video/3", "__parentId": "gid://shopify/Product/1"},
                   {"id": "gid://shopify/Product/2", "title": "Hoodie"},
                   {"id": "gid://shopify/MediaImage/4", "alt": None, "__parentId": "gid://shopify/Product/2"}])
        jobb, n = W.att_gora(p)
        self.assertEqual([(i, a) for i, a, _ in jobb], [("gid://shopify/MediaImage/1", "Tee Black"), ("gid://shopify/MediaImage/4", "Hoodie")])
        self.assertEqual(n, 2)

    def test_samma_bild_pa_flera_produkter_skrivs_en_gang(self):
        p = jsonl([{"id": "gid://shopify/Product/1", "title": "Tee XL"},
                   {"id": "gid://shopify/MediaImage/9", "alt": "", "__parentId": "gid://shopify/Product/1"},
                   {"id": "gid://shopify/Product/2", "title": "Tee M"},
                   {"id": "gid://shopify/MediaImage/9", "alt": "", "__parentId": "gid://shopify/Product/2"}])
        jobb, _ = W.att_gora(p)
        self.assertEqual([(i, a) for i, a, _ in jobb], [("gid://shopify/MediaImage/9", "Tee XL")])

    def test_torrkorning_skriver_inget_och_max_produkter(self):
        jobb = [(f"m{i}", "T", f"p{i // 3}") for i in range(9)]
        k, d = Fake(), tempfile.mkdtemp()
        self.assertEqual(W.kor(k, jobb, os.path.join(d, "f.jsonl"), skriv=False, max_produkter=2), (6, 0))
        self.assertEqual(k.alt, {})
        self.assertEqual(W.kor(k, jobb, os.path.join(d, "f.jsonl"), skriv=True, max_produkter=2, sleep=lambda s: None), (6, 6))
        self.assertEqual(len(k.alt), 6)

    def test_avvikande_aterlasning_stoppar(self):
        class Dalig(Fake):
            def graphql(self, q, v=None):
                r = super().graphql(q, v)
                if "nodes" in r: r["nodes"][0]["alt"] = "fel"
                return r
        with self.assertRaises(W.Stopp):
            W.skriv_grupp(Dalig(), [("m1", "T", "p")])

    def test_utesluter_produkter_med_tagg(self):
        p = jsonl([{"id": "gid://shopify/Product/1", "title": "Tee", "tags": ["price-change-job-active"]},
                   {"id": "gid://shopify/MediaImage/1", "alt": "", "__parentId": "gid://shopify/Product/1"},
                   {"id": "gid://shopify/Product/2", "title": "Hoodie", "tags": ["texter-klara"]},
                   {"id": "gid://shopify/MediaImage/2", "alt": "", "__parentId": "gid://shopify/Product/2"}])
        jobb, n = W.att_gora(p, "price-change-job-active")
        self.assertEqual([i for i, _, _ in jobb], ["gid://shopify/MediaImage/2"]); self.assertEqual(n, 1)
        self.assertEqual(len(W.att_gora(p)[0]), 2)

    def test_aterstall_bara_oforandrad_alt(self):
        k, d = Fake(), tempfile.mkdtemp()
        f = os.path.join(d, "fore.jsonl")
        open(f, "w").write("\n".join(json.dumps({"media_id": i, "produkt": "p", "fore": None, "ny": a}) for i, a in (("m1", "A"), ("m2", "B"), ("m3", "C"))))
        k.alt = {"m1": "A", "m2": "andrad av någon", "m3": "C"}
        self.assertEqual(W.aterstall(k, f, skriv=False), (2, 1)); self.assertEqual(k.alt["m1"], "A")
        self.assertEqual(W.aterstall(k, f, skriv=True, sleep=lambda s: None), (2, 1))
        self.assertEqual((k.alt["m1"], k.alt["m2"], k.alt["m3"]), ("", "andrad av någon", ""))


if __name__ == "__main__":
    unittest.main()
