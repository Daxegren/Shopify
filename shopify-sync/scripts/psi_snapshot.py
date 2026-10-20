#!/usr/bin/env python3
"""Mäter sidhastighet för några representativa sidor med Googles PageSpeed Insights och skriver en kort rapport.

Bara läsning: sidorna hämtas av Googles tjänst, inget ändras på sajten. Bara standardbiblioteket behövs.

  read -rs PSI_API_KEY && export PSI_API_KEY   # nyckeln skapas i Cloud Console (APIs & Services > Credentials), begränsas till PageSpeed Insights API
                                               # och klistras bara in här (syns inte). Skapa den inte med gcloud i terminalen: kommandot skriver ut nyckeln.
  python3 scripts/psi_snapshot.py                        # standardsidor för gorillasports.se, mobil
  python3 scripts/psi_snapshot.py --urls https://a/ https://b/ --strategy desktop

Utan nyckel delar anropen en gemensam gratiskvot som ofta är slut (fel 429).
Fältdata (verkliga besökare, p75) finns bara för sidor med tillräckligt med trafik; labbdata (Lighthouse) finns alltid.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
DEFAULT_URLS = [
    "https://www.gorillasports.se/",
    "https://www.gorillasports.se/collections/stallbara-hantlar",
    "https://www.gorillasports.se/products/multi-pull-up-bar-dorr-svart",
    "https://www.gorillasports.se/blogs/blogg/vad-ar-fascia",
    "https://www.gorillasports.se/collections/spinningcykel",
]
FIELD_KEYS = {"LARGEST_CONTENTFUL_PAINT_MS": "LCP", "INTERACTION_TO_NEXT_PAINT": "INP", "CUMULATIVE_LAYOUT_SHIFT_SCORE": "CLS"}


def fetch(url: str, strategy: str, key: str | None, retries: int = 3) -> dict:
    params = {"url": url, "strategy": strategy, "category": "performance"}
    if key:
        params["key"] = key
    full = f"{ENDPOINT}?{urllib.parse.urlencode(params)}"
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(full, timeout=180) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (500, 503) and attempt < retries - 1:
                time.sleep(2 ** attempt * 3)
                continue
            body = e.read().decode("utf-8", "replace")[:300]
            raise RuntimeError(f"HTTP {e.code}: {body}") from None
    raise RuntimeError("misslyckades efter flera försök")


def summarize(data: dict, top: int = 5) -> dict:
    """Plockar ut det som behövs ur ett PageSpeed-svar. Saknade fält ger None eller tomma listor, inte fel."""
    field = {}
    for k, label in FIELD_KEYS.items():
        m = ((data.get("loadingExperience") or {}).get("metrics") or {}).get(k)
        if m and m.get("percentile") is not None:
            p = m["percentile"]
            field[label] = {"p75": p / 100 if label == "CLS" else p, "category": m.get("category")}
    lh = data.get("lighthouseResult") or {}
    audits = lh.get("audits") or {}
    score = ((lh.get("categories") or {}).get("performance") or {}).get("score")

    def num(name):
        return (audits.get(name) or {}).get("numericValue")

    lcp_el = None
    items = ((audits.get("largest-contentful-paint-element") or {}).get("details") or {}).get("items") or []
    if items and items[0].get("items"):
        node = (items[0]["items"][0] or {}).get("node") or {}
        lcp_el = (node.get("snippet") or node.get("selector") or "")[:140] or None
    opp = []
    for name, a in audits.items():
        d = a.get("details") or {}
        saving = d.get("overallSavingsMs") or 0
        if d.get("type") == "opportunity" and saving > 0:
            opp.append((saving, a.get("title") or name, d.get("overallSavingsBytes")))
    opp.sort(reverse=True)
    third = []
    for it in (((audits.get("third-party-summary") or {}).get("details") or {}).get("items") or [])[:top]:
        third.append({"entity": it.get("entity") if isinstance(it.get("entity"), str) else (it.get("entity") or {}).get("text"),
                      "blocking_ms": round(it.get("blockingTime") or 0), "kb": round((it.get("transferSize") or 0) / 1024)})
    return {"score": None if score is None else round(score * 100), "field": field,
            "lab": {"LCP": num("largest-contentful-paint"), "TBT": num("total-blocking-time"), "CLS": num("cumulative-layout-shift"),
                    "FCP": num("first-contentful-paint")},
            "lcp_element": lcp_el, "opportunities": [(round(s), t, b) for s, t, b in opp[:top]],
            "third_party": third, "total_kb": None if num("total-byte-weight") is None else round(num("total-byte-weight") / 1024)}


def fmt_ms(v) -> str:
    return "–" if v is None else f"{v / 1000:.1f} s"


def render(url: str, s: dict) -> str:
    f = s["field"]
    field = ", ".join(f"{k} {(v['p75'] / 1000):.1f} s" if k == "LCP" else f"{k} {v['p75']}{' ms' if k == 'INP' else ''} ({v['category']})"
                      for k, v in f.items()) or "ingen fältdata"
    out = [f"## {url}", f"- Lighthouse-poäng: {s['score'] if s['score'] is not None else '–'}",
           f"- Verkliga besökare (p75): {field}",
           f"- Labb: LCP {fmt_ms(s['lab']['LCP'])}, FCP {fmt_ms(s['lab']['FCP'])}, blockering (TBT) {fmt_ms(s['lab']['TBT'])}, sidvikt {s['total_kb'] or '–'} kB"]
    if s["lcp_element"]:
        out.append(f"- Största element (LCP): `{s['lcp_element']}`")
    for ms, title, b in s["opportunities"]:
        out.append(f"- Möjlig vinst {ms} ms: {title}" + (f" ({round(b / 1024)} kB)" if b else ""))
    for t in s["third_party"]:
        out.append(f"- Tredjepart: {t['entity']}, blockerar {t['blocking_ms']} ms, {t['kb']} kB")
    return "\n".join(out) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--urls", nargs="*", default=DEFAULT_URLS)
    ap.add_argument("--strategy", choices=["mobile", "desktop"], default="mobile")
    ap.add_argument("--json", help="Spara råsvaren i en fil för senare analys")
    args = ap.parse_args(argv)
    key = os.environ.get("PSI_API_KEY")
    if not key:
        print("Obs: PSI_API_KEY saknas; gratiskvoten är gemensam och ofta slut.", file=sys.stderr)
    raw, failed = {}, 0
    print(f"# Sidhastighet ({args.strategy})\n")
    for url in args.urls:
        try:
            data = fetch(url, args.strategy, key)
            raw[url] = data
            print(render(url, summarize(data)))
        except Exception as exc:  # noqa: BLE001 - en sida får inte stoppa de andra
            failed += 1
            print(f"## {url}\n- MISSLYCKADES: {exc}\n")
    if args.json:
        with open(args.json, "w") as fh:
            json.dump(raw, fh)
    return 1 if failed == len(args.urls) else 0


if __name__ == "__main__":
    sys.exit(main())
