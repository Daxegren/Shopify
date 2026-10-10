"""Kontroller som kombinerar crawl och admin-data."""

from __future__ import annotations

import re
from urllib.parse import urlsplit

from ..config import SiteConfig
from ..crawler import CrawlResult, normalize_url
from ..findings import Finding
from ..html_parse import split_locale
from ..shopify_admin import AdminData

F = Finding
STOP_TOKENS = {"the", "and", "of", "och", "i", "a", "en", "collection", "collections", "products", "pages", "kollektion"}


def _slug_tokens(path: str) -> list[str]:
    _, rest = split_locale(path)
    last = rest.rstrip("/").split("/")[-1]
    return [t for t in re.split(r"[-_]+", last.lower()) if t and not t.isdigit() and t not in STOP_TOKENS]


def _distinct_terms(a: list[str], b: list[str]) -> tuple[set[str], set[str]]:
    """Tar bort gemensamt prefix ('konstnar-anna' vs 'konstnar-per' -> {anna} vs {per})."""
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]:
        i += 1
    return set(a[i:]), set(b[i:])


def _section(path: str) -> str:
    _, rest = split_locale(path)
    parts = rest.strip("/").split("/")
    return parts[0] if parts else ""


def check_redirect_targets(cr: CrawlResult, admin: AdminData, site: SiteConfig) -> list[Finding]:
    out = []
    for r in admin.redirects:
        src = r["path"]
        tgt_path = urlsplit(r["target"]).path or r["target"]
        ta, tb = _slug_tokens(src), _slug_tokens(tgt_path)
        a, b = _distinct_terms(ta, tb)
        if len(ta) >= 2 and len(tb) >= 2 and a and b and _section(src) == _section(tgt_path) and not (a & b):
            out.append(F("redirect_target_mismatch", "medium", "redirects",
                         "Omdirigeringens mål verkar handla om något annat (ingen gemensam term i adressen)",
                         url=site.base_url + src, resource=r["id"], evidence={"target": r["target"], "source_terms": sorted(a), "target_terms": sorted(b)}))
        crawled = cr.urls.get(normalize_url(site.base_url + src))
        if crawled and crawled.redirect_count == 0 and crawled.status == 200:
            out.append(F("redirect_shadowed", "low", "redirects",
                         "Omdirigeringen används inte eftersom sidan själv finns (sidan har företräde)",
                         url=site.base_url + src, resource=r["id"]))
    return out


def check_empty_collections_indexed(cr: CrawlResult, admin: AdminData, site: SiteConfig) -> list[Finding]:
    out = []
    in_sitemap = {urlsplit(u).path.rstrip("/") for u, cu in cr.urls.items() if cu.in_sitemap}
    for c in admin.collections:
        if (c.get("productsCount") or {}).get("count", 0) == 0:
            path = f"/collections/{c['handle']}"
            hits = [p for p in in_sitemap if split_locale(p)[1] == path]
            if hits:
                out.append(F("empty_collection_in_sitemap", "high", "indexing",
                             f"Tom kollektion ligger i sitemapen ({len(hits)} språkversioner)",
                             url=site.base_url + path, resource=c["id"], evidence={"paths": hits[:10]}))
    return out


def check_sitemap_vs_admin(cr: CrawlResult, admin: AdminData, site: SiteConfig) -> list[Finding]:
    """Förklarar 404 i sitemapen: finns handlen alls i admin, och i så fall med vilken status?"""
    out = []
    products = {p["handle"]: p for p in admin.products}
    collections = {c["handle"]: c for c in admin.collections}
    pages = {p["handle"]: p for p in admin.pages}
    for cu in cr.urls.values():
        if not cu.in_sitemap or cu.status < 400:
            continue
        _, rest = split_locale(urlsplit(cu.url).path)
        m = re.match(r"^/(products|collections|pages)/([^/]+)$", rest.rstrip("/"))
        if not m:
            continue
        kind, handle = m.groups()
        obj = {"products": products, "collections": collections, "pages": pages}[kind].get(handle)
        if obj is None:
            reason = "finns inte i admin (borttagen eller bytt handle)"
        elif kind == "products" and obj.get("status") != "ACTIVE":
            reason = f"produkten har status {obj.get('status')}"
        elif kind == "pages" and not obj.get("isPublished"):
            reason = "sidan är inte publicerad"
        else:
            reason = "finns i admin men svarar ändå fel (marknad/språk saknas?)"
        out.append(F("sitemap_error_explained", "info", "indexing", f"Orsak till {cu.status}: {reason}",
                     url=cu.url, evidence={"kind": kind, "handle": handle}))
    return out


ALL_CROSS_CHECKS = [check_redirect_targets, check_empty_collections_indexed, check_sitemap_vs_admin]


def run_cross_checks(cr: CrawlResult, admin: AdminData, site: SiteConfig) -> list[Finding]:
    out: list[Finding] = []
    for check in ALL_CROSS_CHECKS:
        out.extend(check(cr, admin, site))
    return out
