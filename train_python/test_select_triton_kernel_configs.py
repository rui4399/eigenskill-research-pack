from __future__ import annotations

import unittest
from pathlib import Path

import select_triton_kernel_configs as selector


def row(rows: int, cols: int, batch: int, speedup: float, block_m: int, rel_l2: float = 0.10) -> dict:
    return {
        "returncode": 0,
        "rows": rows,
        "cols": cols,
        "batch": batch,
        "high_every": 16,
        "block_m": block_m,
        "block_n": 16,
        "block_k": 64,
        "grouped_mixed_ms": 1.0,
        "torch_fp16_ms": speedup,
        "rowwise_mixed_ms": 2.0,
        "grouped_speedup_vs_torch_fp16": speedup,
        "grouped_speedup_vs_rowwise": 2.0,
        "grouped_rel_l2": rel_l2,
        "guard_max_memory_used_ratio": 0.40,
        "compression_ratio_vs_fp16": 3.7,
    }


class SelectTritonKernelConfigsTests(unittest.TestCase):
    def test_selects_best_config_per_group(self) -> None:
        selected = selector.select_configs(
            [
                row(1024, 1024, 8, 0.9, 16),
                row(1024, 1024, 8, 1.4, 32),
                row(2048, 1024, 16, 0.8, 16),
            ],
            max_rel_l2=0.20,
            max_vram_ratio=0.90,
        )
        self.assertEqual(len(selected), 2)
        self.assertEqual(selected[0]["status"], "fp16_win")
        self.assertEqual(selected[0]["selected"]["block_m"], 32)
        self.assertEqual(selected[1]["status"], "fallback_best_available")

    def test_result_gate_counts_groups(self) -> None:
        selected = selector.select_configs(
            [row(1024, 1024, 8, 1.2, 16), row(2048, 1024, 16, 0.8, 16)],
            max_rel_l2=0.20,
            max_vram_ratio=0.90,
        )
        result = selector.build_result(
            [Path("a.jsonl")],
            selected,
            {
                "max_rel_l2": 0.20,
                "max_vram_ratio": 0.90,
                "min_valid_groups": 2,
                "min_fp16_winning_groups": 1,
                "min_best_fp16_speedup": 1.05,
            },
        )
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["total_groups"], 2)
        self.assertEqual(result["summary"]["fp16_winning_groups"], 1)


if __name__ == "__main__":
    unittest.main()
