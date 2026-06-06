#!/usr/bin/env python3
from __future__ import annotations

import unittest

try:
    import torch
except ModuleNotFoundError:  # pragma: no cover
    torch = None

if torch is not None:
    import measure_qkv_proxy_drift as proxy
else:  # pragma: no cover
    proxy = None


@unittest.skipIf(torch is None, "torch is not installed")
class ProxyDriftMathTest(unittest.TestCase):
    def test_tensor_error_reports_zero_for_identical_tensors(self) -> None:
        ref = torch.tensor([[1.0, -2.0], [3.0, 4.0]])
        got = proxy.tensor_error("hidden", ref, ref.clone())
        self.assertEqual(got["name"], "hidden")
        self.assertAlmostEqual(got["rel_l2"], 0.0, places=7)
        self.assertAlmostEqual(got["normalized_mse"], 0.0, places=7)

    def test_tensor_error_is_scale_normalized(self) -> None:
        ref = torch.tensor([2.0, 0.0])
        approx = torch.tensor([1.0, 0.0])
        got = proxy.tensor_error("x", ref, approx)
        self.assertAlmostEqual(got["rel_l2"], 0.5, places=7)
        self.assertAlmostEqual(got["normalized_mse"], 0.25, places=7)

    def test_normalize_legacy_cache_pairs(self) -> None:
        k0 = torch.zeros((1, 2, 3, 4))
        v0 = torch.ones((1, 2, 3, 4))
        k1 = torch.full((1, 2, 3, 4), 2.0)
        v1 = torch.full((1, 2, 3, 4), 3.0)
        pairs = proxy.normalize_past_key_values(((k0, v0), (k1, v1)))
        self.assertEqual(len(pairs), 2)
        self.assertTrue(torch.equal(pairs[0][0], k0))
        self.assertTrue(torch.equal(pairs[1][1], v1))


if __name__ == "__main__":
    unittest.main()
