# A Unified Constraint-Guided Calibration Framework for Robust Mixed-Precision LLM Quantization

Draft date: 2026-06-28

Target route: AAAI / IJCAI / TMLR first, KBS / ESWA as journal backup.

Status: rigorous synthesis draft built from the public `rui4399` repository
portfolio and the local RTX3090 evidence package. This is not a submission-ready
claim of SOTA quantization, production runtime speedup, or mobile deployment.

## Abstract

Mixed-precision post-training quantization (PTQ) relies on calibration data to
decide which modules should retain higher precision under a fixed memory budget.
Existing workflows usually separate sensitivity estimation, precision
allocation, robustness testing, and runtime packaging into loosely connected
steps, which makes allocation decisions vulnerable to calibration-split noise
and difficult to audit. We propose a unified constraint-guided calibration
framework that treats module sensitivity, calibration-split stability, bit-budget
feasibility, and downstream retention as terms in a single decision objective.
The framework converts calibration split instability (CSI) from a diagnostic
into a constraint on mixed-precision allocation: a module should receive higher
precision only when its estimated sensitivity is useful, stable across plausible
calibration subsets, and compatible with the global bit budget. Across the
current EigenSkill-Q evidence line, CSI gates show that prompt-seed stability
improves with calibration size; a strict second-pool SmolLM2-360M run improves
mean score Spearman from 0.3133 at n=4 to 0.6959 at n=16, with passing
trend-significance and null-permutation gates. RTX3090 experiments add guarded
7B FP16/AWQ/GPTQ comparisons and a 14B AWQ feasibility row, while the broader
repository portfolio separates calibration robustness, benchmark tooling,
packed-runtime evidence, deterministic bypass, and vision-level edge-swarm
ideas into claim-safe tracks. The resulting paper contribution is not a new
standalone quantizer; it is a mathematically unified, auditable framework for
deciding when calibration-driven mixed-precision allocation is supported, when
it is unstable, and which evidence is still required before claiming quality or
systems superiority.

## 1. Introduction

Low-bit PTQ is one of the most practical ways to deploy large language models
under memory and bandwidth constraints. Uniform quantization is simple, but it
spends the same number of bits on modules that may have very different
sensitivity to quantization error. Mixed-precision quantization addresses this
by reserving higher precision for selected modules and using lower precision
elsewhere. The central question is therefore not merely how to quantize a model,
but how to decide which modules deserve scarce high-bit budget.

Most sensitivity-guided PTQ pipelines estimate module importance on a small
calibration set, rank modules, and allocate high precision to the apparently
most sensitive ones. This decomposition is convenient, but it hides a critical
failure mode: a small calibration sample may be an unstable basis for ranking.
If two equally plausible calibration splits produce different sensitivity
orders, a single-split allocation can appear principled while encoding
calibration noise. The problem becomes more serious when the paper also mixes
allocation heuristics, runtime kernels, and deterministic bypass components
without a single objective tying them together.

This paper reframes the EigenSkill-Q evidence line as a unified
constraint-guided calibration framework. Instead of presenting CSI metrics,
allocation rules, task retention, and runtime artifacts as disconnected modules,
we formulate them as coupled constraints on one allocation decision. The
framework asks whether a high-bit assignment is sensitive, stable, budget-valid,
and empirically retained. Runtime packaging and deterministic bypass remain
separate artifact tracks unless they satisfy their own evidence gates.

The public `rui4399` GitHub portfolio supports this separation. The integration
repository `eigenskill-research-pack` stores historical evidence. The
`eigenskill-q-calibration-robustness` repository defines the main
calibration-robustness paper track. The `csi-benchmark-suite` repository
extracts metrics and schemas. The `eigenskill-esmp-runtime` repository isolates
packed mixed-bit runtime evidence. The `hybridskill-bypass-runtime` repository
studies deterministic delegation for strict low-entropy tasks. The
`eigenswarm-vision` repository is deliberately a vision-paper track, not a
completed empirical result. This portfolio split is a strength only if the main
paper keeps one learning objective and one claim boundary.

### Contributions

1. We propose a unified constraint-guided formulation for mixed-precision
   calibration, combining sensitivity, calibration stability, bit-budget
   feasibility, and retention evidence in one allocation objective.
2. We formalize calibration split instability as a constraint, not only a
   post-hoc diagnostic, using rank agreement, top-k set overlap, positive-set
   overlap, bootstrap trend checks, and permutation-null tests.
