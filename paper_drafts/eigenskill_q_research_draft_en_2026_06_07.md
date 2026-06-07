# Calibration Split Instability in Mixed-Precision LLM Quantization

**Consensus Sensitivity Allocation with Gated Packed-System Evidence**

> Research draft, 2026-06-07. This is a paper-format draft grounded in
> the current repository evidence ledger. It is not a submission-ready claim.
> It does not claim state-of-the-art quantization or official PTQ baseline
> superiority. It does not claim production runtime readiness or hardware
> deployment.

## Abstract

Mixed-precision post-training quantization often assumes that a small
calibration set can reliably rank layers or modules by quantization sensitivity.
This assumption is fragile in short-calibration settings: different calibration
splits can induce substantially different sensitivity rankings, and a
single-split bit allocation may fail even against budget-matched random
allocations. We study this failure mode as **calibration split instability** in
module-level mixed-precision LLM quantization. EigenSkill-Q is a reproducible
diagnostic artifact built around this problem. It estimates per-module
fake-quant loss sensitivity on multiple calibration views, allocates a fixed
`{4,8}`-bit budget through cross-split consensus sensitivity, and records every
paper-facing result through executable evidence gates. Across Qwen3-0.6B,
Qwen3-1.7B, OLMo2-0425-1B-Instruct, and SmolLM2-1.7B short-slice diagnostics,
the current evidence ledger passes 47/47 gates. The calibration-instability
gate finds 3/3 unstable model/dataset cases with mean score/cost Spearman
0.0713 and mean top-20 Jaccard 0.1022. A Qwen2.5 perturbation matrix further
separates calibration sample-size and model-scale effects: within-model
limit2-vs-limit8 sensitivity rankings have mean Spearman 0.6356, while direct
0.5B-vs-1.5B cross-scale transfer has Spearman 0.1273. A prompt-seed stability
gate on Qwen2.5-0.5B reports 15 pairwise comparisons across six deterministic
four-prompt samples from the same public WikiText2 prompt pool: mean Spearman
0.4324 with bootstrap 95% CI [0.3557, 0.5174], and mean top-20 Jaccard 0.4672
with CI [0.4200, 0.5292]. A CSI-vs-calibration-size gate further converts this
into a three-point n curve: across six-seed n=2, n=4, and n=8 prompt samples,
mean Spearman increases 0.3725 -> 0.4324 -> 0.6645, mean top-20 Jaccard
increases 0.3797 -> 0.4672 -> 0.6449, and mean positive-set Jaccard increases
0.5485 -> 0.5734 -> 0.7282. A CSI trend-significance gate reports positive
n=8-vs-n=2 bootstrap mean-gain CIs for all three audited stability metrics,
with minimum lower CI bound 0.1352 and minimum random pair dominance
probability 0.9422. A CSI null-permutation gate further rejects a pooled
n=2/n=8 label-shuffle null with maximum Holm-adjusted p-value 0.000149993
over 20,000 Monte-Carlo samples. A rank-inversion theory gate instantiates a
Chebyshev-style variance-over-gap diagnostic on the same artifacts: mean
empirical inversion falls 0.2418 -> 0.1442, and top-quartile-margin inversion
falls 0.0969 -> 0.0427. The robustness stress gate reports
11/11 wins versus uniform INT4, best random seed, and random-seed mean under the
same budget, with a one-sided sign-test p-value of 0.000488 versus best random.
A paired transfer-boundary gate shows consensus avoiding the worse single-split
policy on 4/4 Qwen3 transfer slices while allowing bounded regret versus the
best single split. Finally, an interaction-aware swap gate shows 5
locally-negative-but-globally-improved swap trials, demonstrating that additive
module ranking misses measurable global interactions. The current system
evidence is deliberately gated and prototype-level: public-task coverage now
includes a two-model guarded Ollama ladder over 200 MMLU/GSM8K subset rows and
a tiny official PTQ task-execution smoke matrix over FP16/AutoAWQ/GPTQModel
Qwen2.5-0.5B variants. We further run the same three official PTQ variants on
matched 50-row public MMLU and GSM8K subsets, producing 300 guarded task
executions and a PC-side runtime profile with TTFT, tokens/s, and guarded VRAM.
The same FP16/AutoAWQ/GPTQModel Qwen2.5-0.5B variants also run an 8-row
deterministic IFEval-style instruction-following fixture, producing 24 guarded
executions and a separate PC-side runtime profile; because FP16 is 0/8, this is
reported only as execution-path evidence.
For AutoAWQ and GPTQModel, a matched local baseline pack ties public-calibration
PPL, subset50 task execution, and subset50 runtime into one cited evidence unit;
the later true subset100 gate adds 600 matched public MMLU/GSM8K executions
with a paired PC-side runtime profile while preserving the same local-only
boundary;
it records lower guarded VRAM than FP16 but slower local tokens/s. We also add
aligned expanded public PPL gates for the public-calibrated W4/G128
Qwen2.5-0.5B AutoAWQ and GPTQModel artifacts, each evaluating 16 WikiText2 plus
16 C4 prompts. The official PTQ readiness matrix now covers 5714 total public
PPL tokens across the two packages, with max PPL ratio 1.2570. A further
Qwen2.5-1.5B AutoAWQ W4/G128 public-calibration scale-up smoke runs under an
85% VRAM guard, saves a 1.159 GB local artifact, and evaluates 16 WikiText2 plus
16 C4 public PPL prompts with max PPL ratio 1.1344.
A matching GPTQModel 7.0.0 W4/G128 scale-up smoke now freshly quantizes the
same Qwen2.5-1.5B model under a 90% VRAM guard, saves an eight-file 1.161 GB
local artifact, reloads it through `gptq_torch`, and evaluates 4 public
WikiText2 prompts with PPL ratio 1.1527 over 380 tokens; this is counted only
as native-package readiness, not full AWQ/GPTQ competitiveness.
The same Qwen2.5-1.5B FP16 and AutoAWQ artifacts now also run matched 100-row
public MMLU abstract-algebra and GSM8K subsets, covering 400 guarded task
executions: FP16 obtains 33/100 MMLU and 12/100 GSM8K, AutoAWQ obtains 34/100
MMLU and 11/100 GSM8K, the max drop versus FP16 is 0.01, and peak guarded VRAM
falls from 6531 MiB to 4919 MiB while AutoAWQ remains slower in this local
loader path.
The larger 2026-06-08 Qwen2.5-1.5B task-retention gate extends this to the same
100-row MMLU abstract-algebra fixture plus 200 GSM8K rows, covering 600 guarded
task executions: FP16 obtains 33/100 MMLU and 19/200 GSM8K, while AutoAWQ
obtains 34/100 MMLU and 22/200 GSM8K, with no measured accuracy drop versus the
offloaded FP16 baseline and peak guarded VRAM ratio 0.8295. The paired runtime
profile is reported only as a local guarded profile because the FP16 path uses
HF CPU/GPU offload to stay under the 90% VRAM guard.
The paired statistical gate adds Wilson accuracy intervals and paired bootstrap
AutoAWQ-minus-FP16 deltas over the shared task ids: GSM8K delta is +0.015 with
95% bootstrap CI [-0.035, +0.065], and MMLU delta is +0.010 with CI
[-0.100, +0.130]. These wide intervals are used as uncertainty disclosure, not
as a superiority claim.
ESMP packaging, Triton shape tuning, selected-row
execution, shallow fused-QKV generation, and C++ audit tools are executable.
The repository does not claim a production LLM runtime.

