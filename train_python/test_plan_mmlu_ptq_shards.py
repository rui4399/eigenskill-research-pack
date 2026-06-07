from __future__ import annotations

import argparse
import tempfile
import unittest
from pathlib import Path

import plan_mmlu_ptq_shards as plan


def args_for_test(**overrides):
    values = {
        "suite": "broad20x20",
        "preset": "broad20",
        "mmlu_subject": [],
        "rows_per_subject": 20,
        "total_rows": 0,
        "shard_size": 100,
        "date_tag": "2026_06_08",
        "source": "datasets-server",
        "claim_boundary": "test boundary",
        "max_memory_ratio": 0.90,
        "max_start_memory_ratio": 0.85,
        "min_disk_free_gb": 20,
        "disk_check_path": "/home/rui",
        "timeout_sec": 1800,
        "max_new_tokens": 64,
        "max_accuracy_drop": 0.15,
        "max_ci_accuracy_drop": 0.15,
        "bootstrap_samples": 4000,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class PlanMmluPtqShardsTests(unittest.TestCase):
    def test_select_subject_presets(self) -> None:
        self.assertEqual(len(plan.select_subjects("broad10", [])), 10)
        self.assertEqual(len(plan.select_subjects("broad20", [])), 20)
        self.assertEqual(len(plan.select_subjects("full", [])), len(plan.MMLU_SUBJECTS))
        self.assertEqual(plan.select_subjects("full", ["anatomy", "anatomy"]), ("anatomy",))
        with self.assertRaises(ValueError):
            plan.select_subjects("full", ["not_a_subject"])

    def test_shard_ranges_cover_total(self) -> None:
        self.assertEqual(plan.shard_ranges(250, 100), [(0, 100), (100, 100), (200, 50)])
        with self.assertRaises(ValueError):
            plan.shard_ranges(0, 100)
        with self.assertRaises(ValueError):
            plan.shard_ranges(100, 0)

    def test_build_plan_contains_variant_and_gate_commands(self) -> None:
        result = plan.build_plan(args_for_test())
        self.assertEqual(result["suite"], "broad20x20")
        self.assertEqual(len(result["subjects"]), 20)
        self.assertEqual(result["total_rows_planned"], 400)
        self.assertEqual(len(result["variants"]), 3)
        self.assertEqual(len(result["variants"][0]["shards"]), 4)
        self.assertIn("build_public_task_smoke.py", result["fixture_command"])
        self.assertIn("--mmlu-subject abstract_algebra", result["fixture_command"])
        self.assertIn("Qwen/Qwen2.5-1.5B-Instruct", result["variants"][0]["shards"][0]["command"])
        self.assertIn("/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07", result["variants"][1]["shards"][0]["command"])
        self.assertIn("gate_official_ptq_task_retention.py", result["gate_commands"]["task_retention"])
        self.assertIn("gate_official_ptq_runtime_profile.py", result["gate_commands"]["runtime_profile"])
        self.assertIn("gate_official_ptq_task_statistics.py", result["gate_commands"]["task_statistics"])

    def test_write_markdown_lists_commands(self) -> None:
        result = plan.build_plan(args_for_test(total_rows=40, shard_size=20, mmlu_subject=["anatomy"], rows_per_subject=40))
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "plan.md"
            plan.write_markdown(path, result)
            text = path.read_text(encoding="utf-8")
        self.assertIn("MMLU PTQ Shard Plan", text)
        self.assertIn("Fixture Command", text)
        self.assertIn("Gate Commands", text)
        self.assertIn("autoawq", text)


if __name__ == "__main__":
    unittest.main()
