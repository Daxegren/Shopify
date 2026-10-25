"""Tester för fördjupade kontroller (T16, T17, T19): sidfakta, kontroller och sammanfattningar."""
from site_audit.checks.seo_depth_checks import (check_faceted_urls, check_image_practices, check_pagination,
                                                check_thin_collections, check_third_party_scripts, check_tracking_in_html)
from site_audit.config import site_from_dict
from site_audit.crawler import CrawledUrl, CrawlResult
from site_audit.html_parse import PageFacts, detect_tracking, page_type, parse_page
from site_audit.sitemap import SitemapResult

SITE = site_from_dict({"name": "t", "base_url": "https://www.t.se"})


def cu(url, facts=None, status=200, in_sitemap=True):
    return CrawledUrl(url=url, source="sitemap", depth=0, status=status, final_url=url, hops=[], error=None, loop=False,
                      elapsed_ms=1, content_type="text/html", x_robots_tag=None, in_sitemap=in_sitemap, facts=facts)


def facts(url, **kw):
    path = url.split("t.se", 1)[1].split("?")[0] or "/"
    f = PageFacts(url=url, path=path, locale_prefix=None, page_type=page_type(path))
    for k, v in kw.items():
        setattr(f, k, v)
    return f


def crawl(*urls):
    return CrawlResult(site="t", started_at="2026-10-23T00:00:00Z", finished_at=None,
                       sitemap=SitemapResult([], [], []), urls={u.url: u for u in urls}, geo=[])


def test_parse_page_new_facts():
    html = b"""<html lang="sv"><head><title>T</title>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-ABC123XYZ9"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}
    gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied'});
    fbq('init', '1234567890123456');</script>
    <script src="https://consent.cookiebot.com/uc.js"></script>
    <script type="application/ld+json">{"@type":"Product","name":"P","offers":[{"priceCurrency":"sek","price":"1"},{"priceCurrency":"DKK","price":"2"}]}</script>
    </head><body>
    <img src="a.jpg" width="10" height="10"><img src="b.jpg"><img src="c.jpg" loading="lazy"><img src="d.jpg"><img src="e.jpg" loading="lazy" width="1" height="1">
    <a href="/products/p1">1</a><a href="/collections/x/products/p1">1b</a><a href="/products/p2?variant=1">2</a><a href="/pages/om">om</a>
    </body></html>"""
    f = parse_page("https://www.t.se/collections/x", html, "www.t.se")
    assert f.images_total == 5 and f.images_no_dimensions == 3
    assert f.images_no_lazy == 1  # bara d.jpg: efter de två första och utan lazy
    assert f.product_link_count == 2  # p1 (två adresser) och p2
    assert f.consent_platforms == ["cookiebot"]
    assert f.analytics_ids == ["FB-1234567890123456", "G-ABC123XYZ9"]
    assert f.consent_mode_default and f.consent_mode_v2
    assert f.product_schema[0]["currencies"] == ["DKK", "SEK"]


def test_detect_tracking_incomplete_consent_mode():
    cmps, ids, default, v2 = detect_tracking("gtag('consent', 'default', {ad_storage:'denied'}); GTM-ABCD12 AW-123456789")
    assert default and not v2 and ids == ["AW-123456789", "GTM-ABCD12"] and cmps == []


def test_faceted_and_pagination():
    base = "https://www.t.se/collections/a"
    pages = [
        cu(base, facts(base, canonical=base)),
        cu(base + "?filter.v.price.gte=100", facts(base + "?filter.v.price.gte=100", canonical=base + "?filter.v.price.gte=100")),  # kan indexeras
        cu(base + "?sort_by=price-ascending", facts(base + "?sort_by=price-ascending", canonical=base)),  # canonical till grundsidan: ok
        cu(base + "?page=2", facts(base + "?page=2", canonical=base)),  # canonical till sida 1
        cu(base + "?page=3", facts(base + "?page=3", canonical=base + "?page=3")),  # ok
    ]
    cr = crawl(*pages)
    faceted = check_faceted_urls(cr, SITE)
    assert [f.check for f in faceted] == ["faceted_url_indexable"] and faceted[0].evidence["count"] == 1
    pag = check_pagination(cr, SITE)
    assert [f.check for f in pag] == ["paginated_canonical_to_first"] and pag[0].evidence["count"] == 1


