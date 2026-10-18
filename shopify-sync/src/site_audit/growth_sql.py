"""Genererar BigQuery-vyerna för tillväxtarbetet från sites.toml.

En butik (sajten med growth_views = true) får två vyer i sitt projekt:
  growth_ads_daily_<nyckel>  alla annonser (Google Ads och Meta) på samma form
  growth_daily_<nyckel>      en rad per dag och marknad: ordrar, omsättning, besök, annonskostnad, MER

Över alla butiker skapas en portfölj-vy (portfolio_daily) och en veckovy (portfolio_weekly), så att varje butik
kan analyseras för sig och jämföras med de andra. Portföljen innehåller bara dagssummor per butik och marknad,
aldrig kunduppgifter, eftersom butikerna kan tillhöra olika bolag med eget personuppgiftsansvar.

Belopp ligger i marknadens valuta. De summeras aldrig över marknader utan omräkning; jämförelser görs med kvoter
och index (MER, andel besök som köper, förändring mot föregående period).
"""

from __future__ import annotations

import re

from .config import SiteConfig

_SAFE = re.compile(r"^[A-Za-z0-9_.\-]+$")
_TLD_MARKETS = {".se": "SE", ".dk": "DK", ".fi": "FI", ".no": "NO"}


def _safe(value: str, what: str) -> str:
    if not _SAFE.match(value):
        raise ValueError(f"Ogiltigt värde för {what}: {value!r}")
    return value


def _lit(value: str) -> str:
    """SQL-sträng. Värden kommer från sites.toml (betrodd), men citattecken och backslash hanteras ändå."""
    return "'" + value.replace("\\", "\\\\").replace("'", "\\'") + "'"


def _case(column: str, mapping: dict[str, str]) -> str:
    whens = " ".join(f"WHEN {_lit(k)} THEN {_lit(v)}" for k, v in mapping.items())
    return f"CASE {column} {whens} ELSE {column} END"


def _hostname_market(site: SiteConfig) -> str:
    if site.hostname_markets:
        whens = " ".join(f"WHEN {_lit(h.lower())} THEN {_lit(m)}" for h, m in site.hostname_markets.items())
        return f"CASE hostname {whens} ELSE 'OTHER' END"
    whens = " ".join(f"WHEN ENDS_WITH(hostname, {_lit(t)}) THEN {_lit(m)}" for t, m in _TLD_MARKETS.items())
    return f"CASE {whens} ELSE 'OTHER' END"


def _currency_of_market(site: SiteConfig) -> dict[str, str]:
    out: dict[str, str] = {}
    for cur, market in site.currency_markets.items():
        out.setdefault(market, cur)
    return out


def store_sites(sites: dict[str, SiteConfig]) -> list[SiteConfig]:
    return [s for s in sites.values() if s.growth_views]


def _project(site: SiteConfig) -> str:
    if not site.bq_project:
        raise ValueError(f"bq_project saknas för {site.name}")
    return _safe(site.bq_project, "bq_project")


def store_sql(site: SiteConfig) -> str:
    p, ds, key = _project(site), _safe(site.bq_dataset, "bq_dataset"), _safe(site.table_key, "data_key")
    cur_case = lambda col: _case(col, site.currency_markets)  # noqa: E731
    ads: list[str] = []
    if site.google_ads_customer_ids:
        ads.append(f"SELECT d, 'google_ads' AS platform, {cur_case('currency')} AS market, currency,\n"
                   f"       campaign_id, campaign_name, channel_type AS campaign_type,\n"
                   f"       cost, impressions, clicks, conversions, conversions_value\n"
                   f"FROM `{p}.{ds}.google_ads_daily_{key}`")
    if site.meta_ad_account_ids:
        ads.append(f"SELECT d, 'meta' AS platform, {cur_case('currency')} AS market, currency,\n"
                   f"       campaign_id, campaign_name, CAST(NULL AS STRING) AS campaign_type,\n"
                   f"       spend AS cost, impressions, clicks, purchases AS conversions, purchase_value AS conversions_value\n"
                   f"FROM `{p}.{ds}.meta_ads_daily_{key}`")
    out = [f"-- Butik: {site.name} (nyckel {key})" + (f", bolag {site.company}" if site.company else "")]
    if ads:
        out.append(f"CREATE OR REPLACE VIEW `{p}.{ds}.growth_ads_daily_{key}` AS\n" + "\nUNION ALL\n".join(ads) + ";")

    ctes: list[str] = []
    joined: list[str] = []
    if site.shopify_dataset:
        ctes.append(f"orders AS (\n  SELECT DATE(created_at, 'Europe/Stockholm') AS d, {cur_case('presentment_currency')} AS market,\n"
                    f"         COUNT(*) AS orders, SUM(total_price_presentment) AS revenue\n"
                    f"  FROM `{_safe(site.shopify_dataset, 'shopify_dataset')}.orders`\n  WHERE cancelled_at IS NULL\n  GROUP BY 1, 2\n)")
        joined.append("orders")
    if site.ga4_property_id:
        ctes.append(f"ga4 AS (\n  SELECT d, {_hostname_market(site)} AS market, SUM(sessions) AS sessions, SUM(purchases) AS ga4_purchases\n"
                    f"  FROM `{p}.{ds}.ga4_landing_daily_{key}`\n  GROUP BY 1, 2\n)")
        joined.append("ga4")
    if ads:
        ctes.append(f"ads AS (\n  SELECT d, market,\n"
                    f"         SUM(IF(platform = 'google_ads', cost, 0)) AS google_cost, SUM(IF(platform = 'meta', cost, 0)) AS meta_cost,\n"
                    f"         SUM(IF(platform = 'google_ads', conversions_value, 0)) AS google_value, SUM(IF(platform = 'meta', conversions_value, 0)) AS meta_value,\n"
                    f"         SUM(clicks) AS ad_clicks\n  FROM `{p}.{ds}.growth_ads_daily_{key}`\n  GROUP BY 1, 2\n)")
        joined.append("ads")
    if joined:
        null = lambda t, n: f"CAST(NULL AS {t}) AS {n}"  # noqa: E731
        cols = {
            "orders": ["o.orders", "o.revenue"] if "orders" in joined else [null("INT64", "orders"), null("FLOAT64", "revenue")],
            "ga4": ["g.sessions", "g.ga4_purchases"] if "ga4" in joined else [null("INT64", "sessions"), null("INT64", "ga4_purchases")],
            "ads": [f"a.{c}" for c in ("google_cost", "meta_cost", "google_value", "meta_value", "ad_clicks")] if "ads" in joined
            else [null("FLOAT64", c) for c in ("google_cost", "meta_cost", "google_value", "meta_value")] + [null("INT64", "ad_clicks")],
        }
        alias = {"orders": "o", "ga4": "g", "ads": "a"}
        frm = f"{joined[0]} {alias[joined[0]]}" + "".join(f"\nFULL JOIN {j} {alias[j]} USING (d, market)" for j in joined[1:])
        select = ["d", "market"] + cols["orders"] + cols["ga4"] + cols["ads"] + [
            "SAFE_DIVIDE(" + ("o.revenue" if "orders" in joined else "CAST(NULL AS FLOAT64)")
            + ", IFNULL(" + ("a.google_cost" if "ads" in joined else "0") + ", 0) + IFNULL(" + ("a.meta_cost" if "ads" in joined else "0") + ", 0)) AS mer",
            "SAFE_DIVIDE(" + ("o.orders" if "orders" in joined else "CAST(NULL AS INT64)") + ", " + ("g.sessions" if "ga4" in joined else "CAST(NULL AS INT64)") + ") AS order_rate",
        ]
        out.append(f"CREATE OR REPLACE VIEW `{p}.{ds}.growth_daily_{key}` AS\nWITH " + ",\n".join(ctes)
                   + "\nSELECT " + ",\n       ".join(select) + f"\nFROM {frm};")
    return "\n\n".join(out)


