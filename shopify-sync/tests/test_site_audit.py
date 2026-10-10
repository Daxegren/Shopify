import json
from collections import Counter
from datetime import datetime, timedelta, timezone

import pytest
import requests

from site_audit.audit import run_audit, save_local
from site_audit.checks.admin_checks import run_admin_checks
from site_audit.config import GeoProfile, PageGroup, load_sites, site_from_dict
from site_audit.crawler import Crawler
from site_audit.diff import diff_runs
from site_audit.fetch import Fetcher
from site_audit.html_parse import page_type, split_locale
from site_audit.impact import compare, ga4_window_sql, gsc_window_sql, shopify_window_sql, trend_sql
from site_audit.report import headline_bullets, to_html, to_markdown
from site_audit.shopify_admin import AdminData, _bulk_tree
from site_audit.textutil import find_misspellings, guess_language, osa_distance
from site_fixture.server import start


@pytest.fixture(scope="module")
def fixture_site():
    server, base = start()
    yield base
    server.shutdown()


def make_site(base, **kw):
    site = site_from_dict({
        "name": "test", "base_url": base, "brand_terms": ["Mankovsky"], "primary_locale": "sv",
        "geo_profiles": [{"name": "Sverige", "accept_language": "sv-SE,sv;q=0.9"}],
        "crawl": {"requests_per_second": 0, "concurrency": 4, "max_link_depth": 1, "exclude_patterns": []},
        **kw,
    })
    return site


def fetcher():
    s = requests.Session()
    s.trust_env = False  # förbi proxy för lokal testserver
    return Fetcher("test", 0, 5, session=s)


@pytest.fixture(scope="module")
def crawl_run(fixture_site):
    site = make_site(fixture_site)
    return run_audit(site, admin=False, crawler=Crawler(site, fetcher()))


def checks(run):
    return Counter(f.check for f in run.findings)


def test_helpers():
    assert split_locale("/sv/products/x") == ("sv", "/products/x")
    assert split_locale("/en-ca") == ("en-ca", "/")
    assert split_locale("/products/x") == (None, "/products/x")
    assert page_type("/de/collections/a/products/b") == "product"
    assert page_type("/blogs/news/post") == "article"
    assert osa_distance("mankosvky", "mankovsky") == 1
    assert "mankosvky" in find_misspellings("Tavla av Mankosvky och Mankovsky", ["Mankovsky"])
    assert "mankovsky" not in find_misspellings("Mankovsky", ["Mankovsky"])
    assert guess_language("det är en text och det som är för oss med att vi har den inte så") [0] == "sv"
    assert guess_language("the art and the artists that we have for you in this gallery with our work") [0] == "en"


def test_crawl_finds_expected_problems(crawl_run):
    c = checks(crawl_run)
    by = {}
    for f in crawl_run.findings:
        by.setdefault(f.check, []).append(f)
    # Sitemap-URL som ger 404
    assert any(f.url.endswith("/collections/artist-gone") for f in by["sitemap_url_error"])
    # Omdirigeringskedja som slutar i 404
    assert any(f.url.endswith("/old") for f in by["redirect_to_error"])
    assert any("2 hopp" in f.message for f in by["redirect_to_error"] if f.url.endswith("/old"))
    # En kedja som slutar i fel räknas en gång, inte också som kedja
    assert not any(f.url.endswith("/old") for f in by.get("redirect_chain", []))
    assert any(f.url.endswith("/chain-ok") for f in by["redirect_chain"])
    # Mål utan domän ('//collections/...') är ett eget kritiskt fel, inte ett nätverksfel
    assert any(f.url.endswith("/bad-target") for f in by["redirect_invalid_target"])
    assert not any(f.url.endswith("/bad-target") for f in by.get("fetch_failed", []))
    # Svensk URL skickas till /en-ca/ med 302
    assert any(f.url.endswith("/sv/products/good") for f in by["redirect_changes_locale"])
    assert c["temporary_redirect"] >= 1
    assert c["geo_redirect"] == 1
    # H1
    assert any(f.url.endswith("/products/bad-schema") for f in by["missing_h1"])
    assert any("6 H1" in f.message for f in by["multiple_h1"])
    # Schema
    assert any(f.url.endswith("/products/bad-schema") for f in by["product_schema_bad_image"])
    assert any(f.url.endswith("/products/bad-schema") for f in by["breadcrumb_schema_missing"])
    # hreflang, språk, prestanda, innehåll
    assert c["hreflang_many_variants"] == 1
    assert any(f.url.endswith("/sv/pages/om-oss") for f in by["language_mismatch"])
    assert any(f.url.rstrip("/") == crawl_run.site.base_url for f in by["large_inline_script"])
    assert any(f.url.endswith("/pages/test-page") for f in by["test_or_draft_page"])
    assert c["duplicate_title"] >= 1
    assert any("mankosvky" in f.message for f in by["brand_misspelling"])
    assert c["images_missing_alt"] >= 1
    # Intern länk till 404
    assert any(f.url.endswith("/collections/gone-link") for f in by["broken_internal_link"])
    # Struktur: /pages/about-us länkas inte från någon sida, /pages/about gör det (från navigeringen)
    orphans = {f.url.rsplit("/", 2)[-2] + "/" + f.url.rsplit("/", 1)[-1] for f in by["orphan_page"]}
    assert "pages/about-us" in orphans and "pages/about" not in orphans
    assert c["inventory"] == 1
    # Felsidan räknas inte som soft 404 eftersom den svarar 404
    assert c["soft_404"] == 0


