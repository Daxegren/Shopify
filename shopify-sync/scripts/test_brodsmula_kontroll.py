#!/usr/bin/env python3
"""Nätverksfria tester för brodsmula_kontroll.py. Körning: python3 -I shopify-sync/scripts/test_brodsmula_kontroll.py"""
import copy
import gzip
import importlib.util
import json
import os
import sys
import tempfile
import unittest

HAR = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location("bk", os.path.join(HAR, "brodsmula_kontroll.py"))
bk = importlib.util.module_from_spec(sp)
sys.modules["bk"] = bk
sp.loader.exec_module(bk)

LD = '<script type="application/ld+json">{"@type":"BreadcrumbList","itemListElement":[{"position":1,"name":"Start","item":"https://s.test"},%s{"position":%d,"name":"Kettlebell 8 kg","item":"https://s.test/products/kb"}]}</script>'


def page(crumbs, extra_ld="", canon=1, status_ok=True, other='<a href="/collections/x">x</a>', h1=1):
    nav = '<nav class="custom-breadcrumb" aria-label="breadcrumbs"><a href="/">Hem</a>' + "".join(f'<a href="{h}">{t}</a>' for h, t in crumbs) + '<span class="breadcrumb-current">Kettlebell 8 kg</span></nav>'
    mid = "".join(f'{{"position":{i+2},"name":"{t}","item":"https://s.test{h}"}},' for i, (h, t) in enumerate(crumbs))
    return ("<html><head>" + '<link rel="canonical" href="https://s.test/products/kb">' * canon + (LD % (mid, len(crumbs) + 2)) + extra_ld +
            "</head><body>" + nav + "<h1>x</h1>" * h1 + other + "</body></html>")


BASE = [("/collections/konditionsutrustning", "Kondition")]
NEW = BASE + [("/collections/kettlebell", "Kettlebell")]


class Extract(unittest.TestCase):
    def test_extraherar(self):
        e = bk.extract(page(BASE), "kb")
        self.assertEqual(e["crumbs"][1], ("/collections/konditionsutrustning", "Kondition"))
        self.assertEqual(e["current"], "Kettlebell 8 kg")
        self.assertEqual(e["canonical_count"], 1)
        self.assertEqual(len(e["jsonld_breadcrumbs"][0]), 3)
        self.assertNotIn("/", e["other_links"])      # brödsmulans egna länkar ingår inte i övriga länkar
        self.assertIn("/collections/x", e["other_links"])

    def test_trasig_jsonld(self):
        e = bk.extract(page(BASE, extra_ld='<script type="application/ld+json">{trasig</script>'), "kb")
        self.assertFalse(e["jsonld_valid"])


class Compare(unittest.TestCase):
    def setUp(self):
        self.before = {"kb": bk.extract(page(BASE), "kb")}

    def run_case(self, html):
        return bk.compare(self.before, {"kb": bk.extract(html, "kb")})

    def test_oforandrad_ok(self):
        self.assertTrue(self.run_case(page(BASE))["ok"])

    def test_en_tillagd_kollektionslank_ok(self):
        r = self.run_case(page(NEW))
        self.assertTrue(r["ok"], r["fel"])

    def test_tva_tillagda_fel(self):
        r = self.run_case(page(NEW + [("/collections/y", "Y")]))
        self.assertFalse(r["ok"])

    def test_tillagd_lank_till_icke_kollektion_fel(self):
        self.assertFalse(self.run_case(page(BASE + [("/search?q=x", "Sök")]))["ok"])

    def test_borttagen_lank_fel(self):
        self.assertFalse(self.run_case(page([]))["ok"])

    def test_dubbel_canonical_fel(self):
        self.assertFalse(self.run_case(page(NEW, canon=2))["ok"])

    def test_saknad_ovrig_lank_fel(self):
        self.assertFalse(self.run_case(page(NEW, other=""))["ok"])

    def test_h1_andrat_fel(self):
        self.assertFalse(self.run_case(page(NEW, h1=2))["ok"])

    def test_saknas_i_efter_fel(self):
        self.assertFalse(bk.compare(self.before, {})["ok"])

    def test_schema_tappar_post_fel(self):
        after = bk.extract(page(NEW), "kb")
        after["jsonld_breadcrumbs"] = [after["jsonld_breadcrumbs"][0][:2]]
        self.assertFalse(bk.compare(self.before, {"kb": after})["ok"])

    def test_ordning_andrad_fel(self):
        before = {"kb": bk.extract(page(NEW), "kb")}
        after = bk.extract(page(list(reversed(NEW))), "kb")
        self.assertFalse(bk.compare(before, {"kb": after})["ok"])


class HubbByte(unittest.TestCase):
    OLD = [("/collections/varumarke", "Varumärken")]
    NEW = [("/collections/gymutrustning", "Gymutrustning"), ("/collections/traningsbank", "Träningsbänk")]

    def run_case(self, before_crumbs, after_crumbs, allow):
        b = {"kb": bk.extract(page(before_crumbs), "kb")}
        a = bk.extract(page(after_crumbs), "kb")
        return bk.compare(b, {"kb": a}, allow_hub_change=allow)

    def test_hubbyte_godkanns_bara_nar_tillatet(self):
        self.assertFalse(self.run_case(self.OLD, self.NEW, False)["ok"])
        r = self.run_case(self.OLD, self.NEW, True)
        self.assertTrue(r["ok"], r["fel"])

    def test_hubbyte_till_icke_kollektion_underkanns(self):
        self.assertFalse(self.run_case(self.OLD, [("/collections/gymutrustning", "G"), ("/pages/x", "X")], True)["ok"])

    def test_tva_borttagna_underkanns_aven_nar_tillatet(self):
        self.assertFalse(self.run_case(self.OLD + [("/collections/y", "Y")], self.NEW, True)["ok"])


class Urval(unittest.TestCase):
    def test_stratifierat_urval_ur_gz(self):
        with tempfile.TemporaryDirectory() as d:
            rows = []
            for i in range(10):
                hub = "/collections/cyklar" if i < 6 else "/collections/varumarke"
                rows.append({"url": f"/products/p{i}", "status": 200, "links": [["/", "Hem", "brodsmula", None, "", False], [hub, "H", "brodsmula", None, "", False]]})
            rows.append({"url": "/collections/x", "status": 200, "links": []})
            with gzip.open(os.path.join(d, "sidor.jsonl.gz"), "wt", encoding="utf-8") as f:
                for r in rows:
                    f.write(json.dumps(r) + "\n")
            s = bk.stratified_sample(d, 3)
            self.assertEqual(len(s), 6)
            self.assertEqual(sorted({h for _, h in s}), ["/collections/cyklar", "/collections/varumarke"])
            self.assertEqual(s, bk.stratified_sample(d, 3))      # deterministiskt


if __name__ == "__main__":
    unittest.main(verbosity=1)
