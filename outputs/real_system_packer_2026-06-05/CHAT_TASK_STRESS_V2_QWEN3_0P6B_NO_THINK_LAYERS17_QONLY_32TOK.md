# Chat Task Benchmark

Model: `Qwen/Qwen3-0.6B`
Tasks: `42`
Task format: `native`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 22 / 42 | 0.5238 | 23.4680 | 0.104977 |
| fused | 22 / 42 | 0.5238 | 23.6546 | 0.102466 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `stress_mcq_000` | `mcq` | true | `A` | `<think>  </think>  A. TTFT` |
| baseline | `stress_mcq_001` | `mcq` | true | `A` | `<think>  </think>  A. Packed INT4 weights` |
| baseline | `stress_mcq_002` | `mcq` | true | `A` | `<think>  </think>  A. C4` |
| baseline | `stress_mcq_003` | `mcq` | true | `A` | `<think>  </think>  A. Pass-count regression` |
| baseline | `stress_mcq_004` | `mcq` | false | `A` | `<think>  </think>  D. Full QKV` |
| baseline | `stress_mcq_005` | `mcq` | true | `A` | `<think>  </think>  A. IFEval` |
| baseline | `stress_number_000` | `number` | false | `4096` | `<think>  </think>  We are given that there are 8192 signed 4-bit weights, and each byte can hold two such weights.  - ` |
| baseline | `stress_number_001` | `number` | false | `65536` | `<think>  </think>  Each row has 4096 signed 4-bit weights, so each row is 4096 bytes. Since the kernel` |
| baseline | `stress_number_002` | `number` | false | `4.8` | `<think>  </think>  The average bit width is calculated by multiplying the percentage of 4-bit rows by 4 and the percenta` |
| baseline | `stress_number_003` | `number` | false | `21` | `<think>  </think>  The number of layers packed is $ 3 \times 24 = \boxed{72} $.` |
| baseline | `stress_number_004` | `number` | false | `96` | `<think>  </think>  48` |
| baseline | `stress_number_005` | `number` | false | `7335` | `<think>  </think>  The total memory is 8151 MiB. A 90% guard allows at most:  $$ 0.9 \` |
| baseline | `stress_json_keys_000` | `json_keys` | false | `['metric', 'value']` | `<think>  </think>  ```json {"metric": "TTFT"} ```` |
| baseline | `stress_json_keys_001` | `json_keys` | true | `['risk', 'evidence']` | `<think>  </think>  ```json {   "risk": "calibration_split_instability",   "evidence": "calibration_split_instability" } ` |
| baseline | `stress_json_keys_002` | `json_keys` | true | `['policy', 'decision']` | `<think>  </think>  ```json {"policy": "V-only", "decision": "V-only"} ```` |
| baseline | `stress_json_keys_003` | `json_keys` | true | `['memory_mb', 'tokens_per_second']` | `<think>  </think>  ```json {"memory_mb": "0", "tokens_per_second": "0"} ```` |
| baseline | `stress_json_keys_004` | `json_keys` | true | `['layer', 'role']` | `<think>  </think>  ```json {"layer": "minified", "role": "only"} ```` |
| baseline | `stress_json_keys_005` | `json_keys` | false | `['dataset', 'pass_count']` | `<think>  </think>  ```json {"dataset": "pass_count"} ```` |
| baseline | `stress_contains_all_000` | `contains_all` | false | `['perplexity', 'task', 'accuracy']` | `<think>  </think>  PPL alone is incomplete for instruction models because it lacks the ability to understand and generat` |
| baseline | `stress_contains_all_001` | `contains_all` | false | `['ttft', 'throughput', 'memory']` | `<think>  </think>  Three physical deployment metrics for edge LLM inference are:  1. **Latency**: The time it takes for ` |
| baseline | `stress_contains_all_002` | `contains_all` | false | `['calibration', 'split', 'instability']` | `<think>  </think>  Calibration robustness is crucial because it ensures that the system's performance remains stable and` |
| baseline | `stress_contains_all_003` | `contains_all` | false | `['compression', 'latency', 'speedup']` | `<think>  </think>  **Caveat: Packed Compression and Real Runtime**  It is important to note that **packed compression** ` |
| baseline | `stress_contains_all_004` | `contains_all` | false | `['download', 'leakage', 'random']` | `<think>  </think>  A deterministic stress slice should avoid **inconsistencies, ambiguities, and non-physical assumption` |
| baseline | `stress_contains_all_005` | `contains_all` | false | `['device', 'ttft', 'tokens']` | `<think>  </think>  Before claiming phone deployment, the following must be measured:  1. **Phone Model and Specification` |
| baseline | `stress_contains_none_000` | `contains_none` | true | `['sota']` | `<think>  </think>  A conservative result is one that prioritizes stability, fairness, and long-term sustainability over ` |
| baseline | `stress_contains_none_001` | `contains_none` | true | `['official']` | `<think>  </think>  A local diagnostic is a person who checks and evaluates a person's health, often based on their sympt` |
| baseline | `stress_contains_none_002` | `contains_none` | true | `['proven']` | `<think>  </think>  A packed kernel experiment is a type of computational experiment where a large number of cores (or pr` |
| baseline | `stress_contains_none_003` | `contains_none` | true | `['failure']` | `<think>  </think>  A negative result could be something that doesn't meet expectations, such as a low score, a negative ` |
| baseline | `stress_contains_none_004` | `contains_none` | true | `['delete']` | `<think>  </think>  A C-drive cleanup involves removing or clearing out unnecessary files, data, or programs that are no ` |
| baseline | `stress_contains_none_005` | `contains_none` | true | `['universal']` | `<think>  </think>  A benchmark slice is a specific, standardized piece of data or information used to evaluate or compar` |
| baseline | `stress_sentence_count_000` | `sentence_count` | true | `{'count': 1}` | `<think>  </think>  The role-policy selector is a mechanism that selects the most appropriate role and policy pair based ` |
| baseline | `stress_sentence_count_001` | `sentence_count` | false | `{'count': 2}` | `<think>  </think>  Layer 20 expansion can be risky due to its high demand and limited capacity, which may lead to overex` |
| baseline | `stress_sentence_count_002` | `sentence_count` | true | `{'count': 1}` | `<think>  </think>  A disk guard is useful in exactly one sentence.` |
| baseline | `stress_word_count_000` | `word_count` | false | `{'count': 3}` | `<think>  </think>  Speed, Memory, and Latency.` |
| baseline | `stress_word_count_001` | `word_count` | false | `{'count': 4}` | `<think>  </think>  Robust calibration evidence supports accurate model predictions.` |
| baseline | `stress_word_count_002` | `word_count` | false | `{'count': 5}` | `<think>  </think>  A conservative V-only policy.` |
| baseline | `stress_all_of_000` | `all_of` | true | `[{'type': 'json_keys', 'answer': ['risk', 'next_step']}, {'type': 'contains_none', 'answer': ['unsafe']}]` | `<think>  </think>  ```json {   "risk": "low",   "next_step": "review the data further" } ```` |
| baseline | `stress_all_of_001` | `all_of` | true | `[{'type': 'sentence_count', 'answer': {'count': 1}}, {'type': 'contains_all', 'answer': ['calibration', 'memory']}, {'type': 'contains_none', 'answer': ['universal']}]` | `<think>  </think>  Calibration ensures accurate memory, helping to maintain precise data storage and retrieval.` |
| baseline | `stress_all_of_002` | `all_of` | true | `[{'type': 'json_keys', 'answer': ['policy', 'speedup']}, {'type': 'contains_none', 'answer': ['sota']}]` | `<think>  </think>  ```json {   "policy": "speedup",   "speedup": "increase" } ```` |
| baseline | `stress_all_of_003` | `all_of` | false | `[{'type': 'word_count', 'answer': {'count': 4}}, {'type': 'contains_all', 'answer': ['ttft', 'memory']}]` | `<think>  </think>  1. **Ttft Memory**   2. **Ttft Memory**   3. **Ttft Memory**   4` |
| baseline | `stress_all_of_004` | `all_of` | true | `[{'type': 'json_keys', 'answer': ['layer', 'verdict']}, {'type': 'contains_none', 'answer': ['proven']}]` | `<think>  </think>  ```json {   "layer": "layer",   "verdict": "verdict" } ```` |
| baseline | `stress_all_of_005` | `all_of` | true | `[{'type': 'sentence_count', 'answer': {'count': 1}}, {'type': 'contains_all', 'answer': ['held', 'out', 'prompt']}, {'type': 'contains_none', 'answer': ['official']}]` | `<think>  </think>  The prompt was held out for the user to review.` |
| fused | `stress_mcq_000` | `mcq` | true | `A` | `<think>  </think>  A. TTFT` |
| fused | `stress_mcq_001` | `mcq` | true | `A` | `<think>  </think>  A. Packed INT4 weights` |
| fused | `stress_mcq_002` | `mcq` | true | `A` | `<think>  </think>  A. C4` |
| fused | `stress_mcq_003` | `mcq` | true | `A` | `<think>  </think>  A. Pass-count regression` |
| fused | `stress_mcq_004` | `mcq` | false | `A` | `<think>  </think>  D. Full QKV` |
| fused | `stress_mcq_005` | `mcq` | true | `A` | `<think>  </think>  A. IFEval` |
| fused | `stress_number_000` | `number` | false | `4096` | `<think>  </think>  We are given that there are 8192 signed 4-bit weights, and each byte can hold two such weights.  - ` |
| fused | `stress_number_001` | `number` | false | `65536` | `<think>  </think>  0` |
| fused | `stress_number_002` | `number` | false | `4.8` | `<think>  </think>  The average bit width is calculated by multiplying the percentage of 4-bit rows by 4 and the percenta` |
| fused | `stress_number_003` | `number` | false | `21` | `<think>  </think>  The number of layers packed is $ 3 \times 24 = \boxed{72} $.` |
| fused | `stress_number_004` | `number` | false | `96` | `<think>  </think>  48` |
| fused | `stress_number_005` | `number` | false | `7335` | `<think>  </think>  The total memory is 8151 MiB. A 90% guard allows at most:  $$ 0.9 \` |
| fused | `stress_json_keys_000` | `json_keys` | false | `['metric', 'value']` | `<think>  </think>  ```json {"metric": "TTFT"} ```` |
| fused | `stress_json_keys_001` | `json_keys` | true | `['risk', 'evidence']` | `<think>  </think>  ```json {   "risk": "calibration_split_instability",   "evidence": "calibration_split_instability" } ` |
| fused | `stress_json_keys_002` | `json_keys` | true | `['policy', 'decision']` | `<think>  </think>  ```json {"policy": "V-only", "decision": "V-only"} ```` |
| fused | `stress_json_keys_003` | `json_keys` | true | `['memory_mb', 'tokens_per_second']` | `<think>  </think>  ```json {"memory_mb": "0", "tokens_per_second": "0"} ```` |
| fused | `stress_json_keys_004` | `json_keys` | true | `['layer', 'role']` | `<think>  </think>  ```json {"layer": "minified", "role": "only"} ```` |
| fused | `stress_json_keys_005` | `json_keys` | false | `['dataset', 'pass_count']` | `<think>  </think>  ```json {"dataset": "pass_count"} ```` |
| fused | `stress_contains_all_000` | `contains_all` | false | `['perplexity', 'task', 'accuracy']` | `<think>  </think>  PPL alone is incomplete for instruction models because it lacks the ability to understand and generat` |
| fused | `stress_contains_all_001` | `contains_all` | false | `['ttft', 'throughput', 'memory']` | `<think>  </think>  Three physical deployment metrics for edge LLM inference are:  1. **Latency**: The time it takes for ` |
| fused | `stress_contains_all_002` | `contains_all` | false | `['calibration', 'split', 'instability']` | `<think>  </think>  Calibration robustness is crucial because it ensures that the system's performance remains stable and` |
| fused | `stress_contains_all_003` | `contains_all` | false | `['compression', 'latency', 'speedup']` | `<think>  </think>  **Caveat: Packed Compression and Real Runtime**  It is important to note that **packed compression** ` |
| fused | `stress_contains_all_004` | `contains_all` | false | `['download', 'leakage', 'random']` | `<think>  </think>  A deterministic stress slice should avoid **inconsistencies, ambiguities, and non-physical assumption` |
| fused | `stress_contains_all_005` | `contains_all` | false | `['device', 'ttft', 'tokens']` | `<think>  </think>  Before claiming phone deployment, the following must be measured:  1. **Phone Model and Specification` |
| fused | `stress_contains_none_000` | `contains_none` | true | `['sota']` | `<think>  </think>  A conservative result is one that prioritizes stability, fairness, and long-term sustainability over ` |
| fused | `stress_contains_none_001` | `contains_none` | true | `['official']` | `<think>  </think>  A local diagnostic is a person who checks and evaluates a person's health, often based on their sympt` |
| fused | `stress_contains_none_002` | `contains_none` | true | `['proven']` | `<think>  </think>  A packed kernel experiment is a type of computational experiment where a large number of cores (or pr` |
| fused | `stress_contains_none_003` | `contains_none` | true | `['failure']` | `<think>  </think>  A negative result could be something that doesn't meet expectations, such as a low score, a negative ` |
| fused | `stress_contains_none_004` | `contains_none` | true | `['delete']` | `<think>  </think>  A C-drive cleanup involves removing or clearing out unnecessary files, data, or programs that are no ` |
| fused | `stress_contains_none_005` | `contains_none` | true | `['universal']` | `<think>  </think>  A benchmark slice is a specific, standardized piece of data or information used to evaluate or compar` |
| fused | `stress_sentence_count_000` | `sentence_count` | true | `{'count': 1}` | `<think>  </think>  The role-policy selector is a mechanism that selects the appropriate role and policy based on the con` |
| fused | `stress_sentence_count_001` | `sentence_count` | false | `{'count': 2}` | `<think>  </think>  Layer 20 expansion can be risky due to its high demand and limited capacity, which may lead to overex` |
| fused | `stress_sentence_count_002` | `sentence_count` | true | `{'count': 1}` | `<think>  </think>  A disk guard is useful in exactly one sentence.` |
| fused | `stress_word_count_000` | `word_count` | false | `{'count': 3}` | `<think>  </think>  Speed up!` |
| fused | `stress_word_count_001` | `word_count` | false | `{'count': 4}` | `<think>  </think>  Robust calibration evidence supports accurate model predictions.` |
| fused | `stress_word_count_002` | `word_count` | false | `{'count': 5}` | `<think>  </think>  The conservative V-only policy emphasizes limiting government intervention in private sectors.` |
| fused | `stress_all_of_000` | `all_of` | true | `[{'type': 'json_keys', 'answer': ['risk', 'next_step']}, {'type': 'contains_none', 'answer': ['unsafe']}]` | `<think>  </think>  ```json {   "risk": "low",   "next_step": "review the data further" } ```` |
| fused | `stress_all_of_001` | `all_of` | true | `[{'type': 'sentence_count', 'answer': {'count': 1}}, {'type': 'contains_all', 'answer': ['calibration', 'memory']}, {'type': 'contains_none', 'answer': ['universal']}]` | `<think>  </think>  Calibration ensures accurate memory, helping to maintain precise data storage and retrieval.` |
| fused | `stress_all_of_002` | `all_of` | true | `[{'type': 'json_keys', 'answer': ['policy', 'speedup']}, {'type': 'contains_none', 'answer': ['sota']}]` | `<think>  </think>  ```json {   "policy": "speedup",   "speedup": "increase" } ```` |
| fused | `stress_all_of_003` | `all_of` | false | `[{'type': 'word_count', 'answer': {'count': 4}}, {'type': 'contains_all', 'answer': ['ttft', 'memory']}]` | `<think>  </think>  1. **Ttft Memory**   2. **Ttft Memory**   3. **Ttft Memory**   4` |
| fused | `stress_all_of_004` | `all_of` | true | `[{'type': 'json_keys', 'answer': ['layer', 'verdict']}, {'type': 'contains_none', 'answer': ['proven']}]` | `<think>  </think>  ```json {   "layer": "layer",   "verdict": "verdict" } ```` |
| fused | `stress_all_of_005` | `all_of` | true | `[{'type': 'sentence_count', 'answer': {'count': 1}}, {'type': 'contains_all', 'answer': ['held', 'out', 'prompt']}, {'type': 'contains_none', 'answer': ['official']}]` | `<think>  </think>  The prompt was held out for the user to review.` |
