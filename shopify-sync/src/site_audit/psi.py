"""Core Web Vitals via PageSpeed Insights API (fältdata från CrUX när den finns, annars labbdata).

Kräver en API-nyckel i miljövariabeln PSI_API_KEY (gratis, Google Cloud Console -> Credentials).
Ett urval sidor per sidtyp mäts, eftersom varje anrop tar 10–30 sekunder.
"""

from __future__ import annotations

import logging
import os
from typing import Any

import requests

from .crawler import CrawlResult
from .findings import Finding

log = logging.getLogger(__name__)
ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

# Googles gränser för "bra" och "dålig"
LIMITS = {
    "LARGEST_CONTENTFUL_PAINT_MS": (2500, 4000, "LCP", "ms"),
    "INTERACTION_TO_NEXT_PAINT": (200, 500, "INP", "ms"),
    "CUMULATIVE_LAYOUT_SHIFT_SCORE": (10, 25, "CLS", "/100"),  # CrUX anger CLS × 100
}


def sample_urls(cr: CrawlResult, per_type: int = 2) -> list[str]:
    """Väljer de mest länkade levande sidorna per sidtyp."""
    by_type: dict[str, list] = {}
    for cu in cr.urls.values():
        if cu.facts and cu.status == 200 and not cu.redirect_count:
            by_type.setdefault(cu.facts.page_type, []).append(cu)
    out = []
    for ptype in ("home", "product", "collection", "page", "article"):
        pages = sorted(by_type.get(ptype, []), key=lambda c: -len(c.linked_from))
        out += [c.url for c in pages[:per_type]]
    return out


def run_psi(url: str, strategy: str = "mobile", key: str | None = None, session=None) -> dict[str, Any]:
    params = {"url": url, "strategy": strategy, "category": "performance"}
    if key:
        params["key"] = key
    resp = (session or requests).get(ENDPOINT, params=params, timeout=120)
    resp.raise_for_status()
    return resp.json()


def findings_from_psi(url: str, data: dict[str, Any], strategy: str = "mobile") -> list[Finding]:
    out = []
    field = (data.get("loadingExperience") or {}).get("metrics") or {}
    for key, (good, poor, label, unit) in LIMITS.items():
        m = field.get(key)
        if not m:
            continue
        p75 = m.get("percentile")
        if p75 is None:
            continue
        if p75 > poor:
            sev = "high"
        elif p75 > good:
            sev = "medium"
        else:
            continue
        shown = f"{p75 / 100:.2f}" if label == "CLS" else f"{p75} {unit}"
        out.append(Finding(f"cwv_{label.lower()}", sev, "performance",
                           f"{label} (verkliga besökare, {strategy}) är {shown}", url=url,
                           evidence={"p75": p75, "category": m.get("category"), "source": "CrUX"}))
    lh = data.get("lighthouseResult") or {}
    score = ((lh.get("categories") or {}).get("performance") or {}).get("score")
    if score is not None and score < 0.5:
        audits = lh.get("audits") or {}
        top = sorted(
            ((k, a) for k, a in audits.items() if a.get("details", {}).get("type") == "opportunity" and (a.get("numericValue") or 0) > 0),
            key=lambda kv: -(kv[1].get("numericValue") or 0))[:3]
        out.append(Finding("lighthouse_performance", "medium", "performance",
                           f"Lighthouse-prestanda {score * 100:.0f}/100 ({strategy})", url=url,
                           evidence={"score": score, "top_opportunities": [a.get("title") for _, a in top]}))
    return out


def psi_findings(cr: CrawlResult, per_type: int = 2, strategy: str = "mobile", session=None) -> list[Finding]:
    key = os.environ.get("PSI_API_KEY")
    out = []
    for url in sample_urls(cr, per_type):
        try:
            out += findings_from_psi(url, run_psi(url, strategy, key, session), strategy)
        except Exception as exc:  # noqa: BLE001
            log.warning("PSI misslyckades för %s: %s", url, exc)
    return out
