#!/usr/bin/env python3
"""Nätverksfria tester för intern_lankning_mat.py. Körning: python3 -I shopify-sync/scripts/test_intern_lankning_mat.py
Ingen riktig hämtning görs: hämtningen ersätts av en låtsashämtare. Inga hemligheter läses."""
import importlib.util
import json
import os
import sys
import tempfile
import unittest
from types import SimpleNamespace

HAR = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("ilm", os.path.join(HAR, "intern_lankning_mat.py"))
ilm = importlib.util.module_from_spec(_spec)
sys.modules["ilm"] = ilm
_spec.loader.exec_module(ilm)

HOST = "shop.test"
BASE = "https://shop.test"

PAGE = """<html><head><title>Kettlebell</title><link rel="canonical" href="https://shop.test/collections/kettlebell">
<meta name="robots" content="index, follow"></head><body>
<div id="shopify-section-sections--1__header" class="shopify-section shopify-section-group-header-group">
  <a href="/collections/cyklar">CYKLAR</a><a href="/collections/elcyklar?utm_source=x&pr_prod_strat=1">Elcykel</a>
  <a href="/">Hem</a><a href="/cart">Kundvagn</a>
</div>
<main id="main-content">
  <div id="shopify-section-template--1__collection-products" class="shopify-section">
    <nav aria-label="Breadcrumb"><a href="/">Start</a><a href="/collections/gym">Gym</a></nav>
    <ul class="custom-sidebar-menu"><li><a href="/collections/fria-vikter">FRIA VIKTER</a></li></ul>
    <a href="/products/kb-8">Kettlebell 8 kg</a>
    <a href="/collections/kettlebell/products/kb-12"><img src="x.jpg" alt="Kettlebell 12 kg"></a>
    <a href="/collections/kettlebell-jarn">Läs mer</a>
    <a href="/collections/kettlebell-jarn">Läs mer</a>
    <a href="/collections/viktstall?filter.v.price.gte=1">filter</a>
    <a href="/pages/{{ shop_url }}">trasig</a>
    <a href="https://www.instagram.com/x">extern</a>
    <a href="mailto:a@b.c">mejl</a>
    <ul class="pagination"><a href="/collections/kettlebell?page=2">2</a></ul>
    <ul><li class="js-pagination-result"><a href="/products/kb-20">Kettlebell 20 kg</a></li></ul>
  </div>
</main>
<div class="shopify-section shopify-section-group-footer-group"><a href="/pages/om">Om oss</a></div>
</body></html>"""


class RobotsTest(unittest.TestCase):
    TXT = """User-agent: *
Allow: /
Disallow: /cart/
Disallow: /collections/*sort_by*
Disallow: /*?*oseid=*
Disallow: /account
Allow: /account/login
User-agent: adsbot-google
Disallow: /
"""

    def test_regler(self):
        r = ilm.Robots(self.TXT)
        self.assertTrue(r.allowed("/collections/x"))
        self.assertFalse(r.allowed("/cart/add"))
        self.assertFalse(r.allowed("/collections/x?sort_by=price"))
        self.assertFalse(r.allowed("/products/x?oseid=1"))
        self.assertFalse(r.allowed("/account"))
        self.assertTrue(r.allowed("/account/login"))   # längre Allow vinner
        self.assertTrue(r.allowed("/"))               # adsbot-gruppen gäller inte oss

    def test_tom_robots_tillater_allt(self):
        self.assertTrue(ilm.Robots("").allowed("/vad/som/helst"))

    def test_dollar_ankare(self):
        r = ilm.Robots("User-agent: *\nDisallow: /*.pdf$\n")
        self.assertFalse(r.allowed("/a/b.pdf"))
        self.assertTrue(r.allowed("/a/b.pdf?x=1"))


