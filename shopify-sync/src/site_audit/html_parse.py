"""Plockar ut SEO-relevanta fakta ur en HTML-sida."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from typing import Any
from urllib.parse import urljoin, urlsplit

from bs4 import BeautifulSoup

from .textutil import fingerprint, guess_language, words

LOCALE_PREFIX_RE = re.compile(r"^/([a-z]{2}(?:-[a-z]{2,4})?)(?=/|$)", re.I)
NON_LOCALE_SEGMENTS = {"products", "collections", "pages", "blogs", "search", "cart", "account", "apps", "tools", "policies"}


def split_locale(path: str) -> tuple[str | None, str]:
    """'/sv/products/x' -> ('sv', '/products/x'). Shopify-språkprefix är 2 bokstäver eller sv-se."""
    m = LOCALE_PREFIX_RE.match(path)
    if m and m.group(1).lower() not in NON_LOCALE_SEGMENTS:
        rest = path[m.end():] or "/"
        return m.group(1).lower(), rest
    return None, path or "/"


def page_type(path: str) -> str:
    _, p = split_locale(path)
    p = p.rstrip("/") or "/"
    if p == "/":
        return "home"
    if re.match(r"^/collections/[^/]+/products/", p) or p.startswith("/products/"):
        return "product"
    if p == "/collections" or p == "/collections/all":
        return "collection_list" if p == "/collections" else "collection"
    if p.startswith("/collections/"):
        return "collection"
    if p.startswith("/pages/"):
        return "page"
    if re.match(r"^/blogs/[^/]+/[^/]+", p):
        return "article"
    if p.startswith("/blogs/"):
        return "blog"
    if p.startswith("/policies/"):
        return "policy"
    if p.startswith("/search"):
        return "search"
    return "other"


@dataclass
class PageFacts:
    url: str
    path: str
    locale_prefix: str | None
    page_type: str
    html_bytes: int = 0
    title: str | None = None
    meta_description: str | None = None
    meta_robots: str | None = None
    canonical: str | None = None
    html_lang: str | None = None
    h1: list[str] = field(default_factory=list)
    hreflang: dict[str, str] = field(default_factory=dict)
    jsonld_types: list[str] = field(default_factory=list)
    jsonld_errors: int = 0
    product_schema: list[dict[str, Any]] = field(default_factory=list)
    has_breadcrumb_schema: bool = False
    images_total: int = 0
    images_missing_alt: int = 0
    insecure_resources: int = 0
    inline_script_bytes: int = 0
    largest_inline_script: int = 0
    largest_inline_script_hint: str | None = None
    external_script_hosts: list[str] = field(default_factory=list)
    word_count: int = 0
    text_fingerprint: str | None = None
    detected_language: str | None = None
    language_share: float = 0.0
    internal_links: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d.pop("internal_links")
        return d


def _jsonld_items(data: Any):
    if isinstance(data, list):
        for x in data:
            yield from _jsonld_items(x)
    elif isinstance(data, dict):
        if "@graph" in data:
            yield from _jsonld_items(data["@graph"])
        yield data


def _types(item: dict) -> list[str]:
    t = item.get("@type")
    if isinstance(t, list):
        return [str(x) for x in t]
    return [str(t)] if t else []


def _image_urls(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [u for v in value for u in _image_urls(v)]
    if isinstance(value, dict):
        return _image_urls(value.get("url") or value.get("contentUrl"))
    return []


def valid_absolute_url(u: str) -> bool:
    if not u or "{{" in u or "{%" in u or " " in u.strip():
        return False
    parts = urlsplit(u)
    return parts.scheme in ("http", "https") and bool(parts.netloc) and "." in parts.netloc


def parse_page(url: str, html: bytes, site_host: str) -> PageFacts:
    parts = urlsplit(url)
    locale, _ = split_locale(parts.path)
    facts = PageFacts(url=url, path=parts.path or "/", locale_prefix=locale,
                      page_type=page_type(parts.path or "/"), html_bytes=len(html))
    soup = BeautifulSoup(html, "html.parser")

    if soup.html and soup.html.get("lang"):
        facts.html_lang = soup.html.get("lang").strip().lower()
    if soup.title and soup.title.string:
        facts.title = soup.title.string.strip()
    for meta in soup.find_all("meta"):
        name = (meta.get("name") or "").lower()
        if name == "description":
            facts.meta_description = (meta.get("content") or "").strip()
        elif name == "robots":
            facts.meta_robots = (meta.get("content") or "").strip().lower()
    for link in soup.find_all("link", href=True):
        rel = [r.lower() for r in (link.get("rel") or [])]
        if "canonical" in rel:
            facts.canonical = urljoin(url, link["href"])
        elif "alternate" in rel and link.get("hreflang"):
            facts.hreflang[link["hreflang"].lower()] = urljoin(url, link["href"])
    facts.h1 = [h.get_text(" ", strip=True) for h in soup.find_all("h1")]

    # Strukturerad data
    for script in soup.find_all("script", type="application/ld+json"):
        raw = script.string or script.get_text()
        try:
            data = json.loads(raw)
        except (json.JSONDecodeError, TypeError):
            facts.jsonld_errors += 1
            continue
        for item in _jsonld_items(data):
            types = _types(item)
            facts.jsonld_types.extend(types)
            if "BreadcrumbList" in types:
                facts.has_breadcrumb_schema = True
            if "Product" in types or "ProductGroup" in types:
                imgs = _image_urls(item.get("image"))
                offers = item.get("offers") or (item.get("hasVariant") and [v.get("offers") for v in item["hasVariant"] if isinstance(v, dict)])
                facts.product_schema.append({
                    "name": item.get("name"),
                    "images": imgs,
                    "invalid_images": [u for u in imgs if not valid_absolute_url(u)],
                    "has_offers": bool(offers),
                    "has_brand": bool(item.get("brand")),
                    "has_sku": bool(item.get("sku")),
                })
    facts.jsonld_types = sorted(set(facts.jsonld_types))

    # Bilder
    for img in soup.find_all("img"):
        facts.images_total += 1
        alt = img.get("alt")
        if alt is None or not alt.strip():
            facts.images_missing_alt += 1
        src = img.get("src") or ""
        if src.startswith("http://"):
            facts.insecure_resources += 1

    # Skript
    hosts = set()
    for script in soup.find_all("script"):
        src = script.get("src")
        if src:
            host = urlsplit(urljoin(url, src)).netloc.lower()
            if host and host != site_host:
                hosts.add(host)
            if src.startswith("http://"):
                facts.insecure_resources += 1
            continue
        if (script.get("type") or "").lower() == "application/ld+json":
            continue
        body = script.string or script.get_text() or ""
        size = len(body.encode())
        facts.inline_script_bytes += size
        if size > facts.largest_inline_script:
            facts.largest_inline_script = size
            facts.largest_inline_script_hint = re.sub(r"\s+", " ", body[:120]).strip()
    facts.external_script_hosts = sorted(hosts)

    # Länkar
    links = set()
    for a in soup.find_all("a", href=True):
        href = urljoin(url, a["href"].split("#")[0])
        p = urlsplit(href)
        if p.scheme in ("http", "https") and p.netloc.lower() == site_host:
            links.add(p._replace(fragment="").geturl())
    facts.internal_links = sorted(links)

    # Huvudtext: ta bort sidhuvud, sidfot, navigering och skript
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "svg", "form"]):
        tag.decompose()
    main = soup.find("main") or soup.body or soup
    text = main.get_text(" ", strip=True)
    facts.word_count = len(words(text))
    facts.text_fingerprint = fingerprint(text) if facts.word_count >= 20 else None
    facts.detected_language, facts.language_share = guess_language(text)
    return facts


def is_noindex(facts: PageFacts, headers: dict[str, str] | None = None) -> bool:
    robots = (facts.meta_robots or "") + " " + ((headers or {}).get("x-robots-tag", "").lower())
    return "noindex" in robots
