#!/usr/bin/env python3
"""GTM-nätverkstest: laddas samma Tag Manager-container flera gånger, och skickas samma GA4- eller Meta-händelse dubbelt?

Öppnar en adress som en ny besökare, väntar tills nätverket är lugnt och räknar nätverksanrop till
  * googletagmanager.com/gtm.js, per container (parametern id, t.ex. GTM-M2JNXNW),
  * GA4-händelser: anrop till /g/collect, grupperade på mät-id (parametern tid) och händelsenamn (parametern en),
  * Meta-pixel: anrop till facebook.com/tr, grupperade på pixel-id (id) och händelse (ev).
Körning A är första besöket utan samtycke. Hittas en samtyckesruta klickas "acceptera" (körning B = nya anrop efter klicket), och sidan
laddas sedan om med samtycke sparat (körning C = en hel sidladdning för en besökare som redan godkänt). Hittas ingen ruta körs bara A.
Ingen order läggs och inga uppgifter fylls i.

Webbläsaren slår ihop skripttaggar med exakt samma adress till ETT nätverksanrop, men skriptet körs ändå två gånger (testat i den här
filens självtest). Att bara räkna nätverksanrop missar därför en container som laddas två gånger från samma adress. Testet läser därför
även sidans DOM efter laddning: antal gtm.js-skriptelement per container, antal inbyggda laddningsskript (GTM-snutten) per container och
antal gtm.js-händelser i dataLayer (varje körning av snutten lägger en).

Flaggor:
  * CONTAINER: samma container laddas fler än en gång under samma sidbesök (A+B) eller under sidladdningen i C, enligt nätverksanrop,
    skriptelement i DOM, inbyggda laddningsskript eller fler gtm.js-händelser i dataLayer än containrar.
  * DUBBLETT: samma händelse (samma typ, id, namn och sidadress) skickas fler än en gång inom 2 sekunder.
Dubbletter är en heuristik. En händelse som legitimt upprepas inom 2 sekunder (till exempel scroll eller user_engagement) kan ge falskt
utslag, och två identiska anrop från olika taggar visar att något skickar dubbelt men inte vilken tagg. Titta på listan med anrop (--out)
innan du drar slutsatser. Siffrorna gäller en sida i en körning, inte hela sajten.

  pip install playwright && playwright install chromium
  python3 scripts/gtm_natverkstest.py --url https://www.gorillasports.se/ --out gtm-gorilla-se
  python3 scripts/gtm_natverkstest.py --url https://www.gorillasports.se/products/<handle> --viewport desktop

Test utan internet och utan någon butik:
  python3 scripts/gtm_natverkstest.py --test-logic      # enhetstest av räknelogiken, kräver inte webbläsare
  python3 scripts/gtm_natverkstest.py --selftest        # startar en lokal testsida och en lokal attrapp, kräver Playwright

Alternativ: --chromium-path <sökväg> för en förinstallerad webbläsare, --no-sandbox om Chromium körs som root, --extra-host <värd[:port]>
för en egen domän som serverar gtm.js eller tar emot /g/collect och /tr (server-side GTM), --no-reload för att hoppa över körning C,
--strict för att få felkod 1 om något flaggas. Bara läsning: ingenting ändras i butiken."""
from __future__ import annotations

import argparse
import json
import re
import sys
import threading
import time
from collections import defaultdict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

MOBILE = {"viewport": {"width": 390, "height": 844}, "device_scale_factor": 2, "is_mobile": True, "has_touch": True,
          "user_agent": ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 "
                         "(KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1")}
DESKTOP = {"viewport": {"width": 1366, "height": 850}}
DUP_WINDOW_S = 2.0
# Samma knappmönster som scripts/samtycke_test.py
ACCEPT = re.compile(r"^(acceptera( alla)?|godkänn( alla)?|tillåt( alla)?|jag godkänner|ok|accept( all)?|allow all|agree|i agree|"
                    r"hyväksy( kaikki)?|accepter( alle)?|tillad( alle)?)$", re.I)
REJECT = re.compile(r"^(avvisa( alla)?|neka( alla)?|endast nödvändiga|reject( all)?|decline|deny|only necessary|hylkää|afvis( alle)?)$", re.I)
GOOGLE_TAG_HOSTS = ("googletagmanager.com",)
META_HOSTS = ("facebook.com", "www.facebook.com")
TYPE_LABEL = {"gtm": "GTM-container (gtm.js)", "gtag": "gtag.js (direkt)", "ga4": "GA4-händelse", "meta": "Meta-pixel", "fbevents": "Meta fbevents.js"}


# ----------------------------------------------------------------------------------------------------------------------------------
# Räknelogik (ingen webbläsare behövs)
# ----------------------------------------------------------------------------------------------------------------------------------

def _host_matches(netloc: str, hosts: tuple[str, ...], extra: set[str]) -> bool:
    host = netloc.lower()
    return host in extra or any(host == h or host.endswith("." + h) for h in hosts)


