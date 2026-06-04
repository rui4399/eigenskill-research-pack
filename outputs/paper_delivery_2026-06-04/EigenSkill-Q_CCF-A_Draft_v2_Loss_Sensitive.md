# EigenSkill-Q: Loss-Sensitive Constrained Mixed-Precision Allocation for Verifiable LLM Quantization Control

**Manuscript draft v2.**  
Date: 2026-06-04  
Target posture: ICML / IJCAI / AAAI style research draft.  
Status: stronger than the first draft, but not yet submission-ready because
GPTQ/AWQ/SmoothQuant/rotation baselines and real compressed-runtime measurements
are still missing.

## Abstract

Mixed-precision quantization is a constrained decision problem: each module must
choose a numerical format under memory, latency, and quality constraints. Many
current workflows rely on heuristic layer statistics or offline quantization
pipelines, while LLM-agent systems sometimes ask a small model to emit structured
quantization decisions directly. Both routes are fragile: cheap activation
proxies can mis-rank modules, and language-model generation is unreliable for
low-entropy numerical policies.

We propose **EigenSkill-Q**, a verifiable policy-control framework for LLM
quantization. The framework separates semantic routing from numerical policy
execution. Quantization choices are formulated as constrained optimization or
constrained contextual bandits, while safety-critical low-entropy decisions are
executed by deterministic policy kernels. As a concrete first step, we study
loss-sensitive `{4,8}` mixed-precision weight allocation. For each Linear module,
we quantize only that module, measure the resulting calibration loss increase,
restore the original weight, and allocate 8-bit precision to modules with the
largest loss increase per parameter cost under a 4.5 weighted-average-bit budget.

On `HuggingFaceTB/SmolLM2-360M-Instruct`, this direct perturbation signal
outperforms both uniform INT4 and an activation-statistic rate-distortion proxy
in a simple group-wise fake-quantization scaffold. On an 8-prompt diagnostic set,
PPL improves from `272.18` under uniform INT4 to `212.69` under loss-sensitive
4/8 allocation. On WikiText2 validation slices, the same allocation improves PPL
from `30.26` to `25.92` on 32 prompts and from `27.82` to `24.14` on 128 prompts,
slightly outperforming the activation-statistic RD allocation in both cases.
An additional one-step interaction-aware swap search further improves
WikiText2-128 PPL from `24.14` to `24.07`. On a streamed C4 validation slice,
the same ordering holds, with PPL improving from uniform INT4 `36.94` to
loss-sensitive `32.77` and swap-search `32.57`. These results do not claim production
quantization superiority; they establish a measurable direction for learning-
and optimization-guided policy control.

## 1. Introduction

Post-training quantization has become a core mechanism for serving LLMs under
resource constraints. The practical problem is not simply "choose INT4". Modern
systems must decide which modules keep more precision, which activations require
outlier protection, whether rotations or smoothing are needed, whether residual
correction is worth its cost, and how KV-cache formats should adapt to context
length.

These decisions are structured numerical policies. They have schemas,
constraints, and measurable consequences. A language model may be useful for
semantic routing or explanation, but it is a poor final executor for deterministic
threshold logic, bit budgets, and safety-critical policy fields. This motivates
the core EigenSkill-Q principle:

```text
Use learned models to recognize and adapt policy context.
Use verifiable kernels to execute low-entropy numerical decisions.
```

The first EigenSkill draft overreached by connecting this idea to speculative
edge/swarm/eigen-routing claims. This v2 draft narrows the contribution to a
publishable machine-learning problem: **loss-sensitive constrained
mixed-precision allocation with verifiable policy execution**.

## 2. Problem Formulation

Consider a transformer with quantizable modules indexed by `i = 1, ..., n`.
Each module has weight tensor `W_i`, calibration data `D_cal`, and parameter
cost `c_i`. A mixed-precision policy chooses bit width `b_i` from a discrete set
`B`, such as `{4, 8}`:

```text
pi = (b_1, ..., b_n),      b_i in B.
```

Let `Q_i(W_i; b_i)` denote the quantized-dequantized operator used for fake
quantization diagnostics, and let `L(pi; D_cal)` be next-token negative
log-likelihood after applying the allocation. A constrained allocation objective
is:

```text
minimize_pi   L(pi; D_cal)
subject to    sum_i c_i b_i <= B_mem
              b_i in B.
```

For a broader quantization policy, the action can also include rotations,
outlier protection, residual rank, and KV-cache format:

