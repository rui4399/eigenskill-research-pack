#!/usr/bin/env python3
from __future__ import annotations

"""Gate fused selected-row ESMP sidecar generation evidence.

The sidecar experiment is intentionally narrow: it attaches fused selected-row
packed kernels to real HF generation activations, then discards the sidecar
output. This gate verifies that the integration actually ran inside generation
and stayed within bounded overhead/memory constraints. It does not certify
end-to-end acceleration.
"""

import argparse
import json
from pathlib import Path
from typing import Any


EXPECTED_MODE = "hf_generation_with_fused_selected_row_esmp_sidecar"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def finite_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number:
        return None
    return number


def positive_float(value: Any) -> float | None:
    number = finite_float(value)
    if number is None or number <= 0.0:
        return None
    return number


def sidecar_errors(sidecars: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    for index, sidecar in enumerate(sidecars):
        for error in sidecar.get("errors", []) or []:
            errors.append(f"sidecar[{index}] {error}")
    return errors


def observed_shapes(sidecars: list[dict[str, Any]]) -> set[str]:
    shapes: set[str] = set()
    for sidecar in sidecars:
        shapes.update(str(shape) for shape in sidecar.get("input_shapes", []) or [])
    return shapes


def parse_shape(shape: str) -> tuple[int, ...] | None:
    try:
        return tuple(int(part) for part in shape.split("x"))
    except ValueError:
        return None


def has_sequence_shape(shapes: set[str], sequence_len: int | None) -> bool:
    for shape in shapes:
        dims = parse_shape(shape)
        if dims is None or len(dims) < 2:
            continue
        if sequence_len is None and dims[1] > 1:
            return True
        if sequence_len is not None and dims[1] == sequence_len:
            return True
    return False


def check_guard(guard: dict[str, Any] | None, args: argparse.Namespace) -> list[str]:
    if guard is None:
        return []
    failures: list[str] = []
    if int(guard.get("returncode", -1)) != 0:
        failures.append(f"guarded command returncode {guard.get('returncode')} != 0")
    if guard.get("killed_by_guard"):
        failures.append("guard killed command for memory")
    if guard.get("killed_by_timeout"):
        failures.append("guard killed command for timeout")
    ratio = finite_float(guard.get("max_memory_used_ratio"))
    if ratio is None:
        failures.append("guard missing max_memory_used_ratio")
    elif ratio > args.max_memory_ratio:
        failures.append(f"guard max memory ratio {ratio:.4f} > {args.max_memory_ratio:.4f}")
    return failures


def text_matches(sidecar: dict[str, Any], baseline: dict[str, Any] | None) -> bool | None:
    if baseline is None:
        return None
    return str(sidecar.get("generated_text", "")) == str(baseline.get("generated_text", ""))


def throughput_ratio(sidecar: dict[str, Any], baseline: dict[str, Any] | None) -> float | None:
    if baseline is None:
        return None
    sidecar_tps = positive_float(sidecar.get("tokens_per_second"))
    baseline_tps = positive_float(baseline.get("tokens_per_second"))
    if sidecar_tps is None or baseline_tps is None:
        return None
    return sidecar_tps / baseline_tps


def build_result(
    sidecar: dict[str, Any],
    baseline: dict[str, Any] | None,
    guard: dict[str, Any] | None,
    args: argparse.Namespace,
) -> dict[str, Any]:
    failures: list[str] = []
    if sidecar.get("mode") != EXPECTED_MODE:
        failures.append(f"mode {sidecar.get('mode')!r} != {EXPECTED_MODE!r}")

    sidecars = list(sidecar.get("sidecars", []) or [])
    layers = list(sidecar.get("layers", []) or [])
    if len(sidecars) < args.min_sidecars:
        failures.append(f"sidecars {len(sidecars)} < {args.min_sidecars}")
    if len(layers) < args.min_layers:
        failures.append(f"layers {len(layers)} < {args.min_layers}")

    sidecar_call_count = int(sidecar.get("sidecar_call_count", 0) or 0)
    if sidecar_call_count < args.min_sidecar_calls:
        failures.append(f"sidecar calls {sidecar_call_count} < {args.min_sidecar_calls}")

    for index, item in enumerate(sidecars):
        calls = int(item.get("calls", 0) or 0)
        selected_rows = int(item.get("selected_rows_total", 0) or 0)
        if calls < args.min_calls_per_sidecar:
            failures.append(f"sidecar[{index}] calls {calls} < {args.min_calls_per_sidecar}")
        if selected_rows < args.min_selected_rows_total:
            failures.append(f"sidecar[{index}] selected rows {selected_rows} < {args.min_selected_rows_total}")

    for error in sidecar_errors(sidecars):
        failures.append(error)

    generated_tokens = int(sidecar.get("generated_tokens_text_retokenized", 0) or 0)
    if generated_tokens < args.min_generated_tokens:
        failures.append(f"generated tokens {generated_tokens} < {args.min_generated_tokens}")
    if positive_float(sidecar.get("ttft_seconds")) is None:
        failures.append("missing positive ttft_seconds")
    if positive_float(sidecar.get("elapsed_seconds")) is None:
        failures.append("missing positive elapsed_seconds")
    tokens_per_second = positive_float(sidecar.get("tokens_per_second"))
    if tokens_per_second is None or tokens_per_second < args.min_tokens_per_second:
        failures.append(f"tokens/s {tokens_per_second} < {args.min_tokens_per_second}")

    timing = dict(sidecar.get("sidecar_cuda_event_ms", {}) or {})
    timing_sum = positive_float(timing.get("sum"))
    timing_median = positive_float(timing.get("median"))
    timing_max = positive_float(timing.get("max"))
    if timing_sum is None:
        failures.append("missing positive sidecar CUDA sum ms")
    if timing_median is None:
        failures.append("missing positive sidecar CUDA median ms")
    elif timing_median > args.max_median_sidecar_ms:
        failures.append(f"sidecar median ms {timing_median:.6f} > {args.max_median_sidecar_ms:.6f}")
    if timing_max is None:
        failures.append("missing positive sidecar CUDA max ms")
    elif timing_max > args.max_max_sidecar_ms:
        failures.append(f"sidecar max ms {timing_max:.6f} > {args.max_max_sidecar_ms:.6f}")

    shapes = observed_shapes(sidecars)
    if args.require_prefill_shape and not has_sequence_shape(shapes, None):
        failures.append("missing multi-token prefill sidecar input shape")
    if args.require_decode_shape and not has_sequence_shape(shapes, 1):
        failures.append("missing single-token decode sidecar input shape")

    match = text_matches(sidecar, baseline)
    if baseline is not None and args.require_generated_text_match and match is not True:
        failures.append("generated text differs from baseline")
    ratio = throughput_ratio(sidecar, baseline)
    if baseline is not None and args.min_tps_ratio_vs_baseline > 0.0:
        if ratio is None:
            failures.append("missing throughput ratio vs baseline")
        elif ratio < args.min_tps_ratio_vs_baseline:
            failures.append(f"tokens/s ratio vs baseline {ratio:.4f} < {args.min_tps_ratio_vs_baseline:.4f}")

    failures.extend(check_guard(guard, args))

    return {
        "passed": not failures,
        "failures": failures,
        "summary": {
            "model": sidecar.get("model"),
            "mode": sidecar.get("mode"),
            "layers": layers,
            "sidecar_count": len(sidecars),
            "sidecar_call_count": sidecar_call_count,
            "generated_tokens": generated_tokens,
            "ttft_seconds": finite_float(sidecar.get("ttft_seconds")),
            "elapsed_seconds": finite_float(sidecar.get("elapsed_seconds")),
            "tokens_per_second": finite_float(sidecar.get("tokens_per_second")),
            "baseline_tokens_per_second": None if baseline is None else finite_float(baseline.get("tokens_per_second")),
            "tokens_per_second_ratio_vs_baseline": ratio,
            "generated_text_matches_baseline": match,
            "sidecar_sync_mode": sidecar.get("sidecar_sync_mode"),
            "selected_rows_per_module": sidecar.get("selected_rows_per_module"),
            "sidecar_cuda_event_ms": timing,
            "observed_input_shapes": sorted(shapes),
            "peak_gpu_memory_mib": finite_float(sidecar.get("peak_gpu_memory_mib")),
            "guard_max_memory_used_ratio": None if guard is None else guard.get("max_memory_used_ratio"),
            "guard_max_memory_used_mib": None if guard is None else guard.get("max_memory_used_mib"),
            "guard_memory_total_mib": None if guard is None else guard.get("memory_total_mib"),
        },
        "sidecars": [
            {
                "layer": item.get("layer"),
                "calls": item.get("calls"),
                "selected_rows_total": item.get("selected_rows_total"),
                "low_rows_total": item.get("low_rows_total"),
                "high_rows_total": item.get("high_rows_total"),
                "input_shapes": item.get("input_shapes", []),
                "cuda_event_ms": item.get("cuda_event_ms", {}),
                "errors": item.get("errors", []),
            }
            for item in sidecars
        ],
        "thresholds": {
            "min_layers": args.min_layers,
            "min_sidecars": args.min_sidecars,
            "min_sidecar_calls": args.min_sidecar_calls,
            "min_calls_per_sidecar": args.min_calls_per_sidecar,
            "min_selected_rows_total": args.min_selected_rows_total,
            "min_generated_tokens": args.min_generated_tokens,
            "min_tokens_per_second": args.min_tokens_per_second,
            "max_median_sidecar_ms": args.max_median_sidecar_ms,
            "max_max_sidecar_ms": args.max_max_sidecar_ms,
            "require_prefill_shape": args.require_prefill_shape,
            "require_decode_shape": args.require_decode_shape,
            "require_generated_text_match": args.require_generated_text_match,
            "min_tps_ratio_vs_baseline": args.min_tps_ratio_vs_baseline,
            "max_memory_ratio": args.max_memory_ratio,
        },
    }


def fmt(value: Any, digits: int = 4) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    summary = result["summary"]
    timing = summary["sidecar_cuda_event_ms"]
    lines = [
        "# Fused Sidecar Generation Gate",
        "",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- model: `{summary['model']}`",
        f"- layers: `{summary['layers']}`",
        f"- sidecars: {summary['sidecar_count']}",
        f"- sidecar calls: {summary['sidecar_call_count']}",
        f"- sync mode: `{summary['sidecar_sync_mode']}`",
        f"- generated tokens: {summary['generated_tokens']}",
        f"- TTFT: {fmt(summary['ttft_seconds'], 6)} s",
        f"- tokens/s: {fmt(summary['tokens_per_second'])}",
        f"- baseline tokens/s: {fmt(summary['baseline_tokens_per_second'])}",
        f"- tokens/s ratio vs baseline: {fmt(summary['tokens_per_second_ratio_vs_baseline'])}",
        f"- generated text matches baseline: {summary['generated_text_matches_baseline']}",
        f"- sidecar CUDA sum/median/max ms: {fmt(timing.get('sum'), 6)} / {fmt(timing.get('median'), 6)} / {fmt(timing.get('max'), 6)}",
        f"- observed input shapes: `{summary['observed_input_shapes']}`",
        f"- guard peak memory: {summary['guard_max_memory_used_mib']} / {summary['guard_memory_total_mib']} MiB ({fmt(summary['guard_max_memory_used_ratio'])})",
        "",
        "## Sidecars",
        "",
        "| layer | calls | selected rows | low rows | high rows | median ms | max ms | shapes | errors |",
        "|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for item in result["sidecars"]:
        cuda = item.get("cuda_event_ms", {}) or {}
        errors = item.get("errors", []) or []
        lines.append(
            f"| {item.get('layer')} | {item.get('calls')} | {item.get('selected_rows_total')} | "
            f"{item.get('low_rows_total')} | {item.get('high_rows_total')} | "
            f"{fmt(cuda.get('median'), 6)} | {fmt(cuda.get('max'), 6)} | "
            f"`{item.get('input_shapes', [])}` | {len(errors)} |"
        )
    lines.extend(["", "## Failures", ""])
    if result["failures"]:
        lines.extend(f"- {failure}" for failure in result["failures"])
    else:
        lines.append("- none")
    lines.extend(
        [
            "",
            "## Claim Boundary",
            "",
            "- Valid claim: fused selected-row ESMP kernels execute inside real HF generation hooks with bounded measured overhead and guard-limited VRAM.",
            "- Invalid claim: this sidecar run proves end-to-end LLM acceleration, because dense QKV is still executed.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate fused selected-row ESMP sidecar generation evidence.")
    parser.add_argument("--generation-json", type=Path, required=True)
    parser.add_argument("--baseline-json", type=Path, default=None)
    parser.add_argument("--guard-json", type=Path, default=None)
    parser.add_argument("--out-json", type=Path, default=Path("outputs/real_system_packer_2026-06-05/fused_sidecar_generation_gate.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/real_system_packer_2026-06-05/FUSED_SIDECAR_GENERATION_GATE.md"))
    parser.add_argument("--min-layers", type=int, default=1)
    parser.add_argument("--min-sidecars", type=int, default=1)
    parser.add_argument("--min-sidecar-calls", type=int, default=1)
    parser.add_argument("--min-calls-per-sidecar", type=int, default=1)
    parser.add_argument("--min-selected-rows-total", type=int, default=1)
    parser.add_argument("--min-generated-tokens", type=int, default=1)
    parser.add_argument("--min-tokens-per-second", type=float, default=1.0)
    parser.add_argument("--max-median-sidecar-ms", type=float, default=10.0)
    parser.add_argument("--max-max-sidecar-ms", type=float, default=50.0)
    parser.add_argument("--require-prefill-shape", action="store_true")
    parser.add_argument("--require-decode-shape", action="store_true")
    parser.add_argument("--require-generated-text-match", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--min-tps-ratio-vs-baseline", type=float, default=0.0)
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    args = parser.parse_args()

    baseline = load_json(args.baseline_json) if args.baseline_json else None
    guard = load_json(args.guard_json) if args.guard_json else None
    result = build_result(load_json(args.generation_json), baseline, guard, args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "failures": result["failures"], "out_json": str(args.out_json)}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
