#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import signal
import subprocess
import sys
import time
from pathlib import Path


def query_gpu() -> dict:
    proc = subprocess.run(
        [
            "nvidia-smi",
            "--query-gpu=utilization.gpu,memory.used,memory.total",
            "--format=csv,noheader,nounits",
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=10,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "nvidia-smi failed")
    first = proc.stdout.strip().splitlines()[0]
    util, used, total = [int(part.strip()) for part in first.split(",")[:3]]
    return {
        "utilization_gpu_pct": util,
        "memory_used_mib": used,
        "memory_total_mib": total,
        "memory_used_ratio": used / max(total, 1),
    }


def terminate(proc: subprocess.Popen) -> None:
    if proc.poll() is not None:
        return
    if sys.platform.startswith("win"):
        proc.terminate()
    else:
        proc.send_signal(signal.SIGTERM)
    try:
        proc.wait(timeout=10)
    except subprocess.TimeoutExpired:
        proc.kill()


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a command while enforcing a GPU memory guard.")
    parser.add_argument("--max-memory-ratio", type=float, default=0.85)
    parser.add_argument("--poll-seconds", type=float, default=2.0)
    parser.add_argument("--out", default="")
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    if args.command and args.command[0] == "--":
        args.command = args.command[1:]
    if not args.command:
        raise SystemExit("missing command after --")
    if not 0.0 < args.max_memory_ratio <= 1.0:
        raise SystemExit("--max-memory-ratio must be in (0, 1]")

    samples: list[dict] = []
    start_state = query_gpu()
    if start_state["memory_used_ratio"] > args.max_memory_ratio:
        raise SystemExit(
            f"GPU memory already above guard: {start_state['memory_used_mib']}/"
            f"{start_state['memory_total_mib']} MiB"
        )

    proc = subprocess.Popen(args.command)
    killed = False
    try:
        while proc.poll() is None:
            sample = query_gpu()
            sample["t_seconds"] = time.time()
            samples.append(sample)
            if sample["memory_used_ratio"] > args.max_memory_ratio:
                killed = True
                terminate(proc)
                break
            time.sleep(args.poll_seconds)
    finally:
        terminate(proc)

    end_state = query_gpu()
    max_sample = max(samples, key=lambda item: item["memory_used_ratio"], default=start_state)
    result = {
        "command": args.command,
        "returncode": proc.returncode,
        "killed_by_guard": killed,
        "max_memory_used_mib": max_sample["memory_used_mib"],
        "memory_total_mib": max_sample["memory_total_mib"],
        "max_memory_used_ratio": max_sample["memory_used_ratio"],
        "max_utilization_gpu_pct": max((item["utilization_gpu_pct"] for item in samples), default=start_state["utilization_gpu_pct"]),
        "start_state": start_state,
        "end_state": end_state,
        "samples": samples,
    }
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if killed:
        raise SystemExit(90)
    raise SystemExit(proc.returncode or 0)


if __name__ == "__main__":
    main()
