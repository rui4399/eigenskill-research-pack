# Chat Task Benchmark

Model: `outputs/official_gptqmodel_smoke_2026_06_07/qwen25_0p5b_public_calib_gptq_model`
Tasks: `8`
Task format: `ifeval`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 1 / 8 | 0.1250 | 12.3554 | 0.425140 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `ifeval_v2_json_only` | `all_of` | true | `[{'type': 'json_valid', 'answer': True}, {'type': 'contains_all', 'answer': ['risk', 'next_step']}]` | `{   "risk": "overfitting",   "next_step": "improve the quality of the prompt to prevent overfitting" }` |
| baseline | `ifeval_v2_forbidden_speed_claim` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['compression', 'latency']}, {'type': 'contains_none', 'answer': ['faster']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `A person with a heavy backpack is unable to carry their full weight.` |
| baseline | `ifeval_v2_exact_sentence_count` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['held-out', 'rowguard']}, {'type': 'sentence_count', 'answer': {'count': 2}}]` | `RowGuard claims rely on the assumption that the row guard is holding out to the enemy, which means they are not actually` |
| baseline | `ifeval_v2_word_count` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['TTFT', 'throughput', 'memory']}, {'type': 'word_count', 'answer': {'count': 4}}]` | `performance, throughput, latency, efficiency` |
| baseline | `ifeval_v2_forbidden_sota` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['runtime', 'speedup']}, {'type': 'contains_none', 'answer': ['SOTA']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `The current ESPMFusion Runtime is likely to be more complex and resource-intensive than its predecessor, as it incorpora` |
| baseline | `ifeval_v2_json_metric_value` | `all_of` | false | `[{'type': 'json_valid', 'answer': True}, {'type': 'contains_all', 'answer': ['metric', 'value', 'TTFT']}]` | `{"metric":"no_think","value":"no_think"}` |
| baseline | `ifeval_v2_single_sentence_caveat` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['perplexity', 'task accuracy']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `Perplexity alone may not be sufficient to achieve accurate results in certain tasks.` |
| baseline | `ifeval_v2_forbid_generalizes` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['evidence', 'prompt']}, {'type': 'contains_none', 'answer': ['generalizes']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `A rowguard is an evidence of a breach in the security measures of a building or structure.` |
