# Official PTQ Runtime Profile Gate

Date: `2026-06-08T00:50:13+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `4500`
- mean tokens/s across variants: `8.0334`
- mean TTFT across variants: `0.251598` s
- peak guard VRAM ratio: `0.8730`
- peak guard VRAM MiB: `7116`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 1500 | 10.6969 | 0.152438 | 0.7694 | 6271 | `mmlu` |
| `fp16` | 1 | 1500 | 4.8378 | 0.415698 | 0.8730 | 7116 | `mmlu` |
| `gptqmodel` | 1 | 1500 | 8.5655 | 0.186657 | 0.7232 | 5895 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.2111 | 0.3667 | 0.8813 |
| `gptqmodel` | 1.7705 | 0.4490 | 0.8284 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ local full-MMLU first 1500-row task evidence, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