3. We synthesize the current EigenSkill-Q and RTX3090 evidence into a
   reviewer-facing experimental matrix while explicitly separating completed
   results from required AAAI/KBS baselines.
4. We define an ablation and baseline protocol that can falsify the framework:
   removing stability, budget, consensus, or retention constraints must degrade
   allocation reliability, and strong PTQ baselines must be confronted directly
   before any SOTA claim is made.

## 2. Problem Formulation

Let a transformer model contain quantizable modules
\(\mathcal{M}=\{m_1,\ldots,m_L\}\). Let \(b_i \in \mathcal{B}\) denote the bit
assignment for module \(m_i\), where \(\mathcal{B}\) may be \(\{4,8\}\) in the
current artifacts. Let \(a=(b_1,\ldots,b_L)\) be a mixed-precision allocation.
Let \(C=\{C_1,\ldots,C_S\}\) be a set of calibration splits sampled from a prompt
pool, and let \(D\) be the downstream evaluation distribution.

The allocation problem is:

\[
\min_{a \in \mathcal{A}} \quad
\mathcal{J}(a)
=
\mathcal{L}_{ret}(a;D)
+ \lambda_s \mathcal{R}_{stab}(a;C)
+ \lambda_b \mathcal{R}_{budget}(a)
+ \lambda_u \mathcal{R}_{uncert}(a;C),
\]

subject to:

\[
\frac{1}{L}\sum_{i=1}^{L} b_i \leq B,\quad b_i \in \mathcal{B}.
\]

Here \(\mathcal{L}_{ret}\) measures downstream quality loss relative to the
unquantized or native baseline path, \(\mathcal{R}_{stab}\) penalizes decisions
whose supporting sensitivity estimates are unstable across calibration splits,
\(\mathcal{R}_{budget}\) enforces the memory/bit budget, and
\(\mathcal{R}_{uncert}\) penalizes allocations driven by high-variance or
low-margin rankings.

The present evidence does not fully optimize this objective end to end. It
instantiates the components as executable gates: sensitivity measurement,
seed-stability testing, CSI-vs-n trends, permutation-null checks, and matched
task/PPL probes. This distinction matters. The current paper can claim a
unified framework and a reproducible partial instantiation; it cannot yet claim
that the final objective beats all official PTQ methods at scale.

## 3. Method

### 3.1 Split-Conditioned Sensitivity Estimation

For each calibration split \(C_s\), we estimate a per-module sensitivity score
\(\hat{\Delta}_{i,s}\), such as the change in negative log-likelihood when
module \(m_i\) is quantized under a probe bit width. This produces a score
matrix:

\[
\hat{\Delta} \in \mathbb{R}^{L \times S}.
\]

A naive allocation uses one column of this matrix. The unified framework instead
uses the distribution across splits. A module is considered reliable only when
its sensitivity is both large and stable:

\[
q_i = \mu_i - \alpha \sigma_i,
\quad
\mu_i = \frac{1}{S}\sum_{s=1}^{S}\hat{\Delta}_{i,s},
\quad
\sigma_i^2 = \frac{1}{S-1}\sum_{s=1}^{S}(\hat{\Delta}_{i,s}-\mu_i)^2.
\]

This confidence-adjusted score is one concrete estimator. Other robust
estimators, such as trimmed means, median-of-means, or interaction-aware swap
scores, can be substituted under the same objective.

### 3.2 Calibration Split Instability Constraint

CSI measures whether calibration splits agree about the sensitivity ordering.
For every pair of splits \((s,t)\), the current artifacts compute:

- Spearman correlation between module scores;
- top-k Jaccard overlap between the most sensitive modules;
- positive-set Jaccard overlap for modules with positive measured loss impact.

Let \(G(C)\) be an aggregate stability score over all split pairs. A robust
allocation should satisfy:

\[
G(C) \geq \tau,
\]

or else report that the allocation is under-supported by calibration evidence.
The strict second-pool RTX3090 closure gives a concrete example: with
SmolLM2-360M, mean score Spearman increases from 0.3133 at n=4 to 0.4136 at n=8
and 0.6959 at n=16, and the CSI trend/null gates pass. This supports the
claim that larger calibration samples improve ranking stability in that
measured setting.

### 3.3 Budget-Constrained Allocation

