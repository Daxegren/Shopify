#!/usr/bin/env bash
# Driftsätter veckorapporten som Cloud Run Job: varje måndag 07:00 svensk tid läser den tillväxtvyerna och sparar
# rapporten i Cloud Storage (gs://<projekt>-site-audit/weekly/<sajt>/latest.md och vecka-<datum>.md).
# Använder samma image som data-refresh. Skapar inga hemligheter och ändrar ingen data, bara läser BigQuery.
#
#   PROJECT_ID=gorilla-sports-data IMAGE=<image> ./deploy/weekly_report_job.sh
#
# Förutsättning: vyerna finns (site-audit growth-sql | bq query --use_legacy_sql=false) och data-refresh har kört.
# Hämta rapporten:  gcloud storage cat gs://<projekt>-site-audit/weekly/<sajt>/latest.md
set -euo pipefail

: "${PROJECT_ID:?Sätt PROJECT_ID}"
: "${IMAGE:?Sätt IMAGE till imagen som data-refresh-jobbet använder (gcloud run jobs describe data-refresh --region europe-north1)}"
REGION="${REGION:-europe-north1}"
SCHEDULER_REGION="${SCHEDULER_REGION:-europe-west1}"
JOB="${JOB:-growth-weekly}"
SA="${SA:-shopify-sync@${PROJECT_ID}.iam.gserviceaccount.com}"
SCHEDULE="${SCHEDULE:-0 7 * * 1}"
SITE="${SITE:-gorillasports-se}"
BUCKET="${BUCKET:-${PROJECT_ID}-site-audit}"

gcloud config set project "$PROJECT_ID" >/dev/null
gcloud storage buckets add-iam-policy-binding "gs://${BUCKET}" --member "serviceAccount:$SA" --role roles/storage.objectAdmin >/dev/null

ARGS="--config,/app/sites.toml,weekly,--site,${SITE},--upload,gs://${BUCKET}/weekly"
if gcloud run jobs describe "$JOB" --region "$REGION" >/dev/null 2>&1; then ACTION=update; else ACTION=create; fi
gcloud run jobs "$ACTION" "$JOB" --region "$REGION" --image "$IMAGE" --service-account "$SA" \
  --command site-audit --args="$ARGS" --task-timeout 900 --max-retries 0 --memory 1Gi --cpu 1

gcloud run jobs add-iam-policy-binding "$JOB" --region "$REGION" --member "serviceAccount:$SA" --role roles/run.invoker >/dev/null
URI="https://run.googleapis.com/v2/projects/${PROJECT_ID}/locations/${REGION}/jobs/${JOB}:run"
if gcloud scheduler jobs describe "$JOB" --location "$SCHEDULER_REGION" >/dev/null 2>&1; then
  gcloud scheduler jobs update http "$JOB" --location "$SCHEDULER_REGION" --schedule "$SCHEDULE" --time-zone "Europe/Stockholm" --uri "$URI" --http-method POST --oauth-service-account-email "$SA"
else
  gcloud scheduler jobs create http "$JOB" --location "$SCHEDULER_REGION" --schedule "$SCHEDULE" --time-zone "Europe/Stockholm" --uri "$URI" --http-method POST --oauth-service-account-email "$SA"
fi
echo "Klart. Kör direkt: gcloud run jobs execute $JOB --region $REGION --wait"
echo "Läs rapporten:    gcloud storage cat gs://${BUCKET}/weekly/${SITE}/latest.md"