## 1. Introduction

Low-bit post-training quantization is one of the most practical routes for
deploying large language models under memory and bandwidth constraints. Uniform
low-bit quantization, however, treats all modules as equally tolerant to
quantization error. Mixed precision addresses this by reserving higher precision
for modules believed to be sensitive and using lower precision elsewhere. The
central question becomes deceptively simple: which modules should receive the
scarce high-bit budget?

Most sensitivity-guided allocation pipelines estimate module importance from a
small calibration set. That is convenient, but it creates a statistical
weakness: the bit allocation inherits noise from the calibration split. If two
small calibration samples induce different module rankings, a single-split
allocation can look principled while still selecting the wrong high-bit modules
for the target evaluation distribution. This weakness is easy to hide when the
only comparison is against uniform INT4, because almost any reasonable
sensitivity heuristic can improve over uniform quantization. It becomes visible
when the method is compared against budget-matched random allocations and
cross-split transfer slices.

This draft argues that calibration split instability should be treated as a
first-class research problem for mixed-precision LLM quantization. The current
EigenSkill-Q artifact is not positioned as a new SOTA quantizer. Instead, it
offers three narrower contributions:

1. **Problem definition and measurement.** We define calibration split
   instability as disagreement among module-sensitivity rankings induced by
   small calibration splits, and measure it across Qwen3 and OLMo2 model
   families. We also separate same-model calibration sample-size perturbations
   from cross-model-scale perturbations on Qwen2.5 sensitivity artifacts.
2. **Consensus sensitivity allocation.** We evaluate a simple cross-split
   consensus allocator that protects modules that are consistently sensitive or
   have high average sensitivity under a fixed `{4,8}` budget.
3. **Gated evidence discipline.** We convert scattered fake-quant, runtime,
   task-smoke, paper-alignment, and repository-hygiene outputs into 41 executable gates, each
   with an explicit claim boundary.

The paper is intentionally conservative. It keeps negative results visible:
robust-LCB currently beats uniform INT4 but loses to mean consensus in 2/2
Qwen3-0.6B downstream slices; public MMLU/GSM8K smoke results are negative
capability evidence; packed-runtime evidence is module-level or shallow
generation evidence, not end-to-end deployment. This discipline is part of the
artifact: a claim is paper-facing only when it is tied to a committed artifact,
a runnable gate, and a narrow interpretation.

## 2. Related Work

### Post-training quantization for LLMs

GPTQ uses approximate second-order information for accurate weight-only
post-training quantization. AWQ protects salient weights using activation-aware
signals. SmoothQuant migrates activation scale difficulty into weights to enable
W8A8 inference. LLM.int8() handles outlier features through mixed precision.
QuaRot and SpinQuant reduce outlier difficulty through rotations. These methods
define the baseline ecosystem that a production quantization paper must compare
against. EigenSkill-Q currently includes AWQ/GPTQ and rotation-family proxy
gates, but it does not claim faithful official reproduction or superiority over
these methods.

### Mixed-precision allocation

Mixed-precision quantization methods often use Hessian, gradient, or loss
sensitivity estimates to decide where higher precision is worth the memory
budget. Recent directions such as Q-Palette, IMPQ, WINDQuant, graph-based
mixed-precision allocation, and GPU-adaptive non-uniform quantization make clear
that bit allocation is no longer novel by itself. The defensible contribution
here is narrower: small calibration splits can make sensitivity rankings
unstable, and this instability can be audited and partially mitigated through
cross-split consensus and global-feedback boundary checks.

### Rotation, KV cache, and kernel co-design

Rotation-based PTQ methods such as QuaRot, SpinQuant, BASE-Q, and ParoQuant
attack outlier structure and runtime compatibility. KV-cache methods such as
KVTuner study layer-wise or mixed-precision cache allocation. LUT Tensor Core
and MXFP-format work show that numeric format and kernel co-design matter as
much as bit allocation. EigenSkill-Q keeps these as future comparator families.
The current ESMP/Triton evidence is system-prototype evidence, not a substitute
for faithful kernel/runtime comparisons.

## 3. Problem Formulation

Let an LLM contain linear modules indexed by `i in {1, ..., n}`. Module `i` has
weight `W_i` and storage cost `c_i`. Given a bit set `{4, 8}` and an average-bit
budget `B`, the allocation problem is:

```text
b_i in {4, 8}
sum_i c_i b_i <= B * sum_i c_i
```

For a calibration split `D`, define the full-precision negative log-likelihood:

```text
L(W; D)
```

and the one-module fake-quant loss:

```text
L(W_{-i}, Q4(W_i); D).
```

The positive module sensitivity is:

```text
delta_i(D) = max(L(W_{-i}, Q4(W_i); D) - L(W; D), 0).
```

A cost-normalized ranking score is:

```text
r_i(D) = delta_i(D) / c_i.
```

Single-split allocation ranks modules by `r_i(D)` and promotes the highest
scoring modules to 8-bit until the budget is exhausted. Calibration split
instability appears when `r_i(D_a)` and `r_i(D_b)` produce substantially
different rankings for two small calibration splits.

## 4. Statistical Model of Calibration Split Instability

The empirical gates above can be interpreted through a simple estimator-noise
model. For module `i`, let the per-example loss increase caused by quantizing
only that module be

\[
X_i(x)
=
\Big[
  \ell\!\left(W_{-i}, Q_4(W_i); x\right)
  -
  \ell(W; x)
\Big]_+,
\qquad [a]_+ = \max(a,0),
\tag{1}
\]

where \(W_i\) is the weight tensor of module \(i\), \(W_{-i}\) denotes all
other weights held at full precision, \(Q_4(\cdot)\) is the local 4-bit
fake-quantization operator, and \(\ell(\cdot;x)\) is the token-level
negative-log-likelihood on example \(x\). The population module sensitivity is

\[
s_i^\star = \mathbb{E}_{x \sim \mathcal{D}}[X_i(x)].
\tag{2}
\]

Given a calibration split \(D = \{x_1,\ldots,x_m\}\), the empirical estimator
is

\[
\widehat{s}_i(D)
=
\frac{1}{m}\sum_{t=1}^{m} X_i(x_t),
\qquad
\widehat{r}_i(D)
=
\frac{\widehat{s}_i(D)}{c_i},
\qquad
r_i^\star
=
\frac{s_i^\star}{c_i},
\tag{3}
\]

where \(c_i\) is the module storage cost used by the bit-budget allocator.
Calibration split instability is the event that rankings induced by
\(\widehat{r}_i(D)\) change when \(D\) changes under a small calibration
budget.

**Proposition 1 (noisy sensitivity and pairwise rank inversion).** Assume the
calibration examples are sampled independently from \(\mathcal{D}\) and
\(\operatorname{Var}[X_i(x)] \le \sigma_i^2\). For any \(\epsilon > 0\),

\[
\Pr\!\left(
  \left|\widehat{s}_i(D) - s_i^\star\right| \ge \epsilon
\right)
\le
\frac{\sigma_i^2}{m\epsilon^2}.
\tag{4}
\]

