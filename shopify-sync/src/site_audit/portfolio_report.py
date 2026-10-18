"""Portföljrapport: rangordnar butiker och marknader mot medianen.

Frågan är om en förändring är butikens egen eller gäller hela portföljen (säsong, plattformar). Varje butik och marknad
får veckans förändring mot förra veckan i ordrar, besök och MER; sedan räknas skillnaden mot medianen över alla
rader. Bara förändringar i procent jämförs, belopp i olika valutor summeras aldrig.

`site-audit portfolio-weekly` läser vyn portfolio_daily (skapas av `growth-sql`).
"""

from __future__ import annotations

from datetime import date, timedelta
from statistics import median
from typing import Any

from .growth_report import kpis, pct, periods

METRICS = (("orders", "Ordrar"), ("sessions", "Besök"), ("mer", "MER"))
OUTLIER = 15.0  # procentenheter från medianen som markeras


def portfolio_sql(project: str, dataset: str, today: date) -> str:
    start = periods(today)["w0"][0]
    return (f"SELECT store, vertical, market, currency, d, orders, revenue, sessions, google_cost, meta_cost\n"
            f"FROM `{project}.{dataset}.portfolio_daily` WHERE d >= '{start.isoformat()}'")


def rank(rows: list[dict[str, Any]], today: date) -> list[dict[str, Any]]:
    """En post per butik och marknad med förändring mot förra veckan och skillnad mot medianen."""
    per = periods(today)
    groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for r in rows:
        groups.setdefault((r["store"], r["market"]), []).append(r)
    out = []
    for (store, market), g in sorted(groups.items()):
        w1, w0 = kpis(g, per["w1"]), kpis(g, per["w0"])
        out.append({"store": store, "market": market, "vertical": g[0].get("vertical") or "",
                    **{f"{k}_chg": pct(w1[k], w0[k]) for k, _ in METRICS},
                    "orders": w1["orders"], "orders_prev": w0["orders"]})
    for k, _ in METRICS:
        vals = [o[f"{k}_chg"] for o in out if o[f"{k}_chg"] is not None]
        med = median(vals) if vals else None
        for o in out:
            c = o[f"{k}_chg"]
            o[f"{k}_rel"] = (c - med) if (c is not None and med is not None) else None
            o[f"{k}_median"] = med
    return out


def _c(v: float | None) -> str:
    return "–" if v is None else f"{v:+.0f} %"


def format_report(ranked: list[dict[str, Any]], today: date) -> str:
    per = periods(today)
    lines = ["# Portföljrapport", "",
             f"Vecka {per['w1'][0]} – {per['w1'][1]} mot veckan innan. Rangordnat efter ordrar mot portföljens median. "
             "Förändringar i procent; belopp jämförs inte över valutor. "
             "Ett stort minus mot medianen betyder att orsaken sannolikt är butikens egen, ett värde nära noll att butiken följer portföljen.", ""]
    if not ranked:
        return "\n".join(lines + ["*Ingen data i portfolio_daily för perioden.*", ""])
    med = ranked[0]
    lines += [f"Medianförändring: ordrar {_c(med['orders_median'])}, besök {_c(med['sessions_median'])}, MER {_c(med['mer_median'])}.", "",
              "| Butik | Marknad | Ordrar | Mot median | Besök | Mot median | MER | Mot median |", "|---|---|---|---|---|---|---|---|"]
    for o in sorted(ranked, key=lambda x: (x["orders_rel"] is None, x["orders_rel"] or 0)):
        lines.append(f"| {o['store']} | {o['market']} | {_c(o['orders_chg'])} | {_c(o['orders_rel'])} | {_c(o['sessions_chg'])} | "
                     f"{_c(o['sessions_rel'])} | {_c(o['mer_chg'])} | {_c(o['mer_rel'])} |")
    flagged = [o for o in ranked if o["orders_rel"] is not None and abs(o["orders_rel"]) >= OUTLIER and (o["orders_prev"] or 0) >= 10]
    lines += ["", "## Avviker från portföljen", ""]
    if flagged:
        for o in flagged:
            word = "sämre" if o["orders_rel"] < 0 else "bättre"
            lines.append(f"- {o['store']} {o['market']}: ordrar {_c(o['orders_chg'])}, {abs(o['orders_rel']):.0f} procentenheter {word} än medianen.")
    else:
        lines.append("Ingen butik avviker mer än %d procentenheter från medianen (butiker med färre än 10 ordrar förra veckan räknas inte)." % OUTLIER)
    return "\n".join(lines + [""])


def build_portfolio_report(store, project: str, dataset: str = "portfolio", today: date | None = None) -> str:
    today = today or date.today()
    return format_report(rank(store.query(portfolio_sql(project, dataset, today)), today), today)
