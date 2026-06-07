# Official PTQ Matched Baseline Pack Gate

Date: `2026-06-07T05:16:49+00:00`
Status: **PASS**

## Summary

- variants: `autoawq, gptqmodel`
- PPL slices: `4`
- total PPL tokens: `5714`
- task executions: `300`
- runtime executions: `300`
- max PPL ratio vs FP16: `1.2570`
- max task accuracy drop vs FP16: `0.0400`
- max VRAM ratio vs FP16: `0.9010`
- max tokens/s ratio vs FP16: `0.3315`

## Variant Evidence

| variant | PPL labels | max PPL ratio | task rows | max task drop | tok/s ratio | VRAM ratio |
|---|---|---:|---:|---:|---:|---:|
| `autoawq` | `c4,wikitext2` | 1.2114 | 100 | 0.0400 | 0.1629 | 0.9010 |
| `gptqmodel` | `c4,wikitext2` | 1.2570 | 100 | 0.0000 | 0.3315 | 0.8930 |

## PPL Slices

| variant | label | tokens | FP16 PPL | quant PPL | ratio |
|---|---|---:|---:|---:|---:|
| `autoawq` | `wikitext2` | 1413 | 24.590745 | 29.788817 | 1.211383 |
| `autoawq` | `c4` | 1444 | 29.917597 | 35.374649 | 1.182403 |
| `gptqmodel` | `wikitext2` | 1413 | 24.590745 | 30.909568 | 1.256959 |
| `gptqmodel` | `c4` | 1444 | 29.917597 | 36.362052 | 1.215407 |

## Failures

- none

## Claim Boundary

Valid claim: the local official AutoAWQ and GPTQModel Qwen2.5-0.5B W4/G128 artifacts have matched public-calibration PPL slices, matched 50-row public MMLU/GSM8K task execution, and PC-side runtime/VRAM profiles. Invalid claim: this is a leaderboard-scale or large-model competitive AWQ/GPTQ baseline, a production runtime, mobile deployment, energy result, or SOTA PTQ evidence.
