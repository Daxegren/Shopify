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
    class Ga4ChannelSession:
        def post(self, url, json, timeout):
            assert [d["name"] for d in json["dimensions"]][2] == "sessionDefaultChannelGroup"
            return Resp({"rowCount": 1, "rows": [{"dimensionValues": [{"value": "20260105"}, {"value": "www.X.se"},
                                                                     {"value": "Paid Search"}, {"value": "google / cpc"},
                                                                     {"value": "Shopping SE"}],
                                                   "metricValues": [{"value": "40"}, {"value": "1"}, {"value": "899"}]}]})

    r = list(g.ga4_channel_rows(Ga4ChannelSession(), "123", date(2026, 1, 1), date(2026, 1, 31)))
    assert r == [{"d": "2026-01-05", "property_id": "123", "hostname": "www.x.se", "channel": "Paid Search",
                  "source_medium": "google / cpc", "campaign": "Shopping SE", "sessions": 40, "purchases": 1, "revenue": 899.0}]
    assert [n for n, _, _ in g.GA4_CHANNEL_SCHEMA] == list(r[0])
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
        {"id": "2", "path": "/bumper/p/1", "target": "/products/bumper?pr_prod_strat=e5&pr_rec_id=1&_psid=x&variant=7"},
        {"id": "3", "path": "/curl/p/2", "target": "https://www.x.dk/products/curl?_pos=32&shpxid=1"},
    ])
    by = {}
    for f in check_redirect_table(admin, site):
        by.setdefault(f.check, f)
    assert by["redirect_invalid_target"].url.endswith("/wall-ball/s/283")
    # variant= behålls, spårning tas bort
    assert by["redirect_target_tracking_params"].evidence["clean_target"] == "/products/bumper?variant=7"
    assert by["redirect_table_other_domain"].url.endswith("/curl/p/2")

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


def test_unsure_redirects_go_to_review(tmp_path):
    import csv

    from site_audit.actions import _tokens, build_actions, write_action_files
    from site_audit.findings import Finding

    # Enheter, korta ord och plattformsord räknas inte som gemensamma ord
    assert _tokens("/battle-rope-10-20m_30-40mm-dk/p/728") == {"battle", "rope"}

    class CU:
        def __init__(self, url):
            self.url, self.status, self.redirect_count, self.facts, self.final_url = url, 200, 0, object(), url

    class CR:
        urls = {u: CU(u) for u in ("https://x.se/collections/battle-ropes", "https://x.se/collections/all")}

    fs = [Finding("redirect_target_missing", "critical", "redirects", "m", url="https://x.se/battle-rope-10m/p/728"),
          Finding("redirect_target_missing", "critical", "redirects", "m", url="https://x.se/boksepakke-profi/p/1129")]
    _, sure, review = build_actions(fs, CR(), with_review=True)
    # Gissningar importeras aldrig automatiskt, även när de är bra
    assert sure == []
    assert {r[0]: r[1] for r in review} == {"/battle-rope-10m/p/728": "/collections/battle-ropes",
                                            "/boksepakke-profi/p/1129": "/collections/all"}
    write_action_files(fs, CR(), tmp_path)
    rows = list(csv.reader(open(tmp_path / "redirects_review.csv")))
    assert {r[0] for r in rows[1:]} == {"/battle-rope-10m/p/728", "/boksepakke-profi/p/1129"}


