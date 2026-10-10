"""Hämtar katalog- och innehållsdata från Shopify Admin GraphQL för granskning.

Varje del hämtas separat och fel registreras i stället för att stoppa körningen, eftersom
fält och behörigheter skiljer sig mellan butiker och API-versioner.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

log = logging.getLogger(__name__)

PAGE_SIZE = 100

# Produkter och kollektioner hämtas med Bulk Operations: nästlade listor (bilder,
# kollektionernas produkter) skulle annars överskrida kostnadsgränsen för en vanlig fråga.
PRODUCTS_BULK = """
{
  products {
    edges { node {
      id handle title status vendor productType tags createdAt updatedAt publishedAt
      onlineStoreUrl
      seo { title description }
      description
      media { edges { node { ... on MediaImage { id alt image { url } } } } }
    } }
  }
}
"""

COLLECTIONS_BULK = """
{
  collections {
    edges { node {
      id handle title updatedAt
      seo { title description }
      description
      productsCount { count }
      ruleSet { appliedDisjunctively rules { column relation condition } }
      products { edges { node { id } } }
    } }
  }
}
"""

PAGES_Q = """
query($cursor: String) {
  pages(first: %d, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes { id handle title body isPublished publishedAt createdAt updatedAt templateSuffix }
  }
}
""" % PAGE_SIZE

ARTICLES_Q = """
query($cursor: String) {
  articles(first: %d, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes { id handle title body isPublished publishedAt createdAt blog { handle } }
  }
}
""" % PAGE_SIZE

REDIRECTS_Q = """
query($cursor: String) {
  urlRedirects(first: 250, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes { id path target }
  }
}
"""

LOCALES_Q = """
{ shopLocales { locale primary published } }
"""

MARKETS_Q = """
{ markets(first: 50) { nodes { id name handle status } } }
"""

SHOP_Q = """
{ shop { name myshopifyDomain primaryDomain { url host } currencyCode } }
"""


@dataclass
class AdminData:
    shop: dict[str, Any] | None = None
    products: list[dict[str, Any]] = field(default_factory=list)
    collections: list[dict[str, Any]] = field(default_factory=list)
    pages: list[dict[str, Any]] = field(default_factory=list)
    articles: list[dict[str, Any]] = field(default_factory=list)
    redirects: list[dict[str, Any]] = field(default_factory=list)
    locales: list[dict[str, Any]] = field(default_factory=list)
    markets: list[dict[str, Any]] = field(default_factory=list)
    translations: dict[str, dict[str, dict[str, int]]] = field(default_factory=dict)  # locale -> typ -> mått
    errors: dict[str, str] = field(default_factory=dict)

    def counts(self) -> dict[str, int]:
        return {k: len(getattr(self, k)) for k in ("products", "collections", "pages", "articles", "redirects", "locales", "markets")}


def _paginate(client, query: str, root: str, limit: int | None = None) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    cursor = None
    while True:
        data = client.graphql(query, {"cursor": cursor})[root]
        out.extend(data["nodes"])
        if limit and len(out) >= limit:
            return out[:limit]
        if not data["pageInfo"]["hasNextPage"]:
            return out
        cursor = data["pageInfo"]["endCursor"]


def _bulk_tree(client, query: str, child_key: str, poll_s: float, timeout_s: float) -> list[dict[str, Any]]:
    """Kör en bulk-fråga och bygger tillbaka barnrader (med __parentId) under sina föräldrar."""
    _, objects = client.run_bulk(query, poll_s, timeout_s)
    parents: dict[str, dict[str, Any]] = {}
    order: list[dict[str, Any]] = []
    for obj in objects:
        parent_id = obj.pop("__parentId", None)
        if parent_id:
            parent = parents.get(parent_id)
            if parent is not None:
                parent.setdefault(child_key, {"nodes": []})["nodes"].append(obj)
            continue
        obj.setdefault(child_key, {"nodes": []})
        parents[obj["id"]] = obj
        order.append(obj)
    return order


TRANSLATIONS_Q = """
query($cursor: String, $type: TranslatableResourceType!, $locale: String!) {
  translatableResources(first: 50, after: $cursor, resourceType: $type) {
    pageInfo { hasNextPage endCursor }
    nodes {
      resourceId
      translatableContent { key value digest locale }
      translations(locale: $locale) { key value outdated }
    }
  }
}
"""
TRANSLATION_TYPES = ("PRODUCT", "COLLECTION", "ONLINE_STORE_PAGE")
TEXT_KEYS = {"title", "body_html", "meta_title", "meta_description"}


def translation_coverage(client, locales: list[str], sample: int = 300) -> dict[str, dict[str, dict[str, int]]]:
    """Andel resurser (stickprov) som har översättning per språk och typ."""
    out: dict[str, dict[str, dict[str, int]]] = {}
    for locale in locales:
        out[locale] = {}
        for rtype in TRANSLATION_TYPES:
            stats = {"resources": 0, "title_translated": 0, "fully_translated": 0, "outdated": 0}
            cursor = None
            while stats["resources"] < sample:
                data = client.graphql(TRANSLATIONS_Q, {"cursor": cursor, "type": rtype, "locale": locale})["translatableResources"]
                for node in data["nodes"]:
                    source = {c["key"] for c in node["translatableContent"] if c["key"] in TEXT_KEYS and (c.get("value") or "").strip()}
                    done = {t["key"] for t in node["translations"] if (t.get("value") or "").strip()}
                    stats["resources"] += 1
                    stats["title_translated"] += "title" in done
                    stats["fully_translated"] += bool(source) and source <= done
                    stats["outdated"] += sum(1 for t in node["translations"] if t.get("outdated"))
                if not data["pageInfo"]["hasNextPage"]:
                    break
                cursor = data["pageInfo"]["endCursor"]
            out[locale][rtype] = stats
    return out


def fetch_admin_data(client, limit: int | None = None, poll_s: float = 3, timeout_s: float = 3600) -> AdminData:
    data = AdminData()
    jobs = [
        ("shop", lambda: client.graphql(SHOP_Q)["shop"]),
        ("products", lambda: _bulk_tree(client, PRODUCTS_BULK, "media", poll_s, timeout_s)),
        ("collections", lambda: _bulk_tree(client, COLLECTIONS_BULK, "products", poll_s, timeout_s)),
        ("pages", lambda: _paginate(client, PAGES_Q, "pages", limit)),
        ("articles", lambda: _paginate(client, ARTICLES_Q, "articles", limit)),
        ("redirects", lambda: _paginate(client, REDIRECTS_Q, "urlRedirects", limit)),
        ("locales", lambda: client.graphql(LOCALES_Q)["shopLocales"]),
        ("markets", lambda: client.graphql(MARKETS_Q)["markets"]["nodes"]),
    ]
    for name, job in jobs:
        try:
            setattr(data, name, job())
            log.info("Admin: %s hämtade", name)
        except Exception as exc:  # noqa: BLE001 - registreras och visas i rapporten
            log.warning("Admin: %s kunde inte hämtas: %s", name, exc)
            data.errors[name] = str(exc)[:500]
    secondary = [l["locale"] for l in data.locales if l.get("published") and not l.get("primary")]
    if secondary:
        try:
            data.translations = translation_coverage(client, secondary)
        except Exception as exc:  # noqa: BLE001 - kräver read_translations
            log.warning("Admin: översättningar kunde inte hämtas: %s", exc)
            data.errors["translations"] = str(exc)[:500]
    return data
