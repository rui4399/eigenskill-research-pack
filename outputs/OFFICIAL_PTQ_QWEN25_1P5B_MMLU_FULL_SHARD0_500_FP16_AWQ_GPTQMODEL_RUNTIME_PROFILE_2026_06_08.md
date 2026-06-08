# Official PTQ Runtime Profile Gate

Date: `2026-06-08T00:05:18+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `1500`
- mean tokens/s across variants: `7.9777`
- mean TTFT across variants: `0.243527` s
- peak guard VRAM ratio: `0.8730`
- peak guard VRAM MiB: `7116`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 500 | 10.5848 | 0.144740 | 0.7694 | 6271 | `mmlu` |
| `fp16` | 1 | 500 | 4.8933 | 0.399046 | 0.8730 | 7116 | `mmlu` |
| `gptqmodel` | 1 | 500 | 8.4550 | 0.186795 | 0.7149 | 5827 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.1631 | 0.3627 | 0.8813 |
| `gptqmodel` | 1.7279 | 0.4681 | 0.8189 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local full-MMLU first 500-row task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
