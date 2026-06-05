# Nightly Delivery - 2026-06-05

This file records the concrete artifacts produced in the overnight run. It is
limited to verified code, committed outputs, and scoped claims.

## GitHub State

Repository:

```text
https://github.com/rui4399/eigenskill-research-pack
```

Latest pushed commit before this closeout block:

```text
ae49a09 Add SmolLM2 random16 audit
```

Commits pushed in this run:

```text
8df1892 Add C++ consensus allocation builder
9d12662 Add cross-model quant evidence matrix
a71d7ee Add OLMo2 random16 audit
1aa8fe2 Show OLMo2 consensus repairs random16 failure
74ce201 Add OLMo2 consensus repair reproduction script
94c328f Add revised publication targets
8b12cf9 Add JSON output for C++ evidence matrix
745e2b5 Add baseline environment audit
30cb648 Add baseline install probe utility
99198f6 Add Qwen3 1.7B WikiText2 128 evidence
a8a25c9 Add Qwen3 multi-slice evidence matrix
2e6a3e1 Add SmolLM2 1.7B retry smoke evidence
66a7bc1 Add SmolLM2 1.7B loss-sensitive loop
ae49a09 Add SmolLM2 random16 audit
```

## C++ Work

Added a standalone consensus allocation builder:

```text
inference_cpp/src/quant_consensus_builder.cpp
```

It reproduces the previous Python consensus allocation exactly at the
bit-decision level for Qwen3-1.7B and OLMo2-0425-1B, then emits
evaluator-compatible JSON and Markdown.

Updated the existing C++ evidence matrix:

```text
inference_cpp/src/quant_evidence_matrix.cpp
```

New behavior:

```text
--target auto
```

This selects an already-evaluated target row when different experiments use
different target names, for example `wikitext_c4_consensus` or
`cpp_loss_sensitive_budget`.

Validation:

```text
CTest: 10/10 passed
```

Additional C++ reporting utility:

```text
inference_cpp/src/baseline_install_probe.cpp
```

It converts pip install logs into Markdown/JSON evidence so failed baseline
setup attempts do not remain informal terminal notes.

## Quantization Evidence

Cross-model evidence:

```text
outputs/cross_model_quant_evidence_matrix_auto.md
outputs/cross_model_quant_evidence_matrix_auto.csv
```

Models covered:

```text
Qwen/Qwen3-0.6B
Qwen/Qwen3-1.7B
allenai/OLMo-2-0425-1B-Instruct
```

Datasets:

```text
WikiText2-64
C4-64
```

Important result:

```text
Qwen3-0.6B and Qwen3-1.7B have positive target margins versus best random.
OLMo2 single-split loss-sensitive allocation has one negative row on C4.
```

## Negative Result

The OLMo2 random baseline was expanded from random8 to random16:

```text
outputs/olmo2_0425_1b_random16_negative_audit.md
```

Key result:

```text
OLMo2 C4-64 single-split loss-sensitive:
target PPL       35.8428
best random16    35.5846
margin          -0.2582
```

This is not hidden. It is evidence that one-split sensitivity allocation is
not robust enough on short calibration probes.

## Consensus Repair

The same OLMo2 C4 negative case was rerun with the cross-dataset consensus
allocation against the same random16 pool:

```text
outputs/olmo2_0425_1b_consensus_repairs_random16_negative.md
outputs/olmo2_0425_1b_consensus_vs_random16_evidence_matrix.md
outputs/olmo2_0425_1b_consensus_vs_random16_evidence_matrix.csv
```

Key results:

```text
WikiText2-64 consensus PPL 21.0349 vs best random16 21.4637, margin +0.4288
C4-64        consensus PPL 35.4726 vs best random16 35.5846, margin +0.1120
```

This is the cleanest current story:

```text
short calibration probes are noisy
one-split allocation can fail
cross-dataset consensus repairs the observed best-random failure case
```

## Longer Qwen3-1.7B Slice

The Qwen3-1.7B consensus-vs-random16 evaluation was extended from
WikiText2-64 to WikiText2-128:

```text
outputs/qwen3_1p7b_wikitext2_128_consensus_random16_result.md
outputs/qwen3_1p7b_wikitext_c4_consensus_random16_ppl_wikitext2_128_summary.json
outputs/qwen3_1p7b_wikitext_c4_consensus_random16_wikitext2_128_evidence_matrix.md
outputs/qwen3_1p7b_multi_slice_consensus_random16_evidence_matrix.md
```

Key result:

```text
FP16 PPL:                   20.2931
uniform INT4 PPL:           28.2125
wikitext_c4_consensus PPL:  24.2065
best random16 PPL:          25.1876
target vs best random16:    +0.9811 PPL
```

This is stronger than the short smoke slice because it uses twice as many
WikiText2 prompts while keeping the same 16-random allocation pool.

Multi-slice matrix:

```text
WikiText2-64  target vs best random16: +1.3425 PPL
C4-64         target vs best random16: +0.1259 PPL
WikiText2-128 target vs best random16: +0.9811 PPL
```

## SmolLM2-1.7B Retry

The earlier SmolLM2-1.7B load failure was traced to incomplete model cache.
After retrying the download, the PyTorch `model.safetensors` path is usable,
though ONNX-side cache blobs remain incomplete:

```text
outputs/smollm2_1p7b_retry_smoke_result.md
outputs/smollm2_1p7b_predownload_retry_report.md
outputs/smollm2_1p7b_uniform_ppl_wikitext2_16_retry_summary.json
```

Smoke result:

```text
FP16 PPL:         12.6903
uniform INT4 PPL: 18.1431
uniform INT3 PPL: 197.0120
max GPU memory:   5109 / 8151 MiB = 62.68%
```

This only proves the model is now runnable in the PyTorch fake-quant path.
It is not yet a consensus-vs-random16 allocation result.

Follow-up closed-loop result:

```text
outputs/smollm2_1p7b_retry_loss_sensitive_result.md
outputs/smollm2_1p7b_retry_loss_sensitive_ppl_wikitext2_16_summary.json
```

Key numbers:

```text
FP16 PPL:                  12.6903
uniform INT4 PPL:          18.1431
loss_sensitive_limit8 PPL: 12.8844
loss-sensitive vs uniform: +5.2587 PPL
```

This is a small 32-module / 16-prompt result, but it is a real closed loop:
sensitivity measurement -> allocation -> PPL evaluation.

Random16 follow-up:

```text
outputs/smollm2_1p7b_retry_random16_evidence_matrix.md
loss_sensitive_limit8 vs uniform INT4: +5.2587 PPL
loss_sensitive_limit8 vs best random16: -0.0341 PPL
loss_sensitive_limit8 vs random16 mean: +0.0951 PPL
```

This makes the SmolLM2 result honest: the small allocation is clearly better
than uniform INT4, but it is not yet robust against best-of-16 random.

Full-module follow-up:

```text
outputs/smollm2_1p7b_full_random16_multi_slice_evidence_matrix.md
outputs/smollm2_1p7b_full_random16_result.md
outputs/smollm2_1p7b_module_loss_sensitivity_full_limit8_group128_report.md
outputs/smollm2_1p7b_full_random16_ppl_wikitext2_16_summary.json
outputs/smollm2_1p7b_full_random16_evidence_matrix.md
outputs/smollm2_1p7b_full_random16_ppl_wikitext2_64_summary.json
outputs/smollm2_1p7b_full_random16_wikitext2_64_evidence_matrix.md
outputs/smollm2_1p7b_full_random16_ppl_wikitext2_128_summary.json
outputs/smollm2_1p7b_full_random16_wikitext2_128_evidence_matrix.md
outputs/smollm2_1p7b_full_random16_ppl_c4_64_summary.json
outputs/smollm2_1p7b_full_random16_c4_64_evidence_matrix.md
```

Key numbers, WikiText2-16:

```text
measured Linear modules:     169 / 169
allocation:                  156 x 4-bit, 13 x 8-bit
FP16 PPL:                    12.6903
uniform INT4 PPL:            18.1431
loss_sensitive_full PPL:     13.9866
best random16 PPL:           14.7340
target vs uniform INT4:      +4.1565 PPL
target vs best random16:     +0.7474 PPL
target vs random16 mean:     +3.5992 PPL
```

