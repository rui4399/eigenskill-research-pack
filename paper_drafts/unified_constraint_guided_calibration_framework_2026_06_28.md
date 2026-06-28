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

## 2. Unified Mathematical Formulation

Let a transformer model contain quantizable modules
\(\mathcal{M}=\{m_1,\ldots,m_L\}\). For each module \(m_i\), let
\(b_i \in \mathcal{B}\) be its assigned bit width and let
\(a=(b_1,\ldots,b_L)\) denote a complete mixed-precision allocation. The
current artifacts mostly instantiate \(\mathcal{B}=\{4,8\}\), but the
formulation allows any finite bit set. Let \(C=\{C_1,\ldots,C_S\}\) be
calibration splits sampled from a prompt pool, and let \(D\) be the downstream
evaluation distribution.

We formulate mixed-precision allocation as one constrained learning problem:

\[
\begin{aligned}
\min_{a \in \mathcal{B}^L} \quad
\mathcal{J}(a)
&= \mathcal{L}_{task}(a;D)
+ \lambda_c \mathcal{L}_{cal}(a;C)
+ \lambda_s \mathcal{R}_{stab}(a;C)
+ \lambda_u \mathcal{R}_{uncert}(a;C) \\
&\quad + \lambda_b \mathcal{R}_{budget}(a) \\
\text{s.t.} \quad
&\sum_{i=1}^{L} \mathrm{mem}(m_i,b_i) \leq M, \\
&\mathcal{G}_{stab}(a;C) \geq \tau_s, \\
&\mathcal{G}_{ret}(a;D_{val}) \geq \tau_r.
\end{aligned}
\]

Here \(\mathcal{L}_{task}\) is downstream retention loss relative to an
unquantized or native PTQ reference, \(\mathcal{L}_{cal}\) is calibration loss
estimated on prompt splits, \(\mathcal{R}_{stab}\) penalizes allocations whose
supporting sensitivity evidence changes across splits, \(\mathcal{R}_{uncert}\)
penalizes high-variance or low-margin sensitivity ranks, and
\(\mathcal{R}_{budget}\) penalizes memory-budget violation or inefficient use of
high precision. The two gates \(\mathcal{G}_{stab}\) and \(\mathcal{G}_{ret}\)
are reviewer-facing constraints: an allocation is not promoted to a method claim
unless calibration stability and downstream retention exceed predeclared
thresholds.

This turns the earlier multi-module language into a single objective. Former
component names are not independent contributions in this formulation.
They become terms and operators inside \(\mathcal{J}\): split-conditioned
inference estimates \(\mathcal{L}_{cal}\), stability constraints define
\(\mathcal{R}_{stab}\), allocation search optimizes \(\mathcal{R}_{budget}\), and
adaptive weighting appears only through the coefficients or confidence scores
used inside the same objective.

A Lagrangian form makes the coupling explicit:

\[
\mathcal{L}_{lag}(a,\eta_s,\eta_r)
= \mathcal{J}(a)
+ \eta_s \max(0,\tau_s-\mathcal{G}_{stab}(a;C))
+ \eta_r \max(0,\tau_r-\mathcal{G}_{ret}(a;D_{val})).
\]

This is the mathematical claim reviewers can test. The current evidence does
not fully optimize this objective end to end. It provides a partial but
auditable instantiation: sensitivity measurement, seed-stability testing,
CSI-vs-n trend gates, permutation-null checks, and guarded downstream probes.
The resulting claim is a unified constrained framework plus verified
components, not broad SOTA quantization.

## 3. Method: One Objective, Three Operators

The method consists of operators that estimate or optimize the
single objective above, rather than three standalone modules.

### 3.1 Split-Conditioned Calibration Estimator

For each calibration split \(C_s\), estimate the loss impact of assigning a
module to a lower precision:

\[
\hat{\Delta}_{i,s}
= \ell(f_{a^{(i\downarrow)}};C_s)-\ell(f_{a^{ref}};C_s),
\]

