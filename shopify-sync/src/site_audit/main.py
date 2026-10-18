"""Kommandorad för genomlysning: site-audit <kommando>.

  run         Full genomlysning (admin + crawl), sparar lokalt och valfritt i BigQuery
  page        Snabbanalys av en enskild URL
  diff        Jämför två lokala körningar
  log-change  Registrera en ändring för senare effektmätning
  impact      Före/efter-jämförelse för en sidgrupp (GSC, GA4, Shopify)
  trend       Klick och visningar per sidgrupp över tid
  sql         Skriv ut SQL för effekt/trend (för egen körning i BigQuery)
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from datetime import date
from pathlib import Path

from .config import ConfigError, SiteConfig, load_sites


def _site(args) -> SiteConfig:
    sites = load_sites(args.config)
    if args.site not in sites:
        raise ConfigError(f"Sajten '{args.site}' finns inte i {args.config}. Tillgängliga: {', '.join(sites)}")
    return sites[args.site]


def _store(site: SiteConfig):
    from .storage import BigQueryStore

    if not site.bq_project:
        raise ConfigError("bq_project saknas i konfigurationen.")
    return BigQueryStore(site.bq_project, site.bq_dataset)


def upload_dir(d: Path, uri: str, site: str) -> str:
    """Laddar upp körningens filer till gs://bucket/prefix/<sajt>/<körning>/ och till .../<sajt>/latest/."""
    from google.cloud import storage

    if not uri.startswith("gs://"):
        raise ConfigError("--upload ska vara en gs://-adress")
    bucket_name, _, prefix = uri[5:].partition("/")
    bucket = storage.Client().bucket(bucket_name)
    base = "/".join(x for x in (prefix.strip("/"), site) if x)
    for f in sorted(Path(d).iterdir()):
        if f.is_file():
            for folder in (d.name, "latest"):
                bucket.blob(f"{base}/{folder}/{f.name}").upload_from_filename(str(f))
    return f"gs://{bucket_name}/{base}/{d.name}/"


def split_gs_uri(uri: str) -> tuple[str, str]:
    if not uri.startswith("gs://"):
        raise ConfigError("--upload ska vara en gs://-adress")
    bucket, _, prefix = uri[5:].partition("/")
    return bucket, prefix.strip("/")


def upload_report(markdown: str, uri: str, site: str, day: date) -> str:
    """Sparar veckorapporten som <prefix>/<sajt>/vecka-<datum>.md och som .../latest.md. Ger adressen till den dagliga filen."""
    from google.cloud import storage

    bucket_name, prefix = split_gs_uri(uri)
    bucket = storage.Client().bucket(bucket_name)
    base = "/".join(x for x in (prefix, site) if x)
    for name in (f"vecka-{day.isoformat()}.md", "latest.md"):
        bucket.blob(f"{base}/{name}").upload_from_string(markdown, content_type="text/markdown; charset=utf-8")
    return f"gs://{bucket_name}/{base}/vecka-{day.isoformat()}.md"


def cmd_run(args) -> int:
    from .audit import run_audit, save_local
    from .report import to_html, to_markdown

    sites = load_sites(args.config)
    names = list(sites) if args.site == "all" else [args.site]
    for name in names:
        site = sites[name]
        if args.max_pages:
            site.crawl.max_pages = args.max_pages
        store = _store(site) if (args.bigquery or args.search_data) else None
        run = run_audit(site, crawl=not args.no_crawl, admin=not args.no_admin,
                        search_store=store if args.search_data else None, psi_per_type=args.psi)
        d = save_local(run, args.out)
        summary = run.summary()
        (d / "report.md").write_text(to_markdown(summary, run.findings))
        (d / "report.html").write_text(to_html(summary, run.findings))
        from .actions import write_action_files

        clicks = {k: v["clicks"] for k, v in run.search.by_path.items()} if run.search else None
        write_action_files(run.findings, run.crawl, d, clicks)
        print(f"{name}: {summary['total']} fynd ({summary['by_severity']}) -> {d}")
        if args.upload:
            print(f"{name}: filer uppladdade till {upload_dir(d, args.upload, name)}")
        if args.bigquery:
            store.save_run(run)
            print(f"{name}: sparad i BigQuery {site.bq_project}.{site.bq_dataset}")
    return 0


