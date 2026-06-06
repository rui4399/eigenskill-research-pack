from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import triton_config_selector as selector


def selected(rows: int, cols: int, batch: int, block_m: int, speedup: float, status: str = "fp16_win") -> dict:
    return {
        "rows": rows,
        "cols": cols,
        "batch": batch,
        "high_every": 16,
        "status": status,
        "selected": {
            "rows": rows,
            "cols": cols,
            "batch": batch,
            "high_every": 16,
            "block_m": block_m,
            "block_n": 16,
            "block_k": 128,
            "grouped_speedup_vs_torch_fp16": speedup,
            "grouped_speedup_vs_rowwise": 2.0,
            "grouped_rel_l2": 0.12,
        },
    }


class TritonConfigSelectorTests(unittest.TestCase):
    def test_loads_selector_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "selector.json"
            path.write_text(json.dumps({"selected_configs": [selected(1024, 1024, 8, 32, 1.5)]}), encoding="utf-8")
            configs = selector.load_kernel_configs(path)
        self.assertEqual(len(configs), 1)
        self.assertEqual(configs[0].block_m, 32)
        self.assertEqual(configs[0].speedup_vs_fp16, 1.5)

    def test_chooses_nearest_batch_for_exact_shape(self) -> None:
        configs = [
            selector.TritonKernelConfig(1024, 1024, 8, 16, 32, 16, 64, "fp16_win", 1.1, 1.2, 0.1, "fixture"),
            selector.TritonKernelConfig(1024, 1024, 16, 16, 16, 16, 128, "fp16_win", 1.9, 1.3, 0.1, "fixture"),
            selector.TritonKernelConfig(2048, 1024, 8, 16, 8, 16, 64, "fp16_win", 2.5, 1.3, 0.1, "fixture"),
        ]
        chosen = selector.choose_kernel_config(configs, rows=1024, cols=1024, batch=13, high_every=16)
        self.assertIsNotNone(chosen)
        self.assertEqual(chosen.block_k, 128)

    def test_prefers_matching_high_every_when_available(self) -> None:
        configs = [
            selector.TritonKernelConfig(1024, 1024, 8, 8, 8, 16, 64, "fp16_win", 3.0, 1.0, 0.1, "fixture"),
            selector.TritonKernelConfig(1024, 1024, 8, 16, 32, 16, 128, "fp16_win", 1.2, 1.0, 0.1, "fixture"),
        ]
        chosen = selector.choose_kernel_config(configs, rows=1024, cols=1024, batch=8, high_every=16)
        self.assertIsNotNone(chosen)
        self.assertEqual(chosen.block_m, 32)

    def test_estimates_periodic_high_every(self) -> None:
        self.assertEqual(selector.estimate_periodic_high_every([8, 4, 4, 4, 8, 4, 4, 4, 8]), 4)
        self.assertIsNone(selector.estimate_periodic_high_every([4, 8, 4, 4, 8, 4, 8]))


if __name__ == "__main__":
    unittest.main()
