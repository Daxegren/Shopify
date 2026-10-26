#!/usr/bin/env python3
"""Onsite-kontroll för SEO och GEO (bara läsning, ändrar ingenting i Shopify).

Hämtar robots.txt, llms.txt, sitemap och ett slumpat urval av startsida, kategorier och produkter, och mäter:
  * crawlers (sökmotorer och AI-botar) i robots.txt
  * omdirigeringar http -> https och www
  * titel, metabeskrivning, rubriker, canonical, hreflang, noindex
  * strukturerad data (Product, Organization, BreadcrumbList, FAQ m.fl.) och vilka fält som saknas
  * alt-texter, textmängd på kategorisidor, interna länkar, parametrar som kan ge dubbletter
  * svarstid och sidstorlek

Körning (Cloud Shell, ingen installation behövs, bara Python 3):
  python3 scripts/onsite_kontroll.py --base-url https://www.gorillasports.se --ut ~/onsite-gorilla-se

Skriver <ut>/onsite.json och <ut>/onsite.md. Skriv in den sista raden ("SAMMANFATTNING ...") i chatten.
"""
from __future__ import annotations

import argparse
import gzip
import json
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zlib
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.robotparser import RobotFileParser

UA = "Mozilla/5.0 (compatible; OnsiteKontroll/1.0; +intern kontroll)"
AI_BOTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot",
           "Perplexity-User", "Google-Extended", "Applebot-Extended", "CCBot", "Bytespider", "meta-externalagent"]
SEARCH_BOTS = ["Googlebot", "Googlebot-Image", "Bingbot", "AdsBot-Google"]
GTIN_KEYS = ("gtin", "gtin8", "gtin12", "gtin13", "gtin14", "isbn")
PARAMS = ["sort_by=price-ascending", "filter.v.price.gte=100", "page=2", "utm_source=test", "variant=1", "q=test"]


# ---------------------------------------------------------------- hämtning
class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):  # noqa: D401
        return None


_opener = urllib.request.build_opener(_NoRedirect)


def fetch(url: str, max_hops: int = 6, timeout: int = 30) -> dict:
    """Hämtar en adress och följer omdirigeringar manuellt. Returnerar status, kedja, text, svarstid och rubriker."""
    chain: list[tuple[int, str]] = []
    cur = url
    t0 = time.time()
    for _ in range(max_hops + 1):
        req = urllib.request.Request(cur, headers={"User-Agent": UA, "Accept-Encoding": "gzip, deflate",
                                                   "Accept-Language": "sv,en;q=0.5"})
        try:
            resp = _opener.open(req, timeout=timeout)
            status, headers, raw = resp.status, resp.headers, resp.read()
        except urllib.error.HTTPError as e:
            status, headers = e.code, e.headers
            raw = e.read() if e.fp else b""
        except Exception as e:  # nätverksfel
            return {"url": url, "final": cur, "status": 0, "chain": chain, "error": str(e), "text": "", "bytes": 0,
                    "ms": round((time.time() - t0) * 1000), "headers": {}}
        chain.append((status, cur))
        loc = headers.get("Location")
        if status in (301, 302, 303, 307, 308) and loc:
            cur = urllib.parse.urljoin(cur, loc)
            continue
        enc = (headers.get("Content-Encoding") or "").lower()
        try:
            if enc == "gzip":
                raw = gzip.decompress(raw)
            elif enc == "deflate":
                raw = zlib.decompress(raw)
        except Exception:
            pass
        text = raw.decode("utf-8", errors="replace")
        return {"url": url, "final": cur, "status": status, "chain": chain, "text": text, "bytes": len(raw),
                "ms": round((time.time() - t0) * 1000), "headers": {k.lower(): v for k, v in headers.items()}}
    return {"url": url, "final": cur, "status": 0, "chain": chain, "error": "för många omdirigeringar", "text": "",
            "bytes": 0, "ms": round((time.time() - t0) * 1000), "headers": {}}


