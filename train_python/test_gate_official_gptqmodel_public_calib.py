from __future__ import annotations

import argparse
import json
import tempfile
import unittest
from pathlib import Path

import gate_official_gptqmodel_public_calib as gate


def args(**overrides):
    values = {
        "min_tokens": 128,
        "min_calibration_texts": 1,
        "max_memory_ratio": 0.85,
        "max_ppl_ratio": 5.0,
        "require_fresh_quantization": True,
        "min_eval_slices": 1,
        "min_total_tokens": 128,
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

    def test_passes_two_eval_slices_with_one_fresh_quantization(self) -> None:
        c4_summary = summary(
            prompt_count=4,
            tokens=360,
            artifact_reused=True,
            fp16={"ppl": 31.0, "mean_nll": 3.43},
            gptq={"ppl": 40.0, "mean_nll": 3.69},
            comparison={"ppl_ratio_gptq_vs_fp16": 1.29, "delta_nll_gptq_minus_fp16": 0.26},
        )

        result = gate.build_result(
            summary=summary(),
            guard=guard(),
            evals=[("wikitext2", summary(), guard()), ("c4", c4_summary, guard(max_memory_used_ratio=0.54))],
            args=args(min_eval_slices=2, min_total_tokens=700),
        )

        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["eval_slice_count"], 2)
        self.assertEqual(result["summary"]["total_eval_tokens"], 740)

    def test_loads_labeled_eval_pairs_from_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            wiki_summary = root / "wiki_summary.json"
            wiki_guard = root / "wiki_guard.json"
            c4_summary = root / "c4_summary.json"
            c4_guard = root / "c4_guard.json"
            wiki_summary.write_text(json.dumps(summary(tokens=380)), encoding="utf-8")
            wiki_guard.write_text(json.dumps(guard(max_memory_used_ratio=0.62)), encoding="utf-8")
            c4_summary.write_text(json.dumps(summary(tokens=360, artifact_reused=True)), encoding="utf-8")
            c4_guard.write_text(json.dumps(guard(max_memory_used_ratio=0.54)), encoding="utf-8")

            evals = gate.load_eval_pairs(
                summaries=[("wikitext2", wiki_summary), ("c4", c4_summary)],
                guards=[("wikitext2", wiki_guard), ("c4", c4_guard)],
            )

        self.assertEqual([label for label, _, _ in evals], ["wikitext2", "c4"])
        self.assertEqual(evals[1][1]["tokens"], 360)
        self.assertEqual(evals[1][2]["max_memory_used_ratio"], 0.54)

    def test_write_markdown_renders_eval_slice_table(self) -> None:
        result = gate.build_result(
            summary=summary(),
            guard=guard(),
            evals=[("wikitext2", summary(), guard()), ("c4", summary(tokens=360, artifact_reused=True), guard())],
            args=args(min_eval_slices=2, min_total_tokens=700),
        )

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "gate.md"
            gate.write_markdown(out, result)
            text = out.read_text(encoding="utf-8")

        self.assertIn("## Evaluation Slices", text)
        self.assertIn("| `wikitext2` |", text)
        self.assertIn("| `c4` |", text)

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
