# Official PTQ Runtime Profile Gate

Date: `2026-06-08T03:16:07+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `13500`
- mean tokens/s across variants: `8.2170`
- mean TTFT across variants: `0.255292` s
- peak guard VRAM ratio: `0.8730`
- peak guard VRAM MiB: `7116`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 4500 | 10.9480 | 0.158347 | 0.7694 | 6271 | `mmlu` |
| `fp16` | 1 | 4500 | 4.8561 | 0.417594 | 0.8730 | 7116 | `mmlu` |
| `gptqmodel` | 1 | 4500 | 8.8469 | 0.189934 | 0.7232 | 5895 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.2545 | 0.3792 | 0.8813 |
| `gptqmodel` | 1.8218 | 0.4548 | 0.8284 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local full-MMLU prefix4500 task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
