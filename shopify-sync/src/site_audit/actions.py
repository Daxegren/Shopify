"""Gör om fynd till en prioriterad åtgärdslista och färdiga importfiler.

- actions.csv            vad som ska göras, var, och varför (sorterad efter prioritet)
- redirects_import.csv   Shopify-format ("Redirect from","Redirect to") för Online Store >
                         Navigation > URL Redirects > Import. Gäller nya 301:or för 404-sidor
                         och omskrivna kedjor så att de pekar direkt på slutmålet.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

from .crawler import CrawlResult
from .findings import SEVERITY_RANK, Finding
from .html_parse import split_locale

PRIORITY = {"critical": 100, "high": 60, "medium": 30, "low": 10, "info": 0}


@dataclass
class Action:
    priority: int
    action: str
    target: str
    suggestion: str
    reason: str
    check: str


def _path(url: str) -> str:
    return urlsplit(url).path or "/"


def _tokens(path: str) -> set[str]:
    _, rest = split_locale(path)
    return {t for t in re.split(r"[/\-_]+", rest.lower()) if t and not t.isdigit() and t not in {"products", "collections", "pages", "blogs"}}


def _similar(a: str, b: str) -> bool:
    """Samma ord, eller samma början på minst 5 tecken (artist/artists, konstnar/konstnarer)."""
    if a == b:
        return True
    n = min(len(a), len(b))
    return n >= 5 and a[:5] == b[:5] and abs(len(a) - len(b)) <= 3


def _overlap(want: set[str], have: set[str]) -> float:
    hits = sum(1 for w in want if any(_similar(w, h) for h in have))
    return hits / max(len(want), len(have))


def live_paths(cr: CrawlResult) -> list[str]:
    return sorted({_path(cu.url) for cu in cr.urls.values() if cu.status == 200 and not cu.redirect_count and cu.facts})


def suggest_target(path: str, candidates: list[str]) -> tuple[str, float]:
    """Bästa ersättare för en död URL: samma sektion och språk, flest gemensamma ord i adressen."""
    loc, rest = split_locale(path)
    section = rest.strip("/").split("/")[0] if rest.strip("/") else ""
    want = _tokens(path)
    best, score = None, 0.0
    for c in candidates:
        cloc, crest = split_locale(c)
        if cloc != loc:
            continue
        csec = crest.strip("/").split("/")[0] if crest.strip("/") else ""
        have = _tokens(c)
        if not want or not have:
            continue
        s = _overlap(want, have) + (0.15 if csec == section else 0)
        if s > score:
            best, score = c, s
    if best is None or score < 0.35:
        fallback = f"/{loc}/collections/all" if loc else "/collections/all"
        if section == "pages":
            fallback = f"/{loc}" if loc else "/"
        return fallback, 0.0
    return best, round(score, 2)


def _keep_first(items: list[str], prefix: str, clicks: dict[str, float]) -> list[str]:
    """Sorterar så att sidan med flest klick i Google behålls vid sammanslagning."""
    return sorted(items, key=lambda h: -clicks.get(f"{prefix}{h}".rstrip("/"), 0))


def build_actions(findings: list[Finding], cr: CrawlResult | None,
                  clicks: dict[str, float] | None = None) -> tuple[list[Action], list[tuple[str, str]]]:
    clicks = clicks or {}
    actions: list[Action] = []
    redirects: dict[str, str] = {}
    live = live_paths(cr) if cr else []
    for f in findings:
        p = PRIORITY[f.severity] + int(f.evidence.get("clicks", 0) or 0)
        url = f.url or f.resource or ""
        if f.check in ("sitemap_url_error", "traffic_page_broken", "broken_internal_link") and cr:
            src = _path(url)
            tgt, score = suggest_target(src, live)
            redirects.setdefault(src, tgt)
            actions.append(Action(p, "Skapa 301", src, tgt,
                                  f"{f.message}. Förslag med säkerhet {score:.2f}" + (" (kontrollera manuellt)" if score < 0.6 else ""), f.check))
        elif f.check in ("redirect_chain", "redirect_to_error", "redirect_table_chain") and cr:
            cu = cr.urls.get(url.rstrip("/")) or cr.urls.get(url)
            src = _path(url)
            if cu and cu.status == 200:
                redirects[src] = _path(cu.final_url)
                actions.append(Action(p, "Peka om omdirigering", src, _path(cu.final_url), f.message, f.check))
            else:
                tgt, _ = suggest_target(src, live)
                redirects[src] = tgt
                actions.append(Action(p, "Byt mål på omdirigering", src, tgt, f.message, f.check))
        elif f.check == "large_inline_script_sitewide":
            actions.append(Action(p + f.evidence.get("pages", 0) // 10, "Flytta ut inline-skript", "tema/app",
                                  f"Skriptet börjar: {f.evidence.get('starts_with', '')[:60]}", f.message, f.check))
        elif f.check in ("redirect_changes_locale", "redirect_table_locale", "geo_redirect", "redirect_to_other_market"):
            actions.append(Action(p, "Rätta marknad/språk", url, "Peka svenska URL:er på svensk version, eller ta bort geo-omdirigering från roten",
                                  f.message, f.check))
        elif f.check in ("duplicate_collection_products", "near_duplicate_collection", "duplicate_collection_description", "collection_clones"):
            cols = f.evidence.get("collections") or [url.rsplit("/", 1)[-1], f.evidence.get("other")]
            cols = _keep_first([c for c in cols if c], "/collections/", clicks)
            if len(cols) > 1:
                keep = cols[0]
                for c in cols[1:]:
                    redirects.setdefault(f"/collections/{c}", f"/collections/{keep}")
                actions.append(Action(p, "Slå ihop kollektioner", f"/collections/{keep}",
                                      f"Behåll {keep}, 301 från: {', '.join(cols[1:])}", f.message, f.check))
        elif f.check in ("empty_collection", "empty_collection_in_sitemap"):
            actions.append(Action(p, "Avpublicera eller fyll kollektion", url, "Dölj från Online Store eller lägg till produkter", f.message, f.check))
        elif f.check in ("test_page_published", "test_or_draft_page", "app_generated_page", "outdated_page", "thin_page"):
            actions.append(Action(p, "Avpublicera sida", url, "Avpublicera, eller slå ihop med relevant sida och 301", f.message, f.check))
        elif f.check == "duplicate_role_page":
            handles = _keep_first(f.evidence.get("handles") or [], "/pages/", clicks)
            if len(handles) > 1:
                for h in handles[1:]:
                    redirects.setdefault(f"/pages/{h}", f"/pages/{handles[0]}")
                actions.append(Action(p, "Slå ihop sidor", f"/pages/{handles[0]}", f"301 från: {', '.join(handles[1:])}", f.message, f.check))
        elif f.check in ("missing_h1", "multiple_h1"):
            actions.append(Action(p, "Rätta H1 i temat", f.evidence.get("page_type", url), "En H1 per sida i mallen", f.message, f.check))
        elif f.check in ("duplicate_seo_title", "missing_title", "duplicate_title", "low_ctr_top10"):
            actions.append(Action(p, "Skriv ny SEO-titel", url, "Unik titel med sökord och varumärke", f.message, f.check))
        elif f.check in ("product_images_no_alt", "images_missing_alt"):
            actions.append(Action(p, "Lägg till alt-text", url, "Beskrivande alt-text per bild", f.message, f.check))
        elif f.check.startswith("product_schema") or f.check in ("breadcrumb_schema_missing", "org_schema_missing"):
            actions.append(Action(p, "Rätta strukturerad data", url, "Uppdatera JSON-LD i temat", f.message, f.check))
        elif f.check in ("brand_misspelling",):
            actions.append(Action(p, "Rätta stavning", url, f"Byt '{f.evidence.get('word') or f.message}' mot korrekt varumärke", f.message, f.check))
        elif f.severity != "info":
            actions.append(Action(p, "Granska", url, "", f.message, f.check))
    # Kedjor i förslagen: peka alltid direkt på slutmålet.
    for src in list(redirects):
        seen = {src}
        tgt = redirects[src]
        while tgt in redirects and tgt not in seen:
            seen.add(tgt)
            tgt = redirects[tgt]
        redirects[src] = tgt
    pairs = sorted((s, t) for s, t in redirects.items() if s != t)
    # En åtgärd per (åtgärd, mål); behåll högsta prioritet och samla orsakerna.
    merged: dict[tuple[str, str], Action] = {}
    for a in actions:
        key = (a.action if a.action not in ("Byt mål på omdirigering", "Skapa 301") else "301", a.target)
        if key in merged:
            m = merged[key]
            if a.reason not in m.reason:
                m.reason += f"; {a.reason}"
            if a.priority > m.priority:
                m.priority, m.action, m.suggestion = a.priority, a.action, a.suggestion
        else:
            merged[key] = a
    actions = sorted(merged.values(), key=lambda a: (-a.priority, a.action, a.target))
    return actions, pairs


def write_action_files(findings: list[Finding], cr: CrawlResult | None, out_dir: str | Path,
                       clicks: dict[str, float] | None = None) -> tuple[Path, Path]:
    actions, pairs = build_actions(findings, cr, clicks)
    out = Path(out_dir)
    a_path, r_path = out / "actions.csv", out / "redirects_import.csv"
    with open(a_path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["prioritet", "åtgärd", "mål", "förslag", "orsak", "kontroll"])
        for a in actions:
            w.writerow([a.priority, a.action, a.target, a.suggestion, a.reason, a.check])
    with open(r_path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["Redirect from", "Redirect to"])
        w.writerows(pairs)
    return a_path, r_path
