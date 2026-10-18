"""Veckorapport och larm för en butik, byggda på tillväxtvyerna (se growth_sql.py).

`site-audit weekly --site <sajt>` läser vyerna i BigQuery och skriver en rapport i Markdown med nyckeltal per marknad,
kanaler som förändrats, produkter vars annonsvärde fallit (och om de finns i lager) samt larm. Samma rapport varje vecka
gör att förändringar syns tidigt och att jämförelser görs på samma sätt varje gång.

Perioder, räknat från dagens datum (i dag räknas inte med, eftersom dagen inte är komplett):
  denna vecka   = de 7 senaste hela dagarna
  förra veckan  = de 7 dagarna innan
  basnivå       = de 28 dagarna före det, som veckosnitt (delat med 4)

Belopp ligger i marknadens valuta och summeras aldrig över marknader.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any

# Gränsvärden för larm. Procent mot basnivån (veckosnittet de 28 dagarna före förra veckan).
STALE_DAYS = 2
ORDERS_DROP = -25.0
SESSIONS_DROP = -20.0
MER_DROP = -20.0
ORDER_RATE_DROP = -15.0
AD_COST_DROP = -30.0
AD_COST_RISE = 40.0
STOCKOUT_MIN_CLICKS = 30  # klick på en produkt utan lager som räknas som läckage
VANISHED_MIN_VALUE = 3000.0  # en produkt som tidigare gav minst så mycket annonsvärde och nu inget
UNMATCHED_SHARE = 0.5


@dataclass
class Alert:
    level: str  # "hög", "medel" eller "info"
    source: str
    text: str


@dataclass
class Report:
    markdown: str
    alerts: list[Alert] = field(default_factory=list)

    @property
    def has_high(self) -> bool:
        return any(a.level == "hög" for a in self.alerts)


def periods(today: date) -> dict[str, tuple[date, date]]:
    return {"w1": (today - timedelta(days=7), today - timedelta(days=1)),
            "w0": (today - timedelta(days=14), today - timedelta(days=8)),
            "base": (today - timedelta(days=42), today - timedelta(days=15))}


def pct(new: float | None, old: float | None) -> float | None:
    if new is None or old in (None, 0):
        return None
    return (new - old) / old * 100


def _f(value: Any) -> float:
    return float(value) if value is not None else 0.0


def _in(d: date, window: tuple[date, date]) -> bool:
    return window[0] <= d <= window[1]


def kpis(rows: list[dict[str, Any]], window: tuple[date, date], weeks: float = 1.0) -> dict[str, float | None]:
    """Nyckeltal för ett fönster, per vecka (delat med antal veckor). Orderfrekvens räknas bara på dagar där besök finns."""
    sel = [r for r in rows if _in(r["d"], window)]
    orders = sum(_f(r.get("orders")) for r in sel)
    revenue = sum(_f(r.get("revenue")) for r in sel)
    google, meta = sum(_f(r.get("google_cost")) for r in sel), sum(_f(r.get("meta_cost")) for r in sel)
    with_sessions = [r for r in sel if r.get("sessions") is not None]
    sessions = sum(_f(r["sessions"]) for r in with_sessions)
    orders_ws = sum(_f(r.get("orders")) for r in with_sessions)
    ad = google + meta
    return {"orders": orders / weeks, "revenue": revenue / weeks, "sessions": sessions / weeks if with_sessions else None,
            "ad_cost": ad / weeks, "google_cost": google / weeks, "meta_cost": meta / weeks,
            "mer": revenue / ad if ad else None, "order_rate": orders_ws / sessions * 100 if sessions else None,
            "days_with_sessions": len(with_sessions)}


def freshness_sql(site) -> str:
    p, ds, key = site.bq_project, site.bq_dataset, site.table_key
    parts = []
    if site.shopify_dataset:
        parts.append(f"SELECT 'Shopify-ordrar' AS source, MAX(DATE(created_at, 'Europe/Stockholm')) AS latest FROM `{site.shopify_dataset}.orders`")
    if site.ga4_property_id:
        parts.append(f"SELECT 'GA4 landningssidor', MAX(d) FROM `{p}.{ds}.ga4_landing_daily_{key}`")
        parts.append(f"SELECT 'GA4 kanaler', MAX(d) FROM `{p}.{ds}.ga4_channel_daily_{key}`")
    if site.google_ads_customer_ids:
        parts.append(f"SELECT 'Google Ads kampanjer', MAX(d) FROM `{p}.{ds}.google_ads_daily_{key}`")
        parts.append(f"SELECT 'Google Ads produkter', MAX(d) FROM `{p}.{ds}.google_ads_products_daily_{key}`")
    if site.meta_ad_account_ids:
        parts.append(f"SELECT 'Meta-annonser', MAX(d) FROM `{p}.{ds}.meta_ads_daily_{key}`")
    return "\nUNION ALL\n".join(parts)


def daily_sql(site, today: date) -> str:
    p, ds, key = site.bq_project, site.bq_dataset, site.table_key
    start = periods(today)["base"][0]
    return (f"SELECT d, market, orders, revenue, sessions, google_cost, meta_cost, google_value, meta_value\n"
            f"FROM `{p}.{ds}.growth_daily_{key}` WHERE d >= '{start.isoformat()}'")


def channel_sql(site, today: date) -> str:
    p, ds, key = site.bq_project, site.bq_dataset, site.table_key
    per = periods(today)
    w1, base = per["w1"], per["base"]
    return (f"SELECT hostname, channel,\n"
            f"  SUM(IF(d BETWEEN '{w1[0]}' AND '{w1[1]}', sessions, 0)) AS s1,\n"
            f"  SUM(IF(d BETWEEN '{base[0]}' AND '{base[1]}', sessions, 0)) AS sb,\n"
            f"  SUM(IF(d BETWEEN '{w1[0]}' AND '{w1[1]}', purchases, 0)) AS p1,\n"
            f"  SUM(IF(d BETWEEN '{base[0]}' AND '{base[1]}', purchases, 0)) AS pb\n"
            f"FROM `{p}.{ds}.ga4_channel_daily_{key}` WHERE d BETWEEN '{base[0]}' AND '{w1[1]}' GROUP BY 1, 2")


def product_sql(site, today: date) -> str:
    p, ds, key = site.bq_project, site.bq_dataset, site.table_key
    per = periods(today)
    w1, w0 = per["w1"], per["w0"]
    return (f"SELECT market, item_id, ANY_VALUE(COALESCE(shopify_title, ads_title)) AS title,\n"
            f"  SUM(IF(d BETWEEN '{w1[0]}' AND '{w1[1]}', conversions_value, 0)) AS v1,\n"
            f"  SUM(IF(d BETWEEN '{w0[0]}' AND '{w0[1]}', conversions_value, 0)) AS v0,\n"
            f"  SUM(IF(d BETWEEN '{w1[0]}' AND '{w1[1]}', clicks, 0)) AS c1,\n"
            f"  SUM(IF(d BETWEEN '{w0[0]}' AND '{w0[1]}', clicks, 0)) AS c0,\n"
            f"  ARRAY_AGG(inventory_quantity IGNORE NULLS ORDER BY d DESC LIMIT 1)[SAFE_OFFSET(0)] AS stock,\n"
            f"  LOGICAL_OR(matched) AS matched, ANY_VALUE(status) AS status\n"
            f"FROM `{p}.{ds}.growth_product_daily_{key}` WHERE d BETWEEN '{w0[0]}' AND '{w1[1]}' GROUP BY 1, 2")


def _fmt(v: float | None, digits: int = 0, suffix: str = "") -> str:
    if v is None:
        return "–"
    return f"{v:,.{digits}f}".replace(",", " ").replace(".", ",").replace("-", "−") + suffix


def _chg(v: float | None) -> str:
    if v is None:
        return "–"
    return "0 %" if round(v) == 0 else f"{v:+.0f} %".replace("-", "−")


def check_freshness(rows: list[dict[str, Any]], today: date) -> list[Alert]:
    out = []
    for r in rows:
        latest = r.get("latest")
        if latest is None:
            out.append(Alert("hög", r["source"], "Tabellen saknar data."))
        elif (today - latest).days > STALE_DAYS + 1:  # i går är normalt senaste hela dag
            out.append(Alert("hög", r["source"], f"Senaste dag är {latest.isoformat()}, alltså {(today - latest).days} dagar sedan. Hämtningen verkar ha stannat."))
    return out


def check_kpis(market: str, w1: dict, base: dict) -> list[Alert]:
    out = []
    checks = [("orders", "Ordrar", ORDERS_DROP, "hög"), ("sessions", "Besök", SESSIONS_DROP, "medel"),
              ("mer", "Intäkt per annonskrona (MER)", MER_DROP, "hög"), ("order_rate", "Ordrar per besök", ORDER_RATE_DROP, "medel")]
    for key, label, limit, level in checks:
        c = pct(w1[key], base[key])
        if c is not None and c <= limit:
            out.append(Alert(level, market, f"{label} är {_chg(c)} mot veckosnittet de fyra veckorna innan (gräns {limit:.0f} %).".replace("-", "−")))
    c = pct(w1["ad_cost"], base["ad_cost"])
    if c is not None and (c <= AD_COST_DROP or c >= AD_COST_RISE):
        out.append(Alert("medel", market, f"Annonskostnaden är {_chg(c)} mot veckosnittet. Kontrollera budget, mål och status i annonskontona."))
    return out


def check_products(rows: list[dict[str, Any]]) -> list[Alert]:
    out = []
    if rows:
        clicks = sum(_f(r["c1"]) + _f(r["c0"]) for r in rows)
        unmatched = sum(_f(r["c1"]) + _f(r["c0"]) for r in rows if not r.get("matched"))
        if clicks and unmatched / clicks > UNMATCHED_SHARE:
            out.append(Alert("info", "Produkter", f"{unmatched / clicks:.0%} av annonsklicken kunde inte kopplas till en Shopify-variant, så lagerkontrollen är ofullständig. Kontrollera att annonsflödets id motsvarar variantens id."))
    for r in rows:
        title = (r.get("title") or r["item_id"])[:70]
        stock = r.get("stock")
        if r.get("matched") and stock is not None and stock <= 0 and _f(r["c1"]) >= STOCKOUT_MIN_CLICKS:
            out.append(Alert("hög", f"Produkt {r['market']}", f"{title}: {int(_f(r['c1']))} annonsklick förra veckan men lagersaldo {int(stock)}. Pausa i annonsflödet eller fyll på."))
        elif _f(r["v0"]) >= VANISHED_MIN_VALUE and _f(r["v1"]) == 0 and _f(r["c1"]) < 0.5 * _f(r["c0"]):
            out.append(Alert("medel", f"Produkt {r['market']}", f"{title}: annonsvärdet föll från {_fmt(r['v0'])} till 0 och klicken från {int(_f(r['c0']))} till {int(_f(r['c1']))}. Annonserna verkar ha slutat visa produkten (lager, pris, flöde eller status)."))
    return out


def build_report(store, site, today: date | None = None) -> Report:
    today = today or date.today()
    per = periods(today)
    alerts: list[Alert] = []
    lines = [f"# Tillväxtrapport: {site.name}", "",
             f"Vecka {per['w1'][0].isoformat()} – {per['w1'][1].isoformat()} mot veckan innan och mot veckosnittet de fyra veckorna dessförinnan "
             f"({per['base'][0].isoformat()} – {per['base'][1].isoformat()}). Dagens datum ({today.isoformat()}) är inte med. "
             "Belopp i marknadens egen valuta och summeras inte över marknader.", ""]

    alerts += check_freshness(store.query(freshness_sql(site)), today)

    daily = store.query(daily_sql(site, today))
    markets = sorted({r["market"] for r in daily})
    lines += ["## Nyckeltal per marknad", ""]
    for m in markets:
        rows = [r for r in daily if r["market"] == m]
        w1, w0, base = kpis(rows, per["w1"]), kpis(rows, per["w0"]), kpis(rows, per["base"], weeks=4)
        alerts += check_kpis(m, w1, base)
        lines += [f"### {m}", "", "| Mått | Denna vecka | Förra veckan | Veckosnitt (4 v) | Mot förra | Mot snitt |", "|---|---|---|---|---|---|"]
        for key, label, d in [("orders", "Ordrar", 0), ("revenue", "Omsättning", 0), ("sessions", "Besök (GA4)", 0),
                              ("order_rate", "Ordrar per besök, %", 2), ("google_cost", "Google-kostnad", 0),
                              ("meta_cost", "Meta-kostnad", 0), ("mer", "MER (omsättning / annonskostnad)", 2)]:
            lines.append(f"| {label} | {_fmt(w1[key], d)} | {_fmt(w0[key], d)} | {_fmt(base[key], d)} | {_chg(pct(w1[key], w0[key]))} | {_chg(pct(w1[key], base[key]))} |")
        lines.append("")
        missing = 7 - w1["days_with_sessions"]
        if missing > 0:
            lines += [f"*Besöksdata saknas för {missing} av de 7 dagarna, så besök och ordrar per besök bygger på färre dagar.*", ""]

    if site.ga4_property_id:
        try:
            ch = store.query(channel_sql(site, today))
        except Exception as exc:  # noqa: BLE001 - rapporten ska gå att läsa även om en tabell saknas
            ch = []
            alerts.append(Alert("medel", "GA4 kanaler", f"Kunde inte läsa kanaltabellen: {exc}"))
        movers = sorted(({"host": r["hostname"], "channel": r["channel"], "s1": _f(r["s1"]), "sb": _f(r["sb"]) / 4,
                          "delta": _f(r["s1"]) - _f(r["sb"]) / 4} for r in ch), key=lambda x: x["delta"])
        if movers:
            lines += ["## Kanaler som förändrats mest (besök per vecka mot veckosnittet)", "",
                      "| Domän | Kanal | Denna vecka | Snitt | Förändring |", "|---|---|---|---|---|"]
            for x in movers[:5] + [m for m in movers[-3:] if m["delta"] > 0]:
                lines.append(f"| {x['host']} | {x['channel']} | {_fmt(x['s1'])} | {_fmt(x['sb'])} | {_fmt(x['delta'])} ({_chg(pct(x['s1'], x['sb']))}) |")
            lines.append("")

    if site.google_ads_customer_ids and site.shopify_dataset:
        try:
            prod = store.query(product_sql(site, today))
        except Exception as exc:  # noqa: BLE001
            prod = []
            alerts.append(Alert("medel", "Produkter", f"Kunde inte läsa produktvyn: {exc}"))
        alerts += check_products(prod)
        losers = sorted(prod, key=lambda r: _f(r["v1"]) - _f(r["v0"]))[:5]
        if losers:
            lines += ["## Produkter med största fall i annonsvärde (förra veckan mot denna)", "",
                      "| Marknad | Produkt | Värde förra | Värde nu | Klick förra | Klick nu | Lager |", "|---|---|---|---|---|---|---|"]
            for r in losers:
                stock = r.get("stock")
                lines.append(f"| {r['market']} | {(r.get('title') or r['item_id'])[:60]} | {_fmt(r['v0'])} | {_fmt(r['v1'])} | "
                             f"{_fmt(r['c0'])} | {_fmt(r['c1'])} | {'okänt' if stock is None else int(stock)} |")
            lines.append("")

    order = {"hög": 0, "medel": 1, "info": 2}
    alerts.sort(key=lambda a: order[a.level])
    lines += ["## Larm", ""]
    lines += [f"- **{a.level}** ({a.source}): {a.text}" for a in alerts] or ["Inga larm."]
    lines += ["", "*Annonsernas konverteringsvärde är plattformens egen tillskrivning och överlappar mellan Google och Meta. Shopify-omsättningen är facit.*", ""]
    return Report("\n".join(lines), alerts)
