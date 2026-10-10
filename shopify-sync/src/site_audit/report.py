"""Rapport i Markdown och fristående HTML. Strukturen följer: sammanfattning, åtgärdslista
per kontroll (med antal och exempel) och nyckeltal."""

from __future__ import annotations

import html
from collections import defaultdict
from typing import Any

from .findings import CATEGORIES, SEVERITY_RANK, Finding

SEV_LABEL = {"critical": "Kritisk", "high": "Hög", "medium": "Medel", "low": "Låg", "info": "Info"}
EXAMPLES = 8


def _group(findings: list[Finding]) -> list[tuple[str, list[Finding]]]:
    groups: dict[str, list[Finding]] = defaultdict(list)
    for f in findings:
        groups[f.check].append(f)
    return sorted(groups.items(), key=lambda kv: (min(SEVERITY_RANK[f.severity] for f in kv[1]), -len(kv[1])))


def headline_bullets(findings: list[Finding], limit: int = 12) -> list[str]:
    """Korta punkter i stil med '46 konstnärssidor i sitemapen ger 404'."""
    out = []
    for check, fs in _group([f for f in findings if f.severity != "info"])[:limit]:
        worst = min(fs, key=lambda f: SEVERITY_RANK[f.severity])
        n = len(fs)
        total = sum(f.evidence.get("count", 1) for f in fs) if any("count" in f.evidence for f in fs) else n
        label = worst.message.split(" (")[0]
        out.append(f"{n} × {label}" + (f" (totalt {total} berörda)" if total != n else ""))
    return out


def _example_cell(f: Finding) -> str:
    ev = {k: v for k, v in f.evidence.items() if k not in ("urls",)}
    s = ", ".join(f"{k}: {v}" for k, v in list(ev.items())[:3])
    return s[:200]


def to_markdown(summary: dict[str, Any], findings: list[Finding]) -> str:
    lines = [f"# Genomlysning: {summary['site']}", "",
             f"Körning `{summary['run_id']}` · {summary['started_at'][:16].replace('T', ' ')} UTC", ""]
    sev = summary["by_severity"]
    lines += ["## Sammanfattning", "",
              "| Kritisk | Hög | Medel | Låg | Info |", "|---|---|---|---|---|",
              f"| {sev['critical']} | {sev['high']} | {sev['medium']} | {sev['low']} | {sev['info']} |", ""]
    if "crawl" in summary:
        c = summary["crawl"]
        lines += [f"Crawl: {c['urls']} URL:er ({c['sitemap_urls']} från {c['sitemaps']} sitemaps), "
                  f"{c['status_200']} OK, {c['redirected']} omdirigerade, {c['errors_4xx']} 4xx, {c['errors_5xx']} 5xx.", ""]
    if "admin" in summary:
        a = summary["admin"]
        lines += ["Shopify: " + ", ".join(f"{v} {k}" for k, v in a.items()) + ".", ""]
    lines += ["## Förbättringar", ""] + [f"- {b}" for b in headline_bullets(findings)] + [""]

    by_cat: dict[str, list[Finding]] = defaultdict(list)
    for f in findings:
        by_cat[f.category].append(f)
    for cat, label in CATEGORIES.items():
        fs = by_cat.get(cat)
        if not fs:
            continue
        lines += [f"## {label}", ""]
        for check, group in _group(fs):
            worst = min(group, key=lambda f: SEVERITY_RANK[f.severity])
            lines += [f"### {SEV_LABEL[worst.severity]}: {worst.message} ({len(group)})", "",
                      f"Kontroll: `{check}`", "", "| URL | Detaljer |", "|---|---|"]
            for f in group[:EXAMPLES]:
                lines.append(f"| {f.url or f.resource or ''} | {_example_cell(f).replace('|', '/')} |")
            if len(group) > EXAMPLES:
                lines.append(f"| … och {len(group) - EXAMPLES} till | |")
            lines.append("")
    return "\n".join(lines)


