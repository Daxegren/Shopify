"""Chrome UX Report (CrUX), historik per vecka (T16): hur har verkliga besökares upplevelse utvecklats?

PageSpeed-testet (T6) visar läget idag. CrUX-historiken visar om det blivit bättre eller sämre de senaste månaderna, till
exempel efter att en app installerats. Gratis API, kräver en nyckel och att "Chrome UX Report API" är aktiverat i projektet.
Nyckeln läses ur miljövariabeln CRUX_API_KEY (eller PSI_API_KEY) och skrivs aldrig ut."""

from __future__ import annotations

import os
from statistics import mean
from typing import Any

import requests

ENDPOINT = "https://chromeuxreport.googleapis.com/v1/records:queryHistoryRecord"
METRICS = {
    "largest_contentful_paint": ("LCP", 2500, 4000, 1.0),            # millisekunder
    "interaction_to_next_paint": ("INP", 200, 500, 1.0),             # millisekunder
    "cumulative_layout_shift": ("CLS", 0.1, 0.25, 1.0),
    "experimental_time_to_first_byte": ("TTFB", 800, 1800, 1.0),     # millisekunder
}


def query_history(key: str, origin: str | None = None, url: str | None = None, form_factor: str = "PHONE",
                  session: requests.Session | None = None) -> dict[str, Any]:
    body: dict[str, Any] = {"formFactor": form_factor, "metrics": list(METRICS)}
    if url:
        body["url"] = url
    else:
        body["origin"] = origin
    resp = (session or requests).post(f"{ENDPOINT}?key={key}", json=body, timeout=60)
    if resp.status_code == 404:
        return {}  # för lite besökardata för den här adressen eller formfaktorn
    if resp.status_code >= 400:
        raise RuntimeError(f"CrUX {resp.status_code}: {resp.text[:300]}")
    return resp.json()


def _num(v: Any) -> float | None:
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def weekly_series(data: dict[str, Any]) -> dict[str, list[tuple[str, float | None]]]:
    """{mått: [(sista dag i perioden, p75), ...]} i tidsordning."""
    record = data.get("record", {})
    periods = record.get("collectionPeriods", [])
    labels = []
    for p in periods:
        d = p.get("lastDate", {})
        labels.append(f"{d.get('year', 0):04d}-{d.get('month', 0):02d}-{d.get('day', 0):02d}")
    out = {}
    for metric, (short, *_rest) in METRICS.items():
        p75s = (record.get("metrics", {}).get(metric, {}).get("percentilesTimeseries", {}) or {}).get("p75s", [])
        out[short] = [(labels[i] if i < len(labels) else "?", _num(v)) for i, v in enumerate(p75s)]
    return out


def verdict(short: str, value: float | None) -> str:
    for _, (s, good, poor, _) in METRICS.items():
        if s == short and value is not None:
            return "bra" if value <= good else "dålig" if value > poor else "behöver förbättras"
    return "okänt"


def trend(series: list[tuple[str, float | None]], recent: int = 4, earlier: int = 8) -> dict[str, Any]:
    """Jämför snittet för de senaste veckorna mot veckorna dessförinnan."""
    vals = [v for _, v in series if v is not None]
    if len(vals) < recent + 3:
        return {"enough_data": False}
    last = mean(vals[-recent:])
    before = mean(vals[-(recent + earlier):-recent])
    change = (last - before) / before if before else 0.0
    return {"enough_data": True, "recent_avg": last, "earlier_avg": before, "change_pct": round(change * 100, 1),
            "direction": "sämre" if change > 0.10 else "bättre" if change < -0.10 else "oförändrat"}


def report(origin: str, form_factor: str, series: dict[str, list[tuple[str, float | None]]]) -> str:
    lines = [f"CrUX-historik för {origin} ({form_factor}), p75 per vecka", "",
             "| Mått | Senast | Bedömning | Trend (senaste 4 veckor mot 8 veckorna före) |", "|---|---|---|---|"]
    for short, s in series.items():
        vals = [v for _, v in s if v is not None]
        last = vals[-1] if vals else None
        t = trend(s)
        t_txt = f"{t['direction']} ({t['change_pct']:+.0f} %)" if t.get("enough_data") else "för lite data"
        fmt = "-" if last is None else (f"{last:.2f}" if short == "CLS" else f"{last:.0f} ms")
        lines.append(f"| {short} | {fmt} | {verdict(short, last)} | {t_txt} |")
    return "\n".join(lines)


def key_from_env() -> str:
    key = os.environ.get("CRUX_API_KEY") or os.environ.get("PSI_API_KEY")
    if not key:
        raise RuntimeError("Sätt CRUX_API_KEY (eller PSI_API_KEY): read -rs CRUX_API_KEY && export CRUX_API_KEY")
    return key