# ---------------------------------------------------------------- HTML
class Page(HTMLParser):
    SKIP = {"script", "style", "noscript", "template", "svg"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._in_title = False
        self.meta: dict[str, str] = {}
        self.canonical = ""
        self.hreflang: list[tuple[str, str]] = []
        self.h = {f"h{i}": 0 for i in range(1, 7)}
        self.h1_text: list[str] = []
        self._h1 = False
        self.imgs: list[dict] = []
        self.links: list[str] = []
        self.jsonld: list[str] = []
        self._ld = False
        self._skip = 0
        self._main = 0
        self.has_main = False
        self.words_all = 0
        self.words_main = 0
        self.details = 0

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = (a.get("name") or a.get("property") or a.get("http-equiv") or "").lower()
            if key:
                self.meta[key] = a.get("content", "")
        elif tag == "link":
            rel = a.get("rel", "").lower()
            if "canonical" in rel:
                self.canonical = a.get("href", "")
            elif "alternate" in rel and a.get("hreflang"):
                self.hreflang.append((a["hreflang"], a.get("href", "")))
        elif tag in self.h:
            self.h[tag] += 1
            if tag == "h1":
                self._h1 = True
                self.h1_text.append("")
        elif tag == "img":
            self.imgs.append({"src": a.get("src") or a.get("data-src") or "", "alt": a.get("alt"),
                              "loading": a.get("loading", ""), "width": a.get("width", ""), "height": a.get("height", "")})
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "main":
            self._main += 1
            self.has_main = True
        elif tag == "details":
            self.details += 1
        if tag == "script" and "ld+json" in a.get("type", "").lower():
            self._ld = True
            self.jsonld.append("")
        elif tag in self.SKIP:
            self._skip += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "h1":
            self._h1 = False
        elif tag == "main" and self._main:
            self._main -= 1
        if tag == "script" and self._ld:
            self._ld = False
        elif tag in self.SKIP and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._ld:
            self.jsonld[-1] += data
            return
        if self._h1 and self.h1_text:
            self.h1_text[-1] += data
        if self._skip:
            return
        n = len(data.split())
        self.words_all += n
        if self._main:
            self.words_main += n


def parse_html(html: str) -> Page:
    p = Page()
    try:
        p.feed(html)
    except Exception:
        pass
    return p


def jsonld_nodes(blocks: list[str]) -> tuple[list[dict], int]:
    """Plattar ut alla JSON-LD-block (inklusive @graph). Returnerar noder och antal block som inte gick att tolka."""
    nodes: list[dict] = []
    bad = 0

    def walk(x):
        if isinstance(x, list):
            for i in x:
                walk(i)
        elif isinstance(x, dict):
            nodes.append(x)
            if "@graph" in x:
                walk(x["@graph"])

    for b in blocks:
        try:
            walk(json.loads(b.strip()))
        except Exception:
            bad += 1
    return nodes, bad


def types_of(n: dict) -> list[str]:
    t = n.get("@type")
    return [t] if isinstance(t, str) else [x for x in (t or []) if isinstance(x, str)]


def offers_of(prod: dict) -> list[dict]:
    o = prod.get("offers")
    out = [o] if isinstance(o, dict) else [x for x in (o or []) if isinstance(x, dict)]
    flat: list[dict] = []
    for x in out:
        flat.append(x)
        flat.extend(y for y in (x.get("offers") or []) if isinstance(y, dict))
    return flat


def product_fields(prod: dict) -> dict[str, bool]:
    offs = offers_of(prod)

    def any_off(*keys):
        return any(o.get(k) not in (None, "", []) for o in offs for k in keys)

    brand = prod.get("brand")
    return {
        "name": bool(prod.get("name")),
        "image": bool(prod.get("image")),
        "description": bool(str(prod.get("description") or "").strip()),
        "sku": bool(prod.get("sku")),
        "gtin": any(prod.get(k) for k in GTIN_KEYS) or any_off(*GTIN_KEYS),
        "mpn": bool(prod.get("mpn")),
        "brand": bool((brand.get("name") if isinstance(brand, dict) else brand)),
        "pris": any_off("price", "lowPrice"),
        "valuta": any_off("priceCurrency"),
        "lagerstatus": any_off("availability"),
        "fraktinfo": bool(prod.get("shippingDetails")) or any_off("shippingDetails"),
        "returpolicy": bool(prod.get("hasMerchantReturnPolicy")) or any_off("hasMerchantReturnPolicy"),
        "betyg": bool(prod.get("aggregateRating")),
        "omdomen": bool(prod.get("review")),
    }


def internal(href: str, host: str) -> bool:
    if href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return False
    h = urllib.parse.urlparse(href)
    return not h.netloc or h.netloc.replace("www.", "") == host.replace("www.", "")


def analyse_page(html: str, url: str) -> dict:
    p = parse_html(html)
    host = urllib.parse.urlparse(url).netloc
    nodes, bad = jsonld_nodes(p.jsonld)
    types: dict[str, int] = {}
    for n in nodes:
        for t in types_of(n):
            types[t] = types.get(t, 0) + 1
    prods = [n for n in nodes if "Product" in types_of(n)]
    imgs = [i for i in p.imgs if i["src"] and not i["src"].startswith("data:")]
    robots = (p.meta.get("robots") or "").lower()
    internal_links = [l for l in p.links if internal(l, host)]
    return {
        "url": url,
        "titel": p.title.strip(), "titel_tecken": len(p.title.strip()),
        "beskrivning_tecken": len((p.meta.get("description") or "").strip()),
        "h1_antal": p.h["h1"], "h1": [t.strip() for t in p.h1_text][:2], "h2_antal": p.h["h2"],
        "canonical": p.canonical,
        "canonical_pekar_pa_sig": bool(p.canonical) and urllib.parse.urldefrag(p.canonical)[0].rstrip("/") == url.split("?")[0].rstrip("/"),
        "noindex": "noindex" in robots, "robots_meta": robots,
        "hreflang": [h[0] for h in p.hreflang],
        "og_titel": bool(p.meta.get("og:title")), "og_bild": bool(p.meta.get("og:image")),
        "jsonld_typer": types, "jsonld_trasiga": bad,
        "produkter": [product_fields(x) for x in prods],
        "bilder": len(imgs), "bilder_utan_alt": sum(1 for i in imgs if i["alt"] is None),
        "bilder_tom_alt": sum(1 for i in imgs if i["alt"] is not None and not i["alt"].strip()),
        "ord_main": p.words_main if p.has_main else p.words_all, "ord_totalt": p.words_all, "har_main": p.has_main,
        "interna_lankar": len(internal_links),
        "produktlankar": sum(1 for l in internal_links if "/products/" in l),
        "parameterlankar": sum(1 for l in internal_links if "?" in l and not l.startswith("#")),
        "faq_element": p.details,
        "organization_sameas": any("sameAs" in n and ("Organization" in types_of(n) or "Store" in types_of(n)) for n in nodes),
    }


# ---------------------------------------------------------------- robots och sitemap
def check_robots(text: str, base: str) -> dict:
    rp = RobotFileParser()
    rp.parse(text.splitlines())
    probe = [base + "/", base + "/products/x", base + "/collections/x", base + "/collections/x?sort_by=price-ascending",
             base + "/cart", base + "/search?q=x"]
    bots = {}
    for b in AI_BOTS + SEARCH_BOTS:
        bots[b] = {u.replace(base, "") or "/": rp.can_fetch(b, u) for u in probe}
    explicit = sorted(set(re.findall(r"(?im)^\s*user-agent:\s*(\S+)", text)))
    sitemaps = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", text)
    return {"bots": bots, "agenter_i_filen": explicit, "sitemaps": sitemaps,
            "disallow_rader": len(re.findall(r"(?im)^\s*disallow:", text)),
            "blockerar_alla_ai": [b for b in AI_BOTS if not bots[b]["/"]],
            "blockerar_google": [b for b in SEARCH_BOTS if not bots[b]["/"]]}


def locs(xml: str) -> list[str]:
    return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)