CSS = """
:root{--bg:#fff;--fg:#1d1d1f;--muted:#6b6b70;--card:#f5f5f7;--line:#e2e2e6;--crit:#b3261e;--high:#d0541a;--med:#b58100;--low:#3b6fb6;--info:#6b6b70}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#141416;--fg:#ececf0;--muted:#a0a0a8;--card:#1f1f23;--line:#2e2e34}}
:root[data-theme="dark"]{--bg:#141416;--fg:#ececf0;--muted:#a0a0a8;--card:#1f1f23;--line:#2e2e34}
body{background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif;margin:0;padding:24px 16px;max-width:1100px;margin-inline:auto}
h1{font-size:26px;margin:0 0 4px}h2{margin-top:36px;border-bottom:1px solid var(--line);padding-bottom:6px}
.muted{color:var(--muted)} .tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px;margin:16px 0}
.tile{background:var(--card);border-radius:10px;padding:12px}.tile b{display:block;font-size:24px}
details{background:var(--card);border-radius:10px;margin:10px 0;padding:10px 14px}summary{cursor:pointer;font-weight:600}
table{width:100%;border-collapse:collapse;font-size:13px;margin-top:8px;table-layout:fixed}td{border-top:1px solid var(--line);padding:6px 4px;vertical-align:top;overflow-wrap:anywhere}
.sev{display:inline-block;border-radius:6px;padding:0 6px;font-size:12px;color:#fff;margin-right:6px}
.critical{background:var(--crit)}.high{background:var(--high)}.medium{background:var(--med)}.low{background:var(--low)}.info{background:var(--info)}
ul.bul li{margin:4px 0}
"""


def to_html(summary: dict[str, Any], findings: list[Finding]) -> str:
    e = html.escape
    sev = summary["by_severity"]
    parts = [f"<!doctype html><html lang='sv'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>",
             f"<title>Genomlysning {e(summary['site'])}</title><style>{CSS}</style></head><body>",
             f"<h1>Genomlysning: {e(summary['site'])}</h1><div class='muted'>Körning {e(summary['run_id'])} · {e(summary['started_at'][:16].replace('T', ' '))} UTC</div>",
             "<div class='tiles'>"]
    for k in ("critical", "high", "medium", "low", "info"):
        parts.append(f"<div class='tile'><span class='sev {k}'>{SEV_LABEL[k]}</span><b>{sev[k]}</b></div>")
    if "crawl" in summary:
        c = summary["crawl"]
        parts.append(f"<div class='tile'>URL:er<b>{c['urls']}</b></div><div class='tile'>4xx<b>{c['errors_4xx']}</b></div><div class='tile'>Omdirigerade<b>{c['redirected']}</b></div>")
    parts.append("</div><h2>Förbättringar</h2><ul class='bul'>")
    parts += [f"<li>{e(b)}</li>" for b in headline_bullets(findings)]
    parts.append("</ul>")
    by_cat: dict[str, list[Finding]] = defaultdict(list)
    for f in findings:
        by_cat[f.category].append(f)
    for cat, label in CATEGORIES.items():
        fs = by_cat.get(cat)
        if not fs:
            continue
        parts.append(f"<h2>{e(label)}</h2>")
        for check, group in _group(fs):
            worst = min(group, key=lambda f: SEVERITY_RANK[f.severity])
            parts.append(f"<details><summary><span class='sev {worst.severity}'>{SEV_LABEL[worst.severity]}</span>{e(worst.message)} · {len(group)}</summary>"
                         f"<div class='muted'>Kontroll: {e(check)}</div><table><colgroup><col style='width:55%'><col></colgroup>")
            for f in group[:50]:
                target = f.url or f.resource or ""
                link = f"<a href='{e(target)}'>{e(target)}</a>" if target.startswith("http") else e(target)
                parts.append(f"<tr><td>{link}</td><td>{e(_example_cell(f))}</td></tr>")
            if len(group) > 50:
                parts.append(f"<tr><td colspan='2' class='muted'>… och {len(group) - 50} till (se findings.jsonl)</td></tr>")
            parts.append("</table></details>")
    parts.append("</body></html>")
    return "".join(parts)
