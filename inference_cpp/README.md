# EigenSkill C++ Microbenchmark

This is the first systems artifact for EigenSkill. It does not depend on
llama.cpp, RKNN, ExecuTorch, or any model runtime. The goal is to isolate the
core kernel claim:

```text
dense path:      y = W x
skill path:      z = U^T x; z2 = A z; y = U z2
```

The dense path costs `O(d^2)`. The low-rank skill path costs
`O(dk + k^2 + dk)`, where `k << d`.

## Build On Windows

```powershell
powershell -ExecutionPolicy Bypass -File .\inference_cpp\build-msvc.ps1
```

The script locates Visual Studio with `vswhere`, initializes the x64 MSVC
environment, and writes the executable to:

```text
inference_cpp\build\eigenskill_bench.exe
```

## Run

```powershell
.\inference_cpp\build\eigenskill_bench.exe
```

Useful options:

```text
--dims 512,1024,2048
--ks 1,4,8,16,32
--iters 200
--warmup 20
--seed 42
```

Example:

```powershell
.\inference_cpp\build\eigenskill_bench.exe --dims 1024,2048 --ks 4,8,16 --iters 300
```

## Output Columns

```text
d                  hidden dimension
k                  skill subspace dimension
dense_ms           average dense GEMV latency per iteration
skill_ms           average low-rank skill path latency per iteration
speedup            dense_ms / skill_ms
dense_gflops       approximate dense arithmetic throughput
skill_gflops       approximate low-rank arithmetic throughput
rel_l2_error       relative L2 error against W = U A U^T synthetic baseline
```

For this first benchmark, `W` is generated as `U A U^T`, so the low-rank path is
mathematically equivalent up to floating-point accumulation differences. This
intentionally measures the best-case systems ceiling. Later experiments should
add an arbitrary dense `W`, train or fit `U/A`, and report approximation error.

