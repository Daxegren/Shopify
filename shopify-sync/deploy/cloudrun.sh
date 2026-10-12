#!/usr/bin/env bash
# Driftsätter shopify-sync som Cloud Run Job som körs varje timme via Cloud Scheduler.
#
# Förutsättningar:
#   - gcloud är inloggat (gcloud auth login) mot rätt projekt.
#   - Hemligheterna finns i Secret Manager (se README, steg 3).
#
# Användning:
#   PROJECT_ID=mitt-projekt SHOPIFY_SHOP_DOMAIN=butik.myshopify.com ./deploy/cloudrun.sh
#
# Fler butiker i samma projekt: ett jobb per butik, med eget dataset och egen token, t.ex.
#   PROJECT_ID=... SHOPIFY_SHOP_DOMAIN=mankovsky.myshopify.com JOB=shopify-sync-mankovsky \
#     BQ_DATASET=shopify_mankovsky TOKEN_SECRET=mankovsky-token ./deploy/cloudrun.sh
set -euo pipefail

: "${PROJECT_ID:?Sätt PROJECT_ID}"
: "${SHOPIFY_SHOP_DOMAIN:?Sätt SHOPIFY_SHOP_DOMAIN}"
REGION="${REGION:-europe-north1}"
# Cloud Scheduler finns inte i alla regioner; europe-west1 är säker.
SCHEDULER_REGION="${SCHEDULER_REGION:-europe-west1}"
BQ_LOCATION="${BQ_LOCATION:-EU}"
SINKS="${SINKS:-bigquery}"
SCHEDULE="${SCHEDULE:-7 * * * *}"          # minut 7 varje timme
JOB="${JOB:-shopify-sync}"
BQ_DATASET="${BQ_DATASET:-shopify}"
TOKEN_SECRET="${TOKEN_SECRET:-shopify-access-token}"
SA_NAME="${SA_NAME:-shopify-sync}"
SA="${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
REPO="${REPO:-containers}"
IMAGE="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO}/${JOB}:$(date +%Y%m%d%H%M%S)"

cd "$(dirname "$0")/.."
gcloud config set project "$PROJECT_ID" >/dev/null

echo "== Aktiverar API:er"
gcloud services enable run.googleapis.com cloudscheduler.googleapis.com \
  secretmanager.googleapis.com bigquery.googleapis.com \
  artifactregistry.googleapis.com cloudbuild.googleapis.com

echo "== Tjänstkonto"
gcloud iam service-accounts describe "$SA" >/dev/null 2>&1 || \
  { gcloud iam service-accounts create "$SA_NAME" --display-name "Shopify sync" && sleep 15; }
for role in roles/bigquery.dataEditor roles/bigquery.jobUser roles/secretmanager.secretAccessor; do
  gcloud projects add-iam-policy-binding "$PROJECT_ID" --member "serviceAccount:$SA" \
    --role "$role" --condition=None >/dev/null
done

# Nya projekt bygger med Compute-standardkontot, som behöver byggrättigheter.
PROJECT_NUMBER="$(gcloud projects describe "$PROJECT_ID" --format='value(projectNumber)')"
gcloud projects add-iam-policy-binding "$PROJECT_ID" \
  --member "serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
  --role roles/cloudbuild.builds.builder --condition=None >/dev/null

echo "== Bygger image"
gcloud artifacts repositories describe "$REPO" --location "$REGION" >/dev/null 2>&1 || \
  gcloud artifacts repositories create "$REPO" --repository-format docker --location "$REGION"
# Cloud Build först; faller tillbaka på lokal Docker (finns i Cloud Shell) om det nekas,
# t.ex. medan behörigheter i ett nytt projekt fortfarande sprids.
if ! gcloud builds submit --tag "$IMAGE" .; then
  command -v docker >/dev/null || { echo "Cloud Build misslyckades och Docker saknas."; exit 1; }
  echo "== Cloud Build misslyckades, bygger med Docker i stället"
  gcloud auth configure-docker "${REGION}-docker.pkg.dev" --quiet
  docker build -t "$IMAGE" .
  docker push "$IMAGE"
fi

echo "== Hemligheter"
SECRETS=""
add_secret() {  # env-namn, secret-namn
  if gcloud secrets describe "$2" >/dev/null 2>&1; then
    SECRETS="${SECRETS:+$SECRETS,}$1=$2:latest"
  fi
}
add_secret SHOPIFY_ACCESS_TOKEN "$TOKEN_SECRET"
add_secret SHOPIFY_CLIENT_ID shopify-client-id
add_secret SHOPIFY_CLIENT_SECRET shopify-client-secret
add_secret SUPABASE_DB_URL supabase-db-url
[ -n "$SECRETS" ] || { echo "Inga hemligheter hittades i Secret Manager, se README."; exit 1; }

echo "== Cloud Run Job"
ENV_VARS="SHOPIFY_SHOP_DOMAIN=${SHOPIFY_SHOP_DOMAIN},SINKS=${SINKS},BQ_PROJECT=${PROJECT_ID},BQ_DATASET=${BQ_DATASET},BQ_LOCATION=${BQ_LOCATION}"
if gcloud run jobs describe "$JOB" --region "$REGION" >/dev/null 2>&1; then
  ACTION=update
else
  ACTION=create
fi
gcloud run jobs "$ACTION" "$JOB" --region "$REGION" --image "$IMAGE" \
  --service-account "$SA" --set-env-vars "$ENV_VARS" --set-secrets "$SECRETS" \
  --task-timeout 3600 --max-retries 1 --memory 1Gi

echo "== Schemaläggning"
gcloud run jobs add-iam-policy-binding "$JOB" --region "$REGION" \
  --member "serviceAccount:$SA" --role roles/run.invoker >/dev/null
URI="https://run.googleapis.com/v2/projects/${PROJECT_ID}/locations/${REGION}/jobs/${JOB}:run"
if gcloud scheduler jobs describe "$JOB" --location "$SCHEDULER_REGION" >/dev/null 2>&1; then
  gcloud scheduler jobs update http "$JOB" --location "$SCHEDULER_REGION" --schedule "$SCHEDULE" \
    --uri "$URI" --http-method POST --oauth-service-account-email "$SA"
else
  gcloud scheduler jobs create http "$JOB" --location "$SCHEDULER_REGION" --schedule "$SCHEDULE" \
    --time-zone "Europe/Stockholm" --uri "$URI" --http-method POST --oauth-service-account-email "$SA"
fi

echo "Klart. Första körningen (full backfill): gcloud run jobs execute $JOB --region $REGION --wait"
