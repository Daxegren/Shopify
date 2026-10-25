#!/usr/bin/env bash
# Statusrapport för nattens genomlysningar. Klistra in hela utdata till Claude.
#   cd ~/Shopify/shopify-sync && git pull && bash scripts/audit_status.sh
# Visar senaste körning per jobb och de nyckeltal som avgör om rättningarna fungerat.
set -uo pipefail
PROJECT_ID="${PROJECT_ID:-gorilla-sports-data}"
REGION="${REGION:-europe-north1}"
BUCKET="${BUCKET:-${PROJECT_ID}-site-audit}"
SITES="bestofsports-se bestofsports-dk bestofsports-fi gorillasports-se gorillasports-dk"

echo "== Senaste körningar per jobb (COMPLETE 1/1 = lyckades)"
for j in site-audit-bos-se site-audit-bos-dk site-audit-bos-fi site-audit-gorilla-se site-audit-gorilla-dk; do
  printf '%-26s' "$j"
  gcloud run jobs executions list --job "$j" --region "$REGION" --limit 1 \
    --format="value(metadata.name,status.startTime,status.completionTime,status.succeededCount,status.failedCount)" 2>/dev/null || echo "(saknas)"
done

echo
echo "== Nyckeltal per sajt (senaste rapporten)"
for s in $SITES; do
  echo "-- $s"
  gcloud storage cat "gs://${BUCKET}/audits/${s}/latest/summary.json" 2>/dev/null | python3 -c '
import sys, json
try:
    d = json.load(sys.stdin)
except Exception:
    print("  ingen rapport än"); sys.exit()
sev = d["by_severity"]
print("  fynd:", d["total"], "| kritiska", sev["critical"], "hög", sev["high"], "medel", sev["medium"])
bc = d["by_check"]
for k in ("canonical_offsite", "broken_internal_link", "malformed_link_href", "product_schema_no_image", "collection_few_products", "missing_h1", "duplicate_title"):
    print("  %-26s %s" % (k, bc.get(k, {}).get("count", 0)))
'
done
