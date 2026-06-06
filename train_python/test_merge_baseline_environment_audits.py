from __future__ import annotations

import unittest

import merge_baseline_environment_audits as merge_audits


class MergeBaselineEnvironmentAuditsTests(unittest.TestCase):
    def test_merges_package_availability_across_environments(self) -> None:
        windows = {
            "packages": [
                {"name": "optimum", "available": True, "version": "2.1.0"},
                {"name": "triton", "available": False, "version": ""},
            ],
            "torch": {"available": True, "version": "2.12.0+cpu", "cuda_available": False},
        }
        wsl = {
            "packages": [
                {"name": "optimum", "available": False, "version": ""},
                {"name": "triton", "available": True, "version": "3.7.0"},
            ],
            "torch": {"available": True, "version": "2.12.0+cu130", "cuda_available": True},
        }
        merged = merge_audits.merge([("windows", windows), ("wsl", wsl)])
        packages = {item["name"]: item for item in merged["packages"]}
        self.assertTrue(packages["optimum"]["available"])
        self.assertTrue(packages["triton"]["available"])
        self.assertEqual(merged["torch"]["source_label"], "wsl")
        self.assertTrue(merged["torch"]["cuda_available"])


if __name__ == "__main__":
    unittest.main()
