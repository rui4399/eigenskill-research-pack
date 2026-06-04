# EigenSkill-Q C++ Mixed-Bit Kernel Stage Report

Date: 2026-06-04

## Summary

This stage adds a row-wise mixed-bit storage path to the standalone C++ kernel
artifact. It is not a production low-bit matrix multiplication kernel. It is a
systems baseline for representing policy-selected mixed precision and executing
selected output rows without materializing the full dense output.

## Added API

```text
PackedMixedBitMatrix
pack_mixed_lowbit_per_row(row_bits=2..8)
mixed_lowbit_dequant_gemv
mixed_lowbit_selected_rows_gemv
```

The existing `PackedLowBitMatrix` path now supports 2..8-bit signed row-scaled
storage. `PackedInt4Matrix` remains a compatibility wrapper over the generic
low-bit path.

## Verification

```text
cmake --build build/cpp-wsl -j2: passed
ctest --test-dir build/cpp-wsl --output-on-failure: passed
quant_kernel_verify --dim 256 --active-rows 16: ok=true
```

The verifier checks:

```text
AVX2 dense GEMV against scalar dense GEMV
selected-row GEMV against the corresponding dense rows
INT3/INT4 finite output
mixed-bit finite output
mixed-bit selected-row output against corresponding mixed full-output rows
scalar bypass against y=lambda*x
```

## Benchmark Snapshot

Benchmark command:

```bash
./build/cpp-wsl/quant_kernel_bench --dims 512,1024,2048 --active-rows 16,64,256 --iters 120 --warmup 20
```

Best mixed selected-row case:

```text
d=2048, active_rows=16
dense_ms=2.554907
dense_avx2_ms=0.303719
mixed_full_dequant_ms=11.888089
mixed_selected_ms=0.145753
mixed_selected_speedup_vs_scalar_dense=17.53x
mixed_selected_rel_l2=0.0
```

Aggregate:

```text
mixed selected-row faster than scalar dense: 7/9 cases
full mixed-bit dequant faster than scalar dense: 0/9 cases
full INT4 dequant faster than scalar dense: 0/9 cases
best AVX2 selected-row speedup: 878.42x
best scalar bypass speedup: 36568.86x
```

## Interpretation

The useful result is narrow: the repository now has a C++ path for row-wise
mixed-bit representation plus selected-row bypass. The negative result is also
important: scalar bit unpacking makes full low-bit dequant GEMV slower than
AVX2 FP32 dense GEMV. A speed claim for complete low-bit matrix multiplication
requires vectorized unpack, fused low-bit dot products, or integration with a
mature runtime.

Evidence:

```text
outputs/eigenskill_quant_kernel_mixedbit_benchmark.txt
outputs/eigenskill_quant_kernel_mixedbit_benchmark_summary.json
```
