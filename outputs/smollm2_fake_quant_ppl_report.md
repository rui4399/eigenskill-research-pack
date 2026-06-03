# SmolLM2-360M Fake-Quant PPL Report

Date: 2026-06-04

## Purpose

This is the first real model quality-signal experiment for EigenSkill-Q. It
evaluates short-prompt perplexity after simple per-output-channel symmetric
fake quantization of Linear weights.

Important scope:

- This is **not** GPTQ, AWQ, SmoothQuant, or a production quantizer.
- It dequantizes weights back to floating point, so it does **not** prove memory
  or latency savings.
- It is a short-prompt sanity check to connect calibration-derived allocation to
  model output quality.

## Model And Allocation

Model:

```text
HuggingFaceTB/SmolLM2-360M-Instruct
```

Allocation source:

```text
outputs/smollm2_calib_limit4_rd_alloc_4to8_budget45_summary.json
```

Allocation policy:

```text
candidate bits: {4, 8}
budget avg bits: 4.5
rate_distortion bit histogram: 4-bit=172, 8-bit=53
```

## Command

```bash
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python3 \
  train_python/eval_weight_quant_ppl.py \
  --limit-prompts 8 \
  --max-length 160 \
  --allocation outputs/smollm2_calib_limit4_rd_alloc_4to8_budget45_summary.json \
  --out outputs/smollm2_fake_quant_ppl_4to8_limit8_summary.json
```

## Result

### Per-row scale

One symmetric scale per output row:

| method | prompt count | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---:|---|
| FP16 | 8 | 179.1357 | 0.0000 | 16:225 |
| uniform INT4 | 8 | 2196.1386 | 2.5063 | 4:225 |
| uniform INT3 | 8 | 9460847.9860 | 10.8745 | 3:225 |
| RD allocation 4/8 | 8 | 1931.2498 | 2.3778 | 4:172, 8:53 |

### Group-wise scale

Symmetric scales are recomputed per output row and per input group.

| group size | method | prompt count | PPL | delta NLL vs FP16 | bit histogram |
|---:|---|---:|---:|---:|---|
| 128 | FP16 | 8 | 179.1357 | 0.0000 | 16:225 |
| 128 | uniform INT4 | 8 | 272.1800 | 0.4183 | 4:225 |
| 128 | uniform INT3 | 8 | 9212.2025 | 3.9401 | 3:225 |
| 128 | RD allocation 4/8 | 8 | 292.0088 | 0.4886 | 4:172, 8:53 |
| 64 | FP16 | 8 | 179.1357 | 0.0000 | 16:225 |
| 64 | uniform INT4 | 8 | 281.1517 | 0.4508 | 4:225 |
| 64 | uniform INT3 | 8 | 2612.1018 | 2.6798 | 3:225 |
| 64 | RD allocation 4/8 | 8 | 296.8040 | 0.5049 | 4:172, 8:53 |

## Interpretation

With per-row scales, the conservative 4/8 rate-distortion allocation improves
over uniform INT4 on this short sanity set:

```text
PPL:       2196.14 -> 1931.25
delta NLL: 2.5063  -> 2.3778
```

The result is directionally useful but still weak as scientific evidence. The
absolute PPL degradation is large because the quantizer is a naive fake-quant
baseline without GPTQ/AWQ compensation, activation smoothing, rotations, or
group-wise calibration.

After group-wise scaling is added, uniform INT4 becomes much stronger than the
per-row baseline:

```text
uniform INT4 PPL: 2196.14 -> 272.18 with group size 128
```

However, the current rate-distortion allocation becomes worse than uniform INT4:

```text
group size 128: uniform INT4 PPL 272.18, RD 4/8 PPL 292.01
group size 64:  uniform INT4 PPL 281.15, RD 4/8 PPL 296.80
```

This is a useful negative result. The current sensitivity proxy is not yet
aligned with actual PPL sensitivity. The next allocation must use a stronger
calibration signal, such as per-module loss increase, activation reconstruction
error after fake quantization, or a Hessian/Fisher proxy.

## Measured Loss-Sensitive Allocation

The next allocation replaces the activation-stat sensitivity proxy with direct
per-module fake-quant loss sensitivity. It probes all 225 Linear modules by
quantizing one module at a time to group-wise INT4, evaluating short-prompt
loss, and restoring the original weight.

Sensitivity probe:

```text
probe prompts:              4
max length:                 128
group size:                 128
Linear modules:             225
loss-sensitive bit hist:    4-bit=172, 8-bit=53
weighted average bits:      4.4993
positive loss protected:    57.83%
```

The generated allocation is then evaluated on the same 8-prompt PPL setting
used above:

| method | prompt count | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---:|---|
| FP16 | 8 | 179.1357 | 0.0000 | 16:225 |
| uniform INT4 | 8 | 272.1800 | 0.4183 | 4:225 |
| activation-stat RD 4/8 | 8 | 292.0088 | 0.4886 | 4:172, 8:53 |
| loss-sensitive 4/8 | 8 | 212.6878 | 0.1717 | 4:172, 8:53 |

