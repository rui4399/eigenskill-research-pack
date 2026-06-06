from __future__ import annotations

import argparse
import unittest

import gate_selected_row_benchmark as gate


def args(**overrides):
    values = {
        "packed_runtime": "triton_selected",
        "cached_runtime": "cached_selected",
        "dense_selected_runtime": "dense_selected",
        "min_ok_rows": 4,
        "max_failed_rows": 0,
        "min_packed_cases": 1,
        "min_packed_wins_vs_full": 1,
        "min_best_packed_speedup_vs_full": 1.05,
        "max_rel_l2": 0.25,
        "min_cached_median_speedup_vs_full": 1.0,
        "min_dense_selected_wins_vs_full": 1,
        "max_memory_ratio": 0.90,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def row(runtime: str, speedup: float, rel_l2: float = 0.1, ok: bool = True) -> dict:
    return {
        "ok": ok,
        "runtime": runtime,
        "speedup_vs_dense_full": speedup,
        "rel_l2_vs_dense_selected": rel_l2,
    }


def benchmark(packed_speedup: float = 1.3) -> dict:
    return {
        "model": "Qwen/Qwen3-0.6B",
        "module_count": 1,
        "batches": [1],
        "selected_rows": [64],
        "rows": [
            row("dense_full", 1.0, 0.0),
            row("dense_selected", 1.2, 0.0),
            row("cached_selected", 1.1, 0.1),
            row("triton_selected", packed_speedup, 0.1),
        ],
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


class GateSelectedRowBenchmarkTests(unittest.TestCase):
    def test_passes_with_packed_win_and_guard(self) -> None:
        result = gate.build_result(benchmark(), guard(), args())
        self.assertTrue(result["passed"])
        self.assertEqual(result["runtime_summaries"]["triton_selected"]["wins_vs_full"], 1)

    def test_fails_without_packed_win(self) -> None:
        result = gate.build_result(benchmark(packed_speedup=0.9), guard(), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("wins" in failure for failure in result["failures"]))

    def test_fails_when_guard_memory_exceeds_limit(self) -> None:
        result = gate.build_result(benchmark(), guard(memory_ratio=0.95), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("memory ratio" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
