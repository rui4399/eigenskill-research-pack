from __future__ import annotations

import unittest
from pathlib import Path

import build_rotation_family_proxy as proxy


class BuildRotationFamilyProxyTests(unittest.TestCase):
    def test_assigns_rotation_to_high_priority_modules_under_budget(self) -> None:
        groups = [
            {
                "index": 0,
                "module": "model.layers.0.self_attn.q_proj",
                "shape": [2048, 1024],
                "cost": 100.0,
                "positive_delta_nll": 0.08,
            },
            {
                "index": 1,
                "module": "model.layers.0.self_attn.k_proj",
                "shape": [1024, 1024],
                "cost": 100.0,
                "positive_delta_nll": 0.07,
            },
            {
                "index": 2,
                "module": "model.layers.0.mlp.down_proj",
                "shape": [1024, 4096],
                "cost": 100.0,
                "positive_delta_nll": 0.01,
            },
            {
                "index": 3,
                "module": "model.layers.0.mlp.gate_proj",
                "shape": [4096, 1024],
                "cost": 100.0,
                "positive_delta_nll": 0.05,
            },
        ]
        enriched = proxy.enrich_records(groups)
        records = proxy.assign_rotation(enriched, budget_fraction=0.75)
        rotated = [row for row in records if row["rotation_policy"] != "none"]
        self.assertGreaterEqual(len(rotated), 2)
        self.assertLessEqual(sum(float(row["cost"]) for row in rotated), 300.0)
        self.assertGreater(
            sum(float(row["projected_sensitivity_reduction"]) for row in records),
            0.0,
        )

    def test_summarize_keeps_claim_boundary(self) -> None:
        groups = [
            {
                "index": 0,
                "module": "model.layers.0.self_attn.q_proj",
                "shape": [2048, 1024],
                "cost": 100.0,
                "positive_delta_nll": 0.08,
            }
        ]
        records = proxy.assign_rotation(proxy.enrich_records(groups), budget_fraction=1.0)
        result = proxy.summarize(Path("input.json"), {"model": "toy"}, records, 1.0)
        self.assertIn("QuaRot", result["claim_boundary"])
        self.assertEqual(result["record_count"], 1)


if __name__ == "__main__":
    unittest.main()
