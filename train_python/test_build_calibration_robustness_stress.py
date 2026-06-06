from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import build_calibration_robustness_stress as stress


def write_ppl_summary(path: Path, rows: dict[str, float]) -> Path:
    payload = {
        "model": "toy",
        "results": [
            {"name": name, "metrics": {"ppl": value}}
            for name, value in rows.items()
        ],
    }
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


class CalibrationRobustnessStressTests(unittest.TestCase):
    def test_sign_test_p_value_is_exact_one_sided(self) -> None:
        self.assertAlmostEqual(stress.sign_test_p_value(wins=3, trials=3), 0.125)
        self.assertAlmostEqual(stress.sign_test_p_value(wins=2, trials=3), 0.5)

    def test_bootstrap_ci_is_deterministic_and_contains_mean(self) -> None:
        first = stress.bootstrap_mean_ci([1.0, 2.0, 3.0], iterations=200, seed=11)
        second = stress.bootstrap_mean_ci([1.0, 2.0, 3.0], iterations=200, seed=11)
        self.assertEqual(first, second)
        self.assertLessEqual(first["low"], first["mean"])
        self.assertGreaterEqual(first["high"], first["mean"])

    def test_case_metrics_measure_uniform_random_and_fp16_regret(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = write_ppl_summary(
                Path(tmp) / "summary.json",
                {
                    "fp16": 10.0,
                    "uniform_int4": 20.0,
                    "mean_consensus": 13.0,
                    "random_seed_0": 15.0,
                    "random_seed_1": 17.0,
                },
            )
            case = stress.build_case("toy", path, "mean_consensus")

        self.assertEqual(case["target_name"], "mean_consensus")
        self.assertEqual(case["random_count"], 2)
        self.assertAlmostEqual(case["target_margin_vs_uniform"], 7.0)
        self.assertAlmostEqual(case["target_margin_vs_best_random"], 2.0)
        self.assertAlmostEqual(case["target_fp16_regret"], 3.0)
        self.assertTrue(case["beats_uniform"])
        self.assertTrue(case["beats_best_random"])

    def test_auto_target_prefers_consensus_names_before_loss_sensitive(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = write_ppl_summary(
                Path(tmp) / "summary.json",
                {
                    "fp16": 10.0,
                    "uniform_int4": 20.0,
                    "wikitext_c4_consensus": 12.0,
                    "cpp_loss_sensitive_budget": 11.5,
                    "random_seed_0": 13.0,
                },
            )
            case = stress.build_case("toy", path, "auto")

        self.assertEqual(case["target_name"], "wikitext_c4_consensus")

    def test_report_fails_when_best_random_wins_too_often(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cases = [
                stress.CaseSpec("good", write_ppl_summary(root / "good.json", {
                    "fp16": 10.0,
                    "uniform_int4": 20.0,
                    "target": 12.0,
                    "random_seed_0": 13.0,
                }), "target"),
                stress.CaseSpec("bad", write_ppl_summary(root / "bad.json", {
                    "fp16": 10.0,
                    "uniform_int4": 20.0,
                    "target": 16.0,
                    "random_seed_0": 15.0,
                }), "target"),
            ]
            report = stress.build_report(cases, min_cases=2, min_best_random_win_rate=1.0)

        self.assertFalse(report["passed"])
        self.assertEqual(report["summary"]["target_wins_vs_best_random"], 1)
        self.assertIn("sign_test_p_vs_best_random", report["summary"])
        self.assertIn("mean_margin_vs_best_random_ci", report["summary"])
        self.assertIn("best-random win rate", report["failures"][0])


if __name__ == "__main__":
    unittest.main()