def classify(url: str, post_data: str | None, t: float, extra_hosts: set[str] | None = None) -> list[dict]:
    """Gör om ett nätverksanrop till noll eller flera poster. Ett GA4-anrop kan innehålla flera händelser (batch i bodyn)."""
    extra = {h.lower() for h in (extra_hosts or set())}
    parts = urlsplit(url)
    path = parts.path.lower()
    q = {k: v[0] for k, v in parse_qs(parts.query, keep_blank_values=True).items()}
    recs: list[dict] = []
    if path.endswith("/gtm.js") and _host_matches(parts.netloc, GOOGLE_TAG_HOSTS, extra):
        recs.append({"typ": "gtm", "id": q.get("id", "okänt id"), "event": "gtm.js", "t": t, "dl": "", "url": url[:200]})
    elif path.endswith("/gtag/js") and _host_matches(parts.netloc, GOOGLE_TAG_HOSTS, extra):
        recs.append({"typ": "gtag", "id": q.get("id", "okänt id"), "event": "gtag/js", "t": t, "dl": "", "url": url[:200]})
    elif path.endswith("/g/collect"):
        tid = q.get("tid", "okänt tid")
        lines = [ln for ln in (post_data or "").splitlines() if ln.strip()]
        per_event = [{k: v[0] for k, v in parse_qs(ln, keep_blank_values=True).items()} for ln in lines]
        events = [e for e in per_event if e.get("en")]
        if q.get("en"):
            events.insert(0, q)
        if not events:
            events = [q]  # ett anrop utan händelsenamn räknas ändå, som "(saknas)"
        for e in events:
            recs.append({"typ": "ga4", "id": tid, "event": e.get("en", "(saknas)"), "t": t, "dl": e.get("dl", q.get("dl", "")),
                         "gcs": q.get("gcs", ""), "url": url[:200]})
    elif path in ("/tr", "/tr/") and _host_matches(parts.netloc, META_HOSTS, extra):
        recs.append({"typ": "meta", "id": q.get("id", "okänt id"), "event": q.get("ev", "(saknas)"), "t": t, "dl": q.get("dl", ""),
                     "eid": q.get("eid", ""), "url": url[:200]})
    elif path.endswith("/fbevents.js"):
        recs.append({"typ": "fbevents", "id": "-", "event": "fbevents.js", "t": t, "dl": "", "url": url[:200]})
    return recs


def count_table(phases: dict[str, list[dict]]) -> list[dict]:
    """En rad per (typ, id, händelse) med antal per körning. phases = {"A": [...], "B": [...], "C": [...]}."""
    rows: dict[tuple[str, str, str], dict] = {}
    for ph, recs in phases.items():
        for r in recs:
            key = (r["typ"], r["id"], r["event"])
            row = rows.setdefault(key, {"typ": r["typ"], "id": r["id"], "event": r["event"], **{p: 0 for p in phases}})
            row[ph] += 1
    order = {"gtm": 0, "gtag": 1, "ga4": 2, "meta": 3, "fbevents": 4}
    return sorted(rows.values(), key=lambda x: (order.get(x["typ"], 9), x["id"], x["event"]))


def find_flags(recs: list[dict], window: float = DUP_WINDOW_S) -> list[dict]:
    """Letar containrar som laddats mer än en gång och händelser som skickats flera gånger inom `window` sekunder.
    recs är alla anrop från en och samma sidladdning (körning A+B, eller C)."""
    flags: list[dict] = []
    loads: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in recs:
        if r["typ"] in ("gtm", "gtag"):
            loads[(r["typ"], r["id"])].append(r)
    for (typ, cid), lst in sorted(loads.items()):
        if len(lst) > 1:
            same_url = len({r["url"] for r in lst}) == 1
            flags.append({"slag": "CONTAINER", "typ": typ, "id": cid, "antal": len(lst),
                          "text": f"{TYPE_LABEL[typ]} {cid} laddas {len(lst)} gånger" + (" (samma adress)" if same_url else " (olika adresser)")})
    groups: dict[tuple[str, str, str, str], list[dict]] = defaultdict(list)
    for r in recs:
        if r["typ"] in ("ga4", "meta"):
            groups[(r["typ"], r["id"], r["event"], r.get("dl", ""))].append(r)
    for (typ, eid, ev, dl), lst in sorted(groups.items()):
        lst = sorted(lst, key=lambda r: r["t"])
        cluster = [lst[0]]
        clusters: list[list[dict]] = []
        for r in lst[1:]:
            if r["t"] - cluster[-1]["t"] <= window:
                cluster.append(r)
            else:
                clusters.append(cluster)
                cluster = [r]
        clusters.append(cluster)
        for c in clusters:
            if len(c) > 1:
                span = c[-1]["t"] - c[0]["t"]
                flags.append({"slag": "DUBBLETT", "typ": typ, "id": eid, "event": ev, "antal": len(c),
                              "text": f"{TYPE_LABEL[typ]} {ev} på {eid} skickades {len(c)} gånger inom {span:.1f} s"
                                      + (f" (sida {dl[:60]})" if dl else "")})
    return flags


