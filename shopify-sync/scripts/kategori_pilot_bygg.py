#!/usr/bin/env python3
"""Bygger om pilot/<handle>.json och pilotutkast.md från pilot_texter.py (BARA FILER, inget till Shopify).
Användning: kategori_pilot_bygg.py <mapp>   (mappen har pilot_texter.py, pilot/ och underlag/)"""
import importlib.util, json, os, sys
mapp = sys.argv[1]
spec = importlib.util.spec_from_file_location('t', os.path.join(mapp, 'pilot_texter.py')); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
ut = ['# Pilotutkast kategoritexter BEST OF SPORTS (2026-11-04)', '',
      'Utkast. Inget är skrivet i Shopify. Underlag: `underlag/<handle>.json` (framtaget med kod ur kollektionens egna produkter). Kontroll: `shopify-sync/scripts/kategori_kontroll.py` (0 fel). Oberoende granskning: `granskning-opus.md`; rättelserna därifrån är gjorda.', '']
for h, (stycken, seo, meta) in m.T.items():
    pf = os.path.join(mapp, 'pilot', h + '.json'); d = json.load(open(pf, encoding='utf-8'))
    u = json.load(open(os.path.join(mapp, 'underlag', h + '.json'), encoding='utf-8'))
    d['ny_text'] = ' '.join(stycken); d['ny_html'] = ''.join(f'<p>{s}</p>' for s in stycken)
    d['ny_seo_titel'] = seo; d['ny_meta'] = meta; d['ord_ny'] = len(d['ny_text'].split())
    json.dump(d, open(pf, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    nt = d['nuvarande_text']
    ut += [f"## {d['titel']} (`{h}`, {d['id']})",
           f"- **Nuvarande SEO-titel:** {d['nuvarande_seo_titel']} ({len(d['nuvarande_seo_titel'])} tecken)",
           f"- **Ny SEO-titel:** {seo} ({len(seo)} tecken)",
           f"- **Nuvarande meta:** {d['nuvarande_meta']}",
           f"- **Ny meta:** {meta} ({len(meta)} tecken)",
           f"- **Nuvarande text ({d['ord_nu']} ord), början:** {nt[:300]}…",
           f"- **Ny text ({d['ord_ny']} ord):**", ''] + [f'> {s}\n' for s in stycken] + [
           f"- **Faktaunderlag:** {u['antal_koopbara']} köpbara huvudprodukter (av {u['antal_koopbara_alla']} köpbara i kollektionen), märken {[list(x) for x in u['marken']]}, pris {u['pris_min']}–{u['pris_max']} kr.", '']
open(os.path.join(mapp, 'pilotutkast.md'), 'w', encoding='utf-8').write('\n'.join(ut))
print('klart', len(m.T))
