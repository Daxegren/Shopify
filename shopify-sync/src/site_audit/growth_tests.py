"""Testlogg: varje åtgärd i tillväxtarbetet loggas med hypotes, datum och mätare, och utvärderas efter en bestämd tid.

Det gör att man lär sig av det man gjort, och inte bara rapporterar vad som hänt. Utvärderingen jämför mätaren i fönstret
efter starten med lika många dagar före, och drar av förändringen i övriga marknader i butiken som en grov kontroll
(så att säsong och marknadsläge inte tillskrivs åtgärden). Det är ett underlag för bedömning, inte ett bevis.
"""

from __future__ import annotations

import uuid
from datetime import date, datetime, timedelta, timezone
from typing import Any
from urllib.parse import urlsplit

from .growth_report import kpis, pct

METRICS = {"orders": "Ordrar", "revenue": "Omsättning", "sessions": "Besök", "ad_cost": "Annonskostnad", "mer": "MER (omsättning / annonskostnad)",
           "order_rate": "Ordrar per besök, %",
           "gsc_clicks": "Klick i Google (Search Console, per sida)", "gsc_impressions": "Visningar i Google (Search Console, per sida)"}
GSC_LAG_DAYS = 3  # Search Console är slutgiltig först efter ca tre dagar
CHANNELS = ("google_ads", "meta", "email", "site", "pris", "sortiment", "annat")


def ddl(dataset: str) -> str:
    return (f"CREATE TABLE IF NOT EXISTS `{dataset}.growth_tests` (test_id STRING NOT NULL, store STRING, created_at TIMESTAMP, "
            "start_date DATE, evaluate_days INT64, channel STRING, market STRING, metric STRING, expected_change_pct FLOAT64, "
            "hypothesis STRING, action STRING, owner STRING, status STRING, result_pct FLOAT64, control_pct FLOAT64, "
            "uplift_pct FLOAT64, conclusion STRING, evaluated_at TIMESTAMP, pages STRING)")


def ddl_migrate(dataset: str) -> str:
    """Äldre loggtabeller saknar kolumnen pages (adressfragment för sidmått)."""
    return f"ALTER TABLE `{dataset}.growth_tests` ADD COLUMN IF NOT EXISTS pages STRING"


def is_gsc_metric(metric: str) -> bool:
    return metric.startswith("gsc_")


def _q(value: str) -> str:
    return "'" + value.replace("\\", "\\\\").replace("'", "\\'") + "'"


def add_test(store, site, *, start: date, channel: str, metric: str, hypothesis: str, action: str, market: str | None = None,
             expected_pct: float | None = None, days: int = 28, owner: str | None = None, pages: list[str] | None = None) -> str:
    if metric not in METRICS:
        raise ValueError(f"Okänd mätare {metric}. Välj bland {', '.join(METRICS)}.")
    if channel not in CHANNELS:
        raise ValueError(f"Okänd kanal {channel}. Välj bland {', '.join(CHANNELS)}.")
    if not 7 <= days <= 90:
        raise ValueError("Utvärderingsfönstret ska vara 7–90 dagar.")
    pages = [p.strip() for p in (pages or []) if p.strip()]
    if is_gsc_metric(metric) and not pages:
        raise ValueError("Sidmått (gsc_clicks, gsc_impressions) kräver minst en sida, t.ex. --pages /collections/crosstrainer-kondition")
    test_id = uuid.uuid4().hex[:8]
    store.client.query(ddl(store.dataset)).result()
    store.client.query(ddl_migrate(store.dataset)).result()
    sql = (f"INSERT INTO `{store.dataset}.growth_tests` (test_id, store, created_at, start_date, evaluate_days, channel, market, metric, "
           f"expected_change_pct, hypothesis, action, owner, status, pages) VALUES ({_q(test_id)}, {_q(site.table_key)}, CURRENT_TIMESTAMP(), "
           f"DATE '{start.isoformat()}', {days}, {_q(channel)}, {_q(market) if market else 'NULL'}, {_q(metric)}, "
           f"{expected_pct if expected_pct is not None else 'NULL'}, {_q(hypothesis)}, {_q(action)}, {_q(owner) if owner else 'NULL'}, 'planerad', "
           f"{_q(','.join(pages)) if pages else 'NULL'})")
    store.client.query(sql).result()
    return test_id


def list_tests(store, site) -> list[dict[str, Any]]:
    store.client.query(ddl(store.dataset)).result()
    store.client.query(ddl_migrate(store.dataset)).result()
    return store.query(f"SELECT * FROM `{store.dataset}.growth_tests` WHERE store = {_q(site.table_key)} ORDER BY start_date DESC, created_at DESC")


def _window(start: date, days: int) -> tuple[date, date]:
    return start, start + timedelta(days=days - 1)


def evaluate(rows_by_market: dict[str, list[dict[str, Any]]], test: dict[str, Any], today: date) -> dict[str, Any]:
    """Förändring i mätaren efter start mot lika många dagar före, för testets marknad, och kontroll i övriga marknader."""
    days = int(test["evaluate_days"])
    start: date = test["start_date"]
    after = _window(start, days)
    before = (start - timedelta(days=days), start - timedelta(days=1))
    metric, market = test["metric"], test.get("market")
    complete = after[1] <= today - timedelta(days=1)

    def change(markets: list[str]) -> float | None:
        rows = [r for m in markets for r in rows_by_market.get(m, [])]
        a, b = kpis(rows, after)[metric], kpis(rows, before)[metric]
        return pct(a, b)

    target = [market] if market else list(rows_by_market)
    control = [m for m in rows_by_market if m not in target]
    result = change(target)
    ctrl = change(control) if control else None
    uplift = result - ctrl if result is not None and ctrl is not None else result
    exp = test.get("expected_change_pct")
    if not complete:
        verdict = f"Fönstret är inte slut (slutar {after[1].isoformat()}). Preliminärt resultat."
    elif result is None:
        verdict = "Data saknas för mätaren i något av fönstren."
    elif exp is not None and uplift is not None and uplift >= exp:
        verdict = "Förväntat utfall uppnåtts efter avdrag för kontroll."
    elif uplift is not None and uplift > 0:
        verdict = "Förbättring, men under det förväntade. Bedöm om den är värd att behålla."
    else:
        verdict = "Ingen förbättring efter avdrag för kontroll."
    return {"result_pct": result, "control_pct": ctrl, "uplift_pct": uplift, "complete": complete, "verdict": verdict,
            "after": after, "before": before}


