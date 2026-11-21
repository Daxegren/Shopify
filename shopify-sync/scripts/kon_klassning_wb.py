#!/usr/bin/env python3
"""Läsande könsklassning av aktiva produkter (Workout Brands). Skriver inget i butiken.
Regel: dam = tagg Dam/Women/woman/Kvinna (skiftlägesokänsligt, hel tagg) eller titel som börjar med Ladies/Women eller vendor UC Ladies.
herr = tagg Herr/Man/Men. unisex = tagg Unisex.
Klass (prioritetsordning): båda (både dam- och herrsignal) > unisex (taggen Unisex) > bara dam > bara herr > ingen.
Användning: kon_klassning_wb.py <aktiva.ndjson>  (importeras av analysen)"""
import json
DAM = {"dam", "women", "woman", "kvinna"}; HERR = {"herr", "man", "men"}
def klassa(p):
    tl = [t.lower().strip() for t in (p.get("tags") or [])]
    dam_t = [t for t in tl if t in DAM]; herr_t = [t for t in tl if t in HERR]
    titel = (p.get("title") or "").lower()
    dam = bool(dam_t) or titel.startswith(("ladies", "women")) or (p.get("vendor") or "") == "UC Ladies"
    herr = bool(herr_t)
    uni = "unisex" in tl
    if dam and herr: k = "båda"
    elif uni: k = "unisex"
    elif dam: k = "bara dam"
    elif herr: k = "bara herr"
    else: k = "ingen"
    return k, len(dam_t), len(herr_t)
