# Official PTQ Runtime Profile Gate

Date: `2026-06-08T02:02:58+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `9000`
- mean tokens/s across variants: `8.3454`
- mean TTFT across variants: `0.253617` s
- peak guard VRAM ratio: `0.8730`
- peak guard VRAM MiB: `7116`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 3000 | 11.1693 | 0.152503 | 0.7694 | 6271 | `mmlu` |
| `fp16` | 1 | 3000 | 4.8991 | 0.420055 | 0.8730 | 7116 | `mmlu` |
| `gptqmodel` | 1 | 3000 | 8.9680 | 0.188292 | 0.7232 | 5895 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.2799 | 0.3631 | 0.8813 |
| `gptqmodel` | 1.8305 | 0.4483 | 0.8284 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local full-MMLU prefix3000 task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
