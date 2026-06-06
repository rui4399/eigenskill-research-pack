from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import gate_paper_evidence_alignment as gate


def touch(root: Path, path: str) -> None:
    full = root / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text("x\n", encoding="utf-8")


class PaperEvidenceAlignmentTests(unittest.TestCase):
    def test_clean_paper_passes_with_negated_high_risk_claims(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            required = (
                "outputs/EVIDENCE.md",
                "docs/PAPER_CLAIM_MATRIX.md",
            )
            for path in required:
                touch(root, path)
            ledger = root / "outputs" / "ledger.json"
            ledger.write_text(json.dumps({"gate_count": 2}), encoding="utf-8")
            paper = root / "paper.md"
            paper.write_text(
                "\n".join(
                    [
                        "# Draft",
                        "The current evidence ledger passes 2/2 gates.",
                        "This is not a state-of-the-art quantizer.",
                        "It does not claim production runtime readiness.",
                        "Primary evidence:",
                        "outputs/EVIDENCE.md",
                        "docs/PAPER_CLAIM_MATRIX.md",
                    ]
                ),
                encoding="utf-8",
            )

            report = gate.build_report(root, Path("paper.md"), required_references=required, ledger_json=Path("outputs/ledger.json"))

        self.assertTrue(report["passed"])
        self.assertEqual(report["summary"]["unsafe_claim_count"], 0)
        self.assertEqual(report["summary"]["missing_referenced_path_count"], 0)

    def test_missing_referenced_path_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paper = root / "paper.md"
            paper.write_text("outputs/missing.md\n", encoding="utf-8")
            report = gate.build_report(root, Path("paper.md"), required_references=())

        self.assertFalse(report["passed"])
        self.assertEqual(report["missing_referenced_paths"], ["outputs/missing.md"])

    def test_non_negated_unsafe_claim_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paper = root / "paper.md"
            paper.write_text("EigenSkill-Q is a state-of-the-art quantizer.\n", encoding="utf-8")
            report = gate.build_report(root, Path("paper.md"), required_references=())

        self.assertFalse(report["passed"])
        self.assertEqual(report["summary"]["unsafe_claim_count"], 1)

    def test_gate_count_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ledger = root / "ledger.json"
            ledger.write_text(json.dumps({"gate_count": 20}), encoding="utf-8")
            paper = root / "paper.md"
            paper.write_text("The current evidence ledger passes 19/19 gates.\n", encoding="utf-8")
            report = gate.build_report(root, Path("paper.md"), required_references=(), ledger_json=Path("ledger.json"))

        self.assertFalse(report["passed"])
        self.assertIn("gate count", " ".join(report["failures"]))

    def test_expected_gate_count_can_override_ledger_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ledger = root / "ledger.json"
            ledger.write_text(json.dumps({"gate_count": 20}), encoding="utf-8")
            paper = root / "paper.md"
            paper.write_text("The current evidence ledger passes 21/21 gates.\n", encoding="utf-8")
            report = gate.build_report(
                root,
                Path("paper.md"),
                required_references=(),
                ledger_json=Path("ledger.json"),
                expected_gate_count=21,
            )

        self.assertTrue(report["passed"])
        self.assertEqual(report["summary"]["ledger_gate_count"], 21)


if __name__ == "__main__":
    unittest.main()
