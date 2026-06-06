# Paper Targets And Readiness

Date: 2026-06-05

This note keeps the submission story realistic. It avoids NeurIPS/MLSys and
does not frame the current repository as a production quantizer or edge
runtime.

## Current Defensible Contribution

The strongest current paper direction is:

```text
Calibration-robust mixed-precision fake-quant allocation via cross-dataset
consensus sensitivity, with deterministic C++ audit/reporting tools.
```

The current evidence supports:

- small-model fake-quant diagnostics across Qwen3-0.6B, Qwen3-1.7B,
  OLMo2-0425-1B-Instruct, and SmolLM2-1.7B boundary cases;
- two text sources: WikiText2 and C4;
- random-repeat comparisons at 4.5 average bits;
- budget curves at 4.25, 4.50, and 4.75 average bits;
- minimal AutoAWQ readiness probes on Qwen2.5-0.5B-Instruct, including a
  public-calibrated W4 group-128 bundle and tiny public WikiText2/C4 matched
  FP16-vs-AutoAWQ PPL slices;
- C++ audits for allocation consensus and split-stability;
- guarded GPU logs with explicit peak-VRAM records and claim boundaries.

## Venues To Consider Later

These are candidate directions, not guaranteed fit or current acceptance
targets:

- `TMLR`: good if the method becomes a clean learning/optimization story with
  strong ablations and open review tolerance for negative results.
- `Neural Networks`: possible if the paper emphasizes mixed-precision
  allocation, robustness, and empirical depth across several architectures.
- `Information Sciences`: possible if the work becomes an optimization and
  intelligent-systems contribution with broader comparisons.
- `Knowledge-Based Systems`: possible if the policy/kernel routing angle is
  expanded into decision systems and validated on real tasks.
- `Engineering Applications of Artificial Intelligence`: possible for an
  engineering-focused version with robust experiments and deployability
  evidence.
- `Pattern Recognition`: only plausible if task-level accuracy and compression
  baselines become much stronger; current PPL-only evidence is too narrow.
- `IEEE Transactions on Artificial Intelligence` or similar IEEE AI venues:
  possible if the method is framed as robust resource-aware model optimization,
  but baseline expectations are high.
- model compression / efficient AI workshops attached to ICLR/ICML/ACL/KDD:
  realistic short-cycle targets once baselines and ablations are cleaned up.

Venue rankings and school recognition rules drift. Verify the current official
school list and latest journal/CCF/CAS categorization before committing to a
target.

## Not Ready For Mainline Submission

Do not submit the current repo as a full journal/conference paper yet. The
missing pieces are clear:

1. Production baselines: RTN, GPTQ, AWQ, SmoothQuant, QuaRot/SpinQuant-style
   rotations, and at least one common mixed-precision allocator.
2. More models: at minimum a 0.5B/1B/1.5B/3B scale ladder, plus one non-Qwen
   family beyond OLMo2.
3. Larger evaluation: more WikiText2/C4 prompts, and at least one downstream
   task suite beyond PPL.
4. Statistical robustness: multiple calibration seeds and bootstrap confidence
   intervals for the consensus-vs-single-split claim.
5. Runtime evidence: packed quantized weights or a real integration with an
   inference backend; current PyTorch fake quant cannot support latency,
   memory, or energy claims.
6. Hardware evidence: only after a board or runtime benchmark exists should
   the paper say "edge" empirically.

## Near-Term Submission Path

The fastest credible path is a workshop or arXiv technical report:

```text
Title shape:
Cross-Dataset Consensus Sensitivity for Robust Mixed-Precision LLM Fake
Quantization Diagnostics
```

Required additions before that:

- add RTN/uniform and one public baseline beyond random/category;
- run at least 256 or 512 prompts on WikiText2/C4 for Qwen3 and OLMo2;
- scale the public-calibrated AutoAWQ bundle beyond tiny slices and add
  GPTQ/GPTQModel or another faithful public PTQ comparator under the same
  calibration/evaluation protocol;
- report calibration-seed variance;
- include the budget curve figure from `outputs/consensus_budget_curve.svg`;
- keep all claims explicitly scoped to fake-quant diagnostics.

## Longer-Term Strong Paper Shape

For a stronger journal or recognized conference version, the paper should become:

```text
Robust calibration under noisy sensitivity estimates for constrained
mixed-precision LLM quantization.
```

The core math should define:

- noisy sensitivity estimator `s_i(D)`;
- consensus estimator across calibration distributions;
- budgeted allocation as constrained optimization;
- robustness objective over calibration-set perturbations;
- downstream risk measured by PPL/task degradation under bit budget.

The systems part should stay modest until packed kernels are implemented:

- C++ audit and allocation tools are reproducibility infrastructure;
- C++ selected-row/mixed-bit kernels are microbenchmarks;
- no hardware speedup claim without a real runtime path.
