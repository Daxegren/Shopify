#!/usr/bin/env python3
"""Bygger skrivdata för godkända utkast. Användning: python3 bygg_skriv.py modul1 modul2 ... -> skriv_<ids>.json (id, titel, seo_title, meta, html)."""
import importlib, json, sys
BEST = {"10468773232906", "10462775771402"}  # beställningsvaror (tagg 'På beställning')
HAND = set(l.split()[0] for l in open("handhavd_ids.txt") if l.strip() and not l.startswith("#"))
def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def li(l): return "<ul>\n" + "\n".join("<li>"+esc(x)+"</li>" for x in l) + "\n</ul>"
def html(p):
    spec = sorted(p["spec"], key=lambda s: -len(s))
    h = f"<p>{esc(p['intro'])}</p>"
    if p["passar"]: h += f"<h2>Passar för</h2>{li(p['passar'])}"
    if spec: h += f"<h2>Specifikationer</h2>{li(spec)}"
    fr = "Normal leveranstid är 5–8 arbetsdagar. Fraktavgiften visas i kassan. Se sidan Frakt för övriga länder." + (" Beställningsvaror kan ta upp till en vecka längre." if p["id"] in BEST else "")
    h += f"<h2>Leverans, retur och garanti</h2><p><strong>Frakt och leverans:</strong> {fr}</p><p><strong>Retur:</strong> 30 dagars öppet köp. Vid ångrat köp står du för returfrakten. Vid godkänd reklamation står vi för returfrakten, kontakta kundtjänst för instruktioner.</p><p><strong>Reklamation:</strong> Du har reklamationsrätt enligt konsumentlagstiftningen i ditt land. Tillverkarens garanti anges på produkten när uppgiften finns.</p><p><strong>Säljare:</strong> BOS Latitude 60N AB, org.nr 559500-4325, Lindegårdsvägen 33, 746 36 Bålsta, info@bestofsports.se.</p>"
    if p["faq"]: h += "<h2>Vanliga frågor</h2>" + "".join(f"<h3>{esc(q)}</h3><p>{esc(a)}</p>" for q, a in p["faq"])
    if p["marke"]: h += f"<h2>Om märket</h2><p>{esc(p['marke'])}</p>"
    return h
if __name__ == "__main__":
    _d = {}
    for m in sys.argv[1:]:
        for p in importlib.import_module(m).D: _d[p["id"]] = p  # senaste modulen vinner
    out = []
    for p in _d.values():
        if True:
            if p["id"] in HAND: continue
            out.append({"id": p["id"], "nr": p["nr"], "titel": p["titel"], "seo_title": p["seo_title"], "meta": p["meta"], "html": html(p)})
    json.dump(out, open("skriv_" + "_".join(sys.argv[1:]) + ".json", "w"), ensure_ascii=False, indent=1)
    print(len(out))