def test_ads_parsers():
    from datetime import date

    from site_audit import ads_api as a

    class Resp:
        def __init__(self, data, code=200):
            self.data, self.status_code, self.text = data, code, ""

        def json(self):
            return self.data

    class GoogleSession:
        def __init__(self):
            self.calls = []

        def post(self, url, json, timeout):
            self.calls.append((url, json))
            return Resp([{"results": [{"segments": {"date": "2026-10-01"}, "campaign": {"id": "7", "name": "PMax", "advertisingChannelType": "PERFORMANCE_MAX"},
                                       "customer": {"currencyCode": "SEK"},
                                       "metrics": {"costMicros": "12500000", "impressions": "100", "clicks": "5", "conversions": 1.5, "conversionsValue": 1999.0}}]},
                         {"results": []}])

    gs = GoogleSession()
    rows = list(a.google_ads_campaign_rows(gs, "833-139-0722", date(2026, 10, 1), date(2026, 10, 1), "v21"))
    assert rows == [{"d": "2026-10-01", "customer_id": "8331390722", "campaign_id": "7", "campaign_name": "PMax",
                     "channel_type": "PERFORMANCE_MAX", "currency": "SEK", "cost": 12.5, "impressions": 100, "clicks": 5,
                     "conversions": 1.5, "conversions_value": 1999.0}]
    assert "customers/8331390722/googleAds:searchStream" in gs.calls[0][0] and "BETWEEN '2026-10-01'" in gs.calls[0][1]["query"]
    assert [n for n, _, _ in a.GOOGLE_ADS_SCHEMA] == list(rows[0])

    class ProductSession(GoogleSession):
        def post(self, url, json, timeout):
            return Resp([{"results": [{"segments": {"date": "2026-10-01", "productItemId": "SKU1", "productTitle": "Kettlebell", "productBrand": "GS"},
                                       "customer": {"currencyCode": "DKK"}, "metrics": {"costMicros": "1000000"}}]}])

    prod = list(a.google_ads_product_rows(ProductSession(), "1", date(2026, 10, 1), date(2026, 10, 1)))
    assert prod[0]["item_id"] == "SKU1" and prod[0]["cost"] == 1.0 and prod[0]["clicks"] == 0
    assert [n for n, _, _ in a.GOOGLE_ADS_PRODUCT_SCHEMA] == list(prod[0])

    class MetaSession:
        def __init__(self):
            self.urls = []

        def get(self, url, params, timeout):
            self.urls.append((url, params))
            if len(self.urls) == 1:
                return Resp({"data": [{"date_start": "2026-10-01", "campaign_id": "9", "campaign_name": "Retarget", "account_currency": "DKK",
                                       "spend": "100.5", "impressions": "1000", "reach": "800", "clicks": "20",
                                       "actions": [{"action_type": "omni_purchase", "value": "3"}, {"action_type": "purchase", "value": "3"},
                                                   {"action_type": "link_click", "value": "20"}],
                                       "action_values": [{"action_type": "omni_purchase", "value": "4500"}, {"action_type": "purchase", "value": "4500"}]}],
                             "paging": {"next": "https://graph.facebook.com/next-page"}})
            return Resp({"data": [{"date_start": "2026-10-02", "campaign_id": "9", "campaign_name": "Retarget", "account_currency": "DKK",
                                   "spend": "0", "impressions": "0", "reach": "0", "clicks": "0"}]})

    ms = MetaSession()
    meta = list(a.meta_ads_rows(ms, "act_123", date(2026, 10, 1), date(2026, 10, 2)))
    assert [m["d"] for m in meta] == ["2026-10-01", "2026-10-02"]
    assert meta[0]["purchases"] == 3.0 and meta[0]["purchase_value"] == 4500.0  # omni_purchase och purchase räknas inte dubbelt
    assert meta[0]["account_id"] == "123" and meta[1]["purchases"] == 0.0
    assert ms.urls[0][0].endswith("/act_123/insights") and ms.urls[1] == ("https://graph.facebook.com/next-page", None)
    assert "access_token" not in ms.urls[0][1]  # token ligger i huvudet, aldrig i URL:en
    assert [n for n, _, _ in a.META_ADS_SCHEMA] == list(meta[0])


def test_refresh_skips_unconfigured_and_continues_after_failure(monkeypatch, capsys, tmp_path):
    from site_audit import main as m
    from site_audit.config import site_from_dict

    site = site_from_dict({"name": "x-se", "base_url": "https://x.se", "bq_project": "p", "ga4_property_id": "1",
                           "meta_ad_account_ids": ["act_1"]})
    calls = []

    def fake_fetch(site_, store, source, start, end, **kw):
        calls.append((source, (end - start).days + 1))
        if source == "ga4":
            raise RuntimeError("nekad")
        return 5, f"t_{source}"

    monkeypatch.setattr(m, "fetch_source", fake_fetch)
    monkeypatch.setattr(m, "_site", lambda args: site)
    monkeypatch.setattr(m, "_store", lambda s: type("S", (), {"dataset": "site_audit"})())
    args = type("A", (), {"site": "x-se", "days": 30, "source": None})()
    assert m.cmd_refresh(args) == 1  # ga4 misslyckades, men de andra kördes
    out = capsys.readouterr().out
    assert "ga4: MISSLYCKADES" in out and "google-ads: hoppas över" in out and "meta-ads: 5 rader" in out
    assert ("ga4-kanal", 30) in calls and ("meta-ads", 30) in calls and not any(c[0].startswith("google-ads") for c in calls)


