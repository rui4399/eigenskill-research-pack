# Official PTQ Runtime Profile Gate

Date: `2026-06-08T00:30:43+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `3000`
- mean tokens/s across variants: `7.8559`
- mean TTFT across variants: `0.246843` s
- peak guard VRAM ratio: `0.8730`
- peak guard VRAM MiB: `7116`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 1000 | 10.3844 | 0.146696 | 0.7694 | 6271 | `mmlu` |
| `fp16` | 1 | 1000 | 4.7503 | 0.409682 | 0.8730 | 7116 | `mmlu` |
| `gptqmodel` | 1 | 1000 | 8.4331 | 0.184150 | 0.7149 | 5827 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.1860 | 0.3581 | 0.8813 |
| `gptqmodel` | 1.7753 | 0.4495 | 0.8189 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ local full-MMLU first 1000-row task evidence, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
