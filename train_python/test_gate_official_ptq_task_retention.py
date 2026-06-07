from __future__ import annotations

import argparse
import json
import tempfile
import unittest
from pathlib import Path

import gate_official_ptq_task_retention as gate


def _write_json(path: Path, payload: dict) -> Path:
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def _summary(model: str, task_format: str, tasks: int, passes: int, tok_s: float = 10.0) -> dict:
    return {
        "model": model,
        "task_format": task_format,
        "task_count": tasks,
        "baseline": {
            "aggregate": {
                "tasks": tasks,
                "passes": passes,
                "accuracy": passes / max(tasks, 1),
                "mean_tokens_per_second": tok_s,
                "mean_ttft_seconds": 0.25,
            }
        },
    }


def _guard(returncode: int = 0, ratio: float = 0.5) -> dict:
    return {
        "returncode": returncode,
        "killed_by_guard": False,
        "killed_by_timeout": False,
        "max_memory_used_ratio": ratio,
        "max_memory_used_mib": 4096,
        "memory_total_mib": 8192,
    }


class OfficialPtqTaskRetentionGateTests(unittest.TestCase):
    def test_builds_matrix_and_reports_quantized_accuracy_drops(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cases = []
            for variant, passes in [("fp16", 1), ("autoawq", 0), ("gptqmodel", 1)]:
                summary_path = _write_json(root / f"{variant}_mmlu.json", _summary(f"{variant}-model", "mmlu", 4, passes))
                guard_path = _write_json(root / f"{variant}_mmlu_guard.json", _guard())
                cases.append(gate.parse_case_spec(f"{variant}:mmlu={summary_path}={guard_path}"))

            result = gate.build_result(
                [gate.case_summary(*case) for case in cases],
                argparse.Namespace(
                    baseline_variant="fp16",
                    required_variants=["fp16", "autoawq", "gptqmodel"],
                    required_formats=["mmlu"],
                    min_tasks_per_case=4,
                    max_memory_ratio=0.90,
                    max_accuracy_drop=0.25,
                ),
            )

            self.assertTrue(result["passed"])
            self.assertEqual(result["summary"]["variant_count"], 3)
            self.assertEqual(result["summary"]["format_count"], 1)
            self.assertEqual(result["summary"]["total_tasks"], 12)
            self.assertEqual(result["summary"]["max_accuracy_drop_vs_fp16"], 0.25)
            self.assertEqual(result["summary"]["baseline_zero_accuracy_formats"], [])

            autoawq = [row for row in result["comparisons"] if row["variant"] == "autoawq"][0]
            self.assertEqual(autoawq["baseline_variant"], "fp16")
            self.assertEqual(autoawq["task_format"], "mmlu")
            self.assertEqual(autoawq["accuracy_drop_vs_baseline"], 0.25)

    def test_fails_when_quantized_case_exceeds_accuracy_drop(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fp16 = gate.case_summary(
                *gate.parse_case_spec(
                    f"fp16:mmlu={_write_json(root / 'fp16.json', _summary('fp16', 'mmlu', 4, 4))}="
                    f"{_write_json(root / 'fp16_guard.json', _guard())}"
                )
            )
            awq = gate.case_summary(
                *gate.parse_case_spec(
                    f"autoawq:mmlu={_write_json(root / 'awq.json', _summary('awq', 'mmlu', 4, 0))}="
                    f"{_write_json(root / 'awq_guard.json', _guard())}"
                )
            )

            result = gate.build_result(
                [fp16, awq],
                argparse.Namespace(
                    baseline_variant="fp16",
                    required_variants=["fp16", "autoawq"],
                    required_formats=["mmlu"],
                    min_tasks_per_case=4,
                    max_memory_ratio=0.90,
                    max_accuracy_drop=0.5,
                ),
            )

            self.assertFalse(result["passed"])
            self.assertIn("accuracy drop", result["failures"][0])

    def test_marks_zero_accuracy_baseline_formats_as_execution_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cases = []
            for variant in ["fp16", "autoawq"]:
                summary_path = _write_json(root / f"{variant}_gsm8k.json", _summary(f"{variant}-model", "gsm8k", 4, 0))
                guard_path = _write_json(root / f"{variant}_gsm8k_guard.json", _guard())
                cases.append(gate.parse_case_spec(f"{variant}:gsm8k={summary_path}={guard_path}"))

            result = gate.build_result(
                [gate.case_summary(*case) for case in cases],
                argparse.Namespace(
                    baseline_variant="fp16",
                    required_variants=["fp16", "autoawq"],
                    required_formats=["gsm8k"],
                    min_tasks_per_case=4,
                    max_memory_ratio=0.90,
                    max_accuracy_drop=0.25,
                ),
            )

            self.assertTrue(result["passed"])
            self.assertEqual(result["summary"]["baseline_zero_accuracy_formats"], ["gsm8k"])
            self.assertIn("execution-only", result["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