Given robust scores \(q_i\), the allocation module chooses high-bit modules
under an average-bit or memory budget:

\[
\max_{z_i \in \{0,1\}} \sum_i z_i q_i
\quad \text{s.t.} \quad
\sum_i \mathrm{cost}(z_i) \leq B.
\]

Here \(z_i=1\) can denote assigning module \(m_i\) to 8-bit rather than 4-bit.
This is a knapsack-style subproblem, not a separate model. It is the optimizer
for the unified objective after stability-adjusted scores have been estimated.

### 3.4 Retention and Runtime Evidence Gates

An allocation should not be promoted from diagnostic to method claim unless it
is evaluated against downstream and native PTQ baselines. The current evidence
contains guarded FP16/AWQ/GPTQ task comparisons, including RTX3090 7B MMLU/GSM8K
rows and a 14B AWQ feasibility smoke. These are valuable system feasibility and
comparison rows, but they are not yet sufficient to claim broad SOTA retention.

Runtime artifacts such as ESMP packed kernels are treated as separate evidence
gates. They can support future systems claims only when they show end-to-end
TTFT, tokens/s, memory, and file-size advantages against strong baselines. Until
then, they should remain appendix or separate-track material.

## 4. Repository-Level Evidence Synthesis

The public GitHub portfolio contains thirteen visible repositories. A strict
paper synthesis should not treat all of them as contributions to one method.
Instead, the portfolio should be read as a layered evidence stack: three
repositories form the quantization paper core, three repositories define
adjacent research boundaries, one repository is the broader agent platform, four
repositories document skill/workflow process, and one repository is unrelated to
the PTQ claim.

| Track | Repository | Role in this paper |
|---|---|---|
| Integration evidence | `rui4399/eigenskill-research-pack` | Historical evidence ledger, local RTX3090 package, and paper-draft anchor |
| Main method | `rui4399/eigenskill-q-calibration-robustness` | Primary CSI and robust allocation artifact |
| Benchmark/protocol | `rui4399/csi-benchmark-suite` | Reusable metrics, schemas, null tests, and gates |
| Runtime systems | `rui4399/eigenskill-esmp-runtime` | Separate packed mixed-bit runtime evidence; not a quality claim |
| Deterministic routing | `rui4399/hybridskill-bypass-runtime` | Separate exact-task delegation line; not a PTQ claim |
| Vision architecture | `rui4399/eigenswarm-vision` | Future position-paper material only |
| Agent skills platform | `rui4399/Rui` | Tooling ecosystem; not paper evidence |
| Research planning | `rui4399/rui-research-writing-roadmap` | Writing/process support; can inform milestone discipline but not method novelty |
| Visual QA process | `rui4399/rui-code-visual-qa` | Engineering QA skill; not experimental evidence |
| Delivery QA process | `rui4399/rui-delivery-bridge-qa` | Delivery/release workflow; not experimental evidence |
| Skill authoring | `rui4399/rui-skill-authoring-lab` | Reusable agent-skill development; not experimental evidence |
| Agent operations | `rui4399/rui-agent-ops-runbooks` | Operational runbooks; not experimental evidence |
| Game optimization | `rui4399/game-reshade-optimizer` | Unrelated workflow artifact |

The synthesis rule is strict: the AAAI/KBS paper should include only the first
three tracks as main evidence. ESMP, HybridSkill, and EigenSwarm can motivate a
larger research program, but including them as core contributions would recreate
the "hybrid system without unified learning theory" failure mode.

This portfolio-level reading also changes the paper framing. The central paper
should not be "EigenSkill as a universal agent platform." That claim is too
broad and would collapse unrelated artifacts into one story. The defensible
paper is narrower and stronger: calibration-driven mixed-precision quantization
needs a unified objective that connects sensitivity, split-stability, global
budget, and retention. The non-core repositories remain useful because they
show engineering maturity, reproducibility habits, and future deployment
directions, but they must stay outside the main empirical claim unless they add
direct evidence for that objective.

## 5. Experimental Protocol

### 5.1 Completed Evidence To Report

The current paper can report the following completed evidence:

1. CSI seed-stability curves from the original Qwen2.5 artifacts, including
   n=2/4/8 Qwen2.5-1.5B reprise gates.
2. Strict second-pool SmolLM2-360M n=4/8/16 closure with 6 seeds per calibration
   size and 225/225 Linear modules measured per seed.
