#!/usr/bin/env python3
"""Läs-bara: hämtar offentliga sidor och sparar titel, meta, canonical, hreflang, H1, JSON-LD-typer, alt-täckning.
Användning: offentlig_sidlasning.py <utfil.json> <url> [<url> ...]  (eller urls på stdin med '-')"""
import json, re, sys, time, urllib.request, html as H
def hamta(u, sprak=None):
    for f in range(4):
        try:
            rq = urllib.request.Request(u, headers={"User-Agent": "produktdata-inventering/1.0", **({"Accept-Language": sprak} if sprak else {})})
            with urllib.request.urlopen(rq, timeout=60) as r: return r.status, r.geturl(), r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 404: return 404, u, ""
            time.sleep(2 ** f)
        except Exception: time.sleep(2 ** f)
    return 0, u, ""
def analys(u):
    s, slut, h = hamta(u)
    g = lambda p, fl=re.S | re.I: (re.search(p, h, fl) or [None, None])[1]
    ld = []
    for b in re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', h, re.S | re.I):
        try:
            d = json.loads(b); d = d if isinstance(d, list) else d.get("@graph", [d])
            ld += [x.get("@type") for x in d if isinstance(x, dict)]
        except Exception: ld.append("OGILTIG")
    imgs = re.findall(r'<img\b[^>]*>', h, re.I)
    return {"url": u, "status": s, "slutadress": slut, "bytes": len(h),
        "title": H.unescape(g(r'<title[^>]*>(.*?)</title>') or "").strip(),
        "meta": H.unescape(g(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']') or g(r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']description["\']') or "").strip(),
        "canonical": re.findall(r'<link[^>]+rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', h, re.I),
        "hreflang": re.findall(r'<link[^>]+hreflang=["\']([^"\']+)["\'][^>]*href=["\']([^"\']+)', h, re.I) or [(a, b) for b, a in re.findall(r'<link[^>]+href=["\']([^"\']+)["\'][^>]*hreflang=["\']([^"\']+)', h, re.I)],
        "robots": g(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']'),
        "h1": len(re.findall(r'<h1\b', h, re.I)), "h2": len(re.findall(r'<h2\b', h, re.I)),
        "jsonld": ld, "img": len(imgs), "img_utan_alt": sum(1 for i in imgs if not re.search(r'alt=["\'][^"\']+["\']', i, re.I)),
        "og_title": g(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\'](.*?)["\']'), "lang": g(r'<html[^>]+lang=["\']([^"\']+)')}
if __name__ == "__main__":
    ut, urls = sys.argv[1], sys.argv[2:]
    if urls == ["-"]: urls = [l.strip() for l in sys.stdin if l.strip()]
    res = []
    for u in urls: res.append(analys(u)); time.sleep(0.4)
    json.dump(res, open(ut, "w"), ensure_ascii=False, indent=1); print(len(res), "sidor ->", ut)
