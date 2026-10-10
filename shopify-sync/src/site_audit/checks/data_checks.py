"""Kontroller som kombinerar crawlen med Search Console- och GA4-data i BigQuery.

Datan hämtas med fetch_search_data() och kontrollerna är rena funktioner, så de kan
testas utan BigQuery.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import urlsplit

from ..config import SiteConfig
from ..crawler import CrawlResult, normalize_url
from ..findings import Finding
from ..impact import _p

F = Finding


@dataclass
class SearchData:
    days: int
    by_path: dict[str, dict[str, float]] = field(default_factory=dict)    # path -> clicks, impressions, position
    cannibal: list[dict[str, Any]] = field(default_factory=list)          # query, urls[...]
    ga4_landing: dict[str, dict[str, float]] = field(default_factory=dict)  # path -> sessions, revenue


def gsc_by_path_sql(gsc_table: str) -> str:
    return f"""
SELECT {_p('url')} AS path, SUM(clicks) AS clicks, SUM(impressions) AS impressions,
       SAFE_DIVIDE(SUM(sum_position), SUM(impressions)) + 1 AS position
FROM `{gsc_table}`
WHERE data_date >= DATE_SUB(CURRENT_DATE(), INTERVAL @days DAY) AND search_type = 'WEB'
GROUP BY 1
"""


def gsc_cannibal_sql(gsc_table: str) -> str:
    return f"""
WITH q AS (
  SELECT query, {_p('url')} AS path, SUM(clicks) AS clicks, SUM(impressions) AS impressions,
         SAFE_DIVIDE(SUM(sum_position), SUM(impressions)) + 1 AS position
  FROM `{gsc_table}`
  WHERE data_date >= DATE_SUB(CURRENT_DATE(), INTERVAL @days DAY) AND search_type = 'WEB'
    AND NOT is_anonymized_query AND query IS NOT NULL
  GROUP BY 1, 2
  HAVING impressions >= @min_impressions
)
SELECT query, ARRAY_AGG(STRUCT(path, clicks, impressions, position) ORDER BY impressions DESC LIMIT 5) AS urls,
       SUM(impressions) AS impressions
FROM q GROUP BY 1 HAVING COUNT(*) >= 2
ORDER BY impressions DESC LIMIT 500
"""


def fetch_search_data(store, site: SiteConfig, days: int = 90, min_impressions: int = 50) -> SearchData:
    data = SearchData(days=days)
    bq = store.bq
    if site.gsc_table:
        p = [bq.ScalarQueryParameter("days", "INT64", days)]
        for r in store.query(gsc_by_path_sql(site.gsc_table), p):
            data.by_path[r["path"]] = {"clicks": r["clicks"] or 0, "impressions": r["impressions"] or 0, "position": r["position"]}
        p2 = p + [bq.ScalarQueryParameter("min_impressions", "INT64", min_impressions)]
        data.cannibal = store.query(gsc_cannibal_sql(site.gsc_table), p2)
    return data


def _path(url: str) -> str:
    return (urlsplit(url).path.rstrip("/") or "/")


def check_lost_traffic(cr: CrawlResult, sd: SearchData, site: SiteConfig) -> list[Finding]:
    """Sidor som haft klick i Google men nu ger fel eller omdirigeras till fel."""
    out = []
    crawled = {_path(u): cu for u, cu in cr.urls.items()}
    for path, m in sd.by_path.items():
        cu = crawled.get(path)
        if not cu or m["clicks"] < 1:
            continue
        if cu.status >= 400:
            out.append(F("traffic_page_broken", "critical", "indexing",
                         f"Sidan hade {m['clicks']:.0f} klick senaste {sd.days} dagarna men ger nu {cu.status}",
                         url=cu.url, evidence={"clicks": m["clicks"], "impressions": m["impressions"]}))
        elif cu.redirect_count and m["clicks"] >= 10 and not _https_only(cu.url, cu.final_url):
            out.append(F("traffic_page_redirected", "medium", "redirects",
                         f"Sida med {m['clicks']:.0f} klick omdirigeras (kontrollera att målet är rätt)",
                         url=cu.url, evidence={"final_url": cu.final_url, "clicks": m["clicks"]}))
    return out


def check_zero_impressions(cr: CrawlResult, sd: SearchData, site: SiteConfig) -> list[Finding]:
    """Indexerbara sidor i sitemapen som inte haft en enda visning: kandidater att slå ihop eller ta bort."""
    if not sd.by_path:
        return []
    out = []
    per_type: dict[str, int] = defaultdict(int)
    for cu in cr.urls.values():
        if not cu.in_sitemap or cu.status != 200 or cu.redirect_count or not cu.facts:
            continue
        if sd.by_path.get(_path(cu.url), {}).get("impressions", 0) == 0:
            per_type[cu.facts.page_type] += 1
            out.append(F("no_search_impressions", "low", "content",
                         f"Inga visningar i Google senaste {sd.days} dagarna ({cu.facts.page_type})",
                         url=cu.url, evidence={"page_type": cu.facts.page_type, "words": cu.facts.word_count}))
    if per_type:
        out.append(F("no_impressions_summary", "info", "content",
                     f"{sum(per_type.values())} sidor i sitemapen utan visningar senaste {sd.days} dagarna",
                     url=site.base_url, evidence=dict(per_type)))
    return out


def check_ctr(cr: CrawlResult, sd: SearchData, site: SiteConfig, min_impr: int = 1000, max_ctr: float = 0.01) -> list[Finding]:
    out = []
    for path, m in sd.by_path.items():
        if m["impressions"] >= min_impr and (m["position"] or 99) <= 10:
            ctr = m["clicks"] / m["impressions"] if m["impressions"] else 0
            if ctr < max_ctr:
                out.append(F("low_ctr_top10", "medium", "onpage",
                             f"Topp 10 i snitt men bara {ctr * 100:.1f} % klickfrekvens (titel/beskrivning?)",
                             url=site.base_url + path, evidence={"impressions": m["impressions"], "clicks": m["clicks"],
                                                                 "position": round(m["position"], 1)}))
    return out


def check_cannibalization(cr: CrawlResult, sd: SearchData, site: SiteConfig) -> list[Finding]:
    out = []
    for row in sd.cannibal:
        urls = [u["path"] if isinstance(u, dict) else u.path for u in row["urls"]]
        out.append(F("keyword_cannibalization", "medium", "content",
                     f"{len(urls)} sidor konkurrerar om sökfrasen '{row['query']}'",
                     url=site.base_url + urls[0], evidence={"query": row["query"], "paths": urls,
                                                            "impressions": row["impressions"]}))
    return out


def run_data_checks(cr: CrawlResult, sd: SearchData, site: SiteConfig) -> list[Finding]:
    out: list[Finding] = []
    for check in (check_lost_traffic, check_zero_impressions, check_ctr, check_cannibalization):
        out.extend(check(cr, sd, site))
    return out


def _https_only(url: str, final_url: str) -> bool:
    """http://x/a → https://x/a är Shopifys vanliga omdirigering och inget fel."""
    return url.startswith("http://") and final_url.rstrip("/") == "https://" + url[7:].rstrip("/")
