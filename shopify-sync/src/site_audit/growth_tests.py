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
# Utvärderingsfönster per åtgärdstyp (T38, beslutat 2026-10-27): SEO-texter 56 dagar, tekniska rättningar och omdirigeringar 28,
# annonser och pris 21 (spannet är 14–28). Fönstret sparas per test i kolumnen evaluate_days; kind är bara en etikett och ett förval.
KIND_WINDOWS = {"seo_text": 56, "technical": 28, "ads": 21, "price": 21}
DEFAULT_WINDOW_DAYS = 28  # äldre rader och tester utan åtgärdstyp
FINAL_AFTER_DAYS = 4  # Search Console är slutgiltig efter ca tre dagar; utvärdera tidigast fyra dagar efter att fönstret slutat


def ddl(dataset: str) -> str:
    return (f"CREATE TABLE IF NOT EXISTS `{dataset}.growth_tests` (test_id STRING NOT NULL, store STRING, created_at TIMESTAMP, "
            "start_date DATE, evaluate_days INT64, channel STRING, market STRING, metric STRING, expected_change_pct FLOAT64, "
            "hypothesis STRING, action STRING, owner STRING, status STRING, result_pct FLOAT64, control_pct FLOAT64, "
            "uplift_pct FLOAT64, conclusion STRING, evaluated_at TIMESTAMP, pages STRING, kind STRING)")


def ddl_migrate(dataset: str) -> str:
    """Äldre loggtabeller saknar kolumnen pages (adressfragment för sidmått) och kind (åtgärdstyp). Ett enda uttryck, så att
    ordningen på frågorna i add_test och list_tests är densamma som förut."""
    return f"ALTER TABLE `{dataset}.growth_tests` ADD COLUMN IF NOT EXISTS pages STRING, ADD COLUMN IF NOT EXISTS kind STRING"


def resolve_window(kind: str | None, days: int | None) -> int:
    """Fönstret i dagar: uttryckligt värde först, annars förvalet för åtgärdstypen, annars 28 dagar."""
    if kind is not None and kind not in KIND_WINDOWS:
        raise ValueError(f"Okänd åtgärdstyp {kind}. Välj bland {', '.join(KIND_WINDOWS)}.")
    if days is not None:
        return days
    return KIND_WINDOWS[kind] if kind else DEFAULT_WINDOW_DAYS


def window_days(test: dict[str, Any]) -> int:
    """Testets sparade fönster. Rader utan värde (äldre tabeller) ger 28 dagar."""
    v = test.get("evaluate_days")
    try:
        return int(v) if v is not None and v == v else DEFAULT_WINDOW_DAYS  # v == v utesluter NaN
    except (TypeError, ValueError):
        return DEFAULT_WINDOW_DAYS


def is_gsc_metric(metric: str) -> bool:
    return metric.startswith("gsc_")


def _q(value: str) -> str:
    return "'" + value.replace("\\", "\\\\").replace("'", "\\'") + "'"


def add_test(store, site, *, start: date, channel: str, metric: str, hypothesis: str, action: str, market: str | None = None,
             expected_pct: float | None = None, days: int | None = None, owner: str | None = None, pages: list[str] | None = None,
             kind: str | None = None) -> str:
    days = resolve_window(kind, days)
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
           f"expected_change_pct, hypothesis, action, owner, status, pages, kind) VALUES ({_q(test_id)}, {_q(site.table_key)}, CURRENT_TIMESTAMP(), "
           f"DATE '{start.isoformat()}', {days}, {_q(channel)}, {_q(market) if market else 'NULL'}, {_q(metric)}, "
           f"{expected_pct if expected_pct is not None else 'NULL'}, {_q(hypothesis)}, {_q(action)}, {_q(owner) if owner else 'NULL'}, 'planerad', "
           f"{_q(','.join(pages)) if pages else 'NULL'}, {_q(kind) if kind else 'NULL'})")
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
    days = window_days(test)
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
    days = window_days(test)
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


def _as_date(v: Any) -> date:
    if isinstance(v, datetime):
        return v.date()
    return v if isinstance(v, date) else date.fromisoformat(str(v)[:10])


def due_tests(tests: list[dict[str, Any]], today: date) -> tuple[list[dict[str, Any]], list[dict[str, Any]], int]:
    """Delar testloggen i (utvärderingsklara, ej klara än, antal redan utvärderade).

    Ett test är klart att utvärdera när startdatum + fönster + 4 dagar har nåtts (Search Console är då slutgiltig). Fönstrets sista
    dag är start + fönster − 1. Raderna får nycklarna window, window_last, ready_on, days_since_end och days_overdue."""
    due, waiting, done = [], [], 0
    for t in tests:
        if t.get("status") == "utvärderad":
            done += 1
            continue
        start, days = _as_date(t["start_date"]), window_days(t)
        last = start + timedelta(days=days - 1)
        ready = start + timedelta(days=days + FINAL_AFTER_DAYS)
        row = {**t, "window": days, "window_last": last, "ready_on": ready,
               "days_since_end": (today - last).days, "days_overdue": (today - ready).days}
        (due if today >= ready else waiting).append(row)
    due.sort(key=lambda r: r["ready_on"])
    waiting.sort(key=lambda r: r["ready_on"])
    return due, waiting, done


def format_due(site_name: str, today: date, due: list[dict[str, Any]], waiting: list[dict[str, Any]], done: int) -> str:
    lines = [f"Tester att utvärdera för {site_name} per {today.isoformat()} (fönstret slut + {FINAL_AFTER_DAYS} dagar passerat):"]
    if not due:
        lines.append("  Inga.")
    for r in due:
        exp = r.get("expected_change_pct")
        lines.append(f"  {r['test_id']}  {r['action']}  | förväntat: {'–' if exp is None else f'{exp:+.0f} %'}  | mått: {r['metric']}, fönster {r['window']} dagar"
                     f"  | fönstret slutade {r['window_last'].isoformat()} ({r['days_since_end']} dagar sedan)"
                     f"  | utvärderingsbart sedan {r['ready_on'].isoformat()} ({r['days_overdue']} dagar)")
        lines.append(f"      site-audit test evaluate --site {site_name} --id {r['test_id']} --save")
    if waiting:
        n = waiting[0]
        lines.append(f"Ej utvärderade än: {len(waiting)} test, närmast {n['test_id']} som kan utvärderas {n['ready_on'].isoformat()} "
                     f"({(n['ready_on'] - today).days} dagar kvar).")
    else:
        lines.append("Ej utvärderade än: inga fler väntar på sitt fönster.")
    if done:
        lines.append(f"Redan utvärderade: {done}.")
    return "\n".join(lines)


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