def test_growth_sql_per_store_and_portfolio():
    from site_audit.config import site_from_dict
    from site_audit.growth_sql import growth_sql

    common = {"bq_project": "proj-a", "ga4_property_id": "1", "shopify_dataset": "proj-a.shopify", "growth_views": True}
    sites = {
        "g-se": site_from_dict({"name": "g-se", "base_url": "https://g.se", **common, "google_ads_customer_ids": ["1"],
                                "meta_ad_account_ids": ["act_2"], "vertical": "traning",
                                "hostname_markets": {"www.g.se": "SE", "www.g.dk": "DK"}}),
        "g-dk": site_from_dict({"name": "g-dk", "base_url": "https://g.dk", "bq_project": "proj-a", "ga4_property_id": "1"}),
        "bos-se": site_from_dict({"name": "bos-se", "base_url": "https://bos.se", **common, "data_key": "bestofsports",
                                  "company": "Annat AB", "currency_markets": {"SEK": "SE", "DKK": "DK", "EUR": "FI"}}),
    }
    sql = growth_sql(sites)
    assert sql.count("CREATE OR REPLACE VIEW `proj-a.site_audit.growth_daily_") == 2  # g-dk har inte growth_views
    assert "growth_daily_g_se" in sql and "growth_daily_bestofsports" in sql and "growth_daily_g_dk" not in sql
    assert "`proj-a.site_audit.google_ads_daily_g_se`" in sql and "`proj-a.site_audit.meta_ads_daily_g_se`" in sql
    # butiken utan annonser får inget annonsunderlag men fungerar ändå
    bos = sql[sql.index("-- Butik: bos-se"):sql.index("CREATE SCHEMA")]
    assert "growth_ads_daily_bestofsports" not in bos and "CAST(NULL AS FLOAT64) AS google_cost" in bos
    assert "ENDS_WITH(hostname, '.se')" in bos and "CASE hostname WHEN 'www.g.se' THEN 'SE'" in sql
    assert "'Annat AB' AS company" in sql and "WHEN 'FI' THEN 'EUR'" in sql
    assert "portfolio_daily" in sql and "portfolio_weekly" in sql
    # produktvyn kopplar annonsprodukter till Shopify-varianter, bara för butiker med både annonser och Shopify-data
    assert "growth_product_daily_g_se" in sql and "growth_product_daily_bestofsports" not in sql
    assert "REGEXP_EXTRACT(a.item_id, r'(\\d+)$')" in sql and "v.variant_key IS NOT NULL AS matched" in sql

    import pytest

    with pytest.raises(ValueError):
        growth_sql({"x": site_from_dict({"name": "x", "base_url": "https://x.se", "bq_project": "p"})})
    sqlglot = pytest.importorskip("sqlglot")
    assert len(sqlglot.parse(sql, read="bigquery")) >= 7  # fler vyer och schemat, utan syntaxfel


def test_table_key_separates_store_tables_from_domain_tables():
    from site_audit.config import site_from_dict

    s = site_from_dict({"name": "bos-fi", "base_url": "https://bos.fi", "data_key": "best-of-sports"})
    assert s.table_key == "best_of_sports" and s.slug == "bos_fi"  # GA4/annonser per butik, Search Console per domän
    assert site_from_dict({"name": "g-se", "base_url": "https://g.se"}).table_key == "g_se"


def test_portfolio_draft_parses_and_has_one_view_owner_per_store():
    from pathlib import Path

    from site_audit.config import load_sites

    sites = load_sites(Path(__file__).resolve().parents[1] / "sites.portfolio.draft.toml")
    stores = {}
    for s in sites.values():
        stores.setdefault(s.table_key, []).append(s)
    assert len(stores) == 7  # utkastet: 7 butiker (Gorilla ligger redan i sites.toml, totalt 8 butiker och 13 domäner)
    assert len(sites) == 11
    for key, members in stores.items():
        owners = [m for m in members if m.growth_views]
        assert len(owners) == 1, f"{key}: exakt en sajt per butik ska äga vyerna"
        assert owners[0].hostname_markets, f"{key}: hostname_markets saknas"


def test_google_ads_developer_token_is_optional(monkeypatch):
    from site_audit import ads_api as a

    class Fake:
        def __init__(self):
            self.headers = {}

    monkeypatch.setattr("site_audit.google_api.authorized_session", lambda scopes: Fake())
    assert "developer-token" not in a.google_ads_session(None, "234-712-0945").headers
    h = a.google_ads_session("tok", "234-712-0945").headers
    assert h["developer-token"] == "tok" and h["login-customer-id"] == "2347120945"


def test_google_ads_history_is_fetched_in_windows():
    from datetime import date

    from site_audit import ads_api as a

    ws = list(a.windows(date(2025, 7, 1), date(2025, 9, 5), 31))
    assert ws[0] == (date(2025, 7, 1), date(2025, 7, 31)) and ws[1] == (date(2025, 8, 1), date(2025, 8, 31))
    assert ws[-1] == (date(2025, 9, 1), date(2025, 9, 5)) and len(ws) == 3
    assert list(a.windows(date(2026, 1, 1), date(2026, 1, 1))) == [(date(2026, 1, 1), date(2026, 1, 1))]

    class Resp:
        status_code, text = 200, ""

        def json(self):
            return []

    class S:
        def __init__(self):
            self.queries = []

        def post(self, url, json, timeout):
            self.queries.append(json["query"])
            return Resp()

    s = S()
    assert list(a.google_ads_product_rows(s, "1", date(2025, 7, 1), date(2025, 10, 31), "v26")) == []
    assert len(s.queries) == 4 and "BETWEEN '2025-07-01' AND '2025-07-31'" in s.queries[0] and "'2025-10-31'" in s.queries[-1]


