from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import build_public_ppl_prompts as builder


class BuildPublicPplPromptsTests(unittest.TestCase):
    def test_clean_text_rows_filters_empty_and_short_rows(self) -> None:
        rows = [
            {"text": ""},
            {"text": "short"},
            {"text": "This is a sufficiently long public text row for perplexity evaluation."},
        ]
        prompts = builder.clean_text_rows(rows, min_chars=20, max_chars=40)
        self.assertEqual(len(prompts), 1)
        self.assertLessEqual(len(prompts[0]), 40)
        self.assertTrue(prompts[0].startswith("This is a sufficiently"))

    def test_build_suite_writes_prompt_files_with_fake_loader(self) -> None:
        def fake_loader(dataset: str, config: str | None, split: str, count: int, offset: int) -> list[dict]:
            del dataset, config, split, offset
            return [
                {"text": f"This is public text row number {i} with enough content for PPL."}
                for i in range(count)
            ]

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest = builder.build_suite(
                out_dir=root,
                counts={"wikitext2": 2, "c4": 3},
                source="datasets-server",
                loader=fake_loader,
                min_chars=20,
                max_chars=80,
            )

            self.assertEqual(manifest["artifact_count"], 2)
            paths = [Path(item["path"]) for item in manifest["artifacts"]]
            self.assertTrue(all(path.exists() for path in paths))
            self.assertEqual(paths[0].read_text(encoding="utf-8").count("\n"), 2)
            self.assertEqual(paths[1].read_text(encoding="utf-8").count("\n"), 3)

    def test_build_suite_fetches_more_rows_when_source_contains_short_rows(self) -> None:
        calls: list[int] = []

        def fake_loader(dataset: str, config: str | None, split: str, count: int, offset: int) -> list[dict]:
            del dataset, config, split, count
            calls.append(offset)
            if offset == 0:
                return [{"text": ""}, {"text": "short"}]
            return [
                {"text": f"This later public text row {i} is long enough for PPL prompts."}
                for i in range(4)
            ]

        with tempfile.TemporaryDirectory() as tmp:
            manifest = builder.build_suite(
                out_dir=Path(tmp),
                counts={"wikitext2": 3, "c4": 0},
                source="datasets-server",
                loader=fake_loader,
                min_chars=20,
                max_chars=80,
            )

            self.assertEqual(manifest["artifacts"][0]["prompts"], 3)
            self.assertGreater(len(calls), 1)


if __name__ == "__main__":
    unittest.main()