class LankTest(unittest.TestCase):
    def test_spårning_strippas(self):
        self.assertEqual(ilm.strip_fragment_and_tracking("/collections/x?utm_source=a&pr_prod_strat=b&page=2#top"),
                         ("/collections/x?page=2", ["utm_source", "pr_prod_strat"]))
        self.assertEqual(ilm.strip_fragment_and_tracking("/collections/x/")[0], "/collections/x")
        self.assertEqual(ilm.strip_fragment_and_tracking("/products/x?variant=1")[0], "/products/x?variant=1")

    def test_klassificering(self):
        c = ilm.classify_target
        self.assertEqual(c("/collections/kettlebell"), ("collection", "/collections/kettlebell"))
        self.assertEqual(c("/collections/kettlebell?page=2"), ("collection", "/collections/kettlebell?page=2"))
        self.assertEqual(c("/collections/kettlebell?page=1"), ("collection", "/collections/kettlebell"))
        self.assertEqual(c("/collections/x?filter.v.price.gte=1")[0], "filter")
        self.assertEqual(c("/collections/x/products/y"), ("product", "/products/y"))
        self.assertEqual(c("/products/y?variant=3"), ("product", "/products/y"))
        self.assertEqual(c("/")[0], "home")
        self.assertEqual(c("/blogs/news/artikel")[0], "article")
        self.assertEqual(c("/cart")[0], "other")

    def test_generiska_ankare(self):
        for t in ("Läs mer", "klicka här", "  Se alla ", "Visa mer.", "»"):
            self.assertTrue(ilm.is_generic_anchor(t), t)
        for t in ("Kettlebell", "Elcykel", "Gå till Barncykel", ""):
            self.assertFalse(ilm.is_generic_anchor(t), t)

    def test_extrahera_regioner(self):
        ex = ilm.extract_links(PAGE, BASE + "/collections/kettlebell", HOST)
        by = {(l[0], l[2]): l for l in ex["links"]}
        self.assertIn(("/collections/cyklar", "meny"), by)
        # spårning flaggas men adressen rensas
        el = by[("/collections/elcyklar", "meny")]
        self.assertEqual(el[4], "pr_prod_strat,utm_source")
        self.assertIn(("/collections/fria-vikter", "sidomeny"), by)
        self.assertIn(("/", "brodsmula"), by)
        self.assertIn(("/collections/gym", "brodsmula"), by)
        self.assertIn(("/collections/kettlebell?page=2", "paginering"), by)
        self.assertIn(("/pages/om", "sidfot"), by)
        # produktlistans js-pagination-result är innehåll, inte paginering
        self.assertIn(("/products/kb-20", "innehall"), by)
        # innehållslänk, bildlänk får alt som ankartext, dubblett slås ihop
        self.assertEqual(by[("/products/kb-8", "innehall")][1], "Kettlebell 8 kg")
        self.assertEqual(by[("/collections/kettlebell/products/kb-12", "innehall")][1], "[bild] Kettlebell 12 kg")
        jarn = [l for l in ex["links"] if l[0] == "/collections/kettlebell-jarn"]
        self.assertEqual(len(jarn), 1)
        self.assertEqual(jarn[0][1], "Läs mer")
        self.assertEqual(ex["ext"], 1)
        self.assertEqual(ex["malformed"], 1)
        self.assertEqual(ex["meta"]["title"], "Kettlebell")
        self.assertEqual(ex["meta"]["canonical"], "https://shop.test/collections/kettlebell")

    def test_www_räknas_som_samma_domän(self):
        ex = ilm.extract_links('<main><a href="https://www.shop.test/collections/a">A</a></main>', BASE + "/", HOST)
        self.assertEqual(ex["ext"], 0)
        self.assertEqual(ex["links"][0][0], "/collections/a")


class Fake:
    """Låtsashämtare: pages = {sökväg: (status, html, [hopp])}"""

    def __init__(self, pages, sitemap_paths):
        self.pages, self.sitemap_paths, self.calls = pages, sitemap_paths, []
        self.fetcher = self

    def fetch(self, url, **kw):
        path = url[len(BASE):] or "/"
        self.calls.append(path)
        H = SimpleNamespace
        if path == "/robots.txt":
            return H(status=200, body=b"User-agent: *\nDisallow: /cart/\n", hops=[H(url=url, status=200)], redirect_count=0, final_url=url, headers={}, error=None, is_html=False)
        if path == "/sitemap.xml":
            xml = '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{BASE}{p}</loc></url>" for p in self.sitemap_paths) + "</urlset>"
            return H(status=200, body=xml.encode(), hops=[H(url=url, status=200)], redirect_count=0, final_url=url, headers={}, error=None, is_html=False)
        status, html, *rest = self.pages.get(path, (404, "<html><body>nej</body></html>"))
        if status in (301, 302):
            target = rest[0]
            fin = self.pages.get(target, (200, "<html></html>"))
            return H(status=fin[0], body=fin[1].encode(), hops=[H(url=url, status=status), H(url=BASE + target, status=fin[0])], redirect_count=1,
                     final_url=BASE + target, headers={"content-type": "text/html"}, error=None, is_html=True)
        return H(status=status, body=html.encode(), hops=[H(url=url, status=status)], redirect_count=0, final_url=url,
                 headers={"content-type": "text/html"}, error=None, is_html=True)


