from __future__ import annotations

import argparse
import unittest

import gate_fused_sidecar_generation as gate


def args(**overrides):
    values = {
        "min_layers": 2,
        "min_sidecars": 2,
        "min_sidecar_calls": 8,
        "min_calls_per_sidecar": 4,
        "min_selected_rows_total": 128,
        "min_generated_tokens": 4,
        "min_tokens_per_second": 1.0,
        "max_median_sidecar_ms": 1.0,
        "max_max_sidecar_ms": 2.0,
        "require_prefill_shape": True,
        "require_decode_shape": True,
        "require_generated_text_match": True,
        "min_tps_ratio_vs_baseline": 0.70,
        "max_memory_ratio": 0.90,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def sidecar_item(layer: int, calls: int = 4, errors: list[str] | None = None) -> dict:
    return {
        "layer": layer,
        "calls": calls,
        "selected_rows_total": 192,
        "low_rows_total": 128,
        "high_rows_total": 64,
        "input_shapes": ["1x12x1024", "1x1x1024"],
        "cuda_event_ms": {"sum": 1.0, "mean": 0.25, "median": 0.20, "p90": 0.30, "max": 0.40},
        "errors": errors or [],
    }


def generation(**overrides) -> dict:
    sidecars = [sidecar_item(0), sidecar_item(1)]
    values = {
        "model": "Qwen/Qwen3-0.6B",
        "mode": gate.EXPECTED_MODE,
        "layers": [0, 1],
        "sidecar_sync_mode": "end",
        "selected_rows_per_module": 64,
        "generated_tokens_text_retokenized": 8,
        "ttft_seconds": 0.05,
        "elapsed_seconds": 0.40,
        "tokens_per_second": 20.0,
        "generated_text": "ok",
        "sidecars": sidecars,
        "sidecar_call_count": sum(item["calls"] for item in sidecars),
        "sidecar_cuda_event_ms": {"sum": 2.0, "mean": 0.25, "median": 0.20, "p90": 0.30, "max": 0.40},
        "peak_gpu_memory_mib": 1200.0,
    }
    values.update(overrides)
    return values


def baseline(text: str = "ok", tps: float = 25.0) -> dict:
    return {
        "mode": "hf_same_loader",
        "tokens_per_second": tps,
        "generated_text": text,
    }


def guard(memory_ratio: float = 0.50, returncode: int = 0) -> dict:
    return {
        "returncode": returncode,
        "killed_by_guard": False,
        "killed_by_timeout": False,
        "max_memory_used_ratio": memory_ratio,
        "max_memory_used_mib": 4000,
        "memory_total_mib": 8000,
    }


class GateFusedSidecarGenerationTests(unittest.TestCase):
    def test_passes_when_sidecars_run_and_match_baseline(self) -> None:
        result = gate.build_result(generation(), baseline(), guard(), args())
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["sidecar_call_count"], 8)
        self.assertTrue(result["summary"]["generated_text_matches_baseline"])

    def test_fails_on_sidecar_error(self) -> None:
        broken = generation(sidecars=[sidecar_item(0, errors=["boom"]), sidecar_item(1)])
        broken["sidecar_call_count"] = 8
        result = gate.build_result(broken, baseline(), guard(), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("boom" in failure for failure in result["failures"]))

    def test_fails_on_baseline_text_mismatch(self) -> None:
        result = gate.build_result(generation(), baseline(text="different"), guard(), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("generated text differs" in failure for failure in result["failures"]))

    def test_fails_on_throughput_ratio_regression(self) -> None:
        result = gate.build_result(generation(tokens_per_second=10.0), baseline(tps=25.0), guard(), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("tokens/s ratio" in failure for failure in result["failures"]))

    def test_fails_when_guard_memory_exceeds_limit(self) -> None:
        result = gate.build_result(generation(), baseline(), guard(memory_ratio=0.95), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("memory ratio" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