def test_thin_collections():
    empty, few, ok, noindex = ("https://www.t.se/collections/" + n for n in ("tom", "fa", "bra", "noindex"))
    cr = crawl(cu(empty, facts(empty, canonical=empty, product_link_count=0)),
               cu(few, facts(few, canonical=few, product_link_count=2)),
               cu(ok, facts(ok, canonical=ok, product_link_count=24)),
               cu(noindex, facts(noindex, meta_robots="noindex", product_link_count=0)))
    out = {f.url: f for f in check_thin_collections(cr, SITE)}
    assert set(out) == {empty, few}
    assert out[empty].severity == "medium" and out[few].severity == "low"


def test_third_party_scripts_and_images():
    urls = []
    hosts = [f"h{i}.example" for i in range(13)]
    for i in range(5):
        u = f"https://www.t.se/products/p{i}"
        urls.append(cu(u, facts(u, external_script_hosts=hosts, images_total=10, images_no_dimensions=8, images_no_lazy=12)))
    for i in range(3):
        u = f"https://www.t.se/collections/c{i}"
        urls.append(cu(u, facts(u, external_script_hosts=["a.example"], images_total=30, images_no_dimensions=1, images_no_lazy=2)))
    cr = crawl(*urls)
    tp = {f.evidence["page_type"]: f for f in check_third_party_scripts(cr, SITE)}
    assert tp["product"].severity == "medium" and tp["collection"].severity == "info"
    assert tp["product"].evidence["top_hosts_pct_of_pages"][0][1] == 100
    img = {f.check: f for f in check_image_practices(cr, SITE)}
    assert img["images_without_dimensions"].evidence["page_type"] == "product"
    assert "images_not_lazy" in img  # 12 per produktsida


def test_tracking_in_html():
    pages = []
    for p in ("/", "/collections/a", "/products/b"):
        u = "https://www.t.se" + p
        pages.append(cu(u, facts(u, consent_mode_default=True, consent_mode_v2=False,
                                 analytics_ids=["G-AAAAAA1111", "G-BBBBBB2222"])))
    out = {f.check for f in check_tracking_in_html(crawl(*pages), SITE)}
    assert out == {"consent_platform_not_in_html", "consent_mode_v2_incomplete", "multiple_ga4_ids"}
    assert check_tracking_in_html(crawl(pages[0]), SITE) == []  # för få sidor för slutsats


# ---- T18 flera domäner -------------------------------------------------------------------------------------------
from site_audit.crossdomain import collect_pages, common_paths, compare_domains, evenly  # noqa: E402
from site_audit.fetch import FetchResult  # noqa: E402

SE = site_from_dict({"name": "se", "base_url": "https://www.b.se", "primary_locale": "sv", "shopify_currency": "SEK"})
DK = site_from_dict({"name": "dk", "base_url": "https://www.b.dk", "primary_locale": "da", "shopify_currency": "DKK"})
SITES = {"se": SE, "dk": DK}


def pf(url, **kw):
    path = "/" + url.split("/", 3)[3] if url.count("/") >= 3 else "/"
    f = PageFacts(url=url, path=path, locale_prefix=None, page_type=page_type(path))
    for k, v in kw.items():
        setattr(f, k, v)
    return f


def test_evenly_and_common_paths():
    assert evenly(["c", "a", "b", "d"], 2) == ["a", "c"]
    assert evenly(["a"], 5) == ["a"]
    paths = {"se": {"collection": ["/collections/a", "/collections/b"], "product": ["/products/x"]},
             "dk": {"collection": ["/collections/b", "/collections/c"], "product": ["/products/y"]}}
    assert common_paths(paths, 10) == ["/collections/b"]


