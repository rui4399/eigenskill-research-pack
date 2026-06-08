# Official PTQ Runtime Profile Gate

Date: `2026-06-08T10:36:12+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `42126`
- mean tokens/s across variants: `8.3292`
- mean TTFT across variants: `0.244417` s
- peak guard VRAM ratio: `0.8794`
- peak guard VRAM MiB: `7168`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 14042 | 10.8232 | 0.153977 | 0.8138 | 6633 | `mmlu` |
| `fp16` | 1 | 14042 | 4.9773 | 0.396824 | 0.8794 | 7168 | `mmlu` |
| `gptqmodel` | 1 | 14042 | 9.1870 | 0.182449 | 0.7566 | 6167 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.1745 | 0.3880 | 0.9254 |
| `gptqmodel` | 1.8458 | 0.4598 | 0.8604 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local full-MMLU prefix14042 task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
