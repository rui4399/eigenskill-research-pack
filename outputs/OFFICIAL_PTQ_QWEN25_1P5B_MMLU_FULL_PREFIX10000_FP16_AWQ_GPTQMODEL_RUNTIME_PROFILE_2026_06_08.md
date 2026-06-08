# Official PTQ Runtime Profile Gate

Date: `2026-06-08T06:25:28+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `30000`
- mean tokens/s across variants: `8.3957`
- mean TTFT across variants: `0.249426` s
- peak guard VRAM ratio: `0.8794`
- peak guard VRAM MiB: `7168`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 10000 | 11.0766 | 0.155344 | 0.8138 | 6633 | `mmlu` |
| `fp16` | 1 | 10000 | 4.9898 | 0.406312 | 0.8794 | 7168 | `mmlu` |
| `gptqmodel` | 1 | 10000 | 9.1207 | 0.186622 | 0.7566 | 6167 | `mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 2.2199 | 0.3823 | 0.9254 |
| `gptqmodel` | 1.8279 | 0.4593 | 0.8604 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ matched Qwen2.5-1.5B local full-MMLU prefix10000 task evidence for FP16, AutoAWQ, and GPTQModel, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
