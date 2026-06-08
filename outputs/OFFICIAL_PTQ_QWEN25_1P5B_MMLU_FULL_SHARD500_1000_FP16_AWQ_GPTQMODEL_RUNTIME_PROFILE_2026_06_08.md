# Official PTQ Runtime Profile Gate

Date: `2026-06-08T00:28:49+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `1500`
- mean tokens/s across variants: `7.7342`
- mean TTFT across variants: `0.250158` s
- peak guard VRAM ratio: `0.8457`
- peak guard VRAM MiB: `6893`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 500 | 10.1841 | 0.148652 | 0.7530 | 6138 | `mmlu` |
| `fp16` | 1 | 500 | 4.6074 | 0.420318 | 0.8457 | 6893 | `mmlu` |
| `gptqmodel` | 1 | 500 | 8.4111 | 0.181505 | 0.7099 | 5786 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.2104 | 0.3537 | 0.8905 |
| `gptqmodel` | 1.8256 | 0.4318 | 0.8394 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ local full-MMLU second 500-row task evidence, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
