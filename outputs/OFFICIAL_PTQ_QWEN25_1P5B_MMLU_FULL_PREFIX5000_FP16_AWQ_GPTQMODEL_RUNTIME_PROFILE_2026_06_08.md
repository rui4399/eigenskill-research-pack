# Official PTQ Runtime Profile Gate

Date: `2026-06-08T03:39:22+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `15000`
- mean tokens/s across variants: `8.1751`
- mean TTFT across variants: `0.254670` s
- peak guard VRAM ratio: `0.8730`
- peak guard VRAM MiB: `7116`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 5000 | 10.8964 | 0.157726 | 0.7694 | 6271 | `mmlu` |
| `fp16` | 1 | 5000 | 4.8454 | 0.417038 | 0.8730 | 7116 | `mmlu` |
| `gptqmodel` | 1 | 5000 | 8.7835 | 0.189247 | 0.7232 | 5895 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.2488 | 0.3782 | 0.8813 |
| `gptqmodel` | 1.8127 | 0.4538 | 0.8284 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local full-MMLU prefix5000 task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