def portfolio_sql(stores: list[SiteConfig], project: str | None = None, dataset: str = "portfolio") -> str:
    if not stores:
        raise ValueError("Ingen sajt har growth_views = true i konfigurationen.")
    pp, pd = _safe(project or _project(stores[0]), "portföljprojekt"), _safe(dataset, "portföljdataset")
    keys = [s.table_key for s in stores]
    if len(set(keys)) != len(keys):
        raise ValueError(f"Två butiker har samma nyckel: {keys}. Sätt data_key på sajterna.")
    parts = []
    for s in stores:
        p, ds, key = _project(s), _safe(s.bq_dataset, "bq_dataset"), _safe(s.table_key, "data_key")
        currency = _case("market", {m: c for m, c in _currency_of_market(s).items()}).replace(" ELSE market END", " END")
        parts.append(f"SELECT {_lit(key)} AS store, {_lit(s.company or '')} AS company, {_lit(s.vertical or '')} AS vertical, d, market,\n"
                     f"       {currency} AS currency, orders, revenue, sessions, ga4_purchases,\n"
                     f"       google_cost, meta_cost, google_value, meta_value, ad_clicks, mer, order_rate\n"
                     f"FROM `{p}.{ds}.growth_daily_{key}`")
    daily = f"CREATE OR REPLACE VIEW `{pp}.{pd}.portfolio_daily` AS\n" + "\nUNION ALL\n".join(parts) + ";"
    weekly = (f"CREATE OR REPLACE VIEW `{pp}.{pd}.portfolio_weekly` AS\n"
              "SELECT store, company, vertical, market, currency, DATE_TRUNC(d, ISOWEEK) AS week,\n"
              "       SUM(orders) AS orders, SUM(revenue) AS revenue, SUM(sessions) AS sessions,\n"
              "       IFNULL(SUM(google_cost), 0) + IFNULL(SUM(meta_cost), 0) AS ad_cost,\n"
              "       SAFE_DIVIDE(SUM(revenue), IFNULL(SUM(google_cost), 0) + IFNULL(SUM(meta_cost), 0)) AS mer,\n"
              "       SAFE_DIVIDE(SUM(orders), SUM(sessions)) AS order_rate\n"
              f"FROM `{pp}.{pd}.portfolio_daily`\nGROUP BY 1, 2, 3, 4, 5, 6;")
    return f"CREATE SCHEMA IF NOT EXISTS `{pp}.{pd}` OPTIONS (location = 'EU');\n\n{daily}\n\n{weekly}"


def growth_sql(sites: dict[str, SiteConfig], portfolio_project: str | None = None, portfolio_dataset: str = "portfolio") -> str:
    stores = store_sites(sites)
    if not stores:
        raise ValueError("Ingen sajt har growth_views = true i konfigurationen.")
    head = ("-- Genererad av  site-audit growth-sql  från sites.toml. Ändra inte för hand: ändra konfigurationen och generera om.\n"
            "-- Kör:  site-audit growth-sql | bq query --use_legacy_sql=false\n"
            "-- Belopp ligger i marknadens valuta och summeras inte över marknader. Se docs/tillvaxtdata.md och docs/flera-sajter.md.\n")
    return head + "\n" + "\n\n".join(store_sql(s) for s in stores) + "\n\n" + portfolio_sql(stores, portfolio_project, portfolio_dataset) + "\n"
