from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import build_interaction_swap_boundary as gate


def write_search(path: Path, *, base: float, trials: list[tuple[float, float, float]], best_index: int | None) -> Path:
    trial_rows = []
    for idx, (ppl, out_delta, in_delta) in enumerate(trials):
        trial_rows.append(
            {
                "swap": {
                    "out_module": f"out_{idx}",
                    "in_module": f"in_{idx}",
                    "out_delta": out_delta,
                    "in_delta": in_delta,
                },
                "metrics": {"ppl": ppl, "mean_nll": 1.0},
            }
        )
    if best_index is None:
        best = {"swap": {"out_module": "-", "in_module": "-", "out_index": -1, "in_index": -1}, "metrics": {"ppl": base}}
    else:
        best = trial_rows[best_index]
    path.write_text(
        json.dumps(
            {
                "model": "toy",
                "prompt_count": 8,
                "max_length": 64,
                "group_size": 128,
                "base_metrics": {"ppl": base, "mean_nll": 1.0},
                "trials": trial_rows,
                "best": best,
            }
        ),
        encoding="utf-8",
    )
    return path


def write_guard(path: Path, ratio: float = 0.5, killed: bool = False) -> Path:
    path.write_text(
        json.dumps(
            {
                "returncode": 0 if not killed else 1,
                "killed_by_guard": killed,
                "max_memory_used_ratio": ratio,
                "max_memory_used_mib": int(8192 * ratio),
                "memory_total_mib": 8192,
                "max_utilization_gpu_pct": 70,
            }
        ),
        encoding="utf-8",
    )
    return path


def write_transfer(path: Path, improvements: list[float]) -> Path:
    path.write_text(
        json.dumps(
            {
                "rows": [
                    {
                        "dataset": f"d{idx}",
                        "base": 10.0,
                        "target": 10.0 - improvement,
                        "improvement": improvement,
                        "guard_status": "pass",
                    }
                    for idx, improvement in enumerate(improvements)
                ]
            }
        ),
        encoding="utf-8",
    )
    return path


class InteractionSwapBoundaryTests(unittest.TestCase):
    def test_reports_negative_proxy_global_improvement(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec = gate.SearchCaseSpec(
                "toy",
                write_search(root / "summary.json", base=10.0, trials=[(9.8, 0.20, 0.10), (10.2, 0.05, 0.20)], best_index=0),
                write_guard(root / "guard.json"),
            )
            case = gate.build_search_case(spec)

        self.assertAlmostEqual(case["best_improvement_ppl"], 0.2)
        self.assertEqual(case["interaction_counterexample_count"], 1)
        self.assertTrue(case["best_swap"]["locally_negative"])

    def test_report_passes_with_bounded_transfer_regret(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cases = [
                gate.SearchCaseSpec(
                    "improved",
                    write_search(root / "a.json", base=10.0, trials=[(9.9, 0.2, 0.1), (10.1, 0.1, 0.2)], best_index=0),
                    write_guard(root / "a_guard.json"),
                ),
                gate.SearchCaseSpec(
                    "flat",
                    write_search(root / "b.json", base=11.0, trials=[(11.2, 0.2, 0.1)], best_index=None),
                    write_guard(root / "b_guard.json"),
                ),
            ]
            report = gate.build_report(
                cases,
                transfer_matrix=write_transfer(root / "transfer.json", [0.1, -0.01]),
                min_cases=2,
                min_total_trials=3,
                max_transfer_regret_ppl=0.02,
            )

        self.assertTrue(report["passed"])
        self.assertEqual(report["summary"]["improved_case_count"], 1)
        self.assertEqual(report["summary"]["interaction_counterexample_count"], 1)
        self.assertAlmostEqual(report["summary"]["transfer_max_regret_ppl"], 0.01)

    def test_report_fails_when_transfer_regret_exceeds_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec = gate.SearchCaseSpec(
                "improved",
                write_search(root / "a.json", base=10.0, trials=[(9.9, 0.2, 0.1)], best_index=0),
                write_guard(root / "a_guard.json"),
            )
            report = gate.build_report(
                [spec],
                transfer_matrix=write_transfer(root / "transfer.json", [-0.5]),
                min_cases=1,
                min_total_trials=1,
                max_transfer_regret_ppl=0.02,
            )

        self.assertFalse(report["passed"])
        self.assertIn("transfer regret", " ".join(report["failures"]))


if __name__ == "__main__":
    unittest.main()