Key numbers, WikiText2-64:

```text
FP16 PPL:                    12.6568
uniform INT4 PPL:            18.5164
loss_sensitive_full PPL:     14.8877
best random16 PPL:           15.6654
target vs uniform INT4:      +3.6286 PPL
target vs best random16:     +0.7777 PPL
target vs random16 mean:     +3.2236 PPL
```

Key numbers, C4-64:

```text
FP16 PPL:                    18.4497
uniform INT4 PPL:            26.3475
loss_sensitive_full PPL:     21.4269
best random16 PPL:           22.5529
target vs uniform INT4:      +4.9206 PPL
target vs best random16:     +1.1260 PPL
target vs random16 mean:     +4.6833 PPL
```

Key numbers, WikiText2-128:

```text
FP16 PPL:                    13.2171
uniform INT4 PPL:            18.7966
loss_sensitive_full PPL:     15.3641
best random16 PPL:           16.2050
target vs uniform INT4:      +3.4325 PPL
target vs best random16:     +0.8409 PPL
target vs random16 mean:     +3.1527 PPL
```

This repairs the earlier 32-module SmolLM2 best-random failure. The scope is
still deliberately narrow: short WikiText2 slices, fake quantization, and no
packed runtime speed claim. The C4-64 follow-up is an overfitting check because
the full allocation was built from WikiText2 calibration prompts.

Multi-slice matrix:

```text
WikiText2-16 target vs best random16: +0.7474 PPL
WikiText2-64 target vs best random16: +0.7777 PPL
WikiText2-128 target vs best random16: +0.8409 PPL
C4-64        target vs best random16: +1.1260 PPL
```

## GPU Guard

All GPU runs used:

```text
train_python/run_with_gpu_guard.py --max-memory-ratio 0.85
```

Observed peaks in the new OLMo2 runs:

```text
random16 WikiText2-64:        4592 / 8151 MiB = 56.34%
random16 C4-64:               4593 / 8151 MiB = 56.35%
consensus-vs-random16 Wikitext: 4593 / 8151 MiB = 56.35%
consensus-vs-random16 C4:       4586 / 8151 MiB = 56.26%
SmolLM2 full sensitivity:       4971 / 8151 MiB = 60.99%
SmolLM2 full random16 PPL:      5133 / 8151 MiB = 62.97%
SmolLM2 full random16 PPL-64:   5679 / 8151 MiB = 69.67%
SmolLM2 full random16 PPL-128:  5027 / 8151 MiB = 61.67%
SmolLM2 full random16 C4-64:    5674 / 8151 MiB = 69.61%
```

No guard kill occurred.

## Baseline Package Readiness

Environment audit:

```text
outputs/baseline_environment_audit.md
outputs/baseline_environment_audit.json
```

Install probe:

```text
outputs/baseline_install_probe.md
outputs/baseline_install_probe.json
outputs/baseline_venv_install_optimum.log
outputs/baseline_venv_install_nodeps_optimum_gptqmodel.log
```

Key result:

```text
Full `optimum` dependency install failed with a network read timeout while
downloading large CUDA-side dependencies.

`pip install --no-deps optimum gptqmodel` succeeded as metadata/build
probe only:
  gptqmodel==7.0.0
  optimum==2.1.0
```

This does not establish a runnable GPTQ/AWQ baseline yet. It only records
that public baseline packages are discoverable and that the current blocker
is dependency installation, not missing package names.

## Remaining Limitations

This remains a short-slice PyTorch fake-quant diagnostic.

Do not claim:

```text
production quantizer
hardware latency win
board-level energy result
SOTA over GPTQ/AWQ/SmoothQuant/QuaRot
true Eigen-routing through nonlinear Transformer layers
```

Next high-value work:

```text
1. Add a real public baseline dependency environment, or explicitly keep it as future work.
2. Extend consensus-vs-random16 to a larger prompt slice if runtime allows.
3. Add an interaction-aware swap/search stage on top of consensus.
4. Move more allocation/reporting glue from Python into C++ only where it reduces real dependency surface.
```
