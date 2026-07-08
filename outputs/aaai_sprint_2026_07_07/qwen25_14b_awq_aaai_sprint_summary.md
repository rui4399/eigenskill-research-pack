# Qwen2.5-14B AWQ AAAI Sprint Summary

Generated: 2026-07-08

This 14B extension records downstream task-retention feasibility for the local `Qwen2.5-14B-Instruct-AWQ` checkpoint on the RTX 3090 setup. It is not a full CSI-guided allocation run: the available 14B checkpoint is already AWQ-quantized, and the current layer-sensitivity/fake-quant allocation path is designed around standard linear weights rather than AWQ custom linear modules.

## Task Retention

| Task | Method | Exact / 100 | Accuracy | Role |
|---|---|---:|---:|---|
| MMLU100 | AWQ checkpoint | 65 | 0.65 | 14B large-model downstream retention feasibility |
| GSM8K100 | AWQ checkpoint | 13 | 0.13 | 14B large-model downstream retention feasibility |

## Runtime Notes

- The result files report `quant_mode=fp16` because no extra fake quantization is applied on top of the already-AWQ checkpoint.
- AutoAWQ required a local compatibility alias from `PytorchGELUTanh` to `GELUActivation` for the installed Transformers version.
- `awq_ext` was unavailable, so AutoAWQ used its slower fallback implementation.
- These runs support the 14B scale/retention story, but they should not be described as evidence that CSI-guided allocation dominates at 14B.

## Module Compatibility Probe

A direct module probe found only one standard `torch.nn.Linear` module (`lm_head`) in the AWQ checkpoint. The transformer body uses `WQLinear_GEMM` modules without standard `.weight` tensors exposed to the existing fake-quant sensitivity path. Therefore, full 14B CSI-guided allocation is a method/tooling boundary rather than a completed result for this checkpoint.

Artifact: `outputs/aaai_sprint_2026_07_07/qwen25_14b_awq_module_compat_probe.json`

## Claim Boundary

Use this evidence as: "the pipeline can execute 14B AWQ downstream retention on RTX 3090, with MMLU100 at 65/100 and GSM8K100 at 13/100."

Do not overclaim it as: "14B CSI allocation is complete." A full 14B CSI allocation experiment still requires either an FP16 14B checkpoint or an AWQ-aware sensitivity path for custom quantized linear modules.

## Artifacts

- `outputs/aaai_sprint_2026_07_07/qwen25_14b_awq_mmlu100_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_14b_awq_gsm8k100_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_14b_awq_aaai_sprint_summary.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_14b_awq_aaai_sprint_summary.md`
