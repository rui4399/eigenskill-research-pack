import json
import tempfile
import unittest
from pathlib import Path

import select_projection_role_policy as selector


def write_result(root: Path, name: str, base_passes: int, fused_passes: int, base_tps: float, fused_tps: float, base_ttft: float = 0.2, fused_ttft: float = 0.2) -> Path:
    path = root / name
    data = {
        "baseline": {
            "aggregate": {
                "tasks": 10,
                "passes": base_passes,
                "accuracy": base_passes / 10,
                "mean_tokens_per_second": base_tps,
                "mean_ttft_seconds": base_ttft,
            }
        },
        "fused": {
            "aggregate": {
                "tasks": 10,
                "passes": fused_passes,
                "accuracy": fused_passes / 10,
                "mean_tokens_per_second": fused_tps,
                "mean_ttft_seconds": fused_ttft,
            }
        },
    }
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


class ProjectionRolePolicySelectorTest(unittest.TestCase):
    def test_scores_quality_preserving_candidate_across_splits(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            split_a = write_result(root, "v1.json", 5, 5, 24.0, 24.2, 0.15, 0.14)
            split_b = write_result(root, "ifeval.json", 2, 2, 24.0, 26.0, 0.23, 0.15)

            candidate = selector.parse_candidate(f"layers17_vonly={split_a},{split_b}", ["v1", "ifeval"], root)
            scored = selector.score_candidate(candidate)

            self.assertEqual("conservative_candidate", scored["selector_decision"])
            self.assertEqual(0, scored["total_pass_delta"])
            self.assertGreater(scored["min_speedup"], 1.0)
            self.assertLess(scored["max_ttft_ratio"], 1.0)

    def test_rejects_any_split_quality_regression(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ok = write_result(root, "v1.json", 5, 5, 24.0, 24.2)
            bad = write_result(root, "ifeval.json", 2, 1, 25.0, 22.0)

            candidate = selector.parse_candidate(f"layers1720_vonly={ok},{bad}", ["v1", "ifeval"], root)
            scored = selector.score_candidate(candidate)

            self.assertEqual("reject_quality_regression", scored["selector_decision"])
            self.assertEqual(-1, scored["total_pass_delta"])
            self.assertLess(scored["min_accuracy_delta"], 0.0)

    def test_marks_runtime_regression_without_quality_drop_as_diagnostic(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            slow = write_result(root, "v1.json", 5, 5, 24.0, 16.8, 0.16, 0.43)

            candidate = selector.parse_candidate(f"slow_vonly={slow}", ["v1"], root)
            scored = selector.score_candidate(candidate)

            self.assertEqual("diagnostic_runtime_regression", scored["selector_decision"])
            self.assertEqual(0, scored["total_pass_delta"])
            self.assertLess(scored["min_speedup"], 0.75)


if __name__ == "__main__":
    unittest.main()
