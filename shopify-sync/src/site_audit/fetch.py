"""HTTP-hämtning med hastighetsbegränsning och manuell följning av omdirigeringar,
så att hela kedjan (statuskod per hopp) registreras."""

from __future__ import annotations

import logging
import threading
import time
from dataclasses import dataclass, field
from urllib.parse import urljoin

import requests

log = logging.getLogger(__name__)

MAX_HOPS = 10


@dataclass
class Hop:
    url: str
    status: int
    location: str | None = None


@dataclass
class FetchResult:
    requested_url: str
    final_url: str
    status: int                      # slutlig status (0 = nätverksfel)
    hops: list[Hop] = field(default_factory=list)  # alla hopp inkl. sista
    headers: dict[str, str] = field(default_factory=dict)
    body: bytes = b""
    elapsed_ms: int = 0
    error: str | None = None
    loop: bool = False

    @property
    def redirect_count(self) -> int:
        return max(0, len(self.hops) - 1)

    @property
    def content_type(self) -> str:
        return self.headers.get("content-type", "").lower()

    @property
    def is_html(self) -> bool:
        return "text/html" in self.content_type


class RateLimiter:
    def __init__(self, per_second: float):
        self.interval = 1.0 / per_second if per_second > 0 else 0
        self._lock = threading.Lock()
        self._next = 0.0

    def wait(self) -> None:
        if not self.interval:
            return
        with self._lock:
            now = time.monotonic()
            delay = self._next - now
            self._next = max(now, self._next) + self.interval
        if delay > 0:
            time.sleep(delay)


class Fetcher:
    def __init__(self, user_agent: str, requests_per_second: float = 3.0, timeout_s: float = 30.0,
                 session: requests.Session | None = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": user_agent, "Accept": "text/html,application/xml;q=0.9,*/*;q=0.8"})
        self.limiter = RateLimiter(requests_per_second)
        self._local = threading.local()  # senaste felorsak per tråd
        self.timeout_s = timeout_s

    def fetch(self, url: str, headers: dict[str, str] | None = None, cookies: dict[str, str] | None = None,
              method: str = "GET", read_body: bool = True) -> FetchResult:
        result = FetchResult(requested_url=url, final_url=url, status=0)
        seen: set[str] = set()
        current = url
        start = time.monotonic()
        for _ in range(MAX_HOPS):
            if current in seen:
                result.loop = True
                break
            seen.add(current)
            resp = self._request(method, current, headers, cookies)
            if resp is None:
                result.error = getattr(self._local, "last_error", None) or "nätverksfel"
                result.hops.append(Hop(current, 0))
                break
            location = resp.headers.get("Location")
            result.hops.append(Hop(current, resp.status_code, urljoin(current, location) if location else None))
            if resp.is_redirect and location:
                current = urljoin(current, location)
                resp.close()
                continue
            result.status = resp.status_code
            result.final_url = current
            result.headers = {k.lower(): v for k, v in resp.headers.items()}
            if read_body:
                result.body = resp.content
            resp.close()
            break
        else:
            result.error = f"fler än {MAX_HOPS} omdirigeringar"
        if result.loop:
            result.error = "omdirigeringsloop"
        result.elapsed_ms = int((time.monotonic() - start) * 1000)
        return result

    def _request(self, method, url, headers, cookies) -> requests.Response | None:
        self._local.last_error = None
        for attempt in range(5):
            self.limiter.wait()
            try:
                resp = self.session.request(method, url, headers=headers, cookies=cookies,
                                            allow_redirects=False, timeout=self.timeout_s)
            except requests.RequestException as exc:
                log.warning("Fel vid hämtning av %s: %s", url, exc)
                self._local.last_error = f"{type(exc).__name__}: {str(exc)[:120]}"
                time.sleep(2 ** attempt)
                continue
            if resp.status_code == 429:
                self._local.last_error = "429 Too Many Requests (Shopify bromsar)"
                wait = min(float(resp.headers.get("Retry-After", 2 ** (attempt + 1))), 60)
                log.warning("429 från %s, väntar %.0fs", url, wait)
                resp.close()
                time.sleep(wait)
                continue
            return resp
        return None
