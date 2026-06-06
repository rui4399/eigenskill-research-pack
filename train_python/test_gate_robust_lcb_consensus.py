from __future__ import annotations

import argparse
import unittest

import gate_robust_lcb_consensus as gate


def args(**overrides):
    values = {
        "min_cases": 3,
        "required_policy": "robust_lcb",
        "required_allocation_key": "loss_sensitive_robust_lcb_consensus_4to8",
        "target_avg_bits": 4.5,
        "budget_tolerance": 1.0e-6,
        "min_high_bit_modules": 1,
        "min_consistent_selected": 1,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def payload(
    *,
    policy: str = "robust_lcb",
    allocation_key: str = "loss_sensitive_robust_lcb_consensus_4to8",
    avg_bits: float = 4.49,
    high_count: int = 2,
    consistency: float = 0.75,
) -> dict:
    allocations = {
        allocation_key: [8] * high_count + [4] * 4,
    }
    return {
        "policy": policy,
        "policy_name": allocation_key,
        "score_key": "robust_lcb_score_delta_per_cost",
        "budget_avg_bits": 4.5,
        "allocations": allocations,
        "summaries": [
            {
                "name": allocation_key,
                "avg_bits": avg_bits,
                "bit_hist": {"8": high_count, "4": 4},
                "positive_delta_nll_protected_ratio": 0.25,
            }
        ],
        "selected_modules": [
            {
                "module": "layers.0.mlp.down_proj",
                "robust_lcb_positive_delta_nll": 1.0,
                "robust_lcb_score_delta_per_cost": 0.1,
                "calibration_consistency_ratio": consistency,
            }
        ],
    }


class GateRobustLcbConsensusTests(unittest.TestCase):
    def test_passes_three_budgeted_robust_lcb_cases(self) -> None:
        result = gate.build_result(
            [
                gate.case_summary("qwen3_0p6b", "a.json", payload()),
                gate.case_summary("qwen3_1p7b", "b.json", payload(high_count=3)),
                gate.case_summary("olmo2_1b", "c.json", payload(high_count=1)),
            ],
            args(),
        )
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["case_count"], 3)
        self.assertGreaterEqual(result["summary"]["consistent_selected_modules"], 3)

    def test_fails_when_policy_is_not_robust_lcb(self) -> None:
        result = gate.build_result(
            [
                gate.case_summary("qwen3_0p6b", "a.json", payload(policy="mean_consensus")),
                gate.case_summary("qwen3_1p7b", "b.json", payload()),
                gate.case_summary("olmo2_1b", "c.json", payload()),
            ],
            args(),
        )
        self.assertFalse(result["passed"])
        self.assertTrue(any("policy" in failure for failure in result["failures"]))

    def test_fails_when_no_selected_module_has_consistency(self) -> None:
        result = gate.build_result(
            [
                gate.case_summary("qwen3_0p6b", "a.json", payload(consistency=0.0)),
                gate.case_summary("qwen3_1p7b", "b.json", payload(consistency=0.0)),
                gate.case_summary("olmo2_1b", "c.json", payload(consistency=0.0)),
            ],
            args(min_consistent_selected=1),
        )
        self.assertFalse(result["passed"])
        self.assertTrue(any("consistent selected" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
