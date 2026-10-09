"""Engångsinstallation via OAuth: hämtar en offline-token och sparar den i Secret Manager.

Behövs när appen ägs av en annan organisation än butiken (t.ex. ett partnerkonto), där
client credentials inte fungerar. Endast standardbiblioteket används, så skriptet kan köras
direkt i Cloud Shell utan installation.

Flöde:
  1. Butiken öppnar appens installationslänk -> Shopify skickar till App URL (/?shop=...).
  2. Vi skickar vidare till /admin/oauth/authorize med scopes och ett slumpat state.
  3. Shopify skickar tillbaka till /callback?code=...; vi verifierar HMAC och state,
     byter code mot token och lagrar den. Tokenen skrivs aldrig ut.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import logging
import os
import re
import secrets
import subprocess
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
from collections.abc import Callable

log = logging.getLogger(__name__)

DEFAULT_SCOPES = "read_orders,read_all_orders,read_products,read_inventory,read_customers"
SHOP_RE = re.compile(r"^[a-z0-9][a-z0-9-]*\.myshopify\.com$")


def verify_hmac(params: dict[str, str], client_secret: str) -> bool:
    received = params.get("hmac", "")
    message = "&".join(f"{k}={v}" for k, v in sorted(params.items()) if k not in {"hmac", "signature"})
    expected = hmac.new(client_secret.encode(), message.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, received)


def authorize_url(shop: str, client_id: str, scopes: str, redirect_uri: str, state: str) -> str:
    query = urllib.parse.urlencode(
        {"client_id": client_id, "scope": scopes, "redirect_uri": redirect_uri, "state": state}
    )
    return f"https://{shop}/admin/oauth/authorize?{query}"


def exchange_code(shop: str, client_id: str, client_secret: str, code: str) -> dict:
    req = urllib.request.Request(
        f"https://{shop}/admin/oauth/access_token",
        data=json.dumps({"client_id": client_id, "client_secret": client_secret, "code": code}).encode(),
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def store_in_secret_manager(token: str, secret: str, project: str) -> None:
    exists = subprocess.run(
        ["gcloud", "secrets", "describe", secret, "--project", project],
        capture_output=True,
    ).returncode == 0
    cmd = (
        ["gcloud", "secrets", "versions", "add", secret, "--project", project, "--data-file=-"]
        if exists
        else ["gcloud", "secrets", "create", secret, "--project", project,
              "--replication-policy=automatic", "--data-file=-"]
    )
    subprocess.run(cmd, input=token.encode(), check=True, capture_output=True)


def store_in_file(token: str, path: str) -> None:
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as fh:
        fh.write(token)


class OAuthFlow:
    """Tillståndet för en installation. Hålls separat från HTTP-servern för att kunna testas."""

    def __init__(
        self,
        shop: str,
        client_id: str,
        client_secret: str,
        base_url: str,
        scopes: str,
        store: Callable[[str], None],
        exchange: Callable[[str, str, str, str], dict] = exchange_code,
    ):
        if not SHOP_RE.match(shop):
            raise ValueError(f"Ogiltig butiksadress: {shop} (ska sluta på .myshopify.com)")
        self.shop = shop
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = base_url.rstrip("/") + "/callback"
        self.scopes = scopes
        self.store = store
        self.exchange = exchange
        self.state = secrets.token_urlsafe(24)
        self.done = False
        self.granted_scopes: str | None = None

    @property
    def install_url(self) -> str:
        return authorize_url(self.shop, self.client_id, self.scopes, self.redirect_uri, self.state)

    def handle(self, path: str, params: dict[str, str]) -> tuple[int, dict[str, str], str]:
        """Returnerar (status, headers, body)."""
        if path == "/callback":
            return self._callback(params)
        if path == "/":
            if params.get("hmac") and not verify_hmac(params, self.client_secret):
                return 400, {}, "Ogiltig signatur."
            if params.get("shop") and params["shop"] != self.shop:
                return 400, {}, f"Fel butik: {params['shop']}"
            return 302, {"Location": self.install_url}, ""
        return 404, {}, "Hittades inte."

    def _callback(self, params: dict[str, str]) -> tuple[int, dict[str, str], str]:
        if not verify_hmac(params, self.client_secret):
            return 400, {}, "Ogiltig signatur."
        if not hmac.compare_digest(params.get("state", ""), self.state):
            return 400, {}, "Ogiltigt state. Starta om installationen."
        if params.get("shop") != self.shop:
            return 400, {}, f"Fel butik: {params.get('shop')}"
        result = self.exchange(self.shop, self.client_id, self.client_secret, params["code"])
        token = result.get("access_token")
        if not token:
            return 502, {}, "Shopify returnerade ingen token."
        self.store(token)
        self.granted_scopes = result.get("scope", "")
        self.done = True
        missing = set(self.scopes.split(",")) - set(self.granted_scopes.split(","))
        note = f" Saknade scopes: {', '.join(sorted(missing))}." if missing else ""
        return 200, {}, f"Klart. Tokenen är sparad.{note} Du kan stänga fliken."


def serve(flow: OAuthFlow, port: int) -> None:
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802
            parsed = urllib.parse.urlsplit(self.path)
            params = dict(urllib.parse.parse_qsl(parsed.query, keep_blank_values=True))
            try:
                status, headers, body = flow.handle(parsed.path, params)
            except Exception as exc:  # visas för användaren, utan hemligheter
                log.exception("Fel vid installation")
                status, headers, body = 500, {}, f"Fel: {type(exc).__name__}"
            self.send_response(status)
            for k, v in headers.items():
                self.send_header(k, v)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(body.encode())

        def log_message(self, fmt, *args):  # query innehåller code, logga bara sökvägen
            log.info("%s %s", self.command, urllib.parse.urlsplit(self.path).path)

    server = HTTPServer(("0.0.0.0", port), Handler)
    log.info("Väntar på installation på port %s ...", port)
    while not flow.done:
        server.handle_request()
    server.server_close()
