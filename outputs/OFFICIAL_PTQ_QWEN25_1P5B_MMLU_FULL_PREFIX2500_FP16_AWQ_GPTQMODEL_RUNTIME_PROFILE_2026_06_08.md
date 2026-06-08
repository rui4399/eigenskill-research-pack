# Official PTQ Runtime Profile Gate

Date: `2026-06-08T01:37:50+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `7500`
- mean tokens/s across variants: `8.4015`
- mean TTFT across variants: `0.256090` s
- peak guard VRAM ratio: `0.8730`
- peak guard VRAM MiB: `7116`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 2500 | 11.2880 | 0.154709 | 0.7694 | 6271 | `mmlu` |
| `fp16` | 1 | 2500 | 4.9436 | 0.423534 | 0.8730 | 7116 | `mmlu` |
| `gptqmodel` | 1 | 2500 | 8.9728 | 0.190026 | 0.7232 | 5895 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.2833 | 0.3653 | 0.8813 |
| `gptqmodel` | 1.8150 | 0.4487 | 0.8284 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local full-MMLU prefix2500 task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
