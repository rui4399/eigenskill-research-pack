from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import gate_csi_null_permutation as gate


def write_seed_gate(path: Path, n: int, values: list[float], *, passed: bool = True) -> Path:
    pairs = []
    for index, value in enumerate(values):
        pairs.append(
            {
                "left": f"n{n}_seed{index}",
                "right": f"n{n}_seed{index + 1}",
                "shared_modules": 4,
                "score_spearman": value,
                "top20_jaccard": value + 0.05,
                "positive_jaccard": value + 0.10,
            }
        )
    path.write_text(
        json.dumps({"passed": passed, "summary": {"pair_count": len(pairs)}, "pairs": pairs, "failures": []}),
        encoding="utf-8",
    )
    return path


class CSINullPermutationGateTests(unittest.TestCase):
    def test_parse_case_requires_positive_integer_n(self) -> None:
        case = gate.parse_case("2=seed.json")
        self.assertEqual(case.n, 2)
        self.assertEqual(case.path, Path("seed.json"))
        with self.assertRaises(ValueError):
            gate.parse_case("-1=seed.json")
        with self.assertRaises(ValueError):
            gate.parse_case("seed.json")

    def test_holm_adjust_is_monotonic_in_sorted_order(self) -> None:
        adjusted = gate.holm_adjust([0.01, 0.04, 0.02])
        self.assertEqual(adjusted, [0.03, 0.04, 0.04])

    def test_permutation_p_value_uses_plus_one_correction(self) -> None:
        result = gate.permutation_p_value([0.0, 0.0], [1.0, 1.0], samples=20, seed=7)
        self.assertGreater(result["p_value"], 0.0)
        self.assertLessEqual(result["p_value"], 1.0)
        self.assertEqual(result["observed_gain"], 1.0)

    def test_build_gate_passes_with_clear_distribution_shift(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = gate.build_gate(
                [
                    gate.NullCase(2, write_seed_gate(root / "n2.json", 2, [0.10, 0.11, 0.12, 0.13])),
                    gate.NullCase(8, write_seed_gate(root / "n8.json", 8, [0.80, 0.81, 0.82, 0.83])),
                ],
                permutation_samples=200,
                max_holm_p_value=0.05,
            )
            self.assertTrue(report["passed"])
            self.assertTrue(report["summary"]["all_observed_gains_positive"])
            self.assertTrue(report["summary"]["all_holm_significant"])

    def test_build_gate_fails_when_source_gate_failed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = gate.build_gate(
                [
                    gate.NullCase(2, write_seed_gate(root / "n2.json", 2, [0.10, 0.11, 0.12])),
                    gate.NullCase(8, write_seed_gate(root / "n8.json", 8, [0.80, 0.81, 0.82], passed=False)),
                ],
                permutation_samples=50,
            )
            self.assertFalse(report["passed"])
            self.assertTrue(any("source seed-stability gates failed" in failure for failure in report["failures"]))


if __name__ == "__main__":
    unittest.main()
