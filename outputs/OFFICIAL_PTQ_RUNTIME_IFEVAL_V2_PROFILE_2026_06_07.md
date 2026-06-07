# Official PTQ Runtime Profile Gate

Date: `2026-06-07T08:48:44+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `24`
- mean tokens/s across variants: `16.5678`
- mean TTFT across variants: `0.425468` s
- peak guard VRAM ratio: `0.5113`
- peak guard VRAM MiB: `4168`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 8 | 6.7130 | 0.586322 | 0.4536 | 3697 | `ifeval` |
| `fp16` | 1 | 8 | 30.6348 | 0.264942 | 0.5113 | 4168 | `ifeval` |
| `gptqmodel` | 1 | 8 | 12.3554 | 0.425140 | 0.4518 | 3683 | `ifeval` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 0.2191 | 2.2130 | 0.8870 |
| `gptqmodel` | 0.4033 | 1.6047 | 0.8836 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ deterministic IFEval-style instruction-following v2 tasks, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
