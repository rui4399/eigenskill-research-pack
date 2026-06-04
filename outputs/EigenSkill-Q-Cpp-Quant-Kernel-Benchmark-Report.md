# EigenSkill-Q C++ Quant Kernel Benchmark Report

Date: 2026-06-04

## Scope

This report records a standalone Windows/MSVC C++ microbenchmark. It is not an
integrated LLM runtime and does not measure ARM/NPU energy or board latency.

Benchmarked paths:

- scalar FP32 dense GEMV
- AVX2 FP32 dense GEMV when available
- packed INT4 dequant GEMV with per-row scales
- scalar policy-selected output-row GEMV
- AVX2 policy-selected output-row GEMV when available
- scalar skill bypass, `y = lambda x`

Command:

```powershell
powershell -ExecutionPolicy Bypass -File .\inference_cpp\build-msvc.ps1 -Target quant-kernel
.\inference_cpp\build\quant_kernel_bench.exe --dims 512,1024,2048 --active-rows 16,64,256 --iters 200
```

Evidence:

```text
outputs/eigenskill_quant_kernel_benchmark.txt
```

Compiler-optimization guard: the benchmark marks the core kernels `noinline` and
reads one output element during each warmup/timed iteration to keep stores live.

The same C++ tree was also built with CMake/g++ 11.4 under WSL:

```bash
cmake -S inference_cpp -B inference_cpp/build-wsl -DCMAKE_BUILD_TYPE=Release
cmake --build inference_cpp/build-wsl -j
./inference_cpp/build-wsl/quant_kernel_bench --dims 256 --active-rows 16,64 --iters 50
./inference_cpp/build-wsl/quant_policy_bypass --data data_eval/eigenskill_quant_v1/eval.jsonl --limit 20
```

Both smoke runs completed successfully.

## Selected Results

```text
d=512,  rows=16:  dense=0.159312 ms, dense_avx2=0.018234 ms, int4=0.225300 ms, selected_avx2=0.000536 ms
d=1024, rows=16:  dense=0.632122 ms, dense_avx2=0.067346 ms, int4=0.958060 ms, selected_avx2=0.001083 ms
d=2048, rows=16:  dense=2.591152 ms, dense_avx2=0.369847 ms, int4=3.986131 ms, selected_avx2=0.002425 ms
d=2048, rows=256: dense=2.620207 ms, dense_avx2=0.342829 ms, int4=4.547568 ms, selected_avx2=0.044658 ms
```

Summary:

```text
best dense AVX2 speedup vs scalar dense:      10.26x
packed INT4 faster than scalar dense:         0/9 cases
best scalar selected-row speedup:             121.66x
best AVX2 selected-row speedup:               1068.52x
max dense AVX2 relative error vs scalar:      8.762e-07
max selected AVX2 relative error vs scalar:   1.511e-06
```

## Interpretation

The packed INT4 path is slower than the FP32 dense path in this naive CPU
implementation because nibble unpacking and scalar dequantization dominate the
saved memory traffic. This is useful negative evidence: INT4 storage alone is
not a speed claim without a vectorized or hardware-native dot-product kernel.

The selected-row path is much faster when the policy needs only a small subset
of output rows. For `d=2048, rows=16`, AVX2 selected-row GEMV is about
`1068.52x` faster than scalar full dense GEMV while matching the corresponding
dense rows up to floating-point accumulation error.

The scalar bypass path measures the idealized `O(d)` case and should be treated
as an arithmetic ceiling, not as proof that a Transformer layer can be replaced
by `lambda x` after nonlinear blocks.

## Next Engineering Step

The next C++ step should replace scalar INT4 unpack/dequant with a vectorized
low-bit dot kernel or route through a backend that has native low-bit
matrix-vector support. Until that exists, the project should not claim INT4
kernel speedup.
