# Chat Task Benchmark

Model: `Qwen/Qwen3-0.6B`
Tasks: `12`
Task format: `native`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 7 / 12 | 0.5833 | 24.4976 | 0.159114 |
| fused | 7 / 12 | 0.5833 | 23.7956 | 0.124476 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_style_memory_metric` | `mcq` | true | `B` | `<think>  </think>  B. peak GPU memory` |
| baseline | `mmlu_style_math_benchmark` | `mcq` | false | `A` | `<think>  </think>  B. HumanEval` |
| baseline | `mmlu_style_calibration_instability` | `mcq` | true | `B` | `<think>  </think>  B. calibration split instability` |
| baseline | `gsm8k_style_int4_bytes` | `number` | true | `4096` | `<think>  </think>  Two weights fit in one byte. A row stores 8192 signed 4-bit weights.   So, the number of packed bytes` |
| baseline | `gsm8k_style_average_bits` | `number` | true | `5` | `<think>  </think>  The average bit width is calculated by taking the weighted average of the bit widths of the rows:  $$` |
| baseline | `gsm8k_style_selected_rows_bytes` | `number` | false | `131072` | `<think>  </think>  Each row has 4096 signed 4-bit weights, and two weights fit in one byte.   So, the number of packed b` |
| baseline | `ifeval_style_risk_json` | `json_keys` | true | `['risk', 'next_step']` | `<think>  </think>  ```json {   "risk": "rowguard",   "next_step": "high hidden-state drift" } ```` |
| baseline | `ifeval_style_metric_json` | `json_keys` | true | `['metric', 'value']` | `<think>  </think>  ```json {"metric": "TTFT", "value": "placeholder"} ```` |
| baseline | `ifeval_style_ppl_caveat` | `contains_all` | false | `['perplexity', 'task', 'accuracy']` | `<think>  </think>  Perplexity alone is not sufficient evidence for a quantized instruction model because it measures the` |
| baseline | `ifeval_style_compression_caveat` | `contains_all` | true | `['compression', 'latency', 'speedup']` | `<think>  </think>  **Caveat:** Packed weight compression is not the same as latency speedup.` |
| baseline | `ifeval_style_rowguard_generalization` | `contains_all` | false | `['held', 'out', 'prompt']` | `<think>  </think>  One requirement before claiming a rowguard generalizes across prompts is that the rowguard must be **` |
| baseline | `ifeval_style_deployment_metrics` | `contains_all` | false | `['ttft', 'throughput', 'memory']` | `<think>  </think>  Three physical deployment metrics for an edge LLM are:  1. **TTFT (Total Time to First Token)** – Mea` |
| fused | `mmlu_style_memory_metric` | `mcq` | true | `B` | `<think>  </think>  B. peak GPU memory` |
| fused | `mmlu_style_math_benchmark` | `mcq` | false | `A` | `<think>  </think>  B. HumanEval` |
| fused | `mmlu_style_calibration_instability` | `mcq` | true | `B` | `<think>  </think>  B. calibration split instability` |
| fused | `gsm8k_style_int4_bytes` | `number` | true | `4096` | `<think>  </think>  Two weights fit in one byte. A row stores 8192 signed 4-bit weights.   So, the number of packed bytes` |
| fused | `gsm8k_style_average_bits` | `number` | true | `5` | `<think>  </think>  The average bit width is calculated by taking the weighted average of the bit widths of the rows:  $$` |
| fused | `gsm8k_style_selected_rows_bytes` | `number` | false | `131072` | `<think>  </think>  Each row has 4096 signed 4-bit weights, and two weights fit in one byte.   So, the number of packed b` |
| fused | `ifeval_style_risk_json` | `json_keys` | true | `['risk', 'next_step']` | `<think>  </think>  ```json {   "risk": "rowguard",   "next_step": "high hidden-state drift" } ```` |
| fused | `ifeval_style_metric_json` | `json_keys` | true | `['metric', 'value']` | `<think>  </think>  ```json {"metric": "TTFT", "value": "placeholder"} ```` |
| fused | `ifeval_style_ppl_caveat` | `contains_all` | false | `['perplexity', 'task', 'accuracy']` | `<think>  </think>  Perplexity alone is not sufficient evidence for a quantized instruction model because it measures the` |
| fused | `ifeval_style_compression_caveat` | `contains_all` | true | `['compression', 'latency', 'speedup']` | `<think>  </think>  **Caveat:** Packed weight compression is not the same as latency speedup.` |
| fused | `ifeval_style_rowguard_generalization` | `contains_all` | false | `['held', 'out', 'prompt']` | `<think>  </think>  One requirement before claiming a rowguard generalizes across prompts is that the rowguard must be **` |
| fused | `ifeval_style_deployment_metrics` | `contains_all` | false | `['ttft', 'throughput', 'memory']` | `<think>  </think>  Three physical deployment metrics for an edge LLM are:  1. **TTFT (Total Time to First Token)** – Mea` |
