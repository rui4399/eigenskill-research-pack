# Official PTQ Matched Baseline Pack Gate

Date: `2026-06-07T03:38:48+00:00`
Status: **PASS**

## Summary

- variants: `autoawq, gptqmodel`
- PPL slices: `4`
- total PPL tokens: `2974`
- task executions: `300`
- runtime executions: `300`
- max PPL ratio vs FP16: `1.2949`
- max task accuracy drop vs FP16: `0.0400`
- max VRAM ratio vs FP16: `0.9010`
- max tokens/s ratio vs FP16: `0.3315`

## Variant Evidence

| variant | PPL labels | max PPL ratio | task rows | max task drop | tok/s ratio | VRAM ratio |
|---|---|---:|---:|---:|---:|---:|
| `autoawq` | `c4,wikitext2` | 1.1785 | 100 | 0.0400 | 0.1629 | 0.9010 |
| `gptqmodel` | `c4,wikitext2` | 1.2949 | 100 | 0.0000 | 0.3315 | 0.8930 |

## PPL Slices

| variant | label | tokens | FP16 PPL | quant PPL | ratio |
|---|---|---:|---:|---:|---:|
| `autoawq` | `wikitext2` | 760 | 24.675866 | 29.080631 | 1.178505 |
| `autoawq` | `c4` | 727 | 32.951664 | 38.172702 | 1.158445 |
| `gptqmodel` | `wikitext2` | 760 | 24.675866 | 31.952564 | 1.294891 |
| `gptqmodel` | `c4` | 727 | 32.951664 | 39.809985 | 1.208133 |

## Failures

- none

## Claim Boundary

Valid claim: the local official AutoAWQ and GPTQModel Qwen2.5-0.5B W4/G128 artifacts have matched public-calibration PPL slices, matched 50-row public MMLU/GSM8K task execution, and PC-side runtime/VRAM profiles. Invalid claim: this is a leaderboard-scale or large-model competitive AWQ/GPTQ baseline, a production runtime, mobile deployment, energy result, or SOTA PTQ evidence.
