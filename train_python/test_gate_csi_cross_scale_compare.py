from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import gate_csi_cross_scale_compare as gate


def write_curve(path: Path, points: list[dict]) -> Path:
    path.write_text(
        json.dumps({"passed": True, "summary": {"point_count": len(points)}, "points": points}),
        encoding="utf-8",
    )
    return path


class CsiCrossScaleCompareTests(unittest.TestCase):
    def test_reports_same_n_deltas_and_gain_deltas(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            left = write_curve(
                root / "left.json",
                [
                    {"n": 2, "mean_score_spearman": 0.3, "mean_top20_jaccard": 0.4, "mean_positive_jaccard": 0.5},
                    {"n": 8, "mean_score_spearman": 0.7, "mean_top20_jaccard": 0.6, "mean_positive_jaccard": 0.8},
                ],
            )
            right = write_curve(
                root / "right.json",
                [
                    {"n": 2, "mean_score_spearman": 0.1, "mean_top20_jaccard": 0.2, "mean_positive_jaccard": 0.3},
                    {"n": 8, "mean_score_spearman": 0.6, "mean_top20_jaccard": 0.5, "mean_positive_jaccard": 0.7},
                ],
            )
            report = gate.build_report(gate.ScaleCase("0.5B", left), gate.ScaleCase("1.5B", right))
        self.assertTrue(report["passed"])
        self.assertTrue(report["summary"]["right_lower_all_same_n_metrics"])
        self.assertAlmostEqual(report["same_n_comparison"][0]["mean_score_spearman"]["right_minus_left"], -0.2)
        self.assertAlmostEqual(report["gain_comparison"][0]["right_minus_left_gain"], 0.1)

    def test_fails_with_too_few_common_n_values(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            left = write_curve(root / "left.json", [{"n": 2, "mean_score_spearman": 0.3}])
            right = write_curve(root / "right.json", [{"n": 2, "mean_score_spearman": 0.1}])
            report = gate.build_report(gate.ScaleCase("a", left), gate.ScaleCase("b", right))
        self.assertFalse(report["passed"])
        self.assertIn("need at least two common n values", report["failures"][0])


if __name__ == "__main__":
    unittest.main()
