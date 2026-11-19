import datetime as dt, re, unittest
import gsc_baslinje as G


class T(unittest.TestCase):
    def test_veckor(self):
        v = G.veckor(dt.date(2026, 11, 16), 3)
        self.assertEqual(v[-1], (dt.date(2026, 11, 10), dt.date(2026, 11, 16)))
        self.assertEqual(v[0][0], dt.date(2026, 10, 27))
        self.assertTrue(all((e - s).days == 6 for s, e in v))
        self.assertEqual(v[1][0], v[0][1] + dt.timedelta(days=1))

    def test_regex(self):
        r = re.compile(G.regex_for(["hoodie-man", "kepsar"]).replace("\\-", "-"))
        self.assertTrue(r.search("https://x.com/collections/hoodie-man"))
        self.assertTrue(r.search("https://x.com/collections/kepsar?page=2"))
        self.assertFalse(r.search("https://x.com/collections/hoodie-manx"))


if __name__ == "__main__":
    unittest.main()
