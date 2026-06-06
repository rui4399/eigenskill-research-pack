from __future__ import annotations

import unittest

import build_awq_gptq_proxy as proxy


class BuildAwqGptqProxyTests(unittest.TestCase):
    def test_budgeted_proxy_methods_protect_positive_sensitivity(self) -> None:
        groups = [
            {
                "index": 0,
                "module": "model.layers.0.self_attn.k_proj",
                "shape": [1024, 1024],
                "cost": 100.0,
                "positive_delta_nll": 0.08,
            },
            {
                "index": 1,
                "module": "model.layers.0.self_attn.v_proj",
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
        rows = proxy.enrich(groups)
        scores = proxy.method_scores(rows)
        self.assertIn("gptq_loss_hessian_proxy", scores)
        self.assertIn("awq_activation_saliency_proxy", scores)
        for method, method_scores in scores.items():
            alloc = proxy.budgeted_select(rows, method_scores, 6.0, 4, 8)
            summary = proxy.summarize_method(method, rows, method_scores, alloc, 6.0, 4)
            self.assertTrue(summary["budget_satisfied"])
            self.assertGreater(summary["positive_sensitivity_protected_ratio"], 0.0)


if __name__ == "__main__":
    unittest.main()
