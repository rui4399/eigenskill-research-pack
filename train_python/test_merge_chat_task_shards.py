import json
import tempfile
import unittest
from pathlib import Path

import merge_chat_task_shards as merge


def summary(row_id: str, passed: bool, *, offset: int = 0) -> dict:
    row = {
        "id": row_id,
        "type": "number",
        "prompt": "p",
        "answer": "1",
        "generated_text": "1" if passed else "0",
        "score": {"passed": passed},
        "ttft_seconds": 0.1 + offset,
        "tokens_per_second": 10.0 + offset,
    }
    return {
        "model": "model",
        "loader": "hf",
        "hf_device_map": "",
        "hf_max_gpu_memory_mib": 0,
        "task_file": "tasks.jsonl",
        "task_format": "gsm8k",
        "task_count": 1,
        "task_limit": 1,
        "task_offset": offset,
        "chat_template": True,
        "no_think": True,
        "max_new_tokens": 64,
        "baseline": {"aggregate": {"tasks": 1, "passes": int(passed)}, "rows": [row]},
    }


class MergeChatTaskShardsTests(unittest.TestCase):
    def test_merge_summaries_recomputes_aggregate(self) -> None:
        merged = merge.merge_summaries([summary("a", True), summary("b", False, offset=1)], [Path("a"), Path("b")])
        self.assertEqual(merged["task_count"], 2)
        self.assertEqual(merged["shard_count"], 2)
        self.assertEqual(merged["baseline"]["aggregate"]["tasks"], 2)
        self.assertEqual(merged["baseline"]["aggregate"]["passes"], 1)
        self.assertAlmostEqual(merged["baseline"]["aggregate"]["accuracy"], 0.5)

    def test_merge_summaries_rejects_duplicate_ids(self) -> None:
        with self.assertRaises(ValueError):
            merge.merge_summaries([summary("a", True), summary("a", False, offset=1)], [Path("a"), Path("b")])

    def test_merge_guards_takes_max_memory_and_any_failure(self) -> None:
        guards = [
            {
                "returncode": 0,
                "killed_by_guard": False,
                "killed_by_timeout": False,
                "timeout_seconds": 10,
                "max_memory_used_mib": 100,
                "memory_total_mib": 1000,
                "max_memory_used_ratio": 0.1,
                "max_utilization_gpu_pct": 20,
                "post_cleanup": {"target_count": 1, "estimated_bytes": 2, "errors": []},
            },
            {
                "returncode": 0,
                "killed_by_guard": False,
                "killed_by_timeout": False,
                "timeout_seconds": 20,
                "max_memory_used_mib": 300,
                "memory_total_mib": 1000,
                "max_memory_used_ratio": 0.3,
                "max_utilization_gpu_pct": 30,
                "post_cleanup": {"target_count": 2, "estimated_bytes": 3, "errors": []},
            },
        ]
        merged = merge.merge_guards(guards, [Path("a"), Path("b")])
        self.assertEqual(merged["returncode"], 0)
        self.assertEqual(merged["max_memory_used_mib"], 300)
        self.assertEqual(merged["max_memory_used_ratio"], 0.3)
        self.assertEqual(merged["post_cleanup"]["target_count"], 3)

    def test_cli_writes_merged_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            s1 = root / "s1.json"
            s2 = root / "s2.json"
            g1 = root / "g1.json"
            g2 = root / "g2.json"
            s1.write_text(json.dumps(summary("a", True)), encoding="utf-8")
            s2.write_text(json.dumps(summary("b", False, offset=1)), encoding="utf-8")
            guard = {
                "returncode": 0,
                "killed_by_guard": False,
                "killed_by_timeout": False,
                "timeout_seconds": 10,
                "max_memory_used_mib": 100,
                "memory_total_mib": 1000,
                "max_memory_used_ratio": 0.1,
                "max_utilization_gpu_pct": 20,
                "post_cleanup": {"target_count": 0, "estimated_bytes": 0, "errors": []},
            }
            g1.write_text(json.dumps(guard), encoding="utf-8")
            g2.write_text(json.dumps(guard), encoding="utf-8")
            out_json = root / "merged.json"
            out_md = root / "merged.md"
            out_guard = root / "guard.json"
            old_argv = __import__("sys").argv
            try:
                __import__("sys").argv = [
                    "merge",
                    "--shard",
                    f"{s1}={g1}",
                    "--shard",
                    f"{s2}={g2}",
                    "--out-json",
                    str(out_json),
                    "--out-md",
                    str(out_md),
                    "--out-guard-json",
                    str(out_guard),
                ]
                merge.main()
            finally:
                __import__("sys").argv = old_argv
            self.assertEqual(json.loads(out_json.read_text(encoding="utf-8"))["task_count"], 2)
            self.assertTrue(out_md.exists())
            self.assertEqual(json.loads(out_guard.read_text(encoding="utf-8"))["merged_shard_count"], 2)


if __name__ == "__main__":
    unittest.main()
