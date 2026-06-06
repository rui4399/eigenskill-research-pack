from __future__ import annotations

import argparse
import unittest

import gate_rotation_family_proxy as gate


def args(**overrides):
    values = {
        "min_cases": 2,
        "min_records": 2,
        "min_rotated": 1,
        "required_method_token": "rotation",
        "required_policy_tokens": "quarot,spinquant",
        "min_reduction_ratio": 0.01,
        "budget_tolerance": 1.0e-6,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def case(label: str, method: str = "quarot_spinquant_style_rotation_baseline_proxy") -> dict:
    return {
        "label": label,
        "path": f"{label}.json",
        "method": method,
        "record_count": 12,
        "rotated_count": 3,
        "rotation_budget_fraction": 0.35,
        "rotated_cost_fraction": 0.30,
        "base_positive_sensitivity": 1.0,
        "projected_positive_sensitivity_after_rotation": 0.92,
        "projected_reduction_ratio": 0.08,
        "policy_hist": {
            "none": 9,
            "quarot_static_hadamard_proxy": 1,
            "spinquant_learned_rotation_proxy": 2,
        },
    }


class GateRotationFamilyProxyTests(unittest.TestCase):
    def test_passes_budgeted_rotation_proxy_cases(self) -> None:
        result = gate.build_result([case("wiki"), case("c4")], args())
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["case_count"], 2)
        self.assertEqual(result["summary"]["total_rotated"], 6)

    def test_fails_when_policy_family_is_missing(self) -> None:
        bad = case("wiki")
        bad["policy_hist"] = {"none": 10, "quarot_static_hadamard_proxy": 2}
        result = gate.build_result([bad, case("c4")], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("spinquant" in failure for failure in result["failures"]))

    def test_fails_when_rotation_budget_is_exceeded(self) -> None:
        bad = case("wiki")
        bad["rotated_cost_fraction"] = 0.40
        result = gate.build_result([bad, case("c4")], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("rotated cost" in failure for failure in result["failures"]))

    def test_fails_when_projection_has_no_effect(self) -> None:
        bad = case("wiki")
        bad["projected_reduction_ratio"] = 0.0
        result = gate.build_result([bad, case("c4")], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("projected reduction" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
