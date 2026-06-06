from __future__ import annotations

import argparse
import unittest

import gate_awq_gptq_proxy as gate


def args(**overrides):
    values = {
        "min_cases": 2,
        "min_records": 2,
        "required_artifact_token": "awq_gptq",
        "required_method_tokens": "awq,gptq",
        "target_avg_bits": 4.5,
        "min_protected_ratio": 0.05,
        "budget_tolerance": 1.0e-6,
        "require_external_package": True,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def case(label: str) -> dict:
    return {
        "label": label,
        "path": f"{label}.json",
        "method": "awq_gptq_style_ptq_baseline_proxy",
        "record_count": 12,
        "available_packages": ["optimum"],
        "methods": ["gptq_loss_hessian_proxy", "awq_activation_saliency_proxy"],
        "summaries": [
            {
                "name": "gptq_loss_hessian_proxy",
                "avg_bits": 4.45,
                "target_avg_bits": 4.5,
                "positive_sensitivity_protected_ratio": 0.20,
            },
            {
                "name": "awq_activation_saliency_proxy",
                "avg_bits": 4.40,
                "target_avg_bits": 4.5,
                "positive_sensitivity_protected_ratio": 0.18,
            },
        ],
    }


class GateAwqGptqProxyTests(unittest.TestCase):
    def test_passes_proxy_cases_with_external_package(self) -> None:
        result = gate.build_result([case("wiki"), case("c4")], args())
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["available_package_count"], 1)

    def test_fails_without_required_method_family(self) -> None:
        bad = case("wiki")
        bad["methods"] = ["gptq_loss_hessian_proxy"]
        result = gate.build_result([bad, case("c4")], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("awq" in failure for failure in result["failures"]))

    def test_fails_without_external_package_when_required(self) -> None:
        bad = case("wiki")
        bad["available_packages"] = []
        result = gate.build_result([bad, case("c4")], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("external PTQ package" in failure for failure in result["failures"]))

    def test_fails_when_budget_exceeds_target(self) -> None:
        bad = case("wiki")
        bad["summaries"][0]["avg_bits"] = 4.6
        result = gate.build_result([bad, case("c4")], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("avg_bits" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