def test_summary_report_and_local_save(crawl_run, tmp_path):
    s = crawl_run.summary()
    assert s["crawl"]["sitemap_urls"] == 12 and s["crawl"]["errors_4xx"] >= 2
    md = to_markdown(s, crawl_run.findings)
    html = to_html(s, crawl_run.findings)
    assert "## Förbättringar" in md and "<details>" in html
    assert headline_bullets(crawl_run.findings)
    d = save_local(crawl_run, tmp_path)
    rows = [json.loads(l) for l in (d / "pages.jsonl").read_text().splitlines()]
    assert any(r["url"].endswith("/products/good") and r["h1"] == ["Tavla"] for r in rows)


def test_redirect_loop(fixture_site):
    res = fetcher().fetch(fixture_site + "/redir-a")
    assert res.loop and res.error == "omdirigeringsloop"


def admin_fixture():
    now = datetime.now(timezone.utc)
    recent = (now - timedelta(days=5)).isoformat()
    old = (now - timedelta(days=400)).isoformat()

    def prod(i, handle, title, seo=None, alt=None, created=recent, desc="En fin tavla " * 20):
        return {"id": f"gid://shopify/Product/{i}", "handle": handle, "title": title, "status": "ACTIVE", "vendor": "M",
                "productType": "Print", "tags": ["artist-a"], "createdAt": created, "seo": {"title": seo, "description": None},
                "description": desc, "media": {"nodes": [{"id": f"m{i}", "alt": alt, "image": {"url": "x"}}]}}

    products = [
        prod(1, "tavla-1", "Tavla", seo="Mankovsky Gallery | Tavla", alt="Tavla"),
        prod(2, "img_4031-jpg", "Ny tavla", seo="Mankovsky Gallery | Tavla"),
        prod(3, "dsc0012", "Annan", created=old, desc="Konst av Mankosvky " * 10),
    ]
    ids = [{"id": p["id"]} for p in products]

    def col(i, handle, title, count, nodes, rules=None, desc=""):
        return {"id": f"gid://shopify/Collection/{i}", "handle": handle, "title": title, "description": desc,
                "seo": {}, "productsCount": {"count": count}, "products": {"nodes": nodes},
                "ruleSet": {"appliedDisjunctively": False, "rules": rules or []}}

    dup_desc = "Prints av hög kvalitet för ditt hem och kontor i alla storlekar och format " * 2
    collections = [
        col(1, "tom", "Tom", 0, []),
        col(2, "stockholm", "Konst Stockholm", 3, ids, desc=dup_desc),
        col(3, "goteborg", "Konst Göteborg", 3, ids, desc=dup_desc),
        col(4, "fine-art-prints-1", "Fine art prints 1", 3, ids[:1]),
        col(5, "fine-art-prints-2", "Fine art prints 2", 3, ids[1:2]),
        col(6, "fine-art-prints-copy", "Fine art prints (copy)", 3, ids[2:]),
        col(7, "regel", "Regel", 0, [], rules=[{"column": "TAG", "relation": "EQUALS", "condition": "finns-inte"}]),
    ]
    pages = [
        {"id": "gid://shopify/Page/1", "handle": "about", "title": "Om oss", "body": "<p>" + "text " * 200 + "</p>", "isPublished": True},
        {"id": "gid://shopify/Page/2", "handle": "about-us", "title": "About us", "body": "<p>" + "text " * 200 + "</p>", "isPublished": True},
        {"id": "gid://shopify/Page/3", "handle": "test", "title": "Test", "body": "", "isPublished": True},
        {"id": "gid://shopify/Page/4", "handle": "vernissage-2019", "title": "Vernissage 2019", "body": "kort", "isPublished": True},
        {"id": "gid://shopify/Page/5", "handle": "avada-sitemap", "title": "Sitemap", "body": "", "isPublished": True},
    ]
    redirects = [
        {"id": "r1", "path": "/sv/collections/x", "target": "/en-ca/collections/x"},
        {"id": "r2", "path": "/a", "target": "/b"},
        {"id": "r3", "path": "/b", "target": "/collections/stockholm"},
        {"id": "r4", "path": "/products/old-thing", "target": "/products/finns-inte"},
        {"id": "r5", "path": "/collections/konstnar-anna-berg", "target": "/collections/konstnar-per-svensson"},
    ]
    locales = [{"locale": "de", "primary": True, "published": True}] + [{"locale": l, "primary": False, "published": True} for l in ["sv", "en", "fr"]]
    return AdminData(shop={"name": "x"}, products=products, collections=collections, pages=pages, redirects=redirects, locales=locales)