def test_weekly_report_alerts_and_formatting():
    from datetime import date, timedelta

    from site_audit.config import site_from_dict
    from site_audit.growth_report import build_report, kpis, pct, periods

    today = date(2026, 10, 19)
    site = site_from_dict({"name": "g-se", "base_url": "https://g.se", "bq_project": "p", "ga4_property_id": "1", "growth_views": True,
                           "shopify_dataset": "p.shopify", "google_ads_customer_ids": ["1"], "meta_ad_account_ids": ["act_1"]})
    per = periods(today)
    assert per["w1"] == (date(2026, 10, 12), date(2026, 10, 18)) and per["w0"] == (date(2026, 10, 5), date(2026, 10, 11))
    assert per["base"] == (date(2026, 9, 7), date(2026, 10, 4))

    rows = []
    d = per["base"][0]
    while d <= per["w1"][1]:
        weak = d >= per["w1"][0]  # i veckan faller ordrar och intäkt per annonskrona kraftigt för SE
        rows.append({"d": d, "market": "SE", "orders": 6 if weak else 14, "revenue": 8000.0 if weak else 20000.0,
                     "sessions": 900 if weak else 1000, "google_cost": 2000.0, "meta_cost": 1000.0})
        rows.append({"d": d, "market": "DK", "orders": 10, "revenue": 9000.0, "sessions": 800, "google_cost": 700.0, "meta_cost": 300.0})
        d += timedelta(days=1)

    def fake_query(sql, params=None):
        if "MAX(" in sql:
            return [{"source": "Shopify-ordrar", "latest": today - timedelta(days=1)}, {"source": "GA4 landningssidor", "latest": today - timedelta(days=9)}]
        if "growth_daily" in sql:
            return rows
        if "ga4_channel_daily" in sql:
            return [{"hostname": "www.g.se", "channel": "Paid Search", "s1": 900, "sb": 4000, "p1": 5, "pb": 30},
                    {"hostname": "www.g.se", "channel": "Direct", "s1": 2000, "sb": 7000, "p1": 20, "pb": 80}]
        if "growth_product_daily" in sql:
            return [{"market": "DK", "item_id": "1", "title": "Chinsstång", "v1": 0, "v0": 14000, "c1": 27, "c0": 445, "stock": 0, "matched": True, "status": "ACTIVE"},
                    {"market": "SE", "item_id": "2", "title": "Hantlar", "v1": 5000, "v0": 4800, "c1": 120, "c0": 110, "stock": 0, "matched": True, "status": "ACTIVE"},
                    {"market": "SE", "item_id": "3", "title": "Kettlebell", "v1": 100, "v0": 90, "c1": 5, "c0": 4, "stock": 12, "matched": True, "status": "ACTIVE"}]
        raise AssertionError(sql)

    store = type("S", (), {"query": staticmethod(fake_query)})()
    rep = build_report(store, site, today)
    texts = [(a.level, a.source, a.text) for a in rep.alerts]
    assert rep.has_high
    assert any(l == "hög" and src == "GA4 landningssidor" for l, src, _ in texts)  # föråldrad källa
    assert any(l == "hög" and src == "SE" and "Ordrar" in t for l, src, t in texts)  # ordrar −57 % mot snittet
    assert any(l == "hög" and src == "SE" and "MER" in t for l, src, t in texts)
    assert not any(src == "DK" and l == "hög" for l, src, _ in texts)  # DK oförändrad
    assert any(l == "hög" and "Hantlar" in t for l, src, t in texts)  # klick utan lager
    assert any(l == "medel" and "Chinsstång" in t for l, src, t in texts)  # annonsvärdet gick till noll
    assert not any("Kettlebell" in t for _, _, t in texts)
    assert rep.alerts[0].level == "hög" and "## Nyckeltal per marknad" in rep.markdown and "## Larm" in rep.markdown
    assert "### SE" in rep.markdown and "### DK" in rep.markdown and "Paid Search" in rep.markdown

    assert pct(110, 100) == 10.0 and pct(1, 0) is None and pct(None, 5) is None
    k = kpis([{"d": today, "orders": 3, "revenue": 300.0, "sessions": None, "google_cost": 100.0, "meta_cost": 50.0}], (today, today))
    assert k["sessions"] is None and k["order_rate"] is None and k["mer"] == 2.0 and k["days_with_sessions"] == 0

    import pytest

    sqlglot = pytest.importorskip("sqlglot")
    from site_audit import growth_report as g

    for sql in (g.freshness_sql(site), g.daily_sql(site, today), g.channel_sql(site, today), g.product_sql(site, today)):
        sqlglot.parse_one(sql, read="bigquery")


def test_weekly_upload_target_parsing():
    import pytest

    from site_audit.config import ConfigError
    from site_audit.main import split_gs_uri

    assert split_gs_uri("gs://bucket/weekly/") == ("bucket", "weekly") and split_gs_uri("gs://bucket") == ("bucket", "")
    with pytest.raises(ConfigError):
        split_gs_uri("/tmp/x")