```text
a_i = (b_i, R_i, o_i, r_i, k_i).
```

Then the objective becomes:

```text
minimize    sum_i D_i(W_i, A_i, a_i) + alpha C_i(a_i)
subject to  sum_i M_i(a_i) <= B_mem
            sum_i T_i(a_i) <= B_lat
            Risk_i(a_i) <= epsilon_i.
```

`D_i` may be measured loss increase, activation reconstruction error, output KL,
or a Fisher/Hessian-weighted proxy. `C_i`, `M_i`, and `T_i` capture algorithmic
and hardware costs.

For interaction-aware allocation, the global quality objective can be decomposed
as:

```text
L(pi) - L(pi_0)
  = sum_i g_i(b_i)
    + sum_{i<j} h_ij(b_i, b_j)
    + R_high(pi),
```

where `g_i` is the local one-module perturbation term, `h_ij` captures pairwise
module interaction, and `R_high` contains higher-order effects. The current
loss-sensitive allocator estimates only `g_i`; the swap-search experiment is a
minimal global-feedback correction that tests whether interaction terms can be
exploited under the same bit budget.

## 3. Loss-Sensitive Module Scoring

The activation-statistic proxy used in the first scaffold estimates sensitivity
from input magnitude, variance, and outlier ratios. This is cheap but indirect.
The v2 method measures a direct perturbation signal:

```text
s_i = max(0, L(Q_i^{b_low}(W_i); D_cal) - L(W; D_cal)).
```

Only one module is quantized during each probe, and the original weight is
restored before probing the next module. For `{4,8}` allocation, the base policy
sets all modules to 4-bit. Upgrading module `i` to 8-bit consumes:

```text
Delta M_i = c_i (8 - 4).
```

The current implementation uses a greedy budgeted rule:

```text
score_i = s_i / Delta M_i.
```

Modules are upgraded in descending `score_i` while the budget allows.

### Proposition 1: Optimality Under Uniform Costs And Additive Local Loss

Assume all modules have equal cost and the first-order loss protected by
upgrading a set `S` is additive:

```text
Protected(S) = sum_{i in S} s_i.
```

For a budget that upgrades exactly `k` modules, selecting the `k` largest
`s_i` maximizes `Protected(S)`.

This simple proposition explains the ranking rule under equal costs. With
non-uniform costs, the problem becomes a 0/1 knapsack over `(s_i, Delta M_i)`;
the greedy score is a fractional-relaxation heuristic. We therefore also build
an exact dynamic-programming knapsack solver over the measured one-module
sensitivity objective.

### Proposition 2: Local Sensitivity Additivity Is Not Global PPL Additivity

Let:

```text
s_i = L(Q_i(W_i)) - L(W)
```

be the one-module perturbation loss. For a multi-module allocation `S`, the true
loss is generally:

```text
L(Q_S(W)) - L(W)
  = sum_{i in S} s_i + sum_{i<j} I_{ij} + higher-order terms,
```

where `I_{ij}` captures interaction between quantization errors in modules `i`
and `j`. Exact optimization of `sum_i s_i` can therefore be suboptimal for the
global PPL objective when interaction terms are non-negligible. This motivates
interaction-aware features, Fisher/Hessian approximations, and learned
allocation policies.

### One-Step Policy Improvement

Given a base allocation `pi`, define a neighborhood `N(pi)` containing
budget-preserving swaps that demote one currently high-precision module and
promote one currently low-precision module:

```text
N(pi) = { pi - e_u(8->4) + e_v(4->8) }.
```

The one-step policy-improvement operator is:

```text
pi' = argmin_{q in N(pi) union {pi}} L(q; D_val).
```

This operator is expensive if the neighborhood is exhaustive, so the current
implementation evaluates a bounded candidate pool ranked by local sensitivity.
It is best viewed as a small global-feedback probe, not as a final optimizer.
Its value is diagnostic: if a single swap improves global PPL, then the local
additive proxy is incomplete and a learned interaction-aware allocator is
mathematically justified.

## 4. Learning And Reinforcement Learning View

The offline allocation can be treated as supervised policy learning:

```text
x_i = phi(W_i, A_i, hardware, budget)
y_i = b_i^*
```

where `b_i^*` comes from measured perturbation, exact knapsack, or a stronger
quantizer oracle. A model `pi_theta(b | x_i)` can then amortize allocation for
new models or devices.

