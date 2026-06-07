# Official PTQ Runtime Profile Gate

Date: `2026-06-07T22:05:23+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `300`
- mean tokens/s across variants: `8.5774`
- mean TTFT across variants: `0.252645` s
- peak guard VRAM ratio: `0.8114`
- peak guard VRAM MiB: `6614`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 100 | 11.1998 | 0.154689 | 0.7209 | 5876 | `mmlu` |
| `fp16` | 1 | 100 | 5.1312 | 0.412188 | 0.8114 | 6614 | `mmlu` |
| `gptqmodel` | 1 | 100 | 9.4013 | 0.191056 | 0.6819 | 5558 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.1827 | 0.3753 | 0.8884 |
| `gptqmodel` | 1.8322 | 0.4635 | 0.8403 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ guarded local five-subject 100-row MMLU retention, not full leaderboard, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