def test_inventory_snapshot_is_idempotent_per_day():
    import pytest

    from site_audit.main import inventory_snapshot_sql, snapshot_inventory

    stmts = inventory_snapshot_sql("p.site_audit", "inventory_daily_x", "p.shopify")
    assert stmts[0].startswith("CREATE TABLE IF NOT EXISTS") and stmts[1].startswith("DELETE FROM") and stmts[2].startswith("INSERT INTO")
    assert "WHERE d = CURRENT_DATE('Europe/Stockholm')" in stmts[1]  # omkörning samma dag ersätter dagens rader

    class Job:
        def __init__(self, sql):
            self.num_dml_affected_rows = 321 if sql.startswith("INSERT") else 0

        def result(self):
            return None

    ran = []

    class Client:
        def query(self, sql):
            ran.append(sql)
            return Job(sql)

    store = type("S", (), {"dataset": "p.site_audit", "client": Client()})()
    assert snapshot_inventory(store, "p.shopify", "inventory_daily_x") == 321 and len(ran) == 3
    sqlglot = pytest.importorskip("sqlglot")
    for sql in stmts:
        sqlglot.parse_one(sql, read="bigquery")


def test_growth_test_log_add_and_evaluate():
    from datetime import date, timedelta

    import pytest

    from site_audit import growth_tests as t
    from site_audit.config import site_from_dict

    site = site_from_dict({"name": "g-se", "base_url": "https://g.se", "bq_project": "p"})
    ran = []

    class Job:
        def result(self):
            return None

    class Client:
        def query(self, sql):
            ran.append(sql)
            return Job()

    store = type("S", (), {"dataset": "p.site_audit", "client": Client()})()
    tid = t.add_test(store, site, start=date(2026, 10, 20), channel="google_ads", metric="mer", hypothesis="Lägre mål-ROAS ger fler ordrar",
                     action="Sänk mål-ROAS i SE till 3,8", market="SE", expected_pct=10)
    assert len(tid) == 8 and ran[0].startswith("CREATE TABLE IF NOT EXISTS") and "INSERT INTO `p.site_audit.growth_tests`" in ran[2]
    assert "'planerad'" in ran[2] and "DATE '2026-10-20'" in ran[2]
    with pytest.raises(ValueError):
        t.add_test(store, site, start=date(2026, 10, 20), channel="google_ads", metric="finns_inte", hypothesis="x", action="y")
    # citattecken i fritext får inte bryta SQL:en
    t.add_test(store, site, start=date(2026, 10, 20), channel="meta", metric="orders", hypothesis="It's \"bra\"", action="a")
    assert "It\\'s" in ran[-1]

    start = date(2026, 10, 1)
    def rows(market, before_orders, after_orders):
        out = []
        for i in range(-28, 28):
            d = start + timedelta(days=i)
            out.append({"d": d, "market": market, "orders": after_orders if i >= 0 else before_orders, "revenue": 100.0, "sessions": 1000,
                        "google_cost": 50.0, "meta_cost": 0.0})
        return out

    data = {"SE": rows("SE", 10, 13), "DK": rows("DK", 10, 11)}  # SE +30 %, DK +10 % (kontroll)
    test = {"test_id": "x", "start_date": start, "evaluate_days": 28, "metric": "orders", "market": "SE", "expected_change_pct": 15,
            "hypothesis": "h", "action": "a", "channel": "google_ads"}
    ev = t.evaluate(data, test, date(2026, 11, 30))
    assert round(ev["result_pct"]) == 30 and round(ev["control_pct"]) == 10 and round(ev["uplift_pct"]) == 20
    assert ev["complete"] and ev["verdict"].startswith("Förväntat utfall uppnåtts")
    early = t.evaluate(data, test, date(2026, 10, 10))
    assert not early["complete"] and "Preliminärt" in early["verdict"]
    t.save_evaluation(store, "x", ev)
    assert "SET status = 'utvärderad'" in ran[-1] and "uplift_pct = 20.0000" in ran[-1]
    assert "Netto: +20.0 %" in t.format_evaluation(test, ev)


class _Resp:
    def __init__(self, data, status=200):
        self._d, self.status_code, self.text, self.headers = data, status, "", {}

    def json(self):
        return self._d


