#!/usr/bin/env python3
"""Sammanfattar products_public.json och collections_public.json (se offentlig_inventering.py) till inventering.json."""
import json, re, sys, collections, html
def text(h): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h or ""))).strip()
def main(d):
    p = json.load(open(f"{d}/products_public.json")); k = json.load(open(f"{d}/collections_public.json"))
    lang = collections.Counter(); langs = []
    ut = {"antal_produkter_publicerade": len(p), "antal_kollektioner": len(k)}
    ut["vendors"] = collections.Counter(x["vendor"] for x in p)
    ut["product_type"] = collections.Counter(x["product_type"] or "(tom)" for x in p)
    tg = collections.Counter(t for x in p for t in x.get("tags", [])); ut["taggar"] = tg
    lens = sorted(len(text(x["body_html"])) for x in p); ut["beskrivning_tecken"] = {"min": lens[0], "median": lens[len(lens)//2], "max": lens[-1], "under_200": sum(l < 200 for l in lens), "tom": sum(l == 0 for l in lens)}
    tit = collections.Counter(x["title"].strip().lower() for x in p); ut["dubblettitlar"] = [t for t, c in tit.items() if c > 1]
    ut["varianter_per_produkt"] = collections.Counter(len(x["variants"]) for x in p)
    ut["bilder_per_produkt"] = collections.Counter(len(x["images"]) for x in p)
    ut["bilder_utan_alt"] = sum(1 for x in p for i in x["images"] if not (i.get("alt") or "").strip())
    ut["bilder_totalt"] = sum(len(x["images"]) for x in p)
    ut["engelska_titlar_misstanke"] = [x["title"] for x in p if re.search(r"\b(the|with|for|and|dog|cat|pack)\b", x["title"], re.I)]
    ut["titel_langd"] = {"max": max(len(x["title"]) for x in p), "over_70": sum(len(x["title"]) > 70 for x in p)}
    ut["utan_pris"] = sum(1 for x in p if not x["variants"] or not x["variants"][0].get("price"))
    ut["inte_i_lager_tillgangliga"] = sum(1 for x in p if not any(v.get("available") for v in x["variants"]))
    ut["kollektioner"] = [{"handle": c["handle"], "titel": c["title"], "antal": c.get("products_count"), "beskrivning_tecken": len(text(c.get("body_html")))} for c in k]
    ut["kollektioner_tomma"] = [c["handle"] for c in k if c.get("products_count") == 0]
    ut["kollektioner_utan_beskrivning"] = sum(1 for c in k if not text(c.get("body_html")))
    ut["produkter"] = [{"id": x["id"], "handle": x["handle"], "title": x["title"], "vendor": x["vendor"], "type": x["product_type"], "tags": x["tags"], "tecken": len(text(x["body_html"])), "varianter": len(x["variants"]), "pris": x["variants"][0]["price"] if x["variants"] else None} for x in p]
    json.dump(ut, open(f"{d}/inventering.json", "w"), ensure_ascii=False, indent=1, default=dict)
    print(json.dumps({k2: v for k2, v in ut.items() if k2 not in ("produkter", "kollektioner")}, ensure_ascii=False, default=dict, indent=1))
main(sys.argv[1])
