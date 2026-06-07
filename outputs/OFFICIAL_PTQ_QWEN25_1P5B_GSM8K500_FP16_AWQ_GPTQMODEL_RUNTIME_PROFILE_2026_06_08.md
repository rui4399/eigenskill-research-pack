# Official PTQ Runtime Profile Gate

Date: `2026-06-07T20:57:18+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `1500`
- mean tokens/s across variants: `9.8719`
- mean TTFT across variants: `0.314835` s
- peak guard VRAM ratio: `0.8295`
- peak guard VRAM MiB: `6761`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 500 | 13.7360 | 0.197290 | 0.7391 | 6024 | `gsm8k` |
| `fp16` | 1 | 500 | 5.1042 | 0.490883 | 0.8295 | 6761 | `gsm8k` |
| `gptqmodel` | 1 | 500 | 10.7755 | 0.256331 | 0.6784 | 5530 | `gsm8k` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.6911 | 0.4019 | 0.8910 |
| `gptqmodel` | 2.1111 | 0.5222 | 0.8179 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local GSM8K500 task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
