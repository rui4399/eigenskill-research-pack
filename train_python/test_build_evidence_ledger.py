from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import build_evidence_ledger as ledger


def write_gate(path: Path, passed: bool = True, summary: dict | None = None, failures: list[str] | None = None) -> Path:
    path.write_text(
        json.dumps(
            {
                "passed": passed,
                "summary": summary or {"valid_configs": 4, "total_configs": 4, "best_fp16_speedup": 1.5},
                "failures": failures or [],
            }
        ),
        encoding="utf-8",
    )
    return path


class BuildEvidenceLedgerTests(unittest.TestCase):
    def test_builds_passing_ledger_and_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            gate_path = write_gate(root / "triton_gate.json")
            result = ledger.build_ledger([("triton_shape_family", gate_path)])
            self.assertTrue(result["passed"])
            self.assertEqual(result["gate_count"], 1)
            self.assertIn("configs 4/4", result["entries"][0]["metrics"])
            self.assertEqual(result["entries"][0]["category"], "kernel")

    def test_failed_gate_fails_ledger(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            good = write_gate(root / "good.json")
            bad = write_gate(root / "bad.json", passed=False, failures=["boom"])
            result = ledger.build_ledger([("cpp_runtime", good), ("chat_task", bad)])
            self.assertFalse(result["passed"])
            self.assertEqual(result["failed_count"], 1)
            self.assertEqual(result["failures"][0]["failures"], ["boom"])

    def test_quality_boundary_metrics_are_reported(self) -> None:
        metrics = ledger.metric_parts(
            {
                "case_count": 2,
                "target_wins_vs_uniform": 2,
                "target_wins_vs_mean": 0,
                "mean_target_margin_vs_uniform": 5.61,
                "mean_target_margin_vs_mean": -2.88,
            }
        )
        joined = "; ".join(metrics)
        self.assertIn("wins/uniform 2", joined)
        self.assertIn("wins/mean 0", joined)
        self.assertIn("margin vs uniform 5.6100", joined)
        self.assertIn("margin vs mean -2.8800", joined)

    def test_calibration_stress_metrics_are_reported(self) -> None:
        metrics = ledger.metric_parts(
            {
                "case_count": 11,
                "target_wins_vs_uniform": 11,
                "target_wins_vs_best_random": 11,
                "target_wins_vs_random_mean": 11,
                "mean_margin_vs_uniform": 4.29,
                "mean_margin_vs_uniform_ci": {"low": 3.0, "high": 5.0},
                "worst_margin_vs_best_random": 0.11,
                "sign_test_p_vs_best_random": 0.00049,
                "mean_fp16_regret": 4.16,
            }
        )
        joined = "; ".join(metrics)
        self.assertIn("wins/best-random 11", joined)
        self.assertIn("wins/random-mean 11", joined)
        self.assertIn("mean margin/uniform 4.2900", joined)
        self.assertIn("mean margin/uniform CI [3.0000, 5.0000]", joined)
        self.assertIn("worst margin/best-random 0.1100", joined)
        self.assertIn("sign p/best-random 0.00049", joined)
        self.assertIn("mean FP16 regret 4.1600", joined)

    def test_sensitivity_perturbation_metrics_are_reported(self) -> None:
        metrics = ledger.metric_parts(
            {
                "case_count": 3,
                "sample_size_mean_spearman": 0.63,
                "model_scale_mean_spearman": 0.12,
                "perturbation_separation_margin": 0.51,
            }
        )
        joined = "; ".join(metrics)
        self.assertIn("sample-size rho 0.6300", joined)
        self.assertIn("model-scale rho 0.1200", joined)
        self.assertIn("separation 0.5100", joined)
        self.assertEqual(ledger.infer_category("sensitivity_perturbation_matrix"), "calibration robustness")

    def test_rank_inversion_theory_metrics_are_reported(self) -> None:
        metrics = ledger.metric_parts(
            {
                "point_count": 3,
                "mean_empirical_inversion_rate_initial": 0.24,
                "mean_empirical_inversion_rate_final": 0.14,
                "margin_empirical_inversion_rate_initial": 0.09,
                "margin_empirical_inversion_rate_final": 0.04,
                "mean_chebyshev_bound_final": 0.61,
                "margin_chebyshev_bound_final": 0.27,
                "mean_empirical_inversion_rate_decreasing": True,
                "margin_empirical_inversion_rate_decreasing": True,
            }
        )
        joined = "; ".join(metrics)
        self.assertIn("mean inversion init 0.2400", joined)
        self.assertIn("mean inversion final 0.1400", joined)
        self.assertIn("margin inversion final 0.0400", joined)
        self.assertIn("mean bound final 0.6100", joined)
        self.assertIn("mean inversion decreasing True", joined)
        self.assertEqual(ledger.infer_category("rank_inversion_theory"), "theory")

    def test_csi_trend_significance_metrics_are_reported(self) -> None:
        metrics = ledger.metric_parts(
            {
                "point_count": 3,
                "min_n": 2,
                "max_n": 8,
                "min_full_range_gain_low": 0.1351,
                "min_full_range_dominance_probability": 0.9422,
                "all_full_range_gain_ci_positive": True,
                "all_full_range_dominance_high": True,
            }
        )
        joined = "; ".join(metrics)
        self.assertIn("points 3", joined)
        self.assertIn("n 2->8", joined)
        self.assertIn("min gain CI low 0.1351", joined)
        self.assertIn("min dominance 0.9422", joined)
        self.assertIn("gain CI positive True", joined)
        self.assertEqual(ledger.infer_category("csi_trend_significance"), "calibration robustness")

    def test_allocation_family_metrics_are_reported(self) -> None:
        metrics = ledger.metric_parts(
            {
                "case_count": 6,
                "total_records": 1126,
                "max_avg_bits": 4.4999181196117,
                "min_budget_utilization": 0.9999266915915255,
                "finite_lambda_count": 6,
                "nontrivial_bit_hist_count": 6,
            }
        )
        joined = "; ".join(metrics)
        self.assertIn("cases 6", joined)
        self.assertIn("records 1126", joined)
        self.assertIn("max avg bits 4.4999", joined)
        self.assertIn("min budget util 0.9999", joined)
        self.assertIn("finite lambdas 6", joined)
        self.assertIn("nontrivial hists 6", joined)

    def test_transfer_boundary_metrics_are_reported(self) -> None:
        metrics = ledger.metric_parts(
            {
                "case_count": 2,
                "slice_count": 4,
                "consensus_wins_vs_worst_single": 4,
                "consensus_wins_vs_best_single": 2,
                "min_margin_vs_worst_single": 0.87,
                "max_regret_vs_best_single": 0.30,
            }
        )
        joined = "; ".join(metrics)
        self.assertIn("slices 4", joined)
        self.assertIn("wins/worst-single 4", joined)
        self.assertIn("wins/best-single 2", joined)
        self.assertIn("min margin/worst-single 0.8700", joined)
        self.assertIn("max regret/best-single 0.3000", joined)

    def test_interaction_swap_metrics_are_reported(self) -> None:
        metrics = ledger.metric_parts(
            {
                "case_count": 3,
                "total_trials": 16,
                "improved_case_count": 1,
                "improved_trial_count": 5,
                "interaction_counterexample_count": 5,
                "max_best_improvement_ppl": 0.0501,
                "transfer_positive_rows": 1,
                "transfer_max_regret_ppl": 0.0087,
            }
        )
        joined = "; ".join(metrics)
        self.assertIn("trials 16", joined)
        self.assertIn("improved cases 1", joined)
        self.assertIn("interaction counterexamples 5", joined)
        self.assertIn("max best improvement 0.0501", joined)
        self.assertIn("transfer max regret 0.0087", joined)

    def test_paper_alignment_metrics_are_reported(self) -> None:
        metrics = ledger.metric_parts(
            {
                "required_reference_count": 8,
                "missing_required_reference_count": 0,
                "referenced_repo_path_count": 33,
                "missing_referenced_path_count": 0,
                "unsafe_claim_count": 0,
                "stale_token_count": 0,
                "ledger_gate_count": 20,
            }
        )
        joined = "; ".join(metrics)
        self.assertIn("required refs 8", joined)
        self.assertIn("missing refs 0", joined)
        self.assertIn("paper paths 33", joined)
        self.assertIn("unsafe claims 0", joined)
        self.assertEqual(ledger.infer_category("paper_evidence_alignment"), "paper alignment")

    def test_official_ptq_task_gate_is_not_labeled_as_ptq_comparator(self) -> None:
        self.assertEqual(ledger.infer_category("official_ptq_task_retention"), "task execution smoke")
        self.assertEqual(ledger.infer_category("official_ptq_task_subset50"), "task execution subset")
        self.assertEqual(ledger.infer_category("official_ptq_runtime_profile"), "runtime profile")
        self.assertEqual(ledger.infer_category("official_ptq_subset50_runtime_profile"), "runtime profile")
        self.assertEqual(ledger.infer_category("official_ptq_matched_baseline_pack"), "matched PTQ baseline")

    def test_official_ptq_matched_baseline_pack_metrics_are_reported(self) -> None:
        metrics = ledger.metric_parts(
            {
                "variant_count": 2,
                "ppl_slice_count": 4,
                "task_total_executions": 300,
                "runtime_total_executions": 300,
                "max_ppl_ratio_vs_fp16": 1.294891302929277,
                "max_accuracy_drop_vs_fp16": 0.04,
                "max_vram_ratio_vs_fp16": 0.9010177609259629,
                "max_tokens_per_second_ratio_vs_fp16": 0.3315323860144548,
            }
        )
        joined = "; ".join(metrics)
        self.assertIn("max PPL ratio 1.2949", joined)
        self.assertIn("max drop 0.0400", joined)
        self.assertIn("max VRAM ratio 0.9010", joined)
        self.assertIn("max tok/s ratio 0.3315", joined)

    def test_official_awq_public_calib_eval_metrics_are_reported(self) -> None:
        metrics = ledger.metric_parts(
            {
                "eval_slice_count": 2,
                "total_eval_tokens": 2857,
                "expected_awq_blocks": 8,
                "evals": [
                    {"ppl_ratio_awq_vs_fp16": 1.2108328},
                    {"ppl_ratio_awq_vs_fp16": 1.1817858},
                ],
            }
        )
        joined = "; ".join(metrics)
        self.assertIn("eval slices 2", joined)
        self.assertIn("eval tokens 2857", joined)
        self.assertIn("max eval PPL ratio 1.2108", joined)
        self.assertIn("AWQ blocks 8", joined)
        self.assertEqual(ledger.infer_category("official_awq_public_calib_16_eval"), "official PTQ readiness")

    def test_runtime_profile_metrics_are_reported(self) -> None:
        metrics = ledger.metric_parts(
            {
                "total_cases": 6,
                "total_tasks": 24,
                "mean_tokens_per_second": 11.46,
                "mean_ttft_seconds": 0.5084,
                "max_guard_vram_ratio": 0.6108,
                "max_guard_vram_mib": 4979,
            }
        )
        joined = "; ".join(metrics)
        self.assertIn("cases 6", joined)
        self.assertIn("tasks 24", joined)
        self.assertIn("mean tok/s 11.4600", joined)
        self.assertIn("mean TTFT 0.508400s", joined)
        self.assertIn("VRAM 0.6108", joined)
        self.assertIn("VRAM MiB 4979", joined)

    def test_parse_gate_spec_requires_label(self) -> None:
        label, path = ledger.parse_gate_spec("foo=bar.json")
        self.assertEqual(label, "foo")
        self.assertEqual(path, Path("bar.json"))
        with self.assertRaises(ValueError):
            ledger.parse_gate_spec("bar.json")


if __name__ == "__main__":
    unittest.main()
