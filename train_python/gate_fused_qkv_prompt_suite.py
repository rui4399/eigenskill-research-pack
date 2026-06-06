#!/usr/bin/env python3
from __future__ import annotations

"""Gate fused ESMP QKV prompt-suite quality evidence.

This gate complements single-prompt generation gates. It verifies that a fused
QKV replacement candidate preserves outputs across a small prompt suite, keeps
rule-scored task behavior from regressing when a scored file is provided, and
still satisfies runtime/cache/guard sanity checks.
"""

import argparse
import json
from pathlib import Path
from typing import Any


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


def median_ttft_ratio(prompt_suite: dict[str, Any]) -> float | None:
    aggregate = prompt_suite.get("aggregate", {}) or {}
    baseline = finite_float(aggregate.get("median_baseline_ttft_seconds"))
    fused = finite_float(aggregate.get("median_fused_ttft_seconds"))
    if baseline is None or fused is None or baseline <= 0.0:
        return None
    return fused / baseline


def build_result(
    prompt_suite: dict[str, Any],
    scored: dict[str, Any] | None,
    guard: dict[str, Any] | None,
    args: argparse.Namespace,
) -> dict[str, Any]:
    failures: list[str] = []
    aggregate = prompt_suite.get("aggregate", {}) or {}
    prompts = int(aggregate.get("prompts", 0) or 0)
    exact_matches = int(aggregate.get("exact_matches", 0) or 0)
    exact_rate = finite_float(aggregate.get("exact_match_rate"))
    mean_similarity = finite_float(aggregate.get("mean_char_edit_similarity"))
    median_similarity = finite_float(aggregate.get("median_char_edit_similarity"))
    mean_prefix = finite_float(aggregate.get("mean_common_prefix_ratio"))
    speed_ratio = finite_float(aggregate.get("mean_speedup_fused_vs_baseline"))
    ttft_ratio = median_ttft_ratio(prompt_suite)
    compression = finite_float(prompt_suite.get("replacement_compression_vs_fp32"))
    median_cuda_ms = finite_float((prompt_suite.get("replacement_cuda_event_ms", {}) or {}).get("median"))

    if prompts < args.min_prompts:
        failures.append(f"prompts {prompts} < {args.min_prompts}")
    if exact_matches < args.min_exact_matches:
        failures.append(f"exact matches {exact_matches} < {args.min_exact_matches}")
    if exact_rate is None or exact_rate < args.min_exact_match_rate:
        failures.append(f"exact match rate {exact_rate} < {args.min_exact_match_rate}")
    if mean_similarity is None or mean_similarity < args.min_mean_char_edit_similarity:
        failures.append(f"mean char edit similarity {mean_similarity} < {args.min_mean_char_edit_similarity}")
    if median_similarity is None or median_similarity < args.min_median_char_edit_similarity:
        failures.append(f"median char edit similarity {median_similarity} < {args.min_median_char_edit_similarity}")
    if mean_prefix is None or mean_prefix < args.min_mean_common_prefix_ratio:
        failures.append(f"mean common prefix ratio {mean_prefix} < {args.min_mean_common_prefix_ratio}")
    if speed_ratio is None or speed_ratio < args.min_mean_speed_ratio:
        failures.append(f"mean speed ratio {speed_ratio} < {args.min_mean_speed_ratio}")
    if ttft_ratio is None or ttft_ratio > args.max_median_ttft_ratio:
        failures.append(f"median TTFT ratio {ttft_ratio} > {args.max_median_ttft_ratio}")
    if compression is None or compression < args.min_compression_vs_fp32:
        failures.append(f"compression vs FP32 {compression} < {args.min_compression_vs_fp32}")
    if median_cuda_ms is None or median_cuda_ms > args.max_median_replacement_ms:
        failures.append(f"median replacement CUDA ms {median_cuda_ms} > {args.max_median_replacement_ms}")

    wrapper_calls = int(prompt_suite.get("replacement_wrapper_calls", 0) or 0)
    fused_compute_calls = int(prompt_suite.get("replacement_fused_compute_calls", 0) or 0)
    cache_hits = int(prompt_suite.get("replacement_cache_hits", 0) or 0)
    cache_misses = int(prompt_suite.get("replacement_cache_misses", 0) or 0)
    if wrapper_calls < args.min_wrapper_calls:
        failures.append(f"wrapper calls {wrapper_calls} < {args.min_wrapper_calls}")
    if fused_compute_calls < args.min_fused_compute_calls:
        failures.append(f"fused compute calls {fused_compute_calls} < {args.min_fused_compute_calls}")
    if cache_hits < args.min_cache_hits:
        failures.append(f"cache hits {cache_hits} < {args.min_cache_hits}")
    if cache_misses < args.min_cache_misses:
        failures.append(f"cache misses {cache_misses} < {args.min_cache_misses}")
    if wrapper_calls != fused_compute_calls + cache_hits:
        failures.append(f"wrapper calls {wrapper_calls} != fused compute {fused_compute_calls} + cache hits {cache_hits}")
    if fused_compute_calls != cache_misses:
        failures.append(f"fused compute calls {fused_compute_calls} != cache misses {cache_misses}")

    scored_summary = None
    if scored is not None:
        scored_agg = scored.get("aggregate", {}) or {}
        scored_prompts = int(scored_agg.get("prompts", 0) or 0)
        baseline_passes = int(scored_agg.get("baseline_passes", 0) or 0)
        fused_passes = int(scored_agg.get("fused_passes", 0) or 0)
        regressions = int(scored_agg.get("regressions", 0) or 0)
        fused_pass_rate = finite_float(scored_agg.get("fused_pass_rate"))
        if scored_prompts < args.min_scored_prompts:
            failures.append(f"scored prompts {scored_prompts} < {args.min_scored_prompts}")
        if regressions > args.max_rule_regressions:
            failures.append(f"rule regressions {regressions} > {args.max_rule_regressions}")
        if fused_pass_rate is None or fused_pass_rate < args.min_fused_rule_pass_rate:
            failures.append(f"fused rule pass rate {fused_pass_rate} < {args.min_fused_rule_pass_rate}")
        if fused_passes + args.max_fused_rule_pass_drop < baseline_passes:
            failures.append(
                f"fused rule passes {fused_passes} + allowed drop {args.max_fused_rule_pass_drop} < baseline passes {baseline_passes}"
            )
        scored_summary = {
            "prompts": scored_prompts,
            "baseline_passes": baseline_passes,
            "fused_passes": fused_passes,
            "fused_pass_rate": fused_pass_rate,
            "regressions": regressions,
            "improvements": int(scored_agg.get("improvements", 0) or 0),
            "rule_count": int(scored_agg.get("rule_count", 0) or 0),
        }

    failures.extend(check_guard(guard, args))

    return {
        "passed": not failures,
        "failures": failures,
        "summary": {
            "model": prompt_suite.get("model"),
            "layers": prompt_suite.get("layers", []),
            "package_summary": prompt_suite.get("package_summary"),
            "prompts": prompts,
            "exact_matches": exact_matches,
            "exact_match_rate": exact_rate,
            "mean_char_edit_similarity": mean_similarity,
            "median_char_edit_similarity": median_similarity,
            "mean_common_prefix_ratio": mean_prefix,
            "mean_speedup_fused_vs_baseline": speed_ratio,
            "median_ttft_ratio_vs_baseline": ttft_ratio,
            "replacement_compression_vs_fp32": compression,
            "replacement_median_cuda_ms": median_cuda_ms,
            "replacement_wrapper_calls": wrapper_calls,
            "replacement_fused_compute_calls": fused_compute_calls,
            "replacement_cache_hits": cache_hits,
            "replacement_cache_misses": cache_misses,
            "peak_gpu_memory_mib": finite_float(prompt_suite.get("peak_gpu_memory_mib")),
            "guard_max_memory_used_ratio": None if guard is None else guard.get("max_memory_used_ratio"),
            "guard_max_memory_used_mib": None if guard is None else guard.get("max_memory_used_mib"),
            "guard_memory_total_mib": None if guard is None else guard.get("memory_total_mib"),
            "scored": scored_summary,
        },
        "thresholds": {
            "min_prompts": args.min_prompts,
            "min_exact_matches": args.min_exact_matches,
            "min_exact_match_rate": args.min_exact_match_rate,
            "min_mean_char_edit_similarity": args.min_mean_char_edit_similarity,
            "min_median_char_edit_similarity": args.min_median_char_edit_similarity,
            "min_mean_common_prefix_ratio": args.min_mean_common_prefix_ratio,
            "min_mean_speed_ratio": args.min_mean_speed_ratio,
            "max_median_ttft_ratio": args.max_median_ttft_ratio,
            "min_compression_vs_fp32": args.min_compression_vs_fp32,
            "max_median_replacement_ms": args.max_median_replacement_ms,
            "min_wrapper_calls": args.min_wrapper_calls,
            "min_fused_compute_calls": args.min_fused_compute_calls,
            "min_cache_hits": args.min_cache_hits,
            "min_cache_misses": args.min_cache_misses,
            "min_scored_prompts": args.min_scored_prompts,
            "max_rule_regressions": args.max_rule_regressions,
            "min_fused_rule_pass_rate": args.min_fused_rule_pass_rate,
            "max_fused_rule_pass_drop": args.max_fused_rule_pass_drop,
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
    scored = summary.get("scored") or {}
    lines = [
        "# Fused QKV Prompt-Suite Gate",
        "",
        f"Status: **{'PASS' if result['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- model: `{summary['model']}`",
        f"- layers: `{summary['layers']}`",
        f"- prompts: {summary['prompts']}",
        f"- exact matches: {summary['exact_matches']} / {summary['prompts']}",
        f"- exact match rate: {fmt(summary['exact_match_rate'])}",
        f"- mean / median edit similarity: {fmt(summary['mean_char_edit_similarity'])} / {fmt(summary['median_char_edit_similarity'])}",
        f"- mean common prefix ratio: {fmt(summary['mean_common_prefix_ratio'])}",
        f"- mean speed ratio fused/baseline: {fmt(summary['mean_speedup_fused_vs_baseline'])}x",
        f"- median TTFT ratio fused/baseline: {fmt(summary['median_ttft_ratio_vs_baseline'])}x",
        f"- compression vs FP32: {fmt(summary['replacement_compression_vs_fp32'])}x",
        f"- replacement median CUDA ms: {fmt(summary['replacement_median_cuda_ms'], 6)}",
        f"- wrapper/fused/cache-hit/cache-miss calls: {summary['replacement_wrapper_calls']} / {summary['replacement_fused_compute_calls']} / {summary['replacement_cache_hits']} / {summary['replacement_cache_misses']}",
        f"- guard peak memory: {summary['guard_max_memory_used_mib']} / {summary['guard_memory_total_mib']} MiB ({fmt(summary['guard_max_memory_used_ratio'])})",
        "",
        "## Rule Score",
        "",
    ]
    if scored:
        lines.extend(
            [
                f"- scored prompts: {scored['prompts']}",
                f"- baseline passes: {scored['baseline_passes']}",
                f"- fused passes: {scored['fused_passes']}",
                f"- fused pass rate: {fmt(scored['fused_pass_rate'])}",
                f"- regressions: {scored['regressions']}",
                f"- improvements: {scored['improvements']}",
                f"- rule count: {scored['rule_count']}",
            ]
        )
    else:
        lines.append("- no scored prompt-suite file provided")
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
            "- Valid claim: this candidate preserves the measured prompt-suite outputs under deterministic text and shallow rule checks.",
            "- Invalid claim: this proves broad semantic quality, task accuracy, or SOTA quantization quality.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate fused QKV prompt-suite quality evidence.")
    parser.add_argument("--prompt-suite-json", type=Path, required=True)
    parser.add_argument("--scored-json", type=Path, default=None)
    parser.add_argument("--guard-json", type=Path, default=None)
    parser.add_argument("--out-json", type=Path, default=Path("outputs/real_system_packer_2026-06-05/fused_qkv_prompt_suite_gate.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_GATE.md"))
    parser.add_argument("--min-prompts", type=int, default=1)
    parser.add_argument("--min-exact-matches", type=int, default=0)
    parser.add_argument("--min-exact-match-rate", type=float, default=0.0)
    parser.add_argument("--min-mean-char-edit-similarity", type=float, default=0.0)
    parser.add_argument("--min-median-char-edit-similarity", type=float, default=0.0)
    parser.add_argument("--min-mean-common-prefix-ratio", type=float, default=0.0)
    parser.add_argument("--min-mean-speed-ratio", type=float, default=0.0)
    parser.add_argument("--max-median-ttft-ratio", type=float, default=999.0)
    parser.add_argument("--min-compression-vs-fp32", type=float, default=1.0)
    parser.add_argument("--max-median-replacement-ms", type=float, default=10.0)
    parser.add_argument("--min-wrapper-calls", type=int, default=1)
    parser.add_argument("--min-fused-compute-calls", type=int, default=1)
    parser.add_argument("--min-cache-hits", type=int, default=0)
    parser.add_argument("--min-cache-misses", type=int, default=1)
    parser.add_argument("--min-scored-prompts", type=int, default=0)
    parser.add_argument("--max-rule-regressions", type=int, default=0)
    parser.add_argument("--min-fused-rule-pass-rate", type=float, default=0.0)
    parser.add_argument("--max-fused-rule-pass-drop", type=int, default=0)
    parser.add_argument("--max-memory-ratio", type=float, default=0.90)
    args = parser.parse_args()

    prompt_suite = load_json(args.prompt_suite_json)
    scored = load_json(args.scored_json) if args.scored_json else None
    guard = load_json(args.guard_json) if args.guard_json else None
    result = build_result(prompt_suite, scored, guard, args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"passed": result["passed"], "failures": result["failures"], "out_json": str(args.out_json)}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
