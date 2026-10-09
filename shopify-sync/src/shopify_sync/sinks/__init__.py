from __future__ import annotations

from .base import Sink


def build_sinks(names: tuple[str, ...]) -> list[Sink]:
    sinks: list[Sink] = []
    for name in names:
        if name == "bigquery":
            from ..config import BigQueryConfig
            from .bigquery_sink import BigQuerySink

            sinks.append(BigQuerySink(BigQueryConfig.from_env()))
        elif name == "postgres":
            from ..config import PostgresConfig
            from .postgres_sink import PostgresSink

            sinks.append(PostgresSink(PostgresConfig.from_env()))
    return sinks


__all__ = ["Sink", "build_sinks"]
