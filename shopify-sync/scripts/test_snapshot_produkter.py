import json, os, tempfile, unittest
import snapshot_produkter as S


class Fake:
    def graphql(self, q, v=None):
        return {"nodes": [{"id": i, "status": "ACTIVE", "tags": ["b", "a"], "handle": "h", "variants": {"nodes": [{"id": "v" + i, "price": "10.00", "compareAtPrice": None}]}} for i in v["ids"]]}


class T(unittest.TestCase):
    def test_ids_unika_och_ta(self):
        f = os.path.join(tempfile.mkdtemp(), "f.jsonl")
        open(f, "w").write("\n".join(json.dumps({"media_id": f"m{i}", "produkt": f"p{i % 2}"}) for i in range(5)))
        self.assertEqual(S.produkt_ids(f), ["p0", "p1"])
        snap = S.ta(Fake(), ["p0", "p1"])
        self.assertEqual(snap["p0"]["tags"], ["a", "b"])

    def test_jamfor_hittar_andring(self):
        a = S.ta(Fake(), ["p0", "p1"]); b = json.loads(json.dumps(a))
        self.assertEqual(S.jamfor(a, b), [])
        b["p0"]["varianter"]["vp0"][0] = "9.00"; b["p1"]["tags"].append("x"); del b["p1"]
        self.assertEqual(sorted(S.jamfor(a, b)), [("p0", "varianter"), ("p1", "produkten saknas efteråt")])


if __name__ == "__main__":
    unittest.main()
