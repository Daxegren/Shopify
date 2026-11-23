#!/usr/bin/env python3
"""Läsande ögonblicksbild av produkternas status, taggar och variantpriser, och jämförelse före och efter en skrivning.

Används vid alt-text på BEST OF SPORTS för att visa att pris, jämförpris, taggar och status är oförändrade på de produkter
vars bilder fick alt-text. Bara läsning.
  python3 snapshot_produkter.py --fran ~/bos_alt/fore_alt.jsonl --ut ~/bos_alt/snap_fore.json
  python3 snapshot_produkter.py --jamfor ~/bos_alt/snap_fore.json ~/bos_alt/snap_efter.json
"""
import argparse, json, os, sys
from kon_fyll_target_gender import Klient, Stopp

Q = '''query($ids:[ID!]!){nodes(ids:$ids){... on Product{id status tags handle variants(first:100){nodes{id price compareAtPrice}}}}}'''


def produkt_ids(fore_fil):
    ut = []
    for rad in open(fore_fil, encoding="utf-8"):
        if rad.strip():
            p = json.loads(rad)["produkt"]
            if p not in ut:
                ut.append(p)
    return ut


def ta(k, ids):
    snap = {}
    for n in range(0, len(ids), 50):
        for nod in k.graphql(Q, {"ids": ids[n:n + 50]})["nodes"]:
            if nod:
                snap[nod["id"]] = {"status": nod["status"], "tags": sorted(nod["tags"]), "handle": nod["handle"],
                                   "varianter": {v["id"]: [v["price"], v["compareAtPrice"]] for v in nod["variants"]["nodes"]}}
    return snap


def jamfor(fore, efter):
    """Lista med skillnader (tom lista = oförändrat)."""
    skillnader = []
    for pid, f in fore.items():
        e = efter.get(pid)
        if e is None:
            skillnader.append((pid, "produkten saknas efteråt")); continue
        for nyckel in ("status", "tags", "handle", "varianter"):
            if f[nyckel] != e[nyckel]:
                skillnader.append((pid, nyckel))
    return skillnader


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fran", help="före-fil (jsonl) från wb_alt.py, ger produkt-id:n")
    ap.add_argument("--ut", help="var ögonblicksbilden sparas")
    ap.add_argument("--jamfor", nargs=2, metavar=("FORE", "EFTER"))
    a = ap.parse_args()
    try:
        if a.jamfor:
            fore, efter = (json.load(open(os.path.expanduser(x), encoding="utf-8")) for x in a.jamfor)
            sk = jamfor(fore, efter)
            print(f"{len(fore)} produkter jämförda, {len(sk)} skillnader")
            for pid, vad in sk[:20]:
                print("  ", pid, vad)
            return
        if not (a.fran and a.ut):
            ap.error("--fran och --ut krävs (eller --jamfor)")
        snap = ta(Klient(), produkt_ids(os.path.expanduser(a.fran)))
        json.dump(snap, open(os.path.expanduser(a.ut), "w", encoding="utf-8"))
        print(f"sparade {len(snap)} produkter i {a.ut}")
    except Stopp as e:
        sys.exit(f"STOPP: {e}")


if __name__ == "__main__":
    main()