def render_table(rows: list[dict], phases: list[str], flagged: set[tuple[str, str, str]]) -> str:
    names = {"A": "A före samtycke", "B": "B efter klick", "C": "C ny laddning"}
    head = ["Typ", "Id", "Händelse"] + [names.get(p, p) for p in phases] + ["Flagga"]
    body = []
    for r in rows:
        body.append([TYPE_LABEL[r["typ"]], r["id"], r["event"]] + [str(r[p]) for p in phases]
                    + ["<-- kontrollera" if (r["typ"], r["id"], r["event"]) in flagged else ""])
    if not body:
        return "(inga anrop till GTM, GA4 eller Meta hittades)"
    widths = [max(len(head[i]), *(len(b[i]) for b in body)) for i in range(len(head))]
    fmt = lambda cols: "  ".join(c.ljust(widths[i]) for i, c in enumerate(cols)).rstrip()  # noqa: E731
    return "\n".join([fmt(head), fmt(["-" * w for w in widths])] + [fmt(b) for b in body])


def analyse(phases: dict[str, list[dict]], window: float = DUP_WINDOW_S, dom: dict | None = None) -> dict:
    """phases: A (före samtycke), B (nya anrop efter klick, kan saknas), C (ny sidladdning med samtycke, kan saknas).
    dom: {"A+B": ögonblicksbild, "C": ögonblicksbild} från DOM_JS (kan saknas)."""
    page1 = phases.get("A", []) + phases.get("B", [])
    flags = [{"sidladdning": "A+B (första besöket)", **f} for f in find_flags(page1, window)]
    if "C" in phases:
        flags += [{"sidladdning": "C (ny laddning med samtycke)", **f} for f in find_flags(phases["C"], window)]
    for name, recs in (("A+B", page1), ("C", phases.get("C", []))):
        if dom and name in dom:
            label = "A+B (första besöket)" if name == "A+B" else "C (ny laddning med samtycke)"
            ids = {r["id"] for r in recs if r["typ"] == "gtm"}
            flags += [{"sidladdning": label, **f} for f in find_dom_flags(dom[name], ids)]
    flagged = {(f["typ"], f["id"], f.get("event", "gtm.js" if f["typ"] == "gtm" else "gtag/js")) for f in flags}
    rows = count_table(phases)
    return {"rows": rows, "flags": flags, "flagged_keys": flagged}


DOM_JS = """() => {
  const idOf = u => { try { return new URL(u, location.href).searchParams.get('id') || 'okänt id'; } catch (e) { return 'okänt id'; } };
  const els = {};
  document.querySelectorAll('script[src]').forEach(s => {
    if (/\\/gtm\\.js(\\?|$)/.test(s.src)) { const k = idOf(s.src); els[k] = (els[k] || 0) + 1; }
  });
  const inl = {};
  document.querySelectorAll('script:not([src])').forEach(s => {
    const re = /\\(\\s*window\\s*,\\s*document\\s*,\\s*['"]script['"]\\s*,\\s*['"][^'"]+['"]\\s*,\\s*['"](GTM-[A-Z0-9]+)['"]\\s*\\)/g;
    const t = s.textContent || ''; let m;
    while ((m = re.exec(t))) { inl[m[1]] = (inl[m[1]] || 0) + 1; }
  });
  const dl = (window.dataLayer || []).filter(e => e && e.event === 'gtm.js').length;
  return {elements: els, inline: inl, datalayer_gtm_js: dl};
}"""


def find_dom_flags(snap: dict, network_ids: set[str] | None = None) -> list[dict]:
    """Flaggor ur en DOM-ögonblicksbild: {"elements": {id: n}, "inline": {id: n}, "datalayer_gtm_js": n}."""
    flags: list[dict] = []
    for cid, n in sorted(snap.get("elements", {}).items()):
        if n > 1:
            flags.append({"slag": "CONTAINER", "typ": "gtm", "id": cid, "antal": n,
                          "text": f"{cid} har {n} gtm.js-skriptelement i sidan (webbläsaren kan ha slagit ihop dem till ett nätverksanrop)"})
    for cid, n in sorted(snap.get("inline", {}).items()):
        if n > 1:
            flags.append({"slag": "CONTAINER", "typ": "gtm", "id": cid, "antal": n,
                          "text": f"{cid} har {n} inbyggda laddningsskript (GTM-snutten finns {n} gånger i HTML:en)"})
    containers = set(snap.get("elements", {})) | set(snap.get("inline", {})) | (network_ids or set())
    n_dl = snap.get("datalayer_gtm_js", 0)
    if containers and n_dl > len(containers):
        flags.append({"slag": "CONTAINER", "typ": "gtm", "id": ", ".join(sorted(containers)), "antal": n_dl,
                      "text": f"dataLayer har {n_dl} gtm.js-händelser för {len(containers)} container(s): snutten har kört fler gånger än containrar"})
    return flags


