#!/usr/bin/env python3
"""Läser offentliga sidor (GET) och rapporterar title, meta, canonical, hreflang, h1, JSON-LD-typer, alt-bilder. Inget skrivs.
Användning: python3 -I sidkontroll_offentlig.py <utfil.json> <url> [<url> ...]"""
import json, re, sys, time, urllib.request, html
UA = "Mozilla/5.0 (compatible; produktdata-genomlysning/1.0; las-endast)"
def hamta(u):
    try:
        with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=40) as r:
            return r.status, r.geturl(), r.read().decode("utf-8", "replace")
    except Exception as e:
        return 0, u, str(e)
def kolla(u):
    st, slut, h = hamta(u)
    g = lambda p: (re.search(p, h, re.S | re.I) or [None, None])[1]
    ld = []
    for m in re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', h, re.S):
        try:
            j = json.loads(m); ld += [x.get("@type") for x in (j if isinstance(j, list) else j.get("@graph", [j]))]
        except Exception: ld.append("OGILTIG_JSON")
    imgs = re.findall(r"<img\b[^>]*>", h)
    return {"url": u, "status": st, "slutadress": slut, "bytes": len(h),
        "html_lang": g(r'<html[^>]*\blang="([^"]*)"'), "title": html.unescape(g(r"<title>(.*?)</title>") or "").strip(),
        "meta_description": html.unescape(g(r'<meta\s+name="description"\s+content="(.*?)"') or ""),
        "canonical": g(r'<link\s+rel="canonical"\s+href="(.*?)"'), "robots_meta": g(r'<meta\s+name="robots"\s+content="(.*?)"'),
        "hreflang": re.findall(r'<link[^>]*rel="alternate"[^>]*hreflang="([^"]*)"[^>]*href="([^"]*)"', h) or [(a, b) for b, a in re.findall(r'<link[^>]*rel="alternate"[^>]*href="([^"]*)"[^>]*hreflang="([^"]*)"', h)],
        "og": {k: html.unescape(v) for k, v in re.findall(r'<meta\s+property="og:(title|description|image|type|locale)"\s+content="(.*?)"', h)},
        "h1": [re.sub(r"<[^>]+>|\s+", " ", x).strip() for x in re.findall(r"<h1[^>]*>(.*?)</h1>", h, re.S)],
        "h2_antal": len(re.findall(r"<h2", h)), "jsonld_typer": ld,
        "bilder": len(imgs), "bilder_utan_alt": sum(1 for i in imgs if not re.search(r'\balt="[^"]+"', i)),
        "gtm_ga_tecken": {"gtag": "googletagmanager.com/gtag" in h, "gtm": "googletagmanager.com/gtm" in h, "ga4_id": re.findall(r"G-[A-Z0-9]{6,}", h)[:3], "gads": re.findall(r"AW-\d+", h)[:3], "fb_pixel": "fbq(" in h or "connect.facebook.net" in h, "klaviyo": "klaviyo" in h.lower()},
        "ord_i_synlig_text": len(re.sub(r"\s+", " ", re.sub(r"<script.*?</script>|<style.*?</style>|<[^>]+>", " ", h, flags=re.S)).split())}
res = []
for u in sys.argv[2:]:
    res.append(kolla(u)); time.sleep(1)
json.dump(res, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
for r in res: print(r["url"], r["status"], "|", r["title"][:70], "|", (r["meta_description"] or "-")[:50], "| h1", len(r["h1"]), "| ld", r["jsonld_typer"], "| hreflang", len(r["hreflang"]), "| canon", r["canonical"])
