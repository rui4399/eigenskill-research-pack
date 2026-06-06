# Chat Task Benchmark

Model: `Qwen/Qwen3-0.6B`
Tasks: `8`
Task format: `ifeval`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 2 / 8 | 0.2500 | 25.9604 | 0.193870 |
| fused | 1 / 8 | 0.1250 | 22.1076 | 0.340813 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `ifeval_v2_json_only` | `all_of` | false | `[{'type': 'json_valid', 'answer': True}, {'type': 'contains_all', 'answer': ['risk', 'next_step']}]` | `<think>  </think>  ```json {   "risk": "The quantization rowguard introduces a mechanism to prevent overfitting by limit` |
| baseline | `ifeval_v2_forbidden_speed_claim` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['compression', 'latency']}, {'type': 'contains_none', 'answer': ['faster']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `<think>  </think>  Packed weight compression is a method used to reduce the weight of objects by compressing them into a` |
| baseline | `ifeval_v2_exact_sentence_count` | `all_of` | true | `[{'type': 'contains_all', 'answer': ['held-out', 'rowguard']}, {'type': 'sentence_count', 'answer': {'count': 2}}]` | `<think>  </think>  held-out prompts matter for rowguard claims because they provide context and background information t` |
| baseline | `ifeval_v2_word_count` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['TTFT', 'throughput', 'memory']}, {'type': 'word_count', 'answer': {'count': 4}}]` | `<think>  </think>  edge deployment metrics` |
| baseline | `ifeval_v2_forbidden_sota` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['runtime', 'speedup']}, {'type': 'contains_none', 'answer': ['SOTA']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `<think>  </think>  The current ESMP fused runtime is a cautious and optimized approach to managing execution, balancing ` |
| baseline | `ifeval_v2_json_metric_value` | `all_of` | false | `[{'type': 'json_valid', 'answer': True}, {'type': 'contains_all', 'answer': ['metric', 'value', 'TTFT']}]` | `<think>  </think>  ```json {   "metric": "TTFT",   "value": "placeholder string" } ```` |
| baseline | `ifeval_v2_single_sentence_caveat` | `all_of` | true | `[{'type': 'contains_all', 'answer': ['perplexity', 'task accuracy']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `<think>  </think>  Perplexity alone is insufficient without task accuracy.` |
| baseline | `ifeval_v2_forbid_generalizes` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['evidence', 'prompt']}, {'type': 'contains_none', 'answer': ['generalizes']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `<think>  </think>  The rowguard evidence provides critical insights into the incident's progression and potential outcom` |
| fused | `ifeval_v2_json_only` | `all_of` | false | `[{'type': 'json_valid', 'answer': True}, {'type': 'contains_all', 'answer': ['risk', 'next_step']}]` | `<think>  </think>  ```json {   "risk": "The quantization rowguard introduces a mechanism to prevent overfitting by limit` |
| fused | `ifeval_v2_forbidden_speed_claim` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['compression', 'latency']}, {'type': 'contains_none', 'answer': ['faster']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `<think>  </think>  Packed weight compression is a method used to reduce the weight of objects by compressing them into a` |
| fused | `ifeval_v2_exact_sentence_count` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['held-out', 'rowguard']}, {'type': 'sentence_count', 'answer': {'count': 2}}]` | `<think>  </think>  held-out prompts matter for rowguard claims because they provide critical context and background info` |
| fused | `ifeval_v2_word_count` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['TTFT', 'throughput', 'memory']}, {'type': 'word_count', 'answer': {'count': 4}}]` | `<think>  </think>  edge deployment metrics` |
| fused | `ifeval_v2_forbidden_sota` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['runtime', 'speedup']}, {'type': 'contains_none', 'answer': ['SOTA']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `<think>  </think>  The current ESMP fused runtime is a cautious and optimized approach to enhancing performance in embed` |
| fused | `ifeval_v2_json_metric_value` | `all_of` | false | `[{'type': 'json_valid', 'answer': True}, {'type': 'contains_all', 'answer': ['metric', 'value', 'TTFT']}]` | `<think>  </think>  ```json {   "metric": "TTFT",   "value": "placeholder" } ```` |
| fused | `ifeval_v2_single_sentence_caveat` | `all_of` | true | `[{'type': 'contains_all', 'answer': ['perplexity', 'task accuracy']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `<think>  </think>  Perplexity alone is insufficient without task accuracy.` |
| fused | `ifeval_v2_forbid_generalizes` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['evidence', 'prompt']}, {'type': 'contains_none', 'answer': ['generalizes']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `<think>  </think>  Rowguard evidence is used to determine the accuracy of a claim by analyzing the physical and structur` |
