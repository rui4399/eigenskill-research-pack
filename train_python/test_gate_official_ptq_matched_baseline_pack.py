from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import gate_official_ptq_matched_baseline_pack as gate


def write_json(path: Path, payload: dict) -> Path:
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def ppl_payload(package: str, quant_key: str, ratio: float = 1.2) -> dict:
    return {
        "passed": True,
        "model": "m",
        "package": {"name": package, "version": "1"},
        "prompt_count": 2,
        "tokens": 10,
        "fp16": {"ppl": 10.0},
        quant_key: {"ppl": 10.0 * ratio},
        "comparison": {f"ppl_ratio_{quant_key}_vs_fp16": ratio},
        "failures": [],
    }


class OfficialPtqMatchedBaselinePackTests(unittest.TestCase):
    def test_parse_ppl_case(self) -> None:
        case = gate.parse_ppl_case("autoawq:wikitext2=foo.json")
        self.assertEqual(case.variant, "autoawq")
        self.assertEqual(case.label, "wikitext2")
        self.assertEqual(case.path, Path("foo.json"))

    def test_gate_passes_complete_pack(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ppl_cases = [
                gate.PplCase("autoawq", "wikitext2", write_json(root / "awq_w.json", ppl_payload("autoawq", "awq"))),
                gate.PplCase("autoawq", "c4", write_json(root / "awq_c.json", ppl_payload("autoawq", "awq", 1.1))),
                gate.PplCase("gptqmodel", "wikitext2", write_json(root / "gptq_w.json", ppl_payload("gptqmodel", "gptq", 1.3))),
                gate.PplCase("gptqmodel", "c4", write_json(root / "gptq_c.json", ppl_payload("gptqmodel", "gptq", 1.2))),
            ]
            task = write_json(
                root / "task.json",
                {
                    "passed": True,
                    "summary": {"total_tasks": 300},
                    "cases": [
                        {"variant": "autoawq", "task_format": "mmlu", "tasks": 50, "passes": 10, "guard_max_memory_used_ratio": 0.5},
                        {"variant": "autoawq", "task_format": "gsm8k", "tasks": 50, "passes": 0, "guard_max_memory_used_ratio": 0.5},
                        {"variant": "gptqmodel", "task_format": "mmlu", "tasks": 50, "passes": 10, "guard_max_memory_used_ratio": 0.5},
                        {"variant": "gptqmodel", "task_format": "gsm8k", "tasks": 50, "passes": 0, "guard_max_memory_used_ratio": 0.5},
                    ],
                    "comparisons": [
                        {"variant": "autoawq", "task_format": "mmlu", "baseline_accuracy": 0.2, "accuracy_drop_vs_baseline": 0.05},
                        {"variant": "autoawq", "task_format": "gsm8k", "baseline_accuracy": 0.0, "accuracy_drop_vs_baseline": 0.0},
                        {"variant": "gptqmodel", "task_format": "mmlu", "baseline_accuracy": 0.2, "accuracy_drop_vs_baseline": 0.0},
                        {"variant": "gptqmodel", "task_format": "gsm8k", "baseline_accuracy": 0.0, "accuracy_drop_vs_baseline": 0.0},
                    ],
                },
            )
            runtime = write_json(
                root / "runtime.json",
                {
                    "passed": True,
                    "summary": {"total_tasks": 300, "max_guard_vram_ratio": 0.6},
                    "profiles": {
                        "autoawq": {"total_tasks": 100, "mean_tokens_per_second": 5, "mean_ttft_seconds": 0.3, "max_guard_vram_ratio": 0.5},
                        "gptqmodel": {"total_tasks": 100, "mean_tokens_per_second": 10, "mean_ttft_seconds": 0.2, "max_guard_vram_ratio": 0.5},
                    },
                    "comparisons": [
                        {"variant": "autoawq", "tokens_per_second_ratio_vs_baseline": 0.2, "ttft_ratio_vs_baseline": 3, "vram_ratio_vs_baseline": 0.9},
                        {"variant": "gptqmodel", "tokens_per_second_ratio_vs_baseline": 0.3, "ttft_ratio_vs_baseline": 2, "vram_ratio_vs_baseline": 0.85},
                    ],
                },
            )
            report = gate.build_gate(
                ppl_cases,
                task_matrix_path=task,
                runtime_profile_path=runtime,
                required_variants=["autoawq", "gptqmodel"],
                required_ppl_labels=["wikitext2", "c4"],
            )
            self.assertTrue(report["passed"])
            self.assertEqual(report["summary"]["ppl_slice_count"], 4)
            self.assertAlmostEqual(report["summary"]["max_ppl_ratio_vs_fp16"], 1.3)

    def test_gate_fails_missing_label_or_high_ppl_ratio(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ppl_cases = [
                gate.PplCase("autoawq", "wikitext2", write_json(root / "awq_w.json", ppl_payload("autoawq", "awq", 2.0))),
            ]
            task = write_json(root / "task.json", {"passed": True, "summary": {"total_tasks": 300}, "cases": [], "comparisons": []})
            runtime = write_json(root / "runtime.json", {"passed": True, "summary": {"total_tasks": 300}, "profiles": {}, "comparisons": []})
            report = gate.build_gate(
                ppl_cases,
                task_matrix_path=task,
                runtime_profile_path=runtime,
                required_variants=["autoawq"],
                required_ppl_labels=["wikitext2", "c4"],
            )
            self.assertFalse(report["passed"])
            self.assertTrue(any("missing PPL labels" in failure for failure in report["failures"]))
            self.assertTrue(any("max PPL ratio" in failure for failure in report["failures"]))


if __name__ == "__main__":
    unittest.main()
