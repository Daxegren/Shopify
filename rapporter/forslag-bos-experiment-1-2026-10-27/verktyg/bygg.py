# Bygger alla leveransfiler till experiment 1 på BOS. Läser bara lokala filer (inga anrop mot Shopify, inga skrivningar).
# Kör: python3 verktyg/bygg.py   (från mappen forslag-bos-experiment-1-2026-10-27)
import os, re, json, csv, math, statistics, collections
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
ORIG = '/home/user/Shopify/rapporter/shopify-original-2026-10-27'
import kohortval as kv
from utkast_data import D
from utkast_justeringar import FIX
SUF = ""   # temat lägger själv till " – BEST OF SPORTS" (snippets/doc-head-core.liquid), se plan.md. seo.title får därför vara högst 43 tecken så att den renderade titeln blir högst 60.
GID = "gid://shopify/Product/"

T = [a for a, b, l in kv.pairs]; K = [b for a, b, l in kv.pairs]
pairinfo = {}
for n, (a, b, l) in enumerate(kv.pairs, 1):
    pairinfo[a['id']] = (n, l); pairinfo[b['id']] = (n, l)

# ---- kohorter.csv
def rad(x, koh):
    pid = x['id']
    return [pid, x['handle'], f"https://bestofsports.se/products/{x['handle']}", x['vendor'], x['ptype'], x['price'], x['band'], x['sub'],
            koh, pairinfo[pid][0], pairinfo[pid][1], '', '', x['inv'], x['desc_words'], x['title']]
with open(os.path.join(OUT, 'kohorter.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['produkt_id', 'handle', 'url_se', 'tillverkare', 'typ', 'pris_sek_lagsta_variant', 'prisband', 'undertyp_nyckelord',
                'kohort', 'par_nr', 'matchningsniva', 'seo_title_nu', 'seo_description_nu', 'lager_2026-10-25', 'beskrivning_ord_2026-10-25', 'produkttitel'])
    for x in sorted(T, key=lambda x: int(x['id'])): w.writerow(rad(x, 'T'))
    for x in sorted(K, key=lambda x: int(x['id'])): w.writerow(rad(x, 'K'))

# ---- originaler (alla i T och K). Butiken svarade seo.title = null och seo.description = null för samtliga (se Täckning i plan.md).
orig = {"hamtad": "2026-10-27", "kalla": "Shopify Admin GraphQL, products(query: status:active AND product_type:'Konditionsträning & Fitness'), fälten seo{title description}, läst via produktlistan i 14 sidor (före skrivning); butiken svarade null för båda fälten på alla produkter nedan",
        "att_kontrollera_fore_skrivning": "kör verktyg/forkontroll.graphql för samma id:n och jämför mot den här filen; stoppa om något fält inte längre är null",
        "produkter": {}}
for koh, S in (('T', T), ('K', K)):
    for x in sorted(S, key=lambda x: int(x['id'])):
        assert kv.live[x['id']][1] == '-', x['id']
        orig["produkter"][GID + x['id']] = {"handle": x['handle'], "kohort": koh, "seo": {"title": None, "description": None}}