def cmd_page(args) -> int:
    from urllib.parse import urlsplit

    from .fetch import Fetcher
    from .html_parse import parse_page

    f = Fetcher("SiteAuditBot/0.1", 5)
    res = f.fetch(args.url)
    out = {"status": res.status, "final_url": res.final_url, "hops": [h.__dict__ for h in res.hops]}
    if res.status == 200 and res.is_html:
        out["facts"] = parse_page(res.final_url, res.body, urlsplit(res.final_url).netloc.lower()).to_dict()
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


def cmd_diff(args) -> int:
    from .diff import describe_diff, diff_runs, load_findings

    print(describe_diff(diff_runs(load_findings(args.old), load_findings(args.new))))
    return 0


def _pattern(site: SiteConfig, args) -> tuple[str, str]:
    if args.group:
        g = next((g for g in site.page_groups if g.name == args.group), None)
        if not g:
            raise ConfigError(f"Sidgruppen '{args.group}' finns inte. Tillgängliga: {[g.name for g in site.page_groups]}")
        return g.pattern, g.name
    if not args.pattern:
        raise ConfigError("Ange --group eller --pattern.")
    return args.pattern, args.pattern


def cmd_log_change(args) -> int:
    site = _site(args)
    pattern, label = (_pattern(site, args) if (args.group or args.pattern) else (None, None))
    cid = _store(site).log_change(site.name, args.date, args.description, pattern, args.group)
    print(f"Ändring registrerad: {cid}")
    return 0


def cmd_impact(args) -> int:
    from .impact import run_impact

    site = _site(args)
    pattern, label = _pattern(site, args)
    result, text = run_impact(_store(site), site, pattern, date.fromisoformat(args.date), args.days, label)
    print(text)
    if args.json:
        print(json.dumps(result, indent=2, default=str))
    return 0


def cmd_trend(args) -> int:
    from .impact import trend_sql

    site = _site(args)
    if not site.gsc_table:
        raise ConfigError("gsc_table saknas i konfigurationen.")
    store = _store(site)
    sql = trend_sql(site.gsc_table, [(g.name, g.pattern) for g in site.page_groups], args.grain)
    rows = store.query(sql, [store.bq.ScalarQueryParameter("since", "DATE", date.fromisoformat(args.since))])
    for r in rows:
        print(f"{r['period']}  {r['page_group']:<24} klick {r['clicks']:>8}  visningar {r['impressions']:>10}  pos {r['avg_position'] or 0:.1f}")
    return 0


SOURCES = ("gsc", "ga4", "ga4-kanal", "google-ads", "google-ads-produkter", "meta-ads")


