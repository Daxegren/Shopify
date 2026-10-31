#!/usr/bin/env python3
"""Bygger kontrollbar JSON och granskningsfil ur utkasten. Användning: python3 bygg_utkast.py batch1_a batch1_b ... (modulnamn utan .py)"""
import importlib, json, subprocess, sys
mods = sys.argv[1:] or ["batch1_a"]
D = []
for m in mods:
    D += importlib.import_module(m).D
out, md = [], []
for p in D:
    spec = sorted(p["spec"], key=lambda s: -len(s))
    b = p["intro"] + "\n"
    if p["passar"]: b += "\nPassar dig som:\n" + "\n".join("- " + x for x in p["passar"]) + "\n"
    if spec: b += "\nSpecifikationer:\n" + "\n".join("- " + x for x in spec) + "\n"
    b += "\n[[STANDARDBLOCK]] Leverans, retur och garanti (standardblock) [[/STANDARDBLOCK]]\n"
    if p["faq"]: b += "\nVanliga frågor:\n" + "\n".join(f"- {q} {a}" for q, a in p["faq"]) + "\n"
    if p["marke"]: b += "\nOm märket: " + p["marke"] + "\n"
    out.append({"id": p["id"], "titel": p["titel"], "seo_title": p["seo_title"], **({"meta": p["meta"]} if p["meta"] else {}), "beskrivning": b, "fakta": p["fakta"]})
    md.append(f"### {p['nr']}. {p['orig_titel']}\nProdukt-id: `{p['id']}`\n\n**Titel:** {p['titel']}  ({len(p['titel'])} tecken)\n**SEO-titel:** {p['seo_title']}  ({len(p['seo_title'])} tecken)\n**Metabeskrivning:** {p['meta'] or '(utelämnad: för tunn källa)'}  ({len(p['meta'] or '')} tecken)\n\n**Beskrivning (utkast):**\n\n{b}\n**Motivering:** {p['motivering']}\n\n**Att bekräfta:**\n" + "\n".join("- " + x for x in p["att_bekrafta"]) + "\n\n---\n")
json.dump(out, open("utkast_kontroll.json", "w"), ensure_ascii=False, indent=1)
open("utkast_granskning.md", "w").write("\n".join(md))
r = subprocess.run([sys.executable, "../../shopify-sync/scripts/kontrollera_produkttext.py", "utkast_kontroll.json", "--seo-title-max", "43"], capture_output=True, text=True)
print(r.stdout[-6000:], r.stderr[-1500:], "exit", r.returncode)
