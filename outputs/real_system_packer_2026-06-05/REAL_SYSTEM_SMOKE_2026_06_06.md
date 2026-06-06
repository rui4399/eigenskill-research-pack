# Real-System Smoke Sweep, 2026-06-06

This run was executed on the local RTX 5070 Laptop GPU through
`train_python/run_real_system_sweep.py` with `--max-memory-ratio 0.90`.

Artifacts:

- Raw sweep directory: `outputs/real_system_packer_2026-06-05/smoke_2026_06_06/`
- Summary: `outputs/real_system_packer_2026-06-05/smoke_2026_06_06/REAL_SYSTEM_SWEEP_SUMMARY.md`

## Environment Guard

- GPU: NVIDIA GeForce RTX 5070 Laptop GPU
- VRAM total: 8151 MiB
- Max observed guard VRAM in Triton sweep: 3502 MiB
- Max observed guard VRAM ratio: about 0.43
- C drive free space during run: about 20.0 GB
- All six Triton configs and all six C++ ESMP module runtime cases completed.

## Triton GPU Result

The grouped mixed INT4/INT8 Triton prototype compresses weights by about
`3.50x-3.74x` versus FP16 storage, but it does not yet beat PyTorch FP16 matmul
on these smoke shapes.

Observed grouped speedup versus torch FP16:

| shape | batch | high_every | grouped/FP16 |
|---|---:|---:|---:|
| 2048x1024 | 1 | 16 | 0.3752 |
| 2048x1024 | 4 | 16 | 0.2831 |
| 2048x1024 | 16 | 16 | 0.4893 |
| 2048x1024 | 16 | 8 | 0.2320 |
| 3072x1024 | 8 | 16 | 0.3534 |
| 1024x3072 | 8 | 16 | 0.3921 |

Interpretation: this is useful negative systems evidence. The current Triton
kernel proves packed-storage execution and correctness, but the next kernel
work must reduce unpack/dequant overhead or fuse into a larger transformer path
before claiming GPU speedup.

## C++ ESMP Runtime Result

The module-level CPU ESMP runtime shows the selected-row path is much faster
than full mixed GEMV for 64 active rows.

| module | shape | avg bits | compression vs FP32 | selected/full speedup |
|---|---:|---:|---:|---:|
| layer0 q_proj | 2048x1024 | 4.0 | 7.6413x | 30.9510x |
| layer0 v_proj | 1024x1024 | 8.0 | 3.9082x | 15.3448x |
| layer0 gate_proj | 3072x1024 | 4.0 | 7.6415x | 44.2176x |
| layer0 down_proj | 1024x3072 | 8.0 | 3.9689x | 17.0125x |
| layer10 q_proj | 2048x1024 | 4.0 | 7.6413x | 31.6182x |
| layer10 gate_proj | 3072x1024 | 4.0 | 7.6415x | 47.3512x |

Interpretation: this supports the micro-kernel claim only at module level. It
is not yet end-to-end TTFT or tokens-per-second evidence.

## Claim Boundary

This smoke sweep is strong enough to justify continuing the ESMP artifact path:

1. The binary format is real and readable by both C++ and Python.
2. The GPU prototype gives honest negative/diagnostic evidence.
3. The C++ selected-row path gives a concrete module-level systems signal.

It is not sufficient for a CCF-A or ICLR claim. The next required evidence is
end-to-end generation latency with clear TTFT/tokens-per-second/memory deltas,
plus stronger quantization baselines.
