"""Produktstatus från Google Merchant Center (Merchant API) till BigQuery.

Skriven från den publika API-beskrivningen (Merchant API v1, products). OBS: svarsformen är inte verifierad mot
ett riktigt konto; fältnamnen följer dokumentationen och läses försiktigt (saknade fält ger tomma värden, inget fel).

Behörighet: tjänstkontot läggs till som användare (läsrätt) i Merchant Center-kontot och Merchant API aktiveras i
Cloud-projektet. Omfång: content. Produktstatus är en ögonblicksbild (hur det ser ut nu), så tabellen byggs upp dag för
dag på samma sätt som lagersaldot: körs samma dag igen ersätts dagens rader.
"""

from __future__ import annotations

import json
import time
from datetime import date
from typing import Any, Iterator

MERCHANT_SCOPE = "https://www.googleapis.com/auth/content"

MERCHANT_SCHEMA = [
    ("d", "DATE", "REQUIRED"), ("offer_id", "STRING", "NULLABLE"), ("title", "STRING", "NULLABLE"),
    ("feed_label", "STRING", "NULLABLE"), ("language", "STRING", "NULLABLE"),
    ("approved_countries", "STRING", "NULLABLE"), ("disapproved_countries", "STRING", "NULLABLE"),
    ("is_disapproved", "BOOL", "NULLABLE"), ("top_issue", "STRING", "NULLABLE"), ("issue_count", "INT64", "NULLABLE"),
    ("issues_json", "STRING", "NULLABLE"),
]


def merchant_session():
    from .google_api import authorized_session

    return authorized_session([MERCHANT_SCOPE])


def _countries(statuses: list[dict[str, Any]], key: str) -> list[str]:
    seen: list[str] = []
    for s in statuses:
        for c in s.get(key, []) or []:
            if c not in seen:
                seen.append(c)
    return seen


def merchant_product_rows(session, account_id: str, today: date, version: str = "v1",
                          page_size: int = 1000) -> Iterator[dict[str, Any]]:
    """En rad per produkt med godkända och avvisade länder samt problem. Hämtar alla sidor."""
    acct = "".join(ch for ch in str(account_id) if ch.isdigit())
    url = f"https://merchantapi.googleapis.com/products/{version}/accounts/{acct}/products"
    token: str | None = None
    while True:
        params: dict[str, Any] = {"pageSize": page_size}
        if token:
            params["pageToken"] = token
        for attempt in range(5):
            resp = session.get(url, params=params, timeout=120)
            if resp.status_code in (429, 500, 503):
                time.sleep(2 ** attempt * 2)
                continue
            if resp.status_code >= 400:
                raise RuntimeError(f"Merchant {acct} -> {resp.status_code}: {resp.text[:400]}")
            break
        else:
            raise RuntimeError(f"Merchant {acct} misslyckades efter flera försök")
        data = resp.json()
        for p in data.get("products", []):
            status = p.get("productStatus", {}) or {}
            dest = status.get("destinationStatuses", []) or []
            issues = status.get("itemLevelIssues", []) or []
            approved, disapproved = _countries(dest, "approvedCountries"), _countries(dest, "disapprovedCountries")
            serious = [i for i in issues if str(i.get("severity", "")).upper() in ("DISAPPROVED", "ERROR")]
            top = (serious or issues or [{}])[0]
            yield {"d": today.isoformat(), "offer_id": p.get("offerId", ""),
                   "title": (p.get("productAttributes", {}) or {}).get("title", ""),
                   "feed_label": p.get("feedLabel", ""), "language": p.get("contentLanguage", ""),
                   "approved_countries": ",".join(approved), "disapproved_countries": ",".join(disapproved),
                   "is_disapproved": bool(disapproved) and not approved,
                   "top_issue": top.get("description") or top.get("code") or "", "issue_count": len(issues),
                   "issues_json": json.dumps([{k: i.get(k) for k in ("code", "severity", "attribute", "description")}
                                              for i in issues[:10]], ensure_ascii=False)}
        token = data.get("nextPageToken")
        if not token:
            return