def page(header="", main="", footer=""):
    return (f'<html><head><title>t</title></head><body><div class="shopify-section-group-header-group">{header}</div>'
            f'<main>{main}</main><div class="shopify-section-group-footer-group">{footer}</div></body></html>')


MENU = '<a href="/collections/a">Alfa</a><a href="/collections/b">Beta</a>'
SITE = {
    "/": (200, page(MENU, '<a href="/collections/a">Alfa</a>')),
    "/collections/a": (200, page(MENU, '<a href="/collections/c">klicka här</a><a href="/products/p1">P1</a><a href="/collections/a?page=2">2</a>')),
    "/collections/a?page=2": (200, page(MENU, '<a href="/products/p2">P2</a>')),
    "/collections/b": (200, page(MENU, '<a href="/collections/gammal">Gammal</a><a href="/collections/noidx">Noidx</a><a href="/products/borta">Borta</a>')),
    "/collections/c": (200, page(MENU, '<a href="/products/p1">P1</a>')),
    "/collections/orphan": (200, page(MENU, "")),
    "/collections/gammal": (301, "", "/collections/a"),
    "/collections/noidx": (200, '<html><head><meta name="robots" content="noindex"></head><body><main></main></body></html>'),
    "/products/p1": (200, page(MENU, '<a href="/collections/a">Alfa</a>')),
    "/products/p2": (200, page(MENU, '<a href="/collections/a">Alfa</a>')),
    "/products/p3": (200, page(MENU, "")),
    "/products/borta": (404, "x"),
}
SM = ["/", "/collections/a", "/collections/b", "/collections/c", "/collections/orphan", "/products/p1", "/products/p2", "/products/p3"]


def run_crawl(d, fake=None, **kw):
    fake = fake or Fake(SITE, SM)
    meta = ilm.crawl(BASE, d, fake, threads=2, progress_every=1000, **kw)
    return fake, meta


class CrawlTest(unittest.TestCase):
    def test_crawl_upptäcker_sidor_och_respekterar_robots(self):
        with tempfile.TemporaryDirectory() as d:
            fake, meta = run_crawl(d)
            recs, blocks, _ = ilm.load_run(d)
            self.assertIn("/collections/a?page=2", recs)              # pagineringen följdes
            self.assertIn("/products/borta", recs)                    # länkad men inte i sitemapen
            self.assertEqual(recs["/products/borta"]["status"], 404)
            self.assertNotIn("/cart", fake.calls)
            self.assertEqual(meta["produkter_i_sitemap"], 3)
            self.assertEqual(len(blocks), 1)                          # menyn lagras en gång
            self.assertIsNone(meta["stopp"])

    def test_läser_komprimerad_körning(self):
        import gzip
        import shutil
        with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as d2:
            run_crawl(d)
            for n in ("sidor.jsonl", "block.jsonl"):
                with open(os.path.join(d, n), "rb") as src, gzip.open(os.path.join(d2, n + ".gz"), "wb") as dst:
                    shutil.copyfileobj(src, dst)
            shutil.copy(os.path.join(d, "meta.json"), os.path.join(d2, "meta.json"))
            a, b = ilm.load_run(d), ilm.load_run(d2)
            self.assertEqual(a[0], b[0])
            self.assertEqual(a[1], b[1])

    def test_återupptag_hämtar_inte_om(self):
        with tempfile.TemporaryDirectory() as d:
            run_crawl(d)
            fake2, _ = run_crawl(d)
            self.assertEqual([c for c in fake2.calls if c not in ("/robots.txt", "/sitemap.xml")], [])

    def test_hoppa_over_sidtyp(self):
        site = dict(SITE)
        site["/blogs/news/a1"] = (200, page(MENU, ""))
        site["/collections/c"] = (200, page(MENU, '<a href="/blogs/news/a2">x</a>'))
        with tempfile.TemporaryDirectory() as d:
            fake = Fake(site, SM + ["/blogs/news/a1"])
            _, meta = run_crawl(d, fake=fake, skip_types=("article",))
            self.assertNotIn("/blogs/news/a1", fake.calls)
            self.assertNotIn("/blogs/news/a2", fake.calls)
            self.assertEqual(meta["hoppade_over_sidtyper"], ["article"])

    def test_produkturval(self):
        with tempfile.TemporaryDirectory() as d:
            _, meta = run_crawl(d, products=2, seed=3)
            recs, _, _ = ilm.load_run(d)
            hamtade = [u for u in recs if u.startswith("/products/") and u != "/products/borta"]
            self.assertLessEqual(len(hamtade), 2 + 0)
            self.assertEqual(meta["produkturval"], "slumpmässigt urval, seed 3")


class AnalysTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = tempfile.TemporaryDirectory()
        run_crawl(cls.d.name)
        cls.recs, cls.blocks, cls.meta = ilm.load_run(cls.d.name)
        cls.res = ilm.analyze(cls.recs, cls.blocks, set(SM), HOST, None, [("a", None), ("b", "c")])
        cls.rows = {r["sida"]: r for r in cls.res["rows"]}
        cls.coll = {c["kollektion"]: c for c in cls.res["collections"]}

    @classmethod
    def tearDownClass(cls):
        cls.d.cleanup()

    def test_föräldralös(self):
        # live (200), i sitemapen och utan någon inlänk (inte ens från menyn) -> föräldralös
        self.assertEqual(self.rows["/collections/orphan"]["inlankar_totalt_unika_sidor"], 0)
        self.assertTrue(self.rows["/collections/orphan"]["foraldralos"])
        self.assertTrue(self.rows["/products/p3"]["foraldralos"])
        self.assertFalse(self.rows["/products/p1"]["foraldralos"])
        self.assertEqual(self.rows["/collections/orphan"]["orsak_typ_av_lank"], "ingen inlänk")

    def test_omdirigerad_adress_är_ingen_källa(self):
        # /collections/gammal omdirigerar till /collections/a och får a:s innehåll; c ska bara räknas från a
        self.assertEqual(self.coll["/collections/c"]["innehall_fran_kollektion"], 1)

    def test_bara_navigation(self):
        self.assertTrue(self.rows["/collections/b"]["bara_navigation"])       # b länkas bara från menyn
        self.assertFalse(self.rows["/collections/a"]["bara_navigation"])

    def test_inlänkar_uppdelade(self):
        a = self.coll["/collections/a"]
        self.assertTrue(a["i_meny"])
        self.assertEqual(a["innehall_fran_produkt"], 2)       # p1 och p2
        self.assertEqual(a["innehall_fran_startsida"], 1)
        self.assertEqual(a["paginering_kallsidor"], 0)        # sida 2 räknas som samma källa (självlänk) och exkluderas
        c = self.coll["/collections/c"]
        self.assertFalse(c["i_meny"])
        self.assertEqual(c["innehall_fran_kollektion"], 1)
        self.assertEqual(c["generiska_ankare_innehall"], 1)   # 'klicka här'

    def test_djup(self):
        da = self.res["depth_all"]
        self.assertEqual(da["collection"]["onaadda"], 1)      # orphan nås aldrig
        self.assertEqual(da["product"]["onaadda"], 1)         # p3
        dc = self.res["depth_content"]
        self.assertEqual(dc["collection"]["nadda"], 2)        # a (startsidan) och c (via a)... b nås bara via menyn
        self.assertEqual(self.rows["/collections/c"]["djup_utan_meny_sidfot_sidomeny"], 2)
        self.assertEqual(self.rows["/collections/c"]["djup_alla_lankar"], 2)
        self.assertEqual(self.rows["/collections/a"]["djup_alla_lankar"], 1)

    def test_ankartext_räknas_per_unik_källsida(self):
        # p1 länkas från a (och a?page=2 räknas som a): ankartexten 'p1' har en källa per unik sida
        rows = [x for x in self.res["anchors_long"] if x[0] == "/collections/a" and x[1] == "innehall"]
        self.assertTrue(all(v <= 3 for (_, _, _, v) in rows))
        self.assertEqual(sum(v for (_, _, a, v) in rows if a == "alfa"), 3)    # startsidan, p1, p2

    def test_pagineringssida_är_ett_eget_steg_i_djupet(self):
        # p1 ligger på a (djup 1) -> djup 2; p2 ligger bara på a?page=2 (djup 2) -> djup 3
        self.assertEqual(self.rows["/products/p1"]["djup_alla_lankar"], 2)
        self.assertEqual(self.rows["/products/p2"]["djup_alla_lankar"], 3)

    def test_problemlänkar(self):
        pr = {p["mal"]: p for p in self.res["problems"]}
        self.assertEqual(pr["/collections/gammal"]["problem"], "omdirigerad")
        self.assertEqual(pr["/collections/noidx"]["problem"], "noindex")
        self.assertEqual(pr["/products/borta"]["problem"], "404 (finns inte)")
        self.assertNotIn("/collections/a", pr)

    def test_menyblock_räknas_per_unik_sida_utan_självlänk(self):
        # menyn finns på /, a, b, c, orphan, p1, p2, p3 (a?page=2 räknas som a, den omdirigerade adressen och noindex-sidan saknar meny)
        self.assertEqual(self.coll["/collections/a"]["meny_sidor"], 7)     # alla utom a själv
        self.assertEqual(self.coll["/collections/b"]["meny_sidor"], 7)
        self.assertEqual(self.coll["/collections/c"]["meny_sidor"], 0)     # c finns inte i menyn

    def test_tvillingar_rapporterar_saknad_sida(self):
        tw = {t["handle"]: t for t in self.res["twins"]}
        self.assertEqual(tw["a"]["status"], 200)
        self.assertEqual(tw["c"]["roll"], "bas")
        self.assertEqual(tw["b"]["status"], 200)


