# AAAI Final Submission Checklist

Date: 2026-06-28

Target draft:
`paper_drafts/unified_constraint_guided_calibration_framework_2026_06_28.md`

## Submission Rule

Do not claim SOTA or AAAI-level method superiority until the required dominance,
stability, failure, and efficiency evidence below is complete. The current draft
is a theory-closed framework draft with partial RTX3090 evidence, not a finished
leaderboard paper.

## 2026-07-07 Sprint Mapping

Execution plan:
`docs/superpowers/plans/2026-07-07-aaai-experiment-sprint.md`

Sprint output root:
`outputs/aaai_sprint_2026_07_07/`

| Priority | Experiment | Reviewer objection removed | Required artifact |
|---|---|---|---|
| P0 | CSI-guided allocation downstream retention | "CSI is only an observation; it does not guide decisions." | Pareto curve plus retention table for uniform, sensitivity-only, and CSI-guided allocation |
| P0 | CSI vs simple heuristics | "Variance, entropy, or raw sensitivity may be enough." | Pearson/Spearman table predicting future retention drop |
| P0 | Calibration size scaling | "Stability may not scale into downstream accuracy." | dual-axis CSI/accuracy curve for 16--2048 calibration samples |
| P0 | Seed robustness | "The result may be a lucky seed." | mean, standard deviation, and worst-case table across seeds 0--4 |
| P0 | Bit-width sweep | "The method is not stress-tested at low bits." | INT2/INT3/INT4/INT8/FP16 retention curve on Qwen2.5-1.5B |
| P1 | Objective-aligned ablation | "Terms in the objective are decorative." | ablation table with CSI and accuracy columns |
| P1 | Model-family generalization | "This may be Qwen-specific." | at least one Llama-3.2, Phi-3, or Mistral row |
| P1 | 7B scale check | "The method may not scale beyond small models." | Qwen2.5-7B CSI stability and calibration audit |
| P2 | Dataset shift | "Calibration stability may fail under domain mismatch." | WikiText/C4 calibration vs MMLU/GSM8K evaluation table |
| P2 | Efficiency | "The method may be too expensive." | calibration time, CSI time, inference time, and peak VRAM table |
| P2 | Layer visualization | "The mechanism is not interpretable." | layer id vs CSI score plot for stable and unstable settings |

## Must Complete Before AAAI Submission

| Item | Required artifact | Pass condition |
|---|---|---|
| Win/loss matrix | table over model-task pairs | proposed method wins or ties most rows under fixed memory |
| Average rank | rank table over all methods | proposed method has best or near-best average rank |
| Seed stability | mean, standard deviation, worst-case table | gains are stable across seeds and no severe worst-case collapse |
| Bit-width sweep | INT2/INT3/INT4/INT8/FP16 retention curve | low-bit behavior is explicit rather than hidden in limitations |
| Native PTQ baselines | FP16, uniform W4, AWQ W4/G128, GPTQ W4/G128 | fair comparison under same fixtures |
| Calibration-aware baselines | SmoothQuant plus OmniQuant or equivalent | calibration-aware methods are confronted directly |
| Rotation/outlier baseline | QuaRot or SpinQuant family | modern outlier-handling method is included |
| Allocation baselines | random budget-matched, single-split top-k, mean-only consensus | stability-aware allocation beats non-stability allocation policies |
| Mechanistic ablation | objective-aligned ablation table | each loss/gate has isolated measurable effect |
| Failure cases | failure case section with examples | constraint conflict, gate misfire, and over-smoothing are discussed |
| Claim boundary | reviewer-facing claim section | unsafe claims remain excluded |

## Conditional Baselines

Use these only if the paper introduces a learned ranking/regression surrogate for
module allocation:

| Method | When required |
|---|---|
| XGBoost | if module sensitivity is learned as tabular regression/ranking |
| LightGBM | if gradient-boosted rank/regression baselines are relevant |
| MLP | if a neural module-score predictor is claimed |
| RankNet | if pairwise ranking is claimed |
| LambdaMART | if learning-to-rank is claimed |

If the final method remains a closed-form stability-adjusted score plus
constrained allocation, these are optional diagnostic baselines rather than core
PTQ baselines.

## Should Complete For Stronger Reviews

| Item | Required artifact | Why it matters |
|---|---|---|
| Efficiency table | calibration time, allocation time, inference tokens/s, peak VRAM | prevents "too expensive" rejection |
| Lambda sensitivity | sweep for \(\lambda_s,\lambda_r,\lambda_u,\lambda_b\) | tests brittleness |
| Gate visualization | histograms of \(p_s(a)\) and \(p_r(a)\) | shows gates are informative, not decorative |
| Objective trace | soft objective across accepted allocation moves | connects proposition to empirical behavior |
| Pareto plot | retention-stability-memory frontier | shows dominance beyond one accuracy row |

## Do Not Add

- New modules.
- New theory beyond the existing soft-gate and finite-descent closure.
- New loss terms unless an existing failure cannot be represented.
- Broad SOTA claims before the required tables are complete.
- Runtime speed claims without retention and memory coupling.

## Reviewer-Proof Abstract Ending

Use only after the required tables pass:

> Across multiple model-task fixtures and fixed-memory budgets, the proposed
> stability-aware allocation consistently outperforms strong native PTQ and
> allocation-policy baselines in win/loss rate, average rank, seed stability, and
> worst-case retention.

Until then, use the conservative version:

> The framework provides an auditable path for deciding when calibration-driven
> mixed-precision allocation is stable enough to trust and which evidence is
> still required before claiming SOTA quality or deployment superiority.