os.makedirs(ORIG, exist_ok=True)
json.dump(orig, open(os.path.join(ORIG, 'bos-experiment-1-originaler.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ---- utkast
Tid = {x['id'] for x in T}
BAN = ['upptäck', 'perfekt för dig', 'i dagens snabba', 'höj din', 'nästa nivå', 'oavsett om', 'toppkvalitet', 'unik', 'revolutionerande', '!']
HALSA = re.compile(r'protein|vitamin|kreatin|aminosyr|koffein|energi|fettförbr|viktminsk|rehab|smärta|läk|hälsa|terap|bota|förebygg', re.I)
utkast = []; fel = []
for (id_, h, t, d, m, f) in D:
    fx = FIX.get(id_, {}); t = fx.get('t', t); d = fx.get('d', d)
    st = t + SUF
    assert id_ in Tid, id_ + ' ej i T'
    assert kv.live[id_][1] == '-'
    x = next(z for z in T if z['id'] == id_); assert x['handle'] == h, (id_, x['handle'], h)
    if len(st) > 43 or not 130 <= len(d) <= 155: fel.append((id_, 'langd', len(st), len(d)))
    for b in BAN:
        if b in (st + d).lower(): fel.append((id_, 'fras', b))
    if HALSA.search(st + d): fel.append((id_, 'halsa', HALSA.search(st + d).group(0)))
    src = (f + ' ' + x['title']).replace('×', 'x')
    for n in re.findall(r'\d+(?:,\d+)?', d + ' ' + t):
        if n not in src: fel.append((id_, 'siffra_saknas_i_kalla', n))
    utkast.append({"id": GID + id_, "handle": h, "kohort": "T",
                   "seo_title_fore": None, "seo_title_efter": st, "seo_description_fore": None, "seo_description_efter": d,
                   "motivering": m, "källfakta": f, "längd_titel": len(st), "längd_beskrivning": len(d)})
assert not fel, fel
assert len({u['seo_title_efter'] for u in utkast}) == len(utkast) and len({u['seo_description_efter'] for u in utkast}) == len(utkast)
json.dump(utkast, open(os.path.join(OUT, 'utkast_fore_efter.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# ---- batchar (högst 20 alias per dokument)
def q(s): return json.dumps(s, ensure_ascii=False)
def doc(items, namn, restore=False):
    rows = []
    for i, (gid, ti, de) in enumerate(items, 1):
        t_ = 'null' if ti is None else q(ti); d_ = 'null' if de is None else q(de)
        rows.append(f"  p{i}: productUpdate(product: {{id: {q(gid)}, seo: {{title: {t_}, description: {d_}}}}}) {{\n    product {{ id handle seo {{ title description }} }}\n    userErrors {{ field message }}\n  }}")
    return f"# {namn}. Högst 20 alias. Körs bara av samordnaren efter Davids ja. Läs tillbaka resultatet och jämför mot utkast_fore_efter.json.\nmutation {namn.split()[0].replace('-','_')} {{\n" + "\n".join(rows) + "\n}\n"
os.makedirs(os.path.join(OUT, 'utfor_batchar'), exist_ok=True); os.makedirs(os.path.join(OUT, 'aterstall_batchar'), exist_ok=True)
for fn in os.listdir(os.path.join(OUT, 'utfor_batchar')): os.remove(os.path.join(OUT, 'utfor_batchar', fn))
for fn in os.listdir(os.path.join(OUT, 'aterstall_batchar')): os.remove(os.path.join(OUT, 'aterstall_batchar', fn))
for n in range(0, len(utkast), 20):
    part = utkast[n:n + 20]; nr = n // 20 + 1
    open(os.path.join(OUT, 'utfor_batchar', f'utfor-{nr:02d}.graphql'), 'w', encoding='utf-8').write(
        doc([(u['id'], u['seo_title_efter'], u['seo_description_efter']) for u in part], f"Utfor{nr:02d} (batch {nr}, {len(part)} produkter)"))
    open(os.path.join(OUT, 'aterstall_batchar', f'aterstall-{nr:02d}.graphql'), 'w', encoding='utf-8').write(
        doc([(u['id'], orig['produkter'][u['id']]['seo']['title'], orig['produkter'][u['id']]['seo']['description']) for u in part], f"Aterstall{nr:02d} (batch {nr}, {len(part)} produkter, original)"))
# fix: kanariebatch med en enda produkt
u0 = utkast[0]
open(os.path.join(OUT, 'utfor_batchar', 'utfor-00-kanarie.graphql'), 'w', encoding='utf-8').write(doc([(u0['id'], u0['seo_title_efter'], u0['seo_description_efter'])], "Utfor00 (kanarie, 1 produkt)"))
open(os.path.join(OUT, 'aterstall_batchar', 'aterstall-00-kanarie.graphql'), 'w', encoding='utf-8').write(doc([(u0['id'], None, None)], "Aterstall00 (kanarie, 1 produkt, original = null)"))
ids = [u['id'] for u in utkast]
# kontroll-/inläsningsfråga
fk = "# Läsfråga (ingen skrivning): läs seo för de produkter ett batch rör. Byt listan mot id:n ur batchen.\nquery Forkontroll {\n  nodes(ids: " + json.dumps(ids[:20]) + ") {\n    ... on Product { id handle status seo { title description } }\n  }\n}\n"
open(os.path.join(OUT, 'utfor_batchar', 'forkontroll-01.graphql'), 'w', encoding='utf-8').write(fk)
open(os.path.join(HERE, 'forkontroll.graphql'), 'w', encoding='utf-8').write("# Läsfråga: kör för alla id:n i originalfilen (50 per anrop) och jämför seo mot originalen. Ingen skrivning.\nquery Forkontroll($ids: [ID!]!) {\n  nodes(ids: $ids) {\n    ... on Product { id handle status seo { title description } }\n  }\n}\n")

# ---- baseline.sql
rows_sql = ",\n    ".join(f"STRUCT('{'T' if x['id'] in Tid else 'K'}' AS kohort, {q(x['handle'])} AS handle)" for x in sorted(T + K, key=lambda x: int(x['id'])))
sql = f"""-- Baslinje för experiment 1 (BOS, SEO-titel och metabeskrivning på produkter i Konditionsträning & Fitness).
-- Hämtar senaste 28 dagarnas klick, visningar och position per produkt-URL för behandlingsgruppen (T) och kontrollgruppen (K).
--
-- OBEKRÄFTAD KÄLLA: tabellen gorilla-sports-data.site_audit.gsc_combined_bestofsports_se är en vy (se shopify-sync/sql/audit/views_sources_bestofsports.sql).
-- Den måste verifieras med scripts/kontrollera_datakallor.sh (rad "Search Console se") INNAN baslinjen tas: tabellen ska finnas, ha rader och senaste data_date högst 4 dagar gammal.
-- Bulkexporten startade 2026-10-22; äldre dagar kommer från API-historiken (gsc_api_url_bestofsports_se) om den är hämtad.
-- Kör (Cloud Shell): bq query --use_legacy_sql=false --max_rows=1000 < baseline.sql        (ersätt inget; projektet står redan i tabellnamnet)
--
-- Fönstret slutar 3 dagar bakåt (Search Console är slutgiltig efter cirka tre dagar) och är 28 dagar långt. Ändra SLUT för att låsa baslinjen till ett fast datum.

DECLARE SLUT DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 3 DAY);
DECLARE START DATE DEFAULT DATE_SUB(SLUT, INTERVAL 27 DAY);

-- 1) Kontroll av källan. Om antal_rader är 0 eller senaste_dag är gammal: avbryt, ta inte baslinjen.
SELECT 'kallkontroll' AS del, COUNT(*) AS antal_rader, MIN(data_date) AS forsta_dag, MAX(data_date) AS senaste_dag,
       COUNT(DISTINCT url) AS antal_url, SUM(clicks) AS klick, SUM(impressions) AS visningar
FROM `gorilla-sports-data.site_audit.gsc_combined_bestofsports_se`
WHERE data_date BETWEEN START AND SLUT;

-- 2) Kohortlistan (216 + 216 produkter, ur kohorter.csv). Join sker på handle ur sökvägen /products/<handle>.
CREATE TEMP TABLE kohort AS
SELECT * FROM UNNEST([
    {rows_sql}
]);

CREATE TEMP TABLE per_url AS
SELECT k.kohort, k.handle,
       IFNULL(SUM(g.clicks), 0) AS klick,
       IFNULL(SUM(g.impressions), 0) AS visningar,
       SAFE_DIVIDE(SUM(g.sum_position), SUM(g.impressions)) + 1 AS position,   -- sum_position är 0-baserad i exporten, därav +1 (samma som sql/analys/bos/12)
       COUNT(DISTINCT g.data_date) AS dagar_med_visning
FROM kohort k
LEFT JOIN `gorilla-sports-data.site_audit.gsc_combined_bestofsports_se` g
  ON REGEXP_EXTRACT(g.url, r'^https?://(?:www\\.)?bestofsports\\.se/products/([^/?#]+)') = k.handle
 AND g.data_date BETWEEN START AND SLUT
GROUP BY 1, 2;

-- 3) Sammanfattning per kohort. Används för att se om T och K är lika före start. Stor skillnad = dra om urvalet med trafik som extra stratum (se plan.md).
SELECT kohort, COUNT(*) AS produkter, COUNTIF(visningar > 0) AS med_visningar, COUNTIF(klick > 0) AS med_klick,
       SUM(visningar) AS visningar, SUM(klick) AS klick, ROUND(SAFE_DIVIDE(SUM(klick), SUM(visningar)) * 100, 2) AS ctr_pct,
       ROUND(APPROX_QUANTILES(visningar, 100)[OFFSET(50)], 1) AS median_visningar_per_url, MAX(visningar) AS max_visningar_en_url
FROM per_url GROUP BY kohort ORDER BY kohort;

-- 4) Per URL (spara resultatet som fil/tabell; detta är baslinjen som utvärderingen jämför mot).
SELECT kohort, handle, klick, visningar, ROUND(position, 1) AS position, dagar_med_visning
FROM per_url ORDER BY kohort, visningar DESC;

-- 5) Test av att kontrollen kan misslyckas: antal kohortprodukter vars handle inte hittas alls i tabellen (utan visning under fönstret är normalt, men 432 av 432 betyder att joinen eller URL-formen är fel).
SELECT COUNTIF(visningar = 0) AS utan_visning, COUNT(*) AS totalt FROM per_url;
"""
open(os.path.join(OUT, 'baseline.sql'), 'w', encoding='utf-8').write(sql)

# ---- sammanställning till plan.md (skrivs ut)
def bal(f):
    ct = collections.Counter(f(x) for x in T); ck = collections.Counter(f(x) for x in K)
    return {k_: (ct[k_], ck[k_]) for k_ in sorted(set(ct) | set(ck))}
print('T', len(T), 'K', len(K), 'pool', len(kv.pool), 'ej parade', len(kv.left), 'nivå', collections.Counter(l for _, _, l in kv.pairs))
print('vendor', bal(lambda x: x['vendor'])); print('band', bal(lambda x: x['band'])); print('sub', bal(lambda x: x['sub']))
for nm, S in (('T', T), ('K', K)):
    ps = sorted(x['price'] for x in S); print(nm, 'pris medel', round(statistics.mean(ps)), 'median', statistics.median(ps), 'min', ps[0], 'max', ps[-1], 'beskr median', statistics.median(int(x['desc_words']) for x in S))
print('utkast', len(utkast), 'titel', min(u['längd_titel'] for u in utkast), max(u['längd_titel'] for u in utkast), 'besk', min(u['längd_beskrivning'] for u in utkast), max(u['längd_beskrivning'] for u in utkast))
print('utkast per undertyp', collections.Counter(next(z for z in T if z['id'] == u['id'][len(GID):])['sub'] for u in utkast))
print('batchar', sorted(os.listdir(os.path.join(OUT, 'utfor_batchar'))))
