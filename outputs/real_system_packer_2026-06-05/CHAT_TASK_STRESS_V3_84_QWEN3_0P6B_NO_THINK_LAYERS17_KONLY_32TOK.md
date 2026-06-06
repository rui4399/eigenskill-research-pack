# Chat Task Benchmark

Model: `Qwen/Qwen3-0.6B`
Tasks: `84`
Task format: `native`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 46 / 84 | 0.5476 | 22.2020 | 0.102085 |
| fused | 45 / 84 | 0.5357 | 21.6377 | 0.099487 |

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
| baseline | `stress_mcq_extra_000` | `mcq` | true | `A` | `<think>  </think>  A. ESMP binaries` |
| baseline | `stress_mcq_extra_001` | `mcq` | true | `A` | `<think>  </think>  A. max-start-memory-ratio` |
| baseline | `stress_mcq_extra_002` | `mcq` | true | `A` | `<think>  </think>  A. Task pass count` |
| baseline | `stress_mcq_extra_003` | `mcq` | true | `A` | `<think>  </think>  A. Q only` |
| baseline | `stress_mcq_extra_004` | `mcq` | false | `A` | `<think>  </think>  D. IFEval Q-only` |
| baseline | `stress_mcq_extra_005` | `mcq` | true | `A` | `<think>  </think>  A. Model cache` |
| baseline | `stress_number_extra_000` | `number` | false | `168` | `<think>  </think>  84` |
| baseline | `stress_number_extra_001` | `number` | true | `20` | `<think>  </think>  The number of tasks failed is $ 42 - 22 = \boxed{20} $.` |
| baseline | `stress_number_extra_002` | `number` | false | `49` | `<think>  </think>  4033 rounded down is 4033. To find the percentage, divide by 8151:  $$ ` |
| baseline | `stress_number_extra_003` | `number` | true | `1387` | `<think>  </think>  1265 + 122 = 1387  The total number of MB freed is **1387` |
| baseline | `stress_number_extra_004` | `number` | true | `0` | `<think>  </think>  The total pass delta is 0.` |
| baseline | `stress_number_extra_005` | `number` | false | `512` | `<think>  </think>  A 4-bit row with 1024 weights uses **1 packed byte**.` |
| baseline | `stress_json_keys_extra_000` | `json_keys` | true | `['selected_policy', 'evidence']` | `<think>  </think>  ```json {   "selected_policy": "minified",   "evidence": "only" } ```` |
| baseline | `stress_json_keys_extra_001` | `json_keys` | true | `['c_free_gb', 'guard_limit']` | `<think>  </think>  ```json {"c_free_gb": "0", "guard_limit": "0"} ```` |
| baseline | `stress_json_keys_extra_002` | `json_keys` | false | `['split', 'pass_delta']` | `<think>  </think>  ```json {"pass_delta": "0"} ```` |
| baseline | `stress_json_keys_extra_003` | `json_keys` | false | `['role', 'packed']` | `<think>  </think>  ```json {"role": "packed"} ```` |
| baseline | `stress_json_keys_extra_004` | `json_keys` | true | `['benchmark', 'caveat']` | `<think>  </think>  ```json {"benchmark": "minified", "caveat": "only"} ```` |
| baseline | `stress_json_keys_extra_005` | `json_keys` | false | `['artifact', 'local_only']` | `<think>  </think>  ```json {"artifact": "local_only"} ```` |
| baseline | `stress_contains_all_extra_000` | `contains_all` | false | `['q-only', 'larger', 'slice']` | `<think>  </think>  The next validation target for the selected role policy is to ensure that all users are properly conf` |
| baseline | `stress_contains_all_extra_001` | `contains_all` | false | `['move', 'cache', 'compact']` | `<think>  </think>  A **careful storage migration plan** is a structured and systematic approach to transferring data fro` |
| baseline | `stress_contains_all_extra_002` | `contains_all` | false | `['timeout', 'invalid', 'result']` | `<think>  </think>  The term "full-QKV stress" is not a standard or widely recognized term in the context of stress analy` |
| baseline | `stress_contains_all_extra_003` | `contains_all` | false | `['packed', 'runtime', 'evidence']` | `<think>  </think>  A **conservative systems claim** refers to a claim that a particular system or policy is **conservati` |
| baseline | `stress_contains_all_extra_004` | `contains_all` | false | `['memory', 'disk', 'timeout']` | `<think>  </think>  The GPU guard records **system logs**, **user activity**, and **security events**.` |
| baseline | `stress_contains_all_extra_005` | `contains_all` | false | `['split', 'quality', 'regression']` | `<think>  </think>  Role policies need multiple splits for several key reasons:  1. **To Prevent Conflicts**: When a role` |
| baseline | `stress_contains_none_extra_000` | `contains_none` | true | `['final']` | `<think>  </think>  A candidate who only selects Q as their primary choice.` |
| baseline | `stress_contains_none_extra_001` | `contains_none` | true | `['proof']` | `<think>  </think>  A stress benchmark is a measure of how much pressure or stress a person experiences in a particular s` |
| baseline | `stress_contains_none_extra_002` | `contains_none` | true | `['panic']` | `<think>  </think>  C-drive pressure refers to the pressure or strain that a hard drive experiences when it's being used,` |
| baseline | `stress_contains_none_extra_003` | `contains_none` | true | `['upload']` | `<think>  </think>  Local artifacts are physical items that are created or used by people in a specific place. They can i` |
| baseline | `stress_contains_none_extra_004` | `contains_none` | true | `['bad']` | `<think>  </think>  A selector rejection occurs when the system or application fails to find or accept a particular optio` |
| baseline | `stress_contains_none_extra_005` | `contains_none` | true | `['unlimited']` | `<think>  </think>  GPU memory guarding refers to the process of protecting GPU memory from unauthorized access or misuse` |
| baseline | `stress_sentence_count_extra_000` | `sentence_count` | true | `{'count': 1}` | `<think>  </think>  Q-only is provisional because it represents the current state of knowledge and understanding at the t` |
| baseline | `stress_sentence_count_extra_001` | `sentence_count` | false | `{'count': 2}` | `<think>  </think>  Cache migration requires careful planning to prevent data loss, data corruption, and system instabili` |
| baseline | `stress_sentence_count_extra_002` | `sentence_count` | true | `{'count': 1}` | `<think>  </think>  Timeout results are excluded in exactly one sentence because they are not considered valid or meaning` |
| baseline | `stress_word_count_extra_000` | `word_count` | true | `{'count': 3}` | `<think>  </think>  Selected Role Policy.` |
| baseline | `stress_word_count_extra_001` | `word_count` | false | `{'count': 4}` | `<think>  </think>  storage cleanup summary.` |
| baseline | `stress_word_count_extra_002` | `word_count` | false | `{'count': 5}` | `<think>  </think>  Three splits matter because they define the path to success.` |
| baseline | `stress_all_of_extra_000` | `all_of` | true | `[{'type': 'json_keys', 'answer': ['policy', 'status']}, {'type': 'contains_none', 'answer': ['final']}]` | `<think>  </think>  ```json {   "policy": "policy",   "status": "status" } ```` |
| baseline | `stress_all_of_extra_001` | `all_of` | true | `[{'type': 'sentence_count', 'answer': {'count': 1}}, {'type': 'contains_all', 'answer': ['q-only', 'stress']}, {'type': 'contains_none', 'answer': ['proof']}]` | `<think>  </think>  Q-only and stress are both important factors in the success of a project.` |
| baseline | `stress_all_of_extra_002` | `all_of` | true | `[{'type': 'json_keys', 'answer': ['disk', 'action']}, {'type': 'contains_none', 'answer': ['delete']}]` | `<think>  </think>  ```json {   "disk": "disk",   "action": "action" } ```` |
| baseline | `stress_all_of_extra_003` | `all_of` | false | `[{'type': 'word_count', 'answer': {'count': 4}}, {'type': 'contains_all', 'answer': ['guard', 'memory']}]` | `<think>  </think>  1. Guarded Memory   2. Memory Guard   3. Memory Guarded   4. Guarded Memory` |
| baseline | `stress_all_of_extra_004` | `all_of` | true | `[{'type': 'json_keys', 'answer': ['timeout', 'citation']}, {'type': 'contains_none', 'answer': ['valid']}]` | `<think>  </think>  ```json {   "timeout": "1000",   "citation": "https://example.com/citation" } ```` |
| baseline | `stress_all_of_extra_005` | `all_of` | false | `[{'type': 'sentence_count', 'answer': {'count': 1}}, {'type': 'contains_all', 'answer': ['three', 'split']}, {'type': 'contains_none', 'answer': ['universal']}]` | `<think>  </think>  The two split and the third split are both important in this discussion.` |
| fused | `stress_mcq_000` | `mcq` | true | `A` | `<think>  </think>  A. TTFT` |
| fused | `stress_mcq_001` | `mcq` | true | `A` | `<think>  </think>  A. Packed INT4 weights` |
| fused | `stress_mcq_002` | `mcq` | true | `A` | `<think>  </think>  A. C4` |
| fused | `stress_mcq_003` | `mcq` | true | `A` | `<think>  </think>  A. Pass-count regression` |
| fused | `stress_mcq_004` | `mcq` | false | `A` | `<think>  </think>  D. Full QKV` |
| fused | `stress_mcq_005` | `mcq` | true | `A` | `<think>  </think>  A. IFEval` |
| fused | `stress_number_000` | `number` | false | `4096` | `<think>  </think>  We are given that there are 8192 signed 4-bit weights. Each byte can hold two weights.  - 81` |
| fused | `stress_number_001` | `number` | false | `65536` | `<think>  </think>  The number of packed bytes read is:  $$ \frac{32 \times 4096}{8} = 1` |
| fused | `stress_number_002` | `number` | false | `4.8` | `<think>  </think>  The average bit width is calculated by taking the weighted average of the bit widths of the rows.   -` |
| fused | `stress_number_003` | `number` | false | `21` | `<think>  </think>  The number of layers packed is $ 3 \times 24 = \boxed{72} $.` |
| fused | `stress_number_004` | `number` | false | `96` | `<think>  </think>  48` |
| fused | `stress_number_005` | `number` | false | `7335` | `<think>  </think>  The total memory is 8151 MiB. A 90% guard allows at most:  $$ 0.9 \` |
| fused | `stress_json_keys_000` | `json_keys` | false | `['metric', 'value']` | `<think>  </think>  ```json {"metric": "TTFT"} ```` |
| fused | `stress_json_keys_001` | `json_keys` | false | `['risk', 'evidence']` | `<think>  </think>  ```json {   "risk": "calibration_split_inconsistency",   "evidence": "calibration_split_inconsistency` |
| fused | `stress_json_keys_002` | `json_keys` | true | `['policy', 'decision']` | `<think>  </think>  ```json {"policy": "V-only", "decision": "V-only"} ```` |
| fused | `stress_json_keys_003` | `json_keys` | true | `['memory_mb', 'tokens_per_second']` | `<think>  </think>  ```json {"memory_mb": "0", "tokens_per_second": "0"} ```` |
| fused | `stress_json_keys_004` | `json_keys` | true | `['layer', 'role']` | `<think>  </think>  ```json {"layer": "minified", "role": "only"} ```` |
| fused | `stress_json_keys_005` | `json_keys` | false | `['dataset', 'pass_count']` | `<think>  </think>  ```json {"dataset": "pass_count"} ```` |
| fused | `stress_contains_all_000` | `contains_all` | false | `['perplexity', 'task', 'accuracy']` | `<think>  </think>  PPL alone is incomplete for instruction models because it lacks the ability to understand and generat` |
| fused | `stress_contains_all_001` | `contains_all` | false | `['ttft', 'throughput', 'memory']` | `<think>  </think>  Three physical deployment metrics for edge LLM inference are:  1. **Latency**: The time it takes for ` |
| fused | `stress_contains_all_002` | `contains_all` | false | `['calibration', 'split', 'instability']` | `<think>  </think>  Calibration robustness is crucial because it ensures that the system's performance remains stable and` |
| fused | `stress_contains_all_003` | `contains_all` | false | `['compression', 'latency', 'speedup']` | `<think>  </think>  **Caveat:**   Packed compression and real runtime are not standard terms in the context of software d` |
| fused | `stress_contains_all_004` | `contains_all` | false | `['download', 'leakage', 'random']` | `<think>  </think>  A deterministic stress slice should avoid **inconsistencies, ambiguities, and non-physical assumption` |
| fused | `stress_contains_all_005` | `contains_all` | false | `['device', 'ttft', 'tokens']` | `<think>  </think>  Before claiming phone deployment, the following must be measured:  1. **Phone Model and Specification` |
| fused | `stress_contains_none_000` | `contains_none` | true | `['sota']` | `<think>  </think>  A conservative result is one that prioritizes stability, long-term planning, and adherence to establi` |
| fused | `stress_contains_none_001` | `contains_none` | true | `['official']` | `<think>  </think>  A local diagnostic is a person who checks and evaluates a person's health, often based on their sympt` |
| fused | `stress_contains_none_002` | `contains_none` | true | `['proven']` | `<think>  </think>  A packed kernel experiment is a type of computational experiment where a large number of cores are us` |
| fused | `stress_contains_none_003` | `contains_none` | true | `['failure']` | `<think>  </think>  A negative result could be something that doesn't meet expectations, such as a low score, a negative ` |
| fused | `stress_contains_none_004` | `contains_none` | true | `['delete']` | `<think>  </think>  A C-drive cleanup involves removing or clearing out unnecessary files, data, or system settings that ` |
| fused | `stress_contains_none_005` | `contains_none` | true | `['universal']` | `<think>  </think>  A benchmark slice is a specific, standardized piece of data or information used to evaluate or compar` |
| fused | `stress_sentence_count_000` | `sentence_count` | true | `{'count': 1}` | `<think>  </think>  The role-policy selector is a mechanism that determines which role or policy to apply based on the co` |
| fused | `stress_sentence_count_001` | `sentence_count` | false | `{'count': 2}` | `<think>  </think>  Layer 20 expansion can be risky due to its high demand for infrastructure and resources, which may st` |
| fused | `stress_sentence_count_002` | `sentence_count` | true | `{'count': 1}` | `<think>  </think>  A disk guard is useful in exactly one sentence.` |
| fused | `stress_word_count_000` | `word_count` | false | `{'count': 3}` | `<think>  </think>  Speed, Memory, and Latency.` |
| fused | `stress_word_count_001` | `word_count` | false | `{'count': 4}` | `<think>  </think>  Robust calibration evidence supports accurate model predictions.` |
| fused | `stress_word_count_002` | `word_count` | false | `{'count': 5}` | `<think>  </think>  A conservative V-only policy.` |
| fused | `stress_all_of_000` | `all_of` | true | `[{'type': 'json_keys', 'answer': ['risk', 'next_step']}, {'type': 'contains_none', 'answer': ['unsafe']}]` | `<think>  </think>  ```json {   "risk": "low",   "next_step": "analyze further" } ```` |
| fused | `stress_all_of_001` | `all_of` | true | `[{'type': 'sentence_count', 'answer': {'count': 1}}, {'type': 'contains_all', 'answer': ['calibration', 'memory']}, {'type': 'contains_none', 'answer': ['universal']}]` | `<think>  </think>  Calibration ensures accurate memory, and memory is essential for maintaining proper calibration.` |
| fused | `stress_all_of_002` | `all_of` | true | `[{'type': 'json_keys', 'answer': ['policy', 'speedup']}, {'type': 'contains_none', 'answer': ['sota']}]` | `<think>  </think>  ```json {   "policy": "speedup",   "speedup": "increase" } ```` |
| fused | `stress_all_of_003` | `all_of` | false | `[{'type': 'word_count', 'answer': {'count': 4}}, {'type': 'contains_all', 'answer': ['ttft', 'memory']}]` | `<think>  </think>  1. **Ttft Memory**   2. **Ttft Memory**   3. **Ttft Memory**   4` |
| fused | `stress_all_of_004` | `all_of` | true | `[{'type': 'json_keys', 'answer': ['layer', 'verdict']}, {'type': 'contains_none', 'answer': ['proven']}]` | `<think>  </think>  ```json {   "layer": "layer",   "verdict": "verdict" } ```` |
| fused | `stress_all_of_005` | `all_of` | true | `[{'type': 'sentence_count', 'answer': {'count': 1}}, {'type': 'contains_all', 'answer': ['held', 'out', 'prompt']}, {'type': 'contains_none', 'answer': ['official']}]` | `<think>  </think>  The prompt was held out for the user to review.` |
| fused | `stress_mcq_extra_000` | `mcq` | true | `A` | `<think>  </think>  A. ESMP binaries` |
| fused | `stress_mcq_extra_001` | `mcq` | true | `A` | `<think>  </think>  A. max-start-memory-ratio` |
| fused | `stress_mcq_extra_002` | `mcq` | true | `A` | `<think>  </think>  A. Task pass count` |
| fused | `stress_mcq_extra_003` | `mcq` | true | `A` | `<think>  </think>  A. Q only` |
| fused | `stress_mcq_extra_004` | `mcq` | false | `A` | `<think>  </think>  D. IFEval Q-only` |
| fused | `stress_mcq_extra_005` | `mcq` | true | `A` | `<think>  </think>  A. Model cache` |
| fused | `stress_number_extra_000` | `number` | false | `168` | `<think>  </think>  84` |
| fused | `stress_number_extra_001` | `number` | true | `20` | `<think>  </think>  The policy failed $ 42 - 22 = \boxed{20} $ tasks.` |
| fused | `stress_number_extra_002` | `number` | false | `49` | `<think>  </think>  4033 rounded down is 4033. To find the percentage used:  $$ \frac{4033` |
| fused | `stress_number_extra_003` | `number` | true | `1387` | `<think>  </think>  1265 + 122 = 1387  Final answer: 1387` |
| fused | `stress_number_extra_004` | `number` | true | `0` | `<think>  </think>  The total pass delta is 0.` |
| fused | `stress_number_extra_005` | `number` | false | `512` | `<think>  </think>  A 4-bit row with 1024 weights uses **1 packed byte**.` |
| fused | `stress_json_keys_extra_000` | `json_keys` | true | `['selected_policy', 'evidence']` | `<think>  </think>  ```json {   "selected_policy": "minified",   "evidence": "only" } ```` |
| fused | `stress_json_keys_extra_001` | `json_keys` | true | `['c_free_gb', 'guard_limit']` | `<think>  </think>  ```json {"c_free_gb": "0", "guard_limit": "0"} ```` |
| fused | `stress_json_keys_extra_002` | `json_keys` | false | `['split', 'pass_delta']` | `<think>  </think>  ```json {"pass_delta": "0"} ```` |
| fused | `stress_json_keys_extra_003` | `json_keys` | false | `['role', 'packed']` | `<think>  </think>  ```json {"role": "packed"} ```` |
| fused | `stress_json_keys_extra_004` | `json_keys` | true | `['benchmark', 'caveat']` | `<think>  </think>  ```json {"benchmark": "minified", "caveat": "only"} ```` |
| fused | `stress_json_keys_extra_005` | `json_keys` | false | `['artifact', 'local_only']` | `<think>  </think>  ```json {"artifact": "local_only"} ```` |
| fused | `stress_contains_all_extra_000` | `contains_all` | false | `['q-only', 'larger', 'slice']` | `<think>  </think>  The next validation target for the selected role policy is to ensure that the role is assigned correc` |
| fused | `stress_contains_all_extra_001` | `contains_all` | false | `['move', 'cache', 'compact']` | `<think>  </think>  A **careful storage migration plan** is a structured and systematic approach to transferring data fro` |
| fused | `stress_contains_all_extra_002` | `contains_all` | false | `['timeout', 'invalid', 'result']` | `<think>  </think>  The term "full-QKV stress" is not a standard or widely recognized term in the context of stress analy` |
| fused | `stress_contains_all_extra_003` | `contains_all` | false | `['packed', 'runtime', 'evidence']` | `<think>  </think>  A **conservative systems claim** refers to a statement or argument that emphasizes the **conservative` |
| fused | `stress_contains_all_extra_004` | `contains_all` | false | `['memory', 'disk', 'timeout']` | `<think>  </think>  The GPU guard records **system logs**, **user activity**, and **security alerts**.` |
| fused | `stress_contains_all_extra_005` | `contains_all` | false | `['split', 'quality', 'regression']` | `<think>  </think>  Role policies need multiple splits because:  1. **Role definitions are dynamic**: Roles can change ov` |
| fused | `stress_contains_none_extra_000` | `contains_none` | true | `['final']` | `<think>  </think>  A candidate who only selects Q as their primary choice, without considering other options.` |
| fused | `stress_contains_none_extra_001` | `contains_none` | true | `['proof']` | `<think>  </think>  A stress benchmark is a measure of how much pressure or stress a person experiences in a particular s` |
| fused | `stress_contains_none_extra_002` | `contains_none` | true | `['panic']` | `<think>  </think>  C-drive pressure refers to the pressure or stress that a computer's hard drive experiences when it's ` |
| fused | `stress_contains_none_extra_003` | `contains_none` | true | `['upload']` | `<think>  </think>  Local artifacts are physical items that are created or collected by people in a specific place. They ` |
| fused | `stress_contains_none_extra_004` | `contains_none` | true | `['bad']` | `<think>  </think>  A selector rejection occurs when the chosen option doesn't meet the criteria or doesn't fit the requi` |
| fused | `stress_contains_none_extra_005` | `contains_none` | true | `['unlimited']` | `<think>  </think>  GPU memory guarding is a security measure that protects the GPU from unauthorized access to its memor` |
| fused | `stress_sentence_count_extra_000` | `sentence_count` | true | `{'count': 1}` | `<think>  </think>  Q-only is provisional because it represents the current state of knowledge and understanding at the t` |
| fused | `stress_sentence_count_extra_001` | `sentence_count` | false | `{'count': 2}` | `<think>  </think>  Cache migration requires careful planning to prevent data loss, and it should be done in a controlled` |
| fused | `stress_sentence_count_extra_002` | `sentence_count` | true | `{'count': 1}` | `<think>  </think>  Timeout results are excluded in exactly one sentence because they are not considered valid or meaning` |
| fused | `stress_word_count_extra_000` | `word_count` | true | `{'count': 3}` | `<think>  </think>  Selected Role Policy.` |
| fused | `stress_word_count_extra_001` | `word_count` | false | `{'count': 4}` | `<think>  </think>  storage cleanup summary.` |
| fused | `stress_word_count_extra_002` | `word_count` | false | `{'count': 5}` | `<think>  </think>  Three splits matter because they define the path to success.` |
| fused | `stress_all_of_extra_000` | `all_of` | true | `[{'type': 'json_keys', 'answer': ['policy', 'status']}, {'type': 'contains_none', 'answer': ['final']}]` | `<think>  </think>  ```json {   "policy": "policy",   "status": "status" } ```` |
| fused | `stress_all_of_extra_001` | `all_of` | true | `[{'type': 'sentence_count', 'answer': {'count': 1}}, {'type': 'contains_all', 'answer': ['q-only', 'stress']}, {'type': 'contains_none', 'answer': ['proof']}]` | `<think>  </think>  Q-only and stress are both important factors in achieving clarity and focus.` |
| fused | `stress_all_of_extra_002` | `all_of` | true | `[{'type': 'json_keys', 'answer': ['disk', 'action']}, {'type': 'contains_none', 'answer': ['delete']}]` | `<think>  </think>  ```json {   "disk": "disk",   "action": "action" } ```` |
| fused | `stress_all_of_extra_003` | `all_of` | false | `[{'type': 'word_count', 'answer': {'count': 4}}, {'type': 'contains_all', 'answer': ['guard', 'memory']}]` | `<think>  </think>  1. Guarded Memory   2. Memory Guard   3. Memory Guarded   4. Guarded Memory` |
| fused | `stress_all_of_extra_004` | `all_of` | true | `[{'type': 'json_keys', 'answer': ['timeout', 'citation']}, {'type': 'contains_none', 'answer': ['valid']}]` | `<think>  </think>  ```json {   "timeout": "10000",   "citation": "https://example.com/citation" } ` |
| fused | `stress_all_of_extra_005` | `all_of` | false | `[{'type': 'sentence_count', 'answer': {'count': 1}}, {'type': 'contains_all', 'answer': ['three', 'split']}, {'type': 'contains_none', 'answer': ['universal']}]` | `<think>  </think>  The two split and the third split are both important in this discussion.` |