# ----------------------------------------------------------------------------------------------------------------------------------
# Webbläsare
# ----------------------------------------------------------------------------------------------------------------------------------

def _capture(page, store: list[dict], extra: set[str]) -> None:
    def on_request(req):
        try:
            body = req.post_data
        except Exception:  # noqa: BLE001 - binär eller otillgänglig body
            body = None
        store.extend(classify(req.url, body, time.monotonic(), extra))
    page.on("request", on_request)


def _settle(page, wait_ms: int, idle_timeout_ms: int = 25000) -> None:
    """Väntar tills nätverket är lugnt (inga anrop på 500 ms) och sedan wait_ms till, så att sena taggar hinner skicka."""
    try:
        page.wait_for_load_state("networkidle", timeout=idle_timeout_ms)
    except Exception:  # noqa: BLE001 - sidor med ständig trafik blir aldrig helt lugna; vi går vidare
        pass
    page.wait_for_timeout(wait_ms)


def _dom_snapshot(page) -> dict:
    try:
        return page.evaluate(DOM_JS)
    except Exception as exc:  # noqa: BLE001 - sidan kan ha navigerat bort
        return {"elements": {}, "inline": {}, "datalayer_gtm_js": 0, "fel": str(exc)[:120]}


def _find_accept(page):
    accept = None
    names = []
    for b in page.get_by_role("button").all():
        try:
            if not b.is_visible():
                continue
            name = (b.inner_text() or "").strip()
        except Exception:  # noqa: BLE001
            continue
        names.append(name[:40])
        if accept is None and ACCEPT.match(name):
            accept = b
    return accept, names


def run_browser(url: str, args, extra: set[str]) -> dict:
    from playwright.sync_api import sync_playwright

    phases: dict[str, list[dict]] = {"A": []}
    dom: dict[str, dict] = {}
    info: dict = {"url": url, "viewport": args.viewport}
    with sync_playwright() as pw:
        launch: dict = {"headless": True}
        if args.chromium_path:
            launch["executable_path"] = args.chromium_path
        if args.no_sandbox:
            launch["args"] = ["--no-sandbox"]
        browser = pw.chromium.launch(**launch)
        ctx = browser.new_context(locale="sv-SE", **(DESKTOP if args.viewport == "desktop" else MOBILE))
        page = ctx.new_page()
        store: list[dict] = []
        _capture(page, store, extra)
        page.goto(url, wait_until="domcontentloaded", timeout=45000)
        _settle(page, args.wait_ms)
        phases["A"] = list(store)
        accept, names = _find_accept(page)
        info["visible_buttons"] = names[:12]
        info["banner_found"] = accept is not None
        if accept is not None:
            n = len(store)
            try:
                accept.click(timeout=8000)
                _settle(page, args.wait_ms)
                phases["B"] = list(store[n:])
                info["accepted"] = True
            except Exception as exc:  # noqa: BLE001
                info["accept_error"] = str(exc)[:160]
                phases["B"] = list(store[n:])
            dom["A+B"] = _dom_snapshot(page)
            if not args.no_reload:
                n = len(store)
                page.reload(wait_until="domcontentloaded", timeout=45000)
                _settle(page, args.wait_ms)
                phases["C"] = list(store[n:])
                dom["C"] = _dom_snapshot(page)
        else:
            dom["A+B"] = _dom_snapshot(page)
        browser.close()
    return {"phases": phases, "dom": dom, "info": info}


# ----------------------------------------------------------------------------------------------------------------------------------
# Rapport
# ----------------------------------------------------------------------------------------------------------------------------------

