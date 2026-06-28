# EigenSkill-Q RTX3090 Extension Draft - 2026-06-16

## New RTX3090 Evidence

We extended the local RTX3090 evidence with matched Qwen2.5-7B-Instruct task probes across FP16, AWQ, and GPTQ Int4 checkpoints. The 100-example MMLU slice produced 0.71 FP16 accuracy, 0.70 AWQ accuracy, and 0.74 GPTQ accuracy. The 100-example GSM8K slice produced 0.24 FP16 accuracy, 0.24 AWQ accuracy, and 0.16 GPTQ accuracy. Throughput remained usable on a single RTX3090, with 7B quantized runs around 6.8-11.4 generated tokens/s depending on task and backend.

We also verified a larger Qwen2.5-14B-Instruct-AWQ artifact on the same RTX3090. A 10-example MMLU smoke completed at 0.50 accuracy and 3.85 generated tokens/s, showing feasibility but not enough sample size for a quality claim.

## CSI Reprise

The reserved CSI P3 gates were rerun as a current-date reprise from existing Qwen2.5-1.5B seed-stability artifacts at n=2, n=4, and n=8. The CSI-vs-n curve passed, with monotonic increases in mean score/cost Spearman, top-20 Jaccard, and positive-set Jaccard. The trend-significance gate also passed, and the null-permutation gate reported a maximum Holm-adjusted p-value of 0.00015.

This reprise should be framed as a same-model calibration-size stability audit over existing seed-stability artifacts.

To close the stricter P3 interpretation, we added a second-pool SmolLM2-360M-Instruct CSI experiment using a 32-prompt Wikitext2 validation pool. The run completed n=4, n=8, and n=16 calibration sizes with 6 independent seeds each, measuring all 225 Linear modules per seed. Seed stability improved with calibration size: mean score Spearman rose from 0.3133 at n=4 to 0.4136 at n=8 and 0.6959 at n=16. The CSI-vs-n curve passed monotonicity checks, the trend-significance gate passed with minimum full-range gain lower bound 0.1395, and the null-permutation gate passed with maximum Holm-adjusted p-value 0.0005999.

## Skill Training Addendum

A quant-skill dataset was generated for five narrow policy skills: outlier detection, bit allocation, rotation selection, residual patching, and KV policy. The generated train/eval/test splits contain 1800/600/600 examples with zero exact or input overlap across splits. A deterministic policy bypass reached 1.0 exact JSON and 1.0 decision accuracy on the 600-example test split.

As a training-chain smoke, a SmolLM2-360M-Instruct LoRA adapter was trained for 0.053 epoch on the quant-skill training split using completion-only loss. The run trained 4.34M adapter parameters, completed in 43.86s, and produced train/eval losses of 2.625/2.627. This confirms that the local skill-data and adapter-training path is executable, but the run is intentionally too short to support a learned-skill quality claim.

## Boundary

The new evidence should be framed as local-system feasibility and matched-slice diagnostics. It should not be described as a full benchmark, a SOTA quantization result, a production deployment measurement, or proof of general skill learning.