def test_compare_domains_findings():
    pages = {
        "se": {"/": pf("https://www.b.se/", title="Hem", text_fingerprint="aa", hreflang={"da": "https://www.b.dk/"}),
               "/products/x": pf("https://www.b.se/products/x", title="Cykel", text_fingerprint="bb",
                                 product_schema=[{"currencies": ["SEK"]}])},
        "dk": {"/": pf("https://www.b.dk/", title="Hem", text_fingerprint="aa", hreflang={}, canonical="https://www.b.se/"),
               "/products/x": pf("https://www.b.dk/products/x", title="Cykel", text_fingerprint="bb",
                                 product_schema=[{"currencies": ["SEK"]}])},
    }
    found = {f.check: f for f in compare_domains(pages, SITES)}
    assert found["cross_domain_untranslated"].severity == "high"       # båda sidorna oöversatta
    assert found["canonical_to_sibling_domain"].evidence["count"] == 1
    assert found["schema_currency_mismatch"].message.startswith("dk:")  # DKK förväntas men SEK i schemat
    assert "hreflang_not_reciprocal" in found                           # se pekar på dk, dk pekar inte tillbaka
    assert "hreflang_missing_between_domains" in found                  # dk har inga hreflang alls


def test_compare_domains_clean_translation():
    pages = {
        "se": {"/": pf("https://www.b.se/", title="Hem", text_fingerprint="aa", hreflang={"da": "https://www.b.dk/"},
                       canonical="https://www.b.se/")},
        "dk": {"/": pf("https://www.b.dk/", title="Hjem", text_fingerprint="zz", hreflang={"sv": "https://www.b.se/"},
                       canonical="https://www.b.dk/")},
    }
    assert compare_domains(pages, SITES) == []


class FakeFetcher:
    """Låtsasbutiker med varsin sitemap och några sidor."""

    def __init__(self):
        self.pages = {}
        for host, lang in (("www.b.se", "sv"), ("www.b.dk", "da")):
            self.pages[f"https://{host}/sitemap.xml"] = (
                "<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>"
                f"<url><loc>https://{host}/collections/a</loc></url><url><loc>https://{host}/products/p</loc></url>"
                f"<url><loc>https://{host}/products/only-{lang}</loc></url></urlset>", "application/xml")
            for path in ("/", "/collections/a", "/products/p"):
                self.pages[f"https://{host}{path}"] = (f"<html lang='{lang}'><head><title>{lang} {path}</title></head><body>"
                                                      "<h1>x</h1></body></html>", "text/html")
        self.requested = []

    def fetch(self, url, **kw):
        self.requested.append(url)
        if url in self.pages:
            body, ctype = self.pages[url]
            return FetchResult(requested_url=url, final_url=url, status=200, headers={"content-type": ctype}, body=body.encode())
        return FetchResult(requested_url=url, final_url=url, status=404, headers={"content-type": "text/html"}, body=b"")


def test_collect_pages_uses_only_common_paths():
    ff = FakeFetcher()
    pages, notes = collect_pages(SITES, ff, per_type=5)
    assert set(pages["se"]) == {"/", "/collections/a", "/products/p"} == set(pages["dk"])
    assert not any("only-" in u for u in ff.requested)
    assert notes == []


# ---- T17 URL-inspektion ------------------------------------------------------------------------------------------
from site_audit.inspection import findings_from_rows, inspect_url, run_inspection, sample_urls, summarize  # noqa: E402


class FakeSession:
    def __init__(self, answers):
        self.answers = answers
        self.calls = []

    def post(self, url, json=None, timeout=None):
        self.calls.append(json)

        class R:
            status_code = 200

            def __init__(s, body):
                s._b = body
                s.text = str(body)

            def json(s):
                return s._b

        a = self.answers.get(json["inspectionUrl"])
        if a is None:
            r = R({}); r.status_code = 403; r.text = "no access"; return r
        return R({"inspectionResult": {"indexStatusResult": a}})


