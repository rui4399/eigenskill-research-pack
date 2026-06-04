# EigenSkill-Q C++ Quant Kernel Benchmark Report

Date: 2026-06-04

## Scope

This report records a standalone Windows/MSVC C++ microbenchmark. It is not an
integrated LLM runtime and does not measure ARM/NPU energy or board latency.

Benchmarked paths:

- FP32 dense GEMV
- packed INT4 dequant GEMV with per-row scales
- policy-selected output-row GEMV
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
d=512,  rows=16:  dense=0.151746 ms, int4=0.229690 ms, selected=0.004738 ms, scalar=0.000027 ms
d=1024, rows=16:  dense=0.651000 ms, int4=0.894527 ms, selected=0.010067 ms, scalar=0.000027 ms
d=2048, rows=16:  dense=2.748290 ms, int4=3.712570 ms, selected=0.020900 ms, scalar=0.000055 ms
d=2048, rows=256: dense=2.610602 ms, int4=4.688614 ms, selected=0.323324 ms, scalar=0.000069 ms
```

## Interpretation

The packed INT4 path is slower than the FP32 dense path in this naive CPU
implementation because nibble unpacking and scalar dequantization dominate the
saved memory traffic. This is useful negative evidence: INT4 storage alone is
not a speed claim without a vectorized or hardware-native dot-product kernel.

The selected-row path is much faster when the policy needs only a small subset
of output rows. For `d=2048, rows=16`, selected-row GEMV is about `131.50x`
faster than full dense GEMV while exactly matching the corresponding dense rows.

The scalar bypass path measures the idealized `O(d)` case and should be treated
as an arithmetic ceiling, not as proof that a Transformer layer can be replaced
by `lambda x` after nonlinear blocks.

## Next Engineering Step

The next C++ step should replace scalar INT4 unpack/dequant with an AVX2/NEON
dot kernel or route through a backend that has native low-bit matrix-vector
support. Until that exists, the project should not claim INT4 kernel speedup.
