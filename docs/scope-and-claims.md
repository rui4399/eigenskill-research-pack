# Scope And Claims

This document defines the public claim boundary for the current EigenSkill
research pack. It is intentionally conservative.

## Current Positioning

Use this framing:

```text
EigenSkill is a reproducible proof-of-concept for hybrid skill routing and
deterministic quantization-policy bypass around a small LLM.
```

Do not use this framing yet:

```text
EigenSkill is a completed edge LLM micro-kernel, eigen-routing architecture,
or cross-medium swarm intelligence system.
```

## Claims Supported By The Repository

These claims are supported by committed data, scripts, or reports:

- The quantization-policy v1 dataset contains five policy skills:
  `outlier_detect`, `bit_allocate`, `rotation_select`, `residual_patch`, and
  `kv_policy`.
- The quantization-policy v1 split has no train/eval/test exact or input
  overlap according to `data_eval/eigenskill_quant_v1/audit.json`.
- A deterministic Python bypass reaches 100% `exact_json` and 100%
  `decision_exact` on the committed v1 eval and test splits.
- A deterministic C++ policy evaluator reaches 100%
  `policy_fields_exact` and 100% `decision_exact` on the committed v1 eval
  and test splits. This checks the decision-bearing fields, not every
  auxiliary JSON field.
- A short SmolLM2-360M LoRA smoke run does not learn the quantization-policy
  decisions in a 60-row generation check; this is negative evidence for using
  small SFT alone as the policy executor.
- The older v2 8-skill package demonstrates a hybrid routing mechanism where
  `unit_time_normalize` is handled by a deterministic bypass.
- The v2 8-skill numbers are engineering PoC evidence only because the split
  has severe train/eval overlap.
- The C++ benchmark demonstrates a synthetic low-rank arithmetic best case
  where `W = U A U^T`.
- The fake weight-quantization scaffold has short-slice PPL evidence for
  SmolLM2-360M, Qwen2.5-0.5B, and a local Qwen2.5-1.5B checkpoint. These are
  quality diagnostics for allocation policies, not packed-runtime claims.
- Measured per-module loss sensitivity can improve short-slice fake-quant PPL
  over uniform INT4 in the committed SmolLM2 and Qwen smoke runs. The
  Qwen2.5-1.5B evidence includes 2-prompt, 8-prompt, and consensus
  allocations on WikiText2/C4 slices.

## Claims Not Supported Yet

Do not claim any of the following as results:

- Transformer-layer `O(d)` inference from true eigenvectors.
- Spectral/eigen-routing through LayerNorm, attention, SwiGLU, or residual
  nonlinear dynamics.
- End-to-end speedup over llama.cpp, ExecuTorch, RKNN, Ascend, Qualcomm NPU,
  or any other production runtime.
- ARM NEON, RISC-V, RK3588, Ascend, Jetson, or Qualcomm NPU deployment.
- Board-level latency, throughput, or energy savings.
- Superiority over RTN, GPTQ, AWQ, SmoothQuant, QuaRot, SpinQuant, OmniQuant,
  or other quantization baselines.
- A finished mixed-precision LLM quantization algorithm.
- Acoustic communication, magnetic physical assembly, or swarm intelligence
  implementation.

## Language To Prefer

Prefer:

```text
deterministic bypass
policy bypass
routing PoC
synthetic low-rank microbenchmark
no-leak synthetic quantization-policy split
negative evidence from short LoRA smoke run
future spectral-routing theory track
```

Avoid:

```text
true eigen-routing
edge LLM micro-kernel
hardware-level AI kernel
swarm LLM result
cross-medium deployed system
proven O(d) Transformer inference
rate-distortion quantization result
```

## Paper Direction

The current credible paper direction is not the full original architecture.

The narrower direction is:

```text
Hybrid skill routing for edge-oriented LLM services, where numeric
quantization-policy decisions are routed to deterministic policy kernels and
the LLM handles semantic triggering and non-deterministic language tasks.
```

Required before a serious submission:

1. Replace the overlapping v2 split with a no-leak routing split.
2. Add real quantization baselines and metrics, including perplexity, task
   accuracy, memory, and latency.
3. Implement the bypass kernels in C++ and measure call overhead.
4. Run at least one real edge-board or embedded-device measurement before using
   hardware or energy claims.
5. Separate speculative swarm/acoustic material into a future vision document,
   not the main paper contribution.
