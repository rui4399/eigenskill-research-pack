# Official PTQ Runtime Profile Gate

Date: `2026-06-07T22:28:25+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `600`
- mean tokens/s across variants: `8.8134`
- mean TTFT across variants: `0.245115` s
- peak guard VRAM ratio: `0.8189`
- peak guard VRAM MiB: `6675`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 200 | 11.7995 | 0.149837 | 0.7235 | 5897 | `mmlu` |
| `fp16` | 1 | 200 | 5.2627 | 0.397696 | 0.8189 | 6675 | `mmlu` |
| `gptqmodel` | 1 | 200 | 9.3779 | 0.187812 | 0.6849 | 5583 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.2421 | 0.3768 | 0.8834 |
| `gptqmodel` | 1.7820 | 0.4723 | 0.8364 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ guarded local ten-subject 200-row MMLU retention, not full leaderboard, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