def test_url_inspection_summary_and_findings():
    ok = {"verdict": "PASS", "coverageState": "Submitted and indexed", "googleCanonical": "https://s.se/products/a",
          "userCanonical": "https://s.se/products/a"}
    notidx = {"verdict": "NEUTRAL", "coverageState": "Discovered - currently not indexed"}
    other = {"verdict": "PASS", "coverageState": "Indexed", "googleCanonical": "https://s.se/products/z",
             "userCanonical": "https://s.se/products/b"}
    urls = ["https://s.se/", "https://s.se/products/a", "https://s.se/products/b", "https://s.se/products/c", "https://s.se/collections/x"]
    sess = FakeSession({urls[0]: ok, urls[1]: ok, urls[2]: other, urls[3]: notidx})  # sista saknar svar: fel
    rows = run_inspection(sess, "sc-domain:s.se", urls, sleep_s=0)
    assert rows[1]["page_type"] == "product" and rows[0]["page_type"] == "home"
    assert sess.calls[0] == {"inspectionUrl": urls[0], "siteUrl": "sc-domain:s.se", "languageCode": "sv-SE"}
    summ = summarize(rows)
    assert summ["total"] == 5 and summ["indexed"] == 3
    found = {f.check: f for f in findings_from_rows(rows, "https://s.se")}
    assert found["sitemap_urls_not_indexed"].evidence["by_state"] == {"Discovered - currently not indexed": 1}
    assert found["google_chose_other_canonical"].evidence["count"] == 1
    assert found["inspection_errors"].severity == "info"


def test_sample_urls_even_per_type():
    urls = ["https://s.se/"] + [f"https://s.se/products/p{i:02d}" for i in range(10)] + [f"https://s.se/collections/c{i}" for i in range(3)]
    sample = sample_urls(urls, 4)
    assert sample.count("https://s.se/") == 1
    assert len([u for u in sample if "/products/" in u]) == 4 and len([u for u in sample if "/collections/" in u]) == 3
    assert inspect_url  # importerbar


# ---- T16 CrUX-historik -------------------------------------------------------------------------------------------
from site_audit import crux  # noqa: E402


def _crux_response(lcp, cls):
    periods = [{"lastDate": {"year": 2026, "month": 10, "day": 1 + i}} for i in range(len(lcp))]
    return {"record": {"collectionPeriods": periods, "metrics": {
        "largest_contentful_paint": {"percentilesTimeseries": {"p75s": lcp}},
        "cumulative_layout_shift": {"percentilesTimeseries": {"p75s": cls}}}}}


def test_crux_series_trend_and_report():
    lcp = [2000] * 8 + [3000] * 4                   # försämring efter 8 veckor
    cls = ["0.05"] * 11 + [None]                    # CLS kommer som text, en vecka saknas
    series = crux.weekly_series(_crux_response(lcp, cls))
    assert series["LCP"][0] == ("2026-10-01", 2000.0) and series["CLS"][0][1] == 0.05 and series["CLS"][-1][1] is None
    assert crux.trend(series["LCP"]) == {"enough_data": True, "recent_avg": 3000.0, "earlier_avg": 2000.0,
                                         "change_pct": 50.0, "direction": "sämre"}
    assert crux.trend(series["CLS"])["direction"] == "oförändrat"
    assert crux.verdict("LCP", 3000) == "behöver förbättras" and crux.verdict("LCP", 5000) == "dålig" and crux.verdict("CLS", 0.05) == "bra"
    text = crux.report("https://s.se", "PHONE", series)
    assert "| LCP | 3000 ms | behöver förbättras | sämre (+50 %) |" in text
    assert crux.trend([("a", 1.0)] * 3) == {"enough_data": False}


def test_crux_key_is_required(monkeypatch):
    monkeypatch.delenv("CRUX_API_KEY", raising=False)
    monkeypatch.delenv("PSI_API_KEY", raising=False)
    import pytest as _pytest

    with _pytest.raises(RuntimeError):
        crux.key_from_env()
    monkeypatch.setenv("PSI_API_KEY", "x")
    assert crux.key_from_env() == "x"


# ---- T19 webbläsarskript (ren logik) ----------------------------------------------------------------------------
import importlib.util  # noqa: E402
from pathlib import Path  # noqa: E402


