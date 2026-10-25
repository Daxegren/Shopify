#!/usr/bin/env python3
"""Rättar Gorillas omdirigeringar mot vår granskade fil (rapporter/redirects_granskade.csv).

Torrkörning är standard: läser butikens omdirigeringar och visar före och efter, ändrar inget.

  export SHOPIFY_SHOP_DOMAIN=gs-nordic-production.myshopify.com
  read -rs -p "Token: " SHOPIFY_ACCESS_TOKEN && export SHOPIFY_ACCESS_TOKEN && echo   # eller hämta från Secret Manager utan att skriva ut den
  python3 scripts/redirects_gorilla_apply.py --granskade ../rapporter/redirects_granskade.csv

Skriv aldrig token i chatten. Med --apply skrivs ändringarna, och först sparas en återställningsfil med
nuvarande mål för varje omdirigering som ändras. Kräver att token har skrivrätt för omdirigeringar
(write_online_store_navigation); saknas den stoppar Shopify skrivningen och inget ändras.

Åtgärder: SKAPA (finns ingen omdirigering för källan), ÄNDRA (finns med annat mål), OFÖRÄNDRAD (redan rätt).
Målen kontrolleras: /products/<handle> och /collections/<handle> måste finnas i butiken (produkter måste vara
ACTIVE). Mål som inte finns hoppas över och rapporteras, så att vi inte skapar nya felaktiga omdirigeringar.
Artikelmål (/blogs/...) kan inte kontrolleras här och markeras 'ej kontrollerat'."""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from datetime import date
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

REDIRECTS_Q = """
query($cursor: String) {
  urlRedirects(first: 250, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes { id path target }
  }
}
"""
COLLECTION_Q = "query($h: String!) { collectionByIdentifier(identifier: {handle: $h}) { id } }"
PRODUCT_Q = "query($h: String!) { productByIdentifier(identifier: {handle: $h}) { id status } }"
UPDATE_M = """
mutation($id: ID!, $r: UrlRedirectInput!) {
  urlRedirectUpdate(id: $id, urlRedirect: $r) { urlRedirect { id path target } userErrors { field message } }
}"""
CREATE_M = """
mutation($r: UrlRedirectInput!) {
  urlRedirectCreate(urlRedirect: $r) { urlRedirect { id path target } userErrors { field message } }
}"""


def norm(path: str) -> str:
    return (unquote(path).strip().rstrip("/") or "/").lower()


def load_reviewed(csv_path: str) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    with open(csv_path, encoding="utf-8") as f:
        for row in csv.reader(f):
            if len(row) >= 2 and row[0].startswith("/") and row[1].startswith("/"):
                rows.append((row[0].strip(), row[1].strip()))
    return rows


def plan(reviewed: list[tuple[str, str]], existing: list[dict]) -> list[dict]:
    by_path = {norm(r["path"]): r for r in existing}
    out = []
    for src, target in reviewed:
        cur = by_path.get(norm(src))
        if cur is None:
            out.append({"atgard": "SKAPA", "path": src, "nu": "", "nytt": target, "id": None})
        elif norm(cur["target"]) == norm(target):
            out.append({"atgard": "OFÖRÄNDRAD", "path": cur["path"], "nu": cur["target"], "nytt": target, "id": cur["id"]})
        else:
            out.append({"atgard": "ÄNDRA", "path": cur["path"], "nu": cur["target"], "nytt": target, "id": cur["id"]})
    return out


def target_status(client, target: str) -> str:
    """'ok', 'saknas', 'inte aktiv' eller 'ej kontrollerat'."""
    parts = [p for p in target.split("?")[0].split("/") if p]
    if len(parts) == 2 and parts[0] == "collections":
        return "ok" if client.graphql(COLLECTION_Q, {"h": parts[1]})["collectionByIdentifier"] else "saknas"
    if len(parts) == 2 and parts[0] == "products":
        p = client.graphql(PRODUCT_Q, {"h": parts[1]})["productByIdentifier"]
        if not p:
            return "saknas"
        return "ok" if p.get("status") == "ACTIVE" else "inte aktiv"
    return "ej kontrollerat"


