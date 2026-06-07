# Chat Task Benchmark

Model: `Qwen/Qwen2.5-0.5B-Instruct`
Tasks: `8`
Task format: `ifeval`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 0 / 8 | 0.0000 | 30.6348 | 0.264942 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `ifeval_v2_json_only` | `all_of` | false | `[{'type': 'json_valid', 'answer': True}, {'type': 'contains_all', 'answer': ['risk', 'next_step']}]` | ````json {   "risk": "Overfitting",   "next_step": "Increase the complexity of the model or use more data" } ```` |
| baseline | `ifeval_v2_forbidden_speed_claim` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['compression', 'latency']}, {'type': 'contains_none', 'answer': ['faster']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `Packed weight compression can significantly reduce the load on your body during exercise or physical activity.` |
| baseline | `ifeval_v2_exact_sentence_count` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['held-out', 'rowguard']}, {'type': 'sentence_count', 'answer': {'count': 2}}]` | `Held-out prompts are crucial for rowguard claims because they provide an additional layer of evidence that can strengthe` |
| baseline | `ifeval_v2_word_count` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['TTFT', 'throughput', 'memory']}, {'type': 'word_count', 'answer': {'count': 4}}]` | `Model throughput, latency, inference speed, accuracy` |
| baseline | `ifeval_v2_forbidden_sota` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['runtime', 'speedup']}, {'type': 'contains_none', 'answer': ['SOTA']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `ESMP fused runtime is likely to introduce significant challenges and risks, particularly in terms of security and compli` |
| baseline | `ifeval_v2_json_metric_value` | `all_of` | false | `[{'type': 'json_valid', 'answer': True}, {'type': 'contains_all', 'answer': ['metric', 'value', 'TTFT']}]` | ````json {   "metric": "TTFT",   "value": "a placeholder string" } ```` |
| baseline | `ifeval_v2_single_sentence_caveat` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['perplexity', 'task accuracy']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `Perplexity alone may not be sufficient to fully understand or predict the behavior of complex systems, especially those ` |
| baseline | `ifeval_v2_forbid_generalizes` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['evidence', 'prompt']}, {'type': 'contains_none', 'answer': ['generalizes']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `Rowguard evidence refers to specialized techniques and methodologies used in cybersecurity investigations to gather and ` |