def test_admin_checks():
    site = make_site("https://shop.example", primary_locale="sv", expected_locales=["sv", "en"])
    fs = run_admin_checks(admin_fixture(), site)
    c = Counter(f.check for f in fs)
    assert c["empty_collection"] == 2
    assert c["duplicate_collection_products"] == 1
    assert c["duplicate_collection_description"] == 1
    assert c["collection_clones"] == 1
    assert c["collection_rule_suspect"] == 1
    assert c["duplicate_seo_title"] == 1
    assert c["filename_handle"] == 2
    assert c["brand_misspelling"] >= 1
    assert any(f.check == "product_images_no_alt" and f.severity == "medium" for f in fs)
    assert c["duplicate_role_page"] == 1
    assert c["test_page_published"] == 1
    assert c["outdated_page"] == 1
    assert c["app_generated_page"] == 1
    assert c["redirect_table_locale"] == 1
    assert c["redirect_table_chain"] == 1
    missing = {f.resource for f in fs if f.check == "redirect_target_missing"}
    assert {"r1", "r4", "r5"} == missing  # mål som inte finns i admin
    assert c["primary_locale_unexpected"] == 1
    assert c["unexpected_locales"] == 1


def test_cross_checks():
    from site_audit.checks.cross_checks import check_redirect_targets

    class CR:
        urls = {}

    fs = check_redirect_targets(CR(), admin_fixture(), make_site("https://shop.example"))
    assert any(f.check == "redirect_target_mismatch" and f.url.endswith("konstnar-anna-berg") for f in fs)


def test_bulk_tree():
    class Client:
        def run_bulk(self, q, p, t):
            rows = [{"id": "gid://shopify/Collection/1", "handle": "a"},
                    {"id": "gid://shopify/Product/9", "__parentId": "gid://shopify/Collection/1"},
                    {"id": "gid://shopify/Collection/2", "handle": "b"}]
            return {}, iter(rows)

    tree = _bulk_tree(Client(), "", "products", 0, 1)
    assert [c["handle"] for c in tree] == ["a", "b"]
    assert tree[0]["products"]["nodes"] == [{"id": "gid://shopify/Product/9"}]
    assert tree[1]["products"]["nodes"] == []


