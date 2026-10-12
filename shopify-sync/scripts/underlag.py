"""Tar fram underlag för manuell granskning ur senaste körningen (~/audit-se) och BigQuery.

  python3 scripts/underlag.py titlar          sidor på topp 10 med låg klickfrekvens: titel, beskrivning, H1, sökfraser
  python3 scripts/underlag.py skript          det stora inline-skriptet på startsidan och vilka appar som laddas
  python3 scripts/underlag.py omdirigeringar  gissade omdirigeringsmål med tre alternativ var

Resultatet skrivs till ~/audit-se/underlag_<typ>.md och till skärmen.
"""

from __future__ import annotations

import csv
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

AUDIT = Path(os.path.expanduser("~/audit-se"))
PROJECT = os.environ.get("PROJECT_ID", "gorilla-sports-data")
BASE = "https://www.gorillasports.se"


def _jsonl(name: str):
    with open(AUDIT / name) as fh:
        for line in fh:
            if line.strip():
                yield json.loads(line)


def _pages() -> dict[str, dict]:
    return {p["url"].rstrip("/"): p for p in _jsonl("pages.jsonl")}


def _bq(sql: str) -> list[dict]:
    out = subprocess.run(["bq", "query", "--use_legacy_sql=false", "--format=json", "--max_rows=10000", sql],
                         capture_output=True, text=True, check=True).stdout
    return json.loads(out[out.index("["):]) if "[" in out else []


def titlar() -> str:
    findings = [f for f in _jsonl("findings.jsonl") if f["check"] == "low_ctr_top10"]
    pages = _pages()
    urls = [f["url"].rstrip("/") for f in findings]
    in_list = ", ".join(f"'{u}'" for u in urls)
    rows = _bq(f"""
        WITH q AS (
          SELECT RTRIM(url, '/') AS url, query, SUM(impressions) AS impr, SUM(clicks) AS clicks,
                 ROUND(SUM(sum_position) / NULLIF(SUM(impressions), 0) + 1, 1) AS pos
          FROM `{PROJECT}.searchconsole.searchdata_url_impression`
          WHERE data_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
            AND NOT is_anonymized_query AND RTRIM(url, '/') IN ({in_list})
          GROUP BY 1, 2)
        SELECT * FROM q QUALIFY ROW_NUMBER() OVER (PARTITION BY url ORDER BY impr DESC) <= 5""") if urls else []
    queries: dict[str, list[dict]] = {}
    for r in rows:
        queries.setdefault(r["url"], []).append(r)
    out = ["# Sidor på topp 10 med låg klickfrekvens", ""]
    for f in sorted(findings, key=lambda f: -float(f["evidence"].get("impressions", 0))):
        u = f["url"].rstrip("/")
        p, ev = pages.get(u, {}), f["evidence"]
        out += [f"## {u.replace(BASE, '')}",
                f"- Visningar {int(ev['impressions'])}, klick {int(ev['clicks'])}, snittposition {ev['position']}",
                f"- Titel: {p.get('title')}",
                f"- Beskrivning: {p.get('meta_description')}",
                f"- H1: {' | '.join(p.get('h1') or [])}",
                "- Sökfraser (visningar / klick / position):"]
        out += [f"  - {q['query']}: {q['impr']} / {q['clicks']} / {q['pos']}" for q in queries.get(u, [])]
        out.append("")
    return "\n".join(out)


def skript() -> str:
    req = urllib.request.Request(BASE + "/", headers={"User-Agent": "Mozilla/5.0 (underlag)"})
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    blocks = re.findall(r"<script\b([^>]*)>(.*?)</script>", html, re.S | re.I)
    big = sorted(((len(body), attrs, body) for attrs, body in blocks if body.strip()), reverse=True)[:3]
    out = ["# Största inline-skripten på startsidan", ""]
    for size, attrs, body in big:
        out += [f"## {size / 1024:.0f} KB, attribut: {attrs.strip()[:200] or '-'}",
                "Början:", "```", body.strip()[:1200], "```",
                "Ord som kan avslöja appen:",
                ", ".join(sorted(set(re.findall(r"[A-Za-z][A-Za-z0-9_-]{4,}(?:App|app|Bundle|bundle|Widget|widget|"
                                                r"Builder|builder|Pages|pages|Translate|translate)\b", body)))[:40]) or "-",
                ""]
    srcs = re.findall(r"<script[^>]+src=[\"']([^\"']+)", html, re.I)
    out += ["# Skript med src", ""] + [f"- {s[:160]}" for s in srcs]
    blocks_ids = sorted(set(re.findall(r"shopify-block-([a-z0-9_-]+)", html)))
    out += ["", "# App-block på sidan", ""] + [f"- {b}" for b in blocks_ids[:60]]
    return "\n".join(out)


def omdirigeringar() -> str:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    from site_audit.actions import _overlap, _tokens
    from site_audit.html_parse import split_locale

    pages = _pages()
    live = sorted({p["url"].replace(BASE, "") or "/" for p in pages.values()
                   if p.get("status") == 200 and not p.get("redirect_count") and p.get("title")})
    titles = {p["url"].replace(BASE, ""): p.get("title") for p in pages.values()}
    review = {r["Redirect from"]: r["Förslag"] for r in csv.DictReader(open(AUDIT / "redirects_review.csv"))}
    for r in csv.DictReader(open(AUDIT / "actions.csv")):
        if r["åtgärd"] == "Byt mål på omdirigering" and r["mål"].startswith("/"):
            review.setdefault(r["mål"], r["förslag"])
    out = ["# Gissade omdirigeringsmål", "",
           "Format: gammal URL, verktygets förslag, samt de tre bästa alternativen bland levande sidor.", ""]
    for src in sorted(review):
        loc, _ = split_locale(src)
        want = _tokens(src)
        cands = sorted(((_overlap(want, _tokens(c)), c) for c in live if split_locale(c)[0] == loc and want),
                       reverse=True)[:3]
        out.append(f"- `{src}` → förslag `{review[src]}`")
        for score, c in cands:
            if score > 0:
                out.append(f"    - {score:.2f} `{c}` ({(titles.get(c) or '')[:70]})")
    cols = [c for c in live if c.startswith("/collections/")]
    blogs = [c for c in live if c.startswith("/blogs/")]
    out += ["", f"# Levande kollektioner ({len(cols)})", ""] + [f"- `{c}`" for c in cols]
    out += ["", f"# Levande bloggsidor ({len(blogs)})", ""] + [f"- `{c}`" for c in blogs]
    return "\n".join(out)


def main() -> int:
    kind = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"titlar": titlar, "skript": skript, "omdirigeringar": omdirigeringar}.get(kind)
    if not fn:
        print(__doc__)
        return 1
    text = fn()
    path = AUDIT / f"underlag_{kind}.md"
    path.write_text(text)
    print(text)
    print(f"\n[Sparad i {path}, {len(text) // 1024} KB]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
