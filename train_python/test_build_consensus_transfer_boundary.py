from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import build_consensus_transfer_boundary as transfer


def write_summary(path: Path, rows: dict[str, float]) -> Path:
    path.write_text(
        json.dumps({"results": [{"name": name, "metrics": {"ppl": ppl}} for name, ppl in rows.items()]}),
        encoding="utf-8",
    )
    return path


class ConsensusTransferBoundaryTests(unittest.TestCase):
    def test_build_case_reports_slice_margins_and_regret(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            wiki = write_summary(root / "wiki.json", {
                "wikitext_loss_sensitive": 30.0,
                "c4_loss_sensitive": 24.0,
                "wikitext_c4_consensus": 25.0,
            })
            c4 = write_summary(root / "c4.json", {
                "wikitext_loss_sensitive": 35.0,
                "c4_loss_sensitive": 26.0,
                "wikitext_c4_consensus": 27.0,
            })
            case = transfer.build_case("toy", wiki, c4)

        self.assertEqual(case["label"], "toy")
        self.assertEqual(case["slice_count"], 2)
        self.assertEqual(case["consensus_wins_vs_left_single"], 2)
        self.assertEqual(case["consensus_wins_vs_right_single"], 0)
        self.assertEqual(case["consensus_wins_vs_worst_single"], 2)
        self.assertAlmostEqual(case["max_regret_vs_best_single"], 1.0)
        self.assertAlmostEqual(case["min_margin_vs_worst_single"], 5.0)

    def test_report_passes_as_boundary_when_regret_is_bounded(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            case = transfer.CaseSpec(
                "toy",
                write_summary(root / "wiki.json", {
                    "wikitext_loss_sensitive": 10.0,
                    "c4_loss_sensitive": 8.0,
                    "wikitext_c4_consensus": 8.2,
                }),
                write_summary(root / "c4.json", {
                    "wikitext_loss_sensitive": 11.0,
                    "c4_loss_sensitive": 9.0,
                    "wikitext_c4_consensus": 9.1,
                }),
            )
            report = transfer.build_report([case], min_cases=1, max_regret_vs_best_single=0.5)

        self.assertTrue(report["passed"])
        self.assertEqual(report["summary"]["case_count"], 1)
        self.assertEqual(report["summary"]["consensus_wins_vs_worst_single"], 2)
        self.assertAlmostEqual(report["summary"]["max_regret_vs_best_single"], 0.2)

    def test_report_fails_when_regret_exceeds_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            case = transfer.CaseSpec(
                "toy",
                write_summary(root / "wiki.json", {
                    "wikitext_loss_sensitive": 10.0,
                    "c4_loss_sensitive": 8.0,
                    "wikitext_c4_consensus": 9.0,
                }),
                write_summary(root / "c4.json", {
                    "wikitext_loss_sensitive": 11.0,
                    "c4_loss_sensitive": 9.0,
                    "wikitext_c4_consensus": 10.0,
                }),
            )
            report = transfer.build_report([case], min_cases=1, max_regret_vs_best_single=0.5)

        self.assertFalse(report["passed"])
        self.assertIn("regret", report["failures"][0])


if __name__ == "__main__":
    unittest.main()
