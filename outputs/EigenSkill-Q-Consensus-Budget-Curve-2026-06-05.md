# EigenSkill-Q Consensus Budget Curve Update

Date: 2026-06-05

This update strengthens the quantization track with a budget-curve diagnostic
for the cross-dataset consensus allocator. The goal is to test whether the
allocation behaves like a real constrained mixed-precision policy rather than a
single lucky 4.5-bit point.

## Method

For each model, two short calibration probes are used:

```text
left split:  WikiText2 sensitivity probe
right split: C4 sensitivity probe
```

Each probe measures per-Linear-module loss increase after temporarily
fake-quantizing that module to INT4. The consensus allocator first protects
modules selected by both probes, then fills the remaining budget by average
positive loss-per-cost:

```text
score_i = 0.5 * (delta_i(WikiText2) + delta_i(C4)) / cost_i
```

Three average-bit budgets were generated and evaluated:

```text
4.25, 4.50, 4.75 average bits
```

All model runs used the GPU guard with `--max-memory-ratio 0.85`.

## Results

| dataset | model | 4.25-bit PPL | 4.50-bit PPL | 4.75-bit PPL | uniform INT4 PPL |
|---|---|---:|---:|---:|---:|
| WikiText2-64 | Qwen3-1.7B | 28.0753 | 27.3180 | 26.6163 | 31.8353 |
| C4-64 | Qwen3-1.7B | 30.4752 | 29.9230 | 29.2500 | 32.4338 |
| WikiText2-64 | OLMo2-1B | 23.2779 | 22.5113 | 22.1464 | 24.1311 |
| C4-64 | OLMo2-1B | 37.9817 | 37.2835 | 37.1610 | 38.8025 |

The curve is monotonic across both model families and both datasets: giving the
allocator more 8-bit budget consistently reduces fake-quant PPL.

## GPU Guard

| run | peak VRAM | peak ratio | guard |
|---|---:|---:|---:|
| Qwen3-1.7B WikiText2-64 | 5057 / 8151 MiB | 0.6204 | 0.85 |
| Qwen3-1.7B C4-64 | 5065 / 8151 MiB | 0.6214 | 0.85 |
| OLMo2-1B WikiText2-64 | 4369 / 8151 MiB | 0.5360 | 0.85 |
| OLMo2-1B C4-64 | 4369 / 8151 MiB | 0.5360 | 0.85 |

No run was killed by the guard.

## C++ Evidence

This update also adds a standalone C++ split-stability audit:

```text
inference_cpp/src/quant_sensitivity_stability.cpp
```

It computes positive-set Jaccard, sign agreement, Pearson/Spearman/Kendall
rank statistics, and top-k overlap directly from the sensitivity JSON files.
The C++ build now has six CTest smoke tests, all passing.

## Interpretation

The new result supports a narrower, defensible claim:

```text
Cross-dataset consensus allocation produces a stable budget-quality curve in
short-slice fake-quant diagnostics on Qwen3-1.7B and OLMo2-1B.
```

It does not prove a production quantizer, packed INT4 runtime, hardware latency
gain, or superiority over GPTQ/AWQ/SmoothQuant/QuaRot. Those baselines remain
required before a serious journal or conference submission.

## Evidence Files

```text
outputs/consensus_budget_curve_report.md
outputs/consensus_budget_curve_summary.json
outputs/consensus_budget_curve_summary.csv
data_eval/eval_configs/qwen3_1p7b_consensus_budget_curve.json
data_eval/eval_configs/olmo2_0425_1b_consensus_budget_curve.json
outputs/qwen3_1p7b_consensus_budget_curve_ppl_wikitext2_64_summary.json
outputs/qwen3_1p7b_consensus_budget_curve_ppl_c4_64_summary.json
outputs/olmo2_0425_1b_consensus_budget_curve_ppl_wikitext2_64_summary.json
outputs/olmo2_0425_1b_consensus_budget_curve_ppl_c4_64_summary.json
outputs/qwen3_1p7b_wikitext_c4_sensitivity_stability_cpp.md
outputs/olmo2_0425_1b_wikitext_c4_sensitivity_stability_cpp.md
```