where \(a^{ref}\) is a reference allocation and \(a^{(i\downarrow)}\) is the
allocation with module \(m_i\) quantized under the probe setting. This produces
\(\hat{\Delta} \in \mathbb{R}^{L\times S}\). A single-split method would choose
high-bit modules from one column of this matrix. The unified estimator instead
uses cross-split evidence:

\[
\mu_i = \frac{1}{S}\sum_{s=1}^{S}\hat{\Delta}_{i,s},
\qquad
\sigma_i^2 = \frac{1}{S-1}\sum_{s=1}^{S}(\hat{\Delta}_{i,s}-\mu_i)^2,
\]

\[
q_i = \mu_i - \alpha\sigma_i - \beta\,\mathrm{margin}^{-1}_i.
\]

The score \(q_i\) is not a separate heuristic. It is a surrogate for the part of
\(\mathcal{J}\) that combines calibration loss, instability, and uncertainty.
Large \(\mu_i\) favors protecting sensitive modules; large \(\sigma_i\) or small
rank margin reduces confidence.

### 3.2 CSI as a Constraint, Not a Diagnostic

Calibration Split Instability (CSI) is used to constrain allocation evidence.
For each pair of splits \((s,t)\), compute rank and set agreement metrics:

\[
\rho_{s,t}=\mathrm{Spearman}(\hat{\Delta}_{:,s},\hat{\Delta}_{:,t}),
\]

\[
J^k_{s,t}=\frac{|\mathrm{TopK}(s)\cap\mathrm{TopK}(t)|}
{|\mathrm{TopK}(s)\cup\mathrm{TopK}(t)|}.
\]

The stability gate aggregates these values:

\[
\mathcal{G}_{stab}(a;C)
= w_\rho \, \overline{\rho}
+ w_k \, \overline{J^k}
+ w_p \, \overline{J^{pos}}.
\]

The allocation is claim-eligible only if \(\mathcal{G}_{stab}(a;C)\geq\tau_s\).
Otherwise the correct output is not a new mixed-precision model; it is a
negative audit result saying that the calibration evidence is under-supported.
The strict second-pool RTX3090 closure is a concrete measurement of this gate:
with SmolLM2-360M, mean score Spearman increases from 0.3133 at n=4 to 0.4136
at n=8 and 0.6959 at n=16, and the CSI trend/null gates pass.

### 3.3 Budget-Constrained Allocation Operator

Given \(q_i\), the allocation step solves a discrete constrained optimization
problem:

\[
\max_{z_i\in\{0,1\}} \sum_i z_i q_i
\quad
\text{s.t.}\quad
\sum_i \left[\mathrm{mem}(m_i,b_H)-\mathrm{mem}(m_i,b_L)\right]z_i
\leq M-M_L.
\]

Here \(z_i=1\) means module \(m_i\) is assigned the higher bit width \(b_H\)
instead of the lower bit width \(b_L\), and \(M_L\) is the memory use of the
all-low-bit allocation. This can be solved by dynamic programming, greedy
budgeted ranking, or beam search, but the solver is not the contribution. The
contribution is that the solver optimizes a stability-adjusted surrogate of the
single objective rather than a one-split sensitivity list.

### 3.4 Retention Gate and Claim Promotion

The downstream gate tests whether the selected allocation preserves task quality
relative to baselines:

\[
\mathcal{G}_{ret}(a;D_{val})
= \mathrm{Perf}(f_a,D_{val}) - \mathrm{Perf}(f_{base},D_{val}).
\]

The baseline \(f_{base}\) must be chosen according to the claim. If the claim is
"better than uniform W4," the baseline can be uniform W4. If the claim is SOTA
PTQ, the baseline must include official or fair AWQ, GPTQ, SmoothQuant,
OmniQuant, and rotation-family methods. The current RTX3090 FP16/AWQ/GPTQ rows
support feasibility and guarded comparison only. They do not yet satisfy the
full SOTA gate.

Runtime artifacts such as ESMP packed kernels remain separate evidence gates.
They can support a future systems claim only when end-to-end TTFT, tokens/s,
VRAM, file size, and retention improve under the same allocation. Without that
coupled evidence, runtime speed is not evidence for the calibration framework.

