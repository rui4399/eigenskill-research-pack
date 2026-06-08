# Official PTQ Runtime Profile Gate

Date: `2026-06-08T04:24:18+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `18000`
- mean tokens/s across variants: `8.1407`
- mean TTFT across variants: `0.255897` s
- peak guard VRAM ratio: `0.8730`
- peak guard VRAM MiB: `7116`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 6000 | 10.7409 | 0.161641 | 0.7890 | 6431 | `mmlu` |
| `fp16` | 1 | 6000 | 4.8318 | 0.417520 | 0.8730 | 7116 | `mmlu` |
| `gptqmodel` | 1 | 6000 | 8.8492 | 0.188530 | 0.7352 | 5993 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.2229 | 0.3871 | 0.9037 |
| `gptqmodel` | 1.8314 | 0.4515 | 0.8422 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local full-MMLU prefix6000 task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
