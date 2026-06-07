# RTX 5070 Large-Shape Triton Mixed-GEMM Diagnostic

Date: 2026-06-07

This report follows the initial RTX 5070 mixed-GEMM baseline with a narrower
large-shape probe. It targets a 4096 x 4096 weight matrix with batch 128, which
is closer to transformer projection shapes than the small positive smoke
shapes. The result is deliberately treated as a negative systems diagnostic,
not as an acceleration claim.

## What Changed

- `train_python/triton_mixed_gemm.py` now supports `--repeats` and reports
  median latency plus raw timing samples.
- `train_python/tune_triton_blocks.py` forwards `--repeats` to the kernel
  benchmark, allowing tuning summaries to use repeated measurements.
- The Windows CLI path now remains importable without Triton installed; actual
  CUDA execution still requires Triton and a CUDA device.

## Large-Shape Sweep

The first sweep tested 27 block configurations:

- shape: 4096 x 4096
- batch: 128
- high-bit pattern: every 16th row is INT8, remaining rows are INT4
- block grid: `BM in {16,32,64}`, `BN in {16,32,64}`, `BK in {32,64,128}`
- guard: 85% VRAM

Best single-pass result:

| metric | value |
|---|---:|
| best config | BM=32, BN=32, BK=64 |
| grouped mixed latency | 0.193985 ms |
| torch FP16 latency | 0.131448 ms |
| grouped / FP16 speedup | 0.6776x |
| grouped / row-wise speedup | 19.3682x |
| compression vs FP16 weights | 3.7492x |
| max guard VRAM ratio | 0.7294 |

The companion large-shape gate intentionally failed a 0.70x threshold:

```text
best grouped/FP16 speedup 0.677622568924967 < 0.7
```

## High-Bit-Ratio Probe With Repeated Timing

The second probe fixed the best coarse block family and varied the INT8 row
frequency under median-of-3 timing:

- shape: 4096 x 4096
- batch: 128
- high-bit pattern: every 8, 16, 32, or 64 rows
- block grid: `BM=32`, `BN in {32,64}`, `BK=64`
- timing: `--repeats 3`
- guard: 85% VRAM

Best repeated result:

| metric | value |
|---|---:|
| best config | high_every=64, BM=32, BN=64, BK=64 |
| grouped mixed latency | 0.221938 ms |
| torch FP16 latency | 0.147494 ms |
| grouped / FP16 speedup | 0.6646x |
| grouped / row-wise speedup | 16.1365x |
| compression vs FP16 weights | 3.9215x |
| max guard VRAM ratio | 0.5220 |

The repeated probe passes only as a negative diagnostic gate: all eight tested
configs beat the row-wise dynamic path, but none beats torch FP16.

## Interpretation

The current grouped path has solved the most obvious dynamic-dispatch problem:
it is 16-19x faster than the row-wise mixed-precision path for this large
shape. However, it still loses to torch FP16 on the same RTX 5070. This means
the remaining bottleneck is structural rather than a simple block-size choice.

The next kernel milestone should not be another broad parameter sweep. It
should change the computation layout:

1. fuse INT4 unpack, scale application, and dot accumulation more tightly;
2. reduce or eliminate the separate INT4/INT8 launch split where possible;
3. test Tensor Core-compatible dequantize-to-tile layouts instead of scalarized
   nibble unpack inside the innermost K loop;
4. report median-of-repeats latency, raw samples, compression, and guarded VRAM
   together for every claim.

## Artifacts

- `outputs/rtx5070_large_shape_tuning_2026_06_07/TRITON_BLOCK_TUNING_SUMMARY.md`
- `outputs/rtx5070_large_shape_tuning_2026_06_07/triton_large_shape_gate.json`
- `outputs/rtx5070_large_shape_tuning_2026_06_07/tuning_results.jsonl`
- `outputs/rtx5070_large_shape_high_every_repeat3_2026_06_07/TRITON_BLOCK_TUNING_SUMMARY.md`
- `outputs/rtx5070_large_shape_high_every_repeat3_2026_06_07/TRITON_HIGH_EVERY_REPEAT3_GATE.md`
- `outputs/rtx5070_large_shape_high_every_repeat3_2026_06_07/triton_high_every_repeat3_gate.json`
- `outputs/rtx5070_large_shape_high_every_repeat3_2026_06_07/tuning_results.jsonl`

## Claim Boundary

Valid claim: for a 4096 x 4096, batch-128 RTX 5070 probe, the grouped packed
INT4/INT8 Triton path is much faster than the row-wise mixed path and achieves
3.7-3.9x weight-payload compression, but remains slower than torch FP16.

Invalid claim: this proves end-to-end LLM speedup, Tensor Core acceleration,
mobile performance, energy savings, or production runtime readiness.
