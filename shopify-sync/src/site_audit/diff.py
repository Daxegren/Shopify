"""Jämför två körningar: vad är nytt, vad är åtgärdat och hur har antalet per kontroll ändrats."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any


def load_findings(run_dir: str | Path) -> list[dict[str, Any]]:
    with open(Path(run_dir) / "findings.jsonl") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def _key(f: dict[str, Any]) -> tuple:
    return (f["check"], f.get("url") or f.get("resource") or "")


def diff_runs(old: list[dict[str, Any]], new: list[dict[str, Any]]) -> dict[str, Any]:
    old_keys = {_key(f): f for f in old}
    new_keys = {_key(f): f for f in new}
    resolved = [old_keys[k] for k in old_keys.keys() - new_keys.keys()]
    added = [new_keys[k] for k in new_keys.keys() - old_keys.keys()]
    oc, nc = Counter(f["check"] for f in old), Counter(f["check"] for f in new)
    per_check = {c: {"before": oc.get(c, 0), "after": nc.get(c, 0), "delta": nc.get(c, 0) - oc.get(c, 0)}
                 for c in sorted(set(oc) | set(nc))}
    return {"resolved": resolved, "added": added, "per_check": per_check,
            "totals": {"before": len(old), "after": len(new)}}


def describe_diff(d: dict[str, Any]) -> str:
    lines = [f"Fynd: {d['totals']['before']} → {d['totals']['after']} "
             f"({len(d['resolved'])} åtgärdade, {len(d['added'])} nya)", ""]
    changed = sorted(((c, v) for c, v in d["per_check"].items() if v["delta"]), key=lambda kv: kv[1]["delta"])
    for check, v in changed:
        lines.append(f"  {check}: {v['before']} → {v['after']} ({v['delta']:+d})")
    return "\n".join(lines)
