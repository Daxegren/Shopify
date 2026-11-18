import csv, re, sys, collections
d = sys.argv[1]
rows = list(csv.DictReader(open(d + "/page.csv", encoding="utf-8")))
agg = collections.defaultdict(lambda: [0, 0, 0.0, 0, set()])
for r in rows:
    p = re.sub(r"^https?://[^/]+", "", r["page"]).split("?")[0]
    m = re.match(r"^/([a-z]{2}(?:-[a-z]{2})?)/collections/([^/]+)$", p)
    lang = "sv"
    if m: lang, h = m.group(1), m.group(2)
    else:
        m = re.match(r"^/collections/([^/]+)$", p)
        if not m: continue
        h = m.group(1)
    a = agg[h]; c, i = int(r["clicks"]), int(r["impressions"])
    a[0] += c; a[1] += i; a[2] += float(r["position"]) * i; a[3] += 1; a[4].add(lang)
out = []
for h, (c, i, pw, n, langs) in agg.items():
    out.append((h, c, i, round(100 * c / i, 2) if i else 0, round(pw / i, 1) if i else 0, n, len(langs)))
out.sort(key=lambda x: -x[2])
w = csv.writer(open(sys.argv[2], "w", newline="", encoding="utf-8"), delimiter=";")
w.writerow(["handle", "klick", "visningar", "ctr_pct", "snittposition", "sidor_i_export", "sprak"])
w.writerows(out)
print(len(out), "kollektioner (handle, språk sammanslagna)")
print("== Topp 25 på visningar"); 
for r in out[:25]: print(*r)
print("== Topp 15 på klick")
for r in sorted(out, key=lambda x: -x[1])[:15]: print(*r)