def fetch_source(site: SiteConfig, store, source: str, start: date, end: date, queries: bool = False,
                 table: str | None = None) -> tuple[int, str]:
    """Hämtar en källa för perioden och ersätter den i BigQuery. Ger (antal rader, måltabell)."""
    from . import ads_api as a
    from . import google_api as g

    slug, key = site.slug, site.table_key  # Search Console är per domän; GA4 och annonser per butik
    if source == "gsc":
        if not site.gsc_property:
            raise ConfigError("gsc_property saknas i konfigurationen (t.ex. sc-domain:gorillasports.se).")
        session = g.authorized_session([g.GSC_SCOPE])
        rows = g.gsc_rows(session, site.gsc_property, start, end, with_query=queries)
        table = table or (f"gsc_api_url_query_{slug}" if queries else f"gsc_api_url_{slug}")
        return g.load_rows(store, table, g.GSC_SCHEMA, rows, ("data_date", start, end)), table
    if source in ("ga4", "ga4-kanal"):
        if not site.ga4_property_id:
            raise ConfigError("ga4_property_id saknas i konfigurationen.")
        session = g.authorized_session([g.GA4_SCOPE])
        if source == "ga4-kanal":
            table = table or f"ga4_channel_daily_{key}"
            rows, schema = g.ga4_channel_rows(session, site.ga4_property_id, start, end), g.GA4_CHANNEL_SCHEMA
        else:
            table = table or f"ga4_landing_daily_{key}"
            rows, schema = g.ga4_rows(session, site.ga4_property_id, start, end), g.GA4_SCHEMA
        return g.load_rows(store, table, schema, rows, ("d", start, end)), table
    if source in ("google-ads", "google-ads-produkter"):
        if not site.google_ads_customer_ids:
            raise ConfigError("google_ads_customer_ids saknas i konfigurationen.")
        token = os.environ.get(site.google_ads_developer_token_env)  # valfri sedan Google tog bort kravet
        session = a.google_ads_session(token, site.google_ads_login_customer_id)
        per_account = a.google_ads_product_rows if source == "google-ads-produkter" else a.google_ads_campaign_rows
        schema = a.GOOGLE_ADS_PRODUCT_SCHEMA if source == "google-ads-produkter" else a.GOOGLE_ADS_SCHEMA
        table = table or (f"google_ads_products_daily_{key}" if source == "google-ads-produkter" else f"google_ads_daily_{key}")
        rows = (r for cid in site.google_ads_customer_ids
                for r in per_account(session, cid, start, end, site.google_ads_api_version))
        return g.load_rows(store, table, schema, rows, ("d", start, end)), table
    if source == "meta-ads":
        if not site.meta_ad_account_ids:
            raise ConfigError("meta_ad_account_ids saknas i konfigurationen.")
        token = os.environ.get(site.meta_token_env)
        if not token:
            raise ConfigError(f"Meta-token saknas: sätt miljövariabeln {site.meta_token_env} (hemlighet).")
        session = a.meta_session(token)
        table = table or f"meta_ads_daily_{key}"
        rows = (r for acct in site.meta_ad_account_ids
                for r in a.meta_ads_rows(session, acct, start, end, site.meta_api_version))
        return g.load_rows(store, table, a.META_ADS_SCHEMA, rows, ("d", start, end)), table
    raise ConfigError(f"Okänd källa: {source}. Välj bland {', '.join(SOURCES)}.")


def _source_end(source: str) -> date:
    from datetime import timedelta

    # Search Console är slutgiltig efter ca 3 dagar; övriga källor har data till och med i går.
    return date.today() - timedelta(days=3 if source == "gsc" else 1)


def cmd_backfill(args) -> int:
    from datetime import timedelta

    site = _site(args)
    store = _store(site)
    end = _source_end(args.source)
    start = date.fromisoformat(args.since) if args.since else end - timedelta(days=args.days)
    n, table = fetch_source(site, store, args.source, start, end, queries=args.queries, table=args.table)
    print(f"{n} rader laddade till {store.dataset}.{table} ({start} – {end})")
    return 0


def cmd_refresh(args) -> int:
    """Nattlig hämtning: de senaste N dagarna från alla källor som är konfigurerade för sajten.

    Konverteringar revideras i efterhand, så perioden ersätts varje gång. Ett fel i en källa stoppar
    inte de andra; kommandot returnerar 1 om någon källa misslyckades, så att jobbet syns som felat."""
    from datetime import timedelta

    site = _site(args)
    store = _store(site)
    wanted = args.source or list(SOURCES)
    failed = 0
    for source in wanted:
        if source == "gsc":
            continue  # Search Console fylls av massexporten; historiken hämtas med backfill
        configured = {"ga4": site.ga4_property_id, "ga4-kanal": site.ga4_property_id,
                      "google-ads": site.google_ads_customer_ids, "google-ads-produkter": site.google_ads_customer_ids,
                      "meta-ads": site.meta_ad_account_ids}.get(source)
        if not configured:
            print(f"{source}: hoppas över (inte konfigurerad för {site.name})")
            continue
        end = _source_end(source)
        try:
            n, table = fetch_source(site, store, source, end - timedelta(days=args.days - 1), end)
            print(f"{source}: {n} rader till {store.dataset}.{table}")
        except Exception as exc:  # noqa: BLE001 - en källa får inte stoppa de andra
            failed += 1
            print(f"{source}: MISSLYCKADES: {exc}")
    return 1 if failed else 0


