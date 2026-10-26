#!/usr/bin/env python3
"""Visar var strukturerad data och spårning kommer ifrån på en produktsida (bara läsning).

Skriver ut: varje JSON-LD-skript (öppningstagg och början av innehållet), antal GTM-laddningar per container,
canonical och og:url, och om adresserna i schemat pekar på en annan domän än sidan.

  python3 scripts/schema_kallor.py --base-url https://www.gorillasports.se
  python3 scripts/schema_kallor.py --base-url https://www.gorillasports.dk --url https://www.gorillasports.dk/products/<handle>
Utan --url hämtas den första produkten i sitemapen.
"""
from __future__ import annotations

import argparse
import re
import urllib.parse
import urllib.request


def get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; SchemaKallor/1.0)", "Accept-Encoding": "identity"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def first_product(base: str) -> str:
    idx = get(base + "/sitemap.xml")
    for child in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", idx):
        if "product" in child:
            for u in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", get(child)):
                if "/products/" in u:
                    return u
    raise SystemExit("Hittade ingen produkt i sitemapen. Ange --url.")


def analyse(html: str, page_url: str) -> dict:
    host = urllib.parse.urlparse(page_url).netloc.replace("www.", "")
    scripts = []
    for m in re.finditer(r"<script([^>]*ld\+json[^>]*)>(.*?)</script>", html, re.S | re.I):
        body = re.sub(r"\s+", " ", m.group(2)).strip()
        scripts.append({"attribut": re.sub(r"\s+", " ", m.group(1)).strip(), "borjan": body[:240],
                        "domaner": sorted({urllib.parse.urlparse(u).netloc.replace("www.", "") for u in re.findall(r'https?://[^"\\\s]+', body)
                                           if "schema.org" not in u and "cdn.shopify" not in u and "/cdn/" not in u})})
    return {
        "skript": scripts,
        "gtm": {k: html.count(k) for k in sorted(set(re.findall(r"GTM-[A-Z0-9]+", html)))},
        "gtm_js_laddningar": len(re.findall(r"gtm\.js\?id=GTM-", html)),
        "canonical": re.findall(r'<link[^>]*rel="canonical"[^>]*>', html),
        "og_url": re.findall(r'<meta[^>]*property="og:url"[^>]*>', html),
        "https_https": html.count("https:https"),
        "sidans_domän": host,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base-url", required=True)
    ap.add_argument("--url")
    a = ap.parse_args()
    base = a.base_url.rstrip("/")
    url = a.url or first_product(base)
    r = analyse(get(url), url)
    print(f"Sida: {url}")
    print(f"GTM-containrar (antal förekomster): {r['gtm']}; direkta gtm.js-laddningar från snippeten: {r['gtm_js_laddningar']}")
    print(f"Canonical: {r['canonical']}\nog:url:    {r['og_url']}\n'https:https' i sidan: {r['https_https']}")
    print(f"JSON-LD-skript: {len(r['skript'])}")
    for i, s in enumerate(r["skript"]):
        flagg = [d for d in s["domaner"] if d != r["sidans_domän"]]
        print(f"\n[{i}] <script {s['attribut']}>\n    {s['borjan']}\n    adresser i blocket pekar på: {s['domaner']}" + (f"   <-- ANNAN DOMÄN: {flagg}" if flagg else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
