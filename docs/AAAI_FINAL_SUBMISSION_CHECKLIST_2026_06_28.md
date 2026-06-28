# AAAI Final Submission Checklist

Date: 2026-06-28

Target draft:
`paper_drafts/unified_constraint_guided_calibration_framework_2026_06_28.md`

## Submission Rule

Do not claim SOTA or AAAI-level method superiority until the required dominance,
stability, failure, and efficiency evidence below is complete. The current draft
is a theory-closed framework draft with partial RTX3090 evidence, not a finished
leaderboard paper.

## Must Complete Before AAAI Submission

| Item | Required artifact | Pass condition |
|---|---|---|
| Win/loss matrix | table over model-task pairs | proposed method wins or ties most rows under fixed memory |
| Average rank | rank table over all methods | proposed method has best or near-best average rank |
| Seed stability | mean, standard deviation, worst-case table | gains are stable across seeds and no severe worst-case collapse |
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