For two modules \(i\) and \(j\), define the normalized population margin and
the normalized variance proxy as

\[
\Delta_{ij}
=
\left|r_i^\star - r_j^\star\right|,
\qquad
\tau_{ij}^2
=
\frac{\sigma_i^2}{c_i^2} + \frac{\sigma_j^2}{c_j^2}.
\tag{5}
\]

When \(\Delta_{ij}>0\), a Chebyshev-plus-union-bound argument yields the
diagnostic upper bound

\[
\Pr\!\left[
  \operatorname{sign}\!\left(\widehat{r}_i(D)-\widehat{r}_j(D)\right)
  \ne
  \operatorname{sign}\!\left(r_i^\star-r_j^\star\right)
\right]
\le
\frac{4\tau_{ij}^2}{m\Delta_{ij}^2}.
\tag{6}
\]

This is intentionally a loose diagnostic bound rather than a tight theorem. It
captures the failure mode relevant to mixed-precision allocation: rank
inversions become more likely when the calibration split is small, when
per-module loss increments have high variance, or when many modules have small
pairwise margins near the high-bit allocation threshold.

The rank-inversion gate uses a plug-in version of this bound. For each
calibration size, it treats the deterministic prompt-seed sensitivity estimates
as samples of \(\widehat{r}_i\), computes seed-level means and variances, and
reports the clipped proxy

\[
\widehat{B}_{ij}
=
\min\!\left\{
  1,\,
  \frac{\widehat{\operatorname{Var}}(\widehat{r}_i)
        +\widehat{\operatorname{Var}}(\widehat{r}_j)}
       {\widehat{\Delta}_{ij}^{\,2} + \eta}
\right\},
\qquad
\widehat{\Delta}_{ij}
=
\left|\overline{r}_i-\overline{r}_j\right|,
\tag{7}
\]

with a small numerical stabilizer \(\eta>0\). This plug-in estimate is not a
finite-sample guarantee, but it is auditable: in the measured Qwen2.5-0.5B
setting, both empirical module-pair inversion rate and the variance-over-gap
proxy decrease as calibration size grows from \(n=2\) to \(n=8\).

Consensus averaging reduces the estimator variance when calibration views are
not perfectly correlated. Let \(D_1,\ldots,D_K\) be \(K\) calibration views and
define

\[
\widehat{s}^{\mathrm{cons}}_i
=
\frac{1}{K}\sum_{k=1}^{K}\widehat{s}_i(D_k).
\tag{8}
\]

If the \(K\) estimators are unbiased, have common variance
\(\sigma_i^2/m\), and have average pairwise correlation \(\rho_i\), then

\[
\operatorname{Var}\!\left(\widehat{s}^{\mathrm{cons}}_i\right)
=
\frac{\sigma_i^2}{mK}
\left(1+(K-1)\rho_i\right).
\tag{9}
\]

This does not prove that consensus is optimal, and it does not remove ranking
error when all views share the same bias. It does justify the paper's diagnostic
question: measure CSI directly, report variance across calibration choices, and
treat cross-view agreement as evidence that a high-bit decision is less likely
to be a single-split artifact. The six-seed Qwen2.5 gate in Section 8.3 is the
first local check of this estimator-noise story under a fixed prompt pool, and
the CSI-vs-n curve in Section 8.4 tests the expected direction of stability as
`m` increases from 2 to 8 prompts. The trend-significance gate in Section 8.5
checks whether the n=8-vs-n=2 gains survive nonparametric bootstrap auditing.
The null-permutation gate in Section 8.6 asks whether the same gain remains
unlikely under pooled-label shuffling, and the rank-inversion gate in Section
8.7 then tests the pairwise
inversion-risk proxy implied by the same estimator-noise model. The
WikiText2-vs-C4 gate measures a larger distribution-shift variant of the same
problem.

## 5. Consensus Sensitivity Allocation

Given two calibration views, `D_left` and `D_right`, EigenSkill-Q constructs
left and right high-bit candidate sets:

```text
H_left, H_right.
```

The consensus policy first protects the intersection:

```text
I = H_left ∩ H_right,
```

then fills remaining budget by average cost-normalized sensitivity:

```text
r_i^cons = 0.5 * (delta_i(D_left) + delta_i(D_right)) / c_i.
```

This is not claimed as an optimal robust allocator. It is a deliberately simple
baseline that asks whether cross-split agreement is enough to reduce the worst
single-split risk in short-calibration settings.

## 6. Interaction-aware Global Feedback

Independent module ranking is an additive approximation. It can miss
interactions: a swap that looks worse under local proxy scores may improve
global PPL after the full allocation is applied. The current artifact includes a
bounded one-step swap diagnostic:

1. start from an additive sensitivity allocation;
2. propose one-out/one-in swaps under the same `{4,8}` budget;
3. evaluate each candidate using global fake-quant PPL;
4. report both local proxy gain and global PPL improvement.

The interaction gate is a boundary result rather than a new optimizer. Its role
is to show that interaction effects are measurable and should be modeled by a
future allocator.

## 7. Evidence Gates

Every paper-facing claim is indexed by a gate JSON and a Markdown report. The
current ledger passes 47/47 gates. The most important gates are:

