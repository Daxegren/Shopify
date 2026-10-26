#!/usr/bin/env python3
"""Täckningskarta: alla kontroller i genomlysningens kod mot senaste fynd per sajt (bara läsning).

Visar för varje kontroll som finns i koden hur många fynd den gav på varje sajt i senaste körningen ('-' = inga fynd eller kontrollen
kördes inte). Kontroller som ger fynd men inte finns i koden (till exempel gamla) listas sist. Använd den innan en ny kontroll eller en
ändring föreslås: den visar vad som redan täcks.

  python3 scripts/audit_tackning.py                       # läser gs://<projekt>-site-audit/audits/<sajt>/latest/summary.json
  python3 scripts/audit_tackning.py --lokal katalog       # läser katalog/summary-<sajt>.json
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

SITES = ["gorillasports-se", "gorillasports-dk", "bestofsports-se", "bestofsports-dk", "bestofsports-fi"]
SRC = Path(__file__).resolve().parents[1] / "src" / "site_audit"
SEV = {"critical": "K", "high": "H", "medium": "M", "low": "L", "info": "i"}


def checks_in_code() -> dict[str, str]:
    """check-id -> fil där den skrivs"""
    out: dict[str, str] = {}
    for py in sorted(SRC.rglob("*.py")):
        for m in re.finditer(r'\bF\(\s*"([a-z0-9_]+)"', py.read_text(encoding="utf-8")):
            out.setdefault(m.group(1), py.name)
    return out


def load(site: str, local: str | None, project: str) -> dict:
    try:
        if local:
            return json.loads((Path(local).expanduser() / f"summary-{site}.json").read_text(encoding="utf-8"))
        raw = subprocess.run(["gcloud", "storage", "cat", f"gs://{project}-site-audit/audits/{site}/latest/summary.json"],
                             capture_output=True, text=True, check=True).stdout
        return json.loads(raw)
    except Exception as e:  # noqa: BLE001
        print(f"[varning] {site}: {str(e)[:120]}", file=sys.stderr)
        return {}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lokal")
    ap.add_argument("--projekt", default="gorilla-sports-data")
    a = ap.parse_args()
    code = checks_in_code()
    data = {s: load(s, a.lokal, a.projekt).get("by_check", {}) for s in SITES}
    short = ["G-SE", "G-DK", "B-SE", "B-DK", "B-FI"]
    print(f"{'kontroll':44}{'fil':22}" + "".join(f"{s:>10}" for s in short))
    def row(check: str, where: str) -> str:
        cells = []
        for s in SITES:
            v = data[s].get(check)
            cells.append(f"{SEV.get(v['severity'], '?')}{v['count']}" if v else "-")
        return f"{check:44}{where:22}" + "".join(f"{c:>10}" for c in cells)
    for check in sorted(code):
        print(row(check, code[check]))
    extra = sorted({c for d in data.values() for c in d} - set(code))
    if extra:
        print("\nFynd från kontroller som inte finns som F(\"…\") i koden (admin, sammansatta eller äldre):")
        for check in extra:
            print(row(check, "(okänd källa)"))
    print("\nK=kritisk H=hög M=medel L=låg i=info; siffran är antal fynd i senaste körningen.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
