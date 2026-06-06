from __future__ import annotations

import argparse
import unittest

import gate_triton_tuning as gate


def _args(**overrides):
    defaults = {
        "min_valid_configs": 2,
        "min_fp16_wins": 1,
        "min_best_fp16_speedup": 1.05,
        "min_rowwise_wins": 1,
        "max_rel_l2": 0.20,
        "max_vram_ratio": 0.90,
    }
    defaults.update(overrides)
    return argparse.Namespace(**defaults)


class GateTritonTuningTests(unittest.TestCase):
    def test_summary_counts_wins_and_best_configs(self) -> None:
        rows = [
            {
                "returncode": 0,
                "rows": 2048,
                "cols": 1024,
                "batch": 16,
                "block_m": 16,
                "block_n": 8,
                "block_k": 128,
                "grouped_mixed_ms": 0.04,
                "torch_fp16_ms": 0.06,
                "rowwise_mixed_ms": 0.12,
                "grouped_speedup_vs_torch_fp16": 1.5,
                "grouped_speedup_vs_rowwise": 3.0,
                "grouped_rel_l2": 0.13,
                "guard_max_memory_used_ratio": 0.44,
                "compression_ratio_vs_fp16": 3.7,
            },
            {
                "returncode": 0,
                "grouped_mixed_ms": 0.10,
                "torch_fp16_ms": 0.05,
                "rowwise_mixed_ms": 0.20,
                "grouped_speedup_vs_torch_fp16": 0.5,
                "grouped_speedup_vs_rowwise": 2.0,
                "grouped_rel_l2": 0.12,
                "guard_max_memory_used_ratio": 0.45,
                "compression_ratio_vs_fp16": 3.6,
            },
            {"returncode": 1, "grouped_mixed_ms": None},
        ]
        summary = gate.summarize(rows)
        self.assertEqual(summary["total_configs"], 3)
        self.assertEqual(summary["valid_configs"], 2)
        self.assertEqual(summary["fp16_wins"], 1)
        self.assertEqual(summary["rowwise_wins"], 2)
        self.assertEqual(summary["best_fp16_speedup"], 1.5)
        self.assertEqual(summary["best_rowwise_speedup"], 3.0)

        failures = gate.check_gate(summary, _args())
        self.assertEqual(failures, [])

    def test_gate_fails_on_memory_or_missing_fp16_win(self) -> None:
        summary = gate.summarize(
            [
                {
                    "returncode": 0,
                    "grouped_mixed_ms": 0.10,
                    "grouped_speedup_vs_torch_fp16": 0.9,
                    "grouped_speedup_vs_rowwise": 1.2,
                    "grouped_rel_l2": 0.10,
                    "guard_max_memory_used_ratio": 0.95,
                }
            ]
        )
        failures = gate.check_gate(summary, _args(min_valid_configs=1))
        self.assertTrue(any("FP16 wins" in failure for failure in failures))
        self.assertTrue(any("VRAM" in failure for failure in failures))


if __name__ == "__main__":
    unittest.main()
