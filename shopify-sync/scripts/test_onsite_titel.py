import unittest
import onsite_kontroll as O

HTML = ('<html><head><title>\n   Hantlar – Olika vikter\n  </title></head><body><svg><title>Apple Pay</title></svg><svg><title>Visa</title></svg>'
        '<h1>Hantlar</h1></body></html>')


class T(unittest.TestCase):
    def test_bara_sidans_egen_titel_raknas(self):
        a = O.analyse_page(HTML, "https://x.se/collections/hantlar")
        self.assertEqual(a["titel"], "Hantlar – Olika vikter")
        self.assertEqual(a["titel_tecken"], len("Hantlar – Olika vikter"))

    def test_saknad_titel_ger_tom(self):
        a = O.analyse_page("<html><head></head><body><svg><title>Ikon</title></svg></body></html>", "https://x.se/")
        self.assertEqual(a["titel"], "")


if __name__ == "__main__":
    unittest.main()
