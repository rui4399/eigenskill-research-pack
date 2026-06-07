# Official PTQ Runtime Profile Gate

Date: `2026-06-07T01:47:04+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `6`
- total tasks: `24`
- mean tokens/s across variants: `11.4608`
- mean TTFT across variants: `0.508495` s
- peak guard VRAM ratio: `0.6108`
- peak guard VRAM MiB: `4979`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 2 | 8 | 3.8874 | 0.647097 | 0.5538 | 4514 | `gsm8k,mmlu` |
| `fp16` | 2 | 8 | 22.8842 | 0.385224 | 0.6108 | 4979 | `gsm8k,mmlu` |
| `gptqmodel` | 2 | 8 | 7.6109 | 0.493163 | 0.5420 | 4418 | `gsm8k,mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 0.1699 | 1.6798 | 0.9066 |
| `gptqmodel` | 0.3326 | 1.2802 | 0.8873 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ task-smoke executions, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