class SammanställningTest(unittest.TestCase):
    def test_matvarden_md_innehåller_alla_avsnitt(self):
        with tempfile.TemporaryDirectory() as d:
            run_crawl(d)
            recs, blocks, meta = ilm.load_run(d)
            res = ilm.analyze(recs, blocks, set(SM), HOST, None, [("a", "a-se")])
            gsc = ilm.weakest_visible(res["collections"], [{"handle": "a", "visningar": 10, "position": 5.0}])
            md = ilm.matvarden_md(res, recs, meta, gsc)
            for rubrik in ("(a) Föräldralösa", "(b) Klickdjup", "(c) Inlänkar", "(d) Ankartexter", "(e) Länkar till", "(f) Interna länkar", "(g) Tvillingkollektioner", "(h) Search Console"):
                self.assertIn(rubrik, md)
            self.assertIn("'klicka här'", md)
            self.assertIn("/collections/gammal", md)       # omdirigerad länk redovisas

    def test_brödsmula_räknas_som_egen_källa(self):
        site = dict(SITE)
        site["/products/p1"] = (200, page(MENU, '<nav aria-label="Breadcrumb"><a href="/collections/c">C</a></nav>'))
        with tempfile.TemporaryDirectory() as d:
            ilm.crawl(BASE, d, Fake(site, SM), threads=1, progress_every=1000)
            recs, blocks, _ = ilm.load_run(d)
            res = ilm.analyze(recs, blocks, set(SM), HOST)
            self.assertIn(("product", "/collections/c", 1), res["breadcrumb_targets"])
            c = {x["kollektion"]: x for x in res["collections"]}["/collections/c"]
            self.assertEqual(c["brodsmula_kallsidor"], 1)
            self.assertEqual(c["innehall_totalt"], 2)       # a (länk 'klicka här') + p1 (brödsmula)


class SpårningTest(unittest.TestCase):
    def test_spårning_räknas(self):
        site = dict(SITE)
        site["/collections/b"] = (200, page(MENU, '<a href="/products/p1?utm_source=n&pr_prod_strat=x">P1</a>'))
        with tempfile.TemporaryDirectory() as d:
            ilm.crawl(BASE, d, Fake(site, SM), threads=1, progress_every=1000)
            recs, blocks, _ = ilm.load_run(d)
            res = ilm.analyze(recs, blocks, set(SM), HOST)
            self.assertEqual(res["tracking"]["per_parameter"], {"utm_source": 1, "pr_prod_strat": 1})
            self.assertEqual(res["tracking"]["per_region"], {"innehall": 1})