| Gate | Evidence | Valid claim | Non-claim |
|---|---|---|---|
| Calibration instability | 3 Qwen3/OLMo2 split comparisons | Small calibration splits induce unstable module rankings. | Instability alone proves consensus is superior. |
| Sensitivity perturbation matrix | Qwen2.5 sample-size and model-scale perturbations; see `outputs/SENSITIVITY_PERTURBATION_MATRIX_QWEN25_2026_06_07.md`. | Same-model calibration sample-size changes are more stable than cross-model-scale sensitivity transfer in the measured artifacts. | Downstream quality retention, a universal scaling law, or production quantization. |
| Calibration seed stability | Qwen2.5-0.5B six-seed prompt sampling; see `outputs/CALIBRATION_SEED_STABILITY_QWEN25_0P5B_2026_06_07.md`. | Deterministic small-sample sensitivity runs can be audited for same-model prompt-seed stability with pair-bootstrap confidence intervals; the measured top-sensitive sets still drift. | Does not prove downstream quality retention, broad seed coverage, deployment speed, or SOTA quantization. |
| CSI vs calibration size | Qwen2.5-0.5B n=2/4/8 six-seed curve; see `outputs/CSI_VS_N_CURVE_QWEN25_0P5B_2026_06_07.md`. | Sensitivity-ranking stability increases monotonically with calibration prompt count in this fixed public-prompt setting. | Universal scaling law, downstream quality retention, large-model behavior, deployment speed, or SOTA quantization. |
| CSI trend significance | Qwen2.5-0.5B n=2/4/8 seed-pair metric distributions; see `outputs/CSI_TREND_SIGNIFICANCE_QWEN25_0P5B_2026_06_07.md`. | The measured n=8 stability distribution statistically dominates the measured n=2 distribution for the audited metrics. | Does not prove a universal scaling law, downstream quality retention, broad model behavior, deployment speed, or SOTA quantization. |
| CSI null permutation | Qwen2.5-0.5B n=2/n=8 pooled seed-pair metric distributions; see `outputs/CSI_NULL_PERMUTATION_QWEN25_0P5B_2026_06_07.md`. | The measured n=8-vs-n=2 gains reject a pooled-label permutation null for the audited metrics. | Does not prove a universal scaling law, downstream quality retention, broad model behavior, deployment speed, or SOTA quantization. |
| Rank-inversion theory | Qwen2.5-0.5B n=2/4/8 plug-in inversion-risk curve; see `outputs/RANK_INVERSION_THEORY_QWEN25_0P5B_2026_06_07.md`. | Empirical module-pair inversion risk and variance/gap bound proxies decrease with calibration size in the measured artifacts. | Not a tight theoretical bound, not a universal scaling law, not downstream retention, and not SOTA quantization. |
| Robustness stress | 11 short fake-quant PPL slices | Target policies beat uniform and random baselines on committed slices. | Not SOTA PTQ or task retention. |
| Consensus transfer boundary | 4 paired Qwen3 slices | Consensus avoids the worse single-split policy with bounded best-single regret. | Consensus always beats the best single split. |
| Interaction swap boundary | 16 SmolLM2-1.7B swap trials | Global feedback exposes local-proxy failures. | Global optimality or broad transfer. |
| Allocation-family proxy | Q-Palette-style closed-form Lagrangian allocation on Qwen3 and Qwen2.5 sensitivity artifacts; see `outputs/Q_PALETTE_STYLE_ALLOCATION_FAMILY_GATE_2026_06_06.md`. | Six measured-sensitivity allocation cases satisfy a 4.5 average-bit budget with finite lambda solutions and non-trivial bit histograms. | Faithful Q-Palette/IMPQ/WINDQuant reproduction or downstream quality retention. |
| Public task model ladder | 2 local Ollama models over 200 MMLU/GSM8K subset rows | Public-task evidence is reported without hiding the weaker 4B case. | Leaderboard quality, monotonic scaling, or fused quantized retention. |
| Official PTQ task-execution smoke | FP16/AutoAWQ/GPTQModel Qwen2.5-0.5B on 24 public smoke executions; see `outputs/OFFICIAL_PTQ_TASK_RETENTION_SMOKE_MATRIX_2026_06_07.md`. | Official-package artifacts load and run matching tiny task fixtures under guard; zero-FP16 formats are execution-only. | Broad task retention, leaderboard quality, or AWQ/GPTQ competitiveness. |
| Official PTQ runtime profile | FP16/AutoAWQ/GPTQModel Qwen2.5-0.5B PC-side runtime profile; see `outputs/OFFICIAL_PTQ_RUNTIME_PROFILE_2026_06_07.md`. | TTFT, tokens/s, and peak guarded VRAM are reported for the same task-smoke path. | Not mobile deployment, not production runtime speedup, not energy savings, and not AWQ/GPTQ competitiveness. |
| Official PTQ matched subset50 | FP16/AutoAWQ/GPTQModel Qwen2.5-0.5B on 300 guarded public subset executions; see `outputs/OFFICIAL_PTQ_TASK_SUBSET50_MATRIX_2026_06_07.md`. | Official-package artifacts run the same 50-row MMLU and 50-row GSM8K subsets; MMLU is 13/50 for FP16, 11/50 for AutoAWQ, and 13/50 for GPTQModel. | Leaderboard-scale task retention, reasoning quality, or AWQ/GPTQ competitiveness. |
| Official PTQ subset50 runtime | PC-side subset50 runtime profile; see `outputs/OFFICIAL_PTQ_SUBSET50_RUNTIME_PROFILE_2026_06_07.md`. | TTFT, tokens/s, and guarded VRAM are reported for the 300-task subset path. | Not mobile deployment, not production runtime speedup, and not energy savings. |
| Official PTQ matched subset100 | FP16/AutoAWQ/GPTQModel Qwen2.5-0.5B on 600 guarded public subset executions; see `outputs/OFFICIAL_PTQ_TASK_SUBSET100_MATRIX_2026_06_07.md`. | Official-package artifacts run the regenerated true 100-row MMLU and 100-row GSM8K subsets; MMLU is 25/100 for FP16, 23/100 for AutoAWQ, and 22/100 for GPTQModel, with max drop 0.03. | Leaderboard-scale task retention, broad reasoning quality, large-model evidence, or AWQ/GPTQ competitiveness. |
| Official PTQ subset100 runtime | PC-side subset100 runtime profile; see `outputs/OFFICIAL_PTQ_SUBSET100_RUNTIME_PROFILE_2026_06_07.md`. | TTFT, tokens/s, and guarded VRAM are reported for the 600-task subset path; quantized variants reduce guarded VRAM but are slower than FP16 locally. | Not mobile deployment, not production runtime speedup, and not energy savings. |
| Official PTQ deterministic IFEval-style execution | FP16/AutoAWQ/GPTQModel Qwen2.5-0.5B on 24 guarded deterministic instruction-following executions; see `outputs/OFFICIAL_PTQ_TASK_IFEVAL_V2_MATRIX_2026_06_07.md`. | Official-package artifacts run the same JSON/keyword/length-constrained IFEval-style fixture; FP16 is 0/8, AutoAWQ is 1/8, and GPTQModel is 1/8. | Broad IFEval retention, instruction-following superiority, or AWQ/GPTQ competitiveness. |
| Official PTQ IFEval-style runtime | PC-side runtime profile for the deterministic IFEval-style fixture; see `outputs/OFFICIAL_PTQ_RUNTIME_IFEVAL_V2_PROFILE_2026_06_07.md`. | TTFT, tokens/s, and guarded VRAM are reported for the 24-execution instruction-smoke path. | Not mobile deployment, not production runtime speedup, and not energy savings. |
| Official PTQ matched baseline pack | AutoAWQ/GPTQModel Qwen2.5-0.5B public-calibration PPL, subset50 task, and subset50 runtime evidence; see `outputs/OFFICIAL_PTQ_MATCHED_BASELINE_PACK_QWEN25_0P5B_2026_06_07.md`. | A local matched 0.5B baseline package reports 4 16-prompt PPL slices, 5714 PPL tokens, 300 task executions, 300 runtime executions, max PPL ratio 1.2570, max task drop 0.0400, max VRAM ratio 0.9010, and max quantized tokens/s ratio 0.3315 versus FP16. | Not leaderboard-scale evidence, not large-model AWQ/GPTQ competitiveness, not production runtime, not mobile deployment, not energy evidence, and not SOTA PTQ. |
| Expanded official PTQ public PPL gates | Public-calibrated AutoAWQ and GPTQModel Qwen2.5-0.5B W4/G128 on 16 WikiText2 plus 16 C4 prompts; see `outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_0P5B_BUNDLE_16_GATE_2026_06_07.md` and `outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_0P5B_BUDGET8_16_GATE_2026_06_07.md`. | The reused AutoAWQ and GPTQModel artifacts run 5714 public PPL tokens under guard, with max package-vs-FP16 PPL ratio 1.2570. | Not a complete official AWQ/GPTQ baseline, not task retention, not production runtime, not mobile deployment, and not SOTA PTQ. |
| Qwen2.5-1.5B AutoAWQ scale-up readiness | Public-calibrated AutoAWQ W4/G128 Qwen2.5-1.5B on 16 WikiText2 plus 16 C4 prompts; see `outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_1P5B_BUNDLE_16_GATE_2026_06_07.md`. | The local artifact quantizes under an 85% VRAM guard with peak 6712/8151 MiB and runs 2857 public PPL tokens; max PPL ratio is 1.1344. | Not a complete official AWQ/GPTQ baseline, not task retention, not production runtime, not mobile deployment, and not SOTA PTQ. |
| Qwen2.5-1.5B GPTQModel scale-up readiness | Public-calibrated GPTQModel W4/G128 Qwen2.5-1.5B on a 4-prompt WikiText2 smoke; see `outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_1P5B_SMOKE4_GATE_2026_06_08.md`. | The local artifact is freshly quantized under a 90% VRAM guard, saved as eight files, reloaded through `gptq_torch`, and evaluated with PPL ratio 1.1527 over 380 tokens. | Not a complete official AWQ/GPTQ baseline, not task retention, not production runtime, not mobile deployment, and not SOTA PTQ. |
| Qwen2.5-1.5B matched subset100 task evidence | FP16 and AutoAWQ Qwen2.5-1.5B on 400 guarded public subset executions; see `outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_SUBSET100_MATRIX_2026_06_07.md`. | Matched 100-row MMLU/GSM8K subset evidence is now reported for the larger local artifact: FP16 is 33/100 MMLU and 12/100 GSM8K; AutoAWQ is 34/100 MMLU and 11/100 GSM8K; max drop versus FP16 is 0.01. | Not leaderboard-scale task retention, not reasoning-quality superiority, not complete AWQ/GPTQ/SmoothQuant competitiveness, not production runtime, not mobile deployment, and not SOTA PTQ. |
| Qwen2.5-1.5B subset100 runtime profile | PC-side runtime profile over the same 400 guarded task executions; see `outputs/OFFICIAL_PTQ_QWEN25_1P5B_SUBSET100_RUNTIME_PROFILE_2026_06_07.md`. | TTFT, tokens/s, and guarded VRAM are reported for FP16 and AutoAWQ; AutoAWQ lowers peak guarded VRAM from 6531 MiB to 4919 MiB but is slower than FP16 locally. | Not mobile deployment, not production runtime speedup, not energy savings, and not official AWQ/GPTQ/SmoothQuant competitiveness. |
| Qwen2.5-1.5B GSM8K200/MMLU100 task evidence | FP16 and AutoAWQ Qwen2.5-1.5B on 600 guarded public subset executions; see `outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_GSM8K200_MMLU100_MATRIX_2026_06_08.md`. | The larger slice records FP16 at 33/100 MMLU and 19/200 GSM8K, AutoAWQ at 34/100 MMLU and 22/200 GSM8K, no measured accuracy drop versus FP16, and peak guard VRAM ratio 0.8295. | Not leaderboard-scale task retention, not reasoning-quality superiority, not complete PTQ baseline coverage, not production runtime, not mobile deployment, and not SOTA PTQ. |
| Qwen2.5-1.5B GSM8K200/MMLU100 runtime profile | PC-side runtime profile over the same 600 guarded task executions; see `outputs/OFFICIAL_PTQ_QWEN25_1P5B_GSM8K200_MMLU100_RUNTIME_PROFILE_2026_06_08.md`. | TTFT, tokens/s, and guarded VRAM are reported for FP16 under HF offload and AutoAWQ; this is a controlled local profile. | Because FP16 is offloaded, this is not a production speedup claim, mobile deployment, energy result, or official AWQ/GPTQ/SmoothQuant competitiveness. |
| Qwen2.5-1.5B GSM8K200/MMLU100 statistics | Wilson intervals and paired bootstrap deltas over the same 600 guarded task executions; see `outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_GSM8K200_MMLU100_STATISTICS_2026_06_08.md`. | Task-retention uncertainty is explicit: GSM8K delta +0.015 with CI [-0.035, +0.065], MMLU delta +0.010 with CI [-0.100, +0.130]. | Not statistical superiority, leaderboard-scale retention, complete PTQ baseline coverage, production runtime, mobile deployment, energy, or SOTA PTQ. |
| W4A8 activation reconstruction | Selected Qwen3-0.6B self-attention modules from the ESMP package; see `outputs/w4a8_activation_reconstruction_2026_06_08/W4A8_ACTIVATION_RECONSTRUCTION_GATE.md`. | A8 activation quantization adds bounded module-output drift on sampled real activations: max activation-added rel-L2 0.048561 versus W4A16. | Does not prove full-model quality retention, downstream task retention, end-to-end speed, mobile deployment, energy, or SOTA quantization. |
| W4A8 extended activation reconstruction | Selected Qwen3-0.6B attention and MLP modules from layers 0/7/14/21; see `outputs/w4a8_activation_reconstruction_extended_2026_06_08/W4A8_ACTIVATION_RECONSTRUCTION_EXTENDED_GATE.md`. | The broader 24-module audit passes with median W4A8 rel-L2 0.144851 and max activation-added rel-L2 0.084533 versus W4A16, exposing MLP down projections as the worst integration-risk cases. | Does not prove full-model quality retention, downstream task retention, end-to-end speed, mobile deployment, energy, or SOTA quantization. |
| Packed-system gates | ESMP, Triton, selected-row, sidecar, QKV smoke | Prototype components are executable and audited. | Production Tensor Core/mobile runtime. |
| Paper evidence alignment | Paper draft, required evidence paths, claim-risk scan | The draft cites committed evidence and avoids unsafe non-negated claims. | Peer-review acceptance or complete baseline coverage. |

