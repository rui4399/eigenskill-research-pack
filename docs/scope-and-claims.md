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
- The C++ quant-kernel API exposes FP32 dense GEMV, AVX2 dense GEMV,
  selected-row GEMV, scalar bypass, and row-scaled signed low-bit
  pack/dequant GEMV for 2..8-bit storage, including a mixed-bit per-row matrix
  format. Current low-bit CPU kernels are correctness/structure baselines, not
  full low-bit matmul speedup evidence. The narrower supported systems result
  is selected-row execution, including selected-row execution over mixed-bit
  storage.
- The fake weight-quantization scaffold has short-slice PPL evidence for
  SmolLM2-360M, Qwen2.5-0.5B, and a local Qwen2.5-1.5B checkpoint. These are
  quality diagnostics for allocation policies, not packed-runtime claims.
- Measured per-module loss sensitivity can improve short-slice fake-quant PPL
  over uniform INT4 in the committed SmolLM2 and Qwen smoke runs. The
  Qwen2.5-1.5B evidence includes 2-prompt, 8-prompt, and consensus
  allocations on WikiText2/C4 slices, plus a 16-prompt budget-matched
  comparison against random and structural heuristic mixed-precision baselines.
- A standalone C++ allocation planner now consumes measured module-sensitivity
  JSON and emits evaluator-compatible loss-sensitive, random, and category
  budget allocations. On the Qwen2.5-1.5B 16-prompt WikiText2 slice, the C++
  loss-sensitive allocation reaches PPL `13.14`, versus `13.75` for C++ random,
  `14.28` for C++ category, and `15.04` for uniform INT4.
- A standalone C++ result summarizer now reads evaluator PPL JSON and emits
  Markdown/CSV rankings with random-budget min/mean/max and target-vs-random
  margins. This reduces Python glue in the evidence-reporting path; model
  loading and fake-quant evaluation are still Python/PyTorch.
- A standalone C++ evidence-matrix summarizer now merges multiple evaluator PPL
  JSON files into a cross-dataset Markdown/CSV table with target-vs-uniform,
  target-vs-best-random, and target-vs-random-mean margins. It is a reporting
  tool, not a quantization algorithm.
- The C++ evidence-matrix summarizer supports `--target auto` for cross-model
  reports where the strongest current target config has different names across
  experiments, for example `wikitext_c4_consensus` on Qwen3-1.7B and
  `cpp_loss_sensitive_budget` on Qwen3-0.6B/OLMo2. This only selects an
  already-evaluated result row; it does not rerun or change the evaluator.
  The current cross-model table covers six WikiText2/C4 64-prompt rows. After
  expanding OLMo2 from random8 to random16, one negative best-random comparison
  is explicit: OLMo2 C4 `cpp_loss_sensitive_budget` loses to the best random
  seed by about `0.2582` PPL while still beating uniform INT4 and random mean.
  This should be reported as calibration-noise evidence, not hidden.
- A follow-up OLMo2 consensus-vs-random16 check shows that the cross-dataset
  consensus allocation repairs this specific negative case: on the same C4-64
  prompt slice and random16 pool, `wikitext_c4_consensus` reaches `35.4726` PPL
  versus best random `35.5846`, a `+0.1120` PPL margin. On WikiText2-64 the
  same consensus target beats best random16 by about `+0.4288` PPL. This is a
  narrow robustness result, not a general SOTA quantization claim.
- A standalone C++ consensus-allocation builder now reproduces the Python
  WikiText2+C4 consensus allocation for Qwen3-1.7B and OLMo2-0425-1B exactly
  at the bit-decision level while emitting evaluator-compatible JSON and
  Markdown. This moves the allocation construction path, not only the reporting
  path, out of Python.
- A standalone C++ consensus-allocation audit now reads the left/right
  calibration allocations plus the consensus allocation and reports high-bit
  overlap, Jaccard similarity, weighted average bits, budget use, and bit
  histograms. It is an allocation-stability audit, not a model-quality
  evaluator; downstream quality still comes from PPL checks.
- A standalone C++ split-stability audit now reads two sensitivity JSON files
  and reports positive-set Jaccard, signed-delta agreement, Pearson/Spearman
  correlations, Kendall tau-a, and top-k score overlap. It mirrors the Python
  stability diagnostic and reduces the amount of Python-only evidence in the
  calibration-noise story.
