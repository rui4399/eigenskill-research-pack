# Official PTQ Runtime Profile Gate

Date: `2026-06-07T21:19:40+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `2400`
- mean tokens/s across variants: `9.9195`
- mean TTFT across variants: `0.317215` s
- peak guard VRAM ratio: `0.8295`
- peak guard VRAM MiB: `6761`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 800 | 13.7211 | 0.198943 | 0.7391 | 6024 | `gsm8k` |
| `fp16` | 1 | 800 | 5.1468 | 0.495307 | 0.8295 | 6761 | `gsm8k` |
| `gptqmodel` | 1 | 800 | 10.8905 | 0.257396 | 0.6791 | 5535 | `gsm8k` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.6659 | 0.4017 | 0.8910 |
| `gptqmodel` | 2.1160 | 0.5197 | 0.8187 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local GSM8K800 task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
