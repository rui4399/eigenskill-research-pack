from __future__ import annotations

import argparse
import json
import tempfile
import unittest
from pathlib import Path

import gate_official_ptq_task_statistics as gate


def _write_json(path: Path, payload: dict) -> Path:
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def _summary(task_format: str, passed: list[bool]) -> dict:
    rows = [
        {
            "id": f"{task_format}_{index}",
            "score": {"passed": value},
            "ttft_seconds": 0.1,
            "tokens_per_second": 10.0,
        }
        for index, value in enumerate(passed)
    ]
    return {
        "model": "model",
        "loader": "hf",
        "task_format": task_format,
        "task_count": len(rows),
        "baseline": {
            "aggregate": {
                "tasks": len(rows),
                "passes": sum(1 for value in passed if value),
                "accuracy": sum(1 for value in passed if value) / len(rows),
            },
            "rows": rows,
        },
    }


class OfficialPtqTaskStatisticsGateTests(unittest.TestCase):
    def test_wilson_interval_contains_observed_accuracy(self) -> None:
        ci = gate.wilson_interval(4, 10)
        self.assertLess(ci["low"], ci["mean"])
        self.assertGreater(ci["high"], ci["mean"])

    def test_bootstrap_delta_is_deterministic(self) -> None:
        left = [True, False, False, True]
        right = [True, True, False, True]
        first = gate.bootstrap_paired_delta(left, right, samples=100, seed=7)
        second = gate.bootstrap_paired_delta(left, right, samples=100, seed=7)
        self.assertEqual(first, second)
        self.assertGreater(first["mean"], 0.0)

    def test_build_result_reports_paired_task_statistics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fp16_path = _write_json(root / "fp16.json", _summary("mmlu", [True, False, True, False]))
            awq_path = _write_json(root / "awq.json", _summary("mmlu", [True, True, False, False]))
            cases = [
                gate.case_summary(*gate.parse_case_spec(f"fp16:mmlu={fp16_path}")),
                gate.case_summary(*gate.parse_case_spec(f"autoawq:mmlu={awq_path}")),
            ]
            result = gate.build_result(
                cases,
                argparse.Namespace(
                    baseline_variant="fp16",
                    min_tasks_per_case=4,
                    min_shared_tasks=4,
                    max_ci_accuracy_drop=1.0,
                    bootstrap_samples=200,
                    bootstrap_seed=11,
                    matrix_title="test",
                ),
            )

        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["comparison_count"], 1)
        comparison = result["comparisons"][0]
        self.assertEqual(comparison["shared_tasks"], 4)
        self.assertEqual(comparison["discordant_pairs"]["baseline_only_correct"], 1)
        self.assertEqual(comparison["discordant_pairs"]["candidate_only_correct"], 1)

    def test_fails_when_ci_lower_bound_exceeds_allowed_drop(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fp16_path = _write_json(root / "fp16.json", _summary("mmlu", [True] * 20))
            awq_path = _write_json(root / "awq.json", _summary("mmlu", [False] * 20))
            cases = [
                gate.case_summary(*gate.parse_case_spec(f"fp16:mmlu={fp16_path}")),
                gate.case_summary(*gate.parse_case_spec(f"autoawq:mmlu={awq_path}")),
            ]
            result = gate.build_result(
                cases,
                argparse.Namespace(
                    baseline_variant="fp16",
                    min_tasks_per_case=20,
                    min_shared_tasks=20,
                    max_ci_accuracy_drop=0.2,
                    bootstrap_samples=100,
                    bootstrap_seed=11,
                    matrix_title="test",
                ),
            )

        self.assertFalse(result["passed"])
        self.assertIn("paired bootstrap low delta", result["failures"][0])


if __name__ == "__main__":
    unittest.main()
