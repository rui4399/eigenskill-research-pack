from __future__ import annotations

import argparse
import unittest

import gate_w4a8_activation_reconstruction as gate


def args(**overrides):
    values = {
        "min_modules": 2,
        "max_activation_added_rel_l2": 0.02,
        "max_p90_w4a8_rel_l2": 0.25,
        "min_median_compression": 3.5,
        "max_memory_ratio": 0.90,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def result(**summary_overrides):
    summary = {
        "modules_ok": 2,
        "median_w4a8_rel_l2": 0.16,
        "p90_w4a8_rel_l2": 0.20,
        "max_w4a8_rel_l2": 0.22,
        "median_activation_added_rel_l2": 0.006,
        "max_activation_added_rel_l2": 0.012,
        "median_activation_input_rel_l2": 0.004,
        "median_compression_vs_fp32": 6.0,
    }
    summary.update(summary_overrides)
    return {"summary": summary, "peak_cuda_memory_ratio": 0.6}


class W4A8ActivationGateTests(unittest.TestCase):
    def test_passes_when_thresholds_hold(self) -> None:
        self.assertTrue(gate.build_gate(result(), args())["passed"])

    def test_fails_on_added_activation_drift(self) -> None:
        out = gate.build_gate(result(max_activation_added_rel_l2=0.04), args())
        self.assertFalse(out["passed"])
        self.assertTrue(any("activation-added" in item for item in out["failures"]))

    def test_fails_on_p90_total_drift(self) -> None:
        out = gate.build_gate(result(p90_w4a8_rel_l2=0.4), args())
        self.assertFalse(out["passed"])
        self.assertTrue(any("p90 W4A8" in item for item in out["failures"]))

    def test_fails_on_memory_ratio(self) -> None:
        payload = result()
        payload["peak_cuda_memory_ratio"] = 0.95
        out = gate.build_gate(payload, args())
        self.assertFalse(out["passed"])
        self.assertTrue(any("memory ratio" in item for item in out["failures"]))


if __name__ == "__main__":
    unittest.main()
