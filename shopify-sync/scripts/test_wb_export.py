import json, os, tempfile, unittest
import wb_export as W


class T(unittest.TestCase):
    def test_jsonl_och_produktrad(self):
        d = tempfile.mkdtemp(); p = os.path.join(d, "p.jsonl")
        rader = [{"id": "gid://shopify/Product/1", "handle": "a", "title": "A", "status": "ACTIVE", "vendor": "V", "productType": "T", "tags": ["x", "y"],
                  "category": None, "seo": {"title": None, "description": "d"}, "description": "abc", "tg": {"value": "[1]"}},
                 {"id": "gid://shopify/MediaImage/9", "alt": "", "__parentId": "gid://shopify/Product/1"},
                 {"id": "gid://shopify/MediaImage/10", "alt": "ok", "__parentId": "gid://shopify/Product/1"}]
        open(p, "w").write("\n".join(json.dumps(r) for r in rader))
        (n, b), = W.las_jsonl(p)
        r = W.produkt_rad(n, b)
        self.assertEqual((r["id"], r["taggar"], r["seo_titel"], r["antal_bilder"], r["bilder_utan_alt"], r["beskrivning_tecken"]), ("1", "x,y", "", 2, 1, 3))

    def test_tackning(self):
        noder = [("a", {"title", "meta_title"}, {"title": False}), ("b", {"title", "body_html"}, {"title": True, "body_html": False}), ("c", {"title"}, {})]
        t = W.tackning(noder)
        self.assertEqual(t["title"], {"finns_i_kalla": 3, "oversatt": 2, "foraldrad": 1})
        self.assertEqual(t["meta_title"], {"finns_i_kalla": 1, "oversatt": 0, "foraldrad": 0})
        self.assertEqual(t["body_html"]["oversatt"], 1)


if __name__ == "__main__":
    unittest.main()
