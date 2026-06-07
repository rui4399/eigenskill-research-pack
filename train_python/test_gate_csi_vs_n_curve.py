from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import gate_csi_vs_n_curve as gate


def write_seed_gate(path: Path, n: int, rho: float, top20: float, positive: float) -> Path:
    payload = {
        "passed": True,
        "summary": {
            "case_count": 6,
            "pair_count": 15,
            "unique_prompt_selection_count": 6,
            "mean_score_spearman": rho,
            "mean_score_spearman_ci": {"samples": 100, "low": rho - 0.01, "high": rho + 0.01},
            "mean_top20_jaccard": top20,
            "mean_top20_jaccard_ci": {"samples": 100, "low": top20 - 0.01, "high": top20 + 0.01},
            "mean_positive_jaccard": positive,
            "mean_positive_jaccard_ci": {"samples": 100, "low": positive - 0.01, "high": positive + 0.01},
        },
        "n": n,
    }
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


class CSIVsNCurveGateTests(unittest.TestCase):
    def test_curve_passes_when_metrics_increase_with_n(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = gate.build_curve(
                [
                    gate.CurveCase(2, write_seed_gate(root / "n2.json", 2, 0.30, 0.40, 0.50)),
                    gate.CurveCase(4, write_seed_gate(root / "n4.json", 4, 0.45, 0.50, 0.60)),
                    gate.CurveCase(8, write_seed_gate(root / "n8.json", 8, 0.70, 0.65, 0.75)),
                ],
                min_points=3,
            )
            self.assertTrue(report["passed"])
            self.assertEqual(report["summary"]["point_count"], 3)
            self.assertAlmostEqual(report["summary"]["mean_score_spearman_gain"], 0.40)
            self.assertTrue(report["summary"]["mean_top20_jaccard_monotonic"])

    def test_curve_rejects_non_monotonic_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = gate.build_curve(
                [
                    gate.CurveCase(2, write_seed_gate(root / "n2.json", 2, 0.30, 0.40, 0.50)),
                    gate.CurveCase(4, write_seed_gate(root / "n4.json", 4, 0.29, 0.50, 0.60)),
                    gate.CurveCase(8, write_seed_gate(root / "n8.json", 8, 0.70, 0.65, 0.75)),
                ],
                min_points=3,
            )
            self.assertFalse(report["passed"])
            self.assertTrue(any("mean_score_spearman" in failure for failure in report["failures"]))

    def test_parse_case_requires_positive_integer_n(self) -> None:
        case = gate.parse_case("8=gate.json")
        self.assertEqual(case.n, 8)
        self.assertEqual(case.path, Path("gate.json"))
        with self.assertRaises(ValueError):
            gate.parse_case("n8=gate.json")
        with self.assertRaises(ValueError):
            gate.parse_case("0=gate.json")


if __name__ == "__main__":
    unittest.main()
