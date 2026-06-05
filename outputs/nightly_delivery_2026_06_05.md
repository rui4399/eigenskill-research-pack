# Nightly Delivery - 2026-06-05

This file records the concrete artifacts produced in the overnight run. It is
limited to verified code, committed outputs, and scoped claims.

## GitHub State

Repository:

```text
https://github.com/rui4399/eigenskill-research-pack
```

Latest pushed commit:

```text
1aa8fe2 Show OLMo2 consensus repairs random16 failure
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
