"""Kommandorad: `shopify-sync run` och `shopify-sync print-ddl`."""

from __future__ import annotations

import argparse
import logging
import sys

from .config import ConfigError, ShopifyConfig, SyncConfig


def _run(args: argparse.Namespace) -> int:
    from .shopify_client import ShopifyClient
    from .sinks import build_sinks
    from .sync import sync_entity

    cfg = SyncConfig.from_env()
    entities = tuple(args.entities.split(",")) if args.entities else cfg.entities
    client = ShopifyClient(ShopifyConfig.from_env())
    sinks = build_sinks(cfg.sinks)
    try:
        for sink in sinks:
            sink.ensure_tables()
        for entity in entities:
            sync_entity(client, sinks, entity, cfg, full=args.full)
    finally:
        for sink in sinks:
            sink.close()
    return 0


def _print_ddl(args: argparse.Namespace) -> int:
    if args.target == "postgres":
        from .sinks.postgres_sink import ddl

        sys.stdout.write(ddl(args.schema))
    else:
        from .schema import ALL_TABLES, BQ_TYPES

        for table in ALL_TABLES.values():
            cols = ",\n".join(
                f"  `{c.name}` {BQ_TYPES[c.type]}{' NOT NULL' if c.required else ''}"
                for c in table.columns
            )
            extra = ""
            if table.partition_by:
                extra += f"\nPARTITION BY DATE(`{table.partition_by}`)"
            if table.cluster_by:
                extra += "\nCLUSTER BY " + ", ".join(f"`{c}`" for c in table.cluster_by)
            sys.stdout.write(
                f"CREATE TABLE IF NOT EXISTS `{args.schema}.{table.name}` (\n{cols}\n){extra};\n\n"
            )
    return 0


def _authorize(args: argparse.Namespace) -> int:
    import os

    from .authorize import OAuthFlow, serve, store_in_file, store_in_secret_manager

    import getpass

    client_id = os.environ.get("SHOPIFY_CLIENT_ID") or input("Client ID: ").strip()
    # getpass visar inte det som klistras in.
    client_secret = os.environ.get("SHOPIFY_CLIENT_SECRET") or getpass.getpass("Client secret (syns inte): ").strip()
    if not client_id or not client_secret:
        raise ConfigError("Client ID och Client secret krävs.")
    if args.secret_file:
        store = lambda token: store_in_file(token, args.secret_file)  # noqa: E731
    else:
        store = lambda token: store_in_secret_manager(token, args.secret, args.project)  # noqa: E731

    flow = OAuthFlow(args.shop, client_id, client_secret, args.base_url, args.scopes, store)
    print(f"\nApp URL (ange i appens konfiguration):      {args.base_url.rstrip('/')}/")
    print(f"Redirect URL (ange i appens konfiguration): {flow.redirect_uri}")
    print("\nInstallera sedan appen i butiken via installationslänken, eller öppna:")
    print(f"  {args.base_url.rstrip('/')}/\n")
    serve(flow, args.port)
    target = args.secret_file or f"Secret Manager: {args.secret} ({args.project})"
    print(f"\nToken sparad i {target}. Beviljade scopes: {flow.granted_scopes}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="shopify-sync")
    parser.add_argument("--log-level", default="INFO")
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="Synka Shopify till konfigurerade sinks.")
    run.add_argument("--entities", help="Kommaseparerat, t.ex. orders,products. Default: ENTITIES.")
    run.add_argument("--full", action="store_true", help="Ignorera vattenmärke och hämta allt från SYNC_START_DATE.")
    run.set_defaults(func=_run)

    ddl = sub.add_parser("print-ddl", help="Skriv ut tabellschemat som SQL.")
    ddl.add_argument("target", choices=["postgres", "bigquery"])
    ddl.add_argument("--schema", default="shopify", help="Postgres-schema eller BigQuery-dataset.")
    ddl.set_defaults(func=_print_ddl)

    auth = sub.add_parser("authorize", help="Installera appen via OAuth och spara en offline-token.")
    auth.add_argument("--shop", required=True, help="t.ex. gorilla-sports.myshopify.com")
    auth.add_argument("--base-url", required=True, help="Publik https-adress till den här datorn, t.ex. Cloud Shell Web Preview.")
    auth.add_argument("--port", type=int, default=8080)
    auth.add_argument("--scopes", default=None, help="Kommaseparerade scopes. Default: läsbehörigheterna jobbet behöver.")
    auth.add_argument("--project", default="gorilla-sports-data", help="GCP-projekt för Secret Manager.")
    auth.add_argument("--secret", default="shopify-access-token", help="Namn på hemligheten.")
    auth.add_argument("--secret-file", help="Spara i en lokal fil (0600) i stället för Secret Manager.")
    auth.set_defaults(func=_authorize)

    args = parser.parse_args(argv)
    if getattr(args, "scopes", "x") is None:
        from .authorize import DEFAULT_SCOPES

        args.scopes = DEFAULT_SCOPES
    logging.basicConfig(
        level=args.log_level.upper(),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    try:
        return args.func(args)
    except ConfigError as exc:
        logging.error("%s", exc)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
