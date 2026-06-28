# RTX3090 Experiment Report - 2026-06-16

## Scope

This run completed the RTX3090 local experiment ladder extensions on E: storage:

- Qwen2.5-7B-Instruct FP16 baseline on MMLU/GSM8K at 25 and 100 examples.
- Qwen2.5-7B-Instruct-AWQ and Qwen2.5-7B-Instruct-GPTQ-Int4 matched 25/100 example comparisons.
- Qwen2.5-14B-Instruct-AWQ 10-example feasibility smoke.
- CSI P3 reprise using existing Qwen2.5-1.5B n=2/4/8 seed-stability artifacts.
- Quant-skill data generation, deterministic bypass evaluation, and a lightweight LoRA training smoke.

All new model/cache/temp/toolchain paths were directed to E: (`/mnt/e/...` under WSL).

## Storage And Runtime Notes

- Models:
  - `/mnt/e/models/Qwen2.5-7B-Instruct` - 15G
  - `/mnt/e/models/Qwen2.5-7B-Instruct-AWQ` - 6.7G
  - `/mnt/e/models/Qwen2.5-7B-Instruct-GPTQ-Int4` - 5.3G
  - `/mnt/e/models/Qwen2.5-14B-Instruct-AWQ` - 9.4G
- Python extra deps: `/mnt/e/python_deps/quant`
- HF/cache/temp: `/mnt/e/hf_cache`, `/mnt/e/cache`, `/mnt/e/tmp`
- Triton/Inductor cache: `/mnt/e/triton_cache`, `/mnt/e/torchinductor_cache`
- E: conda toolchain: `/mnt/e/conda_envs/rtx3090_toolchain`

The quantized loaders needed an E: local C/C++ toolchain for Triton compilation. No apt/system compiler install was used.

## 7B Public Task Results

| Variant | Task | Limit | Passes | Accuracy | Mean tok/s | Mean TTFT s | Evidence |
|---|---:|---:|---:|---:|---:|---:|---|
| FP16 | MMLU | 25 | 12/25 | 0.48 | 10.993 | 0.116 | `outputs/RTX3090_FP16_QWEN25_7B_MMLU_25_2026_06_16.md` |
| AWQ | MMLU | 25 | 13/25 | 0.52 | 6.369 | 0.197 | `outputs/RTX3090_AWQ_QWEN25_7B_MMLU_25_2026_06_16.md` |
| GPTQ | MMLU | 25 | 14/25 | 0.56 | 7.581 | 0.159 | `outputs/RTX3090_GPTQMODEL_QWEN25_7B_MMLU_25_2026_06_16.md` |
| FP16 | MMLU | 100 | 71/100 | 0.71 | 8.376 | 0.132 | `outputs/RTX3090_FP16_QWEN25_7B_MMLU_100_2026_06_16.md` |
| AWQ | MMLU | 100 | 70/100 | 0.70 | 6.765 | 0.168 | `outputs/RTX3090_AWQ_QWEN25_7B_MMLU_100_2026_06_16.md` |
| GPTQ | MMLU | 100 | 74/100 | 0.74 | 7.231 | 0.149 | `outputs/RTX3090_GPTQMODEL_QWEN25_7B_MMLU_100_2026_06_16.md` |
| FP16 | GSM8K | 25 | 6/25 | 0.24 | 12.444 | 0.201 | `outputs/RTX3090_FP16_QWEN25_7B_GSM8K_25_2026_06_16.md` |
| AWQ | GSM8K | 25 | 6/25 | 0.24 | 11.395 | 0.217 | `outputs/RTX3090_AWQ_QWEN25_7B_GSM8K_25_2026_06_16.md` |
| GPTQ | GSM8K | 25 | 3/25 | 0.12 | 11.085 | 0.250 | `outputs/RTX3090_GPTQMODEL_QWEN25_7B_GSM8K_25_2026_06_16.md` |
| FP16 | GSM8K | 100 | 24/100 | 0.24 | 15.263 | 0.149 | `outputs/RTX3090_FP16_QWEN25_7B_GSM8K_100_2026_06_16.md` |
| AWQ | GSM8K | 100 | 24/100 | 0.24 | 11.416 | 0.199 | `outputs/RTX3090_AWQ_QWEN25_7B_GSM8K_100_2026_06_16.md` |
| GPTQ | GSM8K | 100 | 16/100 | 0.16 | 10.828 | 0.219 | `outputs/RTX3090_GPTQMODEL_QWEN25_7B_GSM8K_100_2026_06_16.md` |

## 14B AWQ Feasibility

| Variant | Task | Limit | Passes | Accuracy | Mean tok/s | Mean TTFT s | Evidence |
|---|---:|---:|---:|---:|---:|---:|---|
| Qwen2.5-14B-AWQ | MMLU | 10 | 5/10 | 0.50 | 3.851 | 0.330 | `outputs/RTX3090_AWQ14B_QWEN25_14B_MMLU_10_2026_06_16.md` |

## CSI P3 Reprise

