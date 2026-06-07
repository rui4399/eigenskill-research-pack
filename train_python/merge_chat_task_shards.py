#!/usr/bin/env python3
from __future__ import annotations

"""Merge sharded chat-task benchmark summaries and GPU guard reports."""

import argparse
import json
from pathlib import Path
from statistics import mean
from typing import Any

from eval_chat_task_benchmark import aggregate_rows, render_markdown


MERGE_KEYS = (
    "model",
    "loader",
    "hf_device_map",
    "hf_max_gpu_memory_mib",
    "task_format",
    "chat_template",
    "no_think",
    "max_new_tokens",
)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_shard_spec(spec: str) -> tuple[Path, Path]:
    parts = spec.split("=", 1)
    if len(parts) != 2 or not all(part.strip() for part in parts):
        raise ValueError(f"shard must be SUMMARY_JSON=GUARD_JSON: {spec}")
    return Path(parts[0]), Path(parts[1])


def _metadata_value(payload: dict[str, Any], key: str) -> Any:
    return payload.get(key)


def _check_compatible(summaries: list[dict[str, Any]]) -> None:
    if not summaries:
        raise ValueError("at least one shard is required")
    first = summaries[0]
    for idx, summary in enumerate(summaries[1:], start=2):
        for key in MERGE_KEYS:
            if _metadata_value(summary, key) != _metadata_value(first, key):
                raise ValueError(
                    f"shard {idx} has incompatible {key}: "
                    f"{_metadata_value(summary, key)!r} != {_metadata_value(first, key)!r}"
                )
        if ("fused" in summary) != ("fused" in first):
            raise ValueError(f"shard {idx} has incompatible fused section")


def _merge_rows(summaries: list[dict[str, Any]], section: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for shard_idx, summary in enumerate(summaries, start=1):
        section_payload = summary.get(section, {})
        for row in section_payload.get("rows", []):
            row_id = str(row.get("id", ""))
            if row_id in seen_ids:
                raise ValueError(f"duplicate row id across shards: {row_id}")
            seen_ids.add(row_id)
            rows.append(row)
    return rows


def merge_summaries(summaries: list[dict[str, Any]], shard_paths: list[Path]) -> dict[str, Any]:
    _check_compatible(summaries)
    first = summaries[0]
    baseline_rows = _merge_rows(summaries, "baseline")
    result: dict[str, Any] = {
        key: first.get(key)
        for key in (
            "model",
            "loader",
            "hf_device_map",
            "hf_max_gpu_memory_mib",
            "task_format",
            "chat_template",
            "no_think",
            "max_new_tokens",
        )
    }
    result.update(
        {
            "task_file": "merged:" + ",".join(str(path) for path in shard_paths),
            "task_count": len(baseline_rows),
            "task_limit": len(baseline_rows),
            "task_offset": 0,
            "shard_count": len(summaries),
            "shards": [str(path) for path in shard_paths],
            "baseline": {"aggregate": aggregate_rows(baseline_rows), "rows": baseline_rows},
        }
    )
    if "fused" in first:
        fused_rows = _merge_rows(summaries, "fused")
        result["fused"] = {"aggregate": aggregate_rows(fused_rows), "rows": fused_rows}
    return result


def merge_guards(guards: list[dict[str, Any]], guard_paths: list[Path]) -> dict[str, Any]:
    if not guards:
        raise ValueError("at least one guard is required")
    returncodes = [int(guard.get("returncode", 1) or 0) for guard in guards]
    memory_total_mib = max(int(guard.get("memory_total_mib") or 0) for guard in guards)
    max_memory_used_mib = max(int(guard.get("max_memory_used_mib") or 0) for guard in guards)
    return {
        "command": ["merged_chat_task_shards"],
        "returncode": 0 if all(code == 0 for code in returncodes) else max(returncodes),
        "killed_by_guard": any(bool(guard.get("killed_by_guard")) for guard in guards),
        "killed_by_timeout": any(bool(guard.get("killed_by_timeout")) for guard in guards),
        "timeout_seconds": sum(float(guard.get("timeout_seconds") or 0.0) for guard in guards),
        "max_memory_used_mib": max_memory_used_mib,
        "memory_total_mib": memory_total_mib,
        "max_memory_used_ratio": max(
            float(guard.get("max_memory_used_ratio") or 0.0) for guard in guards
        ),
        "max_utilization_gpu_pct": max(int(guard.get("max_utilization_gpu_pct") or 0) for guard in guards),
        "start_state": guards[0].get("start_state", {}),
        "end_state": guards[-1].get("end_state", {}),
        "start_disk_state": guards[0].get("start_disk_state", {}),
        "end_disk_state": guards[-1].get("end_disk_state", {}),
        "post_cleanup": {
            "target_count": sum(int(guard.get("post_cleanup", {}).get("target_count") or 0) for guard in guards),
            "estimated_bytes": sum(int(guard.get("post_cleanup", {}).get("estimated_bytes") or 0) for guard in guards),
            "errors": [
                error
                for guard in guards
                for error in guard.get("post_cleanup", {}).get("errors", [])
            ],
        },
        "merged_shard_count": len(guards),
        "merged_guard_paths": [str(path) for path in guard_paths],
        "mean_shard_max_memory_used_ratio": mean(
            [float(guard.get("max_memory_used_ratio") or 0.0) for guard in guards]
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge sharded chat-task summaries and guard reports.")
    parser.add_argument("--shard", action="append", required=True, help="SUMMARY_JSON=GUARD_JSON")
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    parser.add_argument("--out-guard-json", type=Path, required=True)
    args = parser.parse_args()

    summary_paths: list[Path] = []
    guard_paths: list[Path] = []
    summaries: list[dict[str, Any]] = []
    guards: list[dict[str, Any]] = []
    for spec in args.shard:
        summary_path, guard_path = parse_shard_spec(spec)
        summary_paths.append(summary_path)
        guard_paths.append(guard_path)
        summaries.append(load_json(summary_path))
        guards.append(load_json(guard_path))

    summary = merge_summaries(summaries, summary_paths)
    guard = merge_guards(guards, guard_paths)

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_guard_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    args.out_md.write_text(render_markdown(summary), encoding="utf-8")
    args.out_guard_json.write_text(json.dumps(guard, indent=2, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "out_json": str(args.out_json),
                "out_md": str(args.out_md),
                "out_guard_json": str(args.out_guard_json),
                "tasks": summary["task_count"],
                "guard_max_memory_used_ratio": guard["max_memory_used_ratio"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