The online variant is a constrained contextual bandit. At request or deployment
time, context `x_t` includes model statistics, prompt/domain features, current
memory pressure, latency target, and device state. The policy action `a_t`
selects a quantization configuration:

```text
a_t ~ pi_theta(. | x_t).
```

A practical reward is:

```text
R_t = -QualityDrop_t - beta_M Memory_t - beta_T Latency_t.
```

The constrained objective is:

```text
maximize    E[R_t]
subject to  E[Memory_t] <= B
            E[Latency_t] <= T
            P(QualityDrop_t > delta) <= eta.
```

A primal-dual update can optimize:

```text
J(theta, lambda) =
  E[-R_t]
  + lambda_M E[(Memory_t - B)_+]
  + lambda_T E[(Latency_t - T)_+]
  + lambda_Q E[(QualityDrop_t - delta)_+].
```

The deterministic C++ kernel corresponds to a fixed, auditable policy. The
learned bandit/RL policy is only introduced when it can beat deterministic
rules while satisfying measured constraints.

## 5. System Design

EigenSkill-Q separates three roles:

1. **Router:** detects that an input or calibration context requires a
   quantization-policy skill.
2. **Policy estimator:** computes sensitivity or predicts allocation candidates.
3. **Verifiable executor:** applies deterministic schema-safe policy decisions.

The current repository contains a C++ policy evaluator for five structured
quantization-policy skills:

```text
outlier_detect
bit_allocate
rotation_select
residual_patch
kv_policy
```

This is not yet a full runtime quantizer. It is a control-plane artifact showing
that structured numerical policy decisions can be executed outside of LLM text
generation.

## 6. Experiments

### 6.1 Deterministic Policy Kernel

The no-leak synthetic policy split contains 400 eval and 400 test samples.
The C++ evaluator reaches exact decision agreement:

| split | rows | policy_fields_exact | decision_exact | parse_error |
|---|---:|---:|---:|---:|
| eval | 400 | 1.0000 | 1.0000 | 0.0000 |
| test | 400 | 1.0000 | 1.0000 | 0.0000 |

This supports the bypass premise: low-entropy policy rules can be executed more
reliably by a deterministic kernel than by asking a small model to emit numeric
JSON.

### 6.2 Loss-Sensitive Allocation

Model:

```text
HuggingFaceTB/SmolLM2-360M-Instruct
```

Probe:

```text
Linear modules:             225
probe prompts:              4
group size:                 128
budget avg bits:            4.5
allocation:                 4-bit=172, 8-bit=53
positive loss protected:    57.83%
```

8-prompt diagnostic set:

| method | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---|
| FP16 | 179.14 | 0.0000 | 16:225 |
| uniform INT4 | 272.18 | 0.4183 | 4:225 |
| activation-stat RD 4/8 | 292.01 | 0.4886 | 4:172, 8:53 |
| loss-sensitive 4/8 | 212.69 | 0.1717 | 4:172, 8:53 |

WikiText2 validation, 32 prompts:

| method | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---|
| FP16 | 18.24 | 0.0000 | 16:225 |
| uniform INT4 | 30.26 | 0.5062 | 4:225 |
| uniform INT3 | 1678.70 | 4.5221 | 3:225 |
| activation-stat RD 4/8 | 26.13 | 0.3593 | 4:172, 8:53 |
| loss-sensitive 4/8 | 25.92 | 0.3514 | 4:172, 8:53 |

WikiText2 validation, 128 prompts:

| method | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---|
| FP16 | 17.34 | 0.0000 | 16:225 |
| uniform INT4 | 27.82 | 0.4727 | 4:225 |
| uniform INT3 | 1154.44 | 4.1981 | 3:225 |
| activation-stat RD 4/8 | 24.51 | 0.3459 | 4:172, 8:53 |
| loss-sensitive 4/8 | 24.14 | 0.3305 | 4:172, 8:53 |
| loss-sensitive exact knapsack 4/8 | 24.36 | 0.3396 | 4:175, 8:50 |
| loss-sensitive swap-search 4/8 | 24.07 | 0.3276 | 4:172, 8:53 |

The important result is not that this fake-quant scaffold beats production
quantizers. It does not. The important result is that direct measured
perturbation fixes the activation-proxy failure and gives a measurable target
for ML/RL policy learning.

