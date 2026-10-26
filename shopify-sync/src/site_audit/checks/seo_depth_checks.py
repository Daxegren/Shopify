"""Fördjupade kontroller för SEO, sajthastighet och mätning (T16, T17, T19).

Bygger på det som genomlysningen redan hämtar: sidfakta per URL. Kontrollerna nedan skriver sammanfattande fynd (en rad per
sidtyp eller sajt, med exempel) så att rapporten inte översvämmas av en rad per sida."""

from __future__ import annotations

from collections import Counter, defaultdict
from statistics import median
from urllib.parse import parse_qsl, urlsplit

from ..config import SiteConfig
from ..crawler import CrawledUrl, CrawlResult
from ..findings import Finding

F = Finding

# Filter- och sorteringsparametrar i Shopify (filter.v.*, filter.p.*, sort_by, view). q= är sökresultat.
FACET_KEYS = ("filter.", "sort_by", "view", "constraint", "q")
THIN_COLLECTION_PRODUCTS = 4
THIRD_PARTY_HOSTS_WARN = 12
JS_RENDERED_SHARE = 0.6   # andel kategorier utan produktlänkar i HTML som tolkas som JavaScript-byggd lista
CORE_TYPES = ("home", "collection", "product")


def _is_facet(url: str) -> bool:
    for k, _ in parse_qsl(urlsplit(url).query, keep_blank_values=True):
        if any(k == fk or (fk.endswith(".") and k.startswith(fk)) for fk in FACET_KEYS):
            return True
    return False


def _page_param(url: str) -> bool:
    return any(k == "page" for k, _ in parse_qsl(urlsplit(url).query, keep_blank_values=True))


