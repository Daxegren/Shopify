"""Gemensamma definitioner för butiks- och sajtskanningen: fynd, paket och rapportmall (offline, ingen nätverkstrafik).

Ett fynd är en kontroll som ger ett antal träffar av ett antal granskade objekt. Varje fynd kopplas till ett paket (en sak man kan sälja
och leverera) och en enhet (det som styr arbetsinsatsen). Priser sätts inte här: det är Davids beslut (se docs/paket-och-malgrupper.md).
"""
from __future__ import annotations

import csv
import io

PAKET = {
    "P1": "Katalogstädning (kategorier, attribut, bilder, dubbletter)",
    "P2": "Kollektioner och sidstruktur (tomma sidor, regler, omdirigeringar)",
    "P3": "Teknisk SEO (indexering, canonical, schema, hastighet)",
    "P4": "Innehåll och metadata (titlar, beskrivningar, rubriker, texter)",
    "P5": "Språk och marknader (översättning, hreflang)",
    "P6": "Mätning och uppföljning (baslinje, jämförelse, månadsrapport)",
}
ALLVAR = {"BRIST": 3, "VARNING": 2, "INFO": 1}


def fynd(id, omrade, titel, antal, av, allvar, paket, atgard, enhet, exempel=None):
    """Ett fynd. antal = träffar, av = granskade objekt (0 om okänt)."""
    return {"id": id, "omrade": omrade, "titel": titel, "antal": int(antal), "av": int(av),
            "andel": round(100 * antal / av, 1) if av else None, "allvar": allvar, "paket": paket,
            "atgard": atgard, "enhet": enhet, "exempel": list(exempel or [])[:5]}


def sortera(fynd_lista):
    return sorted(fynd_lista, key=lambda f: (-ALLVAR.get(f["allvar"], 0), -(f["andel"] or 0), -f["antal"]))


def till_csv(fynd_lista) -> str:
    ut = io.StringIO()
    w = csv.writer(ut, delimiter=";")
    w.writerow(["id", "omrade", "titel", "antal", "av", "andel_pct", "allvar", "paket", "atgard", "enhet", "exempel"])
    for f in sortera(fynd_lista):
        w.writerow([f["id"], f["omrade"], f["titel"], f["antal"], f["av"], f["andel"] if f["andel"] is not None else "", f["allvar"],
                    f["paket"], f["atgard"], f["enhet"], " | ".join(f["exempel"])])
    return ut.getvalue()


def rapport_md(namn: str, datum: str, kallor: list[str], fynd_lista, anmarkningar: list[str] | None = None) -> str:
    fl = sortera([f for f in fynd_lista if f["antal"] > 0])  # kontroller utan träffar är inga fynd
    r = [f"# Skanningsrapport: {namn}", "", f"Datum: {datum}. Källor: {', '.join(kallor) or 'inga'}. Läsande skanning, inget har ändrats på sajten.", ""]
    brist = sum(1 for f in fl if f["allvar"] == "BRIST")
    varn = sum(1 for f in fl if f["allvar"] == "VARNING")
    r += [f"**Sammanfattning:** {brist} brister och {varn} varningar fördelade på {len({f['paket'] for f in fl if f['allvar'] != 'INFO'})} paket.", ""]
    r += ["## Fynd per paket", ""]
    for kod, beskr in PAKET.items():
        rader = [f for f in fl if f["paket"] == kod and f["allvar"] != "INFO"]
        if not rader:
            continue
        r += [f"### {kod}. {beskr}", "", "| Fynd | Antal | Av | Andel | Allvar | Åtgärd | Enhet för insats |", "|---|---|---|---|---|---|---|"]
        for f in rader:
            r.append(f"| {f['titel']} | {f['antal']} | {f['av'] or ''} | {str(f['andel']) + ' %' if f['andel'] is not None else ''} | {f['allvar']} | {f['atgard']} | {f['enhet']} |")
        r.append("")
    info = [f for f in fl if f["allvar"] == "INFO"]
    if info:
        r += ["## Att veta", ""] + [f"- {f['titel']}: {f['antal']}" + (f" av {f['av']}" if f["av"] else "") for f in info] + [""]
    ex = [f for f in fl if f["exempel"] and f["allvar"] != "INFO"]
    if ex:
        r += ["## Exempel (för att kunna kontrollera fynden)", ""]
        for f in ex[:12]:
            r.append(f"- {f['titel']}: " + "; ".join(f["exempel"]))
        r.append("")
    if anmarkningar:
        r += ["## Anmärkningar och begränsningar", ""] + [f"- {a}" for a in anmarkningar] + [""]
    return "\n".join(r)