def _script(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).resolve().parents[1] / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_samtycke_classify_and_verdicts():
    st = _script("samtycke_test")
    urls = ["https://www.google-analytics.com/g/collect?v=2&tid=G-AB&en=page_view&gcs=G100",
            "https://www.googletagmanager.com/gtag/js?id=G-AB", "https://cdn.shopify.com/x.js", "https://x.test/cookie-pixel?a=1"]
    rows = st.classify_requests(urls, [r"cookie-pixel"])
    assert [r["gcs"] for r in rows] == ["G100", "", ""] and rows[0]["event"] == "page_view" and rows[0]["tid"] == "G-AB"
    # Consent Mode före samtycke (G100) och godkänt efter: inga problem
    good = st.verdicts([rows[0]], [{"gcs": "G111", "host": "h", "url": "u/g/collect"}], True, True)
    assert not any(v.startswith("PROBLEM") for v in good)
    # Bara skript som laddas (inga händelser) före samtycke är normalt och ger ingen PROBLEM-rad
    script_only = st.classify_requests(["https://www.googletagmanager.com/gtag/js?id=G-AB", "https://scripts.clarity.ms/0.8/clarity.js"])
    assert [r["kind"] for r in script_only] == ["script", "script"]
    v = st.verdicts(script_only, [], True, False)
    assert not any(x.startswith("PROBLEM") for x in v) and any(x.startswith("INFO") for x in v)
    # En Clarity-händelse före samtycke är ett problem
    ev = st.classify_requests(["https://www.clarity.ms/collect"])
    assert ev[0]["kind"] == "event" and any(x.startswith("PROBLEM") for x in st.verdicts(ev, [], False, False))
    assert st.TRACKING_COOKIE.match("_ga_ABC123") and st.TRACKING_COOKIE.match("_clck") and not st.TRACKING_COOKIE.match("cart")
    # Spårning före samtycke utan nekad signal, och ingenting efter godkännande
    bad = st.verdicts([{"gcs": "G111", "host": "h", "url": "u/g/collect", "kind": "event"}], [], True, True)
    assert sum(v.startswith("PROBLEM") for v in bad) == 2
    # Ingen ruta men spårning: observation
    assert any(v.startswith("OBS") for v in st.verdicts([{"gcs": "", "host": "h", "url": "u"}], [], False, False))
    # Efter godkännande fortfarande nekad signal
    assert any("fortfarande nekad" in v for v in st.verdicts([], [{"gcs": "G100", "host": "h", "url": "u"}], True, True))
    assert st.ACCEPT.match("Acceptera alla") and st.REJECT.match("Avvisa alla") and not st.ACCEPT.match("Läs mer")


def test_tillganglighet_summary():
    a11y = _script("tillganglighet_test")
    res = {"startsida": [{"id": "image-alt", "impact": "critical", "help": "h", "nodes": 5},
                         {"id": "color-contrast", "impact": "serious", "help": "h2", "nodes": 3}],
           "produkt": [{"id": "image-alt", "impact": "critical", "help": "h", "nodes": 2}]}
    s = a11y.summarize(res)
    assert s["by_impact"] == {"critical": 7, "serious": 3, "moderate": 0, "minor": 0}
    assert s["rules"][0]["id"] == "image-alt" and s["rules"][0]["pages"] == ["startsida", "produkt"] and s["rules"][0]["nodes"] == 7


def test_deploy_scripts_do_not_split_site_lists_on_commas():
    """gcloud delar --args vid komma. Skriptet som tar SITES=a,b,c måste använda ett annat skiljetecken (^@^), annars
    blir listan flera argument och jobbet misslyckas direkt (hände 2026-10-23)."""
    deploy = Path(__file__).resolve().parents[1] / "deploy"
    text = (deploy / "site_audit_job.sh").read_text(encoding="utf-8")
    line = next(ln for ln in text.splitlines() if ln.startswith('ARGS="'))
    assert line.startswith('ARGS="^@^') and "@--site@${SITES}@" in line
    # Simulera gcloud: efter ^@^ delas strängen på @, och en kommalista ska ligga kvar som ett enda argument
    parts = line[len('ARGS="^@^'):-1].replace("${SITES}", "a,b,c").replace("${BUCKET}", "bkt").split("@")
    assert parts[parts.index("--site") + 1] == "a,b,c"


