# Official PTQ Runtime Profile Gate

Date: `2026-06-08T04:44:21+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `19500`
- mean tokens/s across variants: `8.1441`
- mean TTFT across variants: `0.254086` s
- peak guard VRAM ratio: `0.8760`
- peak guard VRAM MiB: `7140`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 6500 | 10.7132 | 0.160706 | 0.7890 | 6431 | `mmlu` |
| `fp16` | 1 | 6500 | 4.8411 | 0.414129 | 0.8760 | 7140 | `mmlu` |
| `gptqmodel` | 1 | 6500 | 8.8778 | 0.187424 | 0.7359 | 5998 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.2130 | 0.3881 | 0.9007 |
| `gptqmodel` | 1.8338 | 0.4526 | 0.8401 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local full-MMLU prefix6500 task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
