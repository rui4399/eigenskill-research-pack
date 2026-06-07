from __future__ import annotations

import argparse
import unittest

import gate_official_gptqmodel_public_calib as gate


def args(**overrides):
    values = {
        "min_tokens": 128,
        "min_calibration_texts": 1,
        "max_memory_ratio": 0.85,
        "max_ppl_ratio": 5.0,
        "require_fresh_quantization": True,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def summary(**overrides):
    payload = {
        "passed": True,
        "model": "Qwen/Qwen2.5-0.5B-Instruct",
        "package": {"name": "gptqmodel", "version": "7.0.0"},
        "quant_config": {"bits": 4, "group_size": 128},
        "calibration_source": ["data_eval/public_calib/a.txt"],
        "calibration_count": 4,
        "prompt_count": 4,
        "tokens": 380,
        "artifact_reused": False,
        "artifact": {"file_count": 8, "total_bytes": 470821016},
        "fp16": {"ppl": 19.38, "mean_nll": 2.96},
        "gptq": {"ppl": 25.67, "mean_nll": 3.24},
        "comparison": {"ppl_ratio_gptq_vs_fp16": 1.33, "delta_nll_gptq_minus_fp16": 0.28},
    }
    payload.update(overrides)
    return payload


def guard(**overrides):
    payload = {
        "returncode": 0,
        "killed_by_guard": False,
        "killed_by_timeout": False,
        "max_memory_used_ratio": 0.62,
    }
    payload.update(overrides)
    return payload


class GateOfficialGptqModelPublicCalibTests(unittest.TestCase):
    def test_passes_public_calibration_smoke(self) -> None:
        result = gate.build_result(summary=summary(), guard=guard(), args=args())

        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["tokens"], 380)
        self.assertEqual(result["summary"]["package"], "gptqmodel")

    def test_fails_when_formal_run_reuses_artifact(self) -> None:
        result = gate.build_result(summary=summary(artifact_reused=True), guard=guard(), args=args())

        self.assertFalse(result["passed"])
        self.assertTrue(any("reused" in failure for failure in result["failures"]))

    def test_fails_when_guard_exceeds_memory_budget(self) -> None:
        result = gate.build_result(summary=summary(), guard=guard(max_memory_used_ratio=0.91), args=args())

        self.assertFalse(result["passed"])
        self.assertTrue(any("VRAM ratio" in failure for failure in result["failures"]))

    def test_fails_when_ppl_ratio_exceeds_limit(self) -> None:
        result = gate.build_result(
            summary=summary(comparison={"ppl_ratio_gptq_vs_fp16": 9.0}),
            guard=guard(),
            args=args(max_ppl_ratio=2.0),
        )

        self.assertFalse(result["passed"])
        self.assertTrue(any("ppl ratio" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
