#!/usr/bin/env python3
from __future__ import annotations

"""Build a paper-facing ledger from executable evidence gates."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CATEGORIES = {
    "rank_inversion": "theory",
    "theory": "theory",
    "task_model_ladder": "capability retention",
    "official_ptq_task_subset": "task execution subset",
    "official_ptq_task": "task execution smoke",
    "official_ptq_matched": "matched PTQ baseline",
    "official_awq_public_calib": "official PTQ readiness",
    "official_ptq_runtime": "runtime profile",
    "runtime_profile": "runtime profile",
    "quality": "quality",
    "prompt": "quality",
    "allocation": "allocation comparator",
    "interaction": "allocation comparator",
    "swap": "allocation comparator",
    "consensus": "allocation comparator",
    "robust_lcb": "allocation comparator",
    "q_palette": "allocation comparator",
    "impq": "allocation comparator",
    "windquant": "allocation comparator",
    "awq": "ptq comparator",
    "gptq": "ptq comparator",
    "ptq": "ptq comparator",
    "rotation": "rotation comparator",
    "quarot": "rotation comparator",
    "spinquant": "rotation comparator",
    "triton": "kernel",
    "selector": "runtime wiring",
    "selected": "selected-row",
    "cpp": "c++ runtime",
    "sidecar": "decode integration",
    "qkv": "qkv replacement",
    "chat": "task retention",
    "esmp": "artifact integrity",
    "package": "artifact integrity",
    "artifact": "artifact integrity",
    "task_benchmark": "capability retention",
    "benchmark": "capability retention",
    "capability": "capability retention",
    "paper": "paper alignment",
    "alignment": "paper alignment",
    "hygiene": "repo hygiene",
    "public": "repo hygiene",
    "calibration": "calibration robustness",
    "csi": "calibration robustness",
    "curve": "calibration robustness",
    "instability": "calibration robustness",
    "perturbation": "calibration robustness",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_gate_spec(spec: str) -> tuple[str, Path]:
    if "=" not in spec:
        raise ValueError(f"gate spec must be LABEL=PATH: {spec}")
    label, raw_path = spec.split("=", 1)
    label = label.strip()
    if not label:
        raise ValueError(f"empty gate label in spec: {spec}")
    return label, Path(raw_path)


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


def fmt(value: Any, digits: int = 4) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def infer_category(label: str) -> str:
    lower = label.lower()
    for token, category in CATEGORIES.items():
        if token in lower:
            return category
    return "evidence"


def metric_parts(summary: dict[str, Any]) -> list[str]:
    parts: list[str] = []

    def append_ci(label: str, key: str) -> None:
        ci = summary.get(key)
        if not isinstance(ci, dict):
            return
        low = finite_float(ci.get("low"))
        high = finite_float(ci.get("high"))
        if low is not None and high is not None:
            parts.append(f"{label} CI [{low:.4f}, {high:.4f}]")

    if "valid_configs" in summary:
        parts.append(f"configs {summary.get('valid_configs')}/{summary.get('total_configs')}")
    if "fp16_wins" in summary:
        parts.append(f"FP16 wins {summary.get('fp16_wins')}")
    if (value := finite_float(summary.get("best_fp16_speedup"))) is not None:
        parts.append(f"best FP16 {value:.4f}x")
    if "selector_call_count" in summary:
        parts.append(f"selector calls {summary.get('selector_call_count')}")
    if "ok_rows" in summary:
        parts.append(f"ok rows {summary.get('ok_rows')}")
    if "wins_vs_full" in summary:
        parts.append(f"wins/full {summary.get('wins_vs_full')}")
    if (value := finite_float(summary.get("median_selected_speedup_vs_full"))) is not None:
        parts.append(f"median selected {value:.4f}x")
    if "sidecar_call_count" in summary:
        parts.append(f"sidecar calls {summary.get('sidecar_call_count')}")
    if "replacement_count" in summary:
        parts.append(f"replacements {summary.get('replacement_count')}")
    if (value := finite_float(summary.get("tokens_per_second_ratio_vs_baseline"))) is not None:
        parts.append(f"tok/s ratio {value:.4f}x")
    if (value := finite_float(summary.get("ttft_ratio_vs_baseline"))) is not None:
        parts.append(f"TTFT ratio {value:.4f}x")
    if "exact_matches" in summary and "prompts" in summary:
        parts.append(f"exact {summary.get('exact_matches')}/{summary.get('prompts')}")
    if "regressions" in summary and "tasks" in summary:
        parts.append(f"regressions {summary.get('regressions')}")
    if "fused_passes" in summary and "tasks" in summary:
        parts.append(f"fused {summary.get('fused_passes')}/{summary.get('tasks')}")
    if "checked_module_count" in summary:
        parts.append(f"checked modules {summary.get('checked_module_count')}/{summary.get('requested_module_count')}")
    if "missing_file_count" in summary:
        parts.append(f"missing files {summary.get('missing_file_count')}")
    if "failed_module_count" in summary:
        parts.append(f"failed modules {summary.get('failed_module_count')}")
    if "tracked_file_count" in summary:
        parts.append(f"tracked files {summary.get('tracked_file_count')}")
    if "forbidden_file_count" in summary:
        parts.append(f"forbidden files {summary.get('forbidden_file_count')}")
    if "placeholder_count" in summary:
        parts.append(f"placeholders {summary.get('placeholder_count')}")
    if "required_reference_count" in summary:
        parts.append(f"required refs {summary.get('required_reference_count')}")
    if "missing_required_reference_count" in summary:
        parts.append(f"missing refs {summary.get('missing_required_reference_count')}")
    if "referenced_repo_path_count" in summary:
        parts.append(f"paper paths {summary.get('referenced_repo_path_count')}")
    if "missing_referenced_path_count" in summary:
        parts.append(f"missing paths {summary.get('missing_referenced_path_count')}")
    if "unsafe_claim_count" in summary:
        parts.append(f"unsafe claims {summary.get('unsafe_claim_count')}")
    if "stale_token_count" in summary:
        parts.append(f"stale tokens {summary.get('stale_token_count')}")
    if "ledger_gate_count" in summary:
        parts.append(f"ledger gates {summary.get('ledger_gate_count')}")
    if "case_count" in summary:
        parts.append(f"cases {summary.get('case_count')}")
    if "point_count" in summary:
        parts.append(f"points {summary.get('point_count')}")
    if "min_n" in summary and "max_n" in summary:
        parts.append(f"n {summary.get('min_n')}->{summary.get('max_n')}")
    if (value := finite_float(summary.get("mean_score_spearman_gain"))) is not None:
        parts.append(f"rho gain {value:.4f}")
    if (value := finite_float(summary.get("mean_top20_jaccard_gain"))) is not None:
        parts.append(f"top20 gain {value:.4f}")
    if (value := finite_float(summary.get("mean_positive_jaccard_gain"))) is not None:
        parts.append(f"positive gain {value:.4f}")
    if (value := finite_float(summary.get("min_full_range_gain_low"))) is not None:
        parts.append(f"min gain CI low {value:.4f}")
    if (value := finite_float(summary.get("min_full_range_dominance_probability"))) is not None:
        parts.append(f"min dominance {value:.4f}")
    if "all_full_range_gain_ci_positive" in summary:
        parts.append(f"gain CI positive {summary.get('all_full_range_gain_ci_positive')}")
    if "all_full_range_dominance_high" in summary:
        parts.append(f"dominance high {summary.get('all_full_range_dominance_high')}")
    if (value := finite_float(summary.get("min_observed_gain"))) is not None:
        parts.append(f"min observed gain {value:.4f}")
    if (value := finite_float(summary.get("max_holm_adjusted_p_value"))) is not None:
        parts.append(f"max Holm p {value:.6g}")
    if "all_observed_gains_positive" in summary:
        parts.append(f"all gains positive {summary.get('all_observed_gains_positive')}")
    if "all_holm_significant" in summary:
        parts.append(f"Holm significant {summary.get('all_holm_significant')}")
    if (value := finite_float(summary.get("mean_empirical_inversion_rate_initial"))) is not None:
        parts.append(f"mean inversion init {value:.4f}")
    if (value := finite_float(summary.get("mean_empirical_inversion_rate_final"))) is not None:
        parts.append(f"mean inversion final {value:.4f}")
    if (value := finite_float(summary.get("margin_empirical_inversion_rate_initial"))) is not None:
        parts.append(f"margin inversion init {value:.4f}")
    if (value := finite_float(summary.get("margin_empirical_inversion_rate_final"))) is not None:
        parts.append(f"margin inversion final {value:.4f}")
    if (value := finite_float(summary.get("mean_chebyshev_bound_final"))) is not None:
        parts.append(f"mean bound final {value:.4f}")
    if (value := finite_float(summary.get("margin_chebyshev_bound_final"))) is not None:
        parts.append(f"margin bound final {value:.4f}")
    if "mean_score_spearman_monotonic" in summary:
        parts.append(f"rho monotonic {summary.get('mean_score_spearman_monotonic')}")
    if "common_n_count" in summary:
        parts.append(f"common n {summary.get('common_n_count')}")
    if "right_lower_all_same_n_metrics" in summary:
        parts.append(f"right lower all metrics {summary.get('right_lower_all_same_n_metrics')}")
    if isinstance(summary.get("right_gain_larger_by_metric"), dict):
        gain_flags = summary["right_gain_larger_by_metric"]
        true_count = sum(1 for value in gain_flags.values() if value)
        parts.append(f"right larger gains {true_count}/{len(gain_flags)}")
    if "mean_empirical_inversion_rate_decreasing" in summary:
        parts.append(f"mean inversion decreasing {summary.get('mean_empirical_inversion_rate_decreasing')}")
    if "margin_empirical_inversion_rate_decreasing" in summary:
        parts.append(f"margin inversion decreasing {summary.get('margin_empirical_inversion_rate_decreasing')}")
    if (value := finite_float(summary.get("min_budget_utilization"))) is not None:
        parts.append(f"min budget util {value:.4f}")
    if "finite_lambda_count" in summary:
        parts.append(f"finite lambdas {summary.get('finite_lambda_count')}")
    if "nontrivial_bit_hist_count" in summary:
        parts.append(f"nontrivial hists {summary.get('nontrivial_bit_hist_count')}")
    if "model_count" in summary:
        parts.append(f"models {summary.get('model_count')}")
    if "best_total_passes" in summary:
        parts.append(f"best passes {summary.get('best_total_passes')}")
    if (value := finite_float(summary.get("best_accuracy"))) is not None:
        parts.append(f"best accuracy {value:.4f}")
    if "slice_count" in summary:
        parts.append(f"slices {summary.get('slice_count')}")
    if "eval_slice_count" in summary:
        parts.append(f"eval slices {summary.get('eval_slice_count')}")
    if "total_eval_tokens" in summary:
        parts.append(f"eval tokens {summary.get('total_eval_tokens')}")
    eval_ratios = [
        value
        for row in summary.get("evals", []) or []
        if isinstance(row, dict)
        for value in [finite_float(row.get("ppl_ratio_awq_vs_fp16"))]
        if value is not None
    ]
    if eval_ratios:
        parts.append(f"max eval PPL ratio {max(eval_ratios):.4f}")
    if "expected_awq_blocks" in summary:
        parts.append(f"AWQ blocks {summary.get('expected_awq_blocks')}")
    if "unstable_case_count" in summary:
        parts.append(f"unstable {summary.get('unstable_case_count')}")
    if "unique_prompt_selection_count" in summary:
        parts.append(f"prompt selections {summary.get('unique_prompt_selection_count')}")
    if "finite_pair_count" in summary:
        parts.append(f"finite pairs {summary.get('finite_pair_count')}")
    if (value := finite_float(summary.get("sample_size_mean_spearman"))) is not None:
        parts.append(f"sample-size rho {value:.4f}")
    if (value := finite_float(summary.get("model_scale_mean_spearman"))) is not None:
        parts.append(f"model-scale rho {value:.4f}")
    if (value := finite_float(summary.get("perturbation_separation_margin"))) is not None:
        parts.append(f"separation {value:.4f}")
    if (value := finite_float(summary.get("min_score_spearman"))) is not None:
        parts.append(f"min rho {value:.4f}")
    append_ci("mean rho", "mean_score_spearman_ci")
    if (value := finite_float(summary.get("min_top20_jaccard"))) is not None:
        parts.append(f"min top20 {value:.4f}")
    append_ci("mean top20", "mean_top20_jaccard_ci")
    if "total_tasks" in summary:
        parts.append(f"tasks {summary.get('total_tasks')}")
    if "total_cases" in summary:
        parts.append(f"cases {summary.get('total_cases')}")
    if "total_passes" in summary:
        parts.append(f"passes {summary.get('total_passes')}")
    if (value := finite_float(summary.get("mean_accuracy"))) is not None:
        parts.append(f"accuracy {value:.4f}")
    if (value := finite_float(summary.get("max_ppl_ratio_vs_fp16"))) is not None:
        parts.append(f"max PPL ratio {value:.4f}")
    if (value := finite_float(summary.get("max_accuracy_drop_vs_fp16"))) is not None:
        parts.append(f"max drop {value:.4f}")
    if (value := finite_float(summary.get("max_vram_ratio_vs_fp16"))) is not None:
        parts.append(f"max VRAM ratio {value:.4f}")
    if (value := finite_float(summary.get("max_tokens_per_second_ratio_vs_fp16"))) is not None:
        parts.append(f"max tok/s ratio {value:.4f}")
    if (value := finite_float(summary.get("mean_tokens_per_second"))) is not None:
        parts.append(f"mean tok/s {value:.4f}")
    if (value := finite_float(summary.get("mean_ttft_seconds"))) is not None:
        parts.append(f"mean TTFT {value:.6f}s")
    if (value := finite_float(summary.get("max_guard_vram_mib"))) is not None:
        parts.append(f"VRAM MiB {value:.0f}")
    if "target_wins_vs_uniform" in summary:
        parts.append(f"wins/uniform {summary.get('target_wins_vs_uniform')}")
    if "target_wins_vs_best_random" in summary:
        parts.append(f"wins/best-random {summary.get('target_wins_vs_best_random')}")
    if "target_wins_vs_random_mean" in summary:
        parts.append(f"wins/random-mean {summary.get('target_wins_vs_random_mean')}")
    if "target_wins_vs_mean" in summary:
        parts.append(f"wins/mean {summary.get('target_wins_vs_mean')}")
    if (value := finite_float(summary.get("mean_target_margin_vs_uniform"))) is not None:
        parts.append(f"margin vs uniform {value:.4f}")
    if (value := finite_float(summary.get("mean_target_margin_vs_mean"))) is not None:
        parts.append(f"margin vs mean {value:.4f}")
    if (value := finite_float(summary.get("mean_margin_vs_uniform"))) is not None:
        parts.append(f"mean margin/uniform {value:.4f}")
    append_ci("mean margin/uniform", "mean_margin_vs_uniform_ci")
    if (value := finite_float(summary.get("worst_margin_vs_uniform"))) is not None:
        parts.append(f"worst margin/uniform {value:.4f}")
    if (value := finite_float(summary.get("mean_margin_vs_best_random"))) is not None:
        parts.append(f"mean margin/best-random {value:.4f}")
    append_ci("mean margin/best-random", "mean_margin_vs_best_random_ci")
    if (value := finite_float(summary.get("worst_margin_vs_best_random"))) is not None:
        parts.append(f"worst margin/best-random {value:.4f}")
    if (value := finite_float(summary.get("mean_margin_vs_random_mean"))) is not None:
        parts.append(f"mean margin/random-mean {value:.4f}")
    append_ci("mean margin/random-mean", "mean_margin_vs_random_mean_ci")
    if (value := finite_float(summary.get("worst_margin_vs_random_mean"))) is not None:
        parts.append(f"worst margin/random-mean {value:.4f}")
    if (value := finite_float(summary.get("mean_fp16_regret"))) is not None:
        parts.append(f"mean FP16 regret {value:.4f}")
    if (value := finite_float(summary.get("max_fp16_regret"))) is not None:
        parts.append(f"max FP16 regret {value:.4f}")
    if (value := finite_float(summary.get("sign_test_p_vs_uniform"))) is not None:
        parts.append(f"sign p/uniform {value:.5g}")
    if (value := finite_float(summary.get("sign_test_p_vs_best_random"))) is not None:
        parts.append(f"sign p/best-random {value:.5g}")
    if (value := finite_float(summary.get("sign_test_p_vs_random_mean"))) is not None:
        parts.append(f"sign p/random-mean {value:.5g}")
    if "consensus_wins_vs_left_single" in summary:
        parts.append(f"wins/left-single {summary.get('consensus_wins_vs_left_single')}")
    if "consensus_wins_vs_right_single" in summary:
        parts.append(f"wins/right-single {summary.get('consensus_wins_vs_right_single')}")
    if "consensus_wins_vs_best_single" in summary:
        parts.append(f"wins/best-single {summary.get('consensus_wins_vs_best_single')}")
    if "consensus_wins_vs_worst_single" in summary:
        parts.append(f"wins/worst-single {summary.get('consensus_wins_vs_worst_single')}")
    if (value := finite_float(summary.get("min_margin_vs_worst_single"))) is not None:
        parts.append(f"min margin/worst-single {value:.4f}")
    if (value := finite_float(summary.get("mean_regret_vs_best_single"))) is not None:
        parts.append(f"mean regret/best-single {value:.4f}")
    if (value := finite_float(summary.get("max_regret_vs_best_single"))) is not None:
        parts.append(f"max regret/best-single {value:.4f}")
    if "total_trials" in summary:
        parts.append(f"trials {summary.get('total_trials')}")
    if "improved_case_count" in summary:
        parts.append(f"improved cases {summary.get('improved_case_count')}")
    if "improved_trial_count" in summary:
        parts.append(f"improved trials {summary.get('improved_trial_count')}")
    if "interaction_counterexample_count" in summary:
        parts.append(f"interaction counterexamples {summary.get('interaction_counterexample_count')}")
    if (value := finite_float(summary.get("max_best_improvement_ppl"))) is not None:
        parts.append(f"max best improvement {value:.4f}")
    if "transfer_positive_rows" in summary:
        parts.append(f"transfer positives {summary.get('transfer_positive_rows')}")
    if (value := finite_float(summary.get("transfer_max_regret_ppl"))) is not None:
        parts.append(f"transfer max regret {value:.4f}")
    if "total_records" in summary:
        parts.append(f"records {summary.get('total_records')}")
    if "total_high_bit_modules" in summary:
        parts.append(f"high-bit modules {summary.get('total_high_bit_modules')}")
    if "consistent_selected_modules" in summary:
        parts.append(f"consistent selected {summary.get('consistent_selected_modules')}")
    if "selected_modules" in summary:
        parts.append(f"selected modules {summary.get('selected_modules')}")
    if "total_rotated" in summary:
        parts.append(f"rotated {summary.get('total_rotated')}")
    if "available_package_count" in summary:
        parts.append(f"packages {summary.get('available_package_count')}")
    if "method_count" in summary:
        parts.append(f"methods {summary.get('method_count')}")
    if (value := finite_float(summary.get("max_rotated_cost_fraction"))) is not None:
        parts.append(f"rotation cost {value:.4f}")
    if (value := finite_float(summary.get("mean_projected_reduction_ratio"))) is not None:
        parts.append(f"projected reduction {value:.4f}")
    if (value := finite_float(summary.get("max_avg_bits"))) is not None:
        parts.append(f"max avg bits {value:.4f}")
    if (value := finite_float(summary.get("max_target_avg_bits"))) is not None:
        parts.append(f"target bits {value:.4f}")
    if (value := finite_float(summary.get("mean_score_spearman"))) is not None:
        parts.append(f"mean Spearman {value:.4f}")
    if (value := finite_float(summary.get("mean_positive_jaccard"))) is not None:
        parts.append(f"mean Jaccard {value:.4f}")
    append_ci("mean Jaccard", "mean_positive_jaccard_ci")
    if (value := finite_float(summary.get("mean_top20_jaccard"))) is not None:
        parts.append(f"top20 Jaccard {value:.4f}")
    if (value := finite_float(summary.get("mean_speedup_fused_vs_baseline"))) is not None:
        parts.append(f"mean speed {value:.4f}x")
    if (value := finite_float(summary.get("replacement_compression_vs_fp32"))) is not None:
        parts.append(f"compression {value:.4f}x")
    if (value := finite_float(summary.get("median_compression_vs_fp32"))) is not None:
        parts.append(f"compression {value:.4f}x")
    if (value := finite_float(summary.get("compression_ratio_vs_fp32_checked"))) is not None:
        parts.append(f"checked compression {value:.4f}x")
    if (value := finite_float(summary.get("guard_max_memory_used_ratio"))) is not None:
        parts.append(f"VRAM {value:.4f}")
    if (value := finite_float(summary.get("max_guard_vram_ratio"))) is not None:
        parts.append(f"VRAM {value:.4f}")
    return parts


def summarize_gate(label: str, path: Path, payload: dict[str, Any]) -> dict[str, Any]:
    summary = payload.get("summary", {}) or {}
    failures = list(payload.get("failures", []) or [])
    passed = bool(payload.get("passed"))
    return {
        "label": label,
        "category": infer_category(label),
        "path": str(path),
        "passed": passed,
        "failures": failures,
        "metrics": "; ".join(metric_parts(summary)) or "n/a",
        "summary": summary,
    }


def build_ledger(gates: list[tuple[str, Path]]) -> dict[str, Any]:
    entries = [summarize_gate(label, path, load_json(path)) for label, path in gates]
    failed = [entry for entry in entries if not entry["passed"]]
    categories = sorted({entry["category"] for entry in entries})
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failed,
        "gate_count": len(entries),
        "passed_count": len(entries) - len(failed),
        "failed_count": len(failed),
        "categories": categories,
        "entries": entries,
        "failures": [
            {"label": entry["label"], "path": entry["path"], "failures": entry["failures"]}
            for entry in failed
        ],
    }


def write_markdown(path: Path, ledger: dict[str, Any]) -> None:
    lines = [
        "# Evidence Ledger",
        "",
        f"Date: `{ledger['date']}`",
        f"Status: **{'PASS' if ledger['passed'] else 'FAIL'}**",
        f"Gates: `{ledger['passed_count']} / {ledger['gate_count']}` passed",
        f"Categories: `{', '.join(ledger['categories'])}`",
        "",
        "## Gate Summary",
        "",
        "| gate | category | status | key metrics | source |",
        "|---|---|---|---|---|",
    ]
    for entry in ledger["entries"]:
        source = str(entry["path"]).replace("\\", "/")
        status = "PASS" if entry["passed"] else "FAIL"
        metrics = str(entry["metrics"]).replace("|", "\\|")
        lines.append(f"| `{entry['label']}` | {entry['category']} | **{status}** | {metrics} | `{source}` |")
    lines.extend(["", "## Failures", ""])
    if ledger["failures"]:
        for failure in ledger["failures"]:
            lines.append(f"- `{failure['label']}`: {failure['failures']}")
    else:
        lines.append("- none")
    lines.extend(
        [
            "",
            "## Claim Boundary",
            "",
            "- Valid claim: each listed row is backed by an executable gate JSON that passed under its configured thresholds.",
            "- Invalid claim: passing this ledger proves SOTA quantization, mobile deployment, or full paper readiness.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build an evidence ledger from gate JSON files.")
    parser.add_argument("--gate", action="append", required=True, help="LABEL=gate_json")
    parser.add_argument("--out-json", type=Path, default=Path("outputs/real_system_packer_2026-06-05/evidence_ledger.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER.md"))
    args = parser.parse_args()

    gates = [parse_gate_spec(spec) for spec in args.gate]
    ledger = build_ledger(gates)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, ledger)
    print(json.dumps({"passed": ledger["passed"], "gate_count": ledger["gate_count"], "out_json": str(args.out_json)}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if ledger["passed"] else 1)


if __name__ == "__main__":
    main()