This is the first positive real-model signal for the quantization track. The
measured loss-sensitive allocation improves over uniform INT4 and fixes the
activation-stat RD failure on this scaffold:

```text
PPL:       272.18 -> 212.69 vs uniform INT4
delta NLL: 0.4183 -> 0.1717 vs uniform INT4
PPL:       292.01 -> 212.69 vs activation-stat RD 4/8
```

Evidence files:

```text
train_python/measure_module_quant_sensitivity.py
outputs/smollm2_module_loss_sensitivity_limit4_group128.json
outputs/smollm2_module_loss_sensitivity_limit4_group128_report.md
outputs/smollm2_loss_sensitive_alloc_4to8_limit4_group128_summary.json
outputs/smollm2_fake_quant_ppl_loss_sensitive_4to8_group128_limit8_summary.json
```

## WikiText2 Validation Slice

To check whether the direction holds beyond the eight hand-written prompts, a
32-prompt slice was built from WikiText2 validation:

```bash
python3 train_python/build_dataset_prompts.py \
  --dataset wikitext \
  --name wikitext-2-raw-v1 \
  --split validation \
  --limit 32 \
  --out data_eval/text_prompts/wikitext2_validation_32.txt
```

The same loss-sensitive allocation was evaluated with group size 128:

| method | prompt count | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---:|---|
| FP16 | 32 | 18.2407 | 0.0000 | 16:225 |
| uniform INT4 | 32 | 30.2604 | 0.5062 | 4:225 |
| uniform INT3 | 32 | 1678.6969 | 4.5221 | 3:225 |
| activation-stat RD 4/8 | 32 | 26.1269 | 0.3593 | 4:172, 8:53 |
| loss-sensitive 4/8 | 32 | 25.9215 | 0.3514 | 4:172, 8:53 |

This is still a small slice, but it is a more credible signal than only using
hand-written prompts. The measured loss-sensitive allocation preserves the same
direction. On this slice it is also slightly better than the activation-stat RD
allocation, but the margin is small enough that larger slices and repeated
calibration sets are required:

```text
PPL:       30.26 -> 25.92 vs uniform INT4
delta NLL: 0.5062 -> 0.3514 vs uniform INT4
PPL:       26.13 -> 25.92 vs activation-stat RD 4/8
```

Evidence files:

```text
train_python/build_dataset_prompts.py
data_eval/eval_configs/smollm2_group128_compare_allocations.json
data_eval/text_prompts/wikitext2_validation_32.txt
outputs/smollm2_fake_quant_ppl_loss_sensitive_4to8_group128_wikitext2_32_summary.json
outputs/smollm2_fake_quant_ppl_activation_rd_4to8_group128_wikitext2_32_summary.json
```

The slice was then expanded to 128 prompts and evaluated with one shared config
containing both allocation methods:

| method | prompt count | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---:|---|
| FP16 | 128 | 17.3436 | 0.0000 | 16:225 |
| uniform INT4 | 128 | 27.8236 | 0.4727 | 4:225 |
| uniform INT3 | 128 | 1154.4350 | 4.1981 | 3:225 |
| activation-stat RD 4/8 | 128 | 24.5117 | 0.3459 | 4:172, 8:53 |
| loss-sensitive 4/8 | 128 | 24.1374 | 0.3305 | 4:172, 8:53 |

The 128-prompt slice keeps the same ordering:

```text
PPL:       27.82 -> 24.14 vs uniform INT4
delta NLL: 0.4727 -> 0.3305 vs uniform INT4
PPL:       24.51 -> 24.14 vs activation-stat RD 4/8
```

Evidence files:

```text
data_eval/text_prompts/wikitext2_validation_128.txt
outputs/smollm2_fake_quant_ppl_compare_allocations_group128_wikitext2_128_summary.json
```

## Negative Result From 2/3/4/8 Allocation

The earlier 3.2 average-bit allocation over `{2,3,4,8}` was much worse than
uniform INT4 because it assigned many modules to 2-bit or 3-bit. This supports a
more conservative near-term paper strategy:

```text
Start with {4,8} mixed precision for quality evidence.
Treat 2/3-bit as a later experiment requiring stronger compensation.
```

## Next Step

The next meaningful benchmark is:

1. Expand the measured loss-sensitive allocation to C4 and larger WikiText2
   slices beyond the current 128-prompt check.
2. Compare against Fisher/Hessian proxies and activation reconstruction error.
3. Add calibration-aware scaling or GPTQ/AWQ/SmoothQuant/rotation baselines.
4. Repeat across calibration prompt sets and report variance.
5. Report memory/latency only after weights are actually stored in compressed
   form or run through a quantized runtime.