def read_sitemaps(base: str, robots_sitemaps: list[str]) -> dict:
    index_url = robots_sitemaps[0] if robots_sitemaps else base + "/sitemap.xml"
    idx = fetch(index_url)
    out = {"index": index_url, "status": idx["status"], "barn": {}, "produkter": [], "kategorier": [], "sidor": [], "bloggar": []}
    if idx["status"] != 200:
        return out
    children = [c for c in locs(idx["text"]) if c.endswith(".xml") or "sitemap" in c] or []
    if not children:
        children = [index_url]
    for c in children:
        r = fetch(c)
        urls = locs(r["text"]) if r["status"] == 200 else []
        out["barn"][c] = {"status": r["status"], "antal": len(urls)}
        for u in urls:
            path = urllib.parse.urlparse(u).path
            if "/products/" in path:
                out["produkter"].append(u)
            elif "/collections/" in path:
                out["kategorier"].append(u)
            elif "/blogs/" in path:
                out["bloggar"].append(u)
            elif "/pages/" in path:
                out["sidor"].append(u)
    return out


# ---------------------------------------------------------------- sammanställning
def pct(n: int, d: int) -> float:
    return round(n / d * 100, 1) if d else 0.0


def verdict(p: float, good=90, warn=50) -> str:
    return "OK" if p >= good else ("VARNING" if p >= warn else "BRIST")