def cmd_growth_sql(args) -> int:
    """Skriver BigQuery-vyerna för alla butiker (growth_views = true) och portföljen. Kör inget mot BigQuery."""
    from .growth_sql import growth_sql

    sql = growth_sql(load_sites(args.config), args.portfolio_project, args.portfolio_dataset)
    if args.out:
        Path(args.out).write_text(sql)
        print(f"Skrev {args.out}")
    else:
        print(sql)
    return 0


def cmd_weekly(args) -> int:
    """Veckorapport med nyckeltal, kanaler, produkter och larm för en butik. Läser bara från BigQuery."""
    from .growth_report import build_report

    site = _site(args)
    if not site.growth_views:
        raise ConfigError(f"{site.name} har inte growth_views = true. Sätt det på butikens huvudsajt och kör growth-sql först.")
    report = build_report(_store(site), site, date.fromisoformat(args.date) if args.date else None)
    day = date.fromisoformat(args.date) if args.date else date.today()
    if args.out:
        Path(args.out).write_text(report.markdown)
        print(f"Skrev {args.out} ({len(report.alerts)} larm, varav {sum(a.level == 'hög' for a in report.alerts)} höga)")
    elif not args.upload:
        print(report.markdown)
    if args.upload:
        print("Laddade upp " + upload_report(report.markdown, args.upload, site.name, day))
    return 2 if (args.fail_on_alert and report.has_high) else 0


