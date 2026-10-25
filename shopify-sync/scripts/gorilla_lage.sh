#!/usr/bin/env bash
# Läget för Gorilla Sports på en gång: fynd, omsättning, annonser på slutsålda, döda sidor, avvisade produkter, omdirigeringar.
#   cd ~/Shopify/shopify-sync && git pull origin claude/zealous-johnson-0ywddr && bash scripts/gorilla_lage.sh 2>&1 | tee ~/gorilla-lage.txt
# Bara läsning. Varje steg som saknar tabell eller behörighet hoppas över och körningen fortsätter.
set -uo pipefail
P="${PROJECT_ID:-gorilla-sports-data}"
B="${BUCKET:-${P}-site-audit}"
q() { bq query --use_legacy_sql=false --max_rows="${MAXROWS:-40}"; }
steg() { printf '\n\n######## %s\n' "$1"; }

steg "1. Jobbstatus och nyckeltal"
bash scripts/audit_status.sh || echo "(hoppades över)"

for S in gorillasports-se gorillasports-dk; do
  steg "2. Fynd i detalj: $S"
  bash scripts/audit_detaljer.sh "$S" || echo "(hoppades över)"
done

steg "3. Omdirigeringar: kritiska fynd mot vår granskade fil (gorillasports-se)"
gcloud storage cat "gs://${B}/audits/gorillasports-se/latest/findings.jsonl" \
  | python3 scripts/redirect_jamforelse.py --granskade ../rapporter/redirects_granskade.csv || echo "(hoppades över)"

steg "4. Omsättning, senaste 30 dagarna mot de 30 innan"
sed "s/PROJ/${P}/g" sql/analys/omsattning_30d.sql | q || echo "(hoppades över)"

steg "5. Annonsklick på produkter som inte går att köpa (Gorilla)"
sed -e "s/PROJ/${P}/g" -e 's/KEY/gorillasports/g' -e 's/SHOPDS/shopify/g' sql/analys/annonser_pa_slutsalda.sql | q || echo "(hoppades över)"

steg "6. Döda produktsidor med besök (gorillasports.se)"
sed -e "s/PROJ/${P}/g" -e 's/KEY/gorillasports_se/g' -e 's/HOST/gorillasports.se/g' sql/analys/doda_sidor_med_trafik.sql | q || echo "(hoppades över)"

steg "7. Avvisade produkter i Merchant Center med annonsklick eller lager"
sed -e "s/PROJ/${P}/g" -e 's/KEY/gorillasports/g' sql/analys/merchant_avvisade.sql | q || echo "(hoppades över)"

echo; echo "Klart. Klistra in ~/gorilla-lage.txt till Claude."