def test_impact_compare_and_sql():
    rows = [
        {"in_group": True, "period": "before", "clicks": 100}, {"in_group": True, "period": "after", "clicks": 150},
        {"in_group": False, "period": "before", "clicks": 1000}, {"in_group": False, "period": "after", "clicks": 1100},
    ]
    r = compare(rows, ["clicks"])["clicks"]
    assert r["change_pct"] == 50 and round(r["rest_of_site_pct"]) == 10 and round(r["net_pct_points"]) == 40
    for sql in (gsc_window_sql("p.sc.t"), ga4_window_sql("p.analytics_1"), shopify_window_sql("p.shopify"),
                trend_sql("p.sc.t", [("konstnarer", "^/collections/konstnar")])):
        assert "@" in sql or "since" in sql
    assert "konstnarer" in trend_sql("p.sc.t", [("konstnarer", "^/collections/konstnar")])


def test_diff():
    old = [{"check": "a", "url": "1"}, {"check": "a", "url": "2"}, {"check": "b", "url": "3"}]
    new = [{"check": "a", "url": "1"}, {"check": "c", "url": "4"}]
    d = diff_runs(old, new)
    assert len(d["resolved"]) == 2 and len(d["added"]) == 1
    assert d["per_check"]["a"]["delta"] == -1


def test_load_example_config():
    from pathlib import Path

    sites = load_sites(Path(__file__).parents[1] / "sites.example.toml")
    assert "gorillasports-se" in sites
    s = sites["gorillasports-se"]
    assert s.crawl.max_pages > 0 and s.page_groups


def test_data_checks(crawl_run):
    from site_audit.checks.data_checks import SearchData, run_data_checks

    sd = SearchData(days=90, by_path={
        "/collections/artist-gone": {"clicks": 40, "impressions": 900, "position": 8.0},
        "/products/good": {"clicks": 5, "impressions": 2000, "position": 4.0},
        "/sv/products/good": {"clicks": 12, "impressions": 300, "position": 9.0},
    }, cannibal=[{"query": "tavla", "impressions": 500, "urls": [{"path": "/products/good"}, {"path": "/collections/artists"}]}])
    c = Counter(f.check for f in run_data_checks(crawl_run.crawl, sd, crawl_run.site))
    assert c["traffic_page_broken"] == 1
    assert c["traffic_page_redirected"] == 1
    assert c["low_ctr_top10"] == 1
    assert c["keyword_cannibalization"] == 1
    assert c["no_search_impressions"] >= 3 and c["no_impressions_summary"] == 1


def test_robots_parser():
    from site_audit.checks.crawl_checks import blocks_all

    shopify_default = "User-agent: *\nDisallow: /admin\nDisallow: /cart\n\nUser-agent: Nutch\nDisallow: /\n"
    assert not blocks_all(shopify_default, ("*", "googlebot"))
    assert blocks_all("User-agent: *\nDisallow: /\n", ("*",))
    assert blocks_all("User-agent: Bingbot\nUser-agent: Googlebot\nDisallow: /\n", ("googlebot",))


def test_translation_coverage_and_check():
    from site_audit.shopify_admin import translation_coverage

    class Client:
        def graphql(self, q, v):
            nodes = [
                {"resourceId": "1", "translatableContent": [{"key": "title", "value": "A"}, {"key": "body_html", "value": "B"}],
                 "translations": [{"key": "title", "value": "a", "outdated": False}, {"key": "body_html", "value": "b", "outdated": True}]},
                {"resourceId": "2", "translatableContent": [{"key": "title", "value": "A"}, {"key": "body_html", "value": "B"}],
                 "translations": [{"key": "title", "value": "a", "outdated": False}]},
                {"resourceId": "3", "translatableContent": [{"key": "title", "value": "A"}], "translations": []},
            ]
            return {"translatableResources": {"nodes": nodes, "pageInfo": {"hasNextPage": False, "endCursor": None}}}

    cov = translation_coverage(Client(), ["en"])
    st = cov["en"]["PRODUCT"]
    assert st == {"resources": 3, "title_translated": 2, "fully_translated": 1, "outdated": 1}
    admin = AdminData(translations=cov)
    fs = run_admin_checks(admin, make_site("https://shop.example"))
    assert any(f.check == "partial_translation" and f.severity == "high" for f in fs)
    assert any(f.check == "outdated_translation" for f in fs)


