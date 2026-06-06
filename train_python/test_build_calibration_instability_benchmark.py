from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import build_calibration_instability_benchmark as cib


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


class CalibrationInstabilityBenchmarkTests(unittest.TestCase):
    def test_parse_case(self) -> None:
        case = cib.parse_case("qwen=left.json=right.json")
        self.assertEqual(case.label, "qwen")
        self.assertEqual(case.left, Path("left.json"))
        self.assertEqual(case.right, Path("right.json"))

    def test_builds_multi_case_gate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cases = [
                cib.CaseSpec("unstable_a", write_sensitivity(root / "a_l.json", [10, 9, 1]), write_sensitivity(root / "a_r.json", [1, 9, 10]), "wiki", "c4"),
                cib.CaseSpec("unstable_b", write_sensitivity(root / "b_l.json", [7, 6, 1]), write_sensitivity(root / "b_r.json", [1, 6, 7]), "wiki", "c4"),
                cib.CaseSpec("stable", write_sensitivity(root / "c_l.json", [3, 2, 1]), write_sensitivity(root / "c_r.json", [3, 2, 1]), "wiki", "c4"),
            ]
            report = cib.build_benchmark(cases, min_cases=3, min_unstable_cases=2, top_k="1,2")
            self.assertTrue(report["passed"])
            self.assertEqual(report["summary"]["case_count"], 3)
            self.assertEqual(report["summary"]["unstable_case_count"], 2)

    def test_gate_fails_when_too_few_unstable_cases(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cases = [
                cib.CaseSpec("stable_a", write_sensitivity(root / "a_l.json", [3, 2, 1]), write_sensitivity(root / "a_r.json", [3, 2, 1]), "wiki", "c4"),
                cib.CaseSpec("stable_b", write_sensitivity(root / "b_l.json", [4, 2, 1]), write_sensitivity(root / "b_r.json", [4, 2, 1]), "wiki", "c4"),
            ]
            report = cib.build_benchmark(cases, min_cases=2, min_unstable_cases=1)
            self.assertFalse(report["passed"])
            self.assertIn("unstable case count", report["failures"][0])


if __name__ == "__main__":
    unittest.main()
