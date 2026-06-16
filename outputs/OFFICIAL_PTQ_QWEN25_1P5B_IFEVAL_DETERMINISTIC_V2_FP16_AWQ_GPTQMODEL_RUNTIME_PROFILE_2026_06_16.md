# Official PTQ Runtime Profile Gate

Date: `2026-06-16T05:40:58+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- total cases: `3`
- total tasks: `24`
- mean tokens/s across variants: `19.2650`
- mean TTFT across variants: `0.446351` s
- peak guard VRAM ratio: `0.8762`
- peak guard VRAM MiB: `7142`

## Variant Profiles

| variant | cases | tasks | mean tok/s | mean TTFT s | peak VRAM ratio | peak VRAM MiB | formats |
|---|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 1 | 8 | 18.2283 | 0.548219 | 0.4977 | 4057 | `ifeval` |
| `fp16` | 1 | 8 | 24.1735 | 0.261944 | 0.8762 | 7142 | `ifeval` |
| `gptqmodel` | 1 | 8 | 15.3932 | 0.528889 | 0.4542 | 3702 | `ifeval` |

## Comparisons Against Baseline

| variant | tok/s ratio | TTFT ratio | VRAM ratio |
|---|---:|---:|---:|
| `autoawq` | 0.7541 | 2.0929 | 0.5680 |
| `gptqmodel` | 0.6368 | 2.0191 | 0.5183 |

## Failures

- none

## Claim Boundary

- Valid claim: this is a PC-side runtime profile over already-guarded official PTQ 8-row deterministic IFEval-style fixture, reporting TTFT, tokens/s, and peak VRAM for FP16 and official-package quantized artifacts. Invalid claim: this does not prove mobile deployment, production runtime speedup, energy improvement, or official AWQ/GPTQ competitiveness.
