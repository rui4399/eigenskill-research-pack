# RTX 5070 INT4 Layout Probe

Date: 2026-06-07

This report adds a layout diagnostic to the Triton mixed-GEMM track. The prior
large-shape probe showed that grouped packed INT4/INT8 removes row-wise launch
overhead but still loses to torch FP16. This probe asks whether the remaining
gap is dominated by mixed-row dispatch, nibble unpacking, or the dequantized
dot layout.

## Code Change

`train_python/triton_mixed_gemm.py` now supports three all-INT4 paths when
`--high-every 0` is selected:

| path | storage | purpose |
|---|---|---|
| `grouped_mixed` | packed W4 plus row index indirection | baseline grouped path |
| `int4_contiguous` | packed W4 with contiguous output rows | removes row-id gather/scatter overhead |
| `int4_unpacked_i8` | W4 values stored as signed int8 bytes | removes nibble unpacking while keeping the same 4-bit quantization range |

The benchmark also supports `--interleaved-timing`, which rotates benchmark
order across repeats so FP16 is not always measured last.

## Final Interleaved Probe

Configuration:

- device: NVIDIA GeForce RTX 5070 Laptop GPU
- shape: 4096 x 4096
- batch: 512
- quantization: all rows INT4 (`--high-every 0`)
- block config: BM=64, BN=128, BK=64
- timing: median over 5 interleaved repeats
- guard: 85% VRAM

| path | median latency | speed vs torch FP16 | payload compression vs FP16 | rel-L2 vs FP32 reference |
|---|---:|---:|---:|---:|
| row-wise mixed | 16.195866 ms | 0.0346x | 3.9825x | 0.157203 |
| grouped packed W4 | 0.758601 ms | 0.7392x | 3.9825x | 0.157203 |
| contiguous packed W4 | 0.665699 ms | 0.8424x | 3.9825x | 0.157203 |
| W4-as-I8 contiguous | 0.566186 ms | 0.9905x | 1.9980x | 0.157204 |
| torch FP16 | 0.560790 ms | 1.0000x | 1.0000x | reference |

Additional checks:

- contiguous packed W4 is `1.1396x` faster than grouped packed W4;
- W4-as-I8 is `1.1758x` faster than contiguous packed W4;
- W4-as-I8 and packed W4 produce the same quantized result up to
  `2.5718e-4` relative L2 under FP16-scale dequantization;
- guard peak VRAM ratio is `0.5221`, below the 85% limit.

## Interpretation

This is the strongest current RTX 5070 kernel diagnostic, but it is still not
a production acceleration claim. The result separates the bottleneck:

1. row-wise dispatch is not viable for large shapes;
2. contiguous packed W4 removes some row-index overhead but remains below FP16;
3. byte-aligned W4-as-I8 almost reaches torch FP16 while retaining about 2x
   weight-payload compression;
4. therefore the next packed-W4 milestone should target a Tensor Core-friendly
   nibble-unpack/dequant layout, not another broad block-size sweep.

## Artifacts

- `outputs/rtx5070_int4_layout_probe_2026_06_07/final_interleaved_b512/b512_bm64_bn128_bk64.json`
- `outputs/rtx5070_int4_layout_probe_2026_06_07/final_interleaved_b512/b512_bm64_bn128_bk64_guard.json`

## Claim Boundary

Valid claim: on the local RTX 5070, an interleaved timing probe shows that
byte-aligned W4-as-I8 reaches near-FP16 latency (`0.9905x`) with about 2x
weight-payload compression, while fully packed W4 keeps about 4x compression
but remains slower than FP16.

Invalid claim: this proves end-to-end LLM acceleration, stable FP16 speedup,
mobile performance, energy savings, SOTA quantization quality, or production
runtime readiness.
