from __future__ import annotations

import argparse
import unittest

import gate_official_awq_matched_ppl as gate


def args(**overrides):
    values = {
        "max_memory_ratio": 0.90,
        "min_tokens": 16,
        "max_ppl_ratio": 20.0,
        "require_package": "autoawq",
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def summary(**overrides):
    payload = {
        "passed": True,
        "model": "Qwen/Qwen2.5-0.5B-Instruct",
        "package": {"name": "autoawq", "version": "0.2.9"},
        "prompt_count": 4,
        "tokens": 64,
        "fp16": {"ppl": 10.0, "mean_nll": 2.3},
        "awq": {"ppl": 12.0, "mean_nll": 2.48},
        "comparison": {"ppl_ratio_awq_vs_fp16": 1.2, "delta_nll_awq_minus_fp16": 0.18},
        "failures": [],
    }
    payload.update(overrides)
    return payload


def guard(**overrides):
    payload = {
        "returncode": 0,
        "killed_by_guard": False,
        "killed_by_timeout": False,
        "max_memory_used_ratio": 0.61,
    }
    payload.update(overrides)
    return payload


class GateOfficialAwqMatchedPplTests(unittest.TestCase):
    def test_passes_valid_matched_ppl(self) -> None:
        result = gate.build_result(summary(), guard(), args())
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["package"], "autoawq")

    def test_fails_when_guard_exceeds_limit(self) -> None:
        result = gate.build_result(summary(), guard(max_memory_used_ratio=0.95), args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("VRAM" in failure for failure in result["failures"]))

    def test_fails_when_ppl_ratio_too_large(self) -> None:
        bad = summary(comparison={"ppl_ratio_awq_vs_fp16": 99.0, "delta_nll_awq_minus_fp16": 4.6})
        result = gate.build_result(bad, guard(), args(max_ppl_ratio=20.0))
        self.assertFalse(result["passed"])
        self.assertTrue(any("ppl ratio" in failure for failure in result["failures"]))

    def test_fails_when_not_enough_tokens(self) -> None:
        result = gate.build_result(summary(tokens=4), guard(), args(min_tokens=16))
        self.assertFalse(result["passed"])
        self.assertTrue(any("tokens" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
