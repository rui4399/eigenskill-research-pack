from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import build_csi_cross_scale_paper_artifacts as paper


class CrossScalePaperArtifactsTest(unittest.TestCase):
    def test_build_report_preserves_same_n_and_gain_tables(self) -> None:
        report = paper.build_report(
            "Qwen2.5-0.5B",
            Path("outputs/csi_vs_n_curve_qwen25_0p5b_2026_06_07.json"),
            "Qwen2.5-1.5B",
            Path("outputs/csi_vs_n_curve_qwen25_1p5b_2026_06_11.json"),
        )

        self.assertTrue(report["passed"])
        self.assertEqual(report["common_n"], [2, 4, 8])
        self.assertEqual(len(report["same_n_table"]), 3)
        self.assertEqual(len(report["gain_table"]), 3)
        for row in report["same_n_table"]:
            for metric, _, _ in paper.METRICS:
                self.assertLess(row[metric]["right_minus_left"], 0.0)
        spearman_gain = next(row for row in report["gain_table"] if row["metric"] == "mean_score_spearman")
        self.assertGreater(spearman_gain["right_minus_left_gain"], 0.0)
        self.assertIn("not a causal scaling-law claim", report["paper_claim"])

    def test_writers_emit_markdown_and_svg(self) -> None:
        report = paper.build_report(
            "Qwen2.5-0.5B",
            Path("outputs/csi_vs_n_curve_qwen25_0p5b_2026_06_07.json"),
            "Qwen2.5-1.5B",
            Path("outputs/csi_vs_n_curve_qwen25_1p5b_2026_06_11.json"),
        )
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            svg_path = tmp_path / "figure.svg"
            md_path = tmp_path / "report.md"
            paper.write_svg(svg_path, report)
            paper.write_markdown(md_path, report, svg_path)

            svg_text = svg_path.read_text(encoding="utf-8")
            md_text = md_path.read_text(encoding="utf-8")
        self.assertIn("<svg", svg_text)
        self.assertIn("stroke-dasharray", svg_text)
        self.assertIn("Same-n Stability Table", md_text)
        self.assertIn("n=2 to n=8 Gain Table", md_text)


if __name__ == "__main__":
    unittest.main()
