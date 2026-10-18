#!/usr/bin/env bash
# Driftsätter datainsamlingen som Cloud Run Job som körs varje morgon 05:30 svensk tid:
# GA4 (landningssidor och kanaler), Google Ads (kampanjer och produkter) och Meta-annonser till BigQuery.
# De senaste 30 dagarna ersätts varje gång, eftersom konverteringar revideras i efterhand.
# Använder samma image som site-audit (bygg först med deploy/site_audit_job.sh, eller ange IMAGE).
#
#   PROJECT_ID=gorilla-sports-data IMAGE=<image> ./deploy/data_refresh_job.sh
#
# Hemligheter (Secret Manager, skapas av David direkt i Google Cloud, aldrig i chatten):
#   google-ads-developer-token  -> env GOOGLE_ADS_DEVELOPER_TOKEN
#   meta-access-token           -> env META_ACCESS_TOKEN
# Tjänstkontot måste dessutom läggas till som användare i Google Ads-kontona och som läsare i GA4.
set -euo pipefail

: "${PROJECT_ID:?Sätt PROJECT_ID}"
REGION="${REGION:-europe-north1}"
SCHEDULER_REGION="${SCHEDULER_REGION:-europe-west1}"
JOB="${JOB:-data-refresh}"
SA="${SA:-shopify-sync@${PROJECT_ID}.iam.gserviceaccount.com}"
SCHEDULE="${SCHEDULE:-30 5 * * *}"
SITE="${SITE:-gorillasports-se}"
DAYS="${DAYS:-30}"
SECRET_ENV="${SECRET_ENV:-GOOGLE_ADS_DEVELOPER_TOKEN=google-ads-developer-token,META_ACCESS_TOKEN=meta-access-token}"

gcloud config set project "$PROJECT_ID" >/dev/null
: "${IMAGE:?Sätt IMAGE till imagen som site-audit-jobbet använder (gcloud run jobs describe site-audit --region $REGION)}"

SECRETS=""
IFS=',' read -ra PAIRS <<< "$SECRET_ENV"
for pair in "${PAIRS[@]}"; do
  secret="${pair#*=}"
  if gcloud secrets describe "$secret" >/dev/null 2>&1; then
    SECRETS="${SECRETS:+$SECRETS,}${pair%%=*}=${secret}:latest"
  else
    echo "Varning: hemligheten '$secret' finns inte än. Källan som behöver den rapporteras som misslyckad tills den läggs in."
  fi
done

ARGS="--config,/app/sites.toml,refresh,--site,${SITE},--days,${DAYS}"
if gcloud run jobs describe "$JOB" --region "$REGION" >/dev/null 2>&1; then ACTION=update; else ACTION=create; fi
gcloud run jobs "$ACTION" "$JOB" --region "$REGION" --image "$IMAGE" --service-account "$SA" \
  --command site-audit --args="$ARGS" ${SECRETS:+--set-secrets "$SECRETS"} \
  --task-timeout 3600 --max-retries 0 --memory 1Gi --cpu 1

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
echo "Skapa vyerna:    sed 's/PROJ/${PROJECT_ID}/g' sql/growth/views.sql | bq query --use_legacy_sql=false"
