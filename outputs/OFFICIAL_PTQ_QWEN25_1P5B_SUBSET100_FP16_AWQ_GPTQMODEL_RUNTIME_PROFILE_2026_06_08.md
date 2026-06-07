# Official PTQ Runtime Profile Gate

Date: `2026-06-07T19:11:52+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `6`
- total tasks: `600`
- mean tokens/s across variants: `13.5818`
- mean TTFT across variants: `0.191775` s
- peak guard VRAM ratio: `0.8013`
- peak guard VRAM MiB: `6531`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 2 | 200 | 11.7637 | 0.208924 | 0.6035 | 4919 | `gsm8k,mmlu` |
| `fp16` | 2 | 200 | 18.3348 | 0.130220 | 0.8013 | 6531 | `gsm8k,mmlu` |
| `gptqmodel` | 2 | 200 | 10.6469 | 0.236180 | 0.6672 | 5438 | `gsm8k,mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 0.6416 | 1.6044 | 0.7532 |
| `gptqmodel` | 0.5807 | 1.8137 | 0.8326 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local subset100 task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