def test_merchant_product_rows_pages_and_status():
    from datetime import date

    from site_audit.merchant_api import merchant_product_rows

    pages = [
        {"products": [{"offerId": "A1", "contentLanguage": "sv", "feedLabel": "SE", "productAttributes": {"title": "Hantel"},
                       "productStatus": {"destinationStatuses": [{"approvedCountries": ["SE"], "disapprovedCountries": []}],
                                         "itemLevelIssues": [{"code": "x", "severity": "DEMOTED", "description": "Låg bildkvalitet"}]}}],
         "nextPageToken": "t2"},
        {"products": [{"offerId": "B2", "productStatus": {"destinationStatuses": [{"disapprovedCountries": ["SE"]}],
                                                          "itemLevelIssues": [{"code": "p", "severity": "DISAPPROVED", "description": "Pris saknas"}]}}]},
    ]
    calls = []

    class S:
        def get(self, url, params=None, timeout=0):
            calls.append((url, dict(params)))
            return _Resp(pages[len(calls) - 1])

    rows = list(merchant_product_rows(S(), "123-45", date(2026, 10, 19)))
    assert [r["offer_id"] for r in rows] == ["A1", "B2"] and calls[0][0].endswith("/accounts/12345/products")
    assert calls[1][1]["pageToken"] == "t2"
    assert rows[0]["is_disapproved"] is False and rows[0]["top_issue"] == "Låg bildkvalitet"
    assert rows[1]["is_disapproved"] is True and rows[1]["top_issue"] == "Pris saknas" and rows[1]["title"] == ""


def test_klaviyo_order_rows_and_key_not_in_url():
    from datetime import date

    from site_audit.klaviyo_api import klaviyo_order_rows, klaviyo_session

    s = klaviyo_session("pk_secret", "2025-10-15")
    assert s.headers["Authorization"] == "Klaviyo-API-Key pk_secret" and s.headers["revision"] == "2025-10-15"
    urls = []

    def request(method, url, **kw):
        urls.append(url)
        if url.endswith("/metrics/"):
            return _Resp({"data": [{"id": "M1", "attributes": {"name": "Placed Order"}}]})
        return _Resp({"data": {"attributes": {"dates": ["2026-10-01T00:00:00+02:00", "2026-10-02T00:00:00+02:00"], "data": [
            {"dimensions": ["EMAIL"], "measurements": {"count": [3, 0], "sum_value": [900.0, 0]}},
            {"dimensions": [""], "measurements": {"count": [10, 12], "sum_value": [4000.0, 5000.0]}}]}}})

    s.request = request
    rows = list(klaviyo_order_rows(s, date(2026, 10, 1), date(2026, 10, 2)))
    assert {"d": "2026-10-01", "channel": "email", "orders": 3.0, "revenue": 900.0} in rows
    assert len(rows) == 3 and any(r["channel"] == "ingen" and r["d"] == "2026-10-02" for r in rows)
    assert all("pk_secret" not in u for u in urls)


def test_check_access_reports_each_source():
    from site_audit.access_check import check_access, format_access

    def boom():
        raise RuntimeError("403 nekad\nrad två")

    res = check_access(None, None, {"ga4": (True, lambda: None), "meta-ads": (True, boom), "klaviyo": (False, boom)})
    assert res == [("ga4", "OK", ""), ("meta-ads", "FEL", "403 nekad rad två"), ("klaviyo", "saknas", "inte konfigurerad")]
    assert "meta-ads" in format_access("x", res)


def test_portfolio_rank_against_median():
    from datetime import date, timedelta

    from site_audit.portfolio_report import format_report, rank

    today = date(2026, 10, 19)

    def rows(store, w0, w1):
        out = []
        for i in range(1, 15):
            d = today - timedelta(days=i)
            out.append({"d": d, "store": store, "market": "SE", "vertical": "v", "orders": w1 if i <= 7 else w0, "revenue": 1000.0,
                        "sessions": 500, "google_cost": 100.0, "meta_cost": 0.0})
        return out

    data = rows("a", 100, 100) + rows("b", 100, 102) + rows("c", 100, 60)  # c tappar 40 %, medianen är +0 %
    ranked = rank(data, today)
    c = next(o for o in ranked if o["store"] == "c")
    assert round(c["orders_chg"]) == -40 and round(c["orders_rel"]) == -40
    text = format_report(ranked, today)
    assert "c SE: ordrar -40 %" in text and "sämre" in text
    assert "Ingen data" in format_report([], today)


def test_new_analysis_sql_parses():
    from pathlib import Path

    sqlglot = pytest.importorskip("sqlglot")
    for name in ("merchant_avvisade.sql", "epost_andel.sql"):
        sql = Path(__file__).parent.parent.joinpath("sql", "analys", name).read_text().replace("PROJ", "p").replace("KEY", "k")
        assert sqlglot.parse(sql, read="bigquery")


