"""Konfiguration via miljövariabler, så att samma image körs i Cloud Run, på en VM eller lokalt."""

from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone


class ConfigError(RuntimeError):
    pass


def _env(name: str, default: str | None = None) -> str | None:
    value = os.environ.get(name, default)
    return value.strip() if isinstance(value, str) else value


def _require(name: str) -> str:
    value = _env(name)
    if not value:
        raise ConfigError(f"Miljövariabeln {name} saknas.")
    return value


@dataclass(frozen=True)
class ShopifyConfig:
    shop_domain: str
    api_version: str
    access_token: str | None
    client_id: str | None
    client_secret: str | None

    @classmethod
    def from_env(cls) -> "ShopifyConfig":
        domain = _require("SHOPIFY_SHOP_DOMAIN")
        domain = domain.removeprefix("https://").removesuffix("/")
        token = _env("SHOPIFY_ACCESS_TOKEN")
        client_id = _env("SHOPIFY_CLIENT_ID")
        client_secret = _env("SHOPIFY_CLIENT_SECRET")
        if not token and not (client_id and client_secret):
            raise ConfigError(
                "Ange antingen SHOPIFY_ACCESS_TOKEN eller både SHOPIFY_CLIENT_ID och "
                "SHOPIFY_CLIENT_SECRET."
            )
        return cls(
            shop_domain=domain,
            api_version=_env("SHOPIFY_API_VERSION", "2026-07"),
            access_token=token,
            client_id=client_id,
            client_secret=client_secret,
        )


@dataclass(frozen=True)
class BigQueryConfig:
    project: str
    dataset: str
    location: str

    @classmethod
    def from_env(cls) -> "BigQueryConfig":
        return cls(
            project=_require("BQ_PROJECT"),
            dataset=_env("BQ_DATASET", "shopify"),
            location=_env("BQ_LOCATION", "EU"),
        )


@dataclass(frozen=True)
class PostgresConfig:
    dsn: str
    schema: str

    @classmethod
    def from_env(cls) -> "PostgresConfig":
        return cls(
            dsn=_require("SUPABASE_DB_URL"),
            schema=_env("PG_SCHEMA", "shopify"),
        )


@dataclass(frozen=True)
class SyncConfig:
    sinks: tuple[str, ...]
    entities: tuple[str, ...]
    start_date: datetime
    overlap: timedelta
    batch_size: int
    poll_interval_s: float
    timeout_s: float

    @classmethod
    def from_env(cls) -> "SyncConfig":
        sinks = tuple(s.strip() for s in _env("SINKS", "bigquery").split(",") if s.strip())
        unknown = set(sinks) - {"bigquery", "postgres"}
        if unknown or not sinks:
            raise ConfigError(f"SINKS måste vara bigquery och/eller postgres, fick: {sinks}")
        entities = tuple(
            e.strip()
            for e in _env("ENTITIES", "orders,products,customers").split(",")
            if e.strip()
        )
        unknown = set(entities) - {"orders", "products", "customers"}
        if unknown or not entities:
            raise ConfigError(f"Okända ENTITIES: {sorted(unknown)}")
        start = datetime.fromisoformat(_env("SYNC_START_DATE", "2018-01-01"))
        if start.tzinfo is None:
            start = start.replace(tzinfo=timezone.utc)
        return cls(
            sinks=sinks,
            entities=entities,
            start_date=start,
            overlap=timedelta(minutes=int(_env("SYNC_OVERLAP_MINUTES", "15"))),
            batch_size=int(_env("BATCH_SIZE", "5000")),
            poll_interval_s=float(_env("BULK_POLL_SECONDS", "5")),
            timeout_s=float(_env("BULK_TIMEOUT_SECONDS", "3600")),
        )
