"""Annonsdata från Google Ads och Meta (Facebook och Instagram) till BigQuery.

Skriven från de publika API-beskrivningarna (Google Ads API, Meta Marketing API) och oberoende av
andra produkters kod. Samma mönster som google_api.py: en funktion per källa som ger rader, och
`load_rows` som ersätter perioden så att omkörningar inte dubblerar.

Behörighet:
- Google Ads: tjänstkontot (Application Default Credentials, omfång adwords) läggs till som
  användare i hanterarkontot (MCC) eller i varje Google Ads-konto, och Google Ads API aktiveras i Cloud-projektet.
  Utvecklartoken är valfri (env GOOGLE_ADS_DEVELOPER_TOKEN, skickas om den finns). Går kontona via en
  hanterarkonto anges dess id som login-customer-id.
- Meta: en systemanvändartoken med läsrätt (ads_read) ligger i en hemlighet (env META_ACCESS_TOKEN).
  Token skickas i huvudet Authorization och hamnar aldrig i en URL eller i loggen.

Konverteringar revideras i efterhand (Googles konverteringsfördröjning, Metas attributionsfönster på
upp till sju dagar). Nattjobbet hämtar därför om de senaste 30 dagarna varje gång.
"""

from __future__ import annotations

import json
import logging
import time
from datetime import date, timedelta
from typing import Any, Iterator

log = logging.getLogger(__name__)

GOOGLE_ADS_SCOPE = "https://www.googleapis.com/auth/adwords"

GOOGLE_ADS_SCHEMA = [
    ("d", "DATE", "REQUIRED"), ("customer_id", "STRING", "NULLABLE"), ("campaign_id", "STRING", "NULLABLE"),
    ("campaign_name", "STRING", "NULLABLE"), ("channel_type", "STRING", "NULLABLE"), ("currency", "STRING", "NULLABLE"),
    ("cost", "FLOAT64", "NULLABLE"), ("impressions", "INT64", "NULLABLE"), ("clicks", "INT64", "NULLABLE"),
    ("conversions", "FLOAT64", "NULLABLE"), ("conversions_value", "FLOAT64", "NULLABLE"),
]
GOOGLE_ADS_PRODUCT_SCHEMA = [
    ("d", "DATE", "REQUIRED"), ("customer_id", "STRING", "NULLABLE"), ("item_id", "STRING", "NULLABLE"),
    ("title", "STRING", "NULLABLE"), ("brand", "STRING", "NULLABLE"), ("currency", "STRING", "NULLABLE"),
    ("cost", "FLOAT64", "NULLABLE"), ("impressions", "INT64", "NULLABLE"), ("clicks", "INT64", "NULLABLE"),
    ("conversions", "FLOAT64", "NULLABLE"), ("conversions_value", "FLOAT64", "NULLABLE"),
]
META_ADS_SCHEMA = [
    ("d", "DATE", "REQUIRED"), ("account_id", "STRING", "NULLABLE"), ("campaign_id", "STRING", "NULLABLE"),
    ("campaign_name", "STRING", "NULLABLE"), ("currency", "STRING", "NULLABLE"),
    ("spend", "FLOAT64", "NULLABLE"), ("impressions", "INT64", "NULLABLE"), ("reach", "INT64", "NULLABLE"),
    ("clicks", "INT64", "NULLABLE"), ("purchases", "FLOAT64", "NULLABLE"), ("purchase_value", "FLOAT64", "NULLABLE"),
    ("leads", "FLOAT64", "NULLABLE"),
]

_CAMPAIGN_GAQL = (
    "SELECT segments.date, campaign.id, campaign.name, campaign.advertising_channel_type, "
    "customer.currency_code, metrics.cost_micros, metrics.impressions, metrics.clicks, "
    "metrics.conversions, metrics.conversions_value FROM campaign "
    "WHERE segments.date BETWEEN '{start}' AND '{end}'"
)
_PRODUCT_GAQL = (
    "SELECT segments.date, segments.product_item_id, segments.product_title, segments.product_brand, "
    "customer.currency_code, metrics.cost_micros, metrics.impressions, metrics.clicks, "
    "metrics.conversions, metrics.conversions_value FROM shopping_performance_view "
    "WHERE segments.date BETWEEN '{start}' AND '{end}'"
)


def windows(start: date, end: date, days: int = 31) -> Iterator[tuple[date, date]]:
    """Delar [start, end] i fönster om högst `days` dagar. Ett långt svar läses in i minnet på en gång, så långa
    historiker hämtas i bitar (ett minnesfel vid 15 månader var orsaken till att produkthistoriken stoppade)."""
    cur = start
    while cur <= end:
        stop = min(cur + timedelta(days=days - 1), end)
        yield cur, stop
        cur = stop + timedelta(days=1)


def _digits(value: str) -> str:
    return "".join(ch for ch in str(value) if ch.isdigit())


def _sleep_retry(attempt: int) -> None:
    time.sleep(2 ** attempt * 2)


# ---------------------------------------------------------------- Google Ads

def google_ads_session(developer_token: str | None = None, login_customer_id: str | None = None):
    """Session med tjänstkontots inloggning och Google Ads-huvudena. Hemligheter hålls i huvudena.

    Utvecklartoken är valfri: Google meddelade 2026 att den inte längre krävs för att använda API:et (åtkomstnivåer
    hanteras i Google Cloud Console). Finns en token skickas den ändå med."""
    from .google_api import authorized_session

    session = authorized_session([GOOGLE_ADS_SCOPE])
    if developer_token:
        session.headers["developer-token"] = developer_token
    if login_customer_id:
        session.headers["login-customer-id"] = _digits(login_customer_id)
    return session


