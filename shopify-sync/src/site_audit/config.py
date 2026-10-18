"""Konfiguration per sajt i en TOML-fil, så att samma verktyg körs mot alla sajter.

Exempel: se sites.example.toml i projektroten.
"""

from __future__ import annotations

import os
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


class ConfigError(RuntimeError):
    pass


@dataclass
class GeoProfile:
    """Simulerad besökare. Shopify geo-omdirigerar på IP, så headers fångar bara språkstyrda
    omdirigeringar. Riktiga IP-baserade tester kräver att jobbet körs från rätt land."""

    name: str
    accept_language: str
    country_cookie: str | None = None  # t.ex. "SE" -> cookie localization=SE


@dataclass
class CrawlSettings:
    max_pages: int = 5000
    requests_per_second: float = 3.0
    concurrency: int = 4
    timeout_s: float = 30.0
    follow_internal_links: bool = True
    max_link_depth: int = 2
    user_agent: str = "SiteAuditBot/0.1 (+intern genomlysning)"
    include_patterns: list[str] = field(default_factory=list)
    exclude_patterns: list[str] = field(default_factory=lambda: [
        r"/cart", r"/checkout", r"/account", r"/search", r"\?.*(sort_by|filter\.|page=\d{2,})",
    ])
    geo_probe_paths: list[str] = field(default_factory=lambda: ["/"])


@dataclass
class Thresholds:
    html_bytes_warn: int = 1_000_000
    inline_script_bytes_warn: int = 100_000
    title_max: int = 60
    title_min: int = 15
    description_max: int = 160
    thin_words: int = 120
    hreflang_variants_warn: int = 12
    redirect_chain_warn: int = 2
    recent_product_days: int = 90


@dataclass
class PageGroup:
    """Namngiven grupp av URL:er för trend- och effektanalys, t.ex. konstnärssidor."""

    name: str
    pattern: str  # regex mot sökvägen


@dataclass
class SiteConfig:
    name: str
    base_url: str
    shop_domain: str | None = None
    shopify_token_env: str = "SHOPIFY_ACCESS_TOKEN"
    api_version: str = "2026-07"
    brand_terms: list[str] = field(default_factory=list)
    known_misspellings: list[str] = field(default_factory=list)
    primary_locale: str | None = None
    expected_locales: list[str] = field(default_factory=list)
    expected_org_schema: list[str] = field(default_factory=lambda: ["Organization", "OnlineStore", "Store"])
    geo_profiles: list[GeoProfile] = field(default_factory=list)
    page_groups: list[PageGroup] = field(default_factory=list)
    crawl: CrawlSettings = field(default_factory=CrawlSettings)
    thresholds: Thresholds = field(default_factory=Thresholds)
    # BigQuery
    bq_project: str | None = None
    bq_dataset: str = "site_audit"
    gsc_table: str | None = None   # t.ex. "proj.searchconsole.searchdata_url_impression"
    ga4_dataset: str | None = None  # t.ex. "proj.analytics_123456789"
    shopify_dataset: str | None = None  # t.ex. "proj.shopify"
    shopify_currency: str | None = None  # filtrerar ordrar per marknad när butiken delas, t.ex. "SEK"
    gsc_property: str | None = None   # t.ex. "sc-domain:gorillasports.se" (för API-hämtning)
    ga4_property_id: str | None = None  # t.ex. "123456789" (för API-hämtning)
    ga4_api_table: str | None = None  # t.ex. "proj.site_audit.ga4_landing_daily"
    # Annonser. Konto-id:n är inga hemligheter; utvecklartoken och Meta-token läses från miljön.
    google_ads_customer_ids: list[str] = field(default_factory=list)  # t.ex. ["8331390722", "5836710921"]
    google_ads_login_customer_id: str | None = None  # hanterarkonto (MCC), om kontona nås via ett sådant
    google_ads_developer_token_env: str = "GOOGLE_ADS_DEVELOPER_TOKEN"
    google_ads_api_version: str = "v21"  # kontrollera mot Googles versionsplan; äldre versioner stängs av
    meta_ad_account_ids: list[str] = field(default_factory=list)  # t.ex. ["act_1448542818538699"]
    meta_token_env: str = "META_ACCESS_TOKEN"
    meta_api_version: str = "v23.0"

    @property
    def host(self) -> str:
        from urllib.parse import urlsplit

        return urlsplit(self.base_url).netloc.lower()

    def shopify_token(self) -> str | None:
        return os.environ.get(self.shopify_token_env)

    @property
    def slug(self) -> str:
        return self.name.replace("-", "_")


def _build(cls, data: dict[str, Any]):
    known = {f for f in cls.__dataclass_fields__}
    unknown = set(data) - known
    if unknown:
        raise ConfigError(f"Okända fält för {cls.__name__}: {sorted(unknown)}")
    return cls(**data)


def site_from_dict(data: dict[str, Any]) -> SiteConfig:
    data = dict(data)
    if "name" not in data or "base_url" not in data:
        raise ConfigError("Varje sajt behöver name och base_url.")
    data["base_url"] = data["base_url"].rstrip("/")
    data["crawl"] = _build(CrawlSettings, data.get("crawl", {}))
    data["thresholds"] = _build(Thresholds, data.get("thresholds", {}))
    data["geo_profiles"] = [_build(GeoProfile, g) for g in data.get("geo_profiles", [])]
    data["page_groups"] = [_build(PageGroup, g) for g in data.get("page_groups", [])]
    return _build(SiteConfig, data)


def load_sites(path: str | Path) -> dict[str, SiteConfig]:
    with open(path, "rb") as fh:
        raw = tomllib.load(fh)
    defaults = raw.get("defaults", {})
    sites = {}
    for entry in raw.get("site", []):
        merged = _deep_merge(defaults, entry)
        site = site_from_dict(merged)
        sites[site.name] = site
    if not sites:
        raise ConfigError(f"Inga [[site]] i {path}")
    return sites


def _deep_merge(base: dict, override: dict) -> dict:
    out = dict(base)
    for k, v in override.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = v
    return out
