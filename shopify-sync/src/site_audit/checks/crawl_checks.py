"""Kontroller som bara kräver crawldata."""

from __future__ import annotations

import re
from collections import defaultdict
from datetime import date
from urllib.parse import urlsplit

from ..config import SiteConfig
from ..crawler import CrawlResult, CrawledUrl, normalize_url
from ..fetch import INVALID_TARGET
from ..findings import Finding
from ..html_parse import is_noindex, split_locale
from ..textutil import find_misspellings, locale_language

F = Finding
CONTENT_TYPES_NEEDING_H1 = {"product", "collection", "page", "article", "blog", "home"}
SOFT_404_RE = re.compile(r"\b(404|not found|page not found|sidan hittades inte|siden blev ikke fundet|seite nicht gefunden)\b", re.I)
TEST_PAGE_RE = re.compile(r"\b(test|testing|draft|utkast|kopia|copy|dummy|lorem ipsum|temp)\b", re.I)
YEAR_RE = re.compile(r"\b(20[0-3]\d)\b")


def _indexable(cu: CrawledUrl) -> bool:
    if cu.status != 200 or not cu.facts:
        return False
    if is_noindex(cu.facts, {"x-robots-tag": cu.x_robots_tag or ""}):
        return False
    canon = cu.facts.canonical
    return not canon or normalize_url(canon) == normalize_url(cu.final_url)