## 4. Repository-Level Evidence Synthesis

The public GitHub portfolio contains thirteen visible repositories. A strict
paper synthesis does not treat all of them as contributions to one method.
Instead, the portfolio is read as a layered evidence stack: three
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

The synthesis rule is strict: the AAAI/KBS paper includes only the first
three tracks as main evidence. ESMP, HybridSkill, and EigenSwarm can motivate a
larger research program, but including them as core contributions would recreate
the "hybrid system without unified learning theory" failure mode.

This portfolio-level reading also changes the paper framing. The central paper
is not "EigenSkill as a universal agent platform." That claim is too
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

AAAI-level method superiority requires the following baseline coverage:

| Family | Required baselines | Current status |
|---|---|---|
| Native PTQ | FP16, uniform W4, AutoAWQ W4/G128, GPTQModel W4/G128 | partially measured; needs direct CSI-allocation row |
| Calibration-aware PTQ | SmoothQuant, OmniQuant or equivalent official/fair implementation | not complete |
| Rotation/outlier methods | QuaRot or SpinQuant family baseline | not complete |
| Allocation heuristics | random budget-matched, single-split top-k, mean consensus, confidence-adjusted consensus | partially measured in existing gates |
| Runtime | FP16 loader, AWQ/GPTQ loader, ESMP packed path if claimed | ESMP not ready for main speed claim |

### 5.3 Objective-Aligned Ablation Design

The ablation table must map directly onto the unified objective. Each row removes
one term, gate, or operator from \(\mathcal{J}\) and tests whether the predicted
failure appears. This is the key difference between a unified framework paper
and a renamed hybrid-system paper.

| Variant | Objective change | Test statistic | Expected failure mode |
|---|---|---|---|
| Full framework | all terms and gates active | retention, CSI, memory, average rank | best feasible stability/retention trade-off |
| No calibration term | remove \(\mathcal{L}_{cal}\) from scoring | downstream retention vs budget | allocation no longer tracks measured module sensitivity |
| No stability regularizer | set \(\lambda_s=0\), remove \(\mathcal{G}_{stab}\) gate | seed-to-seed rank variance, CSI fail rate | split-sensitive allocations |
| No uncertainty penalty | set \(\lambda_u=0\) | low-margin module flips, confidence interval width | overconfident low-margin rankings |
| No budget regularizer | set \(\lambda_b=0\) or relax memory constraint | memory, average bits, invalid allocations | quality gains come from extra precision rather than better allocation |
| Single split only | set \(S=1\), no cross-split aggregation | variance across prompt seeds | high prompt-seed dependence |
| Mean-only consensus | use \(q_i=\mu_i\) | CSI and downstream retention | instability remains hidden by averaging |
| No retention gate | remove \(\mathcal{G}_{ret}\) | task/PPL regression frequency | stable rankings do not necessarily preserve task quality |
| Runtime-only promotion | report speed without retention coupling | speed/quality Pareto | systems evidence detached from model quality |

A result table reports not only whether the full method wins, but why it
wins. A competitive AAAI version shows that the full objective improves the
Pareto frontier of retention, stability, and memory against single-split,
mean-only, random budget-matched, and native PTQ baselines.

### 5.4 Reporting Format

Every benchmark table reports:

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
appears sensitive in one small prompt sample but disappears under another does
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

The method is positioned beside calibration-aware PTQ and robust
evaluation work. GPTQ, AWQ, SmoothQuant, OmniQuant, QuaRot, and SpinQuant are
not strawman baselines; they are the methods that must be confronted before any
quality claim is promoted. The current contribution is complementary: it asks
whether the calibration evidence used to drive allocation is stable enough to
trust, and how that stability constrains the allocation objective.

The CSI benchmark-suite track supports the measurement side of this claim. The
ESMP runtime track supports a future systems paper only if end-to-end runtime
evidence closes. The HybridSkill bypass track is a separate negative/edge-AI
line about deterministic delegation and is not used as proof of
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
