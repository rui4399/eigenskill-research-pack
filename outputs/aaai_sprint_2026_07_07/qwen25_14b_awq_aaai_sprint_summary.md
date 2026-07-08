# Qwen2.5-14B AWQ AAAI Sprint Summary

Generated: 2026-07-09

14B evidence now includes AWQ downstream task-retention feasibility plus an AWQ-aware activation/scale CSI proxy over WQLinear_GEMM modules. It is still not a full FP16 fake-quant CSI downstream allocation run.

## Task Retention

| Task | Method | Exact / 100 | Accuracy | Role |
|---|---|---:|---:|---|
| MMLU100 | AWQ checkpoint | 65 | 0.65 | 14B large-model downstream retention feasibility |
| GSM8K100 | AWQ checkpoint | 13 | 0.13 | 14B large-model downstream retention feasibility |

## AWQ-Aware Activation CSI Proxy

| Metric | Value |
|---|---:|
| WQLinear_GEMM modules | 336 |
| prompt sample size per split | 64 |
| top-k | 84 |
| top-k Jaccard | 0.9765 |
| Spearman rank correlation | 0.9998 |
| proxy allocation avg bits | 2.9996 |
| bit histogram | {'4': 220, '2': 116} |

This closes part of the 14B calibration-stability gap for the local AWQ checkpoint by measuring split agreement on the actual quantized body modules. It remains a proxy: no 14B weights are dequantized/re-quantized and no downstream CSI allocation score is claimed from this artifact.

## Runtime Notes
- AutoAWQ required a compatibility alias from PytorchGELUTanh to GELUActivation for the installed Transformers version.
- awq_ext was not available, so AutoAWQ used its slower fallback implementation.
- The result files use quant_mode=fp16 because no additional fake quantization is applied on top of the already-AWQ checkpoint.
- These 14B runs do not establish CSI-guided allocation superiority; they establish 14B AWQ task-retention feasibility under the current RTX 3090 environment.
- An AWQ-aware activation/scale proxy was added for all 336 WQLinear_GEMM body modules at n64 seed0/seed1; this measures split stability but does not re-quantize weights.

## Module Compatibility Probe

A direct module probe found only one standard `torch.nn.Linear` module (`lm_head`) in the AWQ checkpoint. The transformer body uses `WQLinear_GEMM`; the new proxy hooks those modules directly, while the original fake-quant path still requires standard `.weight` tensors or an FP16/offload path.

## Claim Boundary

Use this evidence as: "the pipeline can execute 14B AWQ downstream retention on RTX 3090 and can audit AWQ-module calibration stability at n64."

Do not overclaim it as: "14B full fake-quant CSI downstream allocation is complete."

## Artifacts
- `outputs/aaai_sprint_2026_07_07/qwen25_14b_awq_mmlu100_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_14b_awq_gsm8k100_v2.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_14b_awq_activation_csi_proxy_n64_seed0_seed1_2026_07_09.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_14b_awq_module_compat_probe.json`
- `outputs/aaai_sprint_2026_07_07/qwen25_14b_awq_aaai_sprint_summary.json`
