from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_mmlu_ptq_shards as runner


class RunMmluPtqShardsTest(unittest.TestCase):
    def test_selects_offset_range_and_variants(self) -> None:
        plan = {
            "variants": [
                {
                    "variant": "fp16",
                    "shards": [
                        {
                            "offset": 0,
                            "limit": 500,
                            "command": "echo fp16-0",
                            "summary_json": "fp16_0.json",
                            "guard_json": "fp16_0_guard.json",
                        },
                        {
                            "offset": 12000,
                            "limit": 500,
                            "command": "echo fp16-12000",
                            "summary_json": "fp16_12000.json",
                            "guard_json": "fp16_12000_guard.json",
                        },
                    ],
                },
                {
                    "variant": "autoawq",
                    "shards": [
                        {
                            "offset": 12000,
                            "limit": 500,
                            "command": "echo autoawq-12000",
                            "summary_json": "autoawq_12000.json",
                            "guard_json": "autoawq_12000_guard.json",
                        }
                    ],
                },
            ]
        }
        shards = runner.select_shards(
            runner.iter_shards(plan),
            min_offset=12000,
            max_offset=12500,
            variants={"autoawq"},
        )
        self.assertEqual([shard.label for shard in shards], ["autoawq_12000_12500"])

    def test_skip_existing_summary_and_guard(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            summary = root / "summary.json"
            guard = root / "guard.json"
            summary.write_text("{}", encoding="utf-8")
            guard.write_text("{}", encoding="utf-8")
            shard = runner.ShardCommand(
                variant="fp16",
                offset=0,
                limit=1,
                command="this-command-should-not-run",
                summary_json=summary,
                guard_json=guard,
            )
            rc = runner.run_shards([shard], log_dir=root / "logs", dry_run=False)
            self.assertEqual(rc, 0)
            self.assertFalse((root / "logs" / "fp16_0_1.log").exists())


if __name__ == "__main__":
    unittest.main()
