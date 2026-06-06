from __future__ import annotations

import argparse
import unittest

import gate_public_task_model_ladder as gate


def args(**overrides):
    values = {
        "min_models": 2,
        "min_tasks_per_model": 100,
        "require_formats": "mmlu,gsm8k",
        "max_memory_ratio": 0.90,
        "min_best_total_passes": 30,
        "min_best_accuracy": 0.30,
        "require_distinct_model_names": True,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def case(label: str, model: str, passes: int, formats: list[str] | None = None, vram: float = 0.5) -> dict:
    return {
        "label": label,
        "path": f"outputs/{label}.json",
        "source_passed": True,
        "model": model,
        "task_count": 100,
        "passes": passes,
        "accuracy": passes / 100,
        "task_formats": formats or ["gsm8k", "mmlu"],
        "max_guard_vram_ratio": vram,
        "mean_tokens_per_second": 10.0,
        "mean_ttft_seconds": 0.2,
    }


class GatePublicTaskModelLadderTests(unittest.TestCase):
    def test_passes_two_model_ladder_when_best_model_has_signal(self) -> None:
        result = gate.build_result([case("4b", "model-4b", 4), case("7b", "model-7b", 39)], args())
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["model_count"], 2)
        self.assertEqual(result["summary"]["best_total_passes"], 39)

    def test_fails_when_best_model_is_too_weak(self) -> None:
        result = gate.build_result([case("4b", "model-4b", 4), case("7b", "model-7b", 20)], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("best model passes" in failure for failure in result["failures"]))

    def test_fails_when_a_model_is_missing_required_format(self) -> None:
        result = gate.build_result([case("4b", "model-4b", 4, ["mmlu"]), case("7b", "model-7b", 39)], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("missing required task formats" in failure for failure in result["failures"]))

    def test_fails_when_guard_exceeds_limit(self) -> None:
        result = gate.build_result([case("4b", "model-4b", 4), case("7b", "model-7b", 39, vram=0.95)], args())
        self.assertFalse(result["passed"])
        self.assertTrue(any("max VRAM ratio" in failure for failure in result["failures"]))


if __name__ == "__main__":
    unittest.main()
