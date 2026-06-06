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

    def test_parse_gate_spec_requires_label(self) -> None:
        label, path = ledger.parse_gate_spec("foo=bar.json")
        self.assertEqual(label, "foo")
        self.assertEqual(path, Path("bar.json"))
        with self.assertRaises(ValueError):
            ledger.parse_gate_spec("bar.json")


if __name__ == "__main__":
    unittest.main()
