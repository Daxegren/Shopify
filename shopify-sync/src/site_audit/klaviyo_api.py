"""E-postens försäljning från Klaviyo till BigQuery, per dag och kanal.

Skriven från den publika API-beskrivningen (Klaviyo API, revision i huvudet, Metrics och metric-aggregates). OBS: svarsformen
är inte verifierad mot ett riktigt konto. Nyckeln är en privat API-nyckel med läsrätt (Metrics, Events), lagrad som
hemlighet; den skickas bara i huvudet Authorization och hamnar aldrig i en URL eller i loggen.

Vi läser måttet "Placed Order" (Shopify-integrationens beställningshändelse) uppdelat på $attributed_channel, så att
andelen av försäljningen som Klaviyo tillskriver e-post och SMS syns. Det är Klaviyos egen attribuering och ska inte
summeras med Googles eller Metas.
"""

from __future__ import annotations

import time
from datetime import date, timedelta
from typing import Any, Iterator

BASE = "https://a.klaviyo.com/api"
METRIC_NAME = "Placed Order"

KLAVIYO_SCHEMA = [
    ("d", "DATE", "REQUIRED"), ("channel", "STRING", "NULLABLE"), ("orders", "FLOAT64", "NULLABLE"),
    ("revenue", "FLOAT64", "NULLABLE"),
]


def klaviyo_session(api_key: str, revision: str):
    import requests

    s = requests.Session()
    s.headers.update({"Authorization": f"Klaviyo-API-Key {api_key}", "revision": revision, "accept": "application/json"})
    return s


def _request(session, method: str, url: str, **kw):
    for attempt in range(5):
        resp = session.request(method, url, timeout=120, **kw)
        if resp.status_code in (429, 500, 503):
            time.sleep(2 ** attempt * 2)
            continue
        if resp.status_code >= 400:
            raise RuntimeError(f"Klaviyo {url.split('/api')[-1]} -> {resp.status_code}: {resp.text[:300]}")
        return resp.json()
    raise RuntimeError("Klaviyo misslyckades efter flera försök")


def find_metric_id(session, name: str = METRIC_NAME) -> str:
    data = _request(session, "GET", f"{BASE}/metrics/")
    while True:
        for m in data.get("data", []):
            if m.get("attributes", {}).get("name") == name:
                return m["id"]
        nxt = (data.get("links") or {}).get("next")
        if not nxt:
            raise RuntimeError(f"Måttet '{name}' finns inte i Klaviyo-kontot.")
        data = _request(session, "GET", nxt)


def klaviyo_order_rows(session, start: date, end: date, timezone: str = "Europe/Stockholm") -> Iterator[dict[str, Any]]:
    """Beställningar och värde per dag och tillskriven kanal (email, sms, ingen)."""
    metric_id = find_metric_id(session)
    body = {"data": {"type": "metric-aggregate", "attributes": {
        "metric_id": metric_id, "measurements": ["count", "sum_value"], "interval": "day",
        "by": ["$attributed_channel"], "timezone": timezone, "page_size": 500,
        "filter": [f"greater-or-equal(datetime,{start.isoformat()}T00:00:00)",
                   f"less-than(datetime,{(end + timedelta(days=1)).isoformat()}T00:00:00)"]}}}
    data = _request(session, "POST", f"{BASE}/metric-aggregates/", json=body,
                    headers={"content-type": "application/vnd.api+json"})
    attrs = data.get("data", {}).get("attributes", {})
    dates = [str(x)[:10] for x in attrs.get("dates", [])]
    for series in attrs.get("data", []):
        dims = series.get("dimensions") or [""]
        channel = (dims[0] or "ingen").lower()
        counts = series.get("measurements", {}).get("count", [])
        sums = series.get("measurements", {}).get("sum_value", [])
        for i, d in enumerate(dates):
            c = (counts[i] if i < len(counts) else 0) or 0
            v = (sums[i] if i < len(sums) else 0) or 0
            if c or v:
                yield {"d": d, "channel": channel, "orders": float(c), "revenue": float(v)}