def test_audit_job_timeout_and_memory_are_configurable():
    """Gorillas nattliga genomlysning nådde tidsgränsen 7200 s varje natt sedan 2026-10-14. Gränsen ska gå att höja per jobb."""
    text = (Path(__file__).resolve().parents[1] / "deploy" / "site_audit_job.sh").read_text(encoding="utf-8")
    assert 'TASK_TIMEOUT="${TASK_TIMEOUT:-7200}"' in text and '--task-timeout "$TASK_TIMEOUT"' in text
    assert '--memory "$MEMORY"' in text


def test_canonical_www_och_apex_ar_samma_domaen():
    """Best of Sports huvudadress är bestofsports.fi (www omdirigerar dit). Canonical till apex får inte flaggas som annan domän."""
    from site_audit.checks.crawl_checks import _bare
    assert _bare("www.bestofsports.fi") == _bare("bestofsports.fi") == "bestofsports.fi"
    assert _bare("bestofsports.se") != _bare("bestofsports.fi")


def test_bos_anvander_huvudadress_utan_www():
    from pathlib import Path
    from site_audit.config import load_sites
    sites = load_sites(Path(__file__).resolve().parents[1] / "sites.toml")
    for n in ("bestofsports-se", "bestofsports-dk", "bestofsports-fi"):
        assert not sites[n].host.startswith("www."), n
        assert sites[n].crawl.max_pages == 8000
    assert sites["gorillasports-se"].host.startswith("www.")


def test_extra_product_nod_fran_omdomesapp_ger_inte_falska_fynd():
    """Produktsidan har temats fullständiga Product-nod plus en omdömesnod utan bild och pris (Best of Sports). Bara en info-notering."""
    from site_audit.checks.crawl_checks import check_schema
    full = {"images": ["https://www.t.se/a.jpg"], "has_offers": True, "has_brand": True, "has_rating": False,
            "relative_images": [], "invalid_images": []}
    review_only = {"images": [], "has_offers": False, "has_brand": False, "has_rating": True,
                   "relative_images": [], "invalid_images": []}
    u1, u2 = "https://www.t.se/products/x", "https://www.t.se/products/y"
    both = cu(u1, facts(u1, product_schema=[full, review_only]))
    only_review = cu(u2, facts(u2, product_schema=[review_only]))
    names = [x.check for x in check_schema(crawl(both), SITE)]
    assert "product_schema_extra_node" in names
    assert "product_schema_no_image" not in names and "product_schema_no_offers" not in names
    names2 = [x.check for x in check_schema(crawl(only_review), SITE)]
    assert "product_schema_no_image" in names2


def test_malformed_href_hittas_och_normala_lankar_ar_ok():
    from site_audit.html_parse import is_malformed_href
    assert is_malformed_href("<span%20class='notranslate'>{{%20shop_url%20}}</span>")
    assert is_malformed_href("{{ link }}")
    assert not is_malformed_href("/collections/yoga?filter.v.price=1&page=2")
    assert not is_malformed_href("https://www.t.se/pages/om-oss")
    html = (b"<html><head><title>T</title></head><body>"
            b"<a href=\"&lt;span%20class='notranslate'&gt;{{%20shop_url%20}}&lt;/span&gt;\">X</a><a href=\"/products/p1\">p</a></body></html>")
    f = parse_page("https://www.t.se/", html, "www.t.se")
    assert len(f.malformed_hrefs) == 1 and "shop_url" in f.malformed_hrefs[0]


def test_check_malformed_hrefs_samlar_per_adress():
    from site_audit.checks.seo_depth_checks import check_malformed_hrefs
    bad = "<span%20class='notranslate'>{{%20shop_url%20}}</span>"
    pages = [cu(f"https://www.t.se/p{i}", facts(f"https://www.t.se/p{i}", malformed_hrefs=[bad])) for i in range(3)]
    out = check_malformed_hrefs(crawl(*pages), SITE)
    assert len(out) == 1 and out[0].check == "malformed_link_href" and out[0].evidence["pages"] == 3


