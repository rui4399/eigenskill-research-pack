from __future__ import annotations

import argparse
import unittest

import gate_allocation_family_proxy as gate


def args(**overrides):
    values = {
        "min_cases": 2,
        "min_records": 2,
        "required_method_token": "q_palette",
        "budget_tolerance": 1.0e-6,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def case(label: str, method: str = "q_palette_style_lagrangian", avg_bits: float = 4.5) -> dict:
    return {
        "label": label,
        "method": method,
        "record_count": 12,
        "target_avg_bits": 4.5,
        "avg_bits": avg_bits,
        "budget_satisfied": avg_bits <= 4.5,
        "objective_distortion": 1.0,
        "bit_hist": {"4": 10, "8": 2},
    }


class GateAllocationFamilyProxyTests(unittest.TestCase):
    def test_passes_budgeted_proxy_cases(self) -> None:
        result = gate.build_result([case("wiki"), case("c4")], args())
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["case_count"], 2)

    def test_fails_when_method_token_is_missing(self) -> None:
        result = gate.build_result([case("wiki", method="plain_lagrangian"), case("c4")], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("method" in failure for failure in result["failures"]))

    def test_fails_when_budget_is_exceeded(self) -> None:
        result = gate.build_result([case("wiki", avg_bits=4.6), case("c4")], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("avg_bits" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