def report(result: dict, args, out: Path | None) -> tuple[str, int]:
    phases = result["phases"]
    dom = result.get("dom", {})
    a = analyse(phases, dom=dom)
    order = [p for p in ("A", "B", "C") if p in phases]
    lines = [f"GTM-nätverkstest, {result['info']['url']} ({result['info']['viewport']})",
             "Körning A = första besöket utan samtycke. B = nya anrop efter klick på acceptera. C = ny sidladdning med samtycke sparat.", ""]
    if not result["info"].get("banner_found"):
        lines.append("OBS: ingen samtyckesruta hittades, så bara körning A gjordes. Shopifys ruta visas bara i vissa regioner och testet körs från"
                     " ett datacenter; kör från svensk IP eller kontrollera Customer privacy i Shopify admin innan du drar slutsatser.")
        lines.append("")
    lines.append(render_table(a["rows"], order, a["flagged_keys"]))
    lines.append("")
    if dom:
        lines.append("Container i sidans DOM efter laddning (A+B = första besöket, C = ny laddning). Antal gtm.js-skriptelement / inbyggda laddningsskript:")
        for name in ("A+B", "C"):
            if name in dom:
                snap = dom[name]
                ids = sorted(set(snap["elements"]) | set(snap["inline"]))
                cont = ", ".join(f"{i}: {snap['elements'].get(i, 0)} / {snap['inline'].get(i, 0)}" for i in ids) or "inga"
                lines.append(f"  {name}: {cont}; gtm.js-händelser i dataLayer: {snap.get('datalayer_gtm_js', 0)}")
        lines.append("")
    total = {p: len(v) for p, v in phases.items()}
    lines.append("Antal räknade anrop: " + ", ".join(f"{p}={n}" for p, n in total.items()))
    if a["flags"]:
        lines.append("")
        lines.append("FLAGGOR:")
        for f in a["flags"]:
            lines.append(f"  {f['slag']}: {f['text']} [{f['sidladdning']}]")
    else:
        lines.append("Inga flaggor: ingen container laddas mer än en gång och inga händelser skickas dubbelt inom 2 s.")
    ga4_gcs = sorted({r.get("gcs", "") for r in phases.get("A", []) if r["typ"] == "ga4" and r.get("gcs")})
    if ga4_gcs:
        lines.append("Samtyckessignal (gcs) i GA4-anrop före samtycke: " + ", ".join(ga4_gcs) + " (G100 = allt nekat; se samtycke_test.py)")
    text = "\n".join(lines)
    if out is not None:
        out.mkdir(parents=True, exist_ok=True)
        (out / "gtm_natverk.json").write_text(json.dumps(
            {"info": result["info"], "phases": phases, "dom": dom, "tabell": a["rows"], "flaggor": a["flags"]}, ensure_ascii=False, indent=1, default=str),
            encoding="utf-8")
        (out / "gtm_natverk.txt").write_text(text + "\n", encoding="utf-8")
    return text, (1 if a["flags"] else 0)


# ----------------------------------------------------------------------------------------------------------------------------------
# Test: logik och lokal testsida
# ----------------------------------------------------------------------------------------------------------------------------------

