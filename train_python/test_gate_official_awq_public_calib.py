from __future__ import annotations

import argparse
import unittest

import gate_official_awq_public_calib as gate


def args(**overrides):
    values = {
        "min_eval_slices": 2,
        "min_total_tokens": 256,
        "min_awq_blocks": 1,
        "max_memory_ratio": 0.90,
        "max_ppl_ratio": 5.0,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def smoke_summary(**overrides):
    payload = {
        "passed": True,
        "model": "Qwen/Qwen2.5-0.5B-Instruct",
        "package": {"name": "autoawq", "version": "0.2.9"},
        "quant_config": {"w_bit": 4, "q_group_size": 128, "version": "GEMM"},
        "calibration": {
            "source": ["data_eval/public_calib/a.txt", "data_eval/public_calib/b.txt"],
            "sample_count": 12,
            "plan": {"ok": True, "expected_awq_blocks": 8},
        },
        "artifact": {"file_count": 6, "total_bytes": 469809733},
    }
    payload.update(overrides)
    return payload


def eval_summary(label: str = "wikitext2", **overrides):
    payload = {
        "passed": True,
        "model": "Qwen/Qwen2.5-0.5B-Instruct",
        "prompt_source": f"data_eval/public_ppl/{label}.txt",
        "prompt_count": 8,
        "tokens": 512,
        "fp16": {"ppl": 20.0},
        "awq": {"ppl": 24.0},
        "comparison": {"ppl_ratio_awq_vs_fp16": 1.2, "delta_nll_awq_minus_fp16": 0.18},
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


class GateOfficialAwqPublicCalibTests(unittest.TestCase):
    def test_passes_two_public_eval_slices(self) -> None:
        result = gate.build_result(
            smoke=smoke_summary(),
            smoke_guard=guard(max_memory_used_ratio=0.70),
            evals=[("wikitext2", eval_summary("wikitext2"), guard()), ("c4", eval_summary("c4"), guard())],
            args=args(),
        )

        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["eval_slice_count"], 2)
        self.assertEqual(result["summary"]["total_eval_tokens"], 1024)

    def test_fails_without_public_calibration_sources(self) -> None:
        bad_smoke = smoke_summary(calibration={"source": "default", "sample_count": 4, "plan": {"ok": True, "expected_awq_blocks": 1}})
        result = gate.build_result(
            smoke=bad_smoke,
            smoke_guard=guard(),
            evals=[("wikitext2", eval_summary("wikitext2"), guard()), ("c4", eval_summary("c4"), guard())],
            args=args(),
        )

        self.assertFalse(result["passed"])
        self.assertTrue(any("calibration source" in failure for failure in result["failures"]))

    def test_fails_when_eval_ppl_ratio_exceeds_limit(self) -> None:
        result = gate.build_result(
            smoke=smoke_summary(),
            smoke_guard=guard(),
            evals=[
                ("wikitext2", eval_summary("wikitext2", comparison={"ppl_ratio_awq_vs_fp16": 9.0}), guard()),
                ("c4", eval_summary("c4"), guard()),
            ],
            args=args(max_ppl_ratio=5.0),
        )

        self.assertFalse(result["passed"])
        self.assertTrue(any("ppl ratio" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
