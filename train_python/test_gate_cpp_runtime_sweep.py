from __future__ import annotations

import argparse
import unittest

import gate_cpp_runtime_sweep as gate


def args(**overrides):
    values = {
        "min_ok_rows": 2,
        "max_failed_rows": 0,
        "min_wins_vs_full": 2,
        "min_min_speedup_vs_full": 10.0,
        "min_median_speedup_vs_full": 15.0,
        "min_best_speedup_vs_full": 40.0,
        "max_median_selected_ms": 0.25,
        "min_median_compression_vs_fp32": 7.0,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def row(speedup: float, selected_ms: float = 0.2, compression: float = 7.6, ok: bool = True) -> dict:
    return {
        "ok": ok,
        "returncode": 0 if ok else 2,
        "family": "attention",
        "layer_bucket": "early",
        "selected_speedup_vs_full": speedup,
        "selected_mixed_gemv_ms": selected_ms,
        "full_mixed_gemv_ms": selected_ms * speedup,
        "compression_ratio_vs_fp32": compression,
    }


class GateCppRuntimeSweepTests(unittest.TestCase):
    def test_passes_strong_sweep(self) -> None:
        result = gate.build_result([row(16.0), row(50.0)], args())
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["wins_vs_full"], 2)

    def test_fails_when_min_speedup_is_too_low(self) -> None:
        result = gate.build_result([row(9.0), row(50.0)], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("min selected/full speedup" in failure for failure in result["failures"]))

    def test_fails_when_compression_is_too_low(self) -> None:
        result = gate.build_result([row(16.0, compression=2.0), row(50.0, compression=2.0)], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("median compression" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
