# Official PTQ Runtime Profile Gate

Date: `2026-06-07T09:29:51+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `6`
- total tasks: `600`
- mean tokens/s across variants: `14.8764`
- mean TTFT across variants: `0.251615` s
- peak guard VRAM ratio: `0.5210`
- peak guard VRAM MiB: `4247`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 2 | 200 | 5.0185 | 0.356071 | 0.4530 | 3692 | `gsm8k,mmlu` |
| `fp16` | 2 | 200 | 29.3899 | 0.097530 | 0.5210 | 4247 | `gsm8k,mmlu` |
| `gptqmodel` | 2 | 200 | 10.2208 | 0.301244 | 0.4514 | 3679 | `gsm8k,mmlu` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 0.1708 | 3.6509 | 0.8693 |
| `gptqmodel` | 0.3478 | 3.0887 | 0.8663 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ 100-row matched public MMLU/GSM8K subsets, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
