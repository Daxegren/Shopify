"""Lagrar körningar i BigQuery så att fynd och sidfakta kan följas över tid.

Tabeller (dataset site_audit):
  runs      en rad per körning med sammanfattning
  findings  alla fynd, partitionerad på run_date
  pages     alla crawlade URL:er med sidfakta, partitionerad på run_date
  changes   manuell ändringslogg för effektmätning (se impact.py)
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any

from .audit import AuditRun

RUNS_SCHEMA = [
    ("run_id", "STRING", "REQUIRED"), ("site", "STRING", "REQUIRED"), ("run_date", "DATE", "REQUIRED"),
    ("started_at", "TIMESTAMP", "NULLABLE"), ("finished_at", "TIMESTAMP", "NULLABLE"),
    ("total", "INT64", "NULLABLE"), ("critical", "INT64", "NULLABLE"), ("high", "INT64", "NULLABLE"),
    ("medium", "INT64", "NULLABLE"), ("low", "INT64", "NULLABLE"), ("info", "INT64", "NULLABLE"),
    ("summary", "JSON", "NULLABLE"),
]
FINDINGS_SCHEMA = [
    ("run_id", "STRING", "REQUIRED"), ("site", "STRING", "REQUIRED"), ("run_date", "DATE", "REQUIRED"),
    ("check_id", "STRING", "REQUIRED"), ("severity", "STRING", "REQUIRED"), ("category", "STRING", "REQUIRED"),
    ("message", "STRING", "NULLABLE"), ("url", "STRING", "NULLABLE"), ("path", "STRING", "NULLABLE"),
    ("resource", "STRING", "NULLABLE"), ("evidence", "JSON", "NULLABLE"),
]
PAGES_SCHEMA = [
    ("run_id", "STRING", "REQUIRED"), ("site", "STRING", "REQUIRED"), ("run_date", "DATE", "REQUIRED"),
    ("url", "STRING", "REQUIRED"), ("path", "STRING", "NULLABLE"), ("page_type", "STRING", "NULLABLE"),
    ("locale_prefix", "STRING", "NULLABLE"), ("source", "STRING", "NULLABLE"), ("status", "INT64", "NULLABLE"),
    ("final_url", "STRING", "NULLABLE"), ("redirect_count", "INT64", "NULLABLE"), ("in_sitemap", "BOOL", "NULLABLE"),
    ("title", "STRING", "NULLABLE"), ("h1_count", "INT64", "NULLABLE"), ("canonical", "STRING", "NULLABLE"),
    ("hreflang_count", "INT64", "NULLABLE"), ("html_bytes", "INT64", "NULLABLE"), ("inline_script_bytes", "INT64", "NULLABLE"),
    ("word_count", "INT64", "NULLABLE"), ("images_total", "INT64", "NULLABLE"), ("images_missing_alt", "INT64", "NULLABLE"),
    ("detected_language", "STRING", "NULLABLE"), ("jsonld_types", "STRING", "REPEATED"), ("row", "JSON", "NULLABLE"),
]
CHANGES_SCHEMA = [
    ("change_id", "STRING", "REQUIRED"), ("site", "STRING", "REQUIRED"), ("change_date", "DATE", "REQUIRED"),
    ("description", "STRING", "NULLABLE"), ("url_pattern", "STRING", "NULLABLE"), ("page_group", "STRING", "NULLABLE"),
    ("created_at", "TIMESTAMP", "NULLABLE"),
]
TABLES = {"runs": (RUNS_SCHEMA, None), "findings": (FINDINGS_SCHEMA, "run_date"),
          "pages": (PAGES_SCHEMA, "run_date"), "changes": (CHANGES_SCHEMA, None)}


def run_rows(run: AuditRun) -> dict[str, list[dict[str, Any]]]:
    from urllib.parse import urlsplit

    s = run.summary()
    run_date = run.started_at[:10]
    base = {"run_id": run.run_id, "site": run.site.name, "run_date": run_date}
    runs = [{**base, "started_at": run.started_at, "finished_at": run.finished_at, "total": s["total"],
             **s["by_severity"], "summary": json.loads(json.dumps(s, default=str))}]
    findings = [{**base, "check_id": f.check, "severity": f.severity, "category": f.category, "message": f.message,
                 "url": f.url, "path": urlsplit(f.url).path if f.url else None, "resource": f.resource,
                 "evidence": json.loads(json.dumps(f.evidence, default=str))} for f in run.findings]
    pages = []
    if run.crawl:
        for cu in run.crawl.urls.values():
            f = cu.facts
            pages.append({**base, "url": cu.url, "path": urlsplit(cu.url).path, "page_type": f.page_type if f else None,
                          "locale_prefix": f.locale_prefix if f else None, "source": cu.source, "status": cu.status,
                          "final_url": cu.final_url, "redirect_count": cu.redirect_count, "in_sitemap": cu.in_sitemap,
                          "title": f.title if f else None, "h1_count": len(f.h1) if f else None,
                          "canonical": f.canonical if f else None, "hreflang_count": len(f.hreflang) if f else None,
                          "html_bytes": f.html_bytes if f else None, "inline_script_bytes": f.inline_script_bytes if f else None,
                          "word_count": f.word_count if f else None, "images_total": f.images_total if f else None,
                          "images_missing_alt": f.images_missing_alt if f else None,
                          "detected_language": f.detected_language if f else None,
                          "jsonld_types": f.jsonld_types if f else [],
                          "row": json.loads(json.dumps(cu.to_row(), default=str))})
    return {"runs": runs, "findings": findings, "pages": pages}


class BigQueryStore:
    def __init__(self, project: str, dataset: str = "site_audit", location: str = "EU"):
        from google.cloud import bigquery

        self.bq = bigquery
        self.client = bigquery.Client(project=project, location=location)
        self.dataset = f"{project}.{dataset}"
        self.location = location

    def ensure(self) -> None:
        ds = self.bq.Dataset(self.dataset)
        ds.location = self.location
        self.client.create_dataset(ds, exists_ok=True)
        for name, (schema, partition) in TABLES.items():
            table = self.bq.Table(f"{self.dataset}.{name}", schema=[self.bq.SchemaField(n, t, mode=m) for n, t, m in schema])
            if partition:
                table.time_partitioning = self.bq.TimePartitioning(field=partition)
                table.clustering_fields = ["site"]
            self.client.create_table(table, exists_ok=True)

    def _load(self, name: str, rows: list[dict[str, Any]]) -> None:
        if not rows:
            return
        schema = [self.bq.SchemaField(n, t, mode=m) for n, t, m in TABLES[name][0]]
        cfg = self.bq.LoadJobConfig(schema=schema, write_disposition=self.bq.WriteDisposition.WRITE_APPEND)
        self.client.load_table_from_json(rows, f"{self.dataset}.{name}", job_config=cfg).result()

    def save_run(self, run: AuditRun) -> None:
        self.ensure()
        for name, rows in run_rows(run).items():
            self._load(name, rows)

    def log_change(self, site: str, change_date: str, description: str, url_pattern: str | None, page_group: str | None) -> str:
        import uuid

        self.ensure()
        cid = uuid.uuid4().hex[:12]
        self._load("changes", [{"change_id": cid, "site": site, "change_date": change_date, "description": description,
                                "url_pattern": url_pattern, "page_group": page_group,
                                "created_at": datetime.now(timezone.utc).isoformat()}])
        return cid

    def query(self, sql: str, params: list | None = None) -> list[dict[str, Any]]:
        cfg = self.bq.QueryJobConfig(query_parameters=params or [])
        return [dict(r) for r in self.client.query(sql, job_config=cfg).result()]
