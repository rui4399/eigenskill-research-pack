# Chat Task Benchmark

Model: `Qwen/Qwen3-0.6B`
Tasks: `12`
Chat template: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 2 / 12 | 0.1667 | 22.7031 | 0.171191 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_style_memory_metric` | `mcq` | false | `B` | `<think> Okay, so I need to figure out which metric directly reports peak device memory in an edge-LLM deployment paper. ` |
| baseline | `mmlu_style_math_benchmark` | `mcq` | false | `A` | `<think> Okay, let's see. The question is asking which common benchmark is primarily a grade-school math word-problem ben` |
| baseline | `mmlu_style_calibration_instability` | `mcq` | false | `B` | `<think> Okay, let's try to figure out this question. The question is about a mixed-precision policy that ranks important` |
| baseline | `gsm8k_style_int4_bytes` | `number` | false | `4096` | `<think> Okay, let's see. The question is about how many packed bytes are needed for a row that stores 8192 signed 4-bit` |
| baseline | `gsm8k_style_average_bits` | `number` | false | `5` | `<think> Okay, so I need to figure out the average bit width for this matrix. Let me start by understanding the problem. ` |
| baseline | `gsm8k_style_selected_rows_bytes` | `number` | false | `131072` | `<think> Okay, let's see. The problem says that a selected-row kernel reads 64 rows, each with 4096 signed 4` |
| baseline | `ifeval_style_risk_json` | `json_keys` | false | `['risk', 'next_step']` | `<think> Okay, let's tackle this query. The user wants a minified JSON with only the keys 'risk' and 'next_step', describ` |
| baseline | `ifeval_style_metric_json` | `json_keys` | false | `['metric', 'value']` | `<think> Okay, let's see. The user wants me to return minified JSON with only the keys 'metric' and 'value'. The 'metric'` |
| baseline | `ifeval_style_ppl_caveat` | `contains_all` | false | `['perplexity', 'task', 'accuracy']` | `<think> Okay, so the user is asking why perplexity alone isn't enough evidence for a quantized instruction model. Let me` |
| baseline | `ifeval_style_compression_caveat` | `contains_all` | true | `['compression', 'latency', 'speedup']` | `<think> Okay, the user wants a concise caveat that explains the difference between packed weight compression and latency` |
| baseline | `ifeval_style_rowguard_generalization` | `contains_all` | false | `['held', 'out', 'prompt']` | `<think> Okay, the user is asking for one requirement before claiming a rowguard generalizes across prompts. Let me start` |
| baseline | `ifeval_style_deployment_metrics` | `contains_all` | true | `['ttft', 'throughput', 'memory']` | `<think> Okay, the user is asking for three physical deployment metrics for an edge LLM, including TTFT, throughput, and ` |
