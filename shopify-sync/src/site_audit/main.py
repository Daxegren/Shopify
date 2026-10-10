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

        write_action_files(run.findings, run.crawl, d)
        print(f"{name}: {summary['total']} fynd ({summary['by_severity']}) -> {d}")
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


def cmd_backfill(args) -> int:
    from datetime import timedelta

    from . import google_api as g

    site = _site(args)
    store = _store(site)
    end = date.today() - timedelta(days=3)  # GSC-data är slutgiltig efter ca 3 dagar
    start = date.fromisoformat(args.since) if args.since else end - timedelta(days=args.days)
    if args.source == "gsc":
        if not site.gsc_property:
            raise ConfigError("gsc_property saknas i konfigurationen (t.ex. sc-domain:gorillasports.se).")
        session = g.authorized_session([g.GSC_SCOPE])
        rows = g.gsc_rows(session, site.gsc_property, start, end, with_query=args.queries)
        slug = site.name.replace("-", "_")
        table = args.table or (f"gsc_api_url_query_{slug}" if args.queries else f"gsc_api_url_{slug}")
        n = g.load_rows(store, table, g.GSC_SCHEMA, rows, ("data_date", start, end))
    else:
        if not site.ga4_property_id:
            raise ConfigError("ga4_property_id saknas i konfigurationen.")
        session = g.authorized_session([g.GA4_SCOPE])
        table = args.table or f"ga4_landing_daily_{site.name.replace('-', '_')}"
        n = g.load_rows(store, table, g.GA4_SCHEMA, g.ga4_rows(session, site.ga4_property_id, start, end), ("d", start, end))
    print(f"{n} rader laddade till {store.dataset}.{table} ({start} – {end})")
    return 0


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
    b.add_argument("source", choices=["gsc", "ga4"])
    b.add_argument("--site", required=True)
    b.add_argument("--days", type=int, default=480, help="Antal dagar bakåt (GSC max ca 16 mån)")
    b.add_argument("--since", help="Startdatum i stället för --days")
    b.add_argument("--queries", action="store_true", help="GSC: även sökfraser (större tabell)")
    b.add_argument("--table", help="Måltabell i site_audit-datasetet")
    b.set_defaults(func=cmd_backfill)

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
