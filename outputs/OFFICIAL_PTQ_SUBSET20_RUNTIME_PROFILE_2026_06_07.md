# Official PTQ Runtime Profile Gate

Date: `2026-06-07T02:16:13+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `6`
- total tasks: `120`
- mean tokens/s across variants: `14.7072`
- mean TTFT across variants: `0.302620` s
- peak guard VRAM ratio: `0.6131`
- peak guard VRAM MiB: `4997`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 2 | 40 | 4.8116 | 0.417919 | 0.5543 | 4518 | `gsm8k,mmlu` |
| `fp16` | 2 | 40 | 30.5042 | 0.145992 | 0.6131 | 4997 | `gsm8k,mmlu` |
| `gptqmodel` | 2 | 40 | 8.8057 | 0.343950 | 0.5504 | 4486 | `gsm8k,mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 0.1577 | 2.8626 | 0.9041 |
| `gptqmodel` | 0.2887 | 2.3559 | 0.8977 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ 20-row matched public MMLU/GSM8K subsets, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
