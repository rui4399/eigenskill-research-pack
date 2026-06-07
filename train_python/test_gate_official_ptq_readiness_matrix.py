from __future__ import annotations

import argparse
import tempfile
import unittest
from pathlib import Path

import gate_official_ptq_readiness_matrix as gate


def args(**overrides):
    values = {
        "required_packages": ["autoawq", "gptqmodel"],
        "required_labels": ["wikitext2", "c4"],
        "min_packages": 2,
        "min_eval_slices": 2,
        "min_total_tokens": 512,
        "max_ppl_ratio": 2.0,
        "max_memory_ratio": 0.90,
        "require_same_model": True,
        "require_same_quant_shape": True,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def awq_gate(**overrides):
    payload = {
        "passed": True,
        "summary": {
            "model": "Qwen/Qwen2.5-0.5B-Instruct",
            "package": "autoawq",
            "package_version": "0.2.9",
            "quant_config": {"w_bit": 4, "q_group_size": 128, "version": "GEMM"},
            "calibration_source": ["wiki.txt", "c4.txt"],
            "artifact_file_count": 6,
            "artifact_total_bytes": 469809733,
            "eval_slice_count": 2,
            "total_eval_tokens": 1487,
            "evals": [
                {
                    "label": "wikitext2",
                    "prompt_count": 8,
                    "tokens": 760,
                    "fp16_ppl": 24.67,
                    "awq_ppl": 29.08,
                    "ppl_ratio_awq_vs_fp16": 1.18,
                    "guard_max_memory_used_ratio": 0.61,
                },
                {
                    "label": "c4",
                    "prompt_count": 8,
                    "tokens": 727,
                    "fp16_ppl": 32.95,
                    "awq_ppl": 38.17,
                    "ppl_ratio_awq_vs_fp16": 1.16,
                    "guard_max_memory_used_ratio": 0.61,
                },
            ],
        },
        "failures": [],
    }
    payload.update(overrides)
    return payload


def gptq_gate(**overrides):
    payload = {
        "passed": True,
        "summary": {
            "model": "Qwen/Qwen2.5-0.5B-Instruct",
            "package": "gptqmodel",
            "package_version": "7.0.0",
            "quant_config": {"bits": 4, "group_size": 128},
            "calibration_source": ["wiki.txt", "c4.txt"],
            "artifact_file_count": 8,
            "artifact_total_bytes": 470821016,
            "eval_slice_count": 2,
            "total_eval_tokens": 760,
            "evals": [
                {
                    "label": "wikitext2",
                    "prompt_count": 4,
                    "tokens": 380,
                    "fp16_ppl": 19.38,
                    "gptq_ppl": 25.67,
                    "ppl_ratio_gptq_vs_fp16": 1.32,
                    "guard_max_memory_used_ratio": 0.62,
                },
                {
                    "label": "c4",
                    "prompt_count": 4,
                    "tokens": 380,
                    "fp16_ppl": 24.66,
                    "gptq_ppl": 31.39,
                    "ppl_ratio_gptq_vs_fp16": 1.27,
                    "guard_max_memory_used_ratio": 0.63,
                },
            ],
        },
        "failures": [],
    }
    payload.update(overrides)
    return payload


class GateOfficialPtqReadinessMatrixTests(unittest.TestCase):
    def test_passes_aligned_awq_and_gptqmodel_public_slices(self) -> None:
        result = gate.build_result(cases=[("awq", awq_gate()), ("gptqmodel", gptq_gate())], args=args())

        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["package_count"], 2)
        self.assertEqual(result["summary"]["models"], ["Qwen/Qwen2.5-0.5B-Instruct"])
        self.assertEqual(result["summary"]["quant_shapes"], [{"bits": 4, "group_size": 128}])
        self.assertEqual(result["summary"]["common_eval_labels"], ["c4", "wikitext2"])

    def test_fails_when_required_package_is_missing(self) -> None:
        result = gate.build_result(cases=[("awq", awq_gate())], args=args())

        self.assertFalse(result["passed"])
        self.assertTrue(any("missing required package" in failure for failure in result["failures"]))

    def test_fails_when_quant_shapes_do_not_match(self) -> None:
        bad_gptq = gptq_gate()
        bad_gptq["summary"]["quant_config"] = {"bits": 3, "group_size": 128}

        result = gate.build_result(cases=[("awq", awq_gate()), ("gptqmodel", bad_gptq)], args=args())

        self.assertFalse(result["passed"])
        self.assertTrue(any("quant shapes are not aligned" in failure for failure in result["failures"]))

    def test_fails_when_a_required_eval_label_is_missing(self) -> None:
        bad_awq = awq_gate()
        bad_awq["summary"]["evals"] = [bad_awq["summary"]["evals"][0]]

        result = gate.build_result(cases=[("awq", bad_awq), ("gptqmodel", gptq_gate())], args=args())

        self.assertFalse(result["passed"])
        self.assertTrue(any("missing required eval label c4" in failure for failure in result["failures"]))

    def test_write_markdown_renders_package_matrix(self) -> None:
        result = gate.build_result(cases=[("awq", awq_gate()), ("gptqmodel", gptq_gate())], args=args())

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "matrix.md"
            gate.write_markdown(out, result)
            text = out.read_text(encoding="utf-8")

        self.assertIn("# Official PTQ Readiness Matrix", text)
        self.assertIn("| `autoawq` | `wikitext2` |", text)
        self.assertIn("| `gptqmodel` | `c4` |", text)


if __name__ == "__main__":
    unittest.main()
