"""Plockar ut SEO-relevanta fakta ur en HTML-sida."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from typing import Any
from urllib.parse import unquote, urljoin, urlsplit

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
    images_no_dimensions: int = 0       # <img> utan width och height (risk för layoutförskjutning, CLS)
    images_no_lazy: int = 0             # bilder efter de två första som saknar loading="lazy"
    malformed_hrefs: list[str] = field(default_factory=list)   # länkadresser med mallkod eller HTML i (t.ex. {{ shop_url }})
    product_link_count: int = 0         # unika produkter som länkas på sidan (kategorier: antal produkter i listan)
    consent_platforms: list[str] = field(default_factory=list)  # samtyckeslösningar som syns i HTML
    analytics_ids: list[str] = field(default_factory=list)      # G-, GTM-, AW-, UA- och Meta-pixel-id:n i HTML
    consent_mode_default: bool = False  # gtag('consent','default', ...) finns i HTML
    consent_mode_v2: bool = False       # ... med ad_user_data och ad_personalization

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d.pop("internal_links")
        return d


_MALFORMED_HREF = re.compile(r"\{\{|\}\}|\{%|<|>|&lt;|&gt;|notranslate", re.I)


def is_malformed_href(raw: str) -> bool:
    """Adress med mallkod eller HTML i sig (till exempel href="<span class='notranslate'>{{ shop_url }}</span>")."""
    return bool(_MALFORMED_HREF.search(unquote(raw)))


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


def _currencies(offers: Any) -> set[str]:
    """priceCurrency ur erbjudanden (en, flera eller en lista med listor för produktgrupper)."""
    out: set[str] = set()
    if isinstance(offers, dict):
        if offers.get("priceCurrency"):
            out.add(str(offers["priceCurrency"]).upper())
        for key in ("offers", "priceSpecification"):
            if key in offers:
                out |= _currencies(offers[key])
    elif isinstance(offers, list):
        for o in offers:
            out |= _currencies(o)
    return out


def _image_urls(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [u for v in value for u in _image_urls(v)]
    if isinstance(value, dict):
        return _image_urls(value.get("url") or value.get("contentUrl"))
    return []


def _protocol_relative(u: str) -> bool:
    """'//www.butik.se/cdn/...' fungerar, men Google rekommenderar absoluta URL:er."""
    return isinstance(u, str) and u.startswith("//") and valid_absolute_url("https:" + u)


def valid_absolute_url(u: str) -> bool:
    if not u or "{{" in u or "{%" in u or " " in u.strip():
        return False
    parts = urlsplit(u)
    return parts.scheme in ("http", "https") and bool(parts.netloc) and "." in parts.netloc


CMP_SIGNATURES = {
    "cookiebot": r"cookiebot", "onetrust": r"cookielaw\.org|onetrust", "usercentrics": r"usercentrics",
    "iubenda": r"iubenda", "cookieyes": r"cookieyes", "consentmanager": r"consentmanager\.net", "osano": r"osano\.com",
    "termly": r"termly\.io", "trustarc": r"trustarc", "pandectes": r"pandectes", "complianz": r"complianz",
    "shopify_privacy": r"customerPrivacy|consent-tracking-api|privacy-banner",
}
ANALYTICS_ID_RE = re.compile(r"\b(G-[A-Z0-9]{6,12}|GTM-[A-Z0-9]{4,8}|AW-\d{6,12}|UA-\d{4,10}-\d{1,3})\b")
FB_PIXEL_RE = re.compile(r"fbq\(\s*['\"]init['\"]\s*,\s*['\"]?(\d{8,20})")
CONSENT_DEFAULT_RE = re.compile(r"""['"]consent['"]\s*,\s*['"]default['"]""")


def detect_tracking(text: str) -> tuple[list[str], list[str], bool, bool]:
    """Samtyckeslösningar, analys-id:n och Consent Mode i den råa HTML-texten. Observera att Shopifys egen cookiebanner och
    webbpixlar (Customer Events) laddas av JavaScript och syns normalt inte här."""
    cmps = sorted(k for k, pat in CMP_SIGNATURES.items() if re.search(pat, text, re.I))
    ids = sorted(set(ANALYTICS_ID_RE.findall(text)) | {f"FB-{m}" for m in FB_PIXEL_RE.findall(text)})
    default = bool(CONSENT_DEFAULT_RE.search(text))
    v2 = default and "ad_user_data" in text and "ad_personalization" in text
    return cmps, ids, default, v2


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
                    "invalid_images": [u for u in imgs if not valid_absolute_url(u) and not _protocol_relative(u)],
                    "relative_images": [u for u in imgs if _protocol_relative(u)],
                    "has_offers": bool(offers),
                    "has_brand": bool(item.get("brand")),
                    "has_sku": bool(item.get("sku")),
                    "has_rating": bool(item.get("aggregateRating")),
                    "currencies": sorted(_currencies(offers)),
                })
    facts.jsonld_types = sorted(set(facts.jsonld_types))

    # Bilder
    for img in soup.find_all("img"):
        facts.images_total += 1
        if not (img.get("width") and img.get("height")):
            facts.images_no_dimensions += 1
        if facts.images_total > 2 and (img.get("loading") or "").lower() != "lazy" and (img.get("fetchpriority") or "").lower() != "high":
            facts.images_no_lazy += 1
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
        if is_malformed_href(a["href"]) and len(facts.malformed_hrefs) < 5:
            facts.malformed_hrefs.append(a["href"][:200])
        href = urljoin(url, a["href"].split("#")[0])
        p = urlsplit(href)
        if p.scheme in ("http", "https") and p.netloc.lower() == site_host:
            links.add(p._replace(fragment="").geturl())
    facts.internal_links = sorted(links)
    handles = {urlsplit(l).path.split("/products/", 1)[1].split("/")[0] for l in links if "/products/" in urlsplit(l).path}
    facts.product_link_count = len(handles)
    facts.consent_platforms, facts.analytics_ids, facts.consent_mode_default, facts.consent_mode_v2 = detect_tracking(
        html.decode("utf-8", errors="replace"))

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