def gsc_rows_sql(table: str, first: date, last: date) -> str:
    """Klick och visningar per dag och adress ur Search Console-tabellen eller vyn (data_date, url, clicks, impressions)."""
    return (f"SELECT data_date AS d, url, SUM(clicks) AS clicks, SUM(impressions) AS impressions FROM `{table}` "
            f"WHERE data_date BETWEEN '{first.isoformat()}' AND '{last.isoformat()}' GROUP BY 1, 2")


def _path(url: str) -> str:
    return urlsplit(url or "").path.lower()


def evaluate_pages(rows: list[dict[str, Any]], test: dict[str, Any], today: date) -> dict[str, Any]:
    """Sidmått ur Search Console: valda sidor (adressfragment i testets kolumn pages) efter start mot lika många dagar före.

    Kontroll: övriga sidor med samma första led i adressen (till exempel övriga /collections/), så att säsong och Googles
    förändringar inte tillskrivs åtgärden. Sidor som ändrats i samma test ingår inte i kontrollen."""
    days = int(test["evaluate_days"])
    start: date = test["start_date"]
    after = _window(start, days)
    before = (start - timedelta(days=days), start - timedelta(days=1))
    field = "clicks" if test["metric"] == "gsc_clicks" else "impressions"
    fragments = [f.strip().lower() for f in str(test.get("pages") or "").split(",") if f.strip()]
    if not fragments:
        raise ValueError("Testet saknar sidor (kolumnen pages).")
    sections = {f.strip("/").split("/")[0] for f in fragments if f.strip("/")}

    def is_target(path: str) -> bool:
        return any(f in path for f in fragments)

    def total(selector, window) -> float:
        return sum(float(r.get(field) or 0) for r in rows if window[0] <= r["d"] <= window[1] and selector(_path(r["url"])))

    def is_control(path: str) -> bool:
        return not is_target(path) and path.strip("/").split("/")[0] in sections

    result = pct(total(is_target, after), total(is_target, before))
    control_total_before = total(is_control, before)
    ctrl = pct(total(is_control, after), control_total_before) if control_total_before else None
    uplift = result - ctrl if result is not None and ctrl is not None else result
    complete = after[1] <= today - timedelta(days=GSC_LAG_DAYS)
    exp = test.get("expected_change_pct")
    if not complete:
        verdict = f"Fönstret är inte slut (slutar {after[1].isoformat()}, Search Console är slutgiltig efter {GSC_LAG_DAYS} dagar). Preliminärt resultat."
    elif result is None:
        verdict = "Data saknas för sidorna före åtgärden (noll klick eller visningar), så förändringen går inte att beräkna."
    elif exp is not None and uplift is not None and uplift >= exp:
        verdict = "Förväntat utfall uppnåtts efter avdrag för kontroll."
    elif uplift is not None and uplift > 0:
        verdict = "Förbättring, men under det förväntade. Bedöm om den är värd att behålla."
    else:
        verdict = "Ingen förbättring efter avdrag för kontroll."
    return {"result_pct": result, "control_pct": ctrl, "uplift_pct": uplift, "complete": complete, "verdict": verdict,
            "after": after, "before": before, "control_label": "övriga sidor av samma typ"}


def save_evaluation(store, test_id: str, ev: dict[str, Any]) -> None:
    def num(v):
        return "NULL" if v is None else f"{v:.4f}"

    status = "utvärderad" if ev["complete"] else "pågår"
    store.client.query(
        f"UPDATE `{store.dataset}.growth_tests` SET status = {_q(status)}, result_pct = {num(ev['result_pct'])}, "
        f"control_pct = {num(ev['control_pct'])}, uplift_pct = {num(ev['uplift_pct'])}, conclusion = {_q(ev['verdict'])}, "
        f"evaluated_at = CURRENT_TIMESTAMP() WHERE test_id = {_q(test_id)}").result()


def format_evaluation(test: dict[str, Any], ev: dict[str, Any]) -> str:
    f = lambda v: "–" if v is None else f"{v:+.1f} %".replace("-", "−")  # noqa: E731
    return "\n".join([
        f"Test {test['test_id']}: {test['hypothesis']}",
        f"Åtgärd: {test['action']}",
        f"Mätare: {METRICS[test['metric']]}, marknad: {test.get('market') or 'alla'}, kanal: {test['channel']}"
        + (f", sidor: {test['pages']}" if test.get("pages") else ""),
        f"Före: {ev['before'][0]} – {ev['before'][1]}. Efter: {ev['after'][0]} – {ev['after'][1]}.",
        f"Förändring: {f(ev['result_pct'])}. Kontroll ({ev.get('control_label', 'övriga marknader')}): {f(ev['control_pct'])}. Netto: {f(ev['uplift_pct'])}"
        + (f". Förväntat: {f(test.get('expected_change_pct'))}." if test.get("expected_change_pct") is not None else "."),
        ev["verdict"]])


def now_utc() -> datetime:
    return datetime.now(timezone.utc)