The evidence ledger is:

```text
outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md
```

## 8. Experiments

### 8.1 Calibration Split Instability

Across Qwen3-0.6B, Qwen3-1.7B, and OLMo2-0425-1B-Instruct comparisons, the
calibration-instability gate reports:

| Metric | Value |
|---|---:|
| Unstable cases | 3 / 3 |
| Mean score/cost Spearman | 0.0713 |
| Mean positive-set Jaccard | 0.4349 |
| Mean top-20 Jaccard | 0.1022 |

These low rank correlations motivate treating the calibration split as a source
of allocation risk, not merely as an implementation detail.

### 8.2 Sensitivity Perturbation Matrix

The Qwen2.5 perturbation gate separates two different questions: whether a
sensitivity ranking stabilizes when the same model receives more calibration
examples, and whether the same ranking can be transferred across model scale.

| Perturbation | Cases | Mean score/cost Spearman | Top-20 Jaccard |
|---|---:|---:|---:|
| Same-model sample size, limit2 vs limit8 | 2 | 0.6356 | min 0.4815 |
| Cross-model scale, 0.5B vs 1.5B at limit2 | 1 | 0.1273 | 0.2903 |

The separation margin between the sample-size and model-scale Spearman values
is 0.5082. This suggests that calibration instability is not a single scalar
failure mode: more samples can stabilize a ranking inside one model, while
reusing that ranking across model sizes remains weak in the measured artifacts.
This is still a diagnostic result; it does not claim downstream quality
retention or a general scaling law.

### 8.3 Calibration Seed Stability

The Qwen2.5-0.5B seed-stability gate reruns module-loss sensitivity on six
deterministic four-prompt samples from the same 16-prompt WikiText2 pool:

For a stability metric \(q\) such as score/cost Spearman, top-20 Jaccard, or
positive-set Jaccard, let

