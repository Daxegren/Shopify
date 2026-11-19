#!/usr/bin/env python3
"""Samlad skanningsrapport: kombinerar tillgängliga källor till en rapport med fynd per paket (läsande).

Källor (alla valfria, minst en krävs):
  --shopify-export KATALOG   produkter.csv, kollektioner.csv (+ oversattning_sammanfattning.csv) från wb_export.py
  --onsite KATALOG           onsite.json från onsite_kontroll.py (Shopify-butikens publika sidor)
  --url ADRESS               plattformsoberoende skanning av publika sidor (sajtskanning.py körs, tar några minuter)
  python3 skanning_rapport.py --namn "Butik X" --shopify-export ~/wb_export --url https://exempel.se --ut ~/rapport-x
Skriver rapport.md och fynd.csv i --ut.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

from skanning_paket import fynd, rapport_md, till_csv

OMRADE_TILL_PAKET = {"Crawlers": "P3", "GEO": "P3", "Schema": "P3", "Canonical": "P3", "Indexering": "P3", "Hastighet": "P3", "Parametrar": "P3",
                     "Omdirigering": "P3", "Metadata": "P4", "Struktur": "P4", "Bilder": "P4", "Innehåll": "P4", "Kategorier": "P4"}


def fynd_ur_onsite(katalog: str):
    """Omvandlar flaggorna i onsite.json (BRIST/VARNING) till fynd. Returnerar (fynd, kalla)."""
    from onsite_kontroll import flags
    d = json.loads((Path(katalog).expanduser() / "onsite.json").read_text(encoding="utf-8"))
    ut = []
    for niva, omrade, text in flags(d["sammanfattning"]):
        if niva in ("BRIST", "VARNING"):
            ut.append(fynd(f"onsite_{omrade}_{len(ut)}", omrade, text, 1, 0, niva, OMRADE_TILL_PAKET.get(omrade, "P3"), "Se onsite.md för detaljer", "per mall"))
    return ut, f"onsite.json ({d['base']})"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--namn", required=True)
    ap.add_argument("--ut", required=True)
    ap.add_argument("--shopify-export")
    ap.add_argument("--onsite")
    ap.add_argument("--url")
    ap.add_argument("--max-sidor", type=int, default=150)
    a = ap.parse_args()
    if not (a.shopify_export or a.onsite or a.url):
        sys.exit("Ange minst en källa: --shopify-export, --onsite eller --url")
    fl, kallor, anm = [], [], []
    if a.shopify_export:
        import skanning_shopify
        f, k, an = skanning_shopify.analysera(str(Path(a.shopify_export).expanduser()))
        fl += f; kallor += k; anm += an
    if a.onsite:
        f, k = fynd_ur_onsite(a.onsite)
        fl += f; kallor.append(k)
    if a.url:
        import sajtskanning
        f, sidor, k, an = sajtskanning.skanna(a.url, a.max_sidor)
        fl += f; kallor += k; anm += an
    ut = Path(a.ut).expanduser(); ut.mkdir(parents=True, exist_ok=True)
    (ut / "fynd.csv").write_text(till_csv(fl), encoding="utf-8")
    (ut / "rapport.md").write_text(rapport_md(a.namn, date.today().isoformat(), kallor, fl, anm), encoding="utf-8")
    print(f"SAMMANFATTNING {a.namn}: {sum(1 for f in fl if f['allvar'] == 'BRIST')} brister, {sum(1 for f in fl if f['allvar'] == 'VARNING')} varningar. Rapport: {ut}/rapport.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
