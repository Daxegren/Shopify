#!/usr/bin/env python3
"""Hämtar Search Console-data (bara läsning) till CSV-filer.

Användning:  python3 gsc_export.py sc-domain:bestofsports.se [--months 16]
Skriver till ~/gsc_out/<egendom>/ och skriver ut en kort sammanfattning.
Inga nycklar i filen: inloggningen sker via din egen Google-inloggning i Cloud Shell.
"""
import argparse, csv, datetime as dt, os, re, sys
from urllib.parse import quote

SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"
API = "https://www.googleapis.com/webmasters/v3/sites/{site}/searchAnalytics/query"
PAGE = 5000          # rader per anrop (API-max 25 000)
MAX_ROWS = 25000     # tak per rapport

REPORTS = {          # namn: dimensioner
    "page": ["page"],
    "query": ["query"],
    "page_query": ["page", "query"],
    "country": ["country"],
    "device": ["device"],
    "month": ["date"],   # dagsvis; summeras till månader nedan
}


def session():
    try:
        import google.auth
        from google.auth.transport.requests import AuthorizedSession
        creds, _ = google.auth.default(scopes=[SCOPE])
        return AuthorizedSession(creds)
    except Exception as e:  # noqa
        sys.exit(
            "Kunde inte logga in mot Search Console: %s\n"
            "Kör en gång:\n  gcloud auth application-default login --scopes="
            "https://www.googleapis.com/auth/webmasters.readonly,"
            "https://www.googleapis.com/auth/cloud-platform\n"
            "och kör skriptet igen. (Eller använd samma inloggning som ~/gsc.py.)" % e)


def fetch(s, site, dims, start, end):
    rows, offset = [], 0
    while offset < MAX_ROWS:
        body = {"startDate": start, "endDate": end, "dimensions": dims,
                "rowLimit": PAGE, "startRow": offset, "dataState": "final"}
        r = s.post(API.format(site=quote(site, safe="")), json=body, timeout=120)
        if r.status_code != 200:
            sys.exit("Fel %s för %s: %s" % (r.status_code, dims, r.text[:300]))
        part = r.json().get("rows", [])
        rows += part
        if len(part) < PAGE:
            break
        offset += PAGE
    return rows


def to_month(rows):
    agg = {}
    for r in rows:
        m = r["keys"][0][:7]
        a = agg.setdefault(m, [0, 0, 0.0])
        a[0] += r["clicks"]; a[1] += r["impressions"]; a[2] += r["position"] * r["impressions"]
    out = []
    for m, (c, i, p) in sorted(agg.items()):
        out.append({"keys": [m], "clicks": c, "impressions": i,
                    "ctr": c / i if i else 0, "position": p / i if i else 0})
    return out


def write(path, dims, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(dims + ["clicks", "impressions", "ctr", "position"])
        for r in rows:
            w.writerow(r["keys"] + [int(r["clicks"]), int(r["impressions"]),
                                    round(r["ctr"], 4), round(r["position"], 2)])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site")
    ap.add_argument("--months", type=int, default=16)
    a = ap.parse_args()
    end = dt.date.today() - dt.timedelta(days=3)          # färskaste kompletta data
    start = end - dt.timedelta(days=int(min(a.months, 16) * 30.4))
    s = session()
    name = re.sub(r"[^a-zA-Z0-9.]+", "_", a.site.replace("sc-domain:", ""))
    out = os.path.expanduser("~/gsc_out/%s" % name)
    os.makedirs(out, exist_ok=True)
    print("== %s  %s till %s" % (a.site, start, end))
    for rep, dims in REPORTS.items():
        rows = fetch(s, a.site, dims, str(start), str(end))
        if rep == "month":
            rows = to_month(rows); dims = ["month"]
        write("%s/%s.csv" % (out, rep), dims, rows)
        c = sum(r["clicks"] for r in rows); i = sum(r["impressions"] for r in rows)
        if rep in ("device", "country", "month"):
            print("-- %s: %d rader" % (rep, len(rows)))
            for r in rows[:16 if rep == "month" else 6]:
                print("   %-14s klick %6d  visn %8d  ctr %5.1f%%  pos %4.1f" % (
                    r["keys"][0], r["clicks"], r["impressions"], 100 * r["ctr"], r["position"]))
        else:
            print("-- %s: %d rader (summa klick %d, visn %d)" % (rep, len(rows), c, i))
    print("Filer i %s" % out)
    print("Packa för nedladdning:  cd ~/gsc_out && tar czf %s.tgz %s" % (name, name))


if __name__ == "__main__":
    main()