\[
z_{ab}^{(q)}
=
q\!\left(R(D_a), R(D_b)\right),
\qquad
1 \le a < b \le 6,
\tag{10}
\]

where \(R(D_a)\) is the module ranking or selected-set summary induced by prompt
sample \(D_a\). The reported mean and nonparametric confidence interval are

\[
\overline{z}^{(q)}
=
\frac{1}{15}\sum_{a<b}z_{ab}^{(q)},\qquad
\mathrm{CI}_{0.95}^{(q)}
=
\left[
  Q_{0.025}\!\left(\overline{z}^{(q),*}\right),
  Q_{0.975}\!\left(\overline{z}^{(q),*}\right)
\right],
\tag{11}
\]

where \(\overline{z}^{(q),*}\) denotes a bootstrap resample mean over the 15
seed-pair scores.

| Metric | Value |
|---|---:|
| Prompt selections | 6 |
| Pairwise comparisons | 15 |
| Mean score/cost Spearman | 0.4324 |
| Spearman bootstrap 95% CI | [0.3557, 0.5174] |
| Minimum score/cost Spearman | 0.2284 |
| Mean top-20 Jaccard | 0.4672 |
| Top-20 Jaccard bootstrap 95% CI | [0.4200, 0.5292] |
| Minimum top-20 Jaccard | 0.3793 |
| Mean positive-set Jaccard | 0.5734 |
| Positive-set Jaccard bootstrap 95% CI | [0.5375, 0.6120] |

This result is more nuanced than the WikiText2-vs-C4 split comparison:
same-pool prompt seeds produce moderate average rank agreement, but the
top-sensitive module set still changes enough to justify reporting calibration
seed variance instead of a single deterministic allocation trace.

### 8.4 CSI vs Calibration Size

The CSI-vs-n gate aggregates three six-seed Qwen2.5-0.5B prompt-sampling gates.
It checks whether ranking stability improves as the number of calibration
prompts increases from n=2 to n=8:

| Calibration prompts n | Mean score/cost Spearman | Spearman 95% CI | Mean top-20 Jaccard | Top-20 95% CI | Mean positive-set Jaccard |
|---:|---:|---:|---:|---:|---:|
| 2 | 0.3725 | [0.2960, 0.4519] | 0.3797 | [0.3336, 0.4270] | 0.5485 |
| 4 | 0.4324 | [0.3557, 0.5174] | 0.4672 | [0.4200, 0.5292] | 0.5734 |
| 8 | 0.6645 | [0.6236, 0.7048] | 0.6449 | [0.5962, 0.6915] | 0.7282 |

All three reported stability metrics increase monotonically across the three
calibration sizes. This is the first direct empirical check of the Section 4
estimator-noise prediction in the repository: more calibration examples reduce
ranking variance in the measured setting. The claim remains local to one model
and one public prompt pool; it does not prove a universal scaling law.

### 8.5 CSI Trend Significance

The trend-significance gate tests whether the n=8 distribution is not only
higher in mean than n=2, but also separated under simple nonparametric checks.
For each audited stability metric, it independently bootstraps the n=8 minus
n=2 mean gain and computes the probability that a random n=8 seed-pair score
exceeds a random n=2 seed-pair score:

Let \(\mathcal{Z}^{(q)}_{n}\) denote the multiset of seed-pair scores for
calibration size \(n\). The full-range mean gain and dominance probability are

\[
G_q(8,2)
=
\frac{1}{|\mathcal{Z}^{(q)}_8|}
  \sum_{z\in\mathcal{Z}^{(q)}_8} z
-
\frac{1}{|\mathcal{Z}^{(q)}_2|}
  \sum_{z\in\mathcal{Z}^{(q)}_2} z,
\tag{12}
\]

\[
\Pi_q(8,2)
=
\Pr_{z_8\sim\mathcal{Z}^{(q)}_8,\,
      z_2\sim\mathcal{Z}^{(q)}_2}
\left[z_8 > z_2\right].
\tag{13}
\]

The bootstrap confidence interval in the table is computed from resampled
copies of \(G_q(8,2)\). A positive lower endpoint is treated as evidence that
the measured \(n=8\) seed-pair distribution dominates \(n=2\) in this fixed
prompt-pool setting.

| Metric | n=2 mean | n=8 mean | Mean gain | Bootstrap 95% gain CI | P(n=8 pair > n=2 pair) |
|---|---:|---:|---:|---:|---:|
| Score/cost Spearman | 0.3725 | 0.6645 | 0.2920 | [0.2039, 0.3775] | 0.9422 |
| Top-20 Jaccard | 0.3797 | 0.6449 | 0.2651 | [0.1961, 0.3369] | 0.9778 |
| Positive-set Jaccard | 0.5485 | 0.7282 | 0.1797 | [0.1352, 0.2195] | 0.9644 |

All lower confidence bounds are positive, and the minimum random-pair
dominance probability is 0.9422. This strengthens the CSI-vs-n gate from a
monotonic descriptive curve into a gated local trend result, while preserving
the same boundary: it is one fixed model and prompt-pool setting, not a
universal scaling law.

### 8.6 CSI Null Permutation Test

The null-permutation gate complements the bootstrap analysis with a
label-shuffle test. It pools the n=2 and n=8 seed-pair values, repeatedly
shuffles the calibration-size labels, and asks how often the shuffled
n=8-minus-n=2 mean gain is at least as large as the observed gain:

For metric \(q\), let \(g_q^{\mathrm{obs}}\) be the observed gain in
Eq. (12). Each permutation \(b \in \{1,\ldots,B\}\) randomly reassigns the
pooled seed-pair values into two groups with the original group sizes and
computes a null gain \(g_{q,b}^{\mathrm{perm}}\). The plus-one Monte-Carlo
p-value is

\[
p_q
=
\frac{
  1 + \sum_{b=1}^{B}
      \mathbf{1}\!\left[g_{q,b}^{\mathrm{perm}}
      \ge g_q^{\mathrm{obs}}\right]
}{
  B+1
}.
\tag{14}
\]

For the three audited metrics, let \(p_{(1)}\le p_{(2)}\le p_{(3)}\) be the
ordered raw p-values. The Holm-adjusted value reported for the \(k\)-th ordered
test is

\[
p^{\mathrm{Holm}}_{(k)}
=
\max_{\ell\le k}
\left\{
  \min\!\left(1,\, (3-\ell+1)\,p_{(\ell)}\right)
\right\}.
\tag{15}
\]

| Metric | Observed gain | Dominance | Raw p | Holm-adjusted p | Extreme null samples |
|---|---:|---:|---:|---:|---:|
| Score/cost Spearman | 0.2920 | 0.9422 | 4.99975e-05 | 0.000149993 | 0 / 20000 |
| Top-20 Jaccard | 0.2651 | 0.9778 | 4.99975e-05 | 0.000149993 | 0 / 20000 |
| Positive-set Jaccard | 0.1797 | 0.9644 | 4.99975e-05 | 0.000149993 | 0 / 20000 |

The plus-one correction prevents zero p-values, and the Holm correction keeps
the three-metric family-wise test explicit. This is still a local null test
over seed-pair metrics; it does not replace broader model families, larger n
grids, or downstream retention experiments.

### 8.7 Rank-Inversion Theory Gate