def summarize(home: dict, colls: list[dict], prods: list[dict], robots: dict, extra: dict) -> dict:
    s: dict = {}
    n = len(prods)
    fields: dict[str, int] = {}
    with_prod = 0
    multi = 0
    for p in prods:
        if p["produkter"]:
            with_prod += 1
            if len(p["produkter"]) > 1:
                multi += 1
            merged: dict[str, bool] = {}
            for f in p["produkter"]:
                for k, v in f.items():
                    merged[k] = merged.get(k, False) or v
            for k, v in merged.items():
                fields[k] = fields.get(k, 0) + (1 if v else 0)
    s["produktsidor_provade"] = n
    s["produkt_schema_andel"] = pct(with_prod, n)
    s["produkt_schema_dubbletter"] = multi
    s["produktfalt_andel_av_sidor_med_schema"] = {k: pct(v, with_prod) for k, v in sorted(fields.items())}
    s["produkt_breadcrumb_andel"] = pct(sum(1 for p in prods if "BreadcrumbList" in p["jsonld_typer"]), n)
    s["produkt_titel_saknas"] = pct(sum(1 for p in prods if not p["titel"]), n)
    s["produkt_titel_for_lang_over_60"] = pct(sum(1 for p in prods if p["titel_tecken"] > 60), n)
    s["produkt_beskrivning_saknas"] = pct(sum(1 for p in prods if p["beskrivning_tecken"] == 0), n)
    s["produkt_beskrivning_for_kort_under_70"] = pct(sum(1 for p in prods if 0 < p["beskrivning_tecken"] < 70), n)
    s["produkt_h1_ej_exakt_ett"] = pct(sum(1 for p in prods if p["h1_antal"] != 1), n)
    s["produkt_canonical_ej_sjalv"] = pct(sum(1 for p in prods if not p["canonical_pekar_pa_sig"]), n)
    s["produkt_noindex"] = sum(1 for p in prods if p["noindex"])
    imgs = sum(p["bilder"] for p in prods)
    s["produkt_bilder_utan_alt_attribut"] = pct(sum(p["bilder_utan_alt"] for p in prods), imgs)
    s["produkt_bilder_tom_alt"] = pct(sum(p["bilder_tom_alt"] for p in prods), imgs)
    s["produkt_ord_median"] = sorted(p["ord_main"] for p in prods)[n // 2] if n else 0
    s["produkt_under_150_ord"] = pct(sum(1 for p in prods if p["ord_main"] < 150), n)
    s["produkt_faq_element"] = pct(sum(1 for p in prods if p["faq_element"] or "FAQPage" in p["jsonld_typer"]), n)
    s["produkt_interna_lankar_median"] = sorted(p["interna_lankar"] for p in prods)[n // 2] if n else 0

    c = len(colls)
    s["kategorisidor_provade"] = c
    s["kategori_ord_median"] = sorted(x["ord_main"] for x in colls)[c // 2] if c else 0
    s["kategori_under_150_ord"] = pct(sum(1 for x in colls if x["ord_main"] < 150), c)
    s["kategori_utan_h1"] = pct(sum(1 for x in colls if x["h1_antal"] == 0), c)
    s["kategori_beskrivning_saknas"] = pct(sum(1 for x in colls if x["beskrivning_tecken"] == 0), c)
    s["kategori_breadcrumb_andel"] = pct(sum(1 for x in colls if "BreadcrumbList" in x["jsonld_typer"]), c)
    s["kategori_itemlist_eller_collectionpage"] = pct(sum(1 for x in colls if {"ItemList", "CollectionPage"} & set(x["jsonld_typer"])), c)
    s["kategori_faq"] = pct(sum(1 for x in colls if x["faq_element"] or "FAQPage" in x["jsonld_typer"]), c)
    s["kategori_produktlankar_median"] = sorted(x["produktlankar"] for x in colls)[c // 2] if c else 0
    s["kategori_canonical_ej_sjalv"] = pct(sum(1 for x in colls if not x["canonical_pekar_pa_sig"]), c)

    s["startsida_typer"] = home.get("jsonld_typer", {})
    s["startsida_organization_sameas"] = home.get("organization_sameas", False)
    s["startsida_title"] = home.get("titel")
    s["blockerade_ai_botar"] = robots["blockerar_alla_ai"]
    s["blockerade_sokmotorer"] = robots["blockerar_google"]
    s.update(extra)
    return s


def flags(s: dict) -> list[tuple[str, str, str]]:
    """(nivå, område, text). Nivå: BRIST, VARNING, OK."""
    f: list[tuple[str, str, str]] = []

    def add(level, area, text):
        f.append((level, area, text))

    add("OK" if not s["blockerade_sokmotorer"] else "BRIST", "Crawlers", "Sökmotorer tillåtna i robots.txt" if not s["blockerade_sokmotorer"] else f"Blockerade: {s['blockerade_sokmotorer']}")
    add("OK" if not s["blockerade_ai_botar"] else "VARNING", "GEO", "AI-botar tillåtna i robots.txt" if not s["blockerade_ai_botar"] else f"AI-botar som är blockerade: {', '.join(s['blockerade_ai_botar'])}")
    add("OK" if s.get("llms_txt") else "VARNING", "GEO", "llms.txt finns" if s.get("llms_txt") else "llms.txt saknas (valfri, osäkert värde)")
    v = verdict(s["produkt_schema_andel"])
    add(v, "Schema", f"Product-schema på {s['produkt_schema_andel']} % av produktsidorna ({s['produkt_schema_dubbletter']} har flera Product-block)")
    for key, label, hint in [("gtin", "GTIN/EAN", "krävs för Google Merchant och AI-sök"), ("brand", "Varumärke", ""),
                             ("fraktinfo", "shippingDetails", "fraktgräns och avgift bör stå här"), ("returpolicy", "hasMerchantReturnPolicy", ""),
                             ("betyg", "aggregateRating", "kräver recensionssystem"), ("lagerstatus", "Lagerstatus", ""), ("mpn", "MPN", "")]:
        val = s["produktfalt_andel_av_sidor_med_schema"].get(key, 0.0)
        lvl = verdict(val)
        if key in ("mpn", "betyg") and lvl == "BRIST":
            lvl = "VARNING"  # valfria fält: bara en varning
        add(lvl, "Schema", f"{label} i {val} % av produktsidor med schema" + (f" ({hint})" if hint and val < 90 else ""))
    add(verdict(s["produkt_breadcrumb_andel"]), "Schema", f"BreadcrumbList på {s['produkt_breadcrumb_andel']} % av produktsidorna")
    add("OK" if s["startsida_organization_sameas"] else "VARNING", "Schema", "Organization med sameAs på startsidan" if s["startsida_organization_sameas"] else "Organization/sameAs saknas på startsidan")
    add("OK" if s["produkt_beskrivning_saknas"] < 5 else "BRIST", "Metadata", f"Metabeskrivning saknas på {s['produkt_beskrivning_saknas']} % av produktsidorna")
    add("OK" if s["produkt_titel_for_lang_over_60"] < 25 else "VARNING", "Metadata", f"{s['produkt_titel_for_lang_over_60']} % av produkttitlarna är längre än 60 tecken")
    add("OK" if s["produkt_h1_ej_exakt_ett"] < 5 else "BRIST", "Struktur", f"{s['produkt_h1_ej_exakt_ett']} % av produktsidorna har inte exakt en H1")
    add("OK" if s["produkt_canonical_ej_sjalv"] < 5 else "BRIST", "Canonical", f"{s['produkt_canonical_ej_sjalv']} % av produktsidorna har canonical som inte pekar på sidan själv")
    add("OK" if s["produkt_noindex"] == 0 else "BRIST", "Indexering", f"{s['produkt_noindex']} produktsidor med noindex i urvalet")
    add("OK" if s["produkt_bilder_utan_alt_attribut"] + s["produkt_bilder_tom_alt"] < 10 else "VARNING", "Bilder",
        f"Bilder utan alt: {s['produkt_bilder_utan_alt_attribut']} % saknar attributet, {s['produkt_bilder_tom_alt']} % har tom alt")
    add("OK" if s["produkt_under_150_ord"] < 25 else "VARNING", "Innehåll", f"{s['produkt_under_150_ord']} % av produktsidorna har under 150 ord (median {s['produkt_ord_median']})")
    add("OK" if s["produkt_faq_element"] > 25 else "VARNING", "GEO", f"FAQ på {s['produkt_faq_element']} % av produktsidorna")
    add("OK" if s["kategori_under_150_ord"] < 25 else "BRIST", "Kategorier", f"{s['kategori_under_150_ord']} % av kategorisidorna har under 150 ord (median {s['kategori_ord_median']})")
    add("OK" if s["kategori_utan_h1"] == 0 else "BRIST", "Kategorier", f"{s['kategori_utan_h1']} % av kategorisidorna saknar H1 i HTML")
    add("OK" if s["kategori_faq"] > 25 else "VARNING", "GEO", f"FAQ på {s['kategori_faq']} % av kategorisidorna")
    add(verdict(s["kategori_breadcrumb_andel"]), "Schema", f"BreadcrumbList på {s['kategori_breadcrumb_andel']} % av kategorisidorna")
    if "hastighet_ms_median" in s:
        add("OK" if s["hastighet_ms_median"] < 800 else "VARNING", "Hastighet", f"Median svarstid för HTML {s['hastighet_ms_median']} ms (Core Web Vitals mäts inte här)")
    for k, label in [("param_canonical_problem", "Parametrar"), ("http_kedja", "Omdirigering")]:
        if k in s:
            add("OK" if not s[k] else "VARNING", label, "Inga problem" if not s[k] else str(s[k]))
    return f


def markdown(base: str, s: dict, fl: list, robots: dict, sm: dict, examples: dict) -> str:
    order = {"BRIST": 0, "VARNING": 1, "OK": 2}
    L = [f"# Onsite-kontroll {base} ({date.today().isoformat()})", "",
         "Bara läsning. Urval: slumpat (fast frö) ur sitemapen. Resultaten gäller urvalet, inte alla sidor.", "",
         "## Sammanfattning", "", "| Nivå | Område | Resultat |", "|---|---|---|"]
    for lvl, area, txt in sorted(fl, key=lambda x: order[x[0]]):
        L.append(f"| {lvl} | {area} | {txt} |")
    L += ["", "## Sitemap", "", f"Index: {sm['index']} (status {sm['status']}).", "",
          f"Produkter {len(sm['produkter'])}, kategorier {len(sm['kategorier'])}, sidor {len(sm['sidor'])}, blogginlägg {len(sm['bloggar'])}.", ""]
    bad = {k: v for k, v in sm["barn"].items() if v["status"] != 200}
    if bad:
        L += ["Sitemaps som inte svarar 200:", *[f"- {k}: {v['status']}" for k, v in bad.items()], ""]
    L += ["## Botar i robots.txt (startsidan)", "", "| Bot | Tillåten på / | Tillåten på /collections/x?sort_by |", "|---|---|---|"]
    for b, r in robots["bots"].items():
        L.append(f"| {b} | {'ja' if r['/'] else 'NEJ'} | {'ja' if r['/collections/x?sort_by=price-ascending'] else 'nej'} |")
    L += ["", f"Agenter nämnda i filen: {', '.join(robots['agenter_i_filen']) or 'inga'}.", ""]
    for title, items in examples.items():
        if items:
            L += [f"## {title}", "", *[f"- {i}" for i in items[:15]], ""]
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base-url", required=True, help="t.ex. https://www.gorillasports.se")
    ap.add_argument("--ut", required=True, help="katalog för rapporten")
    ap.add_argument("--produkter", type=int, default=40)
    ap.add_argument("--kategorier", type=int, default=20)
    ap.add_argument("--paus", type=float, default=0.4, help="sekunder mellan anrop")
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    base = a.base_url.rstrip("/")
    host = urllib.parse.urlparse(base).netloc
    out = Path(a.ut).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    rnd = random.Random(a.seed)
    extra: dict = {}

    print("robots.txt ...", file=sys.stderr)
    rb = fetch(base + "/robots.txt")
    robots = check_robots(rb["text"] if rb["status"] == 200 else "", base)
    ll = fetch(base + "/llms.txt")
    extra["llms_txt"] = ll["status"] == 200 and len(ll["text"].strip()) > 20 and "<html" not in ll["text"][:300].lower()
    time.sleep(a.paus)

    # http -> https och www
    chain_issues = []
    for u in ("http://" + host + "/", "http://" + host.replace("www.", "") + "/" if host.startswith("www.") else "http://www." + host + "/"):
        r = fetch(u)
        hops = len([c for c in r["chain"] if c[0] in (301, 302, 303, 307, 308)])
        final = urllib.parse.urlparse(r["final"]).netloc
        if hops > 1 or r["status"] != 200 or final != host:
            chain_issues.append(f"{u} -> {r['final']} ({hops} omdirigeringar, status {r['status']})")
        time.sleep(a.paus)
    extra["http_kedja"] = chain_issues

    print("sitemap ...", file=sys.stderr)
    sm = read_sitemaps(base, robots["sitemaps"])
    time.sleep(a.paus)

    print("startsida ...", file=sys.stderr)
    h = fetch(base + "/")
    home = analyse_page(h["text"], base + "/") if h["status"] == 200 else {}

    def sample(urls: list[str], n: int) -> list[str]:
        urls = [u for u in urls if urllib.parse.urlparse(u).path.count("/") >= 2]
        return rnd.sample(urls, min(n, len(urls)))

    prods, colls, times = [], [], []
    failed = []
    for kind, urls, bucket in (("produkt", sample(sm["produkter"], a.produkter), prods), ("kategori", sample(sm["kategorier"], a.kategorier), colls)):
        for i, u in enumerate(urls, 1):
            print(f"{kind} {i}/{len(urls)} ...", file=sys.stderr)
            r = fetch(u)
            if r["status"] == 200:
                bucket.append(analyse_page(r["text"], r["final"]))
                times.append(r["ms"])
            else:
                failed.append(f"{u} -> status {r['status']} {r.get('error', '')}")
            time.sleep(a.paus)
    extra["hastighet_ms_median"] = sorted(times)[len(times) // 2] if times else 0

    # parametrar: ger sorterings- och filterlänkar duplicerade eller indexerbara sidor?
    param_problems = []
    if colls:
        cu = colls[0]["url"].split("?")[0]
        for prm in PARAMS[:3]:
            r = fetch(cu + "?" + prm)
            if r["status"] == 200:
                pg = analyse_page(r["text"], r["final"])
                canon = urllib.parse.urldefrag(pg["canonical"])[0].rstrip("/")
                if "?" in canon or (canon != cu.rstrip("/") and "page=" not in prm):
                    param_problems.append(f"{cu}?{prm}: canonical är {pg['canonical'] or 'saknas'}")
                if not pg["noindex"] and canon != cu.rstrip("/") and "page=" not in prm:
                    param_problems.append(f"{cu}?{prm}: indexerbar, canonical pekar inte på grundsidan")
            time.sleep(a.paus)
    extra["param_canonical_problem"] = param_problems

    s = summarize(home, colls, prods, robots, extra)
    fl = flags(s)

    ex = {
        "Produktsidor utan Product-schema": [p["url"] for p in prods if not p["produkter"]],
        "Produktsidor med flera Product-block": [p["url"] for p in prods if len(p["produkter"]) > 1],
        "Produktsidor utan GTIN i schemat": [p["url"] for p in prods if p["produkter"] and not any(f["gtin"] for f in p["produkter"])],
        "Produktsidor med färre än 150 ord": [f"{p['url']} ({p['ord_main']} ord)" for p in prods if p["ord_main"] < 150],
        "Kategorisidor med färre än 150 ord": [f"{c['url']} ({c['ord_main']} ord)" for c in colls if c["ord_main"] < 150],
        "Kategorisidor utan H1": [c["url"] for c in colls if c["h1_antal"] == 0],
        "Sidor som inte svarade 200": failed,
        "Parametrar": param_problems,
    }
    (out / "onsite.json").write_text(json.dumps({"base": base, "datum": date.today().isoformat(), "sammanfattning": s,
                                                 "robots": robots, "sitemap": {k: (v if k in ("index", "status", "barn") else len(v)) for k, v in sm.items()},
                                                 "produkter": prods, "kategorier": colls, "startsida": home}, ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "onsite.md").write_text(markdown(base, s, fl, robots, sm, ex), encoding="utf-8")
    brist = sum(1 for x in fl if x[0] == "BRIST")
    varn = sum(1 for x in fl if x[0] == "VARNING")
    print(f"SAMMANFATTNING {base}: {brist} brister, {varn} varningar, {len(prods)} produktsidor, {len(colls)} kategorisidor. Rapport: {out}/onsite.md")
    print((out / "onsite.md").read_text(encoding="utf-8").split("## Sitemap")[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
