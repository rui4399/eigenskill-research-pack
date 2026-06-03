# EigenSkill v2 Hybrid 训练与评估报告

日期：2026-06-03

## 结论

EigenSkill v2 已完成 targeted 训练、全量生成评测、merged FP16 导出、dynamic INT8 CPU 导出，并增加了一个面向端侧部署的 hybrid runtime 评测层。

核心结果：

- 纯模型 v2：1391/1440 exact，overall exact = 96.60%。
- v2 hybrid runtime：1439/1440 exact，overall exact = 99.93%。

v2 targeted 训练修复了 `intent_routing`，从 v1 的 95.63% 提升到 99.44%。`unit_time_normalize` 纯模型只从 68.75% 提升到 73.33%，说明小模型对单位换算的语言先验仍会压过 JSON 契约。更可靠的交付形态是：LLM 负责多数 skill，`unit_time_normalize` 由确定性 parser 兜底，形成 hybrid micro-kernel。

## 产物

| Artifact | Path | Size |
| --- | --- | ---: |
| LoRA adapter v2 | `models/eigenskill-smollm2-360m-lora-v2-fp16` | 242.95 MiB |
| Merged FP16 v2 | `models/eigenskill-smollm2-360m-merged-v2-fp16` | 693.51 MiB |
| Dynamic INT8 CPU v2 | `models/eigenskill-smollm2-360m-int8-v2-dynamic` | 528.90 MiB |
| Pure model eval | `outputs/eigenskill_v2_eval.json` | 639240 bytes |
| Hybrid eval | `outputs/eigenskill_v2_hybrid_eval.json` | generated |
| Train log | `outputs/eigenskill_v2_train.log` | 436907 bytes |

## 训练设置

- Base model: `HuggingFaceTB/SmolLM2-360M-Instruct`
- 数据：8 skills，每个 skill 900 条 train、180 条 eval
- 总训练样本：7200
- 总 eval 样本：1440
- 训练轮数：1.5 epoch
- global step: 675
- LoRA rank: 16
- LoRA alpha: 32
- learning rate: 1.2e-4
- max length: 512
- gradient checkpointing: enabled

checkpoint-600 指标：

- `eval_loss`: 0.000861425
- `eval_mean_token_accuracy`: 1.0
- `eval_entropy`: 0.008060886

## 纯模型 v2 生成评测

| Skill | n | Exact | JSON valid | Schema ok |
| --- | ---: | ---: | ---: | ---: |
| `json_repair` | 180 | 100.00% | 100.00% | 100.00% |
| `unit_time_normalize` | 180 | 73.33% | 73.89% | 73.89% |
| `packet_encode` | 180 | 100.00% | 100.00% | 100.00% |
| `sensor_event_triage` | 180 | 100.00% | 0.00% | 0.00% |
| `command_normalization` | 180 | 100.00% | 100.00% | 100.00% |
| `field_extraction` | 180 | 100.00% | 100.00% | 100.00% |
| `intent_routing` | 180 | 99.44% | 0.00% | 0.00% |
| `safety_gate` | 180 | 100.00% | 0.00% | 0.00% |

纯模型剩余失败：

- `unit_time_normalize`: 48/180。典型问题是输出 `1500g`、`1500`、`2m is not a valid unit of measurement`，而不是完整 JSON。
- `intent_routing`: 1/180。`陪我聊会儿，尽快` 被误判为 `reminder`。

## Hybrid Runtime 评测

Hybrid 规则：

- 其它 skill 仍使用模型输出。
- `unit_time_normalize` 由确定性 parser 兜底，输出固定 schema：`kind,duration_minutes,value,unit,date,time`。

| Skill | n | Exact | JSON valid | Schema ok | Hybrid overrides |
| --- | ---: | ---: | ---: | ---: | ---: |
| `json_repair` | 180 | 100.00% | 100.00% | 100.00% | 0 |
| `unit_time_normalize` | 180 | 100.00% | 100.00% | 100.00% | 180 |
| `packet_encode` | 180 | 100.00% | 100.00% | 100.00% | 0 |
| `sensor_event_triage` | 180 | 100.00% | 0.00% | 0.00% | 0 |
| `command_normalization` | 180 | 100.00% | 100.00% | 100.00% | 0 |
| `field_extraction` | 180 | 100.00% | 100.00% | 100.00% | 0 |
| `intent_routing` | 180 | 99.44% | 0.00% | 0.00% | 0 |
| `safety_gate` | 180 | 100.00% | 0.00% | 0.00% | 0 |

Hybrid overall exact = 99.93%。

## 工程判断

`unit_time_normalize` 不适合继续用小模型硬记。单位换算、时间标准化本来就是典型 deterministic micro-kernel，应该在端侧以 C++/SIMD/查表/parser 形式实现，再由模型做意图路由和无法规则化的自然语言槽位处理。这比继续堆 LoRA 数据更符合 EigenSkill 的系统目标：把可规则化技能从 LLM dense path 中旁路出去。

## 推荐下一步

1. 将 `train_python/hybrid_eval_skills.py` 的 parser 迁移到 C++ runtime，作为第一个真实 bypass skill。
2. 给 `intent_routing` 增加“chat vs reminder”极小 hard-negative patch，目标把最后 1 个误判消掉。
3. 为 hybrid package 增加一个小型 CLI：输入 `<skill:...>` prompt，输出模型结果或 parser 旁路结果。
4. 继续保持 FP16/INT8 高精度，不急着做 INT4/1-bit。

## Notion 状态

Notion MCP 当前是 `enabled / OAuth`，但本轮仍未热加载出 Notion 写入工具。可写入的摘要已生成在：

- `outputs/EigenSkill-v2-Notion-Summary.md`

刷新或重启 Codex 后，可直接写入 Notion。
