from __future__ import annotations

import argparse
import unittest

import gate_official_ptq_runtime_profile as gate


def _case(variant: str, task_format: str, tps: float, ttft: float, vram: float, tasks: int = 4) -> dict:
    return {
        "variant": variant,
        "task_format": task_format,
        "tasks": tasks,
        "passes": 1 if variant == "fp16" and task_format == "mmlu" else 0,
        "accuracy": 0.25 if variant == "fp16" and task_format == "mmlu" else 0.0,
        "mean_tokens_per_second": tps,
        "mean_ttft_seconds": ttft,
        "guard_returncode": 0,
        "killed_by_guard": False,
        "killed_by_timeout": False,
        "guard_max_memory_used_ratio": vram,
        "guard_max_memory_used_mib": int(vram * 8192),
        "guard_memory_total_mib": 8192,
    }


class OfficialPtqRuntimeProfileGateTests(unittest.TestCase):
    def test_builds_variant_profiles_and_baseline_ratios(self) -> None:
        matrix = {
            "passed": True,
            "summary": {"case_count": 4},
            "cases": [
                _case("fp16", "mmlu", 20.0, 0.40, 0.61),
                _case("fp16", "gsm8k", 10.0, 0.60, 0.60),
                _case("autoawq", "mmlu", 5.0, 0.70, 0.55),
                _case("autoawq", "gsm8k", 3.0, 0.90, 0.54),
            ],
        }

        result = gate.build_result(
            matrix,
            argparse.Namespace(
                baseline_variant="fp16",
                required_variants=["fp16", "autoawq"],
                min_cases_per_variant=2,
                max_memory_ratio=0.90,
                min_mean_tokens_per_second=1.0,
                max_mean_ttft_seconds=2.0,
            ),
        )

        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["variant_count"], 2)
        self.assertEqual(result["summary"]["total_cases"], 4)
        self.assertAlmostEqual(result["profiles"]["fp16"]["mean_tokens_per_second"], 15.0)
        self.assertAlmostEqual(result["profiles"]["autoawq"]["mean_ttft_seconds"], 0.8)
        comparison = result["comparisons"][0]
        self.assertEqual(comparison["variant"], "autoawq")
        self.assertAlmostEqual(comparison["tokens_per_second_ratio_vs_baseline"], 4.0 / 15.0)
        self.assertAlmostEqual(comparison["ttft_ratio_vs_baseline"], 0.8 / 0.5)

    def test_fails_when_runtime_metrics_are_missing_or_over_guard(self) -> None:
        matrix = {
            "passed": True,
            "summary": {"case_count": 1},
            "cases": [_case("fp16", "mmlu", 0.0, 0.0, 0.95, tasks=4)],
        }

        result = gate.build_result(
            matrix,
            argparse.Namespace(
                baseline_variant="fp16",
                required_variants=["fp16"],
                min_cases_per_variant=1,
                max_memory_ratio=0.90,
                min_mean_tokens_per_second=1.0,
                max_mean_ttft_seconds=2.0,
            ),
        )

        self.assertFalse(result["passed"])
        failures = "\n".join(result["failures"])
        self.assertIn("mean tokens/s", failures)
        self.assertIn("mean TTFT", failures)
        self.assertIn("VRAM ratio", failures)


if __name__ == "__main__":
    unittest.main()
