# Official PTQ Runtime Profile Gate

Date: `2026-06-08T08:02:29+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `36000`
- mean tokens/s across variants: `8.3343`
- mean TTFT across variants: `0.248223` s
- peak guard VRAM ratio: `0.8794`
- peak guard VRAM MiB: `7168`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 12000 | 10.8106 | 0.157657 | 0.8138 | 6633 | `mmlu` |
| `fp16` | 1 | 12000 | 4.9771 | 0.401457 | 0.8794 | 7168 | `mmlu` |
| `gptqmodel` | 1 | 12000 | 9.2153 | 0.185555 | 0.7566 | 6167 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.1720 | 0.3927 | 0.9254 |
| `gptqmodel` | 1.8515 | 0.4622 | 0.8604 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local full-MMLU prefix12000 task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
