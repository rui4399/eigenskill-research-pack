#!/usr/bin/env python3
from __future__ import annotations

"""Gate fused ESMP QKV replacement generation evidence.

This gate is stricter than the sidecar gate because the measured path replaces
selected q_proj/k_proj/v_proj modules inside Hugging Face generation. It still
does not certify quality-preserving quantization; it verifies that the fused
replacement path executes, compresses weights, reuses QKV cache slices, and
stays within bounded latency/memory thresholds on the measured smoke.
"""

import argparse
import json
from pathlib import Path
from typing import Any


EXPECTED_MODE = "hf_generation_with_fused_esmp_qkv_replacement"


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


def common_prefix_len(left: str, right: str) -> int:
    count = 0
    for a, b in zip(left, right):
        if a != b:
            break
        count += 1
    return count


def throughput_ratio(replacement: dict[str, Any], baseline: dict[str, Any] | None) -> float | None:
    if baseline is None:
        return None
    replacement_tps = positive_float(replacement.get("tokens_per_second"))
    baseline_tps = positive_float(baseline.get("tokens_per_second"))
    if replacement_tps is None or baseline_tps is None:
        return None
    return replacement_tps / baseline_tps


def ttft_ratio(replacement: dict[str, Any], baseline: dict[str, Any] | None) -> float | None:
    if baseline is None:
        return None
    replacement_ttft = positive_float(replacement.get("ttft_seconds"))
    baseline_ttft = positive_float(baseline.get("ttft_seconds"))
    if replacement_ttft is None or baseline_ttft is None:
        return None
    return replacement_ttft / baseline_ttft


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


