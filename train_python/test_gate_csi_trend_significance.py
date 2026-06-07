from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import gate_csi_trend_significance as gate


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


class CSITrendSignificanceGateTests(unittest.TestCase):
    def test_parse_case_requires_positive_integer_n(self) -> None:
        case = gate.parse_case("8=foo.json")
        self.assertEqual(case.n, 8)
        self.assertEqual(case.path, Path("foo.json"))
        with self.assertRaises(ValueError):
            gate.parse_case("0=foo.json")
        with self.assertRaises(ValueError):
            gate.parse_case("foo.json")

    def test_dominance_probability_counts_ties_as_half(self) -> None:
        self.assertEqual(gate.dominance_probability([1.0], [2.0]), 1.0)
        self.assertEqual(gate.dominance_probability([2.0], [1.0]), 0.0)
        self.assertEqual(gate.dominance_probability([1.0], [1.0]), 0.5)

    def test_build_gate_passes_when_full_range_gain_is_stable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cases = [
                gate.TrendCase(2, write_seed_gate(root / "n2.json", 2, [0.10, 0.12, 0.14])),
                gate.TrendCase(4, write_seed_gate(root / "n4.json", 4, [0.20, 0.22, 0.24])),
                gate.TrendCase(8, write_seed_gate(root / "n8.json", 8, [0.40, 0.42, 0.44])),
            ]
            report = gate.build_gate(
                cases,
                bootstrap_samples=200,
                min_full_range_gain_low=0.0,
                min_full_range_dominance_probability=0.90,
            )
            self.assertTrue(report["passed"])
            self.assertTrue(report["summary"]["all_full_range_gain_ci_positive"])
            self.assertGreaterEqual(report["summary"]["min_full_range_dominance_probability"], 0.90)

    def test_build_gate_fails_when_source_gate_failed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cases = [
                gate.TrendCase(2, write_seed_gate(root / "n2.json", 2, [0.40, 0.41, 0.42])),
                gate.TrendCase(4, write_seed_gate(root / "n4.json", 4, [0.43, 0.44, 0.45])),
                gate.TrendCase(8, write_seed_gate(root / "n8.json", 8, [0.46, 0.47, 0.48], passed=False)),
            ]
            report = gate.build_gate(cases, bootstrap_samples=50)
            self.assertFalse(report["passed"])
            self.assertTrue(any("source seed-stability gates failed" in failure for failure in report["failures"]))


if __name__ == "__main__":
    unittest.main()