The rank-inversion theory gate tests the Section 4 variance-over-gap prediction
more directly. It loads the same n=2/4/8 seed artifacts, forms all comparable
module pairs, and measures whether the seed-level ordering disagrees with the
mean ordering:

For seed \(a\), define the empirical pairwise inversion indicator

\[
I^{(a)}_{ij}
=
\mathbf{1}\!\left[
  \operatorname{sign}\!\left(\widehat{r}^{(a)}_i-\widehat{r}^{(a)}_j\right)
  \ne
  \operatorname{sign}\!\left(\overline{r}_i-\overline{r}_j\right)
\right],
\tag{16}
\]

where \(\overline{r}_i\) is the seed-mean score for module \(i\). The reported
mean inversion rate and plug-in bound proxy are

\[
\widehat{\mathcal{I}}_n
=
\frac{1}{|\mathcal{P}_n|\,S}
\sum_{(i,j)\in\mathcal{P}_n}\sum_{a=1}^{S} I^{(a)}_{ij},
\tag{17}
\]

\[
\widehat{\mathcal{B}}_n
=
\frac{1}{|\mathcal{P}_n|}
\sum_{(i,j)\in\mathcal{P}_n}
\min\!\left\{
  1,\,
  \frac{
    \widehat{\operatorname{Var}}(\widehat{r}_i)
    +
    \widehat{\operatorname{Var}}(\widehat{r}_j)
  }{
    (\overline{r}_i-\overline{r}_j)^2+\eta
  }
\right\}.
\tag{18}
\]

Here \(\mathcal{P}_n\) is the set of comparable module pairs at calibration
size \(n\), \(S=6\) prompt seeds in this gate, and \(\eta\) is the same
numerical stabilizer used in Eq. (7).

| Calibration prompts n | Module pairs | Mean inversion | Mean bound proxy | Top-quartile-margin inversion | Top-quartile-margin bound |
|---:|---:|---:|---:|---:|---:|
| 2 | 14193 | 0.2418 | 0.8473 | 0.0969 | 0.5974 |
| 4 | 14168 | 0.2114 | 0.7825 | 0.0774 | 0.4701 |
| 8 | 14043 | 0.1442 | 0.6097 | 0.0427 | 0.2713 |

The monotonic decrease is not claimed as a tight theorem. It is a gated
diagnostic showing that the measured calibration-size curve is consistent with
the Chebyshev-style mechanism: as estimator variance decreases relative to
pairwise margins, fewer module orderings flip across prompt seeds.

### 8.8 Robustness Stress Gate

The robustness stress gate aggregates 11 committed Qwen3/OLMo2/SmolLM2 PPL
summaries under a fixed mixed-precision budget:

| Metric | Value |
|---|---:|
| Wins vs uniform INT4 | 11 / 11 |
| Wins vs best random seed | 11 / 11 |
| Wins vs random-seed mean | 11 / 11 |
| Mean margin vs uniform | +4.2942 PPL |
| Worst margin vs best random | +0.1120 PPL |
| Best-random margin bootstrap 95% CI | [+0.6143, +1.7982] PPL |
| One-sided sign-test p vs best random | 0.000488 |
| Mean FP16 regret | +4.1683 PPL |

The result is strong for the committed short-slice fake-quant setting. It does
not replace official GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant comparisons.

### 8.9 Consensus Transfer Boundary

The paired Qwen3 transfer-boundary gate compares WikiText2-only, C4-only, and
cross-split consensus policies:

| Metric | Value |
|---|---:|
| Cases | 2 |
| Paired slices | 4 |
| Wins vs worse single-split policy | 4 / 4 |
| Wins vs best single-split policy | 2 / 4 |
| Min margin vs worse single | +0.8726 PPL |
| Max regret vs best single | +0.3046 PPL |

This supports a robust-risk framing: consensus is not an oracle, but it reduces
the risk of choosing the worse calibration split.

### 8.10 Interaction-aware Swap Boundary

The interaction gate uses SmolLM2-1.7B search cases on WikiText2 and C4:

| Metric | Value |
|---|---:|
| Search cases | 3 |
| Total swap trials | 16 |
| Improved cases | 1 |
| Improved trials | 5 |
| Locally-negative but globally-improved trials | 5 |
| Max best improvement | +0.0502 PPL |
| Transfer positive rows | 1 / 2 |
| Transfer max regret | 0.0087 PPL |
| Max guard VRAM ratio | 0.8487 |

The best WikiText2-64 swap replaces
`model.layers.12.self_attn.v_proj` with `model.layers.22.self_attn.v_proj`.
Its local proxy gain is negative (`-0.000744`), yet the global PPL improves by
0.0502. This is direct evidence that additive sensitivity ranking misses
allocation interactions.

### 8.11 Packed-system Prototype Evidence

The system side is intentionally scoped. The ESMPQ001 format can package and
audit mixed-bit matrices; Triton shape-family tuning finds selected shape wins;
selected-row and C++ runtime sweeps report module-level wins; shallow fused-QKV
generation and prompt-suite gates verify narrow integration paths. The ledger
records these as executable system evidence, but the paper does not claim
end-to-end quality preservation. It does not claim TTFT/tokens/s wins, real
mobile results, or edge-board deployment.

A new RTX 5070 layout probe further separates storage compression from compute
layout; see `outputs/RTX5070_INT4_LAYOUT_PROBE_2026_06_07.md`. On a 4096 x
4096, batch-512 interleaved timing probe, contiguous packed W4 reaches 0.8424x
torch FP16 latency while preserving about 4x weight-payload compression. A
byte-aligned W4-as-I8 layout reaches 0.9905x torch FP16 with about 2x payload
compression. This does not justify an acceleration claim, but it localizes the
remaining systems bottleneck: packed nibble unpacking and dequantized tile
layout, rather than row-wise dispatch alone, are the next kernel targets.

The follow-up delayed-dequantization probe in
`outputs/RTX5070_INT8_DOT_PROBE_2026_06_07.md` tests the next systems step:
keep the dot product in the integer domain and apply row/activation scales only
after accumulation. On the same 4096 x 4096, batch-512 interleaved setting,
packed W4 weights with per-batch INT8 activations reach 0.292345 ms, or 1.6976x
torch FP16, while retaining about 3.9825x weight-payload compression. A
byte-aligned W4-as-I8 variant reaches 0.153371 ms, or 3.2358x torch FP16, but
only retains about 1.9980x weight-payload compression. This is a W4A8-style
kernel diagnostic rather than an end-to-end model claim: it introduces
activation quantization, and the current evidence does not yet show downstream
quality retention, TTFT/tokens/s wins, mobile performance, or energy savings.
A bounded 4096 x 4096 shape-family follow-up over batch 128/512 and eight
BM/BN/BK configurations keeps this conclusion directionally stable: packed W4
x INT8 activation beats torch FP16 in all eight measured configurations
(1.2900x--1.7268x), while W4-as-I8 x INT8 reaches 1.4886x--3.1372x at lower
static compression. The machine-checkable gate in
`outputs/W4A8_SHAPE_FAMILY_GATE_2026_06_08.md` further records 8/8 valid
configs, packed W4 x INT8 median speedup 1.4490x, constant 3.9825x
weight-payload compression, maximum activation-added rel-L2 0.008702 relative
to packed W4A16, and maximum guard-memory ratio 0.6219.

