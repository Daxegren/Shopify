"""Gemensam modell för fynd. Alla kontroller returnerar listor av Finding."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from typing import Any

SEVERITIES = ("critical", "high", "medium", "low", "info")
SEVERITY_RANK = {s: i for i, s in enumerate(SEVERITIES)}

# Kategorier används för gruppering i rapporten och i BigQuery.
CATEGORIES = {
    "indexing": "Indexering och statuskoder",
    "redirects": "Omdirigeringar",
    "international": "Marknader, språk och hreflang",
    "onpage": "Titlar, rubriker och metadata",
    "schema": "Strukturerad data",
    "content": "Innehåll, dubbletter och tunna sidor",
    "catalog": "Produkter och kollektioner",
    "media": "Bilder och alt-texter",
    "performance": "Sidvikt och skript",
    "links": "Interna länkar",
}


@dataclass
class Finding:
    check: str               # stabilt id, t.ex. "sitemap_url_error"
    severity: str            # critical | high | medium | low | info
    category: str            # nyckel i CATEGORIES
    message: str             # kort beskrivning på svenska
    url: str | None = None   # berörd URL eller admin-resurs
    resource: str | None = None  # t.ex. gid://shopify/Product/1
    evidence: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.severity not in SEVERITY_RANK:
            raise ValueError(f"Okänd severity: {self.severity}")
        if self.category not in CATEGORIES:
            raise ValueError(f"Okänd kategori: {self.category}")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def sort_findings(findings: list[Finding]) -> list[Finding]:
    return sorted(findings, key=lambda f: (SEVERITY_RANK[f.severity], f.category, f.check, f.url or ""))


def summarize(findings: list[Finding]) -> dict[str, Any]:
    """Antal per severity, per kategori och per kontroll (med högsta severity)."""
    by_sev = Counter(f.severity for f in findings)
    by_cat = Counter(f.category for f in findings)
    by_check: dict[str, dict[str, Any]] = defaultdict(lambda: {"count": 0, "severity": "info", "category": None, "message": None})
    for f in findings:
        entry = by_check[f.check]
        entry["count"] += 1
        entry["category"] = f.category
        if entry["message"] is None or SEVERITY_RANK[f.severity] < SEVERITY_RANK[entry["severity"]]:
            entry["severity"] = f.severity
            entry["message"] = f.message
    return {
        "total": len(findings),
        "by_severity": {s: by_sev.get(s, 0) for s in SEVERITIES},
        "by_category": dict(by_cat),
        "by_check": dict(by_check),
    }
