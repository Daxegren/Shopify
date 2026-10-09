"""Shopify Admin GraphQL-klient med stöd för Bulk Operations."""

from __future__ import annotations

import json
import logging
import time
from collections.abc import Iterator
from typing import Any

import requests

from .config import ShopifyConfig

log = logging.getLogger(__name__)

RETRY_STATUS = {429, 500, 502, 503, 504}


class ShopifyError(RuntimeError):
    pass


class ShopifyClient:
    def __init__(self, config: ShopifyConfig, session: requests.Session | None = None):
        self.config = config
        self.session = session or requests.Session()
        self._token = config.access_token

    @property
    def graphql_url(self) -> str:
        return (
            f"https://{self.config.shop_domain}/admin/api/"
            f"{self.config.api_version}/graphql.json"
        )

    def _access_token(self) -> str:
        if self._token:
            return self._token
        # Client credentials grant för appar skapade i Shopify Dev Dashboard.
        resp = self._request(
            "POST",
            f"https://{self.config.shop_domain}/admin/oauth/access_token",
            data={
                "grant_type": "client_credentials",
                "client_id": self.config.client_id,
                "client_secret": self.config.client_secret,
            },
        )
        self._token = resp.json()["access_token"]
        return self._token

    def _request(self, method: str, url: str, **kwargs: Any) -> requests.Response:
        delay = 2.0
        last_error = ""
        for attempt in range(6):
            try:
                resp = self.session.request(method, url, timeout=60, **kwargs)
            except (requests.ConnectionError, requests.Timeout) as exc:
                last_error, wait = str(exc), delay
            else:
                if resp.status_code not in RETRY_STATUS:
                    if resp.status_code >= 400:
                        raise ShopifyError(f"{method} {url} -> {resp.status_code}: {resp.text[:500]}")
                    return resp
                last_error = f"HTTP {resp.status_code}"
                wait = float(resp.headers.get("Retry-After", delay))
            log.warning("%s mot Shopify, försök %s, väntar %.0fs", last_error, attempt + 1, wait)
            time.sleep(wait)
            delay = min(delay * 2, 60)
        raise ShopifyError(f"{method} {url} misslyckades efter flera försök: {last_error}")

    def graphql(self, query: str, variables: dict[str, Any] | None = None) -> dict[str, Any]:
        resp = self._request(
            "POST",
            self.graphql_url,
            headers={
                "X-Shopify-Access-Token": self._access_token(),
                "Content-Type": "application/json",
            },
            data=json.dumps({"query": query, "variables": variables or {}}),
        )
        body = resp.json()
        if body.get("errors"):
            raise ShopifyError(f"GraphQL-fel: {body['errors']}")
        return body["data"]

    # --- Bulk operations -------------------------------------------------

    def start_bulk_query(self, bulk_query: str) -> str:
        data = self.graphql(
            """
            mutation($query: String!) {
              bulkOperationRunQuery(query: $query) {
                bulkOperation { id status }
                userErrors { field message }
              }
            }
            """,
            {"query": bulk_query},
        )
        result = data["bulkOperationRunQuery"]
        if result["userErrors"]:
            raise ShopifyError(f"Bulk-frågan avvisades: {result['userErrors']}")
        return result["bulkOperation"]["id"]

    def wait_for_bulk(self, operation_id: str, poll_interval_s: float, timeout_s: float) -> dict[str, Any]:
        deadline = time.monotonic() + timeout_s
        while True:
            node = self.graphql(
                """
                query($id: ID!) {
                  node(id: $id) {
                    ... on BulkOperation {
                      id status errorCode objectCount url partialDataUrl
                    }
                  }
                }
                """,
                {"id": operation_id},
            )["node"]
            status = node["status"]
            if status == "COMPLETED":
                return node
            if status in {"FAILED", "CANCELED", "EXPIRED"}:
                raise ShopifyError(f"Bulk-operation {operation_id} slutade med {status}: {node.get('errorCode')}")
            if time.monotonic() > deadline:
                raise ShopifyError(f"Bulk-operation {operation_id} tog längre tid än {timeout_s:.0f}s.")
            log.info("Bulk %s: %s, %s objekt hittills", operation_id, status, node.get("objectCount"))
            time.sleep(poll_interval_s)

    def iter_jsonl(self, url: str | None) -> Iterator[dict[str, Any]]:
        if not url:  # Inga träffar ger ingen fil.
            return
        with self.session.get(url, stream=True, timeout=300) as resp:
            resp.raise_for_status()
            for line in resp.iter_lines(decode_unicode=True):
                if line:
                    yield json.loads(line)

    def run_bulk(self, bulk_query: str, poll_interval_s: float, timeout_s: float) -> tuple[dict[str, Any], Iterator[dict[str, Any]]]:
        op_id = self.start_bulk_query(bulk_query)
        log.info("Startade bulk-operation %s", op_id)
        op = self.wait_for_bulk(op_id, poll_interval_s, timeout_s)
        return op, self.iter_jsonl(op.get("url"))
