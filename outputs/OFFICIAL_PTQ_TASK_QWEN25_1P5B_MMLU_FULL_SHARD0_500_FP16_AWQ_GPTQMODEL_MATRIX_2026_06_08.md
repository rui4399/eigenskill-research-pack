# Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel full-MMLU first-shard task matrix

Date: `2026-06-08T00:05:01+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['mmlu']`
- total tasks across cases: `1500`
- total passes across cases: `815`
- max accuracy drop vs `fp16`: `0.0480`
- zero-accuracy baseline formats: `[]`
- peak guard VRAM ratio: `0.8730`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `mmlu` | 500 | 284 | 0.5680 | 4.8933 | 0.399046 | 0.8730 | `outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_mmlu_full_0_500_2026_06_08.json` |
| `autoawq` | `mmlu` | 500 | 271 | 0.5420 | 10.5848 | 0.144740 | 0.7694 | `outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_mmlu_full_0_500_2026_06_08.json` |
| `gptqmodel` | `mmlu` | 500 | 260 | 0.5200 | 8.4550 | 0.186795 | 0.7149 | `outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_mmlu_full_0_500_2026_06_08.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `mmlu` | 0.5680 | 0.5420 | 0.0260 |
| `gptqmodel` | `mmlu` | 0.5680 | 0.5200 | 0.0480 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same matched Qwen2.5-1.5B local full-MMLU first 500-row task evidence for FP16, AutoAWQ, and GPTQModel under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