def test_logic() -> int:
    """Enhetstest av räknelogiken. Varje test kan misslyckas på det det ska kontrollera."""
    fails: list[str] = []

    def check(name: str, cond: bool) -> None:
        if not cond:
            fails.append(name)

    g = classify("https://www.googletagmanager.com/gtm.js?id=GTM-ABC123&l=dataLayer", None, 1.0)
    check("gtm.js ger container-id", len(g) == 1 and g[0]["typ"] == "gtm" and g[0]["id"] == "GTM-ABC123")
    check("gtm.js på annan domän räknas inte", classify("https://example.com/gtm.js?id=GTM-X", None, 1.0) == [])
    check("extra värd räknas", len(classify("https://metrics.butik.se/gtm.js?id=GTM-S", None, 1.0, {"metrics.butik.se"})) == 1)
    check("gtag/js räknas separat", classify("https://www.googletagmanager.com/gtag/js?id=G-AAAA", None, 1.0)[0]["typ"] == "gtag")

    e = classify("https://region1.google-analytics.com/g/collect?v=2&tid=G-AAAA&en=page_view&dl=https%3A%2F%2Fb.se%2F", None, 2.0)
    check("GA4 en och tid", len(e) == 1 and e[0]["event"] == "page_view" and e[0]["id"] == "G-AAAA" and e[0]["dl"] == "https://b.se/")
    b = classify("https://www.google-analytics.com/g/collect?v=2&tid=G-AAAA", "en=scroll&epn.x=1\nen=user_engagement&_et=5\n", 3.0)
    check("GA4 batch ger en post per rad i bodyn", [r["event"] for r in b] == ["scroll", "user_engagement"])
    check("GA4 utan en räknas som (saknas)", classify("https://x.se/g/collect?v=2&tid=G-AAAA", None, 1.0)[0]["event"] == "(saknas)")
    m = classify("https://www.facebook.com/tr/?id=999&ev=PageView&dl=https%3A%2F%2Fb.se%2F&eid=e1", None, 4.0)
    check("Meta id och ev", len(m) == 1 and m[0]["id"] == "999" and m[0]["event"] == "PageView" and m[0]["eid"] == "e1")
    check("annan /tr på okänd domän räknas inte", classify("https://example.com/tr?id=1&ev=PageView", None, 1.0) == [])
    check("orelaterat anrop ger inga poster", classify("https://b.se/cart.js", None, 1.0) == [])

    def ev(typ, i, name, t, dl="https://b.se/"):
        return {"typ": typ, "id": i, "event": name, "t": t, "dl": dl, "url": f"https://x/{name}"}

    # container två gånger
    two = [ev("gtm", "GTM-A", "gtm.js", 1.0), ev("gtm", "GTM-A", "gtm.js", 1.1), ev("gtm", "GTM-B", "gtm.js", 1.2)]
    fl = find_flags(two)
    check("container två gånger flaggas", [f["id"] for f in fl if f["slag"] == "CONTAINER"] == ["GTM-A"])
    check("container en gång flaggas inte", find_flags([ev("gtm", "GTM-A", "gtm.js", 1.0)]) == [])
    # dubbletter
    check("samma händelse inom 1,5 s flaggas", len(find_flags([ev("ga4", "G-1", "page_view", 10.0), ev("ga4", "G-1", "page_view", 11.5)])) == 1)
    check("samma händelse 2,5 s isär flaggas inte", find_flags([ev("ga4", "G-1", "page_view", 10.0), ev("ga4", "G-1", "page_view", 12.5)]) == [])
    check("gränsvärdet 2,0 s flaggas", len(find_flags([ev("ga4", "G-1", "page_view", 10.0), ev("ga4", "G-1", "page_view", 12.0)])) == 1)
    check("olika händelsenamn flaggas inte", find_flags([ev("ga4", "G-1", "page_view", 10.0), ev("ga4", "G-1", "scroll", 10.1)]) == [])
    check("olika mät-id flaggas inte", find_flags([ev("ga4", "G-1", "page_view", 10.0), ev("ga4", "G-2", "page_view", 10.1)]) == [])
    check("olika sidadresser flaggas inte", find_flags([ev("ga4", "G-1", "page_view", 10.0, "https://b.se/a"), ev("ga4", "G-1", "page_view", 10.1, "https://b.se/b")]) == [])
    check("Meta PageView två gånger flaggas", len(find_flags([ev("meta", "9", "PageView", 5.0), ev("meta", "9", "PageView", 5.2)])) == 1)
    three = find_flags([ev("ga4", "G-1", "page_view", 1.0), ev("ga4", "G-1", "page_view", 2.5), ev("ga4", "G-1", "page_view", 4.0)])
    check("kedja av tre anrop är ett kluster med antal 3", len(three) == 1 and three[0]["antal"] == 3)
    far = find_flags([ev("ga4", "G-1", "page_view", 1.0), ev("ga4", "G-1", "page_view", 1.5), ev("ga4", "G-1", "page_view", 30.0), ev("ga4", "G-1", "page_view", 30.4)])
    check("två separata kluster ger två flaggor", len(far) == 2)
    # tabell och analys
    ph = {"A": two + [ev("ga4", "G-1", "page_view", 1.3)], "B": [ev("meta", "9", "PageView", 20.0)], "C": [ev("gtm", "GTM-A", "gtm.js", 30.0)]}
    a = analyse(ph)
    rows = {(r["typ"], r["id"], r["event"]): r for r in a["rows"]}
    check("tabell: GTM-A två i A och en i C", rows[("gtm", "GTM-A", "gtm.js")]["A"] == 2 and rows[("gtm", "GTM-A", "gtm.js")]["C"] == 1)
    check("tabell: Meta bara i B", rows[("meta", "9", "PageView")]["B"] == 1 and rows[("meta", "9", "PageView")]["A"] == 0)
    check("en container per sidladdning är inte en flagga i C", all(f["sidladdning"] != "C (ny laddning med samtycke)" for f in a["flags"]))
    txt = render_table(a["rows"], ["A", "B", "C"], a["flagged_keys"])
    check("tabellen markerar flaggad rad", "<-- kontrollera" in txt and "GTM-A" in txt)
    # DOM-flaggor
    d1 = find_dom_flags({"elements": {"GTM-A": 2, "GTM-B": 1}, "inline": {"GTM-A": 1}, "datalayer_gtm_js": 2})
    check("DOM: två skriptelement flaggas, ett inte", [f["id"] for f in d1] == ["GTM-A"])
    two_inline = find_dom_flags({"elements": {"GTM-A": 1}, "inline": {"GTM-A": 2}, "datalayer_gtm_js": 2})
    check("DOM: två inbyggda snuttar flaggas", any("inbyggda" in f["text"] and f["id"] == "GTM-A" for f in two_inline))
    check("DOM: en inbyggd snutt och ett element flaggas inte", find_dom_flags({"elements": {"GTM-A": 1}, "inline": {"GTM-A": 1}, "datalayer_gtm_js": 1}) == [])
    check("DOM: lika många dataLayer-händelser som containrar flaggas inte",
          find_dom_flags({"elements": {"GTM-A": 1, "GTM-B": 1}, "inline": {}, "datalayer_gtm_js": 2}) == [])
    check("DOM: fler dataLayer-händelser än containrar flaggas",
          len(find_dom_flags({"elements": {"GTM-A": 1}, "inline": {}, "datalayer_gtm_js": 2})) == 1)
    check("DOM: tom sida ger inga flaggor", find_dom_flags({"elements": {}, "inline": {}, "datalayer_gtm_js": 0}) == [])
    a2 = analyse({"A": [ev("gtm", "GTM-A", "gtm.js", 1.0)]}, dom={"A+B": {"elements": {"GTM-A": 2}, "inline": {}, "datalayer_gtm_js": 2}})
    check("analys: DOM-flagga syns trots ett nätverksanrop", len(a2["flags"]) >= 1 and ("gtm", "GTM-A", "gtm.js") in a2["flagged_keys"])
    if fails:
        print("ENHETSTEST FEL: " + "; ".join(fails))
        return 1
    print("Enhetstest av räknelogiken: alla kontroller godkända.")
    return 0


