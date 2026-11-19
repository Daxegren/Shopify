import unittest
import gsc_indexering as G


class T(unittest.TestCase):
    def test_rad(self):
        svar = {"inspectionResult": {"indexStatusResult": {"verdict": "PASS", "coverageState": "Submitted and indexed", "lastCrawlTime": "2026-11-16T10:00:00Z",
                "googleCanonical": "https://x/a", "userCanonical": "https://x/a", "indexingState": "INDEXING_ALLOWED"}}}
        r = G.rad("https://x/a", "andrad", svar)
        self.assertEqual((r["verdict"], r["lastCrawlTime"], r["canonical_samma"]), ("PASS", "2026-11-16", "ja"))
        svar["inspectionResult"]["indexStatusResult"]["googleCanonical"] = "https://x/b"
        self.assertEqual(G.rad("u", "k", svar)["canonical_samma"], "nej")
        self.assertEqual(G.rad("u", "k", {})["canonical_samma"], "")

    def test_urls(self):
        u = G.urls()
        self.assertTrue(all(x.startswith("https://workoutbrands.com/collections/") for x, _ in u))
        self.assertEqual(len(u), len(G.ANDRADE) + 2 + len(G.KONTROLL))


if __name__ == "__main__":
    unittest.main()
