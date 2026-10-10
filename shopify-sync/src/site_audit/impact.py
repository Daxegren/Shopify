"""Effektmätning: hur har en grupp sidor utvecklats före/efter en ändring?

Källor (alla i BigQuery, samma plats):
  Search Console bulkexport  <proj>.searchconsole.searchdata_url_impression
  GA4-export                 <proj>.analytics_<id>.events_*
  Shopify (shopify-sync)     <proj>.shopify.orders  (first_visit_landing_page)

Jämförelsen görs mot resten av sajten under samma perioder, så att säsong och
allmän trafikutveckling inte tas för effekt av ändringen.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Any

PATH_FROM_URL = r"REGEXP_EXTRACT({col}, r'^https?://[^/]+(/[^?#]*)')"


def _p(col: str) -> str:
    return "COALESCE(NULLIF(RTRIM(" + PATH_FROM_URL.format(col=col) + ", '/'), ''), '/')"


def gsc_window_sql(gsc_table: str) -> str:
    path = _p("url")
    return f"""
WITH base AS (
  SELECT data_date AS d, {path} AS path, clicks, impressions, sum_position
  FROM `{gsc_table}`
  WHERE data_date BETWEEN @before_start AND @after_end
    AND (@site_url IS NULL OR site_url = @site_url)
),
tagged AS (
  SELECT *, REGEXP_CONTAINS(path, @pattern) AS in_group,
         IF(d < @change_date, 'before', 'after') AS period
  FROM base
  WHERE d < @change_date AND d >= @before_start OR d >= @change_date AND d <= @after_end
)
SELECT in_group, period,
       SUM(clicks) AS clicks, SUM(impressions) AS impressions,
       SAFE_DIVIDE(SUM(sum_position), SUM(impressions)) + 1 AS avg_position,
       COUNT(DISTINCT path) AS pages
FROM tagged GROUP BY 1, 2
"""


def ga4_window_sql(ga4_dataset: str) -> str:
    """Sessioner, köp och intäkt per landningssida (första sidvisningen i sessionen)."""
    return f"""
