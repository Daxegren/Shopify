"""Lokal testsajt som efterliknar en Shopify-butik med kända fel."""

from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

LOREM_SV = ("Det här är en text om konst och om våra konstnärer som har en lång historia. Vi har ställt ut i "
            "många år och det är för oss en glädje att visa verk som inte syns någon annanstans. ") * 6
LOREM_EN = ("This is a text about art and the artists that we represent in our gallery. We have been showing work "
            "for many years and it is our pleasure to present pieces that you will not find anywhere else. ") * 6


def page(title, h1s=(), body="", lang="en", head="", canonical=None):
    h = "".join(f"<h1>{x}</h1>" for x in h1s)
    canon = f"<link rel='canonical' href='{canonical}'>" if canonical else ""
    return (f"<!doctype html><html lang='{lang}'><head><title>{title}</title>"
            f"<meta name='description' content='{title} beskrivning'>{canon}{head}</head>"
            f"<body><header><nav><a href='/pages/about'>Om</a></nav></header><main>{h}{body}</main>"
            f"<footer>Sidfot</footer></body></html>")


def jsonld(obj):
    return f"<script type='application/ld+json'>{json.dumps(obj)}</script>"


def build_routes(base: str) -> dict:
    good_product = {"@context": "https://schema.org", "@type": "Product", "name": "Tavla",
                    "image": [base + "/cdn/tavla.jpg"], "offers": {"@type": "Offer", "price": "100"}, "brand": "Mankovsky"}
    bad_product = {"@context": "https://schema.org", "@type": "Product", "name": "Trasig",
                   "image": "//cdn/{{ product.featured_image }}", "offers": {"@type": "Offer", "price": "50"}}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": []}
    hreflang = "".join(f"<link rel='alternate' hreflang='{l}' href='{base}/{l}/products/good'>" for l in
                       ["de", "fr", "es", "it", "nl", "pl", "fi", "da", "no", "pt", "cs", "ja", "ko"])
    hreflang += f"<link rel='alternate' hreflang='en' href='{base}/products/good'>"
    big_script = "<script>window.trustBadge=" + json.dumps("x" * 150_000) + ";</script>"
    r = {
        "/robots.txt": (200, {"Content-Type": "text/plain"}, "User-agent: *\nSitemap: /sitemap.xml"),
        "/sitemap.xml": (200, {"Content-Type": "application/xml"},
                         f"<?xml version='1.0'?><sitemapindex xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>"
                         f"<sitemap><loc>{base}/sitemap_products_1.xml</loc></sitemap>"
                         f"<sitemap><loc>{base}/sitemap_pages_1.xml</loc></sitemap></sitemapindex>"),
        "/sitemap_products_1.xml": (200, {"Content-Type": "application/xml"},
                                    "<?xml version='1.0'?><urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>" +
                                    "".join(f"<url><loc>{base}{p}</loc></url>" for p in
                                            ["/products/good", "/products/bad-schema", "/collections/artists",
                                             "/collections/artist-gone", "/sv/products/good"]) + "</urlset>"),
        "/sitemap_pages_1.xml": (200, {"Content-Type": "application/xml"},
                                 "<?xml version='1.0'?><urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>" +
                                 "".join(f"<url><loc>{base}{p}</loc></url>" for p in
                                         ["/pages/about", "/pages/about-us", "/pages/test-page", "/sv/pages/om-oss", "/old", "/chain-ok", "/bad-target"]) + "</urlset>"),
        "/": (200, {}, page("Mankovsky Gallery – konst", ["Välkommen"] * 6, LOREM_SV + "<a href='/products/good'>x</a><a href='/collections/gone-link'>y</a>",
                            lang="sv", canonical=base + "/", head=jsonld({"@type": "Organization", "name": "Mankovsky"}) + big_script)),
        "/products/good": (200, {}, page("Tavla av Mankovsky | Galleri", ["Tavla"], LOREM_SV + "<img src='/a.jpg' alt='Tavla'><img src='/b.jpg'>",
                                         lang="sv", canonical=base + "/products/good", head=jsonld(good_product) + jsonld(breadcrumb) + hreflang)),
        "/products/bad-schema": (200, {}, page("Trasig produkt från Mankosvky", [], LOREM_SV, lang="sv",
                                                canonical=base + "/products/bad-schema", head=jsonld(bad_product))),
        "/collections/artists": (200, {}, page("Konstnärer", [], LOREM_SV, lang="sv", canonical=base + "/collections/artists")),
        "/pages/about": (200, {}, page("Om oss", ["Om oss"], LOREM_SV, lang="sv", canonical=base + "/pages/about")),
        "/pages/about-us": (200, {}, page("Om oss", ["Om oss"], LOREM_SV, lang="sv", canonical=base + "/pages/about-us")),
        "/pages/test-page": (200, {}, page("Test page", ["Test"], "kort", lang="sv", canonical=base + "/pages/test-page")),
        "/sv/pages/om-oss": (200, {}, page("Om oss på svenska", ["Om oss"], LOREM_EN, lang="sv", canonical=base + "/sv/pages/om-oss")),
        "/sv/products/good": (302, {"Location": "/en-ca/products/good"}, ""),
        "/en-ca/products/good": (200, {}, page("Painting", ["Painting"], LOREM_EN, lang="en-ca", canonical=base + "/en-ca/products/good")),
        "/old": (301, {"Location": "/older"}, ""),
        "/older": (301, {"Location": "/missing"}, ""),
        "/chain-ok": (301, {"Location": "/chain-ok-2"}, ""),
        "/chain-ok-2": (301, {"Location": "/pages/about"}, ""),
        "/bad-target": (301, {"Location": "//collections/wall-ball"}, ""),
        "/redir-a": (301, {"Location": "/redir-b"}, ""),
        "/redir-b": (301, {"Location": "/redir-a"}, ""),
    }
    return r


class Handler(BaseHTTPRequestHandler):
    routes: dict = {}

    def do_GET(self):  # noqa: N802
        path = self.path.split("?")[0]
        if path == "/" and "sv" in (self.headers.get("Accept-Language") or "") and "geo" in self.server.flags:
            status, headers, body = 302, {"Location": "/en-ca"}, ""
        else:
            status, headers, body = self.routes.get(path, (404, {}, page("404 Not Found", ["Sidan hittades inte"])))
        self.send_response(status)
        for k, v in headers.items():
            self.send_header(k, v)
        if "Content-Type" not in headers:
            self.send_header("Content-Type", "text/html; charset=utf-8")
        data = body.encode()
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *a):
        pass


def start(flags=("geo",)):
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    base = f"http://127.0.0.1:{server.server_address[1]}"
    server.flags = set(flags)
    Handler.routes = build_routes(base)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, base
