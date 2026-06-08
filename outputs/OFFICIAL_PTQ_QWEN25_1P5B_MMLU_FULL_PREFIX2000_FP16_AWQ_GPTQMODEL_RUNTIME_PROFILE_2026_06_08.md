# Official PTQ Runtime Profile Gate

Date: `2026-06-08T01:08:57+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `6000`
- mean tokens/s across variants: `8.1696`
- mean TTFT across variants: `0.253768` s
- peak guard VRAM ratio: `0.8730`
- peak guard VRAM MiB: `7116`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 2000 | 10.8575 | 0.152379 | 0.7694 | 6271 | `mmlu` |
| `fp16` | 1 | 2000 | 4.8733 | 0.419905 | 0.8730 | 7116 | `mmlu` |
| `gptqmodel` | 1 | 2000 | 8.7780 | 0.189020 | 0.7232 | 5895 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.2280 | 0.3629 | 0.8813 |
| `gptqmodel` | 1.8012 | 0.4501 | 0.8284 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ local full-MMLU first 2000-row task evidence, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
