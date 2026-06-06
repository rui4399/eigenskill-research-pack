from __future__ import annotations

import argparse
import unittest

import gate_fused_qkv_generation as gate


def args(**overrides):
    values = {
        "min_replacements": 1,
        "min_generated_tokens": 16,
        "min_tokens_per_second": 10.0,
        "min_compression_vs_fp32": 5.0,
        "max_median_replacement_ms": 0.5,
        "max_max_replacement_ms": 1.0,
        "min_wrapper_calls_per_replacement": 48,
        "min_fused_compute_calls_per_replacement": 16,
        "min_cache_hits_per_replacement": 32,
        "min_cache_misses_per_replacement": 16,
        "min_tps_ratio_vs_baseline": 1.05,
        "max_ttft_ratio_vs_baseline": 1.0,
        "require_generated_text_match": False,
        "min_common_prefix_chars": 12,
        "max_memory_ratio": 0.90,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def replacement_item(**overrides) -> dict:
    values = {
        "modules": [
            "model.layers.0.self_attn.q_proj",
            "model.layers.0.self_attn.k_proj",
            "model.layers.0.self_attn.v_proj",
        ],
        "wrapper_calls": 48,
        "fused_compute_calls": 16,
        "cache_hits": 32,
        "cache_misses": 16,
        "compression_vs_fp32": 6.1,
        "input_shapes": ["1x12x1024", "1x1x1024"],
        "cuda_event_ms": {"sum": 3.2, "mean": 0.2, "median": 0.18, "p90": 0.3, "max": 0.6},
    }
    values.update(overrides)
    return values


def generation(**overrides) -> dict:
    replacements = [replacement_item()]
    values = {
        "model": "Qwen/Qwen3-0.6B",
        "mode": gate.EXPECTED_MODE,
        "layers": [0],
        "replacement_count": 1,
        "replacements": replacements,
        "replacement_compression_vs_fp32": 6.1,
        "replacement_cuda_event_ms": {"sum": 3.2, "mean": 0.2, "median": 0.18, "p90": 0.3, "max": 0.6},
        "generated_tokens_text_retokenized": 16,
        "ttft_seconds": 0.03,
        "elapsed_seconds": 0.50,
        "tokens_per_second": 32.0,
        "generated_text": "same prefix replacement output",
        "peak_gpu_memory_mib": 1200.0,
    }
    values.update(overrides)
    return values


def baseline(text: str = "same prefix baseline output", tps: float = 25.0, ttft: float = 0.04) -> dict:
    return {
        "mode": "hf_same_loader",
        "tokens_per_second": tps,
        "ttft_seconds": ttft,
        "generated_text": text,
    }


def guard(memory_ratio: float = 0.5) -> dict:
    return {
        "returncode": 0,
        "killed_by_guard": False,
        "killed_by_timeout": False,
        "max_memory_used_ratio": memory_ratio,
        "max_memory_used_mib": 4000,
        "memory_total_mib": 8000,
    }


class GateFusedQkvGenerationTests(unittest.TestCase):
    def test_passes_when_replacement_runs_and_cache_invariants_hold(self) -> None:
        result = gate.build_result(generation(), baseline(), guard(), args())
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["total_fused_compute_calls"], 16)
        self.assertEqual(result["summary"]["total_cache_hits"], 32)

    def test_fails_when_cache_invariant_breaks(self) -> None:
        broken = generation(replacements=[replacement_item(cache_hits=16)])
        result = gate.build_result(broken, baseline(), guard(), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("wrapper calls" in failure for failure in result["failures"]))

    def test_fails_when_compression_too_low(self) -> None:
        result = gate.build_result(generation(replacement_compression_vs_fp32=2.0), baseline(), guard(), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("compression" in failure for failure in result["failures"]))

    def test_fails_on_speed_regression(self) -> None:
        result = gate.build_result(generation(tokens_per_second=20.0), baseline(tps=25.0), guard(), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("tokens/s ratio" in failure for failure in result["failures"]))

    def test_fails_on_prefix_regression(self) -> None:
        result = gate.build_result(generation(generated_text="abc"), baseline(text="xyz"), guard(), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("common prefix" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