The exact knapsack check is especially informative. It protects slightly more
local one-module positive loss than the greedy allocator (`57.87%` versus
`57.83%`), but its global WikiText2-128 PPL is slightly worse (`24.36` versus
`24.14`). This supports Proposition 2: the additive local objective is a useful
proxy but not the final objective. A stronger CCF-A version should model module
interactions explicitly or learn the allocation reward from calibration tasks.

The bounded swap-search check then evaluates 8 global-feedback candidates around
the greedy allocation. The best candidate demotes
`model.layers.17.self_attn.v_proj` and promotes
`model.layers.24.self_attn.v_proj`, improving WikiText2-128 PPL from `24.1374`
to `24.0661` while keeping the same `4-bit=172, 8-bit=53` histogram. The gain is
small, but it directly supports the interaction-aware formulation above.

C4 validation, 64 streamed prompts:

| method | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---|
| FP16 | 23.78 | 0.0000 | 16:225 |
| uniform INT4 | 36.94 | 0.4403 | 4:225 |
| uniform INT3 | 2990.80 | 4.8344 | 3:225 |
| activation-stat RD 4/8 | 33.69 | 0.3484 | 4:172, 8:53 |
| loss-sensitive 4/8 | 32.77 | 0.3205 | 4:172, 8:53 |
| loss-sensitive exact knapsack 4/8 | 32.87 | 0.3235 | 4:175, 8:50 |
| loss-sensitive swap-search 4/8 | 32.57 | 0.3146 | 4:172, 8:53 |

This second public-text source reproduces the WikiText2 ordering and reduces the
risk that the positive trend is an artifact of one validation slice.

## 7. Limitations

This draft is not yet a CCF-A submission. The current limitations are explicit:

- fake quantization dequantizes weights back to floating point;
- memory and latency reductions are not proven;
- no GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant baselines are included yet;
- WikiText2 slices are still small;
- C4 validation is currently only a 64-prompt streamed slice;
- the learned contextual bandit/RL component is formulated but not trained;
- the interaction-aware policy improvement is only a bounded one-step search;
- edge-board and NPU measurements remain future work;
- spectral/eigen-routing and swarm/acoustic concepts are out of scope.

## 8. Next Experiments Required For A Serious Submission

1. Evaluate on larger WikiText2/C4 slices with standard token-level PPL protocol.
2. Add RTN, GPTQ, AWQ, SmoothQuant, QuaRot/SpinQuant baselines.
3. Compare sensitivity estimators:
   - one-module measured loss delta;
   - Fisher diagonal;
   - Hessian proxy;
   - activation reconstruction error;
   - output KL divergence.
4. Replace greedy allocation with exact knapsack and learned amortized policies.
5. Add interaction-aware allocation features and compare local additive,
   pairwise, and learned reward models.
6. Expand the current one-step swap search into beam search, pairwise surrogate
   fitting, and policy-gradient or bandit-style allocation.
7. Train a constrained contextual bandit using calibration tasks and hardware
   budgets.
8. Report compressed runtime memory and latency only after implementing a real
   quantized representation or using an established quantization runtime.

## 9. Recommended Venue Framing

The best near-term framing is not NeurIPS/MLSys and not speculative edge swarm.
The credible route is:

- **ICML:** if the loss-sensitive/RL formulation is strengthened with theory and
  strong baselines.
- **IJCAI / AAAI:** if the contribution is positioned as verifiable AI policy
  control for quantization decisions.
- **ACL:** if the routing/tool-use angle and structured generation reliability
  become central.
- **JMLR / AI / TPAMI:** only after the theory, experiments, and baselines are
  substantially expanded.

## 10. Current Evidence Files

```text
train_python/measure_module_quant_sensitivity.py
train_python/build_dataset_prompts.py
train_python/eval_weight_quant_ppl.py
train_python/search_allocation_swaps.py
inference_cpp/src/quant_policy_bypass.cpp
outputs/smollm2_module_loss_sensitivity_limit4_group128.json
outputs/smollm2_fake_quant_ppl_compare_allocations_swap_group128_wikitext2_128_summary.json
outputs/smollm2_allocation_swap_search_group128_wikitext2_128_summary.json
outputs/smollm2_fake_quant_ppl_compare_allocations_swap_group128_c4_en_validation_64_summary.json
outputs/smollm2_fake_quant_ppl_c4_validation_64_report.md
outputs/smollm2_fake_quant_ppl_report.md
outputs/EigenSkill-Q-Loss-Sensitive-Allocation-Update-2026-06-04.md
```
