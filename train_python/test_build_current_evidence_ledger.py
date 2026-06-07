from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import build_current_evidence_ledger as current


def write_gate(repo_root: Path, relative: str) -> None:
    path = repo_root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"passed": True, "summary": {"case_count": 1}, "failures": []}), encoding="utf-8")


class BuildCurrentEvidenceLedgerTests(unittest.TestCase):
    def test_current_manifest_has_expected_gate_count(self) -> None:
        self.assertEqual(len(current.CURRENT_GATE_SPECS), 45)

    def test_build_current_ledger_keeps_relative_sources(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            for _, raw_path in current.CURRENT_GATE_SPECS:
                write_gate(repo_root, raw_path)

            with mock.patch.object(current.ledger, "write_markdown", wraps=current.ledger.write_markdown) as write_md:
                result = current.build_current_ledger(repo_root, Path("ledger.json"), Path("ledger.md"))

            self.assertTrue(result["passed"])
            self.assertEqual(result["gate_count"], 45)
            self.assertEqual(
                result["entries"][0]["path"].replace("\\", "/"),
                current.CURRENT_GATE_SPECS[0][1],
            )
            self.assertFalse(Path(result["entries"][0]["path"]).is_absolute())
            write_md.assert_called_once()


if __name__ == "__main__":
    unittest.main()
