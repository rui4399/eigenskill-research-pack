from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import gate_sensitivity_perturbation_matrix as gate


def write_sensitivity(path: Path, values: list[float]) -> Path:
    path.write_text(
        json.dumps(
            {
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
        ),
        encoding="utf-8",
    )
    return path


class SensitivityPerturbationMatrixTests(unittest.TestCase):
    def test_parse_case_requires_axis_label_and_paths(self) -> None:
        case = gate.parse_case("sample_size:qwen=left.json=right.json")
        self.assertEqual(case.axis, "sample_size")
        self.assertEqual(case.label, "qwen")
        self.assertEqual(case.left, Path("left.json"))
        self.assertEqual(case.right, Path("right.json"))
        with self.assertRaises(ValueError):
            gate.parse_case("qwen=left.json=right.json")

    def test_gate_passes_when_sample_size_is_stable_and_scale_transfer_is_weak(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cases = [
                gate.PerturbationCase(
                    "sample_size",
                    "small",
                    write_sensitivity(root / "small_a.json", [10, 9, 8, 1]),
                    write_sensitivity(root / "small_b.json", [10, 8, 9, 1]),
                ),
                gate.PerturbationCase(
                    "sample_size",
                    "large",
                    write_sensitivity(root / "large_a.json", [7, 6, 5, 1]),
                    write_sensitivity(root / "large_b.json", [7, 5, 6, 1]),
                ),
                gate.PerturbationCase(
                    "model_scale",
                    "cross",
                    write_sensitivity(root / "cross_a.json", [10, 9, 2, 1]),
                    write_sensitivity(root / "cross_b.json", [1, 2, 9, 10]),
                ),
            ]
            report = gate.build_gate(
                cases,
                top_k="1,2",
                min_sample_size_spearman=0.5,
                max_model_scale_spearman=0.3,
                min_separation_margin=0.2,
            )
            self.assertTrue(report["passed"])
            self.assertEqual(report["summary"]["sample_size_case_count"], 2)
            self.assertEqual(report["summary"]["model_scale_case_count"], 1)
            self.assertGreater(report["summary"]["perturbation_separation_margin"], 0.2)

    def test_gate_fails_without_scale_separation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stable_a = write_sensitivity(root / "a.json", [4, 3, 2, 1])
            stable_b = write_sensitivity(root / "b.json", [4, 3, 2, 1])
            cases = [
                gate.PerturbationCase("sample_size", "one", stable_a, stable_b),
                gate.PerturbationCase("sample_size", "two", stable_a, stable_b),
                gate.PerturbationCase("model_scale", "cross", stable_a, stable_b),
            ]
            report = gate.build_gate(cases, min_separation_margin=0.2)
            self.assertFalse(report["passed"])
            self.assertTrue(any("model_scale mean Spearman" in failure for failure in report["failures"]))


if __name__ == "__main__":
    unittest.main()
