from __future__ import annotations

import math
import unittest

import run_official_awq_matched_ppl as matched


class RunOfficialAwqMatchedPplTests(unittest.TestCase):
    def test_select_loss_model_keeps_hf_causal_lm_by_default(self) -> None:
        class FakeCausalLM:
            def __init__(self) -> None:
                self.model = object()

        model = FakeCausalLM()
        self.assertIs(matched.select_loss_model(model, unwrap_awq=False), model)

    def test_select_loss_model_can_unwrap_awq_wrapper(self) -> None:
        class FakeAwqWrapper:
            def __init__(self) -> None:
                self.model = object()

        wrapper = FakeAwqWrapper()
        self.assertIs(matched.select_loss_model(wrapper, unwrap_awq=True), wrapper.model)

    def test_awq_device_map_uses_dict_for_cuda(self) -> None:
        self.assertEqual(matched.awq_device_map("cuda"), {"": "cuda:0"})
        self.assertEqual(matched.awq_device_map("cuda:0"), {"": "cuda:0"})
        self.assertEqual(matched.awq_device_map("cpu"), {"": "cpu"})

    def test_build_summary_computes_awq_deltas(self) -> None:
        summary = matched.build_summary(
            model="Qwen/Qwen2.5-0.5B-Instruct",
            awq_artifact="outputs/local_awq",
            prompt_source="default",
            fp16_metrics={"prompt_count": 4, "tokens": 40, "mean_nll": 2.0, "ppl": math.exp(2.0)},
            awq_metrics={"prompt_count": 4, "tokens": 40, "mean_nll": 2.2, "ppl": math.exp(2.2)},
            elapsed_seconds=12.5,
            package={"name": "autoawq", "version": "0.2.9"},
        )

        self.assertTrue(summary["passed"])
        self.assertAlmostEqual(summary["comparison"]["delta_nll_awq_minus_fp16"], 0.2)
        self.assertGreater(summary["comparison"]["ppl_ratio_awq_vs_fp16"], 1.0)
        self.assertEqual(summary["prompt_count"], 4)
        self.assertEqual(summary["tokens"], 40)

    def test_build_summary_fails_when_counts_do_not_match(self) -> None:
        summary = matched.build_summary(
            model="m",
            awq_artifact="a",
            prompt_source="default",
            fp16_metrics={"prompt_count": 4, "tokens": 40, "mean_nll": 2.0, "ppl": 7.0},
            awq_metrics={"prompt_count": 3, "tokens": 30, "mean_nll": 2.1, "ppl": 8.0},
            elapsed_seconds=1.0,
            package={"name": "autoawq", "version": "0.2.9"},
        )

        self.assertFalse(summary["passed"])
        self.assertIn("prompt/token counts differ", summary["failures"])


if __name__ == "__main__":
    unittest.main()