def test_audit_checks_from_seo_report():
    from site_audit.checks.admin_checks import check_product_text_residue
    from site_audit.checks.crawl_checks import check_link_hygiene, check_schema
    from site_audit.findings import Finding

    site = site_from_dict({"name": "s", "base_url": "https://s.example"})
    clean = {"id": "1", "handle": "a", "status": "ACTIVE", "description": "En vanlig beskrivning av produkten."}
    fence = {"id": "2", "handle": "b", "status": "ACTIVE", "description": "Text ```html <div style=\"x\">hej</div> ```"}
    draft = {"id": "3", "handle": "c", "status": "DRAFT", "description": "ChatGPT skrev detta"}
    ai = {"id": "4", "handle": "d", "status": "ACTIVE", "description": "Certainly! Here is a better description"}
    found = check_product_text_residue(AdminData(products=[clean, fence, draft, ai]), site)
    assert sorted(f.resource for f in found) == ["2", "4"] and all(isinstance(f, Finding) for f in found)

    class Facts:
        def __init__(self, links, schema=None):
            self.internal_links, self.product_schema = links, schema or []
            self.jsonld_types, self.jsonld_errors, self.page_type, self.has_breadcrumb_schema = [], 0, "product", True

    class CU:
        def __init__(self, url, facts):
            self.url, self.facts, self.status, self.source = url, facts, 200, "link"

    prod = {"name": "x", "images": ["https://i/x.jpg"], "invalid_images": [], "relative_images": [], "has_offers": True,
            "has_brand": True, "has_rating": False}
    cr = type("CR", (), {"urls": {
        "u1": CU("https://s.example/a", Facts(["https://s.example/collections/x?_pos=2&_psq=latsdrag", "https://s.example/ok"], [prod])),
        "u2": CU("https://s.example/b", Facts(["https://s.example/p?pr_prod_strat=x"]))}})()
    links = check_link_hygiene(cr, site)
    assert len(links) == 1 and links[0].check == "internal_links_tracking_params" and "2 interna länkar på 2 sidor" in links[0].message
    assert any(f.check == "product_schema_no_rating" for f in check_schema(cr, site))


def test_new_seo_sql_parses_and_uses_word_boundaries():
    from pathlib import Path

    sqlglot = pytest.importorskip("sqlglot")
    base = Path(__file__).parent.parent / "sql" / "analys"
    for name in ("doda_sidor_med_trafik.sql", "sokfragor_luckor.sql"):
        sql = (base / name).read_text().replace("PROJ", "p").replace("KEY", "k").replace("GSCTABLE", "p.d.t")
        assert sqlglot.parse(sql, read="bigquery")
    text = (base / "sokfragor_luckor.sql").read_text()
    assert "|kan|ska|" in text and ")\\s|" in text  # frågeord kräver mellanslag efter ordet (kanin, skateboard matchas inte)


def test_psi_snapshot_summarize_and_render():
    import importlib.util
    from pathlib import Path

    spec = importlib.util.spec_from_file_location("psi_snapshot", Path(__file__).parent.parent / "scripts" / "psi_snapshot.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    data = {
        "loadingExperience": {"metrics": {"LARGEST_CONTENTFUL_PAINT_MS": {"percentile": 5800, "category": "SLOW"},
                                          "CUMULATIVE_LAYOUT_SHIFT_SCORE": {"percentile": 8, "category": "FAST"}}},
        "lighthouseResult": {"categories": {"performance": {"score": 0.42}}, "audits": {
            "largest-contentful-paint": {"numericValue": 6100.0},
            "largest-contentful-paint-element": {"details": {"items": [{"items": [{"node": {"snippet": "<img class=\"hero\">"}}]}]}},
            "unused-javascript": {"title": "Reduce unused JavaScript", "details": {"type": "opportunity", "overallSavingsMs": 900, "overallSavingsBytes": 204800}},
            "uses-text-compression": {"title": "x", "details": {"type": "opportunity", "overallSavingsMs": 0}},
            "third-party-summary": {"details": {"items": [{"entity": "Klaviyo", "blockingTime": 310.4, "transferSize": 51200}]}},
            "total-byte-weight": {"numericValue": 3145728}}}}
    s = mod.summarize(data)
    assert s["score"] == 42 and s["field"]["LCP"]["p75"] == 5800 and s["field"]["CLS"]["p75"] == 0.08
    assert s["opportunities"] == [(900, "Reduce unused JavaScript", 204800)] and s["third_party"][0]["blocking_ms"] == 310
    text = mod.render("https://x/", s)
    assert "LCP 5.8 s" in text and "Möjlig vinst 900 ms" in text and "Klaviyo" in text and "3072 kB" in text
    assert mod.summarize({})["field"] == {} and "ingen fältdata" in mod.render("u", mod.summarize({}))


def test_category_keyword_sql_parses():
    from pathlib import Path

    sqlglot = pytest.importorskip("sqlglot")
    sql = (Path(__file__).parent.parent / "sql" / "analys" / "kategori_sokord.sql").read_text().replace("GSCTABLE", "p.d.t")
    assert sqlglot.parse(sql, read="bigquery")


