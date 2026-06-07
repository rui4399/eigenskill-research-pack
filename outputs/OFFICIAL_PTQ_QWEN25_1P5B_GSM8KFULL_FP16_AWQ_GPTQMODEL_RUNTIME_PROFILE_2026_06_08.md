# Official PTQ Runtime Profile Gate

Date: `2026-06-07T21:36:01+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `3957`
- mean tokens/s across variants: `9.7071`
- mean TTFT across variants: `0.320392` s
- peak guard VRAM ratio: `0.8295`
- peak guard VRAM MiB: `6761`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 1319 | 13.3764 | 0.202863 | 0.7391 | 6024 | `gsm8k` |
| `fp16` | 1 | 1319 | 5.1170 | 0.496028 | 0.8295 | 6761 | `gsm8k` |
| `gptqmodel` | 1 | 1319 | 10.6277 | 0.262285 | 0.6791 | 5535 | `gsm8k` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.6141 | 0.4090 | 0.8910 |
| `gptqmodel` | 2.0769 | 0.5288 | 0.8187 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ Qwen2.5-1.5B full GSM8K PTQ retention, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
