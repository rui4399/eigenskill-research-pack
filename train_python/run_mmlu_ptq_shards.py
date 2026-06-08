#!/usr/bin/env python3
from __future__ import annotations

"""Run missing guarded MMLU PTQ shards from a generated shard plan.

The plan already contains the exact guarded commands. This helper only selects
an offset range, skips completed shards, and records local run logs. It does not
change benchmark semantics.
"""

import argparse
import json
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ShardCommand:
    variant: str
    offset: int
    limit: int
    command: str
    summary_json: Path
    guard_json: Path

    @property
    def end(self) -> int:
        return self.offset + self.limit

    @property
    def label(self) -> str:
        return f"{self.variant}_{self.offset}_{self.end}"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_shards(plan: dict[str, Any]) -> list[ShardCommand]:
    variants = plan.get("variants", [])
    if not isinstance(variants, list):
        raise ValueError("plan variants must be a list")
    shards: list[ShardCommand] = []
    for variant in variants:
        if not isinstance(variant, dict):
            continue
        name = str(variant.get("variant") or variant.get("name") or "").strip()
        if not name:
            raise ValueError(f"variant entry is missing a name: {variant}")
        raw_shards = variant.get("shards", [])
        if not isinstance(raw_shards, list):
            raise ValueError(f"variant {name} shards must be a list")
        for shard in raw_shards:
            if not isinstance(shard, dict):
                continue
            shards.append(
                ShardCommand(
                    variant=name,
                    offset=int(shard["offset"]),
                    limit=int(shard["limit"]),
                    command=str(shard["command"]),
                    summary_json=Path(str(shard["summary_json"])),
                    guard_json=Path(str(shard["guard_json"])),
                )
            )
    return shards


def select_shards(
    shards: list[ShardCommand],
    *,
    min_offset: int,
    max_offset: int,
    variants: set[str] | None,
) -> list[ShardCommand]:
    selected = [
        shard
        for shard in shards
        if shard.offset >= min_offset
        and shard.offset < max_offset
        and (variants is None or shard.variant in variants)
    ]
    return sorted(selected, key=lambda shard: (shard.offset, shard.variant))


def run_shards(shards: list[ShardCommand], *, log_dir: Path, dry_run: bool) -> int:
    log_dir.mkdir(parents=True, exist_ok=True)
    print(f"[runner] queued {len(shards)} shards", flush=True)
    for shard in shards:
        if shard.summary_json.exists() and shard.guard_json.exists():
            print(f"[runner] skip existing {shard.label}", flush=True)
            continue
        print(f"[runner] start {shard.label}", flush=True)
        if dry_run:
            print(shard.command, flush=True)
            continue
        started = time.time()
        log_path = log_dir / f"{shard.label}.log"
        with log_path.open("w", encoding="utf-8") as handle:
            handle.write(f"COMMAND: {shard.command}\n\n")
            handle.flush()
            proc = subprocess.Popen(
                shard.command,
                shell=True,
                stdout=handle,
                stderr=subprocess.STDOUT,
                text=True,
            )
            return_code = proc.wait()
        elapsed = time.time() - started
        print(
            f"[runner] done {shard.label} rc={return_code} elapsed={elapsed:.1f}s log={log_path}",
            flush=True,
        )
        if return_code != 0:
            tail = log_path.read_text(encoding="utf-8", errors="replace")[-4000:]
            print(tail, flush=True)
            return return_code
    print("[runner] selected shards complete", flush=True)
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan-json", type=Path, default=Path("outputs/mmlu_ptq_shard_plan_mmlu_full_2026_06_08.json"))
    parser.add_argument("--min-offset", type=int, default=0)
    parser.add_argument("--max-offset", type=int, default=10**9)
    parser.add_argument("--variant", action="append", default=[])
    parser.add_argument("--log-dir", type=Path, default=Path("outputs/run_logs"))
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.min_offset < 0 or args.max_offset <= args.min_offset:
        raise ValueError("--max-offset must be greater than --min-offset")
    variants = set(args.variant) if args.variant else None
    shards = select_shards(
        iter_shards(load_json(args.plan_json)),
        min_offset=args.min_offset,
        max_offset=args.max_offset,
        variants=variants,
    )
    return run_shards(shards, log_dir=args.log_dir, dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