WITH ev AS (
  SELECT PARSE_DATE('%Y%m%d', event_date) AS d, user_pseudo_id,
         (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') AS sid,
         (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_location') AS loc,
         event_name, event_timestamp, ecommerce.purchase_revenue AS revenue
  FROM `{ga4_dataset}.events_*`
  WHERE _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', @before_start) AND FORMAT_DATE('%Y%m%d', @after_end)
),
sessions AS (
  SELECT user_pseudo_id, sid, MIN(d) AS d,
         ARRAY_AGG(IF(event_name = 'page_view', loc, NULL) IGNORE NULLS ORDER BY event_timestamp LIMIT 1)[SAFE_OFFSET(0)] AS landing,
         COUNTIF(event_name = 'purchase') AS purchases, SUM(IF(event_name = 'purchase', revenue, 0)) AS revenue
  FROM ev WHERE sid IS NOT NULL GROUP BY 1, 2
),
tagged AS (
  SELECT *, REGEXP_CONTAINS({_p('landing')}, @pattern) AS in_group, IF(d < @change_date, 'before', 'after') AS period
  FROM sessions WHERE landing IS NOT NULL
)
SELECT in_group, period, COUNT(*) AS sessions, SUM(purchases) AS purchases, SUM(revenue) AS revenue
FROM tagged GROUP BY 1, 2
"""


def shopify_window_sql(shopify_dataset: str) -> str:
    return f"""
WITH o AS (
  SELECT DATE(created_at) AS d,
         COALESCE(NULLIF(RTRIM(REGEXP_EXTRACT(first_visit_landing_page, r'^(?:https?://[^/]+)?(/[^?#]*)'), '/'), ''), '/') AS landing,
         CAST(total_price AS FLOAT64) AS revenue
  FROM `{shopify_dataset}.orders`
  WHERE DATE(created_at) BETWEEN @before_start AND @after_end AND cancelled_at IS NULL
)
SELECT REGEXP_CONTAINS(IFNULL(landing, ''), @pattern) AS in_group, IF(d < @change_date, 'before', 'after') AS period,
       COUNT(*) AS orders, SUM(revenue) AS revenue
FROM o GROUP BY 1, 2
"""


def trend_sql(gsc_table: str, groups: list[tuple[str, str]], grain: str = "MONTH") -> str:
    """Klick och visningar per sidgrupp och månad/vecka. groups = [(namn, regex)]."""
    cases = "\n".join(f"    WHEN REGEXP_CONTAINS(path, r'''{rx}''') THEN '{name}'" for name, rx in groups)
    return f"""
WITH base AS (
  SELECT DATE_TRUNC(data_date, {grain}) AS period, {_p('url')} AS path, clicks, impressions, sum_position
  FROM `{gsc_table}` WHERE data_date >= @since
)
SELECT period,
  CASE
{cases}
    ELSE 'övrigt'
  END AS page_group,
  SUM(clicks) AS clicks, SUM(impressions) AS impressions,
  SAFE_DIVIDE(SUM(sum_position), SUM(impressions)) + 1 AS avg_position
FROM base GROUP BY 1, 2 ORDER BY 1, 2
"""


@dataclass
class Window:
    change_date: date
    days: int

    @property
    def before_start(self) -> date:
        return self.change_date - timedelta(days=self.days)

    @property
    def after_end(self) -> date:
        return self.change_date + timedelta(days=self.days - 1)


def params(bq, window: Window, pattern: str, site_url: str | None = None) -> list:
    return [
        bq.ScalarQueryParameter("change_date", "DATE", window.change_date),
        bq.ScalarQueryParameter("before_start", "DATE", window.before_start),
        bq.ScalarQueryParameter("after_end", "DATE", window.after_end),
        bq.ScalarQueryParameter("pattern", "STRING", pattern),
        bq.ScalarQueryParameter("site_url", "STRING", site_url),
    ]


def compare(rows: list[dict[str, Any]], metrics: list[str]) -> dict[str, dict[str, Any]]:
    """Gör om rader (in_group, period, mått...) till före/efter för grupp och kontroll,
    plus 'netto' = gruppens förändring minus resten av sajtens förändring (procentenheter)."""
    cell = {(r["in_group"], r["period"]): r for r in rows}
    out: dict[str, dict[str, Any]] = {}
    for m in metrics:
        def val(g, p):
            r = cell.get((g, p))
            return float(r[m]) if r and r.get(m) is not None else 0.0

        gb, ga, cb, ca = val(True, "before"), val(True, "after"), val(False, "before"), val(False, "after")
        g_pct = (ga - gb) / gb * 100 if gb else None
        c_pct = (ca - cb) / cb * 100 if cb else None
        out[m] = {"before": gb, "after": ga, "change_pct": g_pct, "rest_of_site_pct": c_pct,
                  "net_pct_points": (g_pct - c_pct) if g_pct is not None and c_pct is not None else None}
    return out


def describe(result: dict[str, dict[str, dict[str, Any]]], label: str, window: Window) -> str:
    lines = [f"Effekt för '{label}': {window.days} dagar före vs efter {window.change_date.isoformat()}"]
    names = {"clicks": "Klick (Google)", "impressions": "Visningar (Google)", "avg_position": "Snittposition",
             "sessions": "Sessioner (GA4)", "purchases": "Köp (GA4)", "revenue": "Intäkt",
             "orders": "Ordrar (Shopify)"}
    for source, metrics in result.items():
        for m, v in metrics.items():
            if v["change_pct"] is None:
                lines.append(f"  {source}/{names.get(m, m)}: {v['before']:.0f} → {v['after']:.0f} (ingen jämförelsebas)")
                continue
            net = f", netto {v['net_pct_points']:+.0f} p.e. mot resten av sajten" if v["net_pct_points"] is not None else ""
            lines.append(f"  {source}/{names.get(m, m)}: {v['before']:.0f} → {v['after']:.0f} ({v['change_pct']:+.0f} %{net})")
    return "\n".join(lines)


def run_impact(store, site, pattern: str, change_date: date, days: int = 90, label: str | None = None) -> tuple[dict, str]:
    window = Window(change_date, days)
    bq = store.bq
    result: dict[str, dict] = {}
    if site.gsc_table:
        rows = store.query(gsc_window_sql(site.gsc_table), params(bq, window, pattern))
        result["gsc"] = compare(rows, ["clicks", "impressions"])
    if site.ga4_api_table or site.ga4_dataset:
        from .google_api import ga4_api_window_sql

        sql = ga4_api_window_sql(site.ga4_api_table) if site.ga4_api_table else ga4_window_sql(site.ga4_dataset)
        rows = store.query(sql, params(bq, window, pattern))
        result["ga4"] = compare(rows, ["sessions", "purchases", "revenue"])
    if site.shopify_dataset:
        rows = store.query(shopify_window_sql(site.shopify_dataset), params(bq, window, pattern))
        result["shopify"] = compare(rows, ["orders", "revenue"])
    return result, describe(result, label or pattern, window)
