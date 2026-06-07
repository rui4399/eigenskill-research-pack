from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

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

    def test_mmlu_dataset_spec_accepts_new_subjects(self) -> None:
        self.assertEqual(smoke.mmlu_dataset_key("computer_security"), "mmlu_computer_security")
        spec = smoke.mmlu_dataset_spec("computer_security")
        self.assertEqual(spec["dataset"], "cais/mmlu")
        self.assertEqual(spec["config"], "computer_security")
        self.assertEqual(spec["task_format"], "mmlu")
        self.assertEqual(spec["file"], "mmlu_computer_security_test_smoke.jsonl")
        with self.assertRaises(ValueError):
            smoke.mmlu_dataset_key(" ")

    def test_build_suite_supports_multiple_mmlu_subjects(self) -> None:
        def fake_records(dataset, config, split, count, source="auto"):
            return [
                {
                    "question": f"{config}-{idx}",
                    "choices": ["A", "B", "C", "D"],
                    "answer": 0,
                    "subject": config,
                }
                for idx in range(count)
            ]

        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(smoke, "load_streamed_records", side_effect=fake_records):
                manifest = smoke.build_suite(
                    Path(tmp),
                    {"mmlu_abstract_algebra": 2, "mmlu_computer_security": 3},
                    file_tag="broad5",
                    mmlu_combined_file="mmlu_broad5.jsonl",
                    source="datasets-server",
                )

            combined_rows = [
                json.loads(line)
                for line in (Path(tmp) / "mmlu_broad5.jsonl").read_text(encoding="utf-8").splitlines()
            ]

        self.assertEqual(manifest["artifact_count"], 3)
        rows = {item["id"]: item["rows"] for item in manifest["artifacts"]}
        self.assertEqual(rows, {"mmlu_abstract_algebra": 2, "mmlu_computer_security": 3, "mmlu_combined": 5})
        self.assertEqual(len(combined_rows), 5)
        self.assertEqual({row["subject"] for row in combined_rows}, {"abstract_algebra", "computer_security"})

    def test_dataset_server_records_fetch_pages(self) -> None:
        calls = []

        def fake_page(dataset, config, split, offset, length):
            calls.append((dataset, config, split, offset, length))
            return [{"idx": i} for i in range(offset, offset + length)]

        with mock.patch.object(smoke, "load_dataset_server_page", side_effect=fake_page):
            rows = smoke.load_dataset_server_records("dataset", "config", "split", 205)

        self.assertEqual(len(rows), 205)
        self.assertEqual(rows[0], {"idx": 0})
        self.assertEqual(rows[-1], {"idx": 204})
        self.assertEqual(calls, [
            ("dataset", "config", "split", 0, 100),
            ("dataset", "config", "split", 100, 100),
            ("dataset", "config", "split", 200, 5),
        ])

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
