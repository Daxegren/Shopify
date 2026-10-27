#!/usr/bin/env bash
# Visar för en butik vilka datatabeller som finns i BigQuery och hur färska de är. Bara läsning.
# Ett fel (tabell saknas, ingen rad, gammal data) skrivs som SAKNAS eller GAMMAL, så att en tom källa inte ser ut som OK.
#
#   bash scripts/kontrollera_datakallor.sh                 # Best of Sports (nyckel bestofsports)
#   KEY=gorillasports bash scripts/kontrollera_datakallor.sh
#   (DATAKEY, SHOPDS och MARKNADER kan skrivas över, t.ex. DATAKEY=gorillasports_dk för DK-sajtens egna tabeller)
set -uo pipefail
PROJECT_ID="${PROJECT_ID:-gorilla-sports-data}"
KEY="${KEY:-bestofsports}"
# Namnen följer sites.toml och koden i site_audit/main.py (fetch_source). Search Console-tabellerna heter <nyckel>_<marknad>. GA4-, annons- och
# Merchant-tabellerna får butikens data_key, och Gorilla saknar data_key, så där används sajtens namn (gorillasports_se). Gorillas
# Shopify-dataset heter shopify (BOS: shopify_bestofsports). Gorilla har ingen finsk domän.
case "$KEY" in
  gorillasports) DATAKEY="${DATAKEY:-gorillasports_se}"; SHOPDS="${SHOPDS:-shopify}"; MARKNADER="${MARKNADER:-se dk}" ;;
  *)             DATAKEY="${DATAKEY:-${KEY}}";            SHOPDS="${SHOPDS:-shopify_${KEY}}"; MARKNADER="${MARKNADER:-se dk fi}" ;;
esac
MAX_DAGAR="${MAX_DAGAR:-4}"

kolla() {   # namn, tabell, datumkolumn
  local namn="$1" tabell="$2" kol="$3" ut
  ut=$(bq query --use_legacy_sql=false --format=csv --quiet \
       "SELECT COUNT(*) AS n, CAST(MAX(${kol}) AS STRING) AS senaste FROM \`${PROJECT_ID}.${tabell}\`" 2>&1)
  if echo "$ut" | grep -qiE "not found|does not exist|Unrecognized name|Access Denied|error"; then
    printf '%-34s SAKNAS   (%s)\n' "$namn" "$(echo "$ut" | tail -n1 | cut -c1-90)"; return
  fi
  local rad; rad=$(echo "$ut" | tail -n1); local n="${rad%%,*}" senaste="${rad#*,}"
  if [ "${n:-0}" = "0" ]; then printf '%-34s TOM\n' "$namn"; return; fi
  local dagar; dagar=$(python3 - "$senaste" <<'PY'
import sys, datetime
s = sys.argv[1][:10]
try:
    print((datetime.date.today() - datetime.date.fromisoformat(s)).days)
except Exception:
    print(-1)
PY
)
  if [ "$dagar" -gt "$MAX_DAGAR" ] 2>/dev/null; then printf '%-34s GAMMAL   %s rader, senaste %s (%s dagar sedan)\n' "$namn" "$n" "$senaste" "$dagar"
  else printf '%-34s OK       %s rader, senaste %s\n' "$namn" "$n" "$senaste"; fi
}

echo "== Datakällor för ${KEY} (projekt ${PROJECT_ID})"
for m in $MARKNADER; do kolla "Search Console ${m}" "site_audit.gsc_combined_${KEY}_${m}" data_date; done
kolla "Search Console API-historik se" "site_audit.gsc_api_url_${KEY}_se" data_date
kolla "GA4 landningssidor" "site_audit.ga4_landing_daily_${DATAKEY}" d
kolla "GA4 kanaler" "site_audit.ga4_channel_daily_${DATAKEY}" d
kolla "Shopify ordrar" "${SHOPDS}.orders" created_at
kolla "Google Ads per dag" "site_audit.google_ads_daily_${DATAKEY}" d
kolla "Google Ads per produkt" "site_audit.google_ads_products_daily_${DATAKEY}" d
kolla "Merchant Center" "site_audit.merchant_products_${DATAKEY}" d
echo; echo "Kolumnnamnen (data_date, d, created_at) kan skilja; ett 'SAKNAS' med texten Unrecognized name betyder rätt tabell men annat datumfält."
