"""Testlogg: varje åtgärd i tillväxtarbetet loggas med hypotes, datum och mätare, och utvärderas efter en bestämd tid.

Det gör att man lär sig av det man gjort, och inte bara rapporterar vad som hänt. Utvärderingen jämför mätaren i fönstret
efter starten med lika många dagar före, och drar av förändringen i övriga marknader i butiken som en grov kontroll
(så att säsong och marknadsläge inte tillskrivs åtgärden). Det är ett underlag för bedömning, inte ett bevis.
"""

from __future__ import annotations

import uuid
from datetime import date, datetime, timedelta, timezone
from typing import Any

from .growth_report import kpis, pct

METRICS = {"orders": "Ordrar", "revenue": "Omsättning", "sessions": "Besök", "ad_cost": "Annonskostnad", "mer": "MER (omsättning / annonskostnad)",
           "order_rate": "Ordrar per besök, %"}
CHANNELS = ("google_ads", "meta", "email", "site", "pris", "sortiment", "annat")


def ddl(dataset: str) -> str:
    return (f"CREATE TABLE IF NOT EXISTS `{dataset}.growth_tests` (test_id STRING NOT NULL, store STRING, created_at TIMESTAMP, "
            "start_date DATE, evaluate_days INT64, channel STRING, market STRING, metric STRING, expected_change_pct FLOAT64, "
            "hypothesis STRING, action STRING, owner STRING, status STRING, result_pct FLOAT64, control_pct FLOAT64, "
            "uplift_pct FLOAT64, conclusion STRING, evaluated_at TIMESTAMP)")


def _q(value: str) -> str:
    return "'" + value.replace("\\", "\\\\").replace("'", "\\'") + "'"


def add_test(store, site, *, start: date, channel: str, metric: str, hypothesis: str, action: str, market: str | None = None,
             expected_pct: float | None = None, days: int = 28, owner: str | None = None) -> str:
    if metric not in METRICS:
        raise ValueError(f"Okänd mätare {metric}. Välj bland {', '.join(METRICS)}.")
    if channel not in CHANNELS:
        raise ValueError(f"Okänd kanal {channel}. Välj bland {', '.join(CHANNELS)}.")
    if not 7 <= days <= 90:
        raise ValueError("Utvärderingsfönstret ska vara 7–90 dagar.")
    test_id = uuid.uuid4().hex[:8]
    store.client.query(ddl(store.dataset)).result()
    sql = (f"INSERT INTO `{store.dataset}.growth_tests` (test_id, store, created_at, start_date, evaluate_days, channel, market, metric, "
           f"expected_change_pct, hypothesis, action, owner, status) VALUES ({_q(test_id)}, {_q(site.table_key)}, CURRENT_TIMESTAMP(), "
           f"DATE '{start.isoformat()}', {days}, {_q(channel)}, {_q(market) if market else 'NULL'}, {_q(metric)}, "
           f"{expected_pct if expected_pct is not None else 'NULL'}, {_q(hypothesis)}, {_q(action)}, {_q(owner) if owner else 'NULL'}, 'planerad')")
    store.client.query(sql).result()
    return test_id


def list_tests(store, site) -> list[dict[str, Any]]:
    store.client.query(ddl(store.dataset)).result()
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
        f"Mätare: {METRICS[test['metric']]}, marknad: {test.get('market') or 'alla'}, kanal: {test['channel']}",
        f"Före: {ev['before'][0]} – {ev['before'][1]}. Efter: {ev['after'][0]} – {ev['after'][1]}.",
        f"Förändring: {f(ev['result_pct'])}. Kontroll (övriga marknader): {f(ev['control_pct'])}. Netto: {f(ev['uplift_pct'])}"
        + (f". Förväntat: {f(test.get('expected_change_pct'))}." if test.get("expected_change_pct") is not None else "."),
        ev["verdict"]])


def now_utc() -> datetime:
    return datetime.now(timezone.utc)