The synthetic kernel drift is not used as a model-quality proxy. We therefore
add a real-activation reconstruction gate in
`outputs/w4a8_activation_reconstruction_2026_06_08/W4A8_ACTIVATION_RECONSTRUCTION_GATE.md`.
It samples inputs to eight Qwen3-0.6B self-attention projections from the ESMP
package and compares FP activation + ESMP weight against A8 activation + ESMP
weight. The gate passes with median W4A8 output rel-L2 0.123810, p90 W4A8
output rel-L2 0.190244, maximum activation-added rel-L2 0.048561 relative to
W4A16, median activation input rel-L2 0.023349, median compression 7.6411x
versus FP32, and guarded peak GPU memory ratio 0.6841 in the outer process. The
gap between the synthetic 0.008702 drift and the real-activation 0.048561 drift
is reported as an integration-risk measurement rather than hidden: W4A8 has
kernel-level speed evidence, but still needs broader layer coverage and
downstream task retention before it can support an end-to-end quantized LLM
claim.

We then extend the same audit beyond attention-only projections in
`outputs/w4a8_activation_reconstruction_extended_2026_06_08/W4A8_ACTIVATION_RECONSTRUCTION_EXTENDED_GATE.md`.
The extended run covers 24 selected modules from layers 0/7/14/21, including
self-attention and MLP projections. It passes the broader coverage gate with
24/24 modules OK, median W4A8 output rel-L2 0.144851, p90 W4A8 output rel-L2
0.212923, maximum activation-added rel-L2 0.084533 versus W4A16, median
activation input rel-L2 0.035115, median compression 7.6413x versus FP32, and
outer guard peak GPU memory ratio 0.7220. The two largest added-drift cases are
MLP down projections, so this result is not presented as a quality guarantee;
it is the evidence that a future W4A8 runtime needs module-family-aware
activation quantization or a conservative fallback for these layers.

## 9. Discussion

### Why not just use more calibration data?

More calibration data should reduce variance, but calibration data and compute
are themselves constrained in local or edge-oriented workflows. Cross-split
consensus is useful precisely because it exposes disagreement under small
calibration budgets.

### Why random baselines matter

Random baselines are weak, but they are a necessary sanity check. If a
sensitivity heuristic cannot beat budget-matched random allocations, its ranking
signal is not reliable enough to support a method claim.

### Why this is not yet a SOTA quantizer

The current artifact uses fake quantization, short text slices, proxy comparator
families, and prototype runtime gates. A SOTA quantization paper would need
faithful official baselines, larger model scales, downstream capability
benchmarks, and real packed inference measurements.

## 10. Limitations

1. The main quality evidence is short-slice fake-quant PPL, not packed-runtime
   quality.
2. Official GPTQ, AWQ, SmoothQuant, QuaRot, and SpinQuant baselines are not yet
   faithfully reproduced. The baseline dashboard now separates proxy evidence
   from faithful official baseline coverage.
3. Public task evidence is limited local subset coverage, not leaderboard-scale
   capability retention or fused quantized retention.
4. System evidence is prototype/module-level; no Redmi K80 Pro or board-level
   TTFT, tokens/s, memory, energy, or thermal logs are complete.
5. The bit set is limited to `{4,8}` in the main consensus diagnostics; the
   allocation-family proxy also audits `{2,3,4,8}` but remains a proxy.
6. The interaction-aware search is bounded one-step feedback, not a global
   optimization algorithm.

## 11. Conclusion

EigenSkill-Q reframes the project around a measurable quantization problem:
small calibration splits can destabilize module-sensitivity rankings and
therefore destabilize mixed-precision bit allocation. The current artifact
supports a narrow but reviewable claim: cross-split consensus improves the
robustness of short-slice fake-quant allocations over uniform and random
baselines, and global-feedback swap search exposes interaction effects that
additive rankings miss. The next version should replace proxy baselines with
faithful official PTQ comparisons, expand model/task scale, and turn packed
system prototypes into real end-to-end measurements.

## Evidence Appendix

Primary evidence files:

```text
outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md
outputs/CALIBRATION_INSTABILITY_BENCHMARK_2026_06_06.md
outputs/CALIBRATION_ROBUSTNESS_STRESS_GATE_2026_06_07.md
outputs/CONSENSUS_TRANSFER_BOUNDARY_GATE_2026_06_07.md
outputs/INTERACTION_SWAP_BOUNDARY_GATE_2026_06_07.md
outputs/Q_PALETTE_STYLE_ALLOCATION_FAMILY_GATE_2026_06_06.md
outputs/PUBLIC_TASK_MODEL_LADDER_GATE_2026_06_07.md
outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_0P5B_BUNDLE_16_GATE_2026_06_07.md
outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_1P5B_BUNDLE_16_GATE_2026_06_07.md
outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_SUBSET100_MATRIX_2026_06_07.md
outputs/OFFICIAL_PTQ_QWEN25_1P5B_SUBSET100_RUNTIME_PROFILE_2026_06_07.md
outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_GSM8K200_MMLU100_MATRIX_2026_06_08.md
outputs/OFFICIAL_PTQ_QWEN25_1P5B_GSM8K200_MMLU100_RUNTIME_PROFILE_2026_06_08.md
outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_GSM8K200_MMLU100_STATISTICS_2026_06_08.md
outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_0P5B_BUDGET8_16_GATE_2026_06_07.md
outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_1P5B_SMOKE4_GATE_2026_06_08.md
outputs/BASELINE_GAP_DASHBOARD_2026_06_06.md
docs/PAPER_CLAIM_MATRIX.md
docs/SYSTEM_EVIDENCE_GATES.md
docs/SYSTEM_EVIDENCE_RUNBOOK.md
docs/RELATED_WORK_QUANTIZATION_2026.md
```

Verification commands:

```bash
python -m unittest discover -s train_python -p "test_*.py"
python train_python/gate_public_repo_hygiene.py \
  --out-json outputs/real_system_packer_2026-06-05/public_repo_hygiene_gate_2026_06_06.json \
  --out-md outputs/real_system_packer_2026-06-05/PUBLIC_REPO_HYGIENE_GATE_2026_06_06.md
python train_python/build_current_evidence_ledger.py
```

## References

[1] Dettmers et al. LLM.int8(): 8-bit Matrix Multiplication for Transformers at
Scale. arXiv:2208.07339, 2022.

[2] Frantar et al. GPTQ: Accurate Post-Training Quantization for Generative
Pre-trained Transformers. arXiv:2210.17323, 2022.

[3] Xiao et al. SmoothQuant: Accurate and Efficient Post-Training Quantization
for Large Language Models. arXiv:2211.10438, 2022.

[4] Lin et al. AWQ: Activation-aware Weight Quantization for LLM Compression and
Acceleration. arXiv:2306.00978, 2023.

[5] Ashkboos et al. QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs.
arXiv:2404.00456, 2024.

[6] Liu et al. SpinQuant: LLM Quantization with Learned Rotations.
arXiv:2405.16406, 2024.

[7] He et al. Deep Residual Learning for Image Recognition. arXiv:1512.03385,
2015.

[8] See `docs/RELATED_WORK_QUANTIZATION_2026.md` for newer allocation,
calibration-free, rotation, KV-cache, MXFP, and kernel co-design candidates that
are not yet faithful baselines in this repository.