def check_status(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    out = []
    for err_url, err in cr.sitemap.errors:
        out.append(F("sitemap_unreadable", "high", "indexing", f"Sitemap kunde inte läsas ({err})", url=err_url))
    unique_sitemap = {normalize_url(e.url) for e in cr.sitemap.entries}
    crawled_sitemap = sum(1 for cu in cr.urls.values() if cu.in_sitemap)
    if len(unique_sitemap) > crawled_sitemap:
        out.append(F("crawl_truncated", "info", "indexing",
                     f"Crawlen täckte {crawled_sitemap} av {len(unique_sitemap)} sitemap-URL:er (höj crawl.max_pages för full täckning)",
                     url=site.base_url, evidence={"crawled": crawled_sitemap, "in_sitemap": len(unique_sitemap), "max_pages": site.crawl.max_pages}))
    if not cr.sitemap.entries:
        out.append(F("sitemap_empty", "high", "indexing", "Inga URL:er hittades i sitemapen", url=site.base_url + "/sitemap.xml"))
    for cu in cr.urls.values():
        final = cu.status
        if cu.in_sitemap and final >= 400:
            out.append(F("sitemap_url_error", "critical" if final == 404 else "high", "indexing",
                         f"URL i sitemapen ger {final}", url=cu.url, evidence={"sitemap": cu.sitemap, "pagetype": _ptype(cu.url)}))
        elif cu.in_sitemap and cu.redirect_count:
            out.append(F("sitemap_url_redirects", "medium", "indexing", "URL i sitemapen omdirigeras",
                         url=cu.url, evidence={"final_url": cu.final_url, "hops": cu.redirect_count}))
        elif final >= 500:
            out.append(F("server_error", "high", "indexing", f"Serverfel {final}", url=cu.url))
        elif final == 0 and not cu.redirect_count and not cu.loop:  # omdirigerade och loopar hanteras i check_redirects
            out.append(F("fetch_failed", "medium", "indexing", f"Kunde inte hämtas: {cu.error}", url=cu.url,
                         evidence={"error": cu.error, "source": cu.source}))
        elif final == 404 and cu.linked_from:
            out.append(F("broken_internal_link", "high", "links", "Interna länkar pekar på en sida som ger 404",
                         url=cu.url, evidence={"linked_from": cu.linked_from[:10], "count": len(cu.linked_from)}))
        if cu.in_sitemap and cu.facts and is_noindex(cu.facts, {"x-robots-tag": cu.x_robots_tag or ""}):
            out.append(F("sitemap_noindex", "medium", "indexing", "Sidan finns i sitemapen men har noindex", url=cu.url))
        if cu.status == 200 and cu.facts and cu.facts.title and SOFT_404_RE.search(cu.facts.title):
            out.append(F("soft_404", "high", "indexing", "Sidan svarar 200 men ser ut som en felsida",
                         url=cu.url, evidence={"title": cu.facts.title}))
    return out


def _ptype(url: str) -> str:
    from ..html_parse import page_type

    return page_type(urlsplit(url).path)


def check_redirects(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    out = []
    t = site.thresholds
    for cu in cr.urls.values():
        if not cu.redirect_count and not cu.loop:
            continue
        chain = [h["url"] for h in cu.hops]
        codes = [h["status"] for h in cu.hops]
        if cu.loop:
            out.append(F("redirect_loop", "critical", "redirects", "Omdirigeringsloop", url=cu.url, evidence={"chain": chain}))
            continue
        if cu.status == 0 and (cu.error or "").startswith(INVALID_TARGET):
            out.append(F("redirect_invalid_target", "critical", "redirects",
                         "Omdirigeringens mål saknar domän (t.ex. '//collections/...') och fungerar inte i webbläsare heller",
                         url=cu.url, evidence={"chain": chain, "error": cu.error}))
        elif cu.status == 0:
            out.append(F("redirect_unverified", "low", "redirects", "Slutmålet kunde inte hämtas, omdirigeringen är inte kontrollerad",
                         url=cu.url, evidence={"chain": chain, "codes": codes, "error": cu.error}))
        elif cu.status >= 400:
            out.append(F("redirect_to_error", "critical", "redirects",
                         f"Omdirigeringen slutar i {cu.status} efter {cu.redirect_count} hopp",
                         url=cu.url, evidence={"chain": chain, "codes": codes}))
        elif cu.redirect_count >= t.redirect_chain_warn:
            out.append(F("redirect_chain", "high", "redirects", f"Omdirigeringskedja med {cu.redirect_count} hopp",
                         url=cu.url, evidence={"chain": chain, "codes": codes}))
        if any(c in (302, 303, 307) for c in codes[:-1]):
            out.append(F("temporary_redirect", "medium", "redirects", "Tillfällig omdirigering (302/307) i stället för 301",
                         url=cu.url, evidence={"codes": codes, "final_url": cu.final_url}))
        src_loc, src_rest = split_locale(urlsplit(cu.url).path)
        dst_loc, dst_rest = split_locale(urlsplit(cu.final_url).path)
        if src_loc != dst_loc and dst_loc is not None:
            out.append(F("redirect_changes_locale", "high", "international",
                         f"Omdirigering byter marknad/språk ({src_loc or 'rot'} → {dst_loc})",
                         url=cu.url, evidence={"final_url": cu.final_url}))
        dest_host = urlsplit(cu.final_url).netloc
        if dest_host != site.host:
            brand = site.host.split(".")[-2] if site.host.count(".") >= 1 else ""
            sibling = brand and brand in dest_host
            out.append(F("redirect_to_other_market" if sibling else "redirect_offsite", "high" if sibling else "medium",
                         "international" if sibling else "redirects",
                         f"Skickar besökaren till {dest_host}" + (" (annan marknad)" if sibling else ""),
                         url=cu.url, evidence={"final_url": cu.final_url, "linked_from": cu.linked_from[:5]}))
    return out


def check_geo(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    out = []
    for g in cr.geo:
        codes = [h["status"] for h in g.hops]
        if len(g.hops) > 1:
            loc, _ = split_locale(urlsplit(g.final_url).path)
            sev = "high" if any(c in (302, 307) for c in codes[:-1]) else "medium"
            out.append(F("geo_redirect", sev, "international",
                         f"Besökare med profil '{g.profile}' skickas från {g.path} till {loc or g.final_url}",
                         url=site.base_url + g.path, evidence={"codes": codes, "final_url": g.final_url, "profile": g.profile}))
    return out


def check_onpage(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    out = []
    t = site.thresholds
    titles = defaultdict(list)
    descs = defaultdict(list)
    for cu in cr.urls.values():
        f = cu.facts
        if not f or not _indexable(cu):
            continue
        n_h1 = len(f.h1)
        if f.page_type in CONTENT_TYPES_NEEDING_H1:
            if n_h1 == 0:
                out.append(F("missing_h1", "high", "onpage", f"Ingen H1 ({f.page_type})", url=cu.url, evidence={"page_type": f.page_type}))
            elif n_h1 > 1:
                out.append(F("multiple_h1", "medium", "onpage", f"{n_h1} H1 på samma sida ({f.page_type})",
                             url=cu.url, evidence={"h1": f.h1[:6], "page_type": f.page_type}))
        if not f.title:
            out.append(F("missing_title", "high", "onpage", "Titel saknas", url=cu.url))
        else:
            titles[f.title.strip().lower()].append(cu.url)
            if len(f.title) > t.title_max:
                out.append(F("title_too_long", "low", "onpage", f"Titeln är {len(f.title)} tecken", url=cu.url, evidence={"title": f.title}))
            elif len(f.title) < t.title_min:
                out.append(F("title_too_short", "low", "onpage", f"Titeln är bara {len(f.title)} tecken", url=cu.url, evidence={"title": f.title}))
        if not f.meta_description:
            out.append(F("missing_meta_description", "low", "onpage", "Metabeskrivning saknas", url=cu.url))
        else:
            descs[f.meta_description.strip().lower()].append(cu.url)
            if len(f.meta_description) > t.description_max:
                out.append(F("meta_description_too_long", "info", "onpage", f"Metabeskrivningen är {len(f.meta_description)} tecken", url=cu.url))
        if not f.canonical:
            out.append(F("missing_canonical", "medium", "onpage", "Canonical saknas", url=cu.url))
    for title, urls in titles.items():
        if len(urls) > 1:
            out.append(F("duplicate_title", "medium", "onpage", f"Samma titel på {len(urls)} sidor",
                         url=urls[0], evidence={"title": title, "urls": urls[:20], "count": len(urls)}))
    for desc, urls in descs.items():
        if len(urls) > 1:
            out.append(F("duplicate_meta_description", "low", "onpage", f"Samma metabeskrivning på {len(urls)} sidor",
                         url=urls[0], evidence={"urls": urls[:20], "count": len(urls)}))
    return out


def _bare(host: str) -> str:
    """Värdnamn utan inledande www, så att bestofsports.fi och www.bestofsports.fi räknas som samma domän."""
    host = host.lower()
    return host[4:] if host.startswith("www.") else host


def check_canonicals(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    out = []
    for cu in cr.urls.values():
        f = cu.facts
        if not f or not f.canonical or cu.status != 200:
            continue
        canon = normalize_url(f.canonical)
        if _bare(urlsplit(canon).netloc) != _bare(site.host):
            out.append(F("canonical_offsite", "high", "indexing", "Canonical pekar på en annan domän", url=cu.url, evidence={"canonical": canon}))
            continue
        target = cr.urls.get(canon)
        if target and (target.status != 200 or target.redirect_count):
            out.append(F("canonical_not_ok", "high", "indexing",
                         f"Canonical pekar på en URL som ger {target.status}{' via omdirigering' if target.redirect_count else ''}",
                         url=cu.url, evidence={"canonical": canon}))
    return out


def check_hreflang(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    out = []
    t = site.thresholds
    variant_counts = []
    for cu in cr.urls.values():
        f = cu.facts
        if not f or not f.hreflang or not _indexable(cu):
            continue
        variant_counts.append(len(f.hreflang))
        self_ref = any(normalize_url(u) == normalize_url(cu.final_url) for u in f.hreflang.values())
        if not self_ref:
            out.append(F("hreflang_no_self", "medium", "international", "hreflang saknar självreferens", url=cu.url))
        if "x-default" not in f.hreflang:
            out.append(F("hreflang_no_xdefault", "low", "international", "hreflang saknar x-default", url=cu.url))
        for lang, href in f.hreflang.items():
            target = cr.urls.get(normalize_url(href))
            if target is None:
                continue
            if target.status != 200 or target.redirect_count:
                out.append(F("hreflang_bad_target", "high", "international",
                             f"hreflang {lang} pekar på en URL som ger {target.status}{' (omdirigering)' if target.redirect_count else ''}",
                             url=cu.url, evidence={"hreflang": lang, "target": href}))
            elif target.facts and target.facts.hreflang and not any(
                normalize_url(u) == normalize_url(cu.final_url) for u in target.facts.hreflang.values()
            ):
                out.append(F("hreflang_not_reciprocal", "medium", "international",
                             f"hreflang {lang} länkar inte tillbaka", url=cu.url, evidence={"target": href}))
    if variant_counts:
        mx = max(variant_counts)
        if mx >= t.hreflang_variants_warn:
            out.append(F("hreflang_many_variants", "medium", "international",
                         f"Upp till {mx} hreflang-varianter per sida", url=site.base_url,
                         evidence={"max": mx, "median": sorted(variant_counts)[len(variant_counts) // 2]}))
    return out


def check_language(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    """Upptäcker halvöversatta sidor: språkprefix eller html-lang stämmer inte med texten."""
    out = []
    by_locale: dict[str, list[str]] = defaultdict(list)
    for cu in cr.urls.values():
        f = cu.facts
        if not f or not _indexable(cu) or f.word_count < 80:
            continue
        expected = locale_language(f.locale_prefix) or locale_language(f.html_lang) or locale_language(site.primary_locale)
        if not expected or not f.detected_language:
            continue
        if f.detected_language != expected and f.language_share >= 0.5:
            by_locale[f.locale_prefix or "rot"].append(cu.url)
            out.append(F("language_mismatch", "medium", "international",
                         f"Sidan ska vara på '{expected}' men texten är mest '{f.detected_language}'",
                         url=cu.url, evidence={"expected": expected, "detected": f.detected_language, "share": round(f.language_share, 2)}))
        if f.html_lang and f.locale_prefix and locale_language(f.html_lang) != locale_language(f.locale_prefix):
            out.append(F("html_lang_mismatch", "low", "international",
                         f"html lang='{f.html_lang}' men URL-prefix '{f.locale_prefix}'", url=cu.url))
    locales = {cu.facts.locale_prefix for cu in cr.urls.values() if cu.facts and cu.facts.locale_prefix}
    if locales:
        out.append(F("locale_inventory", "info", "international", f"{len(locales)} språk-/marknadsprefix i crawlen",
                     url=site.base_url, evidence={"locales": sorted(locales), "mismatched_pages": {k: len(v) for k, v in by_locale.items()}}))
    return out


def check_schema(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    out = []
    org_types_seen = set()
    for cu in cr.urls.values():
        f = cu.facts
        if not f or cu.status != 200:
            continue
        org_types_seen.update(f.jsonld_types)
        if f.jsonld_errors:
            out.append(F("jsonld_invalid", "high", "schema", f"{f.jsonld_errors} JSON-LD-block går inte att tolka", url=cu.url))
        if f.page_type == "product":
            if not f.product_schema:
                out.append(F("product_schema_missing", "high", "schema", "Produktsida utan Product-schema", url=cu.url))
            nodes = f.product_schema
            complete = [p for p in nodes if p["images"] and p["has_offers"]]
            if complete and len(nodes) > len(complete):
                # Omdömesappar skriver ofta en egen Product-nod (bara aggregateRating och review) vid sidan av temats fullständiga.
                # Den noden ska inte bedömas som en produkt utan bild och pris, men Google kan behandla den som en separat produkt.
                out.append(F("product_schema_extra_node", "info", "schema",
                             f"{len(nodes) - len(complete)} extra Product-nod utan bild och pris (troligen omdömesapp), kopplas inte till produkten",
                             url=cu.url))
                nodes = complete
            for p in nodes:
                if not p["images"]:
                    out.append(F("product_schema_no_image", "high", "schema", "Product-schemat saknar bild", url=cu.url))
                elif p.get("relative_images") and not p["invalid_images"]:
                    out.append(F("product_schema_relative_image", "low", "schema",
                                 "Bild-URL i Product-schemat saknar https: (protokollrelativ)",
                                 url=cu.url, evidence={"images": p["relative_images"][:2]}))
                elif p["invalid_images"]:
                    out.append(F("product_schema_bad_image", "high", "schema", "Trasig bild-URL i Product-schemat",
                                 url=cu.url, evidence={"images": p["invalid_images"][:3]}))
                if not p["has_offers"]:
                    out.append(F("product_schema_no_offers", "medium", "schema", "Product-schemat saknar offers/pris", url=cu.url))
                if not p["has_brand"]:
                    out.append(F("product_schema_no_brand", "low", "schema", "Product-schemat saknar brand", url=cu.url))
                if "has_rating" in p and not p["has_rating"]:
                    out.append(F("product_schema_no_rating", "info", "schema",
                                 "Product-schemat saknar aggregateRating (inga omdömen i strukturerad data)", url=cu.url))
        if f.page_type in ("product", "collection", "article") and not f.has_breadcrumb_schema and _indexable(cu):
            out.append(F("breadcrumb_schema_missing", "low", "schema", f"BreadcrumbList saknas ({f.page_type})", url=cu.url))
    expected = set(site.expected_org_schema)
    if expected and not (org_types_seen & expected):
        out.append(F("org_schema_missing", "medium", "schema",
                     f"Inget av de förväntade schematyperna hittades: {', '.join(sorted(expected))}",
                     url=site.base_url, evidence={"types_seen": sorted(org_types_seen)[:40]}))
    return out


def check_media(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    out = []
    for cu in cr.urls.values():
        f = cu.facts
        if not f or not _indexable(cu):
            continue
        if f.images_missing_alt and f.images_total:
            share = f.images_missing_alt / f.images_total
            sev = "medium" if f.page_type == "product" and share > 0.5 else "low"
            out.append(F("images_missing_alt", sev, "media", f"{f.images_missing_alt} av {f.images_total} bilder saknar alt-text",
                         url=cu.url, evidence={"missing": f.images_missing_alt, "total": f.images_total, "page_type": f.page_type}))
        if f.insecure_resources:
            out.append(F("insecure_resources", "medium", "media", f"{f.insecure_resources} resurser laddas över http://", url=cu.url))
    return out


def check_performance(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    out = []
    t = site.thresholds
    sizes = []
    big_scripts: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for cu in cr.urls.values():
        f = cu.facts
        if not f:
            continue
        sizes.append(f.html_bytes)
        if f.html_bytes >= t.html_bytes_warn:
            out.append(F("html_too_large", "medium", "performance", f"HTML är {f.html_bytes / 1_000_000:.2f} MB",
                         url=cu.url, evidence={"bytes": f.html_bytes, "page_type": f.page_type}))
        if f.largest_inline_script >= t.inline_script_bytes_warn:
            big_scripts[(f.largest_inline_script_hint or "")[:60]].append((cu.url, f.largest_inline_script))
    for hint, pages in big_scripts.items():
        if len(pages) >= 10:
            kb = max(b for _, b in pages) // 1000
            out.append(F("large_inline_script_sitewide", "medium", "performance",
                         f"Samma inline-skript (upp till {kb} KB) på {len(pages)} sidor – tema eller app, åtgärdas på ett ställe",
                         url=pages[0][0], evidence={"pages": len(pages), "starts_with": hint, "sample": [u for u, _ in pages[:10]], "count": len(pages)}))
        else:
            for url, b in pages:
                out.append(F("large_inline_script", "medium", "performance", f"Inline-skript på {b // 1000} KB", url=url,
                             evidence={"bytes": b, "starts_with": hint}))
    if sizes:
        sizes.sort()
        out.append(F("html_size_stats", "info", "performance",
                     f"HTML-storlek: median {sizes[len(sizes)//2] / 1_000_000:.2f} MB, max {sizes[-1] / 1_000_000:.2f} MB",
                     url=site.base_url, evidence={"min": sizes[0], "median": sizes[len(sizes)//2], "max": sizes[-1], "pages": len(sizes)}))
    return out


def check_content(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    out = []
    t = site.thresholds
    by_fp: dict[str, list[str]] = defaultdict(list)
    current_year = date.today().year
    misspell_total: dict[str, list[str]] = defaultdict(list)
    for cu in cr.urls.values():
        f = cu.facts
        if not f or not _indexable(cu):
            continue
        if f.text_fingerprint:
            by_fp[f.text_fingerprint].append(cu.url)
        if f.page_type in ("page", "article", "collection", "blog") and f.word_count < t.thin_words:
            out.append(F("thin_content", "low", "content", f"Tunt innehåll ({f.word_count} ord)", url=cu.url,
                         evidence={"words": f.word_count, "page_type": f.page_type}))
        hay = f"{f.title or ''} {urlsplit(cu.url).path}"
        if TEST_PAGE_RE.search(hay):
            out.append(F("test_or_draft_page", "medium", "content", "Ser ut som en test-, kopia- eller utkastsida",
                         url=cu.url, evidence={"title": f.title}))
        if f.page_type in ("page", "article", "collection"):
            years = [int(y) for y in YEAR_RE.findall(hay)]
            if years and max(years) < current_year - 1:
                out.append(F("outdated_page", "low", "content", f"Sidan verkar gälla {max(years)} (gammalt event/kampanj)",
                             url=cu.url, evidence={"title": f.title}))
        if site.brand_terms and f.title:
            for w in find_misspellings(f"{f.title} {f.meta_description or ''} {' '.join(f.h1)}", site.brand_terms, site.known_misspellings):
                misspell_total[w].append(cu.url)
    for fp, urls in by_fp.items():
        if len(urls) > 1:
            out.append(F("duplicate_content", "medium", "content", f"Identiskt innehåll på {len(urls)} indexerbara sidor",
                         url=urls[0], evidence={"urls": urls[:20], "count": len(urls)}))
    for word, urls in misspell_total.items():
        out.append(F("brand_misspelling", "medium", "content", f"Felstavat varumärke '{word}' i titel/rubrik",
                     url=urls[0], evidence={"urls": urls[:20], "count": len(urls)}))
    return out


def check_structure(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    """Inventering (sidtyp × språk) och föräldralösa sidor. Alla sitemap-URL:er crawlas och deras
    länkar registreras, så en sitemap-sida som ingen annan sida länkar till är verkligen oländad."""
    out = []
    matrix: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for cu in cr.urls.values():
        if cu.facts and cu.status == 200 and not cu.redirect_count:
            matrix[cu.facts.page_type][cu.facts.locale_prefix or "standard"] += 1
    if matrix:
        total = sum(sum(v.values()) for v in matrix.values())
        out.append(F("inventory", "info", "content", f"{total} levande sidor fördelade på {len(matrix)} sidtyper",
                     url=site.base_url, evidence={k: dict(v) for k, v in sorted(matrix.items())}))
    for cu in cr.urls.values():
        if cu.in_sitemap and cu.status == 200 and not cu.redirect_count and cu.facts and not cu.linked_from \
                and cu.facts.page_type in ("product", "collection", "page", "article", "blog"):
            out.append(F("orphan_page", "low", "links", f"Ingen intern länk pekar hit ({cu.facts.page_type})",
                         url=cu.url, evidence={"page_type": cu.facts.page_type}))
    return out


def blocks_all(robots: str, agents: tuple[str, ...]) -> bool:
    """Sant om någon av agenternas grupper har 'Disallow: /'. Shopify blockerar t.ex. Nutch
    helt som standard, vilket inte ska räknas."""
    groups: list[tuple[set[str], list[str]]] = []
    current_agents: set[str] = set()
    rules: list[str] = []
    last_was_agent = False
    for raw in robots.splitlines():
        line = raw.split("#")[0].strip()
        if not line or ":" not in line:
            continue
        key, value = (x.strip() for x in line.split(":", 1))
        key = key.lower()
        if key == "user-agent":
            if not last_was_agent and current_agents:
                groups.append((current_agents, rules))
                current_agents, rules = set(), []
            current_agents.add(value.lower())
            last_was_agent = True
        else:
            if key == "disallow":
                rules.append(value)
            last_was_agent = False
    if current_agents:
        groups.append((current_agents, rules))
    return any(set(agents) & ua and "/" in r for ua, r in groups)


def check_shopify_specifics(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    out = []
    # Produkter nåbara via /collections/x/products/y ska ha canonical till /products/y.
    for cu in cr.urls.values():
        f = cu.facts
        if not f or cu.status != 200:
            continue
        _, rest = split_locale(f.path)
        m = re.match(r"^/collections/[^/]+/products/([^/]+)", rest)
        if m and (not f.canonical or "/collections/" in urlsplit(f.canonical).path):
            out.append(F("collection_product_url_indexable", "medium", "indexing",
                         "Produkt-URL under kollektion saknar canonical till /products/", url=cu.url,
                         evidence={"canonical": f.canonical}))
        if "page=" in urlsplit(cu.url).query and f.canonical and normalize_url(f.canonical) == normalize_url(cu.url) and cu.in_sitemap:
            out.append(F("paginated_in_sitemap", "low", "indexing", "Paginerad URL i sitemapen", url=cu.url))
    # robots.txt
    robots = cr.robots_txt
    if robots is None:
        out.append(F("robots_missing", "medium", "indexing", "robots.txt kunde inte hämtas", url=site.base_url + "/robots.txt"))
    else:
        low = robots.lower()
        if "sitemap:" not in low:
            out.append(F("robots_no_sitemap", "low", "indexing", "robots.txt anger ingen sitemap", url=site.base_url + "/robots.txt"))
        if blocks_all(robots, ("*", "googlebot")):
            out.append(F("robots_blocks_all", "critical", "indexing", "robots.txt blockerar hela sajten", url=site.base_url + "/robots.txt"))
        out.extend(check_ai_crawlers(robots, site))
    return out


# AI-tjänsternas läs- och träningsbotar. Att blockera dem är ett val, inte ett fel: blockerade botar kan inte läsa sajten för
# att svara på frågor (GEO), men sajten kan vilja skydda innehållet. Därför bara info, så att valet är medvetet.
AI_BOTS = ("gptbot", "chatgpt-user", "oai-searchbot", "claudebot", "claude-web", "anthropic-ai", "perplexitybot",
           "google-extended", "ccbot", "applebot-extended", "bytespider")


def check_ai_crawlers(robots: str, site: SiteConfig) -> list[Finding]:
    blocked = [b for b in AI_BOTS if blocks_all(robots, (b,))]
    url = site.base_url + "/robots.txt"
    if blocked:
        return [F("ai_crawlers_blocked", "info", "indexing", f"robots.txt blockerar AI-botar: {', '.join(blocked)}", url=url,
                  evidence={"blocked": blocked, "allowed": [b for b in AI_BOTS if b not in blocked]})]
    return [F("ai_crawlers_allowed", "info", "indexing", "robots.txt blockerar inga kända AI-botar (sajten kan läsas av AI-tjänster)", url=url,
              evidence={"checked": list(AI_BOTS)})]


SEARCH_PARAMS = ("_pos", "_psq", "_ss", "_sid", "_v", "_fid", "pr_prod_strat", "pr_rec_id", "pr_rec_pid", "pr_ref_pid", "pr_seq")


def check_link_hygiene(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    """Interna länkar med söknings- och rekommendationsparametrar (?_pos=2&_psq=...) i stället för rena adresser.

    Parametrarna ger dubbla adresser att crawla och gör att rapporter räknar samma sida flera gånger. En fil per sida räknas,
    inte varje länk, och exemplen visar vilken sida som länkar."""
    pages: dict[str, list[str]] = defaultdict(list)
    for cu in cr.urls.values():
        f = cu.facts
        if not f or cu.status != 200:
            continue
        for link in f.internal_links:
            q = urlsplit(link).query
            if q and any(f"{k}=" in q for k in SEARCH_PARAMS):
                pages[cu.url].append(link)
    out = []
    if pages:
        total = sum(len(v) for v in pages.values())
        sample = sorted(pages)[:5]
        out.append(F("internal_links_tracking_params", "medium", "links",
                     f"{total} interna länkar på {len(pages)} sidor har söknings- eller rekommendationsparametrar",
                     url=site.base_url, evidence={"pages_sample": sample, "link_sample": pages[sample[0]][:3]}))
    return out


ALL_CRAWL_CHECKS = [check_structure, check_shopify_specifics, check_status, check_redirects, check_geo, check_onpage, check_canonicals, check_hreflang,
                    check_language, check_schema, check_media, check_performance, check_content, check_link_hygiene]

from .seo_depth_checks import SEO_DEPTH_CHECKS  # noqa: E402 - importeras efter _indexable, som kontrollerna använder

ALL_CRAWL_CHECKS += SEO_DEPTH_CHECKS


def run_crawl_checks(cr: CrawlResult, site: SiteConfig) -> list[Finding]:
    out: list[Finding] = []
    for check in ALL_CRAWL_CHECKS:
        out.extend(check(cr, site))
    return out
