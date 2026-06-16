# Chat Task Benchmark

Model: `/home/rui/models/Qwen2.5-1.5B-Instruct`
Tasks: `8`
Task format: `ifeval`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 0 / 8 | 0.0000 | 24.1735 | 0.261944 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `ifeval_v2_json_only` | `all_of` | false | `[{'type': 'json_valid', 'answer': True}, {'type': 'contains_all', 'answer': ['risk', 'next_step']}]` | ````json {   "risk": "Overfitting",   "next_step": "Implement regularization techniques to prevent the model from memoriz` |
| baseline | `ifeval_v2_forbidden_speed_claim` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['compression', 'latency']}, {'type': 'contains_none', 'answer': ['faster']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `Packed weight compression involves reducing the volume of materials to save space and increase efficiency in storage or ` |
| baseline | `ifeval_v2_exact_sentence_count` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['held-out', 'rowguard']}, {'type': 'sentence_count', 'answer': {'count': 2}}]` | `Held-out prompts matter because they provide an unbiased test of the model's ability to generalize and make accurate pre` |
| baseline | `ifeval_v2_word_count` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['TTFT', 'throughput', 'memory']}, {'type': 'word_count', 'answer': {'count': 4}}]` | `Latency, throughput, accuracy, reliability.` |
| baseline | `ifeval_v2_forbidden_sota` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['runtime', 'speedup']}, {'type': 'contains_none', 'answer': ['SOTA']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `The current ESMP fused runtime demonstrates significant performance improvements but also introduces complexities that r` |
| baseline | `ifeval_v2_json_metric_value` | `all_of` | false | `[{'type': 'json_valid', 'answer': True}, {'type': 'contains_all', 'answer': ['metric', 'value', 'TTFT']}]` | ````json {   "TTFT": "placeholder_string" } ```` |
| baseline | `ifeval_v2_single_sentence_caveat` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['perplexity', 'task accuracy']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `Perplexity alone is insufficient because it does not account for the task's accuracy; while high perplexity indicates ra` |
| baseline | `ifeval_v2_forbid_generalizes` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['evidence', 'prompt']}, {'type': 'contains_none', 'answer': ['generalizes']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `RowGuard Evidence is a tool designed to help forensic investigators maintain the integrity of digital evidence by provid` |
