import os
os.environ["no_proxy"] = "*"; os.environ["NO_PROXY"] = "*"
for k in ("http_proxy", "HTTP_PROXY", "https_proxy", "HTTPS_PROXY"):
    os.environ.pop(k, None)
import http.server, threading, unittest
import sajtskanning as S

GOD = '<html lang="sv"><head><title>Bra sida om cyklar och reparation</title><meta name="description" content="En bra beskrivning."><link rel="canonical" href="{u}"><meta property="og:image" content="x.jpg"><script type="application/ld+json">{{"@type":"WebPage"}}</script></head><body><main><h1>Bra</h1><p>{ord}</p><img src="a.jpg" alt="en bild"></main></body></html>'
SIDOR = {
    "/": GOD.format(u="{B}/", ord="ord " * 200),
    "/bra": GOD.format(u="{B}/bra", ord="ord " * 200),
    "/dubbel": GOD.format(u="{B}/dubbel", ord="ord " * 200).replace("Bra sida om cyklar och reparation", "Dålig"),
    "/dubbel2": GOD.format(u="{B}/dubbel2", ord="ord " * 200).replace("Bra sida om cyklar och reparation", "Dålig"),
    "/dalig": '<html><head></head><body><h1>A</h1><h1>B</h1><p>kort</p><img src="x.jpg"></body></html>',
}


class H(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        b = f"http://127.0.0.1:{self.server.server_port}"
        if self.path == "/robots.txt":
            body, ct, code = f"User-agent: *\nDisallow: /privat\nSitemap: {b}/sitemap.xml\n", "text/plain", 200
        elif self.path == "/sitemap.xml":
            urls = list(SIDOR) + ["/saknas", "/privat"]
            body, ct, code = "<urlset>" + "".join(f"<url><loc>{b}{u}</loc></url>" for u in urls) + "</urlset>", "application/xml", 200
        elif self.path in SIDOR:
            body, ct, code = SIDOR[self.path].replace("{B}", b), "text/html; charset=utf-8", 200
        else:
            body, ct, code = "nej", "text/plain", 404
        self.send_response(code); self.send_header("Content-Type", ct); self.end_headers(); self.wfile.write(body.encode())


class T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = http.server.HTTPServer(("127.0.0.1", 0), H)
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
        cls.bas = f"http://127.0.0.1:{cls.srv.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()

    def test_hittar_fynd(self):
        fl, sidor, kallor, anm = S.skanna(self.bas, 50, 0, logg=lambda *a: None)
        d = {f["id"]: f for f in fl}
        self.assertEqual(d["icke_200"]["antal"], 1)               # /saknas
        self.assertIn("inte_https", d)                              # testserver är http
        self.assertEqual(d["titel_saknas"]["antal"], 1)             # /dalig
        self.assertEqual(d["h1"]["antal"], 1)
        self.assertEqual(d["titel_dubbletter"]["antal"], 4)  # "/" och "/bra" delar titel, "/dubbel" och "/dubbel2" delar titel
        self.assertEqual(d["tunt"]["antal"], 1)
        self.assertEqual(d["alt"]["antal"], 1)
        self.assertNotIn("/privat", " ".join(s["url"] for s in sidor))  # robots respekteras
        self.assertTrue(any("robots.txt" in a for a in anm))

    def test_urval_bestammer_storlek_och_tar_med_startsidan(self):
        u = S.urval([f"http://x/{i}" for i in range(100)], "http://x", 10)
        self.assertEqual(len(u), 10); self.assertEqual(u[0], "http://x/")


if __name__ == "__main__":
    unittest.main()
