# EigenSkill-Q C++ Quant Kernel API Report

This update moves part of the C++ quant-kernel work from a monolithic
microbenchmark into a small reusable API.

## Added API Surface

```text
inference_cpp/include/eigenskill/quant_kernels.hpp
inference_cpp/src/quant_kernels.cpp
inference_cpp/src/quant_kernel_verify.cpp
```

Covered functions:

```text
dense_gemv
dense_gemv_avx2
selected_rows_gemv
selected_rows_gemv_avx2
pack_int4_per_row
int4_dequant_gemv
scalar_skill_bypass
rel_l2_error
```

Build integration:

```text
CMake target: eigenskill_quant_kernels
CMake verifier: quant_kernel_verify
MSVC target: -Target quant-verify
```

## Verification

WSL/CMake/g++:

```text
cmake -S inference_cpp -B inference_cpp/build-wsl -DCMAKE_BUILD_TYPE=Release
cmake --build inference_cpp/build-wsl -j
./inference_cpp/build-wsl/quant_kernel_verify --dim 512 --active-rows 32
```

Windows/MSVC:

```text
powershell -ExecutionPolicy Bypass -File .\inference_cpp\build-msvc.ps1 -Target quant-verify
.\inference_cpp\build\quant_kernel_verify.exe --dim 512 --active-rows 32
```

Local MSVC verifier result:

```text
dim                         512
active rows                 32
AVX2                        true
dense AVX2 relative L2      4.2847e-07
selected-row relative L2    0
selected AVX2 relative L2   4.7130e-07
INT4 relative L2            1.3646e-01
scalar bypass relative L2   0
ok                          true
```

## Interpretation

This is a correctness and engineering-structure improvement. It makes the C++
selected-row, INT4 pack/dequant, AVX2 dot, and scalar bypass paths callable from
other C++ programs instead of only being embedded in a benchmark.

It is not a packed LLM runtime, not an ARM/NEON/NPU backend, and not an INT4
speedup claim. The previous benchmark still shows that naive packed INT4
dequant GEMV is slower than FP32 dense GEMV in this CPU implementation; the
positive systems signal remains selected-row computation and a cleaner kernel
surface for future runtime integration.

## Evidence Files

```text
inference_cpp/include/eigenskill/quant_kernels.hpp
inference_cpp/src/quant_kernels.cpp
inference_cpp/src/quant_kernel_verify.cpp
inference_cpp/CMakeLists.txt
inference_cpp/build-msvc.ps1
outputs/eigenskill_quant_kernel_verify_msvc.json
```
