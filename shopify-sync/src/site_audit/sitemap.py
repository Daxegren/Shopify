"""Läser sitemap-index och undersitemaps (Shopify: /sitemap.xml -> sitemap_products_1.xml osv.)."""

from __future__ import annotations

import logging
import xml.etree.ElementTree as ET
from dataclasses import dataclass

from .fetch import Fetcher

log = logging.getLogger(__name__)

NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9", "xhtml": "http://www.w3.org/1999/xhtml"}


@dataclass
class SitemapEntry:
    url: str
    sitemap: str
    lastmod: str | None = None
    alternates: dict[str, str] | None = None  # hreflang -> url


@dataclass
class SitemapResult:
    entries: list[SitemapEntry]
    sitemaps: list[str]
    errors: list[tuple[str, str]]  # (sitemap-url, fel)


def _parse(xml: bytes):
    try:
        return ET.fromstring(xml)
    except ET.ParseError:
        return None


def read_sitemaps(fetcher: Fetcher, root_url: str, max_sitemaps: int = 500) -> SitemapResult:
    queue = [root_url]
    seen: set[str] = set()
    entries: list[SitemapEntry] = []
    errors: list[tuple[str, str]] = []
    while queue and len(seen) < max_sitemaps:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        res = fetcher.fetch(url)
        if res.status != 200:
            errors.append((url, f"HTTP {res.status or res.error}"))
            continue
        root = _parse(res.body)
        if root is None:
            errors.append((url, "ogiltig XML"))
            continue
        tag = root.tag.split("}")[-1]
        if tag == "sitemapindex":
            for loc in root.findall("sm:sitemap/sm:loc", NS):
                if loc.text:
                    queue.append(loc.text.strip())
        elif tag == "urlset":
            for node in root.findall("sm:url", NS):
                loc = node.find("sm:loc", NS)
                if loc is None or not loc.text:
                    continue
                lastmod = node.find("sm:lastmod", NS)
                alts = {
                    link.get("hreflang"): link.get("href")
                    for link in node.findall("xhtml:link", NS)
                    if link.get("rel") == "alternate" and link.get("hreflang")
                }
                entries.append(SitemapEntry(loc.text.strip(), url, lastmod.text.strip() if lastmod is not None and lastmod.text else None, alts or None))
        else:
            errors.append((url, f"okänt rotelement {tag}"))
    return SitemapResult(entries, sorted(seen), errors)