3. RTX3090 7B FP16/AWQ/GPTQ comparisons on MMLU and GSM8K at 25/100 examples.
4. RTX3090 Qwen2.5-14B-AWQ 10-example MMLU feasibility smoke.
5. Quant-skill deterministic bypass and LoRA smoke as boundary evidence for the
   separate HybridSkill line, not as the main quantization method.

### 5.2 Required Baselines Before AAAI Submission

The paper should not claim AAAI-level method superiority until it includes:

| Family | Required baselines | Current status |
|---|---|---|
| Native PTQ | FP16, uniform W4, AutoAWQ W4/G128, GPTQModel W4/G128 | partially measured; needs direct CSI-allocation row |
| Calibration-aware PTQ | SmoothQuant, OmniQuant or equivalent official/fair implementation | not complete |
| Rotation/outlier methods | QuaRot or SpinQuant family baseline | not complete |
| Allocation heuristics | random budget-matched, single-split top-k, mean consensus, confidence-adjusted consensus | partially measured in existing gates |
| Runtime | FP16 loader, AWQ/GPTQ loader, ESMP packed path if claimed | ESMP not ready for main speed claim |

### 5.3 Ablation Design

The unified objective must be falsified through ablations:

| Variant | Removed term | Expected failure mode |
|---|---|---|
| Full framework | none | best stability/retention trade-off |
| No stability constraint | \(\mathcal{R}_{stab}\) | split-sensitive allocations |
| No uncertainty penalty | \(\mathcal{R}_{uncert}\) | overconfident low-margin rankings |
| No budget optimization | \(\mathcal{R}_{budget}\) / knapsack step | invalid or inefficient bit use |
| Single split only | cross-split aggregation | high variance across prompt seeds |
| Runtime-only promotion | retention gates | speed evidence detached from quality |

### 5.4 Reporting Format

Every benchmark table should report:

- model family and size;
- calibration prompt source and n;
- number of seeds;
- quantization backend;
- task/PPL fixture;
- accuracy or PPL with confidence intervals;
- peak VRAM, TTFT, tokens/s when runtime is discussed;
- win/loss and average rank across datasets;
- exact artifact paths.

## 6. Results Summary From Current Evidence

The strictest new result is the second-pool CSI closure. For SmolLM2-360M:

| n | Seeds | Mean Spearman | Top-20 Jaccard | Positive-set Jaccard | Gate |
|---:|---:|---:|---:|---:|---|
| 4 | 6 | 0.3133 | 0.3779 | 0.5390 | PASS |
| 8 | 6 | 0.4136 | 0.4363 | 0.5991 | PASS |
| 16 | 6 | 0.6959 | 0.5761 | 0.7512 | PASS |

The CSI-vs-n curve passes monotonicity checks. The trend-significance gate
passes with minimum full-range gain lower bound 0.1395 and minimum dominance
probability 0.9644. The null-permutation gate passes with maximum
Holm-adjusted p-value 0.0005999.

The RTX3090 comparison rows show feasibility at larger local scale but do not
yet prove method superiority. On Qwen2.5-7B-Instruct, the 100-example MMLU slice
reports FP16/AWQ/GPTQ accuracies of 0.71/0.70/0.74, while the 100-example GSM8K
slice reports 0.24/0.24/0.16. Qwen2.5-14B-AWQ completes a 10-example MMLU smoke
with 0.50 accuracy and 3.851 mean generated tokens/s. These rows support local
RTX3090 feasibility and comparison, not broad leaderboard claims.

## 7. Why The Framework Can Work

The mechanism is not that several heuristics are assembled. The mechanism is
that the allocation decision is constrained by independent evidence about
sensitivity, stability, budget, and retention.

First, stability constraints reduce calibration overfitting. A module that
appears sensitive in one small prompt sample but disappears under another should
not dominate a high-bit budget. Second, confidence-adjusted aggregation reduces
rank variance by rewarding modules with both high mean sensitivity and low
split variance. Third, the budget constraint prevents the method from hiding
behind unconstrained high precision. Fourth, downstream retention gates prevent
the CSI score from becoming a self-contained metric with no task consequence.

This gives reviewers a falsifiable story: if stability does not improve with
calibration size, if confidence-adjusted allocation does not beat single-split
allocation, or if downstream retention is insensitive to CSI, the framework
loses its central claim.

## 8. Related Work Positioning

