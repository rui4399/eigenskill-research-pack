# EigenSkill C++ Artifacts

This directory contains standalone C++ artifacts for EigenSkill. They do not
depend on llama.cpp, RKNN, ExecuTorch, or any model runtime.

## Low-Rank GEMV Microbenchmark

The first artifact isolates the core low-rank arithmetic claim:

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

## Build With CMake

The same three C++ artifacts can also be built with CMake on Linux/WSL:

```bash
cmake -S inference_cpp -B inference_cpp/build-wsl -DCMAKE_BUILD_TYPE=Release
cmake --build inference_cpp/build-wsl -j
```

Executables:

```text
inference_cpp/build-wsl/eigenskill_bench
inference_cpp/build-wsl/quant_policy_bypass
inference_cpp/build-wsl/quant_kernel_bench
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

## Quantization-Policy Bypass Evaluator

The second artifact is a deterministic C++ evaluator for the v1
quantization-policy skills:

```text
outlier_detect
bit_allocate
rotation_select
residual_patch
kv_policy
```

It parses the committed JSONL split, applies the same policy rules as
`train_python/hybrid_eval_quant_policy.py`, and reports whether the
decision-bearing fields match the gold JSON. This is a policy-kernel evaluator,
not a general JSON parser and not an integrated LLM runtime.

### Build

```powershell
powershell -ExecutionPolicy Bypass -File .\inference_cpp\build-msvc.ps1 -Target quant-policy
```

Output:

```text
inference_cpp\build\quant_policy_bypass.exe
```

### Run

```powershell
.\inference_cpp\build\quant_policy_bypass.exe `
  --data data_eval\eigenskill_quant_v1\eval.jsonl `
  --out outputs\eigenskill_quant_v1_eval_cpp_policy_summary.json

.\inference_cpp\build\quant_policy_bypass.exe `
  --data data_eval\eigenskill_quant_v1\test.jsonl `
  --out outputs\eigenskill_quant_v1_test_cpp_policy_summary.json
```

Verified local Windows/MSVC result:

```text
eval: n=400, policy_fields_exact=1.0, decision_exact=1.0, parse_error=0.0
test: n=400, policy_fields_exact=1.0, decision_exact=1.0, parse_error=0.0
```

The Python evaluator remains the stricter full JSON baseline because it checks
auxiliary numeric fields such as `risk` and `score`. The C++ evaluator is scoped
to the fields that determine the downstream quantization-policy decision.

## Quant Kernel Microbenchmark

The third artifact benchmarks four standalone kernel shapes that matter for the
quantization-policy direction:

```text
fp32 dense GEMV             full d x d floating-point matrix-vector multiply
packed int4 dequant GEMV    row-scale INT4 weights unpacked during GEMV
selected-row GEMV           only a policy-selected subset of output rows
scalar skill bypass         y = lambda x, the O(d) idealized eigen-skill path
```

This is still a microbenchmark, not an integrated LLM runtime. It does verify
the C++ implementation surface for packed INT4 weights and dynamic row subsets,
which the earlier low-rank benchmark did not cover.

### Build

```powershell
powershell -ExecutionPolicy Bypass -File .\inference_cpp\build-msvc.ps1 -Target quant-kernel
```

Output:

```text
inference_cpp\build\quant_kernel_bench.exe
```

### Run

```powershell
.\inference_cpp\build\quant_kernel_bench.exe --dims 512,1024,2048 --active-rows 16,64,256 --iters 200
```

Output columns:

```text
d            hidden dimension / square matrix size
rows         selected output rows for selected-row GEMV
dense_ms     FP32 dense GEMV latency
int4_ms      packed INT4 dequant GEMV latency
sel_ms       selected-row GEMV latency
scalar_ms    y = lambda x latency
int4_x       dense_ms / int4_ms
sel_x        dense_ms / sel_ms
scalar_x     dense_ms / scalar_ms
int4_err     relative L2 error of INT4 output versus FP32 dense output
sel_err      selected-row output error versus same rows from FP32 dense output
```
