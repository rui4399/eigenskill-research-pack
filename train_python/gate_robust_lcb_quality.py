#!/usr/bin/env python3
from __future__ import annotations

"""Gate robust-LCB downstream fake-quant PPL boundary evidence.

The robust-LCB policy is intentionally conservative. This gate checks that the
target robust-LCB allocation improves over uniform INT4 on the measured prompt
slices while recording whether it beats the mean-consensus allocation. The
mean comparison is reported, not required, so negative evidence remains visible.
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_case_spec(spec: str) -> tuple[str, Path, Path]:
    parts = spec.split("=")
    if len(parts) != 3 or not all(part.strip() for part in parts):
        raise ValueError(f"case must be LABEL=PPL_JSON=GUARD_JSON: {spec}")
    return parts[0].strip(), Path(parts[1].strip()), Path(parts[2].strip())


def result_by_name(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(item.get("name")): item for item in payload.get("results", []) or []}


def ppl_for(results: dict[str, dict[str, Any]], name: str) -> float | None:
    item = results.get(name)
    if not item:
        return None
    try:
        return float(item.get("metrics", {}).get("ppl"))
    except (TypeError, ValueError):
        return None


def guard_summary(guard: dict[str, Any]) -> dict[str, Any]:
    return {
        "returncode": int(guard.get("returncode", -1)),
        "killed_by_guard": bool(guard.get("killed_by_guard")),
        "killed_by_timeout": bool(guard.get("killed_by_timeout")),
        "max_memory_used_ratio": float(guard.get("max_memory_used_ratio") or 0.0),
        "max_utilization_gpu_pct": int(guard.get("max_utilization_gpu_pct") or 0),
    }


def case_summary(
    label: str,
    ppl_path: str | Path,
    ppl_payload: dict[str, Any],
    guard_path: str | Path,
    guard_payload: dict[str, Any],
    *,
    target_config: str = "wikitext_c4_robust_lcb",
    uniform_config: str = "uniform_int4",
    mean_config: str = "wikitext_c4_mean_consensus",
) -> dict[str, Any]:
    results = result_by_name(ppl_payload)
    fp16_ppl = ppl_for(results, "fp16")
    uniform_ppl = ppl_for(results, uniform_config)
    mean_ppl = ppl_for(results, mean_config)
    target_ppl = ppl_for(results, target_config)
    guard = guard_summary(guard_payload)
    return {
        "label": label,
        "ppl_path": str(ppl_path),
        "guard_path": str(guard_path),
        "model": ppl_payload.get("model", ""),
        "prompt_count": int(ppl_payload.get("prompt_count") or 0),
        "max_length": int(ppl_payload.get("max_length") or 0),
        "fp16_ppl": fp16_ppl,
        "uniform_ppl": uniform_ppl,
        "mean_ppl": mean_ppl,
        "target_ppl": target_ppl,
        "target_margin_vs_uniform": (uniform_ppl - target_ppl) if uniform_ppl is not None and target_ppl is not None else None,
        "target_margin_vs_mean": (mean_ppl - target_ppl) if mean_ppl is not None and target_ppl is not None else None,
        "target_beats_uniform": bool(target_ppl is not None and uniform_ppl is not None and target_ppl < uniform_ppl),
        "target_beats_mean": bool(target_ppl is not None and mean_ppl is not None and target_ppl < mean_ppl),
        "guard": guard,
    }


def build_result(cases: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    failures: list[str] = []
    if len(cases) < args.min_cases:
        failures.append(f"case count {len(cases)} < required {args.min_cases}")
    for case in cases:
        for key in ("fp16_ppl", "uniform_ppl", "mean_ppl", "target_ppl"):
            if case[key] is None:
                failures.append(f"{case['label']}: missing {key}")
        guard = case["guard"]
        if guard["returncode"] != 0:
            failures.append(f"{case['label']}: guarded command returncode {guard['returncode']}")
        if guard["killed_by_guard"]:
            failures.append(f"{case['label']}: killed by GPU guard")
        if guard["killed_by_timeout"]:
            failures.append(f"{case['label']}: killed by timeout")
        if guard["max_memory_used_ratio"] > args.max_memory_ratio:
            failures.append(
                f"{case['label']}: memory ratio {guard['max_memory_used_ratio']:.4f} > {args.max_memory_ratio:.4f}"
            )
        if args.require_target_beats_uniform and not case["target_beats_uniform"]:
            failures.append(
                f"{case['label']}: target {args.target_config!r} does not beat uniform {args.uniform_config!r}"
            )

    target_wins_vs_uniform = sum(1 for case in cases if case["target_beats_uniform"])
    target_wins_vs_mean = sum(1 for case in cases if case["target_beats_mean"])
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "case_count": len(cases),
            "target_config": args.target_config,
            "uniform_config": args.uniform_config,
            "mean_config": args.mean_config,
            "target_wins_vs_uniform": target_wins_vs_uniform,
            "target_wins_vs_mean": target_wins_vs_mean,
            "max_guard_vram_ratio": max((case["guard"]["max_memory_used_ratio"] for case in cases), default=0.0),
            "mean_target_margin_vs_uniform": sum(
                float(case["target_margin_vs_uniform"] or 0.0) for case in cases
            )
            / max(len(cases), 1),
            "mean_target_margin_vs_mean": sum(float(case["target_margin_vs_mean"] or 0.0) for case in cases)
            / max(len(cases), 1),
        },
        "cases": cases,
        "failures": failures,
        "claim_boundary": (
            "Valid claim: on the measured guarded Qwen3-0.6B fake-quant PPL slices, robust-LCB improves over "
            "uniform INT4 and its comparison against mean consensus is explicitly reported. Invalid claim: "
            "this proves robust-LCB is the best allocation policy or establishes SOTA quantization quality."
        ),
    }


def fmt(value: Any) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    lines = [
        "# Robust LCB Quality Boundary Gate",
        "",
        f"Date: `{result['date']}`",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        f"Cases: `{result['summary']['case_count']}`",
        f"Target wins vs uniform: `{result['summary']['target_wins_vs_uniform']}`",
        f"Target wins vs mean consensus: `{result['summary']['target_wins_vs_mean']}`",
        f"Max guard VRAM ratio: `{result['summary']['max_guard_vram_ratio']:.4f}`",
        "",
        "## Cases",
        "",
        "| case | FP16 PPL | uniform INT4 | mean consensus | robust LCB | margin vs uniform | margin vs mean | VRAM | source |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for case in result["cases"]:
        lines.append(
            f"| `{case['label']}` | {fmt(case['fp16_ppl'])} | {fmt(case['uniform_ppl'])} | "
            f"{fmt(case['mean_ppl'])} | {fmt(case['target_ppl'])} | "
            f"{fmt(case['target_margin_vs_uniform'])} | {fmt(case['target_margin_vs_mean'])} | "
            f"{case['guard']['max_memory_used_ratio']:.4f} | `{str(case['ppl_path']).replace(chr(92), '/')}` |"
        )
    lines.extend(["", "## Failures", ""])
    if result["failures"]:
        for failure in result["failures"]:
            lines.append(f"- {failure}")
    else:
        lines.append("- none")
    lines.extend(["", "## Claim Boundary", "", f"- {result['claim_boundary']}"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate robust-LCB downstream fake-quant PPL boundary evidence.")
    parser.add_argument("--case", action="append", required=True, help="LABEL=PPL_JSON=GUARD_JSON")
    parser.add_argument("--min-cases", type=int, default=2)
    parser.add_argument("--target-config", default="wikitext_c4_robust_lcb")
    parser.add_argument("--uniform-config", default="uniform_int4")
    parser.add_argument("--mean-config", default="wikitext_c4_mean_consensus")
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    parser.add_argument("--require-target-beats-uniform", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    cases = []
    for label, ppl_path, guard_path in map(parse_case_spec, args.case):
        cases.append(
            case_summary(
                label,
                ppl_path,
                load_json(ppl_path),
                guard_path,
                load_json(guard_path),
                target_config=args.target_config,
                uniform_config=args.uniform_config,
                mean_config=args.mean_config,
            )
        )
    result = build_result(cases, args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "summary": result["summary"], "out_json": str(args.out_json)}, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
