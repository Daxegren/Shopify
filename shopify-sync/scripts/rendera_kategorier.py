#!/usr/bin/env python3
"""Renderande kategorikontroll: ser Google produkterna? Jämför kategorisidans råa HTML med sidan efter att JavaScript körts.

Genomlysningen läser bara den råa HTML:en. Om butikens kategorisidor bygger produktlistan och rubriken med JavaScript visar den
därför "0 produkter" och "ingen H1" trots att besökare och Google (som renderar sidan) ser dem. Det här skriptet hämtar ett urval
kategorier från sitemapen, laddar varje i en riktig webbläsare och klassar dem:

  ok               produkter och H1 finns redan i råa HTML:en
  byggs_med_js     produkter eller H1 saknas i råa HTML:en men finns efter rendering (Google måste rendera sidan)
  tom              inga produkter ens efter rendering (en riktigt tom kategori)
  utan_h1          produkter finns men ingen H1 efter rendering (ett verkligt SEO-fel)

  pip install playwright && playwright install chromium
  python3 scripts/rendera_kategorier.py --base-url https://bestofsports.fi --sample 30 --out rendera-bos-fi

Resultatet skrivs som Markdown och JSON i --out. Läser bara publika sidor och ändrar ingenting."""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit

UA = "Mozilla/5.0 (compatible; GrowthAudit/1.0; +kontroll av egen sajt)"
LOC = re.compile(r"<loc>\s*([^<\s]+)\s*</loc>", re.I)


def parse_locs(xml: str) -> list[str]:
    return LOC.findall(xml)


class _Facts(HTMLParser):
    """Samlar länkar och H1 ur riktiga element, inte ur text inuti <script> och <style>."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.handles: set[str] = set()
        self.h1 = False
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1
        elif tag == "h1" and not self._skip:
            self.h1 = True
        elif tag == "a" and not self._skip:
            href = dict(attrs).get("href") or ""
            path = urlsplit(href).path
            if "/products/" in path:
                self.handles.add(path.split("/products/", 1)[1].split("/")[0])

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip:
            self._skip -= 1


def _facts(html: str) -> _Facts:
    f = _Facts()
    f.feed(html)
    return f


def count_product_links(html: str) -> int:
    """Unika produkthandtag som länkas på sidan."""
    return len(_facts(html).handles)


def has_h1(html: str) -> bool:
    return _facts(html).h1


def evenly(items: list[str], n: int) -> list[str]:
    items = sorted(items)
    if len(items) <= n:
        return items
    step = len(items) / n
    return [items[int(i * step)] for i in range(n)]


def classify(raw_products: int, raw_h1: bool, rendered_products: int, rendered_h1: bool) -> str:
    if rendered_products == 0:
        return "tom"
    if not rendered_h1:
        return "utan_h1"
    if raw_products == 0 or not raw_h1:
        return "byggs_med_js"
    return "ok"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "sv,fi,da,en"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", errors="replace")


def collection_urls(base: str, sample: int) -> list[str]:
    index = fetch(base + "/sitemap.xml")
    maps = [u for u in parse_locs(index) if "collection" in u.lower()] or [base + "/sitemap.xml"]
    urls: list[str] = []
    for m in maps:
        urls += [u for u in parse_locs(fetch(m)) if "/collections/" in u]
    return evenly(sorted(set(urls)), sample)


def run(args) -> int:
    from playwright.sync_api import sync_playwright

    base = args.base_url.rstrip("/")
    urls = collection_urls(base, args.sample)
    if not urls:
        print("Inga kategorier hittades i sitemapen.", file=sys.stderr)
        return 1
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    with sync_playwright() as pw:
        launch = {"headless": True}
        if args.chromium_path:
            launch["executable_path"] = args.chromium_path
        browser = pw.chromium.launch(**launch)
        page = browser.new_context(locale="sv-SE", viewport={"width": 1366, "height": 900}).new_page()
        for u in urls:
            try:
                raw = fetch(u)
                page.goto(u, wait_until="domcontentloaded", timeout=45000)
                try:
                    page.wait_for_load_state("networkidle", timeout=15000)
                except Exception:  # noqa: BLE001  (sidor med öppna anslutningar blir aldrig 'idle')
                    pass
                page.mouse.wheel(0, 4000)
                page.wait_for_timeout(1500)
                rendered = page.content()
            except Exception as e:  # noqa: BLE001
                rows.append({"url": u, "klass": "fel", "fel": str(e)[:120]})
                continue
            row = {"url": u, "raw_produkter": count_product_links(raw), "raw_h1": has_h1(raw),
                   "rend_produkter": count_product_links(rendered), "rend_h1": has_h1(rendered)}
            row["klass"] = classify(row["raw_produkter"], row["raw_h1"], row["rend_produkter"], row["rend_h1"])
            rows.append(row)
            print(f"{row['klass']:13} raw {row['raw_produkter']:>3} → rendered {row['rend_produkter']:>3}  {urlsplit(u).path}")
        browser.close()
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["klass"]] = counts.get(r["klass"], 0) + 1
    (out / "kategorier.json").write_text(json.dumps({"base": base, "rows": rows, "counts": counts}, ensure_ascii=False, indent=1),
                                         encoding="utf-8")
    lines = [f"# Renderande kategorikontroll: {base}", "", f"{len(rows)} kategorier. " + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())), ""]
    for k in ("utan_h1", "tom", "byggs_med_js", "fel", "ok"):
        sel = [r for r in rows if r["klass"] == k]
        if sel:
            lines += [f"## {k} ({len(sel)})"] + [f"- {r['url']}" + (f" (raw {r['raw_produkter']}, rendered {r['rend_produkter']})" if "raw_produkter" in r else "") for r in sel[:15]] + [""]
    (out / "kategorier.md").write_text("\n".join(lines), encoding="utf-8")
    print("\nSammanfattning:", counts, f"\nHela resultatet i {out}/kategorier.md")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--base-url", required=True)
    p.add_argument("--sample", type=int, default=30)
    p.add_argument("--out", default="rendera-kategorier")
    p.add_argument("--chromium-path")
    args = p.parse_args(argv)
    try:
        return run(args)
    except ImportError:
        print("Playwright saknas: pip install playwright && playwright install chromium", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
