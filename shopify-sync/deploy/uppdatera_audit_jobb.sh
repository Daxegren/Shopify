#!/usr/bin/env bash
# Bygger en ny image och sätter den på de fem site-audit-jobben. Allt annat i jobben ligger kvar oförändrat
# (argument, tidsgräns, minne, hemligheter och Cloud Scheduler-tider), eftersom bara --image uppdateras.
#
#   cd ~/Shopify/shopify-sync && git pull origin <gren> && PROJECT_ID=gorilla-sports-data ./deploy/uppdatera_audit_jobb.sh
#
# Jobben körs sedan på sina vanliga tider (svensk tid): BOS SE 01:30, Gorilla SE 04:00, BOS DK 06:00, Gorilla DK 08:30, BOS FI 11:00.
# Starta ett jobb direkt: gcloud run jobs execute <jobb> --region europe-north1
set -euo pipefail

PROJECT_ID="${PROJECT_ID:-gorilla-sports-data}"
REGION="${REGION:-europe-north1}"
SCHEDULER_REGION="${SCHEDULER_REGION:-europe-west1}"
REPO="${REPO:-containers}"
JOBS="${JOBS:-site-audit-bos-se site-audit-gorilla-se site-audit-bos-dk site-audit-gorilla-dk site-audit-bos-fi}"

cd "$(dirname "$0")/.."
gcloud config set project "$PROJECT_ID" >/dev/null
IMAGE="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO}/shopify-sync:audit-$(date +%Y%m%d%H%M%S)"
echo "== Bygger $IMAGE (tar några minuter)"
gcloud builds submit --tag "$IMAGE" .

for job in $JOBS; do
  echo "== Uppdaterar $job"
  gcloud run jobs update "$job" --region "$REGION" --image "$IMAGE"
done

echo; echo "== Kontroll: image per jobb"
for job in $JOBS; do
  printf '%-26s' "$job"; gcloud run jobs describe "$job" --region "$REGION" | grep -m1 -i "image:" | sed 's/^ *//'
done
echo; echo "== Kontroll: schema (Cloud Scheduler)"
gcloud scheduler jobs list --location "$SCHEDULER_REGION" --format="table(name.basename(),schedule,timeZone,state)" | grep -i "site-audit" || true
