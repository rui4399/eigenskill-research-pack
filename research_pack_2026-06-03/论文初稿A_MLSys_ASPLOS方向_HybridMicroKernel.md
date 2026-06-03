# Paper Draft A - Systems Track

## Working Title

EigenSkill: A Hybrid Micro-Kernel Runtime for Skill-Specialized Edge Language Model Inference

## Target Venues

Primary: Journal of Systems Architecture, ACM TECS.

Long-term: MLSys or ASPLOS after stronger system evaluation.

## Abstract

Deploying language models on edge devices is constrained by memory bandwidth, framework overhead, and the mismatch between dense Transformer execution and low-entropy edge tasks. We present EigenSkill, a hybrid inference runtime that separates semantic skill routing from deterministic or low-rank skill execution. Instead of forcing every request through a dense language-model path, EigenSkill routes structured skills such as unit/time normalization, JSON repair, command normalization, packet encoding, sensor triage, and safety gating into specialized micro-kernels whenever their output contract is known. A small language model remains responsible for semantic routing and tasks that require natural-language generalization.

We implement a proof-of-concept using `HuggingFaceTB/SmolLM2-360M-Instruct` with LoRA fine-tuning over eight edge-oriented skills. The pure model achieves 96.60% exact match on 1440 controlled evaluation cases. A hybrid runtime that bypasses the model for deterministic unit/time normalization improves exact match to 99.93%. We also implement a C++ low-rank skill-path microbenchmark comparing dense `W x` execution with a factorized `U A U^T x` path. Our results suggest that skill-specialized hybrid inference is a practical first step toward hardware-aware edge LLM deployment, while full spectral routing requires additional theoretical and empirical validation.

## 1. Introduction

Many edge LLM workloads are not open-ended generation problems. A sensor node, home controller, drone module, or low-power gateway often needs a bounded transformation: classify a sensor event, normalize a command, repair a JSON packet, check whether an action should be blocked, or encode a small packet for downstream execution. Running a full dense Transformer path for every such request is inefficient and sometimes less reliable than deterministic code.

EigenSkill begins from a simple observation: **low-entropy skills should be compiled into runtime paths, not merely prompted into language behavior**. The model should interpret natural language and route requests; the runtime should execute skills whose contracts are known.

## 2. Contributions

1. We propose a hybrid skill inference architecture that separates semantic routing from micro-kernel execution.
2. We build an eight-skill LoRA fine-tuning and evaluation pipeline over a 360M-parameter instruction model.
3. We show that deterministic bypass can remove a systematic failure class in unit/time normalization, improving controlled exact match from 96.60% to 99.93%.
4. We implement a C++ low-rank microbenchmark that isolates the systems ceiling of replacing dense `W x` with `U A U^T x`.
5. We identify the remaining gap between practical hybrid bypass and the more ambitious eigen-regularized Transformer route.

## 3. System Design

EigenSkill runtime has three layers:

| Layer | Role | Current implementation |
| --- | --- | --- |
| Skill contract layer | Defines prompt, schema, label space, and evaluation rules | Python schema and data generator |
| Semantic model layer | Handles natural-language routing and non-deterministic extraction | Merged FP16 SmolLM2-360M LoRA |
| Micro-kernel layer | Executes deterministic or low-rank skills | Python parser and C++ benchmark |

The current runtime first checks whether a skill has a deterministic bypass. If yes, it executes that bypass and returns canonical output. Otherwise, it builds a skill-specific prompt and runs the merged FP16 model.

## 4. Experimental Setup

The prototype uses eight skills:

```text
intent_routing, json_repair, field_extraction, command_normalization, sensor_event_triage, packet_encode, safety_gate, unit_time_normalize
```

Each skill has 900 training examples and 180 evaluation examples. The base model is `HuggingFaceTB/SmolLM2-360M-Instruct`. The training method is LoRA with rank 16 and alpha 32.

## 5. Results

| Runtime | Exact match |
| --- | ---: |
| Pure model | 1391/1440 (96.60%) |
| Hybrid runtime | 1439/1440 (99.93%) |

The key improvement comes from `unit_time_normalize`, where the pure model reaches only 73.33%. The failure mode is not random semantic confusion; the model often computes the answer but violates the contract by returning a bare unit string or natural-language explanation. The hybrid runtime replaces this path with a deterministic parser and reaches 100.00%.

## 6. Discussion

The result supports a systems thesis: for bounded edge skills, the best runtime is often not a smaller prompt or more fine-tuning, but a hybrid path that moves contract-heavy transformations into executable kernels. This also improves interpretability: a failure can be attributed to routing, deterministic parsing, or model generation.

## 7. Limitations

The evaluation is controlled and synthetic/semisynthetic. The C++ benchmark currently uses a synthetic low-rank matrix, not real Transformer weights. No ARM/RK3588/NPU power measurement has been completed yet. Therefore, this draft should not claim production-level acceleration until latency and energy experiments are added.

## 8. Next Experiments

- Port `unit_time_normalize` parser to C++.
- Measure latency against merged FP16 and INT8 model paths.
- Add llama.cpp or ONNX Runtime baselines.
- Test on at least one edge platform.
- Add branch overhead and cache behavior measurements.

## 已核验/需二次核验来源

- ASPLOS 2026 CFP: https://www.asplos-conference.org/asplos2026/cfp/
- ASPLOS'27 CFP: https://www.asplos-conference.org/call-for-papers-asplos27/
- MLSys 2026: https://mlsys.org/
- IEEE Internet of Things Journal: https://ieee-iotj.org/
- ACM Transactions on Embedded Computing Systems: https://acmtecs.hosting.acm.org/
- ACM Transactions on Cyber-Physical Systems: https://www.codes-isss.org/tcps_subdomain/index/
- Journal of Systems Architecture: https://www.sciencedirect.com/journal/journal-of-systems-architecture
- Elsevier Internet of Things: https://www.sciencedirect.com/journal/internet-of-things
- 本地实验依据：`outputs/eigenskill_v2_package_manifest.json`、`outputs/EigenSkill-v2-Hybrid-Training-Report.md`、`train_python/README.md`

说明：网页 scope 和投稿时间会随年度变化。本文档的场景匹配和路线判断已按 2026-06-03 的公开页面做过初步核验，但正式投稿前必须重新确认当年 CFP、页数、匿名要求、重投限制、APC/开放获取政策和 special issue 状态。
