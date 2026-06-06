import json
import tempfile
import unittest
from pathlib import Path

import select_failure_aware_role_policy as policy


def candidate(label, speedup, type_summary):
    return {
        "label": label,
        "speedup": speedup,
        "type_summary": type_summary,
        "regressions": [
            {"type": task_type, "id": f"{label}_{task_type}_{idx}"}
            for task_type, summary in type_summary.items()
            for idx in range(summary.get("regressions", 0))
        ],
    }


class FailureAwareRolePolicyTest(unittest.TestCase):
    def test_selects_fastest_non_regressing_candidate_per_task_type(self):
        report = {
            "reports": [
                candidate(
                    "qonly_layers17",
                    0.92,
                    {
                        "mcq": {"tasks": 4, "baseline_passes": 3, "fused_passes": 2, "regressions": 1, "fixes": 0},
                        "json_keys": {"tasks": 4, "baseline_passes": 3, "fused_passes": 3, "regressions": 0, "fixes": 0},
                    },
                ),
                candidate(
                    "konly_layers17",
                    0.97,
                    {
                        "mcq": {"tasks": 4, "baseline_passes": 3, "fused_passes": 3, "regressions": 0, "fixes": 0},
                        "json_keys": {"tasks": 4, "baseline_passes": 3, "fused_passes": 2, "regressions": 1, "fixes": 0},
                    },
                ),
                candidate(
                    "vonly_layers17",
                    0.95,
                    {
                        "mcq": {"tasks": 4, "baseline_passes": 3, "fused_passes": 2, "regressions": 1, "fixes": 0},
                        "json_keys": {"tasks": 4, "baseline_passes": 3, "fused_passes": 2, "regressions": 1, "fixes": 0},
                    },
                ),
            ]
        }

        result = policy.build_policy(report)

        self.assertEqual("konly_layers17", result["task_type_policies"]["mcq"]["recommended_candidate"])
        self.assertEqual("qonly_layers17", result["task_type_policies"]["json_keys"]["recommended_candidate"])
        self.assertEqual(["qonly_layers17", "vonly_layers17"], result["task_type_policies"]["mcq"]["rejected_candidates"])

    def test_marks_type_unsafe_when_every_candidate_regresses(self):
        report = {
            "reports": [
                candidate("qonly", 0.9, {"json_keys": {"tasks": 2, "baseline_passes": 2, "fused_passes": 1, "regressions": 1, "fixes": 0}}),
                candidate("konly", 0.8, {"json_keys": {"tasks": 2, "baseline_passes": 2, "fused_passes": 1, "regressions": 1, "fixes": 0}}),
            ]
        }

        result = policy.build_policy(report)

        self.assertEqual("no_safe_candidate", result["task_type_policies"]["json_keys"]["decision"])
        self.assertIsNone(result["task_type_policies"]["json_keys"]["recommended_candidate"])

    def test_cli_writes_json_and_markdown(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path = root / "regression.json"
            out_json = root / "policy.json"
            out_md = root / "policy.md"
            input_path.write_text(
                json.dumps(
                    {
                        "reports": [
                            candidate("qonly", 0.91, {"mcq": {"tasks": 2, "baseline_passes": 1, "fused_passes": 1, "regressions": 0, "fixes": 0}})
                        ]
                    }
                ),
                encoding="utf-8",
            )

            rc = policy.main(["--regression-json", str(input_path), "--out-json", str(out_json), "--out-md", str(out_md)])

            self.assertEqual(0, rc)
            self.assertIn("task_type_policies", json.loads(out_json.read_text(encoding="utf-8")))
            self.assertIn("Failure-Aware", out_md.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
