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
the current evidence ledger passes 22/22 gates. The calibration-instability
gate finds 3/3 unstable model/dataset cases with mean score/cost Spearman
0.0713 and mean top-20 Jaccard 0.1022. The robustness stress gate reports
11/11 wins versus uniform INT4, best random seed, and random-seed mean under the
same budget, with a one-sided sign-test p-value of 0.000488 versus best random.
A paired transfer-boundary gate shows consensus avoiding the worse single-split
policy on 4/4 Qwen3 transfer slices while allowing bounded regret versus the
best single split. Finally, an interaction-aware swap gate shows 5
locally-negative-but-globally-improved swap trials, demonstrating that additive
module ranking misses measurable global interactions. The current system
evidence is deliberately gated and prototype-level: public-task coverage now
includes a two-model guarded Ollama ladder over 200 MMLU/GSM8K subset rows,
while ESMP packaging, Triton shape tuning, selected-row execution, shallow
fused-QKV generation, and C++ audit tools are executable. The repository does
not claim a production LLM runtime.

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
   families.
2. **Consensus sensitivity allocation.** We evaluate a simple cross-split
   consensus allocator that protects modules that are consistently sensitive or
   have high average sensitivity under a fixed `{4,8}` budget.
3. **Gated evidence discipline.** We convert scattered fake-quant, runtime,
   task-smoke, paper-alignment, and repository-hygiene outputs into 22 executable gates, each
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

## 4. Consensus Sensitivity Allocation

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

## 5. Interaction-aware Global Feedback

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

## 6. Evidence Gates

Every paper-facing claim is indexed by a gate JSON and a Markdown report. The
current ledger passes 22/22 gates. The most important gates are:

| Gate | Evidence | Valid claim | Non-claim |
|---|---|---|---|
| Calibration instability | 3 Qwen3/OLMo2 split comparisons | Small calibration splits induce unstable module rankings. | Instability alone proves consensus is superior. |
| Robustness stress | 11 short fake-quant PPL slices | Target policies beat uniform and random baselines on committed slices. | Not SOTA PTQ or task retention. |
| Consensus transfer boundary | 4 paired Qwen3 slices | Consensus avoids the worse single-split policy with bounded best-single regret. | Consensus always beats the best single split. |
| Interaction swap boundary | 16 SmolLM2-1.7B swap trials | Global feedback exposes local-proxy failures. | Global optimality or broad transfer. |
| Public task model ladder | 2 local Ollama models over 200 MMLU/GSM8K subset rows | Public-task evidence is reported without hiding the weaker 4B case. | Leaderboard quality, monotonic scaling, or fused quantized retention. |
| Packed-system gates | ESMP, Triton, selected-row, sidecar, QKV smoke | Prototype components are executable and audited. | Production Tensor Core/mobile runtime. |
| Paper evidence alignment | Paper draft, required evidence paths, claim-risk scan | The draft cites committed evidence and avoids unsafe non-negated claims. | Peer-review acceptance or complete baseline coverage. |

The evidence ledger is:

```text
outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md
```

## 7. Experiments

### 7.1 Calibration Split Instability

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

### 7.2 Robustness Stress Gate

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

### 7.3 Consensus Transfer Boundary

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

### 7.4 Interaction-aware Swap Boundary

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

### 7.5 Packed-system Prototype Evidence

The system side is intentionally scoped. The ESMPQ001 format can package and
audit mixed-bit matrices; Triton shape-family tuning finds selected shape wins;
selected-row and C++ runtime sweeps report module-level wins; shallow fused-QKV
generation and prompt-suite gates verify narrow integration paths. The ledger
records these as executable system evidence, but the paper does not claim
end-to-end quality preservation. It does not claim TTFT/tokens/s wins, real
mobile results, or edge-board deployment.

## 8. Discussion

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

## 9. Limitations

1. The main quality evidence is short-slice fake-quant PPL, not packed-runtime
   quality.
2. Official GPTQ, AWQ, SmoothQuant, QuaRot, and SpinQuant baselines are not yet
   faithfully reproduced. The baseline dashboard now separates proxy evidence
   from faithful official baseline coverage.
3. Public task evidence is limited local subset coverage, not leaderboard-scale
   capability retention or fused quantized retention.
4. System evidence is prototype/module-level; no Redmi K80 Pro or board-level
   TTFT, tokens/s, memory, energy, or thermal logs are complete.
5. The bit set is limited to `{4,8}` in the main allocation diagnostics.
6. The interaction-aware search is bounded one-step feedback, not a global
   optimization algorithm.

## 10. Conclusion

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
outputs/PUBLIC_TASK_MODEL_LADDER_GATE_2026_06_07.md
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
