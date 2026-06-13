# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `8`
Task format: `ifeval`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 1 / 8 | 0.1250 | 18.2283 | 0.548219 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `ifeval_v2_json_only` | `all_of` | false | `[{'type': 'json_valid', 'answer': True}, {'type': 'contains_all', 'answer': ['risk', 'next_step']}]` | ````json {   "risk": "High",   "next_step": "Implement regularization techniques to prevent overfitting." } ```` |
| baseline | `ifeval_v2_forbidden_speed_claim` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['compression', 'latency']}, {'type': 'contains_none', 'answer': ['faster']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `Packed weight compression involves carefully arranging and compressing goods to maximize space and weight efficiency in ` |
| baseline | `ifeval_v2_exact_sentence_count` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['held-out', 'rowguard']}, {'type': 'sentence_count', 'answer': {'count': 2}}]` | `Held-out prompts matter for rowguard claims because they provide a way to evaluate the accuracy and reliability of the c` |
| baseline | `ifeval_v2_word_count` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['TTFT', 'throughput', 'memory']}, {'type': 'word_count', 'answer': {'count': 4}}]` | `Latency, throughput, accuracy, reliability` |
| baseline | `ifeval_v2_forbidden_sota` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['runtime', 'speedup']}, {'type': 'contains_none', 'answer': ['SOTA']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `The current ESMP fused runtime demonstrates significant improvements in performance but also introduces new challenges i` |
| baseline | `ifeval_v2_json_metric_value` | `all_of` | false | `[{'type': 'json_valid', 'answer': True}, {'type': 'contains_all', 'answer': ['metric', 'value', 'TTFT']}]` | ````json {   "TTFT": "Placeholder string" } ```` |
| baseline | `ifeval_v2_single_sentence_caveat` | `all_of` | true | `[{'type': 'contains_all', 'answer': ['perplexity', 'task accuracy']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `Perplexity alone is insufficient because it does not guarantee task accuracy, which is crucial for the effectiveness of ` |
| baseline | `ifeval_v2_forbid_generalizes` | `all_of` | false | `[{'type': 'contains_all', 'answer': ['evidence', 'prompt']}, {'type': 'contains_none', 'answer': ['generalizes']}, {'type': 'sentence_count', 'answer': {'count': 1}}]` | `Rowguard evidence is a type of evidence that is used in legal proceedings to prove the existence of a row or dispute bet` |