The RTX3090 ladder P3 stage consumes existing seed-stability JSON files rather than rerunning model inference. A current-date reprise was run from the existing Qwen2.5-1.5B n=2/4/8 seed-stability artifacts:

| Gate | Status | Key Result | Evidence |
|---|---|---|---|
| CSI vs n curve | PASS | all three audited stability metrics strictly increase from n=2 to n=8 | `outputs/CSI_VS_N_CURVE_QWEN25_1P5B_RTX3090_REPRISE_2026_06_16.md` |
| CSI trend significance | PASS | all full-range gain CIs positive; min dominance probability 0.9156 | `outputs/CSI_TREND_SIGNIFICANCE_QWEN25_1P5B_RTX3090_REPRISE_2026_06_16.md` |
| CSI null permutation | PASS | max Holm-adjusted p-value 0.00015 | `outputs/CSI_NULL_PERMUTATION_QWEN25_1P5B_RTX3090_REPRISE_2026_06_16.md` |

Boundary: the reprise is a same-model n=2/4/8 curve over already-completed Qwen2.5-1.5B seed-stability artifacts.

## Strict Second-Pool P3 Closure

To close the literal n=4/8/16 P3 interpretation, a new second-pool CSI run was completed with `HuggingFaceTB/SmolLM2-360M-Instruct` on the 32-prompt pool `data_eval/text_prompts/wikitext2_validation_32.txt`. Each calibration size used 6 independent seeds and measured all 225 Linear modules.

| Gate | Status | Key Result | Evidence |
|---|---|---|---|
| n=4 seed stability | PASS | 6/6 cases, 15/15 finite pairs, mean score Spearman 0.3133 | `outputs/CALIBRATION_SEED_STABILITY_SMOLLM2_360M_N4_SECOND_POOL_2026_06_16.md` |
| n=8 seed stability | PASS | 6/6 cases, 15/15 finite pairs, mean score Spearman 0.4136 | `outputs/CALIBRATION_SEED_STABILITY_SMOLLM2_360M_N8_SECOND_POOL_2026_06_16.md` |
| n=16 seed stability | PASS | 6/6 cases, 15/15 finite pairs, mean score Spearman 0.6959 | `outputs/CALIBRATION_SEED_STABILITY_SMOLLM2_360M_N16_SECOND_POOL_2026_06_16.md` |
| CSI vs n curve | PASS | monotonic gains from n=4 to n=16 across all three stability metrics | `outputs/CSI_VS_N_CURVE_SMOLLM2_360M_SECOND_POOL_2026_06_16.md` |
| CSI trend significance | PASS | min full-range gain CI low 0.1395; min dominance probability 0.9644 | `outputs/CSI_TREND_SIGNIFICANCE_SMOLLM2_360M_SECOND_POOL_2026_06_16.md` |
| CSI null permutation | PASS | max Holm-adjusted p-value 0.0005999 | `outputs/CSI_NULL_PERMUTATION_SMOLLM2_360M_SECOND_POOL_2026_06_16.md` |

## Quant Skill Results

Generated quant-skill data at:

- `data_eval/eigenskill_quant_rtx3090_2026_06_16/train.jsonl`
- `data_eval/eigenskill_quant_rtx3090_2026_06_16/eval.jsonl`
- `data_eval/eigenskill_quant_rtx3090_2026_06_16/test.jsonl`

Split sizes:

- train: 1800
- eval: 600
- test: 600
- skills: `outlier_detect`, `bit_allocate`, `rotation_select`, `residual_patch`, `kv_policy`
- exact/input overlap across train/eval/test: 0

Deterministic quant-policy bypass:

- evidence: `outputs/QUANT_SKILL_DETERMINISTIC_BYPASS_2026_06_16.json`
- test examples: 600
- exact JSON: 1.0
- decision exact: 1.0
- parse error: 0.0

LoRA smoke:

- base model: `HuggingFaceTB/SmolLM2-360M-Instruct`
- output adapter: `/mnt/e/skill_runs/quant_lora_smoke_2026_06_16`
- trainable params: 4,341,760 / 366,162,880 (1.1857%)
- train runtime: 43.86s
- train loss: 2.625
- eval loss: 2.627
- epoch: 0.05333

## Implementation Notes

- `train_python/eval_chat_task_benchmark.py` was previously fixed so top-level heads such as `lm_head` are moved to CUDA with the inner model.
- `gptqmodel==5.6.12`, `autoawq==0.2.9`, `optimum`, `datasets`, `peft`, and `trl` were installed into `/mnt/e/python_deps/quant`.
- A local `pcre.py` compatibility shim maps GPTQModel's `import pcre as re` to stdlib `re`, avoiding a system gcc install for `pypcre`.
- GPTQModel fallback imports for `no_init_weights` were patched inside `/mnt/e/python_deps/quant` because the installed Transformers build does not expose that symbol.
- A local E: conda compiler toolchain enabled Triton/AWQ/GPTQ kernels without installing apt packages.

## Claim Boundary

These results support a local RTX3090 feasibility/comparison claim for the exact models, loaders, task slices, and environment above. They do not establish broad SOTA quantization quality, full benchmark generalization, mobile latency, or production inference throughput.