- A standalone C++ budget-curve summarizer now reads fake-quant PPL summary
  JSON files and regenerates the consensus budget-curve Markdown, CSV, JSON,
  and SVG outputs. It removes the NumPy/matplotlib dependency from this
  reporting path; model loading and fake-quant evaluation remain Python/PyTorch.
- A newer-model Qwen3-0.6B fake-quant run completed under the GPU guard. On
  the same 16-prompt WikiText2 slice, FP16 PPL is `27.82`, uniform INT4 is
  `44.57`, C++ loss-sensitive budget allocation is `34.84`, C++ random budget
  is `39.18`, and C++ category budget is `37.57`. The Qwen3 sensitivity
  calibration used only 4 prompts; a random16 stress check on a 64-prompt
  WikiText2 slice gives FP16 `31.18`, uniform INT4 `49.79`, loss-sensitive
  `39.01`, category `42.19`, and random min/mean/max
  `41.91 / 44.06 / 46.40`. The target is ahead of the best listed random seed
  by `2.90` PPL and the random mean by `5.05` PPL. On a C4-64 check using the
  same WikiText2-calibrated allocation, FP16 is `36.14`, uniform INT4 is
  `52.94`, loss-sensitive is `45.06`, category is `47.72`, and random
  min/mean/max is `47.17 / 48.53 / 50.03`, leaving the target ahead of the best
  random seed by `2.10` PPL. This is still a short-cycle signal rather than a
  mature benchmark.
- A Qwen3-1.7B uniform fake-quant smoke run also completed under the GPU guard:
  FP16 PPL `18.97`, uniform INT4 PPL `27.45`, and uniform INT3 PPL `312.57`
  on the 16-prompt WikiText2 slice. Peak GPU memory was `5525/8151 MiB`
  (`67.78%`).
- Qwen3-1.7B per-module sensitivity originally exceeded the requested GPU
  memory ceiling and was killed at `7628/8151 MiB` (`93.58%`). After adding
  CPU weight backup, low-memory row-chunk fake quantization, checkpointing, and
  resume support, the same 2-prompt sensitivity probe completed at
  `4520/8151 MiB` (`55.45%`). The resulting C++ loss-sensitive allocation beats
  uniform INT4 (`24.80` vs `27.45` PPL) and C++ random budget (`24.80` vs
  `25.39`) on the 16-prompt WikiText2 slice, but the C++ category budget is
  stronger on that slice (`23.84`). The same allocation also beats uniform INT4
  and random on a 64-prompt WikiText2 check (`27.66` vs `31.19` and `28.38`),
  while category remains slightly stronger (`27.48`). This should be reported
  as a mixed result, not as allocator dominance.
- The C++ planner includes an experimental `hybrid_budget` ordering that blends
  normalized loss-per-cost sensitivity with the structural category prior. On
  Qwen3-1.7B it improves over uniform INT4 and random but does not beat the
  category baseline on either 16-prompt (`23.98` vs `23.84`) or 64-prompt
  (`27.68` vs `27.48`) WikiText2 checks. Treat it as an ablation, not a new
  best allocator.
- The C++ planner now also emits a small sensitivity/category blend sweep.
  On Qwen3-1.7B, the low-sensitivity blend candidates
  `blend_sensitivity_05` and `blend_sensitivity_45` improve over
  `category_budget` on both the 16-prompt (`23.52` vs `23.84` PPL) and
  64-prompt (`27.4756` vs `27.4838` PPL) WikiText2 checks at the same
  average-bit budget. This is the current best in-repository Qwen3-1.7B
  WikiText2 fake-quant allocation, but the 64-prompt gain is small. A
  random16 stress check shows the loss-sensitive allocation barely ahead of
  the best random seed on WikiText2-64 (`27.6578` vs `27.6685`) and behind the
  best random seed on C4-64 (`29.2030` vs `28.4562`), while still ahead of the
  random mean on both datasets. Treat this as evidence that the current
  two-prompt sensitivity proxy is informative but not robust; do not advertise
  it as field-leading or as an allocator-dominance result.
- A Qwen3-1.7B two-split consensus allocation, built from one WikiText2
  2-prompt sensitivity split and one C4 2-prompt sensitivity split, improves
  the same 64-prompt checks. It reaches `26.3260` PPL on WikiText2-64 and
  `28.3303` PPL on C4-64. A full random16 re-evaluation confirms the margin:
  random min/mean/max is `27.6685 / 28.2905 / 29.9682` on WikiText2-64 and
  `28.4562 / 29.4357 / 30.0408` on C4-64, leaving consensus ahead of both the
  best random seed and the random mean on both slices. This supports a narrower
  claim: cross-distribution calibration consensus improves the current
  fake-quant diagnostic on Qwen3-1.7B. It is still not a production quantizer,
  packed runtime, or broad benchmark.
