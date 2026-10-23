#!/usr/bin/env python3
"""Tillgänglighet med axe-core (T19): hittar vanliga fel som skärmläsare och tangentbordsanvändare stöter på.

Kör axe-core i en riktig webbläsare på startsida, kategori och produkt, och summerar överträdelser per allvarlighet och regel.
Resultatet är en bra första kontroll men täcker bara ungefär en tredjedel av alla tillgänglighetsfel (axe hittar det som går att
mäta automatiskt, till exempel kontrast, saknad alt-text, saknade formuläretiketter och felaktig ARIA).

  pip install playwright axe-playwright-python && playwright install chromium
  python3 scripts/tillganglighet_test.py --base-url https://www.bestofsports.se --collection /collections/motionscykel --out tillganglighet-bos

axe-core hämtas ur paketet axe-playwright-python, från --axe-js <fil> eller (om inget annat finns) från cdnjs.cloudflare.com."""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

CDN = "https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.0/axe.min.js"
IMPACT_ORDER = ("critical", "serious", "moderate", "minor")
MOBILE = {"viewport": {"width": 390, "height": 844}, "device_scale_factor": 2, "is_mobile": True, "has_touch": True}
DESKTOP = {"viewport": {"width": 1366, "height": 850}}
RUN_AXE = "async () => { const r = await axe.run(document, {resultTypes: ['violations']}); " \
          "return r.violations.map(v => ({id: v.id, impact: v.impact, help: v.help, helpUrl: v.helpUrl, " \
          "nodes: v.nodes.length, sample: v.nodes.slice(0, 3).map(n => n.target.join(' ')) })); }"


def find_axe_js(explicit: str | None) -> str | None:
    if explicit:
        return Path(explicit).read_text(encoding="utf-8")
    try:
        import axe_playwright_python  # type: ignore

        return (Path(axe_playwright_python.__file__).parent / "axe.min.js").read_text(encoding="utf-8")
    except Exception:  # noqa: BLE001
        return None


def summarize(results: dict[str, list[dict]]) -> dict:
    """results[sidnamn] = lista med överträdelser. Returnerar totaler per allvarlighet och de vanligaste reglerna."""
    by_impact: Counter = Counter()
    by_rule: dict[str, dict] = {}
    for page, viol in results.items():
        for v in viol:
            by_impact[v["impact"] or "okänd"] += v["nodes"]
            r = by_rule.setdefault(v["id"], {"id": v["id"], "impact": v["impact"], "help": v["help"], "nodes": 0, "pages": []})
            r["nodes"] += v["nodes"]
            r["pages"].append(page)
    top = sorted(by_rule.values(), key=lambda r: (IMPACT_ORDER.index(r["impact"]) if r["impact"] in IMPACT_ORDER else 9, -r["nodes"]))
    return {"by_impact": {k: by_impact.get(k, 0) for k in IMPACT_ORDER}, "rules": top}


def run(args) -> int:
    from playwright.sync_api import sync_playwright

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    base = args.base_url.rstrip("/")
    paths = {"startsida": "/", "kategori": args.collection or "/collections/all"}
    if args.product:
        paths["produkt"] = args.product
    axe_src = find_axe_js(args.axe_js)
    results: dict[str, list[dict]] = {}
    with sync_playwright() as pw:
        launch = {"headless": True}
        if args.chromium_path:
            launch["executable_path"] = args.chromium_path
        browser = pw.chromium.launch(**launch)
        ctx = browser.new_context(locale="sv-SE", **(DESKTOP if args.viewport == "desktop" else MOBILE))
        page = ctx.new_page()
        queue = list(paths.items())
        while queue:
            name, path = queue.pop(0)
            page.goto(base + path, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(2500)
            if name == "kategori" and "produkt" not in paths:
                link = page.locator('a[href*="/products/"]').first
                if link.count():
                    paths["produkt"] = (link.get_attribute("href") or "").split("?")[0]
                    queue.append(("produkt", paths["produkt"]))
            if axe_src:
                page.evaluate(axe_src)
            else:
                page.add_script_tag(url=CDN)
            results[name] = page.evaluate(RUN_AXE)
        browser.close()
    summ = summarize(results)
    (out / "tillganglighet.json").write_text(json.dumps({"pages": results, "summary": summ, "paths": paths}, ensure_ascii=False, indent=1),
                                             encoding="utf-8")
    print(f"Tillgänglighet (axe-core), {base} ({args.viewport})")
    print("Överträdelser (antal element) per allvarlighet:", ", ".join(f"{k} {v}" for k, v in summ["by_impact"].items()))
    for r in summ["rules"][:12]:
        print(f"- [{r['impact']}] {r['id']}: {r['nodes']} element på {', '.join(sorted(set(r['pages'])))}. {r['help']}")
    print(f"Hela resultatet i {out}/tillganglighet.json")
    return 1 if summ["by_impact"]["critical"] else 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--base-url", required=True)
    p.add_argument("--collection", help="Kategori, t.ex. /collections/motionscykel")
    p.add_argument("--product", help="Produkt, t.ex. /products/namn (annars första produkten i kategorin)")
    p.add_argument("--viewport", choices=["mobile", "desktop"], default="mobile")
    p.add_argument("--out", default="tillganglighet")
    p.add_argument("--axe-js", help="Sökväg till axe.min.js (annars paketet eller CDN)")
    p.add_argument("--chromium-path")
    args = p.parse_args(argv)
    try:
        return run(args)
    except ImportError:
        print("Playwright saknas: pip install playwright axe-playwright-python && playwright install chromium", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
