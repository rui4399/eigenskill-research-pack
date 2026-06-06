from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import build_public_task_smoke as smoke


class BuildPublicTaskSmokeTests(unittest.TestCase):
    def test_take_records_is_bounded(self) -> None:
        rows = ({"x": i} for i in range(10))
        self.assertEqual(smoke.take_records(rows, 3), [{"x": 0}, {"x": 1}, {"x": 2}])
        with self.assertRaises(ValueError):
            smoke.take_records([], -1)

    def test_write_jsonl_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "rows.jsonl"
            smoke.write_jsonl(path, [{"question": "q", "answer": "a"}])
            rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
            self.assertEqual(rows, [{"question": "q", "answer": "a"}])

    def test_artifact_file_retags_smoke_name(self) -> None:
        self.assertEqual(smoke.artifact_file("gsm8k_test_smoke.jsonl", "smoke"), "gsm8k_test_smoke.jsonl")
        self.assertEqual(smoke.artifact_file("gsm8k_test_smoke.jsonl", "subset100"), "gsm8k_test_subset100.jsonl")

    def test_write_markdown_lists_artifacts(self) -> None:
        manifest = {
            "date": "2026-06-06T00:00:00+00:00",
            "artifact_count": 1,
            "claim_boundary": "Tiny public benchmark smoke fixtures; not leaderboard-scale evaluation.",
            "artifacts": [
                {
                    "id": "gsm8k",
                    "dataset": "openai/gsm8k",
                    "config": "main",
                    "split": "test",
                    "task_format": "gsm8k",
                    "rows": 2,
                    "path": "data_eval/public_task_smoke_v1/gsm8k_test_smoke.jsonl",
                }
            ],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "manifest.md"
            smoke.write_markdown(path, manifest)
            text = path.read_text(encoding="utf-8")
            self.assertIn("Public Task Smoke Manifest", text)
            self.assertIn("openai/gsm8k", text)


if __name__ == "__main__":
    unittest.main()