def cmd_sql(args) -> int:
    from . import impact

    site = _site(args)
    if args.kind == "trend":
        print(impact.trend_sql(site.gsc_table or "<gsc_table>", [(g.name, g.pattern) for g in site.page_groups]))
    elif args.kind == "gsc":
        print(impact.gsc_window_sql(site.gsc_table or "<gsc_table>"))
    elif args.kind == "ga4":
        print(impact.ga4_window_sql(site.ga4_dataset or "<ga4_dataset>"))
    else:
        print(impact.shopify_window_sql(site.shopify_dataset or "<shopify_dataset>"))
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="site-audit", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--log-level", default="INFO")
    p.add_argument("--config", default="sites.toml")
    sub = p.add_subparsers(dest="command", required=True)

    r = sub.add_parser("run", help="Full genomlysning")
    r.add_argument("--site", required=True, help="Namn i konfigurationen, eller 'all'")
    r.add_argument("--out", default="audits")
    r.add_argument("--no-crawl", action="store_true")
    r.add_argument("--no-admin", action="store_true")
    r.add_argument("--max-pages", type=int)
    r.add_argument("--bigquery", action="store_true", help="Spara körningen i BigQuery")
    r.add_argument("--search-data", action="store_true", help="Kombinera med Search Console-data i BigQuery")
    r.add_argument("--upload", metavar="GS_URI", help="Ladda upp rapport och åtgärdsfiler till Cloud Storage, t.ex. gs://bucket/audits")
    r.add_argument("--psi", type=int, default=0, metavar="N", help="Mät Core Web Vitals för N sidor per sidtyp (kräver PSI_API_KEY)")
    r.set_defaults(func=cmd_run)

    pg = sub.add_parser("page", help="Analysera en enskild URL")
    pg.add_argument("url")
    pg.set_defaults(func=cmd_page)

    d = sub.add_parser("diff", help="Jämför två körningar")
    d.add_argument("old")
    d.add_argument("new")
    d.set_defaults(func=cmd_diff)

    for name, fn in (("log-change", cmd_log_change), ("impact", cmd_impact)):
        s = sub.add_parser(name)
        s.add_argument("--site", required=True)
        s.add_argument("--date", required=True, help="Ändringsdatum, ÅÅÅÅ-MM-DD")
        s.add_argument("--group")
        s.add_argument("--pattern", help="Regex mot sökvägen, t.ex. ^/collections/konstnar")
        if name == "log-change":
            s.add_argument("--description", required=True)
        else:
            s.add_argument("--days", type=int, default=90)
            s.add_argument("--json", action="store_true")
        s.set_defaults(func=fn)

    t = sub.add_parser("trend")
    t.add_argument("--site", required=True)
    t.add_argument("--since", required=True)
    t.add_argument("--grain", default="MONTH", choices=["DAY", "WEEK", "MONTH"])
    t.set_defaults(func=cmd_trend)

    b = sub.add_parser("backfill", help="Hämta historik via Search Console API eller GA4 Data API")
    b.add_argument("source", choices=list(SOURCES), help="ga4-kanal: besök per kanal; google-ads, google-ads-produkter, meta-ads: annonsdata")
    b.add_argument("--site", required=True)
    b.add_argument("--days", type=int, default=480, help="Antal dagar bakåt (GSC max ca 16 mån)")
    b.add_argument("--since", help="Startdatum i stället för --days")
    b.add_argument("--queries", action="store_true", help="GSC: även sökfraser (större tabell)")
    b.add_argument("--table", help="Måltabell i site_audit-datasetet")
    b.set_defaults(func=cmd_backfill)

    rf = sub.add_parser("refresh", help="Hämta om de senaste dagarna från alla konfigurerade datakällor")
    rf.add_argument("--site", required=True)
    rf.add_argument("--days", type=int, default=30, help="Antal dagar som ersätts (konverteringar revideras i efterhand)")
    rf.add_argument("--source", action="append", choices=list(SOURCES), help="Begränsa till vissa källor (kan anges flera gånger)")
    rf.set_defaults(func=cmd_refresh)

    gs = sub.add_parser("growth-sql", help="Generera vyerna för tillväxtarbetet (per butik och för portföljen)")
    gs.add_argument("--out", help="Skriv till fil i stället för skärmen")
    gs.add_argument("--portfolio-project", help="Projekt för portföljvyerna (standard: första butikens projekt)")
    gs.add_argument("--portfolio-dataset", default="portfolio")
    gs.set_defaults(func=cmd_growth_sql)

    wk = sub.add_parser("weekly", help="Veckorapport och larm för en butik (läser tillväxtvyerna)")
    wk.add_argument("--site", required=True)
    wk.add_argument("--date", help="Räkna från detta datum i stället för i dag, ÅÅÅÅ-MM-DD")
    wk.add_argument("--out", help="Skriv rapporten till en fil, t.ex. rapporter/vecka-2026-10-19.md")
    wk.add_argument("--upload", metavar="GS_URI", help="Spara rapporten i Cloud Storage, t.ex. gs://bucket/weekly (skriver inte till skärmen)")
    wk.add_argument("--fail-on-alert", action="store_true", help="Avsluta med kod 2 om något larm är högt (för schemalagd körning)")
    wk.set_defaults(func=cmd_weekly)

    q = sub.add_parser("sql")
    q.add_argument("--site", required=True)
    q.add_argument("kind", choices=["trend", "gsc", "ga4", "shopify"])
    q.set_defaults(func=cmd_sql)

    args = p.parse_args(argv)
    logging.basicConfig(level=args.log_level.upper(), format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    try:
        return args.func(args)
    except ConfigError as exc:
        logging.error("%s", exc)
        return 2


if __name__ == "__main__":
    sys.exit(main())
