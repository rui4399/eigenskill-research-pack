from __future__ import annotations

import argparse
import unittest

import gate_official_awq_smoke as gate


def args(**overrides):
    values = {
        "max_memory_ratio": 0.90,
        "min_quantized_bytes": 1024,
        "require_package": "autoawq",
        "require_w_bit": 4,
        "require_q_group_size": 128,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def summary(**overrides):
    payload = {
        "passed": True,
        "model": "Qwen/Qwen2.5-0.5B-Instruct",
        "package": {"name": "autoawq", "version": "0.2.9"},
        "quant_config": {"w_bit": 4, "q_group_size": 128, "zero_point": True, "version": "GEMM"},
        "artifact": {"file_count": 3, "total_bytes": 2048, "path": "outputs/local_awq_model"},
        "generation_smoke": {"ok": True, "prompt": "hello", "text": "hello world"},
    }
    payload.update(overrides)
    return payload


def guard(**overrides):
    payload = {
        "returncode": 0,
        "killed_by_guard": False,
        "killed_by_timeout": False,
        "max_memory_used_ratio": 0.5,
    }
    payload.update(overrides)
    return payload


class GateOfficialAwqSmokeTests(unittest.TestCase):
    def test_passes_valid_awq_smoke(self) -> None:
        result = gate.build_result(summary(), guard(), args())
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["package"], "autoawq")

    def test_fails_when_summary_failed(self) -> None:
        result = gate.build_result(summary(passed=False), guard(), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("summary did not pass" in failure for failure in result["failures"]))

    def test_fails_when_guard_exceeds_limit(self) -> None:
        result = gate.build_result(summary(), guard(max_memory_used_ratio=0.95), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("VRAM" in failure for failure in result["failures"]))

    def test_fails_when_quant_config_mismatches(self) -> None:
        bad = summary(quant_config={"w_bit": 3, "q_group_size": 128})
        result = gate.build_result(bad, guard(), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("w_bit" in failure for failure in result["failures"]))

    def test_fails_when_artifact_is_too_small(self) -> None:
        bad = summary(artifact={"file_count": 1, "total_bytes": 32, "path": "x"})
        result = gate.build_result(bad, guard(), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("artifact bytes" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
