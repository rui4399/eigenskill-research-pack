# Paper Targets And Readiness

Date: 2026-06-07

This file is the single publication-readiness note for the public repository.
Older venue lists were folded here so the project does not present several
competing submission stories.

## Current Defensible Contribution

The strongest current paper direction is:

```text
Calibration split instability in mixed-precision LLM quantization, with
consensus sensitivity allocation and gated packed-system evidence.
```

The current evidence supports:

- calibration-split instability diagnostics on Qwen3-0.6B, Qwen3-1.7B,
  OLMo-2-0425-1B-Instruct, and SmolLM2-1.7B boundary cases;
- WikiText2/C4 short-slice fake-quant PPL comparisons and random-repeat
  allocation audits around the 4.5 average-bit budget;
- budget and robustness gates for mean consensus, robust-LCB, transfer
  boundaries, and bounded interaction-aware swap search;
- a Q-Palette-style closed-form Lagrangian allocation proxy over measured Qwen3
  and Qwen2.5 sensitivity artifacts, gated for finite lambda, budget use, and
  non-trivial bit histograms;
- a public-calibrated AutoAWQ W4 group-128 readiness bundle on
  Qwen2.5-0.5B-Instruct with tiny public WikiText2/C4 matched PPL slices;
- expanded 16-prompt-per-split AutoAWQ and GPTQModel public PPL gates for the
  same public-calibrated Qwen2.5-0.5B W4/G128 setting, aligned in the official
  PTQ readiness matrix;
- a local matched AutoAWQ/GPTQModel Qwen2.5-0.5B W4/G128 baseline pack that
  ties public-calibration PPL, subset50 MMLU/GSM8K execution, and PC-side
  runtime/VRAM into one explicit claim boundary;
- ESMP package integrity, Triton shape-family kernels, selected-row probes, and
  shallow generation integration gates;
- explicit gap tracking for official baselines, task retention, and mobile
  deployment.

The current evidence does not support a broad quantization-method claim, a
production runtime claim, or a real-device deployment claim.

## Best-Fit Near-Term Venues

These are fit hypotheses, not acceptance claims. School and CCF/CAS recognition
rules drift, so verify the latest official list before choosing a target.

| Route | Why it fits | What must improve first |
|---|---|---|
| ACL Findings / EMNLP Findings / COLING | Compression diagnostic, calibration robustness, public task subsets. | Larger slices, stronger task retention, clearer baseline table. |
| AAAI / IJCAI | Resource-aware optimization with empirical robustness. | Official AWQ/GPTQ or faithful comparator, more seeds, more models. |
| TMLR | Clean problem definition plus negative evidence and ablations. | Stronger theory/variance framing and reproducible baseline package. |
| Neural Networks / Information Sciences | Journal-length robustness and optimization study. | Broader model ladder, statistical tests, official baselines. |
| Engineering Applications of Artificial Intelligence | Engineering artifact with gated systems evidence. | Runtime or device metrics beyond module-level probes. |
| Efficient-LLM / model-compression workshops | Short-cycle artifact release and focused feedback. | Clean tables, exact scripts, and conservative claims. |

Avoid positioning the current artifact for ASPLOS/ISCA/MICRO/OSDI-style systems
venues until there is real runtime integration, end-to-end TTFT/tokens/s, memory
and power evidence. Avoid TNNLS/TPAMI-style claims until the theory and task
evidence become much deeper.

## Not Ready For Mainline Submission

The blockers are concrete:

1. Official baselines: the local AutoAWQ/GPTQModel 0.5B matched pack and the
   expanded 16-prompt public PPL gates are useful but not enough; larger AWQ/GPTQ
   rows, SmoothQuant, and at least one faithful rotation or mixed-precision
   allocation comparator are still missing.
2. Larger evaluation: more WikiText2/C4 prompts and multiple calibration seeds.
3. Downstream retention: MMLU/GSM8K/IFEval or similar task slices on the actual
   quantized/fused variants, not only base-model capability smoke.
4. Statistical robustness: bootstrap or confidence intervals for
   consensus-vs-single-split risk.
5. Runtime evidence: packed quantized weights integrated into an inference path;
   PyTorch fake quant cannot justify latency, memory, or energy claims.
6. Mobile evidence: Redmi K80 Pro or another real device needs TTFT, tokens/s,
   peak memory, thermal and power logs before any deployment language is used.

## Near-Term Artifact Path

The next credible public milestone is a technical report or workshop artifact:

```text
Calibration Split Instability in Mixed-Precision LLM Quantization:
Consensus Sensitivity Allocation with Gated Packed-System Evidence
```

Before releasing that version:

- scale the public-calibrated AutoAWQ/GPTQModel pack beyond tiny slices and
  beyond Qwen2.5-0.5B;
- add SmoothQuant and at least one faithful rotation-family or allocation
  comparator under the same calibration and evaluation protocol;
- rerun core fake-quant rows with more calibration seeds;
- include the budget-curve figure from `outputs/consensus_budget_curve.svg`;
- keep C++ reporting tools framed as reproducibility infrastructure unless tied
  to measured kernel/runtime gates.

## Stronger Paper Shape

A stronger journal or recognized-conference version should define:

- a noisy sensitivity estimator `s_i(D)` over calibration data;
- a consensus estimator across calibration distributions or splits;
- a constrained bit-allocation objective under a fixed average-bit budget;
- a robustness objective over calibration perturbations;
- downstream risk measured by PPL and task degradation.

The systems contribution should remain scoped until the runtime catches up:

- ESMP packaging and C++ inspection are real artifact infrastructure;
- Triton and selected-row kernels are module-level probes;
- no end-to-end speed or mobile claim should appear without physical
  measurements.
