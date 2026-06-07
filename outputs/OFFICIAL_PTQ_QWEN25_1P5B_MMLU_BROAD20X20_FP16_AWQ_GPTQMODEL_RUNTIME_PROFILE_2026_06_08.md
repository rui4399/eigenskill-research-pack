# Official PTQ Runtime Profile Gate

Date: `2026-06-07T23:12:13+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `1200`
- mean tokens/s across variants: `8.8340`
- mean TTFT across variants: `0.256271` s
- peak guard VRAM ratio: `0.8201`
- peak guard VRAM MiB: `6685`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 400 | 11.8433 | 0.157150 | 0.7265 | 5922 | `mmlu` |
| `fp16` | 1 | 400 | 5.2316 | 0.407572 | 0.8201 | 6685 | `mmlu` |
| `gptqmodel` | 1 | 400 | 9.4272 | 0.204092 | 0.6921 | 5641 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.2638 | 0.3856 | 0.8859 |
| `gptqmodel` | 1.8020 | 0.5007 | 0.8438 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local MMLU broad20x20 task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
