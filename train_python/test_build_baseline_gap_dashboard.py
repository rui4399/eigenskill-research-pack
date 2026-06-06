from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import build_baseline_gap_dashboard as dashboard


class BaselineGapDashboardTests(unittest.TestCase):
    def test_evaluates_covered_package_only_and_missing_items(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_dir = root / "outputs"
            output_dir.mkdir()
            (output_dir / "random16_summary.json").write_text("{}", encoding="utf-8")
            manifest = {
                "schema_version": 1,
                "items": [
                    {
                        "id": "covered",
                        "family": "in_repo",
                        "priority": "required",
                        "paper_blocker": False,
                        "required_evidence_globs": ["outputs/*random16*.json"],
                        "required_packages": [],
                    },
                    {
                        "id": "partial",
                        "family": "capability",
                        "priority": "high",
                        "paper_blocker": True,
                        "partial_evidence_globs": ["outputs/*random16*.json"],
                        "required_evidence_globs": ["outputs/*mmlu*.json"],
                        "required_packages": [],
                    },
                    {
                        "id": "package_only",
                        "family": "external",
                        "priority": "high",
                        "paper_blocker": True,
                        "required_evidence_globs": ["outputs/*awq*.json"],
                        "required_packages": ["awq"],
                        "package_mode": "any",
                    },
                    {
                        "id": "missing",
                        "family": "external",
                        "priority": "high",
                        "paper_blocker": True,
                        "required_evidence_globs": ["outputs/*spinquant*.json"],
                        "required_packages": [],
                    },
                ],
            }
            audit = {"packages": [{"name": "awq", "available": True, "version": "1.0"}]}
            result = dashboard.evaluate_manifest(root, manifest, audit)
            statuses = {item["id"]: item["status"] for item in result["items"]}
            self.assertEqual(statuses["covered"], "covered")
            self.assertEqual(statuses["partial"], "partial")
            self.assertEqual(statuses["package_only"], "package_only")
            self.assertEqual(statuses["missing"], "missing")
            self.assertFalse(result["passed"])
            self.assertEqual(result["paper_blocker_missing"], ["partial", "package_only", "missing"])

    def test_all_package_mode_requires_every_package(self) -> None:
        available = {
            "torch": {"available": True},
            "triton": {"available": False},
        }
        self.assertFalse(dashboard.packages_ok(["torch", "triton"], available, "all"))
        self.assertTrue(dashboard.packages_ok(["torch", "triton"], available, "any"))

    def test_writes_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "dashboard.md"
            payload = {
                "date": "2026-06-06T00:00:00+00:00",
                "passed": False,
                "item_count": 1,
                "status_counts": {"missing": 1},
                "paper_blocker_missing": ["x"],
                "items": [
                    {
                        "id": "x",
                        "family": "external",
                        "priority": "high",
                        "paper_blocker": True,
                        "status": "missing",
                        "evidence_count": 0,
                        "package_summary": [],
                        "claim_boundary": "future work",
                    }
                ],
            }
            dashboard.write_markdown(path, payload)
            text = path.read_text(encoding="utf-8")
            self.assertIn("Baseline Gap Dashboard", text)
            self.assertIn("NOT READY", text)

    def test_load_json_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "x.json"
            path.write_text(json.dumps({"ok": True}), encoding="utf-8")
            self.assertEqual(dashboard.load_json(path), {"ok": True})


if __name__ == "__main__":
    unittest.main()
