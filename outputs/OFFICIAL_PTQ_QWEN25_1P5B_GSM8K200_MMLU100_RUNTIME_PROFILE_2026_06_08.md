# Official PTQ Runtime Profile Gate

Date: `2026-06-07T17:31:48+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16']`
- total cases: `4`
- total tasks: `600`
- mean tokens/s across variants: `8.9874`
- mean TTFT across variants: `0.320733` s
- peak guard VRAM ratio: `0.8295`
- peak guard VRAM MiB: `6761`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 2 | 300 | 12.9601 | 0.187606 | 0.7391 | 6024 | `gsm8k,mmlu` |
| `fp16` | 2 | 300 | 5.0148 | 0.453859 | 0.8295 | 6761 | `gsm8k,mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.5844 | 0.4134 | 0.8910 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local GSM8K200 plus MMLU100 task evidence with HF FP16 offload, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
