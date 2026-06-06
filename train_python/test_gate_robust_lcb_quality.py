from __future__ import annotations

import argparse
import unittest

import gate_robust_lcb_quality as gate


def args(**overrides):
    values = {
        "min_cases": 2,
        "target_config": "wikitext_c4_robust_lcb",
        "uniform_config": "uniform_int4",
        "mean_config": "wikitext_c4_mean_consensus",
        "max_memory_ratio": 0.90,
        "require_target_beats_uniform": True,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def ppl_payload(uniform: float = 55.0, mean: float = 45.0, robust: float = 49.0) -> dict:
    return {
        "model": "Qwen/Qwen3-0.6B",
        "results": [
            {"name": "fp16", "metrics": {"ppl": 34.0, "mean_nll": 3.5}},
            {"name": "uniform_int4", "metrics": {"ppl": uniform, "mean_nll": 4.0}},
            {"name": "wikitext_c4_mean_consensus", "metrics": {"ppl": mean, "mean_nll": 3.8}},
            {"name": "wikitext_c4_robust_lcb", "metrics": {"ppl": robust, "mean_nll": 3.9}},
        ],
    }


def guard_payload(max_ratio: float = 0.70) -> dict:
    return {
        "returncode": 0,
        "killed_by_guard": False,
        "killed_by_timeout": False,
        "max_memory_used_ratio": max_ratio,
    }


class GateRobustLcbQualityTests(unittest.TestCase):
    def test_passes_when_robust_beats_uniform_under_guard(self) -> None:
        result = gate.build_result(
            [
                gate.case_summary("wiki", "wiki.json", ppl_payload(), "wiki_guard.json", guard_payload()),
                gate.case_summary("c4", "c4.json", ppl_payload(uniform=52.0, mean=44.0, robust=47.0), "c4_guard.json", guard_payload()),
            ],
            args(),
        )
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["target_wins_vs_uniform"], 2)
        self.assertEqual(result["summary"]["target_wins_vs_mean"], 0)

    def test_fails_when_robust_loses_to_uniform(self) -> None:
        result = gate.build_result(
            [
                gate.case_summary("wiki", "wiki.json", ppl_payload(uniform=48.0, robust=49.0), "wiki_guard.json", guard_payload()),
                gate.case_summary("c4", "c4.json", ppl_payload(), "c4_guard.json", guard_payload()),
            ],
            args(),
        )
        self.assertFalse(result["passed"])
        self.assertTrue(any("uniform" in failure for failure in result["failures"]))

    def test_fails_when_guard_exceeds_limit(self) -> None:
        result = gate.build_result(
            [
                gate.case_summary("wiki", "wiki.json", ppl_payload(), "wiki_guard.json", guard_payload(max_ratio=0.91)),
                gate.case_summary("c4", "c4.json", ppl_payload(), "c4_guard.json", guard_payload()),
            ],
            args(),
        )
        self.assertFalse(result["passed"])
        self.assertTrue(any("memory" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
