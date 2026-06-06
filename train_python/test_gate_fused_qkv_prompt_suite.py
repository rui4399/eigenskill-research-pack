from __future__ import annotations

import argparse
import unittest

import gate_fused_qkv_prompt_suite as gate


def args(**overrides):
    values = {
        "min_prompts": 6,
        "min_exact_matches": 6,
        "min_exact_match_rate": 1.0,
        "min_mean_char_edit_similarity": 0.99,
        "min_median_char_edit_similarity": 0.99,
        "min_mean_common_prefix_ratio": 0.99,
        "min_mean_speed_ratio": 0.80,
        "max_median_ttft_ratio": 1.25,
        "min_compression_vs_fp32": 3.5,
        "max_median_replacement_ms": 0.25,
        "min_wrapper_calls": 100,
        "min_fused_compute_calls": 30,
        "min_cache_hits": 60,
        "min_cache_misses": 30,
        "min_scored_prompts": 6,
        "max_rule_regressions": 0,
        "min_fused_rule_pass_rate": 0.80,
        "max_fused_rule_pass_drop": 0,
        "max_memory_ratio": 0.90,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def prompt_suite(**overrides) -> dict:
    values = {
        "model": "Qwen/Qwen3-0.6B",
        "layers": [1, 7],
        "package_summary": "pack_summary.json",
        "aggregate": {
            "prompts": 6,
            "exact_matches": 6,
            "exact_match_rate": 1.0,
            "mean_char_edit_similarity": 1.0,
            "median_char_edit_similarity": 1.0,
            "mean_common_prefix_ratio": 1.0,
            "mean_speedup_fused_vs_baseline": 0.90,
            "median_baseline_ttft_seconds": 0.04,
            "median_fused_ttft_seconds": 0.044,
        },
        "replacement_compression_vs_fp32": 3.9,
        "replacement_cuda_event_ms": {"median": 0.14, "max": 0.5},
        "replacement_wrapper_calls": 1152,
        "replacement_fused_compute_calls": 384,
        "replacement_cache_hits": 768,
        "replacement_cache_misses": 384,
        "peak_gpu_memory_mib": 1200.0,
    }
    values.update(overrides)
    return values


def scored(**overrides) -> dict:
    values = {
        "aggregate": {
            "prompts": 6,
            "baseline_passes": 5,
            "fused_passes": 5,
            "fused_pass_rate": 5 / 6,
            "regressions": 0,
            "improvements": 0,
            "rule_count": 2,
        }
    }
    values.update(overrides)
    return values


def guard(memory_ratio: float = 0.5) -> dict:
    return {
        "returncode": 0,
        "killed_by_guard": False,
        "killed_by_timeout": False,
        "max_memory_used_ratio": memory_ratio,
        "max_memory_used_mib": 4000,
        "memory_total_mib": 8000,
    }


class GateFusedQkvPromptSuiteTests(unittest.TestCase):
    def test_passes_quality_preserving_prompt_suite(self) -> None:
        result = gate.build_result(prompt_suite(), scored(), guard(), args())
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["scored"]["regressions"], 0)

    def test_fails_when_exact_match_rate_is_too_low(self) -> None:
        data = prompt_suite(aggregate={**prompt_suite()["aggregate"], "exact_matches": 4, "exact_match_rate": 4 / 6})
        result = gate.build_result(data, scored(), guard(), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("exact match" in failure for failure in result["failures"]))

    def test_fails_on_rule_regression(self) -> None:
        data = scored(aggregate={**scored()["aggregate"], "fused_passes": 4, "regressions": 1, "fused_pass_rate": 4 / 6})
        result = gate.build_result(prompt_suite(), data, guard(), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("rule regressions" in failure for failure in result["failures"]))

    def test_fails_when_cache_invariant_breaks(self) -> None:
        data = prompt_suite(replacement_cache_hits=700)
        result = gate.build_result(data, scored(), guard(), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("wrapper calls" in failure for failure in result["failures"]))

    def test_fails_on_guard_memory_excess(self) -> None:
        result = gate.build_result(prompt_suite(), scored(), guard(memory_ratio=0.95), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("memory ratio" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
