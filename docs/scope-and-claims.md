# Scope And Claims

This file is a short public boundary for the current repository. It deliberately
replaces the older long-form progress log. If there is any conflict, the
authoritative documents are:

```text
docs/PAPER_CLAIM_MATRIX.md
docs/SYSTEM_EVIDENCE_GATES.md
outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md
```

## Current Scope

EigenSkill-Q is currently scoped as:

```text
a calibration-robustness and mixed-precision fake-quantization research
artifact, with C++/packed-system prototypes used as gated supporting evidence.
```

The active research question is:

```text
When module sensitivity is estimated from very small calibration splits, how
unstable are the resulting mixed-precision allocation decisions, and can
cross-split consensus reduce the risk of choosing a bad single split?
```

## Supported Claims

The repository supports only claims that appear in `docs/PAPER_CLAIM_MATRIX.md`.
In compressed form, the supported claims are:

- small calibration splits produce unstable module-sensitivity rankings in the
  committed Qwen3/OLMo2 fake-quant diagnostics;
- Qwen2.5 perturbation diagnostics separate same-model calibration sample-size
  instability from much weaker cross-model-scale sensitivity transfer;
- Qwen2.5 six-seed prompt diagnostics show that deterministic small-sample
  sensitivity runs can have moderate average rank agreement while still
  drifting in top-sensitive module sets;
- Qwen2.5 CSI-vs-calibration-size diagnostics show monotonic stability gains
  across n=2, n=4, and n=8 prompt samples in one fixed public-prompt setting;
- Qwen2.5 CSI trend-significance diagnostics show positive n=8-vs-n=2
  bootstrap mean-gain CIs for the audited stability metrics, with minimum
  random seed-pair dominance probability 0.9422 in the same fixed setting;
- Qwen2.5 CSI null-permutation diagnostics reject a pooled n=2/n=8
  label-shuffle null for the audited stability gains, with maximum
  Holm-adjusted p-value 0.000149993 in the same fixed setting;
- a Chebyshev-style plug-in rank-inversion analysis over the same n=2/4/8
  Qwen2.5 seed artifacts shows decreasing empirical inversion risk and
  decreasing variance/gap^2 bound proxies;
- consensus-style allocation passes the committed short-slice robustness stress
  gate against uniform INT4 and random mixed-precision baselines;
- paired Qwen3 transfer slices show consensus avoiding the worse single-split
  policy, with bounded regret versus the best single split;
- bounded global-feedback swap search exposes interaction counterexamples that
  additive module ranking misses on committed SmolLM2-1.7B fake-quant slices;
- a Q-Palette-style closed-form Lagrangian allocation proxy now covers measured
  Qwen3 and Qwen2.5 sensitivity artifacts with finite lambda and strict budget
  checks, while remaining explicitly non-faithful to Q-Palette/IMPQ/WINDQuant;
- local AutoAWQ/GPTQModel Qwen2.5-0.5B W4/G128 evidence is bundled into a
  matched baseline pack covering public-calibration PPL, subset50 task
  execution, and PC-side runtime/VRAM, with the explicit negative result that
  the quantized local paths are slower than FP16;
- the same official PTQ variants now have true 100-row matched MMLU/GSM8K
  subset execution and PC-side runtime gates, with max task drop 0.03 versus
  FP16 and the same negative local-speed boundary;
- Qwen2.5-1.5B now has a matched FP16/AutoAWQ/GPTQModel subset100 task/runtime
  matrix. It strengthens native-baseline confrontation, but still reports lower
  guarded VRAM and slower local loader throughput rather than production
  acceleration;
- the same Qwen2.5-1.5B baseline confrontation now extends to GSM8K200/MMLU100
  across FP16, AutoAWQ, and GPTQModel, with paired bootstrap uncertainty
  reported rather than hidden;
- the Qwen2.5-1.5B baseline confrontation also has a full GSM8K1319
  single-task row across FP16, AutoAWQ, and GPTQModel, still bounded as local
  single-task retention evidence rather than leaderboard-scale benchmark
  quality;
- the Qwen2.5-1.5B baseline confrontation also has a five-subject MMLU Broad5x20
  row across FP16, AutoAWQ, and GPTQModel, still bounded as local subset
  evidence rather than full MMLU benchmark quality;
- the same FP16/AutoAWQ/GPTQModel Qwen2.5-0.5B variants have deterministic
  IFEval-style instruction-following execution and runtime smoke gates, kept as
  execution-path evidence because the FP16 baseline is 0/8;
- the public-calibrated AutoAWQ and GPTQModel Qwen2.5-0.5B W4/G128 artifacts
  have aligned expanded 16-prompt-per-split WikiText2/C4 PPL gates, totaling
  5714 eval tokens across both packages;
- ESMP package integrity, selected-row probes, Triton shape-family kernels, and
  shallow generation integrations are executable prototype evidence;
- missing broad official baselines, leaderboard-scale task benchmarks, and
  hardware measurements are tracked as gaps rather than claimed as results.

## Public-Branch Rule

The repository should be edited as a claim-bounded artifact. Private planning,
mentor-facing prose, Obsidian notes, NotebookLM source lists, Notion drafts,
delivery bundles, and chat/WeChat handoff material should stay outside the
public tree unless they are converted into a reproducible gate, artifact
manifest row, or claim-matrix row.

## Explicit Non-Claims

Do not present this repository as:

- a state-of-the-art quantizer;
- a faithful official GPTQ, AWQ, SmoothQuant, QuaRot, or SpinQuant
  implementation;
- a production Tensor Core, llama.cpp, ExecuTorch, RKNN, Ascend, or Qualcomm
  runtime;
- a Redmi K80 Pro or board-level deployment result;
- evidence of TTFT, tokens/s, peak memory, energy, or thermal improvement on a
  real device;
- proof that spectral/eigen routing survives LayerNorm, attention, SwiGLU, or
  residual nonlinearities;
- a cross-medium acoustic, magnetic assembly, or physical swarm system.

## Language To Prefer

Prefer:

```text
calibration split instability
consensus sensitivity allocation
short-slice fake-quant diagnostic
gated packed-system prototype
claim boundary
negative capability evidence
```

Avoid:

```text
completed edge LLM micro-kernel
true eigen-routing
proven O(d) Transformer inference
hardware-level AI kernel
swarm LLM result
production mobile deployment
SOTA quantizer
```

## Next Evidence Needed

The next paper-strengthening steps are:

1. faithful public quantization baselines under matched budgets;
2. larger WikiText2/C4 slices and broader calibration-seed sweeps beyond the
   current n=2/4/8 Qwen2.5-0.5B curve;
3. downstream task-retention evaluation beyond local subset gates, especially
   full MMLU and broader IFEval;
4. interaction-aware/global-feedback allocation checks;
5. real packed-runtime or on-device TTFT/tokens/s/peak-memory measurements.

The first item is only partially started by the local AutoAWQ/GPTQModel
Qwen2.5-0.5B matched pack and the expanded 16-prompt public PPL gates.
It does not yet cover larger models, SmoothQuant, rotation-family baselines,
full MMLU, or leaderboard-scale tasks.

Historical notes and removed speculative material are summarized in
`docs/HISTORICAL_ARTIFACTS.md`.