def fetch_redirects(client) -> list[dict]:
    out, cursor = [], None
    while True:
        d = client.graphql(REDIRECTS_Q, {"cursor": cursor})["urlRedirects"]
        out.extend(d["nodes"])
        if not d["pageInfo"]["hasNextPage"]:
            return out
        cursor = d["pageInfo"]["endCursor"]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--granskade", required=True)
    ap.add_argument("--apply", action="store_true", help="Skriv ändringarna (standard är torrkörning)")
    ap.add_argument("--ut", default=".", help="Katalog för rapport och återställningsfil")
    args = ap.parse_args()

    from shopify_sync.config import ShopifyConfig
    from shopify_sync.shopify_client import ShopifyClient

    client = ShopifyClient(ShopifyConfig.from_env())
    reviewed = load_reviewed(args.granskade)
    existing = fetch_redirects(client)
    print(f"Granskade omdirigeringar: {len(reviewed)}. Omdirigeringar i butiken: {len(existing)}.")
    rows = plan(reviewed, existing)

    cache: dict[str, str] = {}
    for r in rows:
        if r["atgard"] == "OFÖRÄNDRAD":
            r["mal"] = "-"
            continue
        r["mal"] = cache.setdefault(r["nytt"], target_status(client, r["nytt"]))

    todo = [r for r in rows if r["atgard"] != "OFÖRÄNDRAD" and r["mal"] in ("ok", "ej kontrollerat")]
    blocked = [r for r in rows if r["atgard"] != "OFÖRÄNDRAD" and r["mal"] not in ("ok", "ej kontrollerat")]

    out = Path(args.ut)
    out.mkdir(parents=True, exist_ok=True)
    stamp = date.today().isoformat()
    report = out / f"redirects-gorilla-{'apply' if args.apply else 'torrkorning'}-{stamp}.csv"
    with report.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["åtgärd", "källa", "nuvarande mål", "nytt mål", "kontroll av mål"])
        for r in rows:
            w.writerow([r["atgard"], r["path"], r["nu"], r["nytt"], r["mal"]])

    for r in rows:
        print(f"{r['atgard']:<11} {r['path']}\n            nu:   {r['nu'] or '(ingen)'}\n            nytt: {r['nytt']}   [mål: {r['mal']}]")
    print(f"\nSammanfattning: ändra {sum(r['atgard']=='ÄNDRA' for r in todo)}, skapa {sum(r['atgard']=='SKAPA' for r in todo)}, "
          f"oförändrade {sum(r['atgard']=='OFÖRÄNDRAD' for r in rows)}, stoppade (målet saknas eller är inte aktivt) {len(blocked)}.")
    for r in blocked:
        print(f"  STOPPAD {r['path']} -> {r['nytt']} ({r['mal']})")
    print(f"Rapport: {report}")

    if not args.apply:
        print("\nTorrkörning: inget ändrat. Kör med --apply när du har granskat rapporten.")
        return 0

    snap = out / f"redirects-gorilla-aterstall-{stamp}.json"
    snap.write_text(json.dumps([{"id": r["id"], "path": r["path"], "target_innan": r["nu"], "atgard": r["atgard"]} for r in todo],
                               ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Återställningsfil sparad: {snap}")
    fel = 0
    for r in todo:
        if r["atgard"] == "ÄNDRA":
            res = client.graphql(UPDATE_M, {"id": r["id"], "r": {"target": r["nytt"]}})["urlRedirectUpdate"]
        else:
            res = client.graphql(CREATE_M, {"r": {"path": r["path"], "target": r["nytt"]}})["urlRedirectCreate"]
        if res["userErrors"]:
            fel += 1
            print(f"FEL {r['path']}: {res['userErrors']}")
        time.sleep(0.3)
    print(f"Klart. {len(todo) - fel} lyckades, {fel} fel.")
    return 1 if fel else 0


if __name__ == "__main__":
    raise SystemExit(main())
