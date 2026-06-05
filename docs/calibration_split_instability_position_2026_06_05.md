# Calibration Split Instability Position

Date: 2026-06-05

This note reframes the current EigenSkill-Q branch as a calibration-robustness
study, not as a new quantizer.

## Paper Claim

The defensible research problem is:

> Existing LLM mixed-precision allocation pipelines often assume that a small
> calibration split gives a stable module-sensitivity ordering. In short edge
> settings, this assumption can fail: different public-text calibration sources
> produce low rank correlation and low top-k overlap, which makes bit allocation
> brittle under distribution shift.

The current method should be described as a conservative consensus diagnostic:
build sensitivity allocations on two calibration sources, measure their
instability, then allocate high precision to modules that survive the split.

## What Is New Enough To Study

- Calibration Split Instability (CSI) as a measurable failure mode.
- C++ reproducibility tools that report rank correlation, positive-set overlap,
  top-k overlap, sign agreement, and a scalar CSI score.
- Short-slice evidence that one-split sensitivity can beat random on one source
  while losing on another, and that consensus can repair some failures.

## What Is Not Claimed

- No claim of a new production quantization algorithm.
- No SOTA claim against AWQ, GPTQ, SmoothQuant, QuaRot, SpinQuant, or FP4
  runtimes.
- No packed-kernel memory, latency, or board-level energy result.
- No claim that beating random seeds is sufficient evidence for a top-tier
  quantization paper.

## New C++ Evidence Hook

`quant_sensitivity_stability` now emits `markdown`, `csv`, and `json`. The JSON
contains:

```json
{
  "calibration_split_instability": {
    "positive_set_instability": "...",
    "sign_instability": "...",
    "score_rank_instability": "...",
    "mean_topk_jaccard": "...",
    "topk_instability": "...",
    "csi": "..."
  }
}
```

CSI is the mean of:

- `1 - positive_set_jaccard`
- `1 - sign_agreement`
- `1 - ((score_spearman + 1) / 2)`
- `1 - mean_topk_jaccard`

It is intentionally simple and audit-friendly. It is a diagnostic score, not a
theorem.

## Next Experiments Required For A Serious Submission

1. Add AWQ/GPTQ/SmoothQuant/QuaRot/SpinQuant comparisons or integration points.
2. Add ability benchmarks beyond PPL: MMLU-style classification, GSM8K-style
   arithmetic, IFEval-style instruction following, and a code benchmark if the
   model supports it.
3. Scale beyond 1.7B when hardware allows: at least one 3B/4B stress model and
   one 7B-class model on a rented GPU or bigger local device.
4. Report CSI across model families and calibration-source pairs, not just
   downstream PPL.
5. Separate random baselines as sanity checks from real quantization baselines
   as method comparisons.

