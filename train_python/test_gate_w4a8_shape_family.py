from __future__ import annotations

import argparse
import unittest

import gate_w4a8_shape_family as gate


def args(**overrides):
    values = {
        "min_configs": 2,
        "min_packed_speedup": 1.0,
        "min_packed_vs_w4a16_speedup": 1.0,
        "min_compression": 3.5,
        "max_added_rel_l2": 0.02,
        "max_memory_ratio": 0.90,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def row(speed: float = 1.2, drift: float = 0.01, memory: float = 0.6) -> dict:
    return {
        "returncode": 0,
        "guard_killed": False,
        "int4_packed_x_i8_speedup_vs_torch_fp16": speed,
        "int4_unpacked_i8_x_i8_speedup_vs_torch_fp16": speed + 0.5,
        "int4_packed_x_i8_speedup_vs_packed_w4a16": 1.3,
        "compression_ratio_vs_fp16": 3.98,
        "int4_packed_x_i8_vs_w4a16_rel_l2": drift,
        "guard_max_memory_used_ratio": memory,
    }


class W4A8ShapeFamilyGateTests(unittest.TestCase):
    def test_passes_when_all_thresholds_hold(self) -> None:
        result = gate.build_result([row(1.2), row(1.4)], args())
        self.assertTrue(result["passed"])
        self.assertTrue(result["summary"]["all_packed_configs_beat_fp16"])

    def test_fails_when_any_packed_config_loses_to_fp16(self) -> None:
        result = gate.build_result([row(1.2), row(0.95)], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("min packed" in failure for failure in result["failures"]))

    def test_fails_when_activation_drift_exceeds_threshold(self) -> None:
        result = gate.build_result([row(1.2), row(1.3, drift=0.03)], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("rel-L2" in failure for failure in result["failures"]))

    def test_fails_when_guard_memory_exceeds_threshold(self) -> None:
        result = gate.build_result([row(1.2), row(1.3, memory=0.95)], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("guard memory" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
