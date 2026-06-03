# EigenSkill C++ Microbenchmark Implementation Report

Date: 2026-06-02

## What Was Implemented

Implemented the first EigenSkill systems artifact:

```text
dense path: y = W x
skill path: z = U^T x; z2 = A z; y = U z2
```

Location:

```text
inference_cpp/
```

Files:

```text
inference_cpp/src/eigenskill_bench.cpp
inference_cpp/build-msvc.ps1
inference_cpp/README.md
```

The implementation is intentionally standalone. It does not depend on
llama.cpp, RKNN, ExecuTorch, ONNX Runtime, or any model runtime. This isolates
the core systems claim before integrating with full inference frameworks.

## Kernel Design

Dense baseline:

```text
W: d x d
x: d
y = W x
cost: O(d^2)
```

Low-rank EigenSkill path:

```text
U: d x k
A: k x k
z = U^T x
z2 = A z
y = U z2
cost: O(dk + k^2 + dk)
```

The benchmark constructs:

```text
W = U A U^T
```

so the low-rank path is mathematically equivalent to the dense path up to
floating-point accumulation error. This measures the best-case execution ceiling
for a trained EigenSkill bypass.

## Benchmark Result

Output saved at:

```text
outputs/eigenskill_cpp_benchmark.txt
```

Representative results:

```text
d=512,  k=4:  dense 0.158000 ms, skill 0.001976 ms, speedup 79.96x
d=1024, k=4:  dense 0.668580 ms, skill 0.003935 ms, speedup 169.89x
d=2048, k=4:  dense 2.770634 ms, skill 0.008564 ms, speedup 323.51x
d=2048, k=16: dense 2.652209 ms, skill 0.030829 ms, speedup 86.03x
d=2048, k=32: dense 2.762792 ms, skill 0.063888 ms, speedup 43.24x
```

Relative L2 error was around `1e-6`, matching the synthetic low-rank ground
truth within floating-point error.

## Interpretation

This benchmark does not prove that a real Transformer layer can always be
bypassed. It proves a narrower systems claim:

```text
If training exposes a reliable skill-conditioned low-rank subspace, then the
corresponding C++ low-rank execution path can be orders of magnitude faster than
materializing the equivalent dense GEMV.
```

The next research question is therefore training-side:

```text
Can Eigen-Regularization learn U and A for selected FFN layers while preserving
task accuracy on narrow skills such as Intent Routing and JSON Repair?
```

## Next Step

Recommended next implementation:

```text
train_python/
  dataset generator for intent routing and JSON repair
  SmolLM2-360M baseline fine-tuning
  Eigen-Regularization loss for selected FFN projections
  export learned U/A matrices for the C++ microbenchmark
```

