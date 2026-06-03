# quant-v1 数据修复与旁路基线

日期：2026-06-03

## 结论摘要

这一轮实验把 EigenSkill-Q 从“训练完成”推进到更可信的工程证据：我们发现并修复了量化策略数据集 v0 的一个关键可学习性问题，并建立了一个 100% 可复现的确定性旁路微内核基线。

当前最重要的结论不是“纯 LoRA 小模型已经学会量化数学”，而是：

1. 量化策略任务更像数值规则编译/微内核路由，不适合完全交给 360M 小模型短 SFT 记忆。
2. 修复后的 quant-v1 数据集可以从输入文本完全复原标签，train/eval/test 没有 exact 或 input overlap。
3. 确定性 EigenSkill bypass 在 quant-v1 eval/test 上达到 100% exact_json 与 100% decision_exact。
4. 纯 LoRA smoke 仍然是负结果，应作为“为什么需要旁路微内核”的证据，而不是包装成泛化成功。

## 数据集修复

新增/更新脚本：

- `train_python/generate_quant_skill_data.py`
- `train_python/hybrid_eval_quant_policy.py`
- `train_python/eval_quant_policy.py`

quant-v1 输出：

- `data_eval/eigenskill_quant_v1/train.jsonl`
- `data_eval/eigenskill_quant_v1/eval.jsonl`
- `data_eval/eigenskill_quant_v1/test.jsonl`
- `data_eval/eigenskill_quant_v1/audit.json`

数据规模：

| split | rows | per skill |
|---|---:|---:|
| train | 1200 | 240 |
| eval | 400 | 80 |
| test | 400 | 80 |

无泄漏审计：

| pair | exact overlap | input overlap |
|---|---:|---:|
| train-eval | 0 | 0 |
| train-test | 0 | 0 |
| eval-test | 0 | 0 |

## 修复点

v0 的部分标签使用生成时的高精度隐藏浮点值计算，但输入文本只暴露 2-3 位小数。这会制造不可学习标签，尤其影响 `outlier_detect` 的 `risk/protect/policy`。

v1 修复策略：先把参数四舍五入到输入中实际可见的小数，再基于可见值生成标签。这样模型或旁路微内核面对的是可判定任务。

同时修复了旁路评估脚本的解析问题：`p99` 中的 `99` 不能被当作一个数值特征，必须按字段名解析 `max/p99/kurtosis`。

## v1 确定性旁路基线

脚本：`train_python/hybrid_eval_quant_policy.py`

输出：

- `outputs/eigenskill_quant_v1_eval_hybrid_policy.json`
- `outputs/eigenskill_quant_v1_test_hybrid_policy.json`

### Eval

| metric | value |
|---|---:|
| n | 400 |
| exact_json | 1.000 |
| decision_exact | 1.000 |
| parse_error | 0.000 |

### Test

| metric | value |
|---|---:|
| n | 400 |
| exact_json | 1.000 |
| decision_exact | 1.000 |
| parse_error | 0.000 |

五类 skill 均为 100%：

- `outlier_detect`
- `bit_allocate`
- `rotation_select`
- `residual_patch`
- `kv_policy`

这说明当前任务可以被一个轻量 C++/SIMD/regex-parser 风格的量化策略旁路微内核稳定解决，适合作为 EigenSkill 的系统侧核心证据。

## 纯 LoRA 结果

v0 1 epoch LoRA：

- 模型：`models/eigenskill-quant-v0-smollm2-360m-lora-fp16`
- 训练日志：`outputs/eigenskill_quant_v0_train_1epoch.log`
- eval_loss: 0.7816
- eval_mean_token_accuracy: 0.7962
- 生成式 60 条 policy eval: `decision_exact = 0.0`

v1 smoke LoRA：

- 模型：`models/eigenskill-quant-v1-smollm2-360m-lora-smoke`
- 训练日志：`outputs/eigenskill_quant_v1_train_smoke.log`
- eval_loss: 1.549
- eval_mean_token_accuracy: 0.6968
- 生成式 60 条 policy eval: `decision_exact = 0.0`

解释：token-level accuracy 不能证明策略生成正确。短训 LoRA 学到了一部分 JSON 形态或 skill token，但没有稳定学到数值比较、阈值分段和字段约束。

## 对论文主线的影响

更可信的表述应从“LLM 自身学会所有量化数学”转为：

> EigenSkill-Q 将量化策略拆成可验证的小型 skill routing contract。LLM/adapter 负责语义触发和 skill id 选择，数值敏感的 rate-distortion / outlier / rotation / KV cache policy 则交给确定性旁路微内核执行，从而在低功耗端侧取得可解释、可验证、低延迟的策略推理。

这个方向比纯 SFT 更像系统/模型协同设计，也更适合 MLSys、ASPLOS workshop、TinyML、edge AI、embedded AI 方向。

## 下一步

1. 把 `hybrid_eval_quant_policy.py` 迁移到 C++，做 SIMD/regex-free 的结构化 parser + policy kernel。
2. 把 quant-v1 扩展到真实量化方法：GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant/KVQuant/MXFP4/NVFP4 等。
3. 不再只用 token accuracy，固定使用：schema valid、decision exact、exact JSON、latency、energy、memory traffic。
4. 如果继续训练 LoRA，需要加入 completion-only loss、结构化 JSON grammar/constrained decoding，或把模型目标改成只预测 `skill_id + policy_family`，不要让小模型直接回归连续小数。
5. 对导师汇报时，应把纯 LoRA 负结果解释为“旁路必要性证据”，不要回避。
