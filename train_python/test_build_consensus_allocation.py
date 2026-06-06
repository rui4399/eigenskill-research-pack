from __future__ import annotations

import unittest

import build_consensus_allocation as consensus


def group(module: str, positive: float, rank: int) -> dict:
    return {
        "module": module,
        "cost": 1.0,
        "param_count": 1,
        "positive_delta_nll": positive,
        "sensitivity_rank": rank,
    }


class BuildConsensusAllocationTests(unittest.TestCase):
    def test_robust_lcb_score_prefers_cross_split_consistency(self) -> None:
        left = [
            group("one_sided", 10.0, 1),
            group("consistent", 4.0, 2),
            group("weak", 1.0, 3),
        ]
        right = [
            group("one_sided", 0.0, 3),
            group("consistent", 4.0, 1),
            group("weak", 1.0, 2),
        ]
        rows = consensus.consensus_groups(left, right, robust_gamma=1.0)

        by_name = {row["module"]: row for row in rows}
        self.assertGreater(by_name["one_sided"]["consensus_score_delta_per_cost"], by_name["consistent"]["consensus_score_delta_per_cost"])
        self.assertLess(by_name["one_sided"]["robust_lcb_score_delta_per_cost"], by_name["consistent"]["robust_lcb_score_delta_per_cost"])

        alloc, meta = consensus.build_consensus(
            rows,
            [4, 4, 4],
            [4, 4, 4],
            budget_avg_bits=5.5,
            base_bits=4,
            high_bits=8,
            score_key="robust_lcb_score_delta_per_cost",
        )

        selected = consensus.module_set(rows, alloc, 8)
        self.assertEqual(selected, {"consistent"})
        self.assertEqual(meta["score_key"], "robust_lcb_score_delta_per_cost")

    def test_mean_policy_keeps_existing_one_sided_behavior(self) -> None:
        left = [
            group("one_sided", 10.0, 1),
            group("consistent", 4.0, 2),
        ]
        right = [
            group("one_sided", 0.0, 2),
            group("consistent", 4.0, 1),
        ]
        rows = consensus.consensus_groups(left, right)
        alloc, _meta = consensus.build_consensus(rows, [4, 4], [4, 4], 6.0, 4, 8)
        self.assertEqual(consensus.module_set(rows, alloc, 8), {"one_sided"})


if __name__ == "__main__":
    unittest.main()
