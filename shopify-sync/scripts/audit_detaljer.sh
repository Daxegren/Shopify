#!/usr/bin/env bash
# Fördjupning för en sajt: de vanligaste kontrollerna per allvarlighet och exempel på de allvarligaste.
#   bash scripts/audit_detaljer.sh gorillasports-se
# Läser senaste rapporten i bucketen. Bara läsning.
set -uo pipefail
SITE="${1:?Ange sajt, till exempel gorillasports-se}"
PROJECT_ID="${PROJECT_ID:-gorilla-sports-data}"
BUCKET="${BUCKET:-${PROJECT_ID}-site-audit}"
BASE="gs://${BUCKET}/audits/${SITE}/latest"
echo "== Kontroller per allvarlighet (${SITE})"
gcloud storage cat "${BASE}/summary.json" | python3 -c '
import sys, json
d = json.load(sys.stdin)
order = {"critical": 0, "high": 1, "medium": 2}
rows = sorted(d["by_check"].items(), key=lambda kv: (order.get(kv[1]["severity"], 9), -kv[1]["count"]))
for k, v in rows:
    if v["severity"] in order:
        print("%-9s %6d  %-34s %s" % (v["severity"], v["count"], k, v["message"][:80]))
' | head -n 30
echo
echo "== Exempel på kritiska och höga fynd (upp till 3 per kontroll)"
gcloud storage cat "${BASE}/findings.jsonl" | python3 -c '
import sys, json, collections
seen = collections.defaultdict(int)
for line in sys.stdin:
    f = json.loads(line)
    if f.get("severity") in ("critical", "high") or f.get("check") == "broken_internal_link":
        c = f.get("check")
        if seen[c] < 3:
            seen[c] += 1
            print("%-9s %-30s %s" % (f.get("severity"), c, (f.get("url") or "")[:100]))
            ev = f.get("evidence")
            if ev: print("          ", json.dumps(ev, ensure_ascii=False)[:200])
'
