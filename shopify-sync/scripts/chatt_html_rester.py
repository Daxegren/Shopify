#!/usr/bin/env python3
"""Läsande analys: rester av kopierad chattgränssnitts-HTML i beskrivningar. Skriver inget i Shopify.
Användning: chatt_html_rester.py <in.ndjson|in.json> <typ> <ut.csv> [--html-field descriptionHtml]
Indata: en post per rad (ndjson) eller JSON-lista. Fält: id/legacyResourceId, handle, vendor, tags, createdAt, + HTML-fältet."""
import sys, re, json, csv, collections
PAT = {
 "data-start": r'data-start=', "data-end": r'data-end=',
 "data-is-last-node": r'data-is-last-node', "data-is-only-node": r'data-is-only-node',
 "data-message-id": r'data-message-id', "data-testid": r'data-testid',
 "class markdown/prose": r'class="[^"]*(markdown|prose)[^"]*"',
 "&lt;span data-": r'&lt;span data-',
 "dubbelkodning &amp;amp;": r'&amp;amp;',
 "tom wrapper (span/div/p)": r'<(span|div|p)[^>]*>\s*(&nbsp;|\s)*</\1>',
 "kapslad span": r'<span[^>]*>\s*<span',
 "em-streck (—)": r'—',
 "ChatGPT/OpenAI": r'(?i)chatgpt|openai',
}
WEAK = {"tom wrapper (span/div/p)", "kapslad span", "em-streck (—)", "dubbelkodning &amp;amp;"}
CP = {k: re.compile(v) for k, v in PAT.items()}
def scan(html):
    out = {}
    for k, rx in CP.items():
        n = len(rx.findall(html or ""))
        if n: out[k] = n
    return out
def load(p):
    t = open(p, encoding="utf-8").read()
    if t.lstrip().startswith("["): return json.loads(t)
    return [json.loads(l) for l in t.splitlines() if l.strip()]
if __name__ == "__main__":
    src, typ, dst = sys.argv[1:4]; fld = sys.argv[5] if len(sys.argv) > 5 else "descriptionHtml"
    rows = load(src); res = []
    for r in rows:
        h = r.get(fld) or ""
        hits = scan(h)
        # "—" räknas som flaggat först från 5 förekomster (massor), övrigt är brödtext
        if hits.get("em-streck (—)", 0) < 5: hits.pop("em-streck (—)", None)
        if hits:
            res.append({"id": r.get("legacyResourceId") or r.get("id"), "handle": r.get("handle"), "typ": typ,
              "vendor": r.get("vendor", ""), "in_sheet": ("ja" if "in sheet" in (r.get("tags") or []) else "nej") if "tags" in r else "",
              "skapad_manad": (r.get("createdAt") or "")[:7], "uppdaterad_manad": (r.get("updatedAt") or "")[:7],
              "styrka": ("stark" if any(k not in WEAK for k in hits) else "svag"), "antal_traffar": sum(hits.values()), "monster": "; ".join(f"{k}={v}" for k, v in sorted(hits.items(), key=lambda x: -x[1]))})
    res.sort(key=lambda x: -x["antal_traffar"])
    with open(dst, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(res[0].keys()) if res else ["id"], delimiter=";"); w.writeheader(); w.writerows(res)
    print(typ, "berörda", len(res), "av", len(rows))
