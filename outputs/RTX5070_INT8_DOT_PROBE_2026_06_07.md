# RTX 5070 INT8 Dot Probe

Date: 2026-06-07

This report follows the RTX 5070 INT4 layout probe. The previous W4A16 paths
showed that contiguous storage and byte-aligned W4-as-I8 nearly close the FP16
latency gap, but packed W4 remained slower when each tile was dequantized to
FP16 before the dot product. This probe tests a delayed-dequantization path:
weights and activations are multiplied in the integer domain, and the row and
activation scales are applied only after the integer dot accumulation.

## Code Change

`train_python/triton_mixed_gemm.py` now includes two all-INT4, int8-activation
diagnostic paths for `--high-every 0`:

| path | weight storage | activation storage | dequantization point |
|---|---|---|---|
| `int4_packed_x_i8` | packed W4 nibbles plus per-row scale | per-batch signed int8 plus scale | after int32 dot |
| `int4_unpacked_i8_x_i8` | W4-range signed int8 bytes plus per-row scale | per-batch signed int8 plus scale | after int32 dot |

The first path preserves the packed-W4 weight payload. The second path removes
nibble unpacking and is useful for isolating whether packed-W4 decoding or the
integer dot itself dominates latency.

## Final Interleaved Probe

Configuration:

- device: NVIDIA GeForce RTX 5070 Laptop GPU
- shape: 4096 x 4096
- batch: 512
- quantization: all rows INT4 (`--high-every 0`)
- activation quantization: per-batch signed INT8
- block config: BM=64, BN=128, BK=64
- timing: median over 5 interleaved repeats
- guard: 85% VRAM

| path | median latency | speed vs torch FP16 | weight-payload compression vs FP16 | rel-L2 vs FP32 reference |
|---|---:|---:|---:|---:|
| row-wise mixed W4A16 | 15.194954 ms | 0.0327x | 3.9825x | 0.157203 |
| grouped packed W4A16 | 0.680555 ms | 0.7292x | 3.9825x | 0.157203 |
| contiguous packed W4A16 | 0.538864 ms | 0.9210x | 3.9825x | 0.157203 |
| W4-as-I8 W4A16 | 0.500442 ms | 0.9917x | 1.9980x | 0.157204 |
| packed W4 x INT8 activation | 0.292345 ms | 1.6976x | 3.9825x | 0.157449 |
| W4-as-I8 x INT8 activation | 0.153371 ms | 3.2358x | 1.9980x | 0.157449 |
| torch FP16 | 0.496278 ms | 1.0000x | 1.0000x | reference |

Additional checks:

- packed W4 x INT8 activation is `1.8432x` faster than contiguous packed W4A16;
- W4-as-I8 x INT8 activation is `3.2629x` faster than W4-as-I8 W4A16;
- activation quantization adds `0.0087` relative L2 compared with the packed
  W4A16 output;
- guard peak VRAM ratio is `0.5358`, below the 85% limit;
- max observed GPU utilization is 100% during the guarded run.

## Interpretation

This is the first local RTX 5070 result in this repository where a low-bit
diagnostic kernel beats the torch FP16 baseline for the large GEMM shape. The
mechanism is narrower than a production LLM claim: the kernel changes from
W4A16 to W4A8-style computation by quantizing activations to INT8, accumulating
integer dot products, and applying scales after the dot.

The result is still useful for the systems track because it identifies a viable
next kernel direction. Packed W4 storage plus delayed dequantization reaches
`1.6976x` torch FP16 while preserving about `3.9825x` weight-payload
compression. Removing nibble unpacking with W4-as-I8 reaches `3.2358x` but
halves the static compression benefit. Therefore, the next milestone is a
quality-aware packed-W4/W4A8 path and a larger shape family gate, not another
W4A16 block-size sweep.

## Shape-Family Follow-up

A bounded follow-up sweep keeps rows=4096, cols=4096, all rows INT4, and tests
two batches (128 and 512) with eight BM/BN/BK configurations. It is intentionally
small, but it checks whether the delayed-dequantization result is a single
timing accident.

Summary over 8 successful guarded runs:

| metric | min | max |
|---|---:|---:|
| packed W4 x INT8 activation speed vs torch FP16 | 1.2900x | 1.7268x |
| W4-as-I8 x INT8 activation speed vs torch FP16 | 1.4886x | 3.1372x |
| packed W4 x INT8 activation speed vs packed W4A16 | 1.6382x | 2.5382x |
| guard peak VRAM ratio | 0.6134 | 0.6219 |

Artifacts:

- `outputs/rtx5070_int8_tensorcore_probe_2026_06_07/shape_family_4096/TRITON_BLOCK_TUNING_SUMMARY.md`
- `outputs/rtx5070_int8_tensorcore_probe_2026_06_07/shape_family_4096/tuning_results.jsonl`

Machine-checkable gate:

- `outputs/W4A8_SHAPE_FAMILY_GATE_2026_06_08.md`
- `outputs/w4a8_shape_family_gate_2026_06_08.json`

## Artifacts

- `outputs/rtx5070_int8_tensorcore_probe_2026_06_07/final_interleaved_b512/b512_bm64_bn128_bk64.json`
- `outputs/rtx5070_int8_tensorcore_probe_2026_06_07/final_interleaved_b512/b512_bm64_bn128_bk64_guard.json`

## Claim Boundary

Valid claim: on the local RTX 5070, a bounded 4096 x 4096, batch-128/512
Triton shape-family probe shows that packed W4 weights with per-batch INT8
activations and delayed dequantization beat torch FP16 in all eight measured
configurations, with speedups from `1.2900x` to `1.7268x` while retaining about
`3.9825x` weight-payload compression.

Invalid claim: this proves end-to-end LLM acceleration, production runtime
readiness, mobile performance, energy savings, model-quality preservation under
activation quantization, or SOTA quantization quality.