TEST_PAGE = """<!doctype html><html lang="sv"><head><meta charset="utf-8"><title>GTM-test</title></head><body>
<h1>Testbutik</h1>
<button id="acc" type="button">Acceptera alla</button>
<script>window.dataLayer = [];
document.getElementById('acc').addEventListener('click', function () {
  try { localStorage.setItem('samtycke', '1'); } catch (e) {}
  document.dispatchEvent(new CustomEvent('samtycke-givet'));
});</script>
<script src="/gtm.js?id=GTM-TESTAAA"></script>
<script src="/gtm.js?id=GTM-TESTAAA"></script>
<script src="/gtm.js?id=GTM-TESTBBB"></script>
<script src="/gtm.js?id=GTM-TESTCCC"></script>
<script src="/gtm.js?id=GTM-TESTCCC&l=dataLayer2"></script>
</body></html>"""

# Attrapp: varje körning av filen beter sig som en container och lägger en gtm.js-händelse i dataLayer, som den riktiga GTM-snutten gör.
# AAA skickar sidvisning (GA4) och, efter samtycke, Meta PageView. AAA laddas två gånger med exakt samma adress: webbläsaren gör då ETT
# nätverksanrop men kör skriptet två gånger, så förväntat resultat är två sidvisningar och två PageView (dubbletter), en nätverksräkning
# på 1 men två skriptelement i DOM.
# BBB skickar en batch med två GA4-händelser (scroll och user_engagement) i bodyn, en gång.
# CCC laddas två gånger med olika adresser (en extra parameter): två nätverksanrop och två skriptelement.
FAKE_GTM = """(function () {
  var id = new URL(document.currentScript.src).searchParams.get('id');
  var ok = false; try { ok = localStorage.getItem('samtycke') === '1'; } catch (e) {}
  var dl = encodeURIComponent(location.href);
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({'gtm.start': Date.now(), event: 'gtm.js'});
  // Pixeln har ts och r i adressen, som den riktiga pixeln, annars slår webbläsaren ihop två identiska bildanrop till ett
  function pixel() { new Image().src = '/tr?id=PIXEL111&ev=PageView&dl=' + dl + '&ts=' + Date.now() + '&r=' + Math.random(); }
  if (id === 'GTM-TESTAAA') {
    navigator.sendBeacon('/g/collect?v=2&tid=G-TEST1111&gcs=' + (ok ? 'G111' : 'G100') + '&en=page_view&dl=' + dl);
    if (ok) { pixel(); } else { document.addEventListener('samtycke-givet', pixel); }
  }
  if (id === 'GTM-TESTBBB') {
    navigator.sendBeacon('/g/collect?v=2&tid=G-TEST1111&gcs=' + (ok ? 'G111' : 'G100') + '&dl=' + dl,
                         'en=scroll&epn.percent_scrolled=90\\nen=user_engagement&_et=1000');
  }
})();"""