The method should be positioned beside calibration-aware PTQ and robust
evaluation work. GPTQ, AWQ, SmoothQuant, OmniQuant, QuaRot, and SpinQuant are
not strawman baselines; they are the methods that must be confronted before any
quality claim is promoted. The current contribution is complementary: it asks
whether the calibration evidence used to drive allocation is stable enough to
trust, and how that stability should constrain the allocation objective.

The CSI benchmark-suite track supports the measurement side of this claim. The
ESMP runtime track supports a future systems paper only if end-to-end runtime
evidence closes. The HybridSkill bypass track is a separate negative/edge-AI
line about deterministic delegation and should not be used as proof of
quantization quality.

## 9. Threats To Validity

The current evidence is still limited in several ways. First, many rows are
local guarded subsets rather than full benchmark submissions. Second, the
second-pool n=4/8/16 closure uses SmolLM2-360M; larger model families need the
same strict second-pool treatment. Third, official SmoothQuant and
rotation-family baselines are not yet complete. Fourth, ESMP runtime evidence
does not yet support an end-to-end acceleration claim. Fifth, deterministic
bypass results belong to a different task family and should not be merged into
the PTQ method claim.

These limitations do not invalidate the framework, but they determine the venue
position. The paper is currently a strong KBS/ESWA-style framework and evidence
synthesis candidate, and an AAAI candidate only after direct CSI-allocation
retention baselines and stronger official PTQ comparisons are added.

## 10. Conclusion

This draft reframes EigenSkill-Q as a unified constraint-guided calibration
framework rather than a collection of heuristics. The key move is to make
calibration stability a first-class constraint on mixed-precision allocation.
The current evidence shows that calibration-size increases can improve
split-stability and that the measurement/gating infrastructure is reproducible
across local RTX3090 experiments. The remaining AAAI-critical step is to show
that allocations selected under this unified objective improve or preserve
downstream retention against strong native PTQ and calibration-aware baselines.
Until that evidence exists, the correct claim is disciplined but valuable:
calibration-driven mixed-precision quantization needs auditable stability
constraints, and the EigenSkill-Q portfolio provides a concrete framework for
measuring and enforcing them.

## Reviewer-Facing Claim Boundary

Safe claims:

- The framework unifies sensitivity, stability, budget, and retention evidence
  into a single allocation objective.
- CSI can be measured with reproducible seed-stability, trend, and
  permutation-null gates.
- Current artifacts show monotonic stability gains with larger calibration size
  in the measured Qwen2.5 and SmolLM2 settings.
- RTX3090 evidence supports local feasibility and guarded comparisons for the
  exact measured models and tasks.

Unsafe claims:

- The method is SOTA PTQ.
- ESMP currently accelerates end-to-end LLM inference.
- Deterministic bypass proves quantization quality.
- EigenSwarm is implemented.
- Results generalize to all models, tasks, or calibration distributions.

## Evidence Pointers

- Main integration repo:
  <https://github.com/rui4399/eigenskill-research-pack>
- Calibration robustness repo:
  <https://github.com/rui4399/eigenskill-q-calibration-robustness>
- CSI benchmark suite:
  <https://github.com/rui4399/csi-benchmark-suite>
- ESMP runtime boundary:
  <https://github.com/rui4399/eigenskill-esmp-runtime>
- Hybrid bypass boundary:
  <https://github.com/rui4399/hybridskill-bypass-runtime>
- Vision boundary:
  <https://github.com/rui4399/eigenswarm-vision>
- Agent platform boundary:
  <https://github.com/rui4399/Rui>
- Research writing/process boundary:
  <https://github.com/rui4399/rui-research-writing-roadmap>
- Code visual QA process boundary:
  <https://github.com/rui4399/rui-code-visual-qa>
- Delivery bridge QA process boundary:
  <https://github.com/rui4399/rui-delivery-bridge-qa>
- Skill authoring process boundary:
  <https://github.com/rui4399/rui-skill-authoring-lab>
- Agent operations process boundary:
  <https://github.com/rui4399/rui-agent-ops-runbooks>
- Unrelated game optimization artifact:
  <https://github.com/rui4399/game-reshade-optimizer>
- Local report:
  `outputs/RTX3090_EXPERIMENT_REPORT_2026_06_16.md`
- Local completion audit:
  `outputs/RTX3090_COMPLETION_AUDIT_2026_06_16.md`