def test_actions_and_redirect_import(crawl_run, tmp_path):
    import csv

    from site_audit.actions import build_actions, suggest_target, write_action_files

    assert suggest_target("/collections/artist-anna-berg", ["/collections/artist-anna", "/pages/about"])[0] == "/collections/artist-anna"
    assert suggest_target("/sv/pages/x", ["/pages/x"])[0] == "/sv"  # aldrig över språkgräns
    actions, pairs = build_actions(crawl_run.findings, crawl_run.crawl)
    srcs = dict(pairs)
    assert "/collections/artist-gone" in srcs and "/old" in srcs
    assert all(s != t for s, t in pairs)
    assert actions[0].priority >= actions[-1].priority
    a, r = write_action_files(crawl_run.findings, crawl_run.crawl, tmp_path)
    rows = list(csv.reader(open(r)))
    assert rows[0] == ["Redirect from", "Redirect to"] and len(rows) > 1


def test_google_api_parsers():
    from datetime import date

    from site_audit import google_api as g

    class Resp:
        def __init__(self, data, code=200):
            self.data, self.status_code, self.text = data, code, ""

        def json(self):
            return self.data

    class GscSession:
        def __init__(self):
            self.calls = []

        def post(self, url, json, timeout):
            self.calls.append((url, json))
            return Resp({"rows": [{"keys": [json["startDate"], "https://x.se/a"], "clicks": 3, "impressions": 10, "position": 2.5}]})

    s = GscSession()
    rows = list(g.gsc_rows(s, "sc-domain:x.se", date(2026, 1, 1), date(2026, 1, 2)))
    assert len(rows) == 2 and rows[0]["sum_position"] == 15.0 and rows[0]["data_date"] == "2026-01-01"
    assert "sc-domain%3Ax.se" in s.calls[0][0]

    class Ga4Session:
        def post(self, url, json, timeout):
            return Resp({"rowCount": 1, "rows": [{"dimensionValues": [{"value": "20260105"}, {"value": "www.X.se"}, {"value": "/collections/a"}],
                                                   "metricValues": [{"value": "12"}, {"value": "2"}, {"value": "1999.5"}]}]})

    r = list(g.ga4_rows(Ga4Session(), "123", date(2026, 1, 1), date(2026, 1, 31)))
    assert r == [{"d": "2026-01-05", "property_id": "123", "hostname": "www.x.se", "landing": "/collections/a",
                  "sessions": 12, "purchases": 2, "revenue": 1999.5}]
    assert "@pattern" in g.ga4_api_window_sql("p.d.t") and "@host" in g.ga4_api_window_sql("p.d.t")
    assert "@currency" in shopify_window_sql("p.shopify") and "@host" in ga4_window_sql("p.analytics_1")


def test_psi(crawl_run):
    from site_audit.psi import findings_from_psi, sample_urls

    urls = sample_urls(crawl_run.crawl, 1)
    assert urls[0].rstrip("/") == crawl_run.site.base_url and len(urls) >= 3
    data = {"loadingExperience": {"metrics": {
        "LARGEST_CONTENTFUL_PAINT_MS": {"percentile": 4800, "category": "SLOW"},
        "CUMULATIVE_LAYOUT_SHIFT_SCORE": {"percentile": 15, "category": "AVERAGE"},
        "INTERACTION_TO_NEXT_PAINT": {"percentile": 120, "category": "FAST"}}},
        "lighthouseResult": {"categories": {"performance": {"score": 0.31}}, "audits": {
            "unused-javascript": {"title": "Reduce unused JavaScript", "numericValue": 1200, "details": {"type": "opportunity"}}}}}
    fs = {f.check: f for f in findings_from_psi("https://x/", data)}
    assert fs["cwv_lcp"].severity == "high" and fs["cwv_cls"].severity == "medium" and "cwv_inp" not in fs
    assert fs["lighthouse_performance"].evidence["top_opportunities"] == ["Reduce unused JavaScript"]


def test_interleave_and_truncation(fixture_site):
    from site_audit.crawler import interleave_by_sitemap

    site = make_site(fixture_site)
    site.crawl.max_pages = 4
    site.crawl.follow_internal_links = False
    run = run_audit(site, admin=False, crawler=Crawler(site, fetcher()))
    sitemaps = {cu.sitemap for cu in run.crawl.urls.values() if cu.in_sitemap}
    assert len(sitemaps) == 2  # båda sitemaps representerade trots gränsen
    assert any(f.check == "crawl_truncated" for f in run.findings)
    order = interleave_by_sitemap(run.crawl.sitemap)
    assert "products" in order[0] and "pages" in order[1]


