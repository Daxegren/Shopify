#!/usr/bin/env python3
"""Samtycke och mätning i riktig webbläsare (T19): skickas spårning före samtycke, och startar den efter godkännande?

Öppnar sidan som en ny besökare utan cookies, väntar utan att klicka och loggar alla anrop till analys- och annonstjänster.
Klickar sedan på godkänn och loggar vad som tillkommer. Läser också Googles samtyckessignal (gcs) i GA4-anropen och
Shopifys Customer Privacy API. Ingen order läggs och inga uppgifter fylls i.

  pip install playwright && playwright install chromium
  python3 scripts/samtycke_test.py --base-url https://www.bestofsports.se --out samtycke-bos

Tolkning av Googles samtyckessignal i GA4-anrop (parametern gcs): G100 = allt nekat, G111 = analys och annonser godkända,
G101 = bara annonser, G110 = bara analys. Anrop med G100 före samtycke är normalt (Consent Mode utan cookies).
Resultatet är en heuristik: bannerknappar hittas på text. Titta på skärmdumparna innan du drar slutsatser."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

MOBILE = {"viewport": {"width": 390, "height": 844}, "device_scale_factor": 2, "is_mobile": True, "has_touch": True,
          "user_agent": ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 "
                         "(KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1")}
DESKTOP = {"viewport": {"width": 1366, "height": 850}}

TRACKING = re.compile(
    r"google-analytics\.com|analytics\.google\.com|/g/collect|googletagmanager\.com/gtag|doubleclick\.net|googleadservices\.com|"
    r"google\.[a-z.]+/pagead|facebook\.com/tr|connect\.facebook\.net/.*fbevents|analytics\.tiktok\.com|clarity\.ms|hotjar\.|"
    r"snap\.licdn\.com|pinterest\.com/ct|bat\.bing\.com|klaviyo\.com/client/event", re.I)
ACCEPT = re.compile(r"^(acceptera( alla)?|godkänn( alla)?|tillåt( alla)?|jag godkänner|ok|accept( all)?|allow all|agree|i agree|"
                    r"hyväksy( kaikki)?|accepter( alle)?|tillad( alle)?)$", re.I)
REJECT = re.compile(r"^(avvisa( alla)?|neka( alla)?|endast nödvändiga|reject( all)?|decline|deny|only necessary|hylkää|afvis( alle)?)$", re.I)
GCS_MEANING = {"G100": "allt nekat", "G101": "bara annonser godkända", "G110": "bara analys godkänd", "G111": "analys och annonser godkända"}


def classify_requests(urls: list[str], extra_patterns: list[str] | None = None) -> list[dict]:
    """Plockar ut anrop till spårningstjänster och läser GA4-parametrar (händelse, mätid, samtyckessignal)."""
    extra = [re.compile(p) for p in (extra_patterns or [])]
    out = []
    for u in urls:
        if not (TRACKING.search(u) or any(p.search(u) for p in extra)):
            continue
        q = parse_qs(urlsplit(u).query)
        out.append({"host": urlsplit(u).netloc, "event": (q.get("en") or [""])[0], "tid": (q.get("tid") or [""])[0],
                    "gcs": (q.get("gcs") or [""])[0], "url": u[:160]})
    return out


def verdicts(before: list[dict], after: list[dict], banner_found: bool, accepted: bool) -> list[str]:
    """Slutsatser i klartext. before = anrop utan interaktion, after = nya anrop efter godkännande."""
    out = []
    granted_before = [r for r in before if r["gcs"] in ("G111", "G110", "G101") or (not r["gcs"] and "collect" not in r["url"])]
    denied_before = [r for r in before if r["gcs"] == "G100"]
    if granted_before:
        hosts = sorted({r["host"] for r in granted_before})
        out.append(f"PROBLEM: spårning skickas före samtycke utan nekad samtyckessignal ({len(granted_before)} anrop till {', '.join(hosts[:4])})")
    elif denied_before:
        out.append(f"OK: {len(denied_before)} GA4-anrop före samtycke har gcs=G100 (Consent Mode, inga cookies)")
    elif not before:
        out.append("OK: ingen spårning skickas före samtycke")
    if not banner_found:
        out.append("OBS: ingen samtyckesruta hittades" + (", men spårning körs" if before else ""))
    if accepted and not after:
        out.append("PROBLEM: ingen ny spårning startade efter godkännande (mätning kan gå förlorad)")
    elif accepted:
        states = sorted({r["gcs"] for r in after if r["gcs"]})
        txt = ", ".join(f"{s} ({GCS_MEANING.get(s, 'okänd')})" for s in states) or "ingen gcs i anropen"
        out.append(f"OK: {len(after)} nya spårningsanrop efter godkännande, samtyckessignal: {txt}")
        if states and "G111" not in states and "G110" not in states:
            out.append("PROBLEM: efter godkännande är samtyckessignalen fortfarande nekad (taggarna får inte uppdaterat samtycke)")
    return out


def run(args) -> int:
    from playwright.sync_api import sync_playwright

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    report: dict = {"url": args.base_url, "viewport": args.viewport}
    with sync_playwright() as pw:
        launch = {"headless": True}
        if args.chromium_path:
            launch["executable_path"] = args.chromium_path
        browser = pw.chromium.launch(**launch)
        ctx = browser.new_context(locale="sv-SE", **(DESKTOP if args.viewport == "desktop" else MOBILE))
        page = ctx.new_page()
        requests_seen: list[str] = []
        page.on("request", lambda r: requests_seen.append(r.url))
        page.goto(args.base_url.rstrip("/") + args.path, wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(args.wait_ms)
        before_urls = list(requests_seen)
        before = classify_requests(before_urls, args.track_pattern)
        cookies_before = sorted(c["name"] for c in ctx.cookies())
        page.screenshot(path=str(out / "01-fore-samtycke.png"))

        state = page.evaluate("""() => ({
            shopifyPrivacy: !!(window.Shopify && window.Shopify.customerPrivacy),
            shopifyConsent: (window.Shopify && window.Shopify.customerPrivacy && window.Shopify.customerPrivacy.currentVisitorConsent)
                ? JSON.stringify(window.Shopify.customerPrivacy.currentVisitorConsent()) : null,
            dataLayerConsent: (window.dataLayer || []).filter(e => e && e[0] === 'consent').map(e => JSON.stringify(Array.from(e))).slice(0, 6),
            googleConsentState: (window.google_tag_data && window.google_tag_data.ics && window.google_tag_data.ics.entries)
                ? JSON.stringify(window.google_tag_data.ics.entries) : null,
        })""")
        buttons = page.get_by_role("button").all()
        accept_btn = reject_btn = None
        names = []
        for b in buttons:
            try:
                if not b.is_visible():
                    continue
                name = (b.inner_text() or "").strip()
            except Exception:  # noqa: BLE001
                continue
            names.append(name[:40])
            if accept_btn is None and ACCEPT.match(name):
                accept_btn = b
            if reject_btn is None and REJECT.match(name):
                reject_btn = b
        banner_found = accept_btn is not None or reject_btn is not None
        after: list[dict] = []
        accepted = False
        if accept_btn is not None:
            n_before = len(requests_seen)
            try:
                accept_btn.click(timeout=8000)
                page.wait_for_timeout(args.wait_ms)
                accepted = True
                after = classify_requests(requests_seen[n_before:], args.track_pattern)
                page.screenshot(path=str(out / "02-efter-godkannande.png"))
            except Exception as exc:  # noqa: BLE001
                report["accept_error"] = str(exc)[:160]
        cookies_after = sorted(c["name"] for c in ctx.cookies())
        browser.close()
    report.update({
        "banner_found": banner_found, "accept_button": bool(accept_btn), "reject_button": bool(reject_btn),
        "visible_buttons": names[:12], "state": state, "tracking_before_consent": before, "tracking_after_accept": after,
        "cookies_before": cookies_before, "cookies_after": cookies_after,
        "new_cookies_after_accept": sorted(set(cookies_after) - set(cookies_before)),
        "verdicts": verdicts(before, after, banner_found, accepted),
    })
    (out / "samtycke.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Samtycke och mätning, {args.base_url}{args.path} ({args.viewport})")
    print(f"- Ruta hittad: {'ja' if banner_found else 'nej'}; knappar: {', '.join(names[:8]) or '-'}")
    print(f"- Shopify Customer Privacy API: {'finns' if state['shopifyPrivacy'] else 'saknas'}; Consent Mode i dataLayer: "
          f"{len(state['dataLayerConsent'])} kommandon")
    print(f"- Spårningsanrop före samtycke: {len(before)}; efter godkännande: {len(after)}; cookies före/efter: "
          f"{len(cookies_before)}/{len(cookies_after)}")
    for v in report["verdicts"]:
        print(f"  {v}")
    print(f"Rapport och skärmdumpar i {out}/")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--base-url", required=True)
    p.add_argument("--path", default="/", help="Sida att testa (standard startsidan)")
    p.add_argument("--viewport", choices=["mobile", "desktop"], default="mobile")
    p.add_argument("--wait-ms", type=int, default=6000, help="Väntetid utan interaktion och efter klick")
    p.add_argument("--out", default="samtycke")
    p.add_argument("--chromium-path")
    p.add_argument("--track-pattern", action="append", default=[], help="Extra regex som räknas som spårning (för tester)")
    args = p.parse_args(argv)
    try:
        return run(args)
    except ImportError:
        print("Playwright saknas: pip install playwright && playwright install chromium", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
