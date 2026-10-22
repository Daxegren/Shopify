"""Kontrollerar åtkomsten till varje datakälla för en butik med ett litet läsanrop. Ändrar ingenting.

`site-audit check-access --site <sajt>` ger en rad per källa: OK, saknas (inte konfigurerad) eller FEL med orsak.
Nyckelvärden skrivs aldrig ut; felmeddelanden kortas.
"""

from __future__ import annotations

import os
from datetime import date, timedelta
from typing import Callable


def _first(it) -> None:
    next(iter(it), None)


def probes(site, store) -> dict[str, tuple[bool, Callable[[], None]]]:
    """Källa -> (konfigurerad, anrop som ger fel om åtkomst saknas)."""
    from . import ads_api as a
    from . import google_api as g

    y = date.today() - timedelta(days=1)

    def shopify() -> None:
        store.query(f"SELECT 1 FROM `{site.shopify_dataset}.orders` LIMIT 1")

    def ga4() -> None:
        session = g.authorized_session([g.GA4_SCOPE])
        for pid in site.ga4_property_map():
            _first(g.ga4_rows(session, pid, y, y))

    def gads() -> None:
        token = os.environ.get(site.google_ads_developer_token_env)
        s = a.google_ads_session(token, site.google_ads_login_customer_id)
        for cid in site.google_ads_customer_ids:
            _first(a.google_ads_campaign_rows(s, cid, y, y, site.google_ads_api_version))

    def meta() -> None:
        token = os.environ.get(site.meta_token_env)
        if not token:
            raise RuntimeError(f"miljövariabeln {site.meta_token_env} saknas")
        s = a.meta_session(token)
        for acct in site.meta_ad_account_ids:
            _first(a.meta_ads_rows(s, acct, y, y, site.meta_api_version))

    def merchant() -> None:
        from . import merchant_api as m

        r = m.merchant_session().get(f"https://merchantapi.googleapis.com/products/{site.merchant_api_version}/accounts/"
                                     f"{site.merchant_account_id}/products", params={"pageSize": 1}, timeout=60)
        if r.status_code >= 400:
            raise RuntimeError(f"{r.status_code}: {r.text[:200]}")

    def klaviyo() -> None:
        from . import klaviyo_api as k

        key = os.environ.get(site.klaviyo_api_key_env)
        if not key:
            raise RuntimeError(f"miljövariabeln {site.klaviyo_api_key_env} saknas")
        k.find_metric_id(k.klaviyo_session(key, site.klaviyo_revision))

    return {"shopify (BigQuery)": (bool(site.shopify_dataset), shopify), "ga4": (bool(site.ga4_property_id), ga4),
            "google-ads": (bool(site.google_ads_customer_ids), gads), "meta-ads": (bool(site.meta_ad_account_ids), meta),
            "merchant": (bool(site.merchant_account_id), merchant), "klaviyo": (site.klaviyo_enabled, klaviyo)}


def check_access(site, store, overrides: dict | None = None) -> list[tuple[str, str, str]]:
    """Ger (källa, status, detalj). status är OK, saknas eller FEL."""
    out = []
    for name, (configured, fn) in (overrides or probes(site, store)).items():
        if not configured:
            out.append((name, "saknas", "inte konfigurerad"))
            continue
        try:
            fn()
            out.append((name, "OK", ""))
        except Exception as exc:  # noqa: BLE001 - varje källa rapporteras för sig
            out.append((name, "FEL", str(exc).replace("\n", " ")[:200]))
    return out


def format_access(site_name: str, results: list[tuple[str, str, str]]) -> str:
    lines = [f"Åtkomst för {site_name}:"]
    lines += [f"  {n:<20} {s:<7} {d}".rstrip() for n, s, d in results]
    return "\n".join(lines)