def build_result(
    replacement: dict[str, Any],
    baseline: dict[str, Any] | None,
    guard: dict[str, Any] | None,
    args: argparse.Namespace,
) -> dict[str, Any]:
    failures: list[str] = []
    if replacement.get("mode") != EXPECTED_MODE:
        failures.append(f"mode {replacement.get('mode')!r} != {EXPECTED_MODE!r}")

    replacements = list(replacement.get("replacements", []) or [])
    replacement_count = int(replacement.get("replacement_count", len(replacements)) or 0)
    if replacement_count < args.min_replacements:
        failures.append(f"replacement count {replacement_count} < {args.min_replacements}")
    if len(replacements) < args.min_replacements:
        failures.append(f"replacement records {len(replacements)} < {args.min_replacements}")

    generated_tokens = int(replacement.get("generated_tokens_text_retokenized", 0) or 0)
    if generated_tokens < args.min_generated_tokens:
        failures.append(f"generated tokens {generated_tokens} < {args.min_generated_tokens}")
    if positive_float(replacement.get("ttft_seconds")) is None:
        failures.append("missing positive ttft_seconds")
    if positive_float(replacement.get("elapsed_seconds")) is None:
        failures.append("missing positive elapsed_seconds")
    tokens_per_second = positive_float(replacement.get("tokens_per_second"))
    if tokens_per_second is None or tokens_per_second < args.min_tokens_per_second:
        failures.append(f"tokens/s {tokens_per_second} < {args.min_tokens_per_second}")

    compression = finite_float(replacement.get("replacement_compression_vs_fp32"))
    if compression is None or compression < args.min_compression_vs_fp32:
        failures.append(f"compression vs FP32 {compression} < {args.min_compression_vs_fp32}")

    timing = dict(replacement.get("replacement_cuda_event_ms", {}) or {})
    timing_median = positive_float(timing.get("median"))
    timing_max = positive_float(timing.get("max"))
    if timing_median is None:
        failures.append("missing positive replacement CUDA median ms")
    elif timing_median > args.max_median_replacement_ms:
        failures.append(f"replacement median ms {timing_median:.6f} > {args.max_median_replacement_ms:.6f}")
    if timing_max is None:
        failures.append("missing positive replacement CUDA max ms")
    elif timing_max > args.max_max_replacement_ms:
        failures.append(f"replacement max ms {timing_max:.6f} > {args.max_max_replacement_ms:.6f}")

    total_wrapper_calls = 0
    total_fused_compute_calls = 0
    total_cache_hits = 0
    total_cache_misses = 0
    for index, item in enumerate(replacements):
        wrapper_calls = int(item.get("wrapper_calls", 0) or 0)
        fused_compute_calls = int(item.get("fused_compute_calls", 0) or 0)
        cache_hits = int(item.get("cache_hits", 0) or 0)
        cache_misses = int(item.get("cache_misses", 0) or 0)
        total_wrapper_calls += wrapper_calls
        total_fused_compute_calls += fused_compute_calls
        total_cache_hits += cache_hits
        total_cache_misses += cache_misses
        if wrapper_calls < args.min_wrapper_calls_per_replacement:
            failures.append(f"replacement[{index}] wrapper calls {wrapper_calls} < {args.min_wrapper_calls_per_replacement}")
        if fused_compute_calls < args.min_fused_compute_calls_per_replacement:
            failures.append(f"replacement[{index}] fused compute calls {fused_compute_calls} < {args.min_fused_compute_calls_per_replacement}")
        if cache_hits < args.min_cache_hits_per_replacement:
            failures.append(f"replacement[{index}] cache hits {cache_hits} < {args.min_cache_hits_per_replacement}")
        if cache_misses < args.min_cache_misses_per_replacement:
            failures.append(f"replacement[{index}] cache misses {cache_misses} < {args.min_cache_misses_per_replacement}")
        if wrapper_calls != fused_compute_calls + cache_hits:
            failures.append(
                f"replacement[{index}] wrapper calls {wrapper_calls} != fused compute {fused_compute_calls} + cache hits {cache_hits}"
            )
        if fused_compute_calls != cache_misses:
            failures.append(f"replacement[{index}] fused compute calls {fused_compute_calls} != cache misses {cache_misses}")

    tps_ratio = throughput_ratio(replacement, baseline)
    if baseline is not None and args.min_tps_ratio_vs_baseline > 0.0:
        if tps_ratio is None:
            failures.append("missing throughput ratio vs baseline")
        elif tps_ratio < args.min_tps_ratio_vs_baseline:
            failures.append(f"tokens/s ratio vs baseline {tps_ratio:.4f} < {args.min_tps_ratio_vs_baseline:.4f}")

    first_token_ratio = ttft_ratio(replacement, baseline)
    if baseline is not None and args.max_ttft_ratio_vs_baseline > 0.0:
        if first_token_ratio is None:
            failures.append("missing TTFT ratio vs baseline")
        elif first_token_ratio > args.max_ttft_ratio_vs_baseline:
            failures.append(f"TTFT ratio vs baseline {first_token_ratio:.4f} > {args.max_ttft_ratio_vs_baseline:.4f}")

    prefix_len: int | None = None
    exact_text_match: bool | None = None
    if baseline is not None:
        output = str(replacement.get("generated_text", ""))
        baseline_output = str(baseline.get("generated_text", ""))
        exact_text_match = output == baseline_output
        prefix_len = common_prefix_len(output, baseline_output)
        if args.require_generated_text_match and not exact_text_match:
            failures.append("generated text differs from baseline")
        if prefix_len < args.min_common_prefix_chars:
            failures.append(f"common prefix chars {prefix_len} < {args.min_common_prefix_chars}")

    failures.extend(check_guard(guard, args))

    return {
        "passed": not failures,
        "failures": failures,
        "summary": {
            "model": replacement.get("model"),
            "mode": replacement.get("mode"),
            "layers": replacement.get("layers", []),
            "replacement_count": replacement_count,
            "generated_tokens": generated_tokens,
            "ttft_seconds": finite_float(replacement.get("ttft_seconds")),
            "elapsed_seconds": finite_float(replacement.get("elapsed_seconds")),
            "tokens_per_second": finite_float(replacement.get("tokens_per_second")),
            "baseline_tokens_per_second": None if baseline is None else finite_float(baseline.get("tokens_per_second")),
            "tokens_per_second_ratio_vs_baseline": tps_ratio,
            "baseline_ttft_seconds": None if baseline is None else finite_float(baseline.get("ttft_seconds")),
            "ttft_ratio_vs_baseline": first_token_ratio,
            "generated_text_exact_match": exact_text_match,
            "common_prefix_chars": prefix_len,
            "replacement_compression_vs_fp32": compression,
            "replacement_cuda_event_ms": timing,
            "total_wrapper_calls": total_wrapper_calls,
            "total_fused_compute_calls": total_fused_compute_calls,
            "total_cache_hits": total_cache_hits,
            "total_cache_misses": total_cache_misses,
            "peak_gpu_memory_mib": finite_float(replacement.get("peak_gpu_memory_mib")),
            "guard_max_memory_used_ratio": None if guard is None else guard.get("max_memory_used_ratio"),
            "guard_max_memory_used_mib": None if guard is None else guard.get("max_memory_used_mib"),
            "guard_memory_total_mib": None if guard is None else guard.get("memory_total_mib"),
        },
        "replacements": [
            {
                "modules": item.get("modules", []),
                "wrapper_calls": item.get("wrapper_calls"),
                "fused_compute_calls": item.get("fused_compute_calls"),
                "cache_hits": item.get("cache_hits"),
                "cache_misses": item.get("cache_misses"),
                "compression_vs_fp32": item.get("compression_vs_fp32"),
                "input_shapes": item.get("input_shapes", []),
                "cuda_event_ms": item.get("cuda_event_ms", {}),
            }
            for item in replacements
        ],
        "thresholds": {
            "min_replacements": args.min_replacements,
            "min_generated_tokens": args.min_generated_tokens,
            "min_tokens_per_second": args.min_tokens_per_second,
            "min_compression_vs_fp32": args.min_compression_vs_fp32,
            "max_median_replacement_ms": args.max_median_replacement_ms,
            "max_max_replacement_ms": args.max_max_replacement_ms,
            "min_wrapper_calls_per_replacement": args.min_wrapper_calls_per_replacement,
            "min_fused_compute_calls_per_replacement": args.min_fused_compute_calls_per_replacement,
            "min_cache_hits_per_replacement": args.min_cache_hits_per_replacement,
            "min_cache_misses_per_replacement": args.min_cache_misses_per_replacement,
            "min_tps_ratio_vs_baseline": args.min_tps_ratio_vs_baseline,
            "max_ttft_ratio_vs_baseline": args.max_ttft_ratio_vs_baseline,
            "require_generated_text_match": args.require_generated_text_match,
            "min_common_prefix_chars": args.min_common_prefix_chars,
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
    timing = summary["replacement_cuda_event_ms"]
    lines = [
        "# Fused QKV Replacement Generation Gate",
        "",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- model: `{summary['model']}`",
        f"- layers: `{summary['layers']}`",
        f"- replacements: {summary['replacement_count']}",
        f"- generated tokens: {summary['generated_tokens']}",
        f"- TTFT: {fmt(summary['ttft_seconds'], 6)} s",
        f"- baseline TTFT: {fmt(summary['baseline_ttft_seconds'], 6)} s",
        f"- TTFT ratio vs baseline: {fmt(summary['ttft_ratio_vs_baseline'])}",
        f"- tokens/s: {fmt(summary['tokens_per_second'])}",
        f"- baseline tokens/s: {fmt(summary['baseline_tokens_per_second'])}",
        f"- tokens/s ratio vs baseline: {fmt(summary['tokens_per_second_ratio_vs_baseline'])}",
        f"- exact text match: {summary['generated_text_exact_match']}",
        f"- common prefix chars: {summary['common_prefix_chars']}",
        f"- compression vs FP32: {fmt(summary['replacement_compression_vs_fp32'])}x",
        f"- wrapper/fused/cache-hit/cache-miss calls: {summary['total_wrapper_calls']} / {summary['total_fused_compute_calls']} / {summary['total_cache_hits']} / {summary['total_cache_misses']}",
        f"- replacement CUDA median/max ms: {fmt(timing.get('median'), 6)} / {fmt(timing.get('max'), 6)}",
        f"- guard peak memory: {summary['guard_max_memory_used_mib']} / {summary['guard_memory_total_mib']} MiB ({fmt(summary['guard_max_memory_used_ratio'])})",
        "",
        "## Replacements",
        "",
        "| index | modules | wrapper | fused | hits | misses | compression | median ms | max ms | shapes |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for index, item in enumerate(result["replacements"]):
        cuda = item.get("cuda_event_ms", {}) or {}
        modules = ", ".join(str(module).split(".")[-1] for module in item.get("modules", []))
        lines.append(
            f"| {index} | `{modules}` | {item.get('wrapper_calls')} | {item.get('fused_compute_calls')} | "
            f"{item.get('cache_hits')} | {item.get('cache_misses')} | {fmt(item.get('compression_vs_fp32'))}x | "
            f"{fmt(cuda.get('median'), 6)} | {fmt(cuda.get('max'), 6)} | `{item.get('input_shapes', [])}` |"
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
            "- Valid claim: selected QKV projections can be replaced by the fused ESMP runtime in a guarded HF generation smoke, with measured compression, QKV cache reuse, TTFT, and throughput.",
            "- Invalid claim: this is a quality-preserving full-model quantizer or a production Tensor Core runtime.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate fused ESMP QKV replacement generation evidence.")
    parser.add_argument("--generation-json", type=Path, required=True)
    parser.add_argument("--baseline-json", type=Path, default=None)
    parser.add_argument("--guard-json", type=Path, default=None)
    parser.add_argument("--out-json", type=Path, default=Path("outputs/real_system_packer_2026-06-05/fused_qkv_generation_gate.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/real_system_packer_2026-06-05/FUSED_QKV_GENERATION_GATE.md"))
    parser.add_argument("--min-replacements", type=int, default=1)
    parser.add_argument("--min-generated-tokens", type=int, default=1)
    parser.add_argument("--min-tokens-per-second", type=float, default=1.0)
    parser.add_argument("--min-compression-vs-fp32", type=float, default=1.0)
    parser.add_argument("--max-median-replacement-ms", type=float, default=10.0)
    parser.add_argument("--max-max-replacement-ms", type=float, default=50.0)
    parser.add_argument("--min-wrapper-calls-per-replacement", type=int, default=1)
    parser.add_argument("--min-fused-compute-calls-per-replacement", type=int, default=1)
    parser.add_argument("--min-cache-hits-per-replacement", type=int, default=0)
    parser.add_argument("--min-cache-misses-per-replacement", type=int, default=1)
    parser.add_argument("--min-tps-ratio-vs-baseline", type=float, default=0.0)
    parser.add_argument("--max-ttft-ratio-vs-baseline", type=float, default=0.0)
    parser.add_argument("--require-generated-text-match", action=argparse.BooleanOptionalAction, default=False)
    parser.add_argument("--min-common-prefix-chars", type=int, default=0)
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
