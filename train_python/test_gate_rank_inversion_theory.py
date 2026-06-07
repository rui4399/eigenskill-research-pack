from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import gate_rank_inversion_theory as gate


def write_sensitivity_artifact(path: Path, scores: dict[str, float]) -> Path:
    groups = [
        {
            "module": module,
            "positive_delta_nll": score,
            "cost": 1.0,
        }
        for module, score in scores.items()
    ]
    path.write_text(json.dumps({"groups": groups}), encoding="utf-8")
    return path


def write_seed_gate(path: Path, n: int, seed_scores: list[dict[str, float]]) -> Path:
    prompt_selections = []
    for idx, scores in enumerate(seed_scores):
        artifact = write_sensitivity_artifact(path.parent / f"n{n}_seed{idx}.json", scores)
        prompt_selections.append({"label": f"n{n}_seed{idx}", "path": str(artifact)})
    path.write_text(
        json.dumps({"passed": True, "prompt_selections": prompt_selections}),
        encoding="utf-8",
    )
    return path


class RankInversionTheoryGateTests(unittest.TestCase):
    def test_gate_passes_when_inversion_risk_decreases(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            n2 = write_seed_gate(
                root / "n2_gate.json",
                2,
                [
                    {"a": 4.0, "b": 3.0, "c": 2.0, "d": 1.0},
                    {"a": 2.0, "b": 4.0, "c": 1.0, "d": 3.0},
                    {"a": 3.0, "b": 2.0, "c": 4.0, "d": 1.0},
                ],
            )
            n4 = write_seed_gate(
                root / "n4_gate.json",
                4,
                [
                    {"a": 4.0, "b": 3.0, "c": 2.0, "d": 1.0},
                    {"a": 2.8, "b": 3.2, "c": 1.8, "d": 1.2},
                    {"a": 4.1, "b": 2.9, "c": 2.2, "d": 0.9},
                ],
            )
            n8 = write_seed_gate(
                root / "n8_gate.json",
                8,
                [
                    {"a": 4.00, "b": 3.00, "c": 2.00, "d": 1.00},
                    {"a": 4.02, "b": 2.98, "c": 2.01, "d": 0.99},
                    {"a": 3.99, "b": 3.01, "c": 1.99, "d": 1.01},
                ],
            )
            report = gate.build_gate(
                [gate.RiskCase(2, n2), gate.RiskCase(4, n4), gate.RiskCase(8, n8)],
                margin_quantile=0.0,
                max_final_margin_inversion_rate=0.01,
            )
            self.assertTrue(report["passed"])
            self.assertTrue(report["summary"]["mean_empirical_inversion_rate_decreasing"])
            self.assertTrue(report["summary"]["mean_chebyshev_bound_decreasing"])

    def test_gate_rejects_when_final_margin_risk_is_too_high(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            noisy = [
                {"a": 4.0, "b": 3.0, "c": 2.0, "d": 1.0},
                {"a": 2.0, "b": 4.0, "c": 1.0, "d": 3.0},
                {"a": 3.0, "b": 2.0, "c": 4.0, "d": 1.0},
            ]
            n2 = write_seed_gate(root / "n2_gate.json", 2, noisy)
            n4 = write_seed_gate(root / "n4_gate.json", 4, noisy)
            n8 = write_seed_gate(root / "n8_gate.json", 8, noisy)
            report = gate.build_gate(
                [gate.RiskCase(2, n2), gate.RiskCase(4, n4), gate.RiskCase(8, n8)],
                margin_quantile=0.0,
                max_final_margin_inversion_rate=0.01,
            )
            self.assertFalse(report["passed"])
            self.assertTrue(any("final margin" in failure for failure in report["failures"]))

    def test_parse_case_requires_positive_integer_n(self) -> None:
        case = gate.parse_case("8=seed_gate.json")
        self.assertEqual(case.n, 8)
        self.assertEqual(case.path, Path("seed_gate.json"))
        with self.assertRaises(ValueError):
            gate.parse_case("n8=seed_gate.json")
        with self.assertRaises(ValueError):
            gate.parse_case("0=seed_gate.json")


if __name__ == "__main__":
    unittest.main()
