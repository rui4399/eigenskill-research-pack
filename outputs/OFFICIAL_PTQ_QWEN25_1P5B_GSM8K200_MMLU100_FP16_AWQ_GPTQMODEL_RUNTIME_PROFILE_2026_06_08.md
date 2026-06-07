# Official PTQ Runtime Profile Gate

Date: `2026-06-07T19:33:42+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `6`
- total tasks: `900`
- mean tokens/s across variants: `9.5151`
- mean TTFT across variants: `0.291967` s
- peak guard VRAM ratio: `0.8295`
- peak guard VRAM MiB: `6761`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 2 | 300 | 12.9601 | 0.187606 | 0.7391 | 6024 | `gsm8k,mmlu` |
| `fp16` | 2 | 300 | 5.0148 | 0.453859 | 0.8295 | 6761 | `gsm8k,mmlu` |
| `gptqmodel` | 2 | 300 | 10.5705 | 0.234437 | 0.6767 | 5516 | `gsm8k,mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.5844 | 0.4134 | 0.8910 |
| `gptqmodel` | 2.1079 | 0.5165 | 0.8159 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local GSM8K200 plus MMLU100 task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
