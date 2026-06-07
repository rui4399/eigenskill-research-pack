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
- consensus-style allocation passes the committed short-slice robustness stress
  gate against uniform INT4 and random mixed-precision baselines;
- paired Qwen3 transfer slices show consensus avoiding the worse single-split
  policy, with bounded regret versus the best single split;
- bounded global-feedback swap search exposes interaction counterexamples that
  additive module ranking misses on committed SmolLM2-1.7B fake-quant slices;
- local AutoAWQ/GPTQModel Qwen2.5-0.5B W4/G128 evidence is bundled into a
  matched baseline pack covering public-calibration PPL, subset50 task
  execution, and PC-side runtime/VRAM, with the explicit negative result that
  the quantized local paths are slower than FP16;
- the public-calibrated AutoAWQ Qwen2.5-0.5B W4/G128 artifact has an expanded
  16-prompt-per-split WikiText2/C4 PPL gate totaling 2857 eval tokens;
- ESMP package integrity, selected-row probes, Triton shape-family kernels, and
  shallow generation integrations are executable prototype evidence;
- missing broad official baselines, leaderboard-scale task benchmarks, and
  hardware measurements are tracked as gaps rather than claimed as results.

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
2. larger WikiText2/C4 slices and multiple calibration seeds;
3. downstream task-retention evaluation beyond tiny smoke gates;
4. interaction-aware/global-feedback allocation checks;
5. real packed-runtime or on-device TTFT/tokens/s/peak-memory measurements.

The first item is only partially started by the local AutoAWQ/GPTQModel
Qwen2.5-0.5B matched pack and the expanded AutoAWQ 16-prompt public PPL gate.
It does not yet cover larger models, SmoothQuant, rotation-family baselines, or
leaderboard-scale tasks.

Historical notes and removed speculative material are summarized in
`docs/HISTORICAL_ARTIFACTS.md`.
