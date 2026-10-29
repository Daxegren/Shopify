#!/usr/bin/env python3
"""Kontrollerar utkast till produkttexter mot standarden i docs/produkttexter-standard.md. Bara läsning, ingen koppling till någon butik.

  python3 scripts/kontrollera_produkttext.py utkast.json [--seo-title-max 43] [--meta-min 130] [--meta-max 155] [--json]

Indata: en JSON-lista med ett objekt per produkt. Fält (alternativa namn inom parentes):
  id/handle, titel (title, titel_efter), seo_title (seo_title_efter), meta (seo_description, seo_description_efter),
  beskrivning (body, beskrivning_efter), fakta (källfakta, kallfakta): all källtext som texterna får bygga på, inklusive originaltiteln.
Fält som saknas hoppas över. Text mellan [[STANDARDBLOCK]] och [[/STANDARDBLOCK]] (leverans, retur, garanti) räknas inte som produktpåståenden.

Allvarlighet: FEL = ska rättas före godkännande; VARNING = bedöms av granskare. Slutkoden är 1 om något FEL finns, annars 0.
Kontrollen ersätter inte granskaren: den hittar mönster, inte felaktiga fakta som råkar stå i källtexten."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass

ALIAS = {
    "id": ("id", "handle", "produkt_id"),
    "titel": ("titel", "title", "titel_efter"),
    "seo_title": ("seo_title", "seo_title_efter"),
    "meta": ("meta", "seo_description", "seo_description_efter"),
    "beskrivning": ("beskrivning", "body", "beskrivning_efter"),
    "fakta": ("fakta", "källfakta", "kallfakta"),
}
FORBJUDNA_FRASER = ["upptäck", "perfekt för dig", "i dagens snabba", "höj din", "nästa nivå", "oavsett om", "toppkvalitet", "unik", "revolutionerande", "fantastisk", "oslagbar"]
SUPERLATIV = re.compile(r"\b(bäst\w*|marknadsledande|ledande|världens|nummer 1|nr 1|störst\w*|billigast\w*)\b", re.I)
HALSA = re.compile(r"protein|vitamin|kreatin|aminosyr|koffein|energi|fettförbr|viktminsk|viktnedgång|rehab|smärta|läk|hälsa|terap|bota|förebygg|vibration|massage|behandl|sjukdom|ledvärk|blodtryck", re.I)
URSPRUNG = re.compile(r"\b(tillverk\w+|producer\w+|design\w+)\b[^.\n]{0,40}\bi\s+(?-i:[A-ZÅÄÖ])\w+|\bmade in\b", re.I)
NATIONALITET = re.compile(r"\b(tysk\w*|italiensk\w*|svensk\w*|norsk\w*|dansk\w*|finsk\w*|kinesisk\w*|amerikansk\w*|engelsk\w*|holländsk\w*|taiwanesisk\w*)\b", re.I)
LOFTEN = re.compile(r"\b(garanterad\w*|garanterar|bevisad\w*|kliniskt|certifierad\w*|godkänd\w*|testvinnare)\b", re.I)
PRIS = re.compile(r"\b(rea|rabatt\w*|billig\w*|fraktfri\w*|gratis frakt|kampanj\w*|erbjudande\w*)\b|\d[\d\s.,]*\s?(kr|sek|dkk|eur|€)\b", re.I)
ENGELSKA_ORD = re.compile(r"\b(with|the|and|for|your|black|white|red|blue|green|pink|grey|gray|yellow)\b", re.I)
TAGG = re.compile(r"<[^>]+>")
STANDARD = re.compile(r"\[\[STANDARDBLOCK\]\].*?\[\[/STANDARDBLOCK\]\]", re.S)
TAL = re.compile(r"\d+(?:[.,]\d+)?")


@dataclass
class Fynd:
    produkt: str
    nivå: str
    regel: str
    text: str


def hamta(p: dict, nyckel: str):
    for n in ALIAS[nyckel]:
        if p.get(n) not in (None, ""):
            return p[n]
    return None


def normalisera_tal(s: str) -> str:
    s = re.sub(r"(?<=\d)[\s ](?=\d{3}\b)", "", s)
    return s.replace(",", ".")


def tal_i(s: str) -> set[str]:
    out = set()
    for t in TAL.findall(normalisera_tal(s)):
        t = t.rstrip("0").rstrip(".") if "." in t else t
        out.add(t)
    return out


def ren_text(s: str) -> str:
    return TAGG.sub(" ", STANDARD.sub(" ", s))


def kontrollera_produkt(p: dict, opt: argparse.Namespace) -> list[Fynd]:
    pid = str(hamta(p, "id") or "?")
    f: list[Fynd] = []
    titel, seo, meta = hamta(p, "titel"), hamta(p, "seo_title"), hamta(p, "meta")
    body, fakta = hamta(p, "beskrivning"), hamta(p, "fakta")
    texter = {k: v for k, v in (("titel", titel), ("seo_title", seo), ("meta", meta), ("beskrivning", body)) if v}

    def fel(regel, text, nivå="FEL"):
        f.append(Fynd(pid, nivå, regel, text))

    if titel:
        if len(titel) > opt.title_max:
            fel("titel_lang", f"{len(titel)} tecken, högst {opt.title_max}")
        if titel.count(",") > 2:
            fel("titel_kommatecken", f"{titel.count(',')} kommatecken, högst 2", "VARNING")
        if titel.isupper():
            fel("titel_versaler", titel)
    if seo:
        if len(seo) > opt.seo_title_max:
            fel("seo_titel_lang", f"{len(seo)} tecken, högst {opt.seo_title_max}")
        if opt.seo_suffix and opt.seo_suffix.strip(" -–|").lower() in seo.lower():
            fel("varumarke_dubbelt", "SEO-titeln innehåller redan varumärket som temat lägger till")
    if meta and not (opt.meta_min <= len(meta) <= opt.meta_max):
        fel("meta_langd", f"{len(meta)} tecken, ska vara {opt.meta_min}–{opt.meta_max}")

    for namn, t in texter.items():
        ren = ren_text(t)
        låg = ren.lower()
        for fras in FORBJUDNA_FRASER:
            if fras in låg:
                fel("forbjuden_fras", f"{namn}: '{fras}'")
        if "!" in ren:
            fel("utropstecken", namn)
        m = SUPERLATIV.search(ren)
        if m:
            fel("superlativ", f"{namn}: '{m.group(0)}'")
        m = HALSA.search(ren)
        if m:
            fel("halsa", f"{namn}: '{m.group(0)}' (kräver manuell granskning)")
        if PRIS.search(ren):
            fel("pris_eller_kampanj", f"{namn}: '{PRIS.search(ren).group(0).strip()}'")
        if ENGELSKA_ORD.search(ren):
            fel("engelska_ord", f"{namn}: '{ENGELSKA_ORD.search(ren).group(0)}'", "VARNING")
        fk = (fakta or "").lower()
        for m in URSPRUNG.finditer(ren):
            fel("ursprung", f"{namn}: '{m.group(0)}' (ursprung kräver källa)", "VARNING" if fk and m.group(0).lower() in fk else "FEL")
        for m in NATIONALITET.finditer(ren):
            if m.group(0).lower() not in fk:
                fel("nationalitet_utan_kalla", f"{namn}: '{m.group(0)}'")
        for m in LOFTEN.finditer(ren):
            if m.group(0).lower() not in fk:
                fel("lofte_utan_kalla", f"{namn}: '{m.group(0)}'")

    if fakta:
        kallt = tal_i(fakta)
        for namn, t in texter.items():
            for n in sorted(tal_i(ren_text(t)) - kallt, key=float):
                fel("tal_utan_kalla", f"{namn}: {n}")
    elif texter:
        fel("fakta_saknas", "ingen källtext angiven, tal och påståenden kan inte kontrolleras")

    if body:
        ren = ren_text(body)
        låg = ren.lower()
        for rubrik in ("passar dig som", "specifikationer"):
            if rubrik not in låg:
                fel("struktur", f"saknar avsnittet '{rubrik}'", "VARNING")
        if "leverans" not in body.lower() and "[[standardblock]]" not in body.lower():
            fel("struktur", "saknar leverans/retur-avsnitt eller standardblock", "VARNING")
        forsta = next((r.strip() for r in ren.splitlines() if r.strip()), "")
        if len(re.findall(r"[.!?](?:\s|$)", forsta)) > 3:
            fel("struktur", "första stycket har fler än 3 meningar (svar först, kort)", "VARNING")
        ord_antal = len(ren.split())
        if ord_antal < 40 or ord_antal > 450:
            fel("beskrivning_langd", f"{ord_antal} ord (förväntat 40–450)", "VARNING")
    return f


def kontrollera_batch(produkter: list[dict], opt: argparse.Namespace) -> list[Fynd]:
    fynd: list[Fynd] = []
    for p in produkter:
        fynd += kontrollera_produkt(p, opt)
    for nyckel, regel in (("titel", "dubblett_titel"), ("seo_title", "dubblett_seo_titel"), ("meta", "dubblett_meta")):
        sett: dict[str, str] = {}
        for p in produkter:
            v = hamta(p, nyckel)
            if v:
                k = v.strip().lower()
                if k in sett:
                    fynd.append(Fynd(str(hamta(p, "id") or "?"), "FEL", regel, f"samma som {sett[k]}"))
                sett[k] = str(hamta(p, "id") or "?")
    return fynd


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("fil")
    ap.add_argument("--title-max", type=int, default=70)
    ap.add_argument("--seo-title-max", type=int, default=60)
    ap.add_argument("--seo-suffix", default="", help="Text temat lägger till efter SEO-titeln, till exempel ' – BEST OF SPORTS' (varumärket får då inte stå i SEO-titeln).")
    ap.add_argument("--meta-min", type=int, default=130)
    ap.add_argument("--meta-max", type=int, default=155)
    ap.add_argument("--json", action="store_true")
    opt = ap.parse_args(argv)
    with open(opt.fil, encoding="utf-8") as fh:
        data = json.load(fh)
    produkter = data if isinstance(data, list) else data.get("produkter", [])
    fynd = kontrollera_batch(produkter, opt)
    n_fel = sum(1 for x in fynd if x.nivå == "FEL")
    if opt.json:
        print(json.dumps([x.__dict__ for x in fynd], ensure_ascii=False, indent=1))
    else:
        for x in fynd:
            print(f"{x.nivå:8} {x.produkt[-14:]:>14}  {x.regel:24} {x.text}")
        print(f"\n{len(produkter)} produkter, {n_fel} FEL, {len(fynd) - n_fel} VARNINGAR")
    return 1 if n_fel else 0


if __name__ == "__main__":
    sys.exit(main())