def test_merge_keeps_page_with_most_clicks():
    from site_audit.actions import build_actions
    from site_audit.findings import Finding

    f = Finding("duplicate_collection_products", "high", "content", "dubbletter", url="https://x/collections/a",
                evidence={"collections": ["a", "b", "c"]})
    _, pairs = build_actions([f], None, clicks={"/collections/b": 50, "/collections/a": 3})
    assert dict(pairs) == {"/collections/a": "/collections/b", "/collections/c": "/collections/b"}


def test_review_fixes():
    from site_audit.audit import reconcile_redirect_targets
    from site_audit.crawler import normalize_url
    from site_audit.findings import Finding
    from site_audit.html_parse import parse_page

    # Spårningsparametrar tas bort
    assert normalize_url("https://x.se/products/a?pr_prod_strat=e5&pr_rec_id=1&shpxid=2&color=red") == "https://x.se/products/a?color=red"
    # Protokollrelativ bild är inte trasig
    html = b"<html><head><script type='application/ld+json'>{\"@type\":\"Product\",\"image\":\"//www.x.se/cdn/a.jpg\",\"offers\":{}}</script></head><body></body></html>"
    p = parse_page("https://www.x.se/products/a", html, "www.x.se").product_schema[0]
    assert p["invalid_images"] == [] and p["relative_images"] == ["//www.x.se/cdn/a.jpg"]

    class CU:
        def __init__(self, status):
            self.status = status

    class CR:
        urls = {"https://x.se/a": CU(200), "https://x.se/b": CU(404), "https://x.se/c": CU(0)}

    fs = [Finding("redirect_target_missing", "critical", "redirects", "m", url=u) for u in ("https://x.se/a", "https://x.se/b", "https://x.se/c")]
    out = {f.url: f for f in reconcile_redirect_targets(fs, CR())}
    assert "https://x.se/a" not in out
    assert out["https://x.se/b"].severity == "critical" and out["https://x.se/c"].check == "redirect_target_unverified"


def test_second_review_fixes():
    from site_audit.checks.admin_checks import check_redirect_table
    from site_audit.crawler import CrawledUrl
    from site_audit.fetch import FetchResult, Hop
    from site_audit.shopify_admin import AdminData

    site = make_site("https://www.x.se")
    cr = Crawler(site, fetcher())
    # Kundkonto och kassa crawlas inte
    assert not cr.allowed("https://www.x.se/customer_authentication/redirect?locale=sv")
    assert not cr.allowed("https://www.x.se/en/account/login")
    assert cr.allowed("https://www.x.se/collections/accounting-books")

    # Omdirigeringstabellen: mål utan domän och mål med spårningsparametrar
    admin = AdminData(redirects=[
        {"id": "1", "path": "/wall-ball/s/283", "target": "//collections/wall-ball"},
        {"id": "2", "path": "/bumper/p/1", "target": "/products/bumper?pr_prod_strat=e5&pr_rec_id=1&color=red"},
    ])
    by = {f.check: f for f in check_redirect_table(admin, site)}
    assert by["redirect_invalid_target"].url.endswith("/wall-ball/s/283")
    assert by["redirect_target_tracking_params"].evidence["clean_target"] == "/products/bumper?color=red"

    # Om-hämtning efter 429: lyckas den andra gången ersätts resultatet
    class FlakyFetcher:
        def __init__(self):
            self.calls = 0
            self.limiter = None

        def fetch(self, url, **kw):
            self.calls += 1
            if self.calls == 1:
                return FetchResult(url, url, 0, [Hop(url, 0)], error="429 Too Many Requests (Shopify bromsar)")
            return FetchResult(url, url, 200, [Hop(url, 200)], headers={"content-type": "text/plain"})

    c = Crawler(site, FlakyFetcher())
    c.retry_cooldown_s = 0
    first = c._crawl_one("https://www.x.se/a", "sitemap", 0)
    first.in_sitemap = True
    results = {first.url: first}
    c._retry_failed(results)
    assert results[first.url].status == 200 and results[first.url].in_sitemap