def test_kategorier_byggda_med_js_ger_ett_samlat_fynd():
    urls = [f"https://www.t.se/collections/c{i}" for i in range(12)]
    pages = [cu(u, facts(u, product_link_count=0, h1=[])) for u in urls]
    out = check_thin_collections(crawl(*pages), SITE)
    assert [x.check for x in out] == ["collections_rendered_by_js"]
    # få tomma kategorier bland många fulla: ett fynd per tom kategori som förut
    pages2 = [cu(u, facts(u, product_link_count=20)) for u in urls[:10]] + [cu(u, facts(u, product_link_count=0)) for u in urls[10:]]
    assert {x.check for x in check_thin_collections(crawl(*pages2), SITE)} == {"collection_few_products"}


def test_missing_h1_pa_js_kategori_ar_bara_info():
    from site_audit.checks.crawl_checks import check_onpage
    u = "https://www.t.se/collections/x"
    f = facts(u, product_link_count=0, h1=[], title="T")
    out = [x for x in check_onpage(crawl(cu(u, f)), SITE) if x.check == "missing_h1"]
    assert out and out[0].severity == "info"
    f2 = facts(u, product_link_count=12, h1=[], title="T")
    out2 = [x for x in check_onpage(crawl(cu(u, f2)), SITE) if x.check == "missing_h1"]
    assert out2 and out2[0].severity == "high"


def test_rendera_kategorier_klassning_och_hjalpfunktioner():
    import importlib.util
    spec = importlib.util.spec_from_file_location("rk", Path(__file__).resolve().parents[1] / "scripts" / "rendera_kategorier.py")
    rk = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rk)
    assert rk.classify(10, True, 10, True) == "ok"
    assert rk.classify(0, False, 12, True) == "byggs_med_js"
    assert rk.classify(0, False, 0, False) == "tom"
    assert rk.classify(8, True, 8, False) == "utan_h1"
    assert rk.count_product_links('<a href="/products/a">x</a><a href="/collections/c/products/a?v=1">y</a><a href="/products/b">z</a>') == 2
    assert rk.has_h1("<H1 class='t'>x</H1>") and not rk.has_h1("<h2>x</h2>")
    assert rk.parse_locs("<loc> https://t.se/collections/a </loc><loc>https://t.se/collections/b</loc>") == ["https://t.se/collections/a", "https://t.se/collections/b"]


def test_rendera_kategorier_ignorerar_text_i_script():
    import importlib.util
    spec = importlib.util.spec_from_file_location("rk2", Path(__file__).resolve().parents[1] / "scripts" / "rendera_kategorier.py")
    rk = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rk)
    html = "<script>x='<a href=\"/products/fel\">'; y='<h1>'</script><a href='/products/ratt?v=1'>a</a>"
    assert rk.count_product_links(html) == 1 and not rk.has_h1(html)


def test_redirect_jamforelse_skiljer_granskade_fran_nya():
    import importlib.util
    spec = importlib.util.spec_from_file_location("rj", Path(__file__).resolve().parents[1] / "scripts" / "redirect_jamforelse.py")
    rj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rj)
    findings = [
        {"check": "redirect_target_missing", "url": "https://www.gorillasports.se/boksepakke-profi-27kg/p/1129", "evidence": {"target": "/products/boksepakke-profi-27kg"}},
        {"check": "redirect_to_error", "url": "https://www.gorillasports.se/blogs/blogg/ny-sida", "evidence": {"chain": ["a", "https://www.gorillasports.se/blogs"]}},
        {"check": "missing_h1", "url": "https://www.gorillasports.se/pages/x"},
    ]
    covered, new = rj.classify(findings, {"/boksepakke-profi-27kg/p/1129": "/collections/boxningspaket"})
    assert [c["kalla"] for c in covered] == ["/boksepakke-profi-27kg/p/1129"]
    assert [n["kalla"] for n in new] == ["/blogs/blogg/ny-sida"]
