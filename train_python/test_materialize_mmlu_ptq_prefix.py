from __future__ import annotations

import unittest

import materialize_mmlu_ptq_prefix as materialize


def fake_plan() -> dict:
    variants = []
    for variant in ("fp16", "autoawq", "gptqmodel"):
        variants.append(
            {
                "variant": variant,
                "shards": [
                    {
                        "offset": 0,
                        "limit": 500,
                        "summary_json": f"outputs/shards/{variant}_0_500.json",
                        "guard_json": f"outputs/shards/{variant}_0_500_guard.json",
                    },
                    {
                        "offset": 500,
                        "limit": 500,
                        "summary_json": f"outputs/shards/{variant}_500_1000.json",
                        "guard_json": f"outputs/shards/{variant}_500_1000_guard.json",
                    },
                ],
            }
        )
    return {"variants": variants}


class MaterializeMmluPtqPrefixTests(unittest.TestCase):
    def test_build_prefix_plan_writes_expected_commands(self) -> None:
        result = materialize.build_prefix_plan(fake_plan(), 1000, date_tag="2026_06_08")

        self.assertEqual(len(result.commands), 6)
        self.assertIn("PREFIX1000", str(result.matrix_md))
        self.assertEqual(
            result.variant_paths["fp16"].summary_json,
            materialize.Path("outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_prefix1000_2026_06_08.json"),
        )

        merge_command = result.commands[0]
        self.assertEqual(merge_command[:2], ["python", "train_python/merge_chat_task_shards.py"])
        self.assertIn("outputs/shards/fp16_0_500.json=outputs/shards/fp16_0_500_guard.json", merge_command)
        self.assertIn("outputs/shards/fp16_500_1000.json=outputs/shards/fp16_500_1000_guard.json", merge_command)

        retention_command = result.commands[3]
        self.assertIn("train_python/gate_official_ptq_task_retention.py", retention_command)
        self.assertIn("--required-variant", retention_command)
        self.assertIn("autoawq:mmlu=", " ".join(retention_command))

        statistics_command = result.commands[-1]
        self.assertIn("train_python/gate_official_ptq_task_statistics.py", statistics_command)
        self.assertIn("--bootstrap-samples", statistics_command)

    def test_prefix_must_match_shard_boundary(self) -> None:
        with self.assertRaises(ValueError):
            materialize.build_prefix_plan(fake_plan(), 750)

    def test_missing_variant_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            materialize.build_prefix_plan({"variants": []}, 1000)


if __name__ == "__main__":
    unittest.main()