- A split-stability audit supports the calibration-noise interpretation behind
  the consensus method. For WikiText2-vs-C4 two-prompt sensitivity probes,
  Qwen3-1.7B has score/cost Spearman `0.0734` and top-20 score-set Jaccard
  `0.1429`; OLMo2 has score/cost Spearman `0.1845` and top-20 score-set
  Jaccard `0.1111`. These low correlations justify reporting consensus
  robustness, not single-split allocator dominance.
- A budget-curve diagnostic for the same consensus allocator now evaluates
  4.25, 4.50, and 4.75 average-bit budgets on both Qwen3-1.7B and
  OLMo2-0425-1B-Instruct. PPL improves monotonically as more 8-bit budget is
  released on Qwen3 WikiText2-64 (`28.0753 -> 27.3180 -> 26.6163`),
  Qwen3 WikiText2-128 (`27.7279 -> 27.4054 -> 26.5665`), Qwen3 C4-64
  (`30.4752 -> 29.9230 -> 29.2500`), OLMo2 WikiText2-64
  (`23.2779 -> 22.5113 -> 22.1464`), OLMo2 WikiText2-128
  (`25.7774 -> 25.0435 -> 24.6993`), and OLMo2 C4-64
  (`37.9817 -> 37.2835 -> 37.1610`). GPU-guarded runs stayed below the
  requested 85% memory ceiling, peaking at `5071/8151 MiB` for Qwen3 and
  `4376/8151 MiB` for OLMo2. This supports a budget-quality curve claim for
  the fake-quant diagnostic, not a packed-runtime or hardware claim.
- A non-Qwen `allenai/OLMo-2-0425-1B-Instruct` fake-quant run completed under
  the GPU guard. On the 16-prompt WikiText2 slice, FP16 PPL is `17.12`,
  uniform INT4 PPL is `20.70`, and uniform INT3 PPL is `58.84`. A 2-prompt
  low-memory sensitivity probe over all 113 Linear modules completed at
  `4175/8151 MiB` (`51.22%`). The resulting C++ planner allocations improved
  over uniform INT4, C++ random budget, and C++ category budget on both the
  16-prompt and 64-prompt WikiText2 checks. The best 16-prompt tested blend is
  `blend_sensitivity_85` (`18.76` PPL), while the 64-prompt check is slightly
  better with `loss_sensitive_budget` (`21.12` PPL) than `blend_sensitivity_85`
  (`21.13` PPL). The C++ planner also supports `--random-repeats`; the original
  single-split loss-sensitive allocation is clearly ahead of random8 on
  WikiText2-64 (`21.12` vs best random `21.46`) but only barely ahead on C4-64
  (`35.84` vs `35.85`). A new OLMo2 WikiText2+C4 two-split consensus allocation
  fixes that weak C4 margin: it reaches `21.0349` PPL on WikiText2-64 and
  `35.4726` PPL on C4-64, beating the listed best random seeds on both slices
  (`21.4637` and `35.8512`, respectively). The C4 sensitivity probe completed
  at `4253/8151 MiB` (`52.18%`), and the consensus PPL checks peaked at about
  `4492/8151 MiB` (`55.11%`). Treat this as second-model support for the
  narrow claim that cross-dataset calibration consensus improves this
  short-slice fake-quant diagnostic, not as a production quantizer or broad
  benchmark.
- A `google/gemma-3-1b-it` candidate was attempted but blocked by gated
  Hugging Face access in this environment. Report it only as an access
  blocker, not as a failed quantization result or quality datapoint.
- A `meta-llama/Llama-3.2-1B-Instruct` candidate was attempted and also blocked
  by gated Hugging Face access in this environment. The guard log peaked at
  `871/8151 MiB` (`10.69%`) because the model did not load. Report it only as
  an access blocker, not as a quality datapoint.
- The GPU guard script can enforce a max-memory ratio before and during CUDA
  runs. A Qwen2.5-1.5B 16-prompt comparison completed at 56.85% peak GPU
  memory after the fake-quant evaluator was changed to in-place group-wise
  quantization.

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
