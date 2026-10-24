#!/usr/bin/env bash
# Driftsätter site-audit som Cloud Run Job som körs varje natt 04:00 svensk tid.
# Använder samma image som shopify-sync (bygg först med deploy/cloudrun.sh, eller ange IMAGE).
#
#   PROJECT_ID=gorilla-sports-data ./deploy/site_audit_job.sh
#
# sites.toml i projektroten bakas in i imagen. Tokens läses från Secret Manager enligt
# SECRET_ENV (env-namn=secret-namn, kommaseparerat).
set -euo pipefail

: "${PROJECT_ID:?Sätt PROJECT_ID}"
REGION="${REGION:-europe-north1}"
SCHEDULER_REGION="${SCHEDULER_REGION:-europe-west1}"
JOB="${JOB:-site-audit}"
SA="${SA:-shopify-sync@${PROJECT_ID}.iam.gserviceaccount.com}"
SCHEDULE="${SCHEDULE:-0 4 * * *}"
TASK_TIMEOUT="${TASK_TIMEOUT:-7200}"   # sekunder; Cloud Run tillåter högst 86400. Ett jobb per domän behöver normalt 3 timmar (10800)
MEMORY="${MEMORY:-2Gi}"
SITES="${SITES:-all}"
SECRET_ENV="${SECRET_ENV:-SHOPIFY_ACCESS_TOKEN=shopify-access-token}"
REPO="${REPO:-containers}"

cd "$(dirname "$0")/.."
[ -f sites.toml ] || { echo "sites.toml saknas. Kopiera sites.example.toml och anpassa."; exit 1; }
gcloud config set project "$PROJECT_ID" >/dev/null

if [ -z "${IMAGE:-}" ]; then
  IMAGE="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO}/shopify-sync:audit-$(date +%Y%m%d%H%M%S)"
  echo "== Bygger $IMAGE"
  if ! gcloud builds submit --tag "$IMAGE" .; then
    gcloud auth configure-docker "${REGION}-docker.pkg.dev" --quiet
    docker build -t "$IMAGE" . && docker push "$IMAGE"
  fi
fi

SECRETS=""
IFS=',' read -ra PAIRS <<< "$SECRET_ENV"
for pair in "${PAIRS[@]}"; do
  secret="${pair#*=}"
  gcloud secrets describe "$secret" >/dev/null 2>&1 && SECRETS="${SECRETS:+$SECRETS,}${pair%%=*}=${secret}:latest"
done

# Rapport, actions.csv och redirects_import.csv sparas i en bucket, eftersom jobbets disk töms efter körningen.
BUCKET="${BUCKET:-${PROJECT_ID}-site-audit}"
if ! gcloud storage buckets describe "gs://${BUCKET}" >/dev/null 2>&1; then
  gcloud storage buckets create "gs://${BUCKET}" --location "$REGION" --uniform-bucket-level-access
fi
gcloud storage buckets add-iam-policy-binding "gs://${BUCKET}" \
  --member "serviceAccount:$SA" --role roles/storage.objectAdmin >/dev/null

# gcloud delar --args vid varje komma, så en lista med flera sajter (SITES=a,b,c) skulle bli flera argument. Därför skiljetecknet @
# (syntaxen ^@^ i början talar om vilket tecken som skiljer argumenten åt).
ARGS="^@^--config@/app/sites.toml@run@--site@${SITES}@--out@/tmp/audits@--bigquery@--search-data@--upload@gs://${BUCKET}/audits"
if gcloud run jobs describe "$JOB" --region "$REGION" >/dev/null 2>&1; then ACTION=update; else ACTION=create; fi
gcloud run jobs "$ACTION" "$JOB" --region "$REGION" --image "$IMAGE" --service-account "$SA" \
  --command site-audit --args="$ARGS" ${SECRETS:+--set-secrets "$SECRETS"} \
  --task-timeout "$TASK_TIMEOUT" --max-retries 0 --memory "$MEMORY" --cpu 1

gcloud run jobs add-iam-policy-binding "$JOB" --region "$REGION" \
  --member "serviceAccount:$SA" --role roles/run.invoker >/dev/null
URI="https://run.googleapis.com/v2/projects/${PROJECT_ID}/locations/${REGION}/jobs/${JOB}:run"
if gcloud scheduler jobs describe "$JOB" --location "$SCHEDULER_REGION" >/dev/null 2>&1; then
  gcloud scheduler jobs update http "$JOB" --location "$SCHEDULER_REGION" --schedule "$SCHEDULE" \
    --time-zone "Europe/Stockholm" --uri "$URI" --http-method POST --oauth-service-account-email "$SA"
else
  gcloud scheduler jobs create http "$JOB" --location "$SCHEDULER_REGION" --schedule "$SCHEDULE" \
    --time-zone "Europe/Stockholm" --uri "$URI" --http-method POST --oauth-service-account-email "$SA"
fi

echo "Klart. Kör direkt: gcloud run jobs execute $JOB --region $REGION --wait"
echo "Hämta filer:      gcloud storage cp -r gs://${BUCKET}/audits/<sajt>/latest ."
echo "Skapa vyer:       sed 's/PROJ/${PROJECT_ID}/g' sql/audit/views.sql | bq query --use_legacy_sql=false"
