from __future__ import annotations

import unittest

import run_official_awq_smoke as smoke


class FakeTokenizer:
    def __init__(self, lengths: list[int]) -> None:
        self.lengths = lengths
        self.calls = 0

    def encode(self, _text: str) -> list[int]:
        length = self.lengths[self.calls]
        self.calls += 1
        return list(range(length))


class RunOfficialAwqSmokeTests(unittest.TestCase):
    def test_calibration_plan_detects_empty_awq_blocks(self) -> None:
        plan = smoke.build_calibration_plan(
            ["a", "b", "c"],
            FakeTokenizer([4, 5, 6]),
            max_samples=3,
            max_seq_len=32,
        )
        self.assertEqual(plan["accepted_sample_count"], 3)
        self.assertEqual(plan["total_accepted_tokens"], 15)
        self.assertEqual(plan["expected_awq_blocks"], 0)
        self.assertFalse(plan["ok"])

    def test_calibration_plan_passes_when_full_block_exists(self) -> None:
        plan = smoke.build_calibration_plan(
            ["a", "b", "c"],
            FakeTokenizer([10, 12, 11]),
            max_samples=3,
            max_seq_len=16,
        )
        self.assertEqual(plan["expected_awq_blocks"], 2)
        self.assertTrue(plan["ok"])


if __name__ == "__main__":
    unittest.main()
