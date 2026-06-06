from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import summarize_system_metrics as metrics


class SummarizeSystemMetricsTests(unittest.TestCase):
    def test_adds_baseline_ratios_and_compression(self) -> None:
        rows = [
            metrics.metric_row(
                "base",
                Path("base.json"),
                {
                    "mode": "hf_same_loader",
                    "ttft_seconds": 1.0,
                    "tokens_per_second": 10.0,
                    "peak_gpu_memory_mib": 1000.0,
                },
            ),
            metrics.metric_row(
                "packed",
                Path("packed.json"),
                {
                    "mode": "cached",
                    "ttft_seconds": 0.5,
                    "tokens_per_second": 20.0,
                    "peak_gpu_memory_mib": 900.0,
                    "replaced_module_count": 3,
                    "selected_compression_vs_fp32": 6.25,
                },
            ),
        ]

        metrics.add_baseline_ratios(rows, "base")
        self.assertEqual(rows[1]["ttft_speedup_vs_baseline"], 2.0)
        self.assertEqual(rows[1]["tps_ratio_vs_baseline"], 2.0)
        self.assertEqual(rows[1]["memory_delta_mib_vs_baseline"], -100.0)
        self.assertEqual(rows[1]["replacement_compression_vs_fp32"], 6.25)

    def test_load_case_requires_label(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "case.json"
            path.write_text(json.dumps({"ttft_seconds": 1.0}), encoding="utf-8")
            label, loaded_path, data = metrics.load_case(f"demo={path}")
        self.assertEqual(label, "demo")
        self.assertEqual(loaded_path, path)
        self.assertEqual(data["ttft_seconds"], 1.0)


if __name__ == "__main__":
    unittest.main()
