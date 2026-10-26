#!/usr/bin/env python3
"""Hämtar vikt per SKU (variant) ur Shopify och skriver en CSV: sku, vikt_kg. Bara läsning.

  export SHOPIFY_SHOP_DOMAIN=gs-nordic-production.myshopify.com
  export SHOPIFY_ACCESS_TOKEN="$(gcloud secrets versions access latest --secret=shopify-access-token)"   # läs-token räcker (read_products, read_inventory)
  PYTHONPATH=src python3 scripts/hamta_vikter.py --ut ~/vikter_gorilla.csv

Läs in resultatet i BigQuery (se sql/analys/net_profit_ordrar.sql). Vikt saknas ofta för tilläggsprodukter; antalet utan vikt skrivs ut."""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

Q = """
query($cursor: String) {
  productVariants(first: 250, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes { id sku inventoryItem { measurement { weight { value unit } } } }
  }
}
"""
TO_KG = {"KILOGRAMS": 1.0, "GRAMS": 0.001, "POUNDS": 0.45359237, "OUNCES": 0.028349523}


def kg(weight: dict | None) -> float | None:
    if not weight:
        return None
    f = TO_KG.get(weight.get("unit"))
    return None if f is None else round(float(weight["value"]) * f, 4)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ut", default="vikter_gorilla.csv")
    args = ap.parse_args()
    from shopify_sync.config import ShopifyConfig
    from shopify_sync.shopify_client import ShopifyClient

    client = ShopifyClient(ShopifyConfig.from_env())
    rows, cursor = [], None
    while True:
        d = client.graphql(Q, {"cursor": cursor})["productVariants"]
        for n in d["nodes"]:
            w = kg(((n.get("inventoryItem") or {}).get("measurement") or {}).get("weight"))
            rows.append((str(n.get("sku") or "").strip(), w))
        if not d["pageInfo"]["hasNextPage"]:
            break
        cursor = d["pageInfo"]["endCursor"]
    with open(args.ut, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["sku", "vikt_kg"])
        for sku, kgv in rows:
            if sku:
                w.writerow([sku, "" if kgv is None else kgv])
    utan = sum(1 for s, k in rows if s and (k is None or k == 0))
    print(f"{len(rows)} varianter, {utan} utan vikt (eller vikt 0). Skrev {args.ut}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
