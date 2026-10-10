"""Historik via Search Console API och GA4 Data API till BigQuery.

Bulkexporterna fyller inte i bakåt i tiden. API:erna ger upp till 16 månader (GSC) och hela
egendomens historik (GA4), så effektmätningen fungerar från första dagen.

Search Console-raderna sparas i samma form som bulkexporten (data_date, url, query, clicks,
impressions, sum_position), så att SQL:en i impact.py fungerar oförändrad mot båda.

Autentisering: tjänstkontot (Application Default Credentials) läggs till som användare i
Search Console-egendomen och som Viewer i GA4-egendomen.
"""

from __future__ import annotations

import logging
import time
from datetime import date, timedelta
from typing import Any, Iterator
from urllib.parse import quote

log = logging.getLogger(__name__)

GSC_SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"
GA4_SCOPE = "https://www.googleapis.com/auth/analytics.readonly"

GSC_SCHEMA = [
    ("data_date", "DATE", "REQUIRED"), ("site_url", "STRING", "NULLABLE"), ("url", "STRING", "NULLABLE"),
    ("query", "STRING", "NULLABLE"), ("country", "STRING", "NULLABLE"), ("device", "STRING", "NULLABLE"),
    ("search_type", "STRING", "NULLABLE"), ("is_anonymized_query", "BOOL", "NULLABLE"),
    ("clicks", "INT64", "NULLABLE"), ("impressions", "INT64", "NULLABLE"), ("sum_position", "FLOAT64", "NULLABLE"),
]
GA4_SCHEMA = [
    ("d", "DATE", "REQUIRED"), ("property_id", "STRING", "NULLABLE"), ("landing", "STRING", "NULLABLE"),
    ("sessions", "INT64", "NULLABLE"), ("purchases", "INT64", "NULLABLE"), ("revenue", "FLOAT64", "NULLABLE"),
]


def authorized_session(scopes: list[str]):
    import google.auth
    from google.auth.transport.requests import AuthorizedSession

    creds, _ = google.auth.default(scopes=scopes)
    return AuthorizedSession(creds)


def _post(session, url: str, body: dict[str, Any]) -> dict[str, Any]:
    for attempt in range(5):
        resp = session.post(url, json=body, timeout=120)
        if resp.status_code in (429, 500, 503):
            time.sleep(2 ** attempt * 2)
            continue
        if resp.status_code >= 400:
            raise RuntimeError(f"{url} -> {resp.status_code}: {resp.text[:500]}")
        return resp.json()
    raise RuntimeError(f"{url} misslyckades efter flera försök")


def gsc_rows(session, site_url: str, start: date, end: date, with_query: bool = False,
             row_limit: int = 25000) -> Iterator[dict[str, Any]]:
    """En dag i taget (så att 25 000-gränsen räcker), sidor och valfritt sökfraser."""
    endpoint = f"https://searchconsole.googleapis.com/webmasters/v3/sites/{quote(site_url, safe='')}/searchAnalytics/query"
    dims = ["date", "page"] + (["query"] if with_query else [])
    d = start
    while d <= end:
        start_row = 0
        while True:
            body = {"startDate": d.isoformat(), "endDate": d.isoformat(), "dimensions": dims,
                    "type": "web", "rowLimit": row_limit, "startRow": start_row, "dataState": "final"}
            rows = _post(session, endpoint, body).get("rows", [])
            for r in rows:
                keys = r["keys"]
                impressions = int(r.get("impressions", 0))
                yield {
                    "data_date": keys[0], "site_url": site_url, "url": keys[1],
                    "query": keys[2] if with_query else None, "country": None, "device": None,
                    "search_type": "WEB", "is_anonymized_query": False,
                    "clicks": int(r.get("clicks", 0)), "impressions": impressions,
                    # Bulkexporten: snittposition = sum_position / impressions + 1
                    "sum_position": (float(r.get("position", 1)) - 1) * impressions,
                }
            if len(rows) < row_limit:
                break
            start_row += row_limit
        d += timedelta(days=1)


def ga4_rows(session, property_id: str, start: date, end: date, page_size: int = 100000) -> Iterator[dict[str, Any]]:
    endpoint = f"https://analyticsdata.googleapis.com/v1beta/properties/{property_id}:runReport"
    offset = 0
    while True:
        body = {
            "dateRanges": [{"startDate": start.isoformat(), "endDate": end.isoformat()}],
            "dimensions": [{"name": "date"}, {"name": "landingPage"}],
            "metrics": [{"name": "sessions"}, {"name": "ecommercePurchases"}, {"name": "purchaseRevenue"}],
            "limit": page_size, "offset": offset, "keepEmptyRows": False,
        }
        data = _post(session, endpoint, body)
        rows = data.get("rows", [])
        for r in rows:
            dv, mv = r["dimensionValues"], r["metricValues"]
            ds = dv[0]["value"]
            yield {"d": f"{ds[:4]}-{ds[4:6]}-{ds[6:]}", "property_id": property_id, "landing": dv[1]["value"],
                   "sessions": int(float(mv[0]["value"])), "purchases": int(float(mv[1]["value"])),
                   "revenue": float(mv[2]["value"])}
        offset += len(rows)
        if not rows or offset >= int(data.get("rowCount", 0)):
            break


def load_rows(store, table: str, schema, rows: Iterator[dict[str, Any]], replace_range: tuple[str, date, date] | None = None,
              batch: int = 50000) -> int:
    """Laddar rader i batchar. replace_range=(datumkolumn, start, slut) tar först bort perioden så att
    omkörningar inte dubblerar."""
    bq = store.bq
    full = f"{store.dataset}.{table}"
    t = bq.Table(full, schema=[bq.SchemaField(n, ty, mode=m) for n, ty, m in schema])
    t.time_partitioning = bq.TimePartitioning(field=schema[0][0])
    store.client.create_table(t, exists_ok=True)
    if replace_range:
        col, s, e = replace_range
        store.client.query(f"DELETE FROM `{full}` WHERE {col} BETWEEN @s AND @e", job_config=bq.QueryJobConfig(
            query_parameters=[bq.ScalarQueryParameter("s", "DATE", s), bq.ScalarQueryParameter("e", "DATE", e)])).result()
    cfg = bq.LoadJobConfig(schema=t.schema, write_disposition=bq.WriteDisposition.WRITE_APPEND)
    total, buf = 0, []
    for r in rows:
        buf.append(r)
        if len(buf) >= batch:
            store.client.load_table_from_json(buf, full, job_config=cfg).result()
            total += len(buf)
            buf = []
    if buf:
        store.client.load_table_from_json(buf, full, job_config=cfg).result()
        total += len(buf)
    return total


def ga4_api_window_sql(table: str) -> str:
    """Samma utdata som impact.ga4_window_sql, men från API-tabellen."""
    return f"""
SELECT REGEXP_CONTAINS(COALESCE(NULLIF(RTRIM(REGEXP_EXTRACT(landing, r'^([^?#]*)'), '/'), ''), '/'), @pattern) AS in_group,
       IF(d < @change_date, 'before', 'after') AS period,
       SUM(sessions) AS sessions, SUM(purchases) AS purchases, SUM(revenue) AS revenue
FROM `{table}`
WHERE d BETWEEN @before_start AND @after_end
GROUP BY 1, 2
"""
