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

| method | prompt count | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---:|---|
| FP16 | 8 | 179.1357 | 0.0000 | 16:225 |
| uniform INT4 | 8 | 2196.1386 | 2.5063 | 4:225 |
| uniform INT3 | 8 | 9460847.9860 | 10.8745 | 3:225 |
| RD allocation 4/8 | 8 | 1931.2498 | 2.3778 | 4:172, 8:53 |

## Interpretation

The conservative 4/8 rate-distortion allocation improves over uniform INT4 on
this short sanity set:

```text
PPL:       2196.14 -> 1931.25
delta NLL: 2.5063  -> 2.3778
```

The result is directionally useful but still weak as scientific evidence. The
absolute PPL degradation is large because the quantizer is a naive fake-quant
baseline without GPTQ/AWQ compensation, activation smoothing, rotations, or
group-wise calibration.

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

1. Replace naive fake quantization with group-wise quantization.
2. Add calibration-aware scaling or GPTQ/AWQ baselines.
3. Evaluate on WikiText2/C4 slices rather than eight hand-written prompts.
4. Report memory/latency only after weights are actually stored in compressed
   form or run through a quantized runtime.