def _google_ads_stream(session, version: str, customer_id: str, query: str) -> Iterator[dict[str, Any]]:
    url = f"https://googleads.googleapis.com/{version}/customers/{_digits(customer_id)}/googleAds:searchStream"
    for attempt in range(5):
        resp = session.post(url, json={"query": query}, timeout=300)
        if resp.status_code in (429, 500, 503):
            _sleep_retry(attempt)
            continue
        if resp.status_code >= 400:
            raise RuntimeError(f"Google Ads {customer_id} -> {resp.status_code}: {resp.text[:500]}")
        for batch in resp.json():
            yield from batch.get("results", [])
        return
    raise RuntimeError(f"Google Ads {customer_id} misslyckades efter flera försök")


def _gads_metrics(m: dict[str, Any]) -> dict[str, Any]:
    return {"cost": int(m.get("costMicros", 0)) / 1_000_000, "impressions": int(m.get("impressions", 0)),
            "clicks": int(m.get("clicks", 0)), "conversions": float(m.get("conversions", 0)),
            "conversions_value": float(m.get("conversionsValue", 0))}


def google_ads_campaign_rows(session, customer_id: str, start: date, end: date,
                             version: str = "v21", chunk_days: int = 31) -> Iterator[dict[str, Any]]:
    """Kostnad, klick och konverteringar per dag och kampanj. Kostnad i kontots valuta."""
    for w_start, w_end in windows(start, end, chunk_days):
        q = _CAMPAIGN_GAQL.format(start=w_start.isoformat(), end=w_end.isoformat())
        for r in _google_ads_stream(session, version, customer_id, q):
            c = r.get("campaign", {})
            yield {"d": r["segments"]["date"], "customer_id": _digits(customer_id), "campaign_id": str(c.get("id", "")),
                   "campaign_name": c.get("name", ""), "channel_type": c.get("advertisingChannelType", ""),
                   "currency": r.get("customer", {}).get("currencyCode", ""), **_gads_metrics(r.get("metrics", {}))}


def google_ads_product_rows(session, customer_id: str, start: date, end: date,
                            version: str = "v21", chunk_days: int = 31) -> Iterator[dict[str, Any]]:
    """Resultat per dag och produkt i Shopping och Performance Max. Kopplas till Shopify via item_id."""
    for w_start, w_end in windows(start, end, chunk_days):
        q = _PRODUCT_GAQL.format(start=w_start.isoformat(), end=w_end.isoformat())
        for r in _google_ads_stream(session, version, customer_id, q):
            s = r["segments"]
            yield {"d": s["date"], "customer_id": _digits(customer_id), "item_id": s.get("productItemId", ""),
                   "title": s.get("productTitle", ""), "brand": s.get("productBrand", ""),
                   "currency": r.get("customer", {}).get("currencyCode", ""), **_gads_metrics(r.get("metrics", {}))}


# ---------------------------------------------------------------------- Meta

# Metas "actions" listar samma köp under flera namn. Ta bara ett, i denna ordning, för att undvika dubbelräkning.
_PURCHASE_TYPES = ("omni_purchase", "purchase", "offsite_conversion.fb_pixel_purchase")
_LEAD_TYPES = ("lead", "onsite_conversion.lead_grouped", "offsite_conversion.fb_pixel_lead")


def _action_total(items: list[dict[str, Any]] | None, types: tuple[str, ...]) -> float:
    by_type = {i.get("action_type"): float(i.get("value", 0)) for i in items or []}
    for t in types:
        if t in by_type:
            return by_type[t]
    return 0.0


def meta_session(token: str):
    import requests

    session = requests.Session()
    session.headers["Authorization"] = f"Bearer {token}"
    return session


def meta_ads_rows(session, account_id: str, start: date, end: date, version: str = "v23.0",
                  page_size: int = 500) -> Iterator[dict[str, Any]]:
    """Utgift, klick och köp per dag och kampanj. Köp och köpvärde enligt Metas egen attribuering."""
    acct = account_id if account_id.startswith("act_") else f"act_{_digits(account_id)}"
    url: str | None = f"https://graph.facebook.com/{version}/{acct}/insights"
    params: dict[str, Any] | None = {
        "level": "campaign", "time_increment": 1, "limit": page_size,
        "time_range": json.dumps({"since": start.isoformat(), "until": end.isoformat()}),
        "fields": "campaign_id,campaign_name,spend,impressions,reach,clicks,actions,action_values,account_currency",
    }
    while url:
        for attempt in range(6):
            resp = session.get(url, params=params, timeout=120)
            err = (resp.json().get("error", {}) if resp.status_code >= 400 else {})
            if resp.status_code in (429, 500, 503) or err.get("code") in (4, 17, 32, 613):  # begränsning eller tillfälligt fel
                _sleep_retry(attempt)
                continue
            if resp.status_code >= 400:
                raise RuntimeError(f"Meta {acct} -> {resp.status_code}: {err.get('message', resp.text[:300])}")
            break
        else:
            raise RuntimeError(f"Meta {acct} misslyckades efter flera försök")
        data = resp.json()
        for r in data.get("data", []):
            yield {"d": r["date_start"], "account_id": acct.removeprefix("act_"), "campaign_id": r.get("campaign_id", ""),
                   "campaign_name": r.get("campaign_name", ""), "currency": r.get("account_currency", ""),
                   "spend": float(r.get("spend", 0)), "impressions": int(r.get("impressions", 0)),
                   "reach": int(r.get("reach", 0)), "clicks": int(r.get("clicks", 0)),
                   "purchases": _action_total(r.get("actions"), _PURCHASE_TYPES),
                   "purchase_value": _action_total(r.get("action_values"), _PURCHASE_TYPES),
                   "leads": _action_total(r.get("actions"), _LEAD_TYPES)}
        url, params = data.get("paging", {}).get("next"), None  # next-länken bär redan alla parametrar