def check_faceted_urls(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    """Filter- och sorteringsadresser som går att indexera (saknar noindex och pekar inte med canonical på grundsidan)."""
    from .crawl_checks import _indexable

    bad = [cu for cu in cr.urls.values() if cu.status == 200 and cu.facts and _is_facet(cu.url) and _indexable(cu)]
    if not bad:
        return []
    return [F("faceted_url_indexable", "medium", "indexing",
              f"{len(bad)} filter- eller sorteringsadresser kan indexeras (saknar noindex eller canonical till grundsidan)",
              url=bad[0].url, evidence={"count": len(bad), "sample": [cu.url for cu in bad[:10]]})]


def check_pagination(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    """Paginerade sidor (?page=2) med canonical till sida 1 döljer produkter på sida 2 och framåt för Google."""
    bad = []
    for cu in cr.urls.values():
        f = cu.facts
        if cu.status != 200 or not f or not _page_param(cu.url) or not f.canonical:
            continue
        if not _page_param(f.canonical):
            bad.append(cu)
    if not bad:
        return []
    return [F("paginated_canonical_to_first", "low", "indexing",
              f"{len(bad)} paginerade sidor har canonical till sida 1 (produkter på sida 2 och framåt hittas då bara via sitemapen)",
              url=bad[0].url, evidence={"count": len(bad), "sample": [cu.url for cu in bad[:10]]})]


def check_thin_collections(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    """Kategorier som går att indexera men visar få eller inga produkter (räknat på första sidan i listan)."""
    from .crawl_checks import _indexable

    thin = []
    collections = 0
    for cu in cr.urls.values():
        f = cu.facts
        if not f or f.page_type != "collection" or not _indexable(cu):
            continue
        collections += 1
        if f.product_link_count < THIN_COLLECTION_PRODUCTS:
            thin.append((cu, f.product_link_count))
    out = []
    empty = sum(1 for _, n in thin if n == 0)
    if collections >= 10 and empty / collections >= JS_RENDERED_SHARE:
        # De flesta kategorier saknar produktlänkar i råa HTML:en: listan byggs sannolikt med JavaScript. Ett fynd per kategori vore
        # missvisande, så det blir ett samlat fynd som hänvisar till den renderande kontrollen.
        return [F("collections_rendered_by_js", "medium", "catalog",
                  f"{empty} av {collections} kategorier saknar produktlänkar i HTML:en (produktlistan byggs troligen med JavaScript, "
                  "Google måste rendera sidorna). Verifiera med scripts/rendera_kategorier.py",
                  url=site.base_url, evidence={"collections": collections, "without_product_links": empty,
                                               "sample": [cu.url for cu, n in thin if n == 0][:10]})]
    for cu, n in sorted(thin, key=lambda x: x[1]):
        out.append(F("collection_few_products", "medium" if n == 0 else "low", "catalog",
                     f"Kategori visar {n} produkter (färre än {THIN_COLLECTION_PRODUCTS}) men går att indexera",
                     url=cu.url, evidence={"products_listed": n, "in_sitemap": cu.in_sitemap}))
    return out


def check_third_party_scripts(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    """Hur många externa skriptvärdar laddar varje sidtyp, och vilka är vanligast? Appar och taggar är oftast det som gör
    en Shopify-sida långsam."""
    by_type: dict[str, list[list[str]]] = defaultdict(list)
    for cu in cr.urls.values():
        f = cu.facts
        if cu.status == 200 and f and f.page_type in CORE_TYPES:
            by_type[f.page_type].append(f.external_script_hosts)
    out = []
    for ptype in CORE_TYPES:
        pages = by_type.get(ptype)
        if not pages:
            continue
        med = median(len(h) for h in pages)
        freq = Counter(h for hosts in pages for h in set(hosts))
        top = [(h, round(c / len(pages) * 100)) for h, c in freq.most_common(10)]
        sev = "medium" if med >= THIRD_PARTY_HOSTS_WARN else "info"
        out.append(F("third_party_script_hosts", sev, "performance",
                     f"{ptype}: median {med:.0f} externa skriptvärdar per sida ({len(pages)} sidor)",
                     url=site.base_url, evidence={"page_type": ptype, "median_hosts": med, "pages": len(pages),
                                                    "top_hosts_pct_of_pages": top}))
    return out


def check_image_practices(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    """Bilder utan angiven bredd och höjd ger layoutförskjutning (CLS); bilder utan lazy loading laddas i onödan."""
    out = []
    for ptype in ("collection", "product"):
        pages = [cu.facts for cu in cr.urls.values() if cu.status == 200 and cu.facts and cu.facts.page_type == ptype]
        total = sum(f.images_total for f in pages)
        if not pages or total < 20:
            continue
        no_dim = sum(f.images_no_dimensions for f in pages)
        no_lazy = sum(f.images_no_lazy for f in pages)
        if no_dim / total > 0.3:
            out.append(F("images_without_dimensions", "low", "performance",
                         f"{ptype}: {no_dim / total:.0%} av bilderna saknar bredd och höjd (risk för layoutförskjutning)",
                         url=site.base_url, evidence={"page_type": ptype, "images": total, "without": no_dim, "pages": len(pages)}))
        avg_not_lazy = no_lazy / len(pages)
        if avg_not_lazy > 10:
            out.append(F("images_not_lazy", "low", "performance",
                         f"{ptype}: i snitt {avg_not_lazy:.0f} bilder per sida laddas direkt trots att de ligger under första skärmen",
                         url=site.base_url, evidence={"page_type": ptype, "average": round(avg_not_lazy, 1), "pages": len(pages)}))
    return out


def check_tracking_in_html(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    """Samtycke och taggar enligt HTML. Begränsad: Shopifys cookiebanner, Customer Privacy API och webbpixlar (Customer Events,
    där GA4 från Google & YouTube-appen ligger) laddas av JavaScript och syns inte här. Fynden är därför bara information;
    avgörande test görs i webbläsare med scripts/samtycke_test.py."""
    pages = [cu.facts for cu in cr.urls.values() if cu.status == 200 and cu.facts and cu.facts.page_type in CORE_TYPES]
    if len(pages) < 3:
        return []
    out = []
    cmps = Counter(c for f in pages for c in f.consent_platforms)
    default = sum(f.consent_mode_default for f in pages)
    v2 = sum(f.consent_mode_v2 for f in pages)
    ids = Counter(i for f in pages for i in f.analytics_ids)
    n = len(pages)
    if not cmps:
        out.append(F("consent_platform_not_in_html", "info", "performance",
                     "Ingen samtyckeslösning syns i sidornas HTML (Shopifys egen cookiebanner laddas med JavaScript och syns inte här). "
                     "Kontrollera i webbläsare med scripts/samtycke_test.py",
                     url=site.base_url, evidence={"pages_checked": n}))
    else:
        out.append(F("consent_platform_in_html", "info", "performance",
                     f"Samtyckeslösning i HTML: {', '.join(sorted(cmps))}", url=site.base_url,
                     evidence={"platforms": dict(cmps), "pages_checked": n}))
    if default and v2 < default:
        out.append(F("consent_mode_v2_incomplete", "medium", "performance",
                     "Consent Mode finns men saknar ad_user_data och ad_personalization (krävs sedan 2024 för annonsmätning i EES)",
                     url=site.base_url, evidence={"with_default": default, "with_v2": v2, "pages_checked": n}))
    g_ids = sorted(i for i in ids if i.startswith("G-"))
    if len(g_ids) > 1:
        out.append(F("multiple_ga4_ids", "low", "performance",
                     f"Flera GA4-mätid i HTML ({', '.join(g_ids)}): data kan hamna i fel egendom eller dubbelräknas",
                     url=site.base_url, evidence={"ids": dict(ids)}))
    return out


def check_malformed_hrefs(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    """Länkar vars adress innehåller mallkod eller HTML ({{ shop_url }}, <span class='notranslate'>). Orsaken är oftast en text i temat
    eller en översättning som skrivits sönder, och ger en trasig länk på alla sidor där texten används (sidfot, kundvagn)."""
    by_href: dict[str, list[str]] = defaultdict(list)
    for cu in cr.urls.values():
        if cu.status == 200 and cu.facts:
            for h in cu.facts.malformed_hrefs:
                by_href[h].append(cu.url)
    out = []
    for href, pages in sorted(by_href.items(), key=lambda kv: -len(kv[1]))[:10]:
        out.append(F("malformed_link_href", "high", "links",
                     f"Länkadress med mallkod eller HTML på {len(pages)} sidor: {href[:90]}",
                     url=pages[0], evidence={"href": href, "pages": len(pages), "sample": pages[:5]}))
    return out


def _bare_netloc(url: str) -> str:
    host = urlsplit(url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def check_multiple_canonicals(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    """Sidor med fler än en canonical-tagg. Det sker oftast när temat skriver en egen tagg och ett snippet en andra. Är taggarna olika
    kan Google ignorera båda, och pekar den ena på en annan domän riskerar sidan att inte indexeras på sin egen adress."""
    by_type: dict[str, list[tuple[CrawledUrl, list[str]]]] = defaultdict(list)
    for cu in cr.urls.values():
        f = cu.facts
        if f and cu.status == 200 and len(f.canonicals) > 1:
            by_type[f.page_type].append((cu, f.canonicals))
    out = []
    for ptype, rows in sorted(by_type.items()):
        distinct = [(cu, c) for cu, c in rows if len({c2.rstrip("/") for c2 in c}) > 1]
        identical = len(rows) - len(distinct)
        if distinct:
            hosts = Counter(_bare_netloc(c2) for _, c in distinct for c2 in c)
            out.append(F("multiple_canonical_tags", "high", "indexing",
                         f"{len(distinct)} {ptype}-sidor har flera olika canonical-taggar (Google kan ignorera dem)",
                         url=distinct[0][0].url, evidence={"page_type": ptype, "count": len(distinct), "hosts": dict(hosts),
                                                           "sample": [{"url": cu.url, "canonicals": c[:3]} for cu, c in distinct[:5]]}))
        if identical:
            out.append(F("duplicate_canonical_tags", "low", "indexing", f"{identical} {ptype}-sidor har samma canonical två gånger",
                         url=rows[0][0].url, evidence={"page_type": ptype, "count": identical}))
    return out


def check_schema_domains(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    """Strukturerad data (produkt, erbjudande, brödsmulor, artikel) vars adresser pekar på en annan domän än sidan. Händer när temat
    använder shop.url, som alltid är butikens primärdomän, i stället för request.origin. Organization undantas."""
    by_type: dict[str, list[tuple[CrawledUrl, list[str]]]] = defaultdict(list)
    for cu in cr.urls.values():
        f = cu.facts
        if not f or cu.status != 200 or not f.jsonld_hosts:
            continue
        own = _bare_netloc(cu.url)
        other = [h for h in f.jsonld_hosts if h != own]
        if other:
            by_type[f.page_type].append((cu, other))
    out = []
    for ptype, rows in sorted(by_type.items()):
        hosts = Counter(h for _, o in rows for h in o)
        out.append(F("schema_url_other_domain", "high" if ptype == "product" else "medium", "schema",
                     f"{len(rows)} {ptype}-sidor har strukturerad data med adresser på en annan domän ({', '.join(sorted(hosts))})",
                     url=rows[0][0].url, evidence={"page_type": ptype, "count": len(rows), "hosts": dict(hosts),
                                                   "sample": [cu.url for cu, _ in rows[:5]]}))
    return out


def check_gtm_loaded_twice(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    """Samma Google Tag Manager-container som laddas mer än en gång på samma sida (till exempel ett inbyggt skript i temat och ett
    snippet som läser samma ID från temainställningarna). Taggar kan då köras två gånger."""
    pages = [cu for cu in cr.urls.values() if cu.facts and cu.status == 200 and cu.facts.gtm_loaders]
    if not pages:
        return []
    dup: dict[str, list[str]] = defaultdict(list)
    for cu in pages:
        for container, n in cu.facts.gtm_loaders.items():
            if n > 1:
                dup[container].append(cu.url)
    out = []
    for container, urls in sorted(dup.items()):
        out.append(F("gtm_container_loaded_twice", "high", "tracking",
                     f"Containern {container} laddas mer än en gång på {len(urls)} av {len(pages)} sidor med GTM (taggar kan köras två gånger)",
                     url=urls[0], evidence={"container": container, "pages": len(urls), "pages_with_gtm": len(pages), "sample": urls[:5],
                                            "loaders": cr.urls[urls[0]].facts.gtm_loaders}))
    return out


def check_schema_coverage(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    """Saknade fält som drabbar hela sajten: fraktinformation i produktschemat och brödsmulor på kategorisidor. Samlade fynd,
    eftersom orsaken nästan alltid är en mall."""
    from .crawl_checks import _indexable

    out = []
    prods = [cu for cu in cr.urls.values() if cu.facts and cu.status == 200 and cu.facts.page_type == "product" and cu.facts.product_schema]
    if len(prods) >= 10:
        lacking = [cu for cu in prods if not any(p.get("has_shipping") for p in cu.facts.product_schema)]
        share = len(lacking) / len(prods)
        if share >= 0.2:
            out.append(F("shipping_details_missing", "medium" if share >= 0.9 else "low", "schema",
                         f"{len(lacking)} av {len(prods)} produktsidor ({share:.0%}) saknar shippingDetails i produktschemat (fraktgräns och avgift)",
                         url=site.base_url, evidence={"pages": len(lacking), "product_pages_with_schema": len(prods), "sample": [cu.url for cu in lacking[:5]]}))
    colls = [cu for cu in cr.urls.values() if cu.facts and cu.facts.page_type == "collection" and _indexable(cu)]
    if len(colls) >= 10:
        lacking = [cu for cu in colls if not cu.facts.has_breadcrumb_schema]
        share = len(lacking) / len(colls)
        if share >= 0.8:
            out.append(F("collections_without_breadcrumb_schema", "medium", "schema",
                         f"{len(lacking)} av {len(colls)} kategorisidor ({share:.0%}) saknar BreadcrumbList (mallen skriver ingen)",
                         url=site.base_url, evidence={"pages": len(lacking), "collections": len(colls), "sample": [cu.url for cu in lacking[:5]]}))
    return out


SEO_DEPTH_CHECKS = [check_faceted_urls, check_pagination, check_thin_collections, check_third_party_scripts,
                    check_image_practices, check_tracking_in_html, check_malformed_hrefs, check_multiple_canonicals,
                    check_schema_domains, check_gtm_loaded_twice, check_schema_coverage]
