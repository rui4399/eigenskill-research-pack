from __future__ import annotations

import math
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import torch

import run_official_gptqmodel_public_calib as gptq


class RunOfficialGptqModelPublicCalibTests(unittest.TestCase):
    def test_load_texts_reads_files_and_deduplicates(self) -> None:
        with TemporaryDirectory() as tmp:
            first = Path(tmp) / "first.txt"
            second = Path(tmp) / "second.txt"
            first.write_text("alpha\n\n beta \nalpha\n", encoding="utf-8")
            second.write_text("gamma\nbeta\n", encoding="utf-8")

            texts = gptq.load_texts([first, second])

        self.assertEqual(texts, ["alpha", "beta", "gamma"])

    def test_build_summary_computes_gptq_deltas(self) -> None:
        summary = gptq.build_summary(
            model="Qwen/Qwen2.5-0.5B-Instruct",
            artifact="outputs/local_gptq",
            calibration_source=["data_eval/public_calib.txt"],
            calibration_count=8,
            quant_config={"bits": 4, "group_size": 128},
            fp16_metrics={"prompt_count": 2, "tokens": 20, "mean_nll": 2.0, "ppl": math.exp(2.0)},
            gptq_metrics={"prompt_count": 2, "tokens": 20, "mean_nll": 2.3, "ppl": math.exp(2.3)},
            artifact_summary={"file_count": 4, "total_bytes": 1234},
            package={"name": "gptqmodel", "version": "7.0.0"},
            elapsed_seconds=10.0,
        )

        self.assertTrue(summary["passed"])
        self.assertEqual(summary["tokens"], 20)
        self.assertAlmostEqual(summary["comparison"]["delta_nll_gptq_minus_fp16"], 0.3)
        self.assertGreater(summary["comparison"]["ppl_ratio_gptq_vs_fp16"], 1.0)

    def test_build_summary_fails_for_mismatched_counts_or_empty_artifact(self) -> None:
        summary = gptq.build_summary(
            model="m",
            artifact="a",
            calibration_source=[],
            calibration_count=0,
            quant_config={"bits": 4, "group_size": 128},
            fp16_metrics={"prompt_count": 2, "tokens": 20, "mean_nll": 2.0, "ppl": 7.0},
            gptq_metrics={"prompt_count": 1, "tokens": 10, "mean_nll": 2.1, "ppl": 8.0},
            artifact_summary={"file_count": 0, "total_bytes": 0},
            package={"name": "gptqmodel", "version": "7.0.0"},
            elapsed_seconds=1.0,
        )

        self.assertFalse(summary["passed"])
        self.assertIn("prompt/token counts differ", summary["failures"])
        self.assertIn("no saved GPTQ artifact files", summary["failures"])
        self.assertIn("no public calibration source", summary["failures"])

    def test_device_arg_normalizes_cuda(self) -> None:
        self.assertEqual(gptq.gptq_device("cuda"), "cuda:0")
        self.assertEqual(gptq.gptq_device("cuda:0"), "cuda:0")
        self.assertEqual(gptq.gptq_device("cpu"), "cpu")

    def test_hf_kwargs_can_force_local_files_only(self) -> None:
        self.assertEqual(gptq.hf_kwargs(local_files_only=True), {"local_files_only": True})
        self.assertEqual(gptq.hf_kwargs(local_files_only=False), {})

    def test_select_loss_model_only_unwraps_when_requested(self) -> None:
        class FakeCausalLM:
            def __init__(self) -> None:
                self.model = object()

        model = FakeCausalLM()
        self.assertIs(gptq.select_loss_model(model, unwrap=False), model)
        self.assertIs(gptq.select_loss_model(model, unwrap=True), model.model)

    def test_output_loss_falls_back_to_logits(self) -> None:
        class FakeOutput:
            def __init__(self) -> None:
                self.logits = torch.tensor(
                    [
                        [
                            [0.0, 4.0, 0.0],
                            [0.0, 0.0, 4.0],
                            [4.0, 0.0, 0.0],
                        ]
                    ],
                    dtype=torch.float32,
                )

        input_ids = torch.tensor([[0, 1, 2]], dtype=torch.long)
        loss = gptq.output_loss(FakeOutput(), input_ids)

        self.assertLess(float(loss.item()), 0.1)

    def test_move_wrapped_model_to_device_targets_inner_model(self) -> None:
        class Inner:
            def __init__(self) -> None:
                self.device = ""

            def to(self, device: str) -> None:
                self.device = device

        class Wrapper:
            def __init__(self) -> None:
                self.model = Inner()

        wrapper = Wrapper()
        self.assertIs(gptq.move_wrapped_model_to_device(wrapper, "cuda:0"), wrapper)
        self.assertEqual(wrapper.model.device, "cuda:0")

    def test_load_saved_gptq_model_uses_from_quantized(self) -> None:
        class FakeGPTQModel:
            called_with: dict[str, object] = {}

            @classmethod
            def from_quantized(cls, model_id_or_path: str, **kwargs: object) -> str:
                cls.called_with = {"model_id_or_path": model_id_or_path, **kwargs}
                return "reloaded-model"

        with TemporaryDirectory() as tmp:
            loaded = gptq.load_saved_gptq_model(FakeGPTQModel, Path(tmp), "cuda:0", "gptq_torch")

        self.assertEqual(loaded, "reloaded-model")
        self.assertEqual(FakeGPTQModel.called_with["device"], "cuda:0")
        self.assertEqual(FakeGPTQModel.called_with["backend"], "gptq_torch")
        self.assertIs(FakeGPTQModel.called_with["trust_remote_code"], True)

    def test_should_quantize_respects_reuse_existing_artifact(self) -> None:
        with TemporaryDirectory() as tmp:
            save_dir = Path(tmp) / "artifact"

            self.assertTrue(gptq.should_quantize(save_dir, reuse_existing_artifact=False))
            self.assertTrue(gptq.should_quantize(save_dir, reuse_existing_artifact=True))

            save_dir.mkdir()
            (save_dir / "model.safetensors").write_text("x", encoding="utf-8")

            self.assertFalse(gptq.should_quantize(save_dir, reuse_existing_artifact=True))


if __name__ == "__main__":
    unittest.main()