class _Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, body: bytes = b"", ctype: str = "text/plain") -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):  # noqa: N802
        path = urlsplit(self.path).path
        if path == "/":
            self._send(200, TEST_PAGE.encode(), "text/html; charset=utf-8")
        elif path == "/gtm.js":
            self._send(200, FAKE_GTM.encode(), "application/javascript")
        elif path == "/tr":
            self._send(200, b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;", "image/gif")
        else:
            self._send(404)

    def do_POST(self):  # noqa: N802
        n = int(self.headers.get("Content-Length") or 0)
        if n:
            self.rfile.read(n)
        self._send(204)

    def log_message(self, *a):  # tyst
        pass


def selftest(args) -> int:
    srv = ThreadingHTTPServer(("127.0.0.1", 0), _Handler)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    host = f"127.0.0.1:{port}"
    args.viewport = args.viewport or "desktop"
    try:
        result = run_browser(f"http://{host}/", args, {host})
    except ImportError:
        print("Playwright saknas: pip install playwright && playwright install chromium", file=sys.stderr)
        return 2
    finally:
        srv.shutdown()
    text, _ = report(result, args, Path(args.out) if args.out else None)
    print(text)
    a = analyse(result["phases"], dom=result.get("dom"))
    rows = {(r["typ"], r["id"], r["event"]): r for r in a["rows"]}
    dom = result.get("dom", {})
    flags = a["flags"]
    expected = [
        ("AAA: ett nätverksanrop i A trots att skriptet laddas två gånger (webbläsaren slår ihop identiska adresser)",
         rows.get(("gtm", "GTM-TESTAAA", "gtm.js"), {}).get("A") == 1),
        ("AAA: två skriptelement i DOM", dom.get("A+B", {}).get("elements", {}).get("GTM-TESTAAA") == 2),
        ("BBB: ett nätverksanrop och ett skriptelement", rows.get(("gtm", "GTM-TESTBBB", "gtm.js"), {}).get("A") == 1
         and dom.get("A+B", {}).get("elements", {}).get("GTM-TESTBBB") == 1),
        ("CCC: två nätverksanrop i A (olika adresser)", rows.get(("gtm", "GTM-TESTCCC", "gtm.js"), {}).get("A") == 2),
        ("dataLayer har 5 gtm.js-händelser (AAA 2, BBB 1, CCC 2)", dom.get("A+B", {}).get("datalayer_gtm_js") == 5),
        ("två page_view i A", rows.get(("ga4", "G-TEST1111", "page_view"), {}).get("A") == 2),
        ("batch ger scroll och user_engagement i A", rows.get(("ga4", "G-TEST1111", "scroll"), {}).get("A") == 1
         and rows.get(("ga4", "G-TEST1111", "user_engagement"), {}).get("A") == 1),
        ("ingen Meta-händelse före samtycke", rows.get(("meta", "PIXEL111", "PageView"), {}).get("A", 0) == 0),
        ("två PageView efter klick (B)", rows.get(("meta", "PIXEL111", "PageView"), {}).get("B") == 2),
        ("ny laddning (C) har två page_view och två PageView", rows.get(("ga4", "G-TEST1111", "page_view"), {}).get("C") == 2
         and rows.get(("meta", "PIXEL111", "PageView"), {}).get("C") == 2),
        ("flagga för AAA (via DOM)", any(f["slag"] == "CONTAINER" and f["id"] == "GTM-TESTAAA" for f in flags)),
        ("flagga för CCC (via nätverk)", any(f["slag"] == "CONTAINER" and f["id"] == "GTM-TESTCCC" and "laddas 2 gånger" in f["text"] for f in flags)),
        ("ingen containerflagga för enbart BBB", not any(f["slag"] == "CONTAINER" and f["id"] == "GTM-TESTBBB" for f in flags)),
        ("flagga för dataLayer-händelser", any(f["slag"] == "CONTAINER" and "dataLayer" in f["text"] for f in flags)),
        ("dubblett page_view flaggad", any(f["slag"] == "DUBBLETT" and f["event"] == "page_view" for f in flags)),
        ("dubblett PageView flaggad", any(f["slag"] == "DUBBLETT" and f["event"] == "PageView" for f in flags)),
        ("scroll flaggas inte (ett anrop)", not any(f.get("event") == "scroll" for f in flags)),
    ]
    bad = [name for name, ok in expected if not ok]
    print()
    print("SJÄLVTEST FEL: " + "; ".join(bad) if bad else "SJÄLVTEST OK: tabellen och flaggorna stämmer med vad testsidan är byggd att göra.")
    return 1 if bad else 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--url", help="Adressen som testas, t.ex. https://www.gorillasports.se/")
    p.add_argument("--viewport", choices=["mobile", "desktop"], default=None, help="Standard: mobil (desktop i --selftest)")
    p.add_argument("--wait-ms", type=int, default=3000, help="Extra väntetid efter att nätverket blivit lugnt (standard 3000)")
    p.add_argument("--out", default=None, help="Mapp för gtm_natverk.json och gtm_natverk.txt (standard: ingen fil)")
    p.add_argument("--chromium-path", help="Sökväg till en förinstallerad Chromium")
    p.add_argument("--no-sandbox", action="store_true", help="Starta Chromium med --no-sandbox (behövs ofta när den körs som root)")
    p.add_argument("--extra-host", action="append", default=[], help="Värd[:port] som också räknas, t.ex. en server-side GTM-domän")
    p.add_argument("--no-reload", action="store_true", help="Hoppa över körning C (ny sidladdning med samtycke)")
    p.add_argument("--strict", action="store_true", help="Avsluta med felkod 1 om något flaggas")
    p.add_argument("--test-logic", action="store_true", help="Kör enhetstest av räknelogiken (ingen webbläsare)")
    p.add_argument("--selftest", action="store_true", help="Kör mot en lokal testsida och en lokal attrapp (kräver Playwright)")
    args = p.parse_args(argv)
    if args.test_logic:
        return test_logic()
    if args.selftest:
        return selftest(args)
    if not args.url:
        p.error("--url krävs (eller --test-logic / --selftest)")
    args.viewport = args.viewport or "mobile"
    try:
        result = run_browser(args.url, args, {h.lower() for h in args.extra_host})
    except ImportError:
        print("Playwright saknas: pip install playwright && playwright install chromium", file=sys.stderr)
        return 2
    text, code = report(result, args, Path(args.out) if args.out else None)
    print(text)
    if args.out:
        print(f"\nRapport i {args.out}/")
    return code if args.strict else 0


if __name__ == "__main__":
    sys.exit(main())
