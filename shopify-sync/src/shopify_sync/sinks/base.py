from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

from ..schema import Table


class Sink(ABC):
    """Ett lagringsmål. Alla skrivningar är idempotenta upserts på primärnyckeln."""

    name: str

    @abstractmethod
    def ensure_tables(self) -> None: ...

    @abstractmethod
    def upsert(self, table: Table, rows: list[dict[str, Any]]) -> None: ...

    @abstractmethod
    def get_watermark(self, entity: str) -> datetime | None: ...

    @abstractmethod
    def set_watermark(self, entity: str, watermark: datetime, object_count: int) -> None: ...

    def close(self) -> None:
        pass
