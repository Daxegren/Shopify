"""Fynd ur en Shopify-export (produkter.csv, kollektioner.csv och valfritt oversattning_sammanfattning.csv från wb_export.py). Offline."""
from __future__ import annotations

import csv
import os
from collections import Counter

from skanning_paket import fynd


def _las(sokvag):
    with open(sokvag, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter=";"))


def analysera(katalog: str):
    """Returnerar (fynd, kallor, anmarkningar)."""
    ut, anm, kallor = [], [], []
    p_fil, k_fil, o_fil = (os.path.join(katalog, n) for n in ("produkter.csv", "kollektioner.csv", "oversattning_sammanfattning.csv"))
    if os.path.exists(p_fil):
        kallor.append("produkter.csv")
        P = _las(p_fil)
        akt = [p for p in P if p["status"] == "ACTIVE"]
        n = len(akt)
        st = Counter(p["status"] for p in P)
        ut.append(fynd("utkast", "Katalog", "Produkter i status utkast/arkiverad (av alla)", len(P) - st["ACTIVE"], len(P), "INFO", "P1",
                       "Granska om de ska publiceras eller tas bort", "per 100 produkter"))
        bilder = sum(int(p["antal_bilder"]) for p in akt)
        utan = sum(int(p["bilder_utan_alt"]) for p in akt)
        ut.append(fynd("alt_text", "Bilder", "Bilder utan alt-text (aktiva produkter)", utan, bilder, "BRIST" if bilder and utan / bilder > 0.2 else "VARNING",
                       "P1", "Sätt alt-text i bulk (wb_alt.py)", "per 1 000 bilder"))
        ut.append(fynd("utan_bild", "Bilder", "Aktiva produkter utan bild", sum(1 for p in akt if int(p["antal_bilder"]) == 0), n, "BRIST", "P1",
                       "Lägg till bild eller avpublicera", "per produkt"))
        okat = [p for p in akt if not p["kategori"] or p["kategori"].strip().lower() in ("okategoriserat", "uncategorized")]
        ut.append(fynd("utan_kategori", "Katalog", "Aktiva produkter utan produktkategori", len(okat), n, "BRIST" if n and len(okat) / n > 0.1 else "VARNING",
                       "P1", "Sätt produktkategori (kategori_satt.py)", "per 100 produkter", [p["titel"] for p in okat[:3]]))
        if any(p.get("kon_varde") for p in akt):
            utan_kon = [p for p in akt if not p.get("kon_varde")]
            ut.append(fynd("utan_kon", "Attribut", "Aktiva produkter utan fältet Avsett för (kön)", len(utan_kon), n, "VARNING", "P1",
                           "Fyll attributet efter regel (kon_fyll_target_gender.py)", "per 1 000 produkter"))
        t = Counter(p["titel"].strip().lower() for p in akt)
        dub = [k for k, v in t.items() if v > 1]
        ut.append(fynd("dubblettitlar", "Katalog", "Produkttitlar som används på flera aktiva produkter (antal produkter)", sum(t[k] for k in dub), n, "VARNING",
                       "P1", "Granska: samma produkt i flera storlekar eller riktiga dubbletter", "per 100 produkter", dub[:3]))
        ut.append(fynd("kort_beskrivning", "Innehåll", "Aktiva produkter med beskrivning under 100 tecken", sum(1 for p in akt if int(p["beskrivning_tecken"]) < 100), n,
                       "VARNING", "P4", "Skriv produkttexter", "per produkt"))
        st_ = [p for p in akt if p["seo_titel"]]
        sd_ = [p for p in akt if p["seo_beskrivning"]]
        ut.append(fynd("seo_titel_lang", "Metadata", "SEO-titlar över 60 tecken (av satta)", sum(1 for p in st_ if len(p["seo_titel"]) > 60), len(st_), "VARNING", "P4",
                       "Korta titeln", "per 100 produkter"))
        ut.append(fynd("seo_beskr_lang", "Metadata", "SEO-beskrivningar över 160 tecken (av satta)", sum(1 for p in sd_ if len(p["seo_beskrivning"]) > 160), len(sd_), "VARNING",
                       "P4", "Korta beskrivningen", "per 100 produkter"))
        anm.append("SEO-titel/-beskrivning tomma på en produkt betyder att Shopify använder produkttiteln/texten; det är inte i sig ett fel.")
    if os.path.exists(k_fil):
        kallor.append("kollektioner.csv")
        K = _las(k_fil)
        tom = [c for c in K if c["antal_produkter"] == "0"]
        ut.append(fynd("tomma_kollektioner", "Kollektioner", "Tomma kollektioner", len(tom), len(K), "BRIST" if len(tom) > 5 else "VARNING", "P2",
                       "Regelfix, avpublicera och omdirigera", "per kollektion", [c["handle"] for c in tom[:5]]))
        ut.append(fynd("kollektion_utan_seo_titel", "Kollektioner", "Kollektioner utan SEO-titel", sum(1 for c in K if not c["seo_titel"]), len(K), "VARNING", "P4",
                       "Skriv SEO-titel (prioritera efter visningar)", "per kollektion"))
        ut.append(fynd("kollektion_utan_seo_beskr", "Kollektioner", "Kollektioner utan SEO-beskrivning", sum(1 for c in K if not c["seo_beskrivning"]), len(K), "VARNING",
                       "P4", "Skriv SEO-beskrivning", "per kollektion"))
        ut.append(fynd("kollektion_kort_text", "Kollektioner", "Kollektioner med nästan ingen beskrivning (under 50 tecken)", sum(1 for c in K if int(c["beskrivning_tecken"]) < 50),
                       len(K), "VARNING", "P4", "Skriv kategoritext", "per kollektion"))
    if os.path.exists(o_fil):
        kallor.append("oversattning_sammanfattning.csv")
        R = _las(o_fil)
        anm.append("Översättningstäckningen räknas på alla produkter i exporten, även utkast och arkiverade; täckningen för aktiva produkter är sannolikt högre.")
        by: dict[tuple[str, str], dict] = {}
        for r in R:
            by.setdefault((r["typ"], r["nyckel"]), {})[r["sprak"]] = r
        for typ, nyckel, namn in (("PRODUCT", "title", "produkttitlar"), ("COLLECTION", "title", "kollektionstitlar"), ("COLLECTION", "body_html", "kollektionsbeskrivningar")):
            d = by.get((typ, nyckel), {})
            if not d:
                continue
            tot = max(int(v["finns_i_kalla"]) for v in d.values())
            if not tot:
                continue
            sam = sorted(d.items(), key=lambda kv: int(kv[1]["oversatt"]))
            saknas = [(l, tot - int(v["oversatt"])) for l, v in sam[:3]]
            ut.append(fynd(f"ovs_{typ.lower()}_{nyckel}", "Språk", f"Minst översatta {namn} (de tre sämsta språken: " + ", ".join(f"{l} saknar {s}" for l, s in saknas) + ")",
                           sum(s for _, s in saknas), tot * 3, "VARNING", "P5", "Översätt saknade texter per språk", "per språk och 1 000 texter"))
            foralt = [(l, int(v["foraldrad"])) for l, v in d.items()]
            tot_for = sum(f for _, f in foralt)
            tot_ovs = sum(int(v["oversatt"]) for v in d.values())
            ut.append(fynd(f"ovs_foraldrad_{typ.lower()}_{nyckel}", "Språk", f"Föråldrade översättningar av {namn} (alla språk)", tot_for, tot_ovs, "VARNING", "P5",
                           "Översätt om ändrade källtexter", "per språk och 1 000 texter"))
    return ut, kallor, anm
