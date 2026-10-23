"""Indexeringsstatus via Search Console URL Inspection API (T17).

Frågar Google om ett urval av sajtens adresser är indexerade, vilken canonical Google valde och när sidan senast hämtades.
Det är det enda sättet att se skillnaden mellan "finns i sitemapen" och "finns i Google". Kvot: cirka 2 000 frågor per dag och
egendom, så urvalet är litet och jämnt fördelat per sidtyp. Kräver att tjänstkontot är användare i Search Console-egendomen."""

from __future__ import annotations

import time
from collections import Counter, defaultdict
from typing import Any
from urllib.parse import urlsplit

from .findings import Finding
from .google_api import GSC_SCOPE, _post  # noqa: F401 - GSC_SCOPE återanvänds av kommandot
from .html_parse import page_type
from .crossdomain import evenly

F = Finding
INSPECT_ENDPOINT = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"
MAX_PER_RUN = 400


def inspect_url(session, site_url: str, url: str, language: str = "sv-SE") -> dict[str, Any]:
    data = _post(session, INSPECT_ENDPOINT, {"inspectionUrl": url, "siteUrl": site_url, "languageCode": language})
    result = data.get("inspectionResult", {})
    idx = result.get("indexStatusResult", {})
    return {"url": url, "page_type": page_type(urlsplit(url).path or "/"),
            "verdict": idx.get("verdict"), "coverage": idx.get("coverageState"), "indexing": idx.get("indexingState"),
            "robots": idx.get("robotsTxtState"), "fetch": idx.get("pageFetchState"), "last_crawl": idx.get("lastCrawlTime"),
            "google_canonical": idx.get("googleCanonical"), "user_canonical": idx.get("userCanonical"),
            "crawled_as": idx.get("crawledAs")}


def sample_urls(urls: list[str], per_type: int) -> list[str]:
    """Jämnt urval per sidtyp av sitemapens adresser (startsida, kategorier, produkter, artiklar)."""
    by_type: dict[str, list[str]] = defaultdict(list)
    for u in urls:
        by_type[page_type(urlsplit(u).path or "/")].append(u)
    out: list[str] = []
    for ptype in ("home", "collection", "product", "article", "page"):
        out.extend(evenly(by_type.get(ptype, []), per_type))
    return out[:MAX_PER_RUN]


def run_inspection(session, site_url: str, urls: list[str], sleep_s: float = 0.15, language: str = "sv-SE") -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for u in urls:
        try:
            rows.append(inspect_url(session, site_url, u, language))
        except RuntimeError as exc:
            rows.append({"url": u, "page_type": None, "verdict": "FEL", "coverage": str(exc)[:200]})
        time.sleep(sleep_s)
    return rows


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_type: dict[str, Counter] = defaultdict(Counter)
    for r in rows:
        by_type[r.get("page_type") or "okänd"][r.get("coverage") or r.get("verdict") or "okänt"] += 1
    return {"total": len(rows), "indexed": sum(1 for r in rows if r.get("verdict") == "PASS"),
            "by_type": {t: dict(c) for t, c in by_type.items()}}


def findings_from_rows(rows: list[dict[str, Any]], site_url: str) -> list[Finding]:
    out: list[Finding] = []
    ok = [r for r in rows if r.get("verdict") != "FEL"]
    not_indexed = [r for r in ok if r.get("verdict") != "PASS"]
    if ok and not_indexed:
        share = len(not_indexed) / len(ok)
        by_state = Counter(r.get("coverage") or "okänt" for r in not_indexed)
        out.append(F("sitemap_urls_not_indexed", "high" if share >= 0.3 else "medium", "indexing",
                     f"{len(not_indexed)} av {len(ok)} granskade sitemap-adresser är inte indexerade ({share:.0%})",
                     url=not_indexed[0]["url"], evidence={"by_state": dict(by_state), "sample": [r["url"] for r in not_indexed[:10]]}))
    other = [r for r in ok if r.get("google_canonical") and r.get("user_canonical")
             and r["google_canonical"].rstrip("/") != r["user_canonical"].rstrip("/")]
    if other:
        out.append(F("google_chose_other_canonical", "medium", "indexing",
                     f"{len(other)} sidor där Google valt en annan canonical än den sajten anger",
                     url=other[0]["url"], evidence={"count": len(other),
                                                     "sample": [{"url": r["url"], "google": r["google_canonical"]} for r in other[:10]]}))
    errors = [r for r in rows if r.get("verdict") == "FEL"]
    if errors:
        out.append(F("inspection_errors", "info", "indexing", f"{len(errors)} adresser kunde inte inspekteras (kvot eller behörighet)",
                     url=site_url, evidence={"sample": [r["coverage"] for r in errors[:3]]}))
    return out
