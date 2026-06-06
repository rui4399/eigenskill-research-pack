from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import build_evidence_ledger as ledger


def write_gate(path: Path, passed: bool = True, summary: dict | None = None, failures: list[str] | None = None) -> Path:
    path.write_text(
        json.dumps(
            {
                "passed": passed,
                "summary": summary or {"valid_configs": 4, "total_configs": 4, "best_fp16_speedup": 1.5},
                "failures": failures or [],
            }
        ),
        encoding="utf-8",
    )
    return path


class BuildEvidenceLedgerTests(unittest.TestCase):
    def test_builds_passing_ledger_and_metrics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            gate_path = write_gate(root / "triton_gate.json")
            result = ledger.build_ledger([("triton_shape_family", gate_path)])
            self.assertTrue(result["passed"])
            self.assertEqual(result["gate_count"], 1)
            self.assertIn("configs 4/4", result["entries"][0]["metrics"])
            self.assertEqual(result["entries"][0]["category"], "kernel")

    def test_failed_gate_fails_ledger(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            good = write_gate(root / "good.json")
            bad = write_gate(root / "bad.json", passed=False, failures=["boom"])
            result = ledger.build_ledger([("cpp_runtime", good), ("chat_task", bad)])
            self.assertFalse(result["passed"])
            self.assertEqual(result["failed_count"], 1)
            self.assertEqual(result["failures"][0]["failures"], ["boom"])

    def test_parse_gate_spec_requires_label(self) -> None:
        label, path = ledger.parse_gate_spec("foo=bar.json")
        self.assertEqual(label, "foo")
        self.assertEqual(path, Path("bar.json"))
        with self.assertRaises(ValueError):
            ledger.parse_gate_spec("bar.json")


if __name__ == "__main__":
    unittest.main()
