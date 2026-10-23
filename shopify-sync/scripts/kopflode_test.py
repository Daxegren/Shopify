#!/usr/bin/env python3
"""Köpflödeskontroll: går igenom en butik som en besökare och mäter var det tar stopp.

Steg: startsida, kategori, produkt, lägg i varukorg, varukorg, kassan. Skriver en rapport (Markdown och JSON) och skärmdumpar.
Ingen order läggs och inga uppgifter fylls i. Kassan öppnas bara, så en kassasession skapas hos Shopify (ofarligt; inget
e-postmeddelande skickas eftersom ingen e-postadress anges).

Kräver Playwright och en webbläsare:
  pip install playwright && playwright install chromium
  python3 scripts/kopflode_test.py --base-url https://www.bestofsports.se --collection /collections/motionscykel --out kopflode-bos

Alternativ: --viewport desktop, --product /products/<handle> (annars väljs den första produkten i kategorin som går att köpa),
--chromium-path <sökväg> för en förinstallerad webbläsare. Kör gärna både mobil (standard) och desktop.
Resultatet är en heuristik: knappar och texter hittas med vanliga Shopify-väljare och kan missa ovanliga teman. Läs rapporten
och titta på skärmdumparna, dra inga slutsatser av ett enskilt steg som misslyckas utan att titta på bilden.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from urllib.parse import urljoin, urlsplit

MOBILE = {"viewport": {"width": 390, "height": 844}, "device_scale_factor": 2, "is_mobile": True, "has_touch": True,
          "user_agent": ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 "
                         "(KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1")}
DESKTOP = {"viewport": {"width": 1366, "height": 850}}
COOKIE_WORDS = re.compile(r"cookie|kakor|samtycke|consent|integritet", re.I)
SOLD_OUT_WORDS = re.compile(r"slut i lager|slutsåld|sold out|ej i lager|out of stock|utsolgt|loppuunmyyty", re.I)
SHIPPING_WORDS = re.compile(r"frakt|leverans|shipping|delivery|toimitus|fragt|levering", re.I)
RETURN_WORDS = re.compile(r"retur|ångerrätt|returns?|palautus|fortrydelsesret", re.I)
ADD_TO_CART = ['form[action*="/cart/add"] [type=submit]', 'button[name="add"]', 'button:has-text("Lägg i varukorg")',
               'button:has-text("Add to cart")', 'button:has-text("Köp")', 'button:has-text("Tilføj til kurv")',
               'button:has-text("Lisää ostoskoriin")']
CHECKOUT_BTN = ['button[name="checkout"]', 'input[name="checkout"]', 'a[href*="/checkout"]', 'button:has-text("Kassa")',
                'button:has-text("Checkout")', 'button:has-text("Till kassan")']


@dataclass
class Step:
    name: str
    ok: bool = False
    url: str = ""
    seconds: float = 0.0
    notes: list[str] = field(default_factory=list)
    problems: list[str] = field(default_factory=list)
    screenshot: str = ""


class Collector:
    """Samlar konsolfel och misslyckade anrop under ett steg."""

    def __init__(self, page):
        self.console: list[str] = []
        self.failed: list[str] = []
        # Webbläsaren loggar ett konsolfel för en saknad favicon som inte säger något om köpflödet
        page.on("console", lambda m: self.console.append(m.text[:200])
                if m.type == "error" and "favicon" not in (m.location.get("url", "") if m.location else "") else None)
        page.on("requestfailed", lambda r: self.failed.append(f"{r.url[:120]} ({r.failure})"))
        page.on("response", lambda r: self.failed.append(f"{r.status} {r.url[:120]}") if r.status >= 400 else None)

    def drain(self) -> tuple[list[str], list[str]]:
        c, f = self.console[:], self.failed[:]
        self.console.clear()
        self.failed.clear()
        return c, f


def first_visible(page, selectors: list[str]):
    for sel in selectors:
        try:
            loc = page.locator(sel).first
            if loc.count() and loc.is_visible():
                return loc, sel
        except Exception:  # noqa: BLE001 - ogiltig väljare i det här temat
            continue
    return None, ""


def price_from_page(page) -> str:
    """Pris från produktschemat (JSON-LD) eller metataggen product:price:amount."""
    for raw in page.eval_on_selector_all('script[type="application/ld+json"]', "els => els.map(e => e.textContent)"):
        try:
            data = json.loads(raw)
        except Exception:  # noqa: BLE001
            continue
        for item in data if isinstance(data, list) else [data]:
            if not isinstance(item, dict):
                continue
            offers = item.get("offers")
            offers = offers if isinstance(offers, list) else [offers] if offers else []
            for o in offers:
                if isinstance(o, dict) and o.get("price"):
                    return f"{o.get('price')} {o.get('priceCurrency', '')}".strip()
    meta = page.locator('meta[property="product:price:amount"]').first
    if meta.count():
        return meta.get_attribute("content") or ""
    return ""


def shot(page, out: Path, name: str) -> str:
    path = out / f"{name}.png"
    try:
        page.screenshot(path=str(path), full_page=False)
    except Exception:  # noqa: BLE001
        return ""
    return path.name


def timed_goto(page, url: str, timeout_ms: int = 45000) -> tuple[float, int | None]:
    t0 = time.time()
    resp = page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
    try:
        page.wait_for_load_state("load", timeout=15000)
    except Exception:  # noqa: BLE001
        pass
    return time.time() - t0, resp.status if resp else None


def run(args) -> list[Step]:
    from playwright.sync_api import sync_playwright

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    base = args.base_url.rstrip("/")
    steps: list[Step] = []
    with sync_playwright() as pw:
        launch = {"headless": True}
        if args.chromium_path:
            launch["executable_path"] = args.chromium_path
        browser = pw.chromium.launch(**launch)
        ctx = browser.new_context(locale="sv-SE", **(DESKTOP if args.viewport == "desktop" else MOBILE))
        page = ctx.new_page()
        col = Collector(page)

        def finish(step: Step, status: int | None, secs: float):
            step.seconds = round(secs, 1)
            step.url = page.url
            console, failed = col.drain()
            if status and status >= 400:
                step.problems.append(f"HTTP {status}")
            if console:
                step.problems.append(f"{len(console)} konsolfel, t.ex. {console[0]}")
            ext_failed = [f for f in failed if not re.match(r"^(3\d\d) ", f)]
            if ext_failed:
                step.notes.append(f"{len(ext_failed)} misslyckade anrop, t.ex. {ext_failed[0]}")
            if secs > 6:
                step.problems.append(f"Långsam sida: {secs:.1f} s till laddad")
            step.screenshot = shot(page, out, f"{len(steps) + 1:02d}-{step.name}")
            steps.append(step)

        # 1. Startsida
        s = Step("startsida")
        secs, status = timed_goto(page, base + "/")
        body = page.inner_text("body")
        if COOKIE_WORDS.search(body[:3000]):
            s.notes.append("Cookie- eller samtyckesruta syns (kontrollera att den inte döljer innehåll på mobil)")
        s.ok = bool(status and status < 400)
        finish(s, status, secs)

        # 2. Kategori
        s = Step("kategori")
        coll = args.collection or "/collections/all"
        secs, status = timed_goto(page, urljoin(base + "/", coll.lstrip("/")))
        links = page.eval_on_selector_all('a[href*="/products/"]', "els => [...new Set(els.map(e => e.getAttribute('href')))]")
        s.notes.append(f"{len(links)} unika produktlänkar på första sidan")
        sold = len(SOLD_OUT_WORDS.findall(page.inner_text("body")))
        if sold:
            s.notes.append(f"{sold} förekomster av 'slut i lager' på kategorisidan")
        if not links:
            s.problems.append("Inga produkter syns i kategorin")
        s.ok = bool(status and status < 400 and links)
        finish(s, status, secs)

        # 3. Produkt
        s = Step("produkt")
        target = args.product
        if not target and links:
            target = links[0]
        if not target:
            s.problems.append("Ingen produkt att öppna")
            finish(s, None, 0.0)
            browser.close()
            return steps
        target_url = urljoin(base + "/", target.split("?")[0].lstrip("/")) if target.startswith("/") else target
        secs, status = timed_goto(page, target_url)
        body = page.inner_text("body")
        price = price_from_page(page)
        s.notes.append(f"Pris i schema: {price or 'saknas'}")
        if not price:
            s.problems.append("Inget pris i produktschemat (påverkar Google Shopping och synlighet)")
        s.notes.append("Fraktinformation syns på produktsidan" if SHIPPING_WORDS.search(body) else "Ingen fraktinformation syns på produktsidan")
        s.notes.append("Returinformation syns på produktsidan" if RETURN_WORDS.search(body) else "Ingen returinformation syns på produktsidan")
        if SOLD_OUT_WORDS.search(body):
            s.problems.append("Produkten är markerad som slut i lager")
        btn, sel = first_visible(page, ADD_TO_CART)
        if btn is None:
            s.problems.append("Hittar ingen synlig 'Lägg i varukorg'-knapp")
        else:
            s.notes.append(f"Köpknapp hittad ({sel}), aktiverad: {btn.is_enabled()}")
            if not btn.is_enabled():
                s.problems.append("Köpknappen är inaktiverad (kan vara slut i lager eller ett val som saknas)")
        s.ok = bool(status and status < 400 and btn is not None and btn.is_enabled())
        finish(s, status, secs)

        # 4. Lägg i varukorg
        s = Step("lagg-i-varukorg")
        t0 = time.time()
        if btn is None or not btn.is_enabled():
            s.problems.append("Hoppades över: ingen aktiv köpknapp")
        else:
            try:
                btn.click(timeout=10000)
                page.wait_for_timeout(2500)
                s.ok = True
            except Exception as exc:  # noqa: BLE001
                s.problems.append(f"Klicket på köpknappen misslyckades: {str(exc)[:120]}")
        finish(s, None, time.time() - t0)

        # 5. Varukorg
        s = Step("varukorg")
        secs, status = timed_goto(page, base + "/cart")
        body = page.inner_text("body")
        in_cart = len(page.locator('a[href*="/products/"]').all()) if status and status < 400 else 0
        s.notes.append(f"{in_cart} produktlänkar i varukorgen")
        cbtn, csel = first_visible(page, CHECKOUT_BTN)
        s.notes.append(f"Kassaknapp: {csel or 'saknas'}")
        if re.search(r"(?i)varukorgen är tom|your cart is empty|ostoskori on tyhjä|din kurv er tom", body):
            s.problems.append("Varukorgen är tom efter köpklicket (köpet registrerades inte)")
        elif cbtn is None:
            s.problems.append("Hittar ingen kassaknapp")
        s.ok = bool(cbtn is not None and not s.problems)
        finish(s, status, secs)

        # 6. Kassan
        s = Step("kassan")
        t0 = time.time()
        if cbtn is None:
            s.problems.append("Hoppades över: ingen kassaknapp")
            finish(s, None, 0.0)
        else:
            try:
                cbtn.click(timeout=10000)
                page.wait_for_url(re.compile(r"/checkouts?/"), timeout=30000)
                page.wait_for_timeout(3000)
                host = urlsplit(page.url).netloc
                s.notes.append(f"Kassan öppnades på {host}")
                text = page.inner_text("body")
                s.notes.append("Betalningsalternativ nämns" if re.search(r"(?i)kort|card|swish|klarna|paypal|apple pay|google pay|mobilepay|vipps", text)
                               else "Inga betalningsalternativ syns ännu (visas ofta först efter adress)")
                s.notes.append("Fraktval nämns" if SHIPPING_WORDS.search(text) else "Fraktval syns inte ännu (visas ofta först efter adress)")
                s.ok = True
            except Exception as exc:  # noqa: BLE001
                s.problems.append(f"Kassan öppnades inte: {str(exc)[:140]}")
            finish(s, None, time.time() - t0)
        browser.close()
    return steps


def write_report(steps: list[Step], args) -> None:
    out = Path(args.out)
    (out / "kopflode.json").write_text(json.dumps([asdict(s) for s in steps], ensure_ascii=False, indent=1), encoding="utf-8")
    lines = [f"# Köpflödeskontroll {args.base_url} ({args.viewport})", "",
             "| Steg | Resultat | Tid (s) | Problem |", "|---|---|---|---|"]
    for s in steps:
        lines.append(f"| {s.name} | {'OK' if s.ok else 'STOPP'} | {s.seconds} | {'; '.join(s.problems) or '-'} |")
    lines += ["", "## Detaljer"]
    for s in steps:
        lines += [f"### {s.name}", f"- Adress: {s.url}"] + [f"- {n}" for n in s.notes] + [f"- PROBLEM: {p}" for p in s.problems]
        if s.screenshot:
            lines.append(f"- Skärmdump: {s.screenshot}")
    (out / "kopflode.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:4 + len(steps)]))
    print(f"\nRapport och skärmdumpar i {out}/")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--base-url", required=True, help="t.ex. https://www.bestofsports.se")
    p.add_argument("--collection", help="Kategorisökväg, t.ex. /collections/motionscykel (standard: /collections/all)")
    p.add_argument("--product", help="Produktsökväg, t.ex. /products/namn (standard: första i kategorin)")
    p.add_argument("--viewport", choices=["mobile", "desktop"], default="mobile")
    p.add_argument("--out", default="kopflode", help="Mapp för rapport och skärmdumpar")
    p.add_argument("--chromium-path", help="Sökväg till en förinstallerad Chromium (annars används Playwrights)")
    args = p.parse_args(argv)
    try:
        steps = run(args)
    except ImportError:
        print("Playwright saknas: pip install playwright && playwright install chromium", file=sys.stderr)
        return 2
    write_report(steps, args)
    return 0 if all(s.ok for s in steps) else 1


if __name__ == "__main__":
    sys.exit(main())
