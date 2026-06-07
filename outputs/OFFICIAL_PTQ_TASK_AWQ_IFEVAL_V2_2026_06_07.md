# Chat Task Benchmark

Model: `outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_public_calib_awq_model`
Tasks: `8`
Task format: `ifeval`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 1 / 8 | 0.1250 | 6.7130 | 0.586322 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `ifeval_v2_json_only` | `all_of` | false | `[{'type': 'json_valid', 'answer': True}, {'type': 'contains_all', 'answer': ['risk', 'next_step']}]` | ````json {   "risk": "overfitting",   "next_step": "quantize" } ```` |
| baseline | `ifeval_v2_forbidden_speed_claim` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['compression', 'latency']}, {'type': 'contains_none', 'answer': ['faster']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `Packed weight can be effectively compressed using various techniques such as compression straps or wraps to reduce the r` |
| baseline | `ifeval_v2_exact_sentence_count` | `all_of` | true | `[{'type': 'contains_all', 'answer': ['held-out', 'rowguard']}, {'type': 'sentence_count', 'answer': {'count': 2}}]` | `Held-out prompts are crucial for rowguard claims because they provide a clear and concise way to express the exact wordi` |
| baseline | `ifeval_v2_word_count` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['TTFT', 'throughput', 'memory']}, {'type': 'word_count', 'answer': {'count': 4}}]` | `temperature, latency, accuracy, performance` |
| baseline | `ifeval_v2_forbidden_sota` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['runtime', 'speedup']}, {'type': 'contains_none', 'answer': ['SOTA']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `ESMO's merged runtime is currently facing challenges due to regulatory updates and evolving industry practices, leading ` |
| baseline | `ifeval_v2_json_metric_value` | `all_of` | false | `[{'type': 'json_valid', 'answer': True}, {'type': 'contains_all', 'answer': ['metric', 'value', 'TTFT']}]` | ````json {   "metric": "TTFT",   "value": "placeholder_value" } ```` |
| baseline | `ifeval_v2_single_sentence_caveat` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['perplexity', 'task accuracy']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `The model's ability to generate text accurately and effectively depends on its understanding of the task at hand, not so` |
| baseline | `ifeval_v2_forbid_generalizes` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['evidence', 'prompt']}, {'type': 'contains_none', 'answer': ['generalizes']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `Rowguard evidence is physical evidence collected from the scene of an incident or crime.` |
