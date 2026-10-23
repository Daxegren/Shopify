"""Fördjupade kontroller för SEO, sajthastighet och mätning (T16, T17, T19).

Bygger på det som genomlysningen redan hämtar: sidfakta per URL. Kontrollerna nedan skriver sammanfattande fynd (en rad per
sidtyp eller sajt, med exempel) så att rapporten inte översvämmas av en rad per sida."""

from __future__ import annotations

from collections import Counter, defaultdict
from statistics import median
from urllib.parse import parse_qsl, urlsplit

from ..config import SiteConfig
from ..crawler import CrawlResult
from ..findings import Finding

F = Finding

# Filter- och sorteringsparametrar i Shopify (filter.v.*, filter.p.*, sort_by, view). q= är sökresultat.
FACET_KEYS = ("filter.", "sort_by", "view", "constraint", "q")
THIN_COLLECTION_PRODUCTS = 4
THIRD_PARTY_HOSTS_WARN = 12
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
    for cu in cr.urls.values():
        f = cu.facts
        if not f or f.page_type != "collection" or not _indexable(cu):
            continue
        if f.product_link_count < THIN_COLLECTION_PRODUCTS:
            thin.append((cu, f.product_link_count))
    out = []
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


SEO_DEPTH_CHECKS = [check_faceted_urls, check_pagination, check_thin_collections, check_third_party_scripts,
                    check_image_practices, check_tracking_in_html]
