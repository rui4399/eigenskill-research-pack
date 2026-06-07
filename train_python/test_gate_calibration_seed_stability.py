from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import gate_calibration_seed_stability as gate


def write_sensitivity(path: Path, values: list[float], *, seed: int | None = None) -> Path:
    payload = {
        "groups": [
            {
                "module": f"layer.{idx}.proj",
                "positive_delta_nll": value,
                "delta_nll": value,
                "cost": 1.0,
            }
            for idx, value in enumerate(values)
        ]
    }
    if seed is not None:
        payload["prompt_selection"] = {
            "source": "prompts.txt",
            "pool_size": 16,
            "sample_size": 4,
            "seed": seed,
            "selected_indices": [seed % 16, (seed + 3) % 16, (seed + 6) % 16, (seed + 9) % 16],
        }
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


class CalibrationSeedStabilityGateTests(unittest.TestCase):
    def test_parse_case_requires_label_and_path(self) -> None:
        case = gate.parse_case("seed11=left.json")
        self.assertEqual(case.label, "seed11")
        self.assertEqual(case.path, Path("left.json"))
        with self.assertRaises(ValueError):
            gate.parse_case("left.json")

    def test_gate_reports_pairwise_seed_stability(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cases = [
                gate.SeedCase("seed11", write_sensitivity(root / "seed11.json", [10, 9, 2, 1], seed=11)),
                gate.SeedCase("seed12", write_sensitivity(root / "seed12.json", [9, 10, 2, 1], seed=12)),
                gate.SeedCase("seed13", write_sensitivity(root / "seed13.json", [1, 2, 9, 10], seed=13)),
            ]
            report = gate.build_gate(cases, top_k="1,2,20", min_cases=3, min_pairs=3, bootstrap_samples=50)
            self.assertTrue(report["passed"])
            self.assertEqual(report["summary"]["case_count"], 3)
            self.assertEqual(report["summary"]["pair_count"], 3)
            self.assertEqual(report["summary"]["unique_prompt_selection_count"], 3)
            self.assertEqual(report["summary"]["mean_score_spearman_ci"]["samples"], 50)
            self.assertIsNotNone(report["summary"]["mean_score_spearman_ci"]["low"])
            self.assertIsNotNone(report["summary"]["mean_top20_jaccard_ci"]["high"])
            self.assertEqual(len(report["pairs"]), 3)

    def test_bootstrap_ci_can_be_disabled(self) -> None:
        ci = gate.bootstrap_mean_ci([0.1, 0.2, 0.3], samples=0, seed=1)
        self.assertEqual(ci["samples"], 0)
        self.assertIsNone(ci["low"])

    def test_gate_rejects_missing_prompt_selection_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cases = [
                gate.SeedCase("a", write_sensitivity(root / "a.json", [4, 3, 2, 1], seed=1)),
                gate.SeedCase("b", write_sensitivity(root / "b.json", [4, 2, 3, 1])),
            ]
            report = gate.build_gate(cases)
            self.assertFalse(report["passed"])
            self.assertTrue(any("missing prompt_selection" in failure for failure in report["failures"]))


if __name__ == "__main__":
    unittest.main()
