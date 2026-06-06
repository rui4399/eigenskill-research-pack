from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import gate_public_repo_hygiene as hygiene


class PublicRepoHygieneTests(unittest.TestCase):
    def test_flags_generated_delivery_files(self) -> None:
        files = [
            "README.md",
            "outputs/paper_delivery_2026-06-04/report.md",
            "research_pack_2026-06-03/old.md",
            "docs/obsidian_quant_route/00-index.md",
            "paper.docx",
        ]
        bad = hygiene.find_forbidden_files(files)
        self.assertEqual(len(bad), 4)

    def test_flags_blank_placeholders(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            readme = root / "README.md"
            readme.write_text("# x\nBase model:\nUseful commands:\n", encoding="utf-8")
            findings = hygiene.find_placeholders(root, ["README.md"])
            self.assertEqual(len(findings), 2)
            self.assertEqual(findings[0]["line"], 2)

    def test_scans_nested_readmes_and_stale_v2_claims(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            nested = root / "train_python"
            nested.mkdir()
            readme = nested / "README.md"
            readme.write_text("# x\nThe current strongest package is v2:\n", encoding="utf-8")
            findings = hygiene.find_placeholders(root, ["train_python/README.md"])
            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0]["path"], "train_python/README.md")

    def test_clean_report_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            readme = root / "README.md"
            readme.write_text("# Clean\n\nNo placeholder rows.\n", encoding="utf-8")
            report = hygiene.build_report(root, ["README.md", "train_python/foo.py"])
            self.assertTrue(report["passed"])
            self.assertEqual(report["summary"]["forbidden_file_count"], 0)


if __name__ == "__main__":
    unittest.main()
