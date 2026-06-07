# Official PTQ Runtime Profile Gate

Date: `2026-06-07T02:42:59+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `6`
- total tasks: `300`
- mean tokens/s across variants: `15.8107`
- mean TTFT across variants: `0.250121` s
- peak guard VRAM ratio: `0.6148`
- peak guard VRAM MiB: `5011`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 2 | 100 | 5.1705 | 0.359323 | 0.5539 | 4515 | `gsm8k,mmlu` |
| `fp16` | 2 | 100 | 31.7391 | 0.104508 | 0.6148 | 5011 | `gsm8k,mmlu` |
| `gptqmodel` | 2 | 100 | 10.5225 | 0.286532 | 0.5490 | 4475 | `gsm8k,mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 0.1629 | 3.4382 | 0.9010 |
| `gptqmodel` | 0.3315 | 2.7417 | 0.8930 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ 50-row matched public MMLU/GSM8K subsets, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
