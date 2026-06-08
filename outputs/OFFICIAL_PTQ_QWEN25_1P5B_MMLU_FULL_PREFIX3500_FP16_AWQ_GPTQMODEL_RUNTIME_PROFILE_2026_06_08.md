# Official PTQ Runtime Profile Gate

Date: `2026-06-08T02:24:05+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `10500`
- mean tokens/s across variants: `8.2129`
- mean TTFT across variants: `0.256150` s
- peak guard VRAM ratio: `0.8730`
- peak guard VRAM MiB: `7116`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 3500 | 10.8438 | 0.160563 | 0.7694 | 6271 | `mmlu` |
| `fp16` | 1 | 3500 | 4.8743 | 0.419125 | 0.8730 | 7116 | `mmlu` |
| `gptqmodel` | 1 | 3500 | 8.9205 | 0.188762 | 0.7232 | 5895 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.2247 | 0.3831 | 0.8813 |
| `gptqmodel` | 1.8301 | 0.4504 | 0.8284 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local full-MMLU prefix3500 task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