def test_growth_test_log_page_metric():
    from datetime import date, timedelta

    import pytest

    from site_audit import growth_tests as t

    ran = []

    class Client:
        def query(self, sql):
            ran.append(sql)
            return type("J", (), {"result": lambda self: None})()

    store = type("S", (), {"dataset": "p.site_audit", "client": Client()})()
    site = type("Site", (), {"table_key": "gs"})()
    with pytest.raises(ValueError):
        t.add_test(store, site, start=date(2026, 10, 22), channel="site", metric="gsc_clicks", hypothesis="h", action="a")
    tid = t.add_test(store, site, start=date(2026, 10, 22), channel="site", metric="gsc_clicks", hypothesis="Länkar ger klick",
                     action="Länkblock i blogg", pages=["/collections/motionscykel-kondition", " /collections/spinningcykel"], expected_pct=10)
    assert "ADD COLUMN IF NOT EXISTS pages" in ran[1] and "'/collections/motionscykel-kondition,/collections/spinningcykel'" in ran[-1] and len(tid) == 8

    start = date(2026, 10, 22)
    rows = []
    for i in range(-28, 28):
        d = start + timedelta(days=i)
        rows += [{"d": d, "url": "https://www.gorillasports.se/collections/spinningcykel?page=2", "clicks": 10 if i >= 0 else 5, "impressions": 100},
                 {"d": d, "url": "https://www.gorillasports.se/collections/hantlar", "clicks": 11 if i >= 0 else 10, "impressions": 100},
                 {"d": d, "url": "https://www.gorillasports.se/blogs/blogg/x", "clicks": 50 if i >= 0 else 20, "impressions": 100}]
    test = {"test_id": "x", "start_date": start, "evaluate_days": 28, "metric": "gsc_clicks", "pages": "/collections/spinningcykel",
            "expected_change_pct": 20, "hypothesis": "h", "action": "a", "channel": "site"}
    ev = t.evaluate_pages(rows, test, date(2026, 12, 1))
    # måltidssidor +100 %, övriga /collections/ +10 % (bloggen räknas inte som kontroll)
    assert round(ev["result_pct"]) == 100 and round(ev["control_pct"]) == 10 and round(ev["uplift_pct"]) == 90
    assert ev["complete"] and ev["verdict"].startswith("Förväntat utfall uppnåtts")
    assert "Kontroll (övriga sidor av samma typ)" in t.format_evaluation(test, ev)
    early = t.evaluate_pages(rows, test, date(2026, 11, 20))
    assert not early["complete"] and "Preliminärt" in early["verdict"]
    sqlglot = pytest.importorskip("sqlglot")
    sqlglot.parse_one(t.gsc_rows_sql("p.d.gsc", date(2026, 10, 1), date(2026, 10, 31)), read="bigquery")


def test_diff_text_script_reports_only_changes():
    import importlib.util
    from pathlib import Path

    spec = importlib.util.spec_from_file_location("diff_text", Path(__file__).parent.parent / "scripts" / "diff_text.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod.changes("abc", "abc") == []
    found = mod.changes("Hej kvalitéer och mer", "Hej kvaléteter och mer")
    assert found and all(t in ("replace", "insert", "delete") for t, _, _ in found)


def test_fetch_ga4_with_several_properties_filters_hostnames(monkeypatch):
    from datetime import date

    from site_audit import google_api as g
    from site_audit import main as m
    from site_audit.config import site_from_dict

    site = site_from_dict({"name": "bos-se", "base_url": "https://www.bos.se", "bq_project": "p", "data_key": "bos",
                           "ga4_property_id": "1", "ga4_properties": {"1": ["bos.se"], "2": ["bos.dk"], "3": ["www.bos.fi"]}})
    assert site.ga4_property_map() == {"1": ["bos.se"], "2": ["bos.dk"], "3": ["www.bos.fi"]}

    def fake_rows(session, pid, start, end, **kw):
        # varje egendom får data från alla tre domäner, som om en delad tagg skickade till alla (felkonfiguration)
        for host in ("www.bos.se", "www.bos.dk", "www.bos.fi"):
            yield {"d": "2026-10-20", "property_id": pid, "hostname": host, "landing": "/", "sessions": 10, "purchases": 1, "revenue": 5.0}

    loaded = {}

    def fake_load(store, table, schema, rows, replace_range=None, **kw):
        loaded["table"], loaded["rows"], loaded["range"] = table, list(rows), replace_range
        return len(loaded["rows"])

    monkeypatch.setattr(g, "authorized_session", lambda scopes: object())
    monkeypatch.setattr(g, "ga4_rows", fake_rows)
    monkeypatch.setattr(g, "load_rows", fake_load)
    n, table = m.fetch_source(site, object(), "ga4", date(2026, 10, 20), date(2026, 10, 20))
    # bara en rad per egendom och domän som egendomen hör till: inget dubblerat
    assert n == 3 and table == "ga4_landing_daily_bos"
    assert sorted((r["property_id"], r["hostname"]) for r in loaded["rows"]) == [("1", "www.bos.se"), ("2", "www.bos.dk"), ("3", "www.bos.fi")]
    assert loaded["range"] == ("d", date(2026, 10, 20), date(2026, 10, 20))
    single = site_from_dict({"name": "x", "base_url": "https://x.se", "ga4_property_id": "9"})
    assert single.ga4_property_map() == {"9": []}