class PolitFetchTest(unittest.TestCase):
    def test_pausar_och_avbryter(self):
        class F:
            def fetch(self, url):
                return SimpleNamespace(status=429, error="429 Too Many Requests", hops=[], body=b"")
        sleeps = []
        pf = ilm.PoliteFetcher(F(), max_consecutive=2, pause_s=10, max_pauses=2, sleep=sleeps.append)
        with self.assertRaises(ilm.Abort):
            for _ in range(20):
                pf.fetch("x")
        self.assertEqual(sleeps, [10, 20])

    def test_sänker_takten_efter_paus(self):
        class F:
            limiter = SimpleNamespace(interval=1.0)

            def fetch(self, url):
                return SimpleNamespace(status=503, error=None, hops=[1], body=b"")
        f = F()
        pf = ilm.PoliteFetcher(f, max_consecutive=1, pause_s=0, max_pauses=2, sleep=lambda s: None)
        with self.assertRaises(ilm.Abort):
            for _ in range(5):
                pf.fetch("x")
        self.assertAlmostEqual(f.limiter.interval, 2.25)

    def test_lyckad_hämtning_nollställer(self):
        res = iter([429, 429, 200, 429, 200])

        class F:
            def fetch(self, url):
                s = next(res)
                return SimpleNamespace(status=s, error=None, hops=[1], body=b"")
        pf = ilm.PoliteFetcher(F(), max_consecutive=3, sleep=lambda s: self.fail("ska inte pausa"))
        for _ in range(5):
            pf.fetch("x")

    def test_gräns_för_hastighet(self):
        self.assertLessEqual(ilm.MAX_RPS, 3.0)
        self.assertNotIn("@", ilm.USER_AGENT)


class UrvalTest(unittest.TestCase):
    def test_grupper(self):
        base = {"status": 200, "i_meny": True, "innehall_totalt": 1, "innehall_fran_kollektion": 1, "innehall_fran_artikel": 0}
        ctab = [dict(base, kollektion="/collections/proteinpulver"), dict(base, kollektion="/collections/barncyklar"),
                dict(base, kollektion="/collections/kettlebell")]
        out = ilm.urval_gruppsidor(ctab)
        self.assertEqual([(o["grupp"], o["kollektion"]) for o in out], [("barn/junior", "/collections/barncyklar"), ("kosttillskott", "/collections/proteinpulver")])


class GscTest(unittest.TestCase):
    def test_svagast_först(self):
        ctab = [{"kollektion": "/collections/a", "status": 200, "i_meny": True, "sidomeny_kallsidor": 5, "innehall_totalt": 10,
                 "innehall_fran_kollektion": 1, "innehall_fran_produkt": 9, "innehall_fran_artikel": 0, "djup_utan_navigation": 2, "ankare_innehall": "A (1)"},
                {"kollektion": "/collections/b", "status": 200, "i_meny": False, "sidomeny_kallsidor": 0, "innehall_totalt": 1,
                 "innehall_fran_kollektion": 1, "innehall_fran_produkt": 0, "innehall_fran_artikel": 0, "djup_utan_navigation": 3, "ankare_innehall": ""}]
        out = ilm.weakest_visible(ctab, [{"handle": "a", "visningar": 100, "position": 5.0}, {"handle": "b", "visningar": 50, "position": 9.0},
                                         {"handle": "saknas", "visningar": 1, "position": 1.0}])
        self.assertEqual([o["handle"] for o in out], ["saknas", "b", "a"])
        self.assertIn("finns ej", out[0]["status"])

    def test_csv_läsning(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "g.csv")
            with open(p, "w", encoding="utf-8") as f:
                f.write("handle,visningar,position\nx,10,\"5,5\"\n")
            self.assertEqual(ilm.load_gsc(p), [{"handle": "x", "visningar": 10, "position": 5.5}])


if __name__ == "__main__":
    unittest.main(verbosity=1)
