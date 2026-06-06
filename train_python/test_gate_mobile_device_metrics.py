from __future__ import annotations

import argparse
import unittest

import gate_mobile_device_metrics as gate


def args(**overrides):
    values = {
        "required_model_tokens": "redmi,k80",
        "max_ttft_seconds": 30.0,
        "min_tokens_per_second": 0.1,
        "min_generated_tokens": 1,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def payload(**overrides):
    data = {
        "real_device_connected": True,
        "device_props": {
            "ro.product.manufacturer": "Xiaomi",
            "ro.product.model": "24122RKC7C",
            "ro.product.device": "miro",
            "ro.product.marketname": "REDMI K80 Pro",
        },
        "benchmark_metrics": {
            "ttft_seconds": 1.25,
            "tokens_per_second": 7.5,
            "peak_memory_mb": 2048,
            "generated_tokens": 64,
        },
    }
    data.update(overrides)
    return data


class GateMobileDeviceMetricsTests(unittest.TestCase):
    def test_passes_real_device_metrics_using_market_name_identity(self) -> None:
        result = gate.build_result(payload(), args())
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["ttft_seconds"], 1.25)

    def test_fails_without_real_device_flag(self) -> None:
        result = gate.build_result(payload(real_device_connected=False), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("real_device_connected" in failure for failure in result["failures"]))

    def test_fails_missing_peak_memory(self) -> None:
        bad = payload()
        bad["benchmark_metrics"] = dict(bad["benchmark_metrics"])
        bad["benchmark_metrics"].pop("peak_memory_mb")
        result = gate.build_result(bad, args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("peak memory" in failure for failure in result["failures"]))

    def test_accepts_common_metric_aliases(self) -> None:
        data = payload(
            benchmark_metrics={
                "time_to_first_token_seconds": 2.0,
                "tps": 5.0,
                "peak_pss_mb": 1024,
                "tokens": 8,
            }
        )
        result = gate.build_result(data, args())
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["generated_tokens"], 8.0)


if __name__ == "__main__":
    unittest.main()
