# EigenSkill-Q 阶段交付：可验证量化策略旁路

日期：2026-06-04

## 结论

当前最稳的研究主线是：

```text
Verifiable Policy Bypass for Sensitivity-Rate-Distortion Guided
Mixed-Precision LLM Quantization
```

不要把项目写成已经完成的 edge LLM、swarm LLM 或真正 eigen-routing。短周期
成果应聚焦在“量化策略技能 + 可验证 policy kernel + 数学/强化学习扩展”。

## 已完成

1. 新增 C++ policy evaluator：
   `inference_cpp/src/quant_policy_bypass.cpp`
2. 扩展 Windows/MSVC build 脚本：
   `inference_cpp/build-msvc.ps1 -Target quant-policy`
3. 验证 eval/test：

| split | rows | policy_fields_exact | decision_exact | parse_error | throughput |
|---|---:|---:|---:|---:|---:|
| eval | 400 | 1.000000 | 1.000000 | 0.000000 | 8261 rows/s |
| test | 400 | 1.000000 | 1.000000 | 0.000000 | 6924 rows/s |

4. Python strict oracle 已验证：

| split | rows | exact_json | decision_exact | parse_error |
|---|---:|---:|---:|---:|
| eval | 400 | 1.000000 | 1.000000 | 0.000000 |
| test | 400 | 1.000000 | 1.000000 | 0.000000 |

5. 已写交付文件：

```text
outputs/EigenSkill-Q-Cpp-Policy-Bypass-Report.md
outputs/paper_delivery_2026-06-04/EigenSkill-Q_CCF-A_Draft.md
outputs/paper_delivery_2026-06-04/EigenSkill-Q_CCF-A_Draft_v2_Loss_Sensitive.md
outputs/paper_delivery_2026-06-04/EigenSkill-Q_CCF-A_Draft_v2_Loss_Sensitive.docx
outputs/paper_delivery_2026-06-04/EigenSkill-Q_CCF-A_Draft_v2_Loss_Sensitive.html
outputs/paper_delivery_2026-06-04/导师速览.md
outputs/paper_delivery_2026-06-04/authorization-and-channel-audit.md
```

## 2026-06-04 增补：loss-sensitive 量化分配正结果

本阶段把 EigenSkill-Q 的量化主线从 activation-stat proxy 推进到 measured
loss sensitivity。具体做法是对 SmolLM2-360M 的 225 个 Linear 模块逐一做
group-wise INT4 fake quant，测量单模块量化导致的短 prompt loss 增量，然后
在 4.5 weighted average bits 预算下把 8-bit 分配给最敏感的模块。

敏感度探测：

```text
model:                       HuggingFaceTB/SmolLM2-360M-Instruct
probe prompts:               4
max length:                  128
group size:                  128
Linear modules:              225
loss-sensitive allocation:   4-bit=172, 8-bit=53
weighted average bits:       4.4993
positive loss protected:     57.83%
```

8-prompt PPL 评估，max length 160，group size 128：

| method | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---|
| FP16 | 179.14 | 0.0000 | 16:225 |
| uniform INT4 | 272.18 | 0.4183 | 4:225 |
| activation-stat RD 4/8 | 292.01 | 0.4886 | 4:172, 8:53 |
| loss-sensitive 4/8 | 212.69 | 0.1717 | 4:172, 8:53 |

这说明旧的 activation-stat RD proxy 在 group-wise quantization 下失败，但
measured per-module loss sensitivity 能显著优于 uniform INT4 和旧 RD 分配。
它仍然只是 fake quant 诊断，不能声称真实显存、延迟或能耗下降。

公共数据集补充，WikiText2 validation 32 prompts：

| method | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---|
| FP16 | 18.24 | 0.0000 | 16:225 |
| uniform INT4 | 30.26 | 0.5062 | 4:225 |
| uniform INT3 | 1678.70 | 4.5221 | 3:225 |
| activation-stat RD 4/8 | 26.13 | 0.3593 | 4:172, 8:53 |
| loss-sensitive 4/8 | 25.92 | 0.3514 | 4:172, 8:53 |

这给论文主线补上了比手写 prompt 更可信的公共文本切片证据。

扩大到 WikiText2 validation 128 prompts 后：

| method | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---|
| FP16 | 17.34 | 0.0000 | 16:225 |
| uniform INT4 | 27.82 | 0.4727 | 4:225 |
| uniform INT3 | 1154.44 | 4.1981 | 3:225 |
| activation-stat RD 4/8 | 24.51 | 0.3459 | 4:172, 8:53 |
| loss-sensitive 4/8 | 24.14 | 0.3305 | 4:172, 8:53 |
| loss-sensitive exact knapsack 4/8 | 24.36 | 0.3396 | 4:175, 8:50 |

128 prompt 结果保持同样排序：loss-sensitive 优于 uniform INT4，也略优于
activation-stat RD。

新增 exact knapsack 检查后，局部 one-module sensitivity 目标的精确最优不等于
全局 PPL 最优：exact knapsack 保护更多局部 loss，但 PPL 略差于 greedy。这为
后续 Fisher/Hessian/interaction-aware/RL allocation 提供了更强问题动机。

新增证据文件：

```text
train_python/measure_module_quant_sensitivity.py
train_python/build_dataset_prompts.py
train_python/build_loss_sensitive_knapsack_alloc.py
data_eval/eval_configs/smollm2_group128_compare_allocations.json
data_eval/text_prompts/wikitext2_validation_32.txt
data_eval/text_prompts/wikitext2_validation_128.txt
outputs/EigenSkill-Q-Loss-Sensitive-Allocation-Update-2026-06-04.md
outputs/paper_delivery_2026-06-04/EigenSkill-Q_CCF-A_Draft_v2_Loss_Sensitive.md
outputs/smollm2_module_loss_sensitivity_limit4_group128.json
outputs/smollm2_module_loss_sensitivity_limit4_group128_report.md
outputs/smollm2_loss_sensitive_alloc_4to8_limit4_group128_summary.json
outputs/smollm2_fake_quant_ppl_loss_sensitive_4to8_group128_limit8_summary.json
outputs/smollm2_fake_quant_ppl_loss_sensitive_4to8_group128_wikitext2_32_summary.json
outputs/smollm2_fake_quant_ppl_activation_rd_4to8_group128_wikitext2_32_summary.json
outputs/smollm2_fake_quant_ppl_compare_allocations_group128_wikitext2_128_summary.json
outputs/smollm2_fake_quant_ppl_compare_allocations_exact_group128_wikitext2_128_summary.json
```

## 2026-06-04 追加：interaction-aware swap-search

在 greedy loss-sensitive allocation 之后，新增了一个 bounded one-step
policy-improvement 搜索。它生成少量预算不变的 4/8-bit swap 候选，并用全局
WikiText2-128 PPL 反馈选择最优交换。

结果：

```text
base allocation: loss-sensitive 4/8
evaluated swaps: 8
base PPL:        24.1374
best PPL:        24.0661
demote:          model.layers.17.self_attn.v_proj
promote:         model.layers.24.self_attn.v_proj
bit histogram:   4-bit=172, 8-bit=53
```

统一 WikiText2-128 表：

| method | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---|
| FP16 | 17.34 | 0.0000 | 16:225 |
| uniform INT4 | 27.82 | 0.4727 | 4:225 |
| uniform INT3 | 1154.44 | 4.1981 | 3:225 |
| activation-stat RD 4/8 | 24.51 | 0.3459 | 4:172, 8:53 |
| loss-sensitive greedy 4/8 | 24.14 | 0.3305 | 4:172, 8:53 |
| loss-sensitive exact knapsack 4/8 | 24.36 | 0.3396 | 4:175, 8:50 |
| loss-sensitive swap-search 4/8 | 24.07 | 0.3276 | 4:172, 8:53 |

含义：局部 one-module sensitivity 是有效特征，但不是完整目标。exact
knapsack 和 swap-search 一起说明全局 PPL 中存在模块交互项，后续主线应转向
interaction-aware allocation、pairwise surrogate、learned reward model 和
constrained contextual bandit/RL。

## 2026-06-04 追加：C4 validation 小切片

新增 `build_dataset_prompts.py --streaming`，避免 C4 validation 全量下载 1024
个 shard。当前只用 streaming 扫描 66 行，构建 64 条 C4 English validation
prompts。

| method | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---|
| FP16 | 23.78 | 0.0000 | 16:225 |
| uniform INT4 | 36.94 | 0.4403 | 4:225 |
| uniform INT3 | 2990.80 | 4.8344 | 3:225 |
| activation-stat RD 4/8 | 33.69 | 0.3484 | 4:172, 8:53 |
| loss-sensitive greedy 4/8 | 32.77 | 0.3205 | 4:172, 8:53 |
| loss-sensitive exact knapsack 4/8 | 32.87 | 0.3235 | 4:175, 8:50 |
| loss-sensitive swap-search 4/8 | 32.57 | 0.3146 | 4:172, 8:53 |

含义：C4 复现 WikiText2 排序，说明 positive trend 不是单一验证切片偶然现象。

新增证据：

```text
train_python/search_allocation_swaps.py
train_python/build_dataset_prompts.py
data_eval/text_prompts/c4_en_validation_64.txt
outputs/smollm2_allocation_swap_search_group128_wikitext2_128_summary.json
outputs/smollm2_allocation_swap_search_group128_wikitext2_128_report.md
outputs/smollm2_loss_sensitive_swap_search_alloc_4to8_group128_summary.json
outputs/smollm2_fake_quant_ppl_compare_allocations_swap_group128_wikitext2_128_summary.json
outputs/smollm2_fake_quant_ppl_c4_validation_64_report.md
outputs/smollm2_fake_quant_ppl_compare_allocations_swap_group128_c4_en_validation_64_summary.json
```

## 数学主线

把量化策略写成约束优化：

```text
minimize    sum_l D_l(W_l, A_l, Q_l) + alpha C_l(b_l, R_l, o_l, r_l, k_l)
subject to  sum_l M_l(b_l, k_l) <= B
            sum_l T_l(b_l, R_l, r_l, k_l) <= T
            Risk_l(o_l, b_l, k_l) <= epsilon_l
```

在线版本写成 constrained contextual bandit：

```text
maximize    E[Reward(x_t, a_t)]
subject to  E[Memory(x_t, a_t)] <= B
            E[Latency(x_t, a_t)] <= T
            P(QualityDrop(x_t, a_t) > delta) <= eta
```

## 候选 CCF-A 路线

避开 NeurIPS / MLSys 后，建议按证据强度选择：

- ICML：数学、rate-distortion、bandit/RL 足够强时；
- IJCAI / AAAI：AI policy learning + 真实量化实验；
- ACL：可靠工具执行 / structured generation / LLM serving；
- AI / TPAMI / JMLR：期刊路线，需要完整理论和更强实验。

TNNLS 在 CCF AI 官方页列为 B，不建议作为“CCF-A”主推，除非学校另有名单。

## 不能声称

- 不能声称已完成真正 Transformer `O(d)` eigen-routing；
- 不能声称已超过 GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant/QuIP/AQLM；
- 不能声称已有真实 edge/NPU/ARM 能耗或延迟结果；
- 不能把 swarm/acoustic/physical assembly 写成已实现贡献。

## 下一步

1. 真实模型：Qwen2.5-0.5B/1.5B、Llama-3.2-1B/3B、SmolLM2-1.7B。
2. 真实量化：RTN、GPTQ、AWQ、SmoothQuant、QuaRot/SpinQuant。
3. 策略实验：heuristic、deterministic C++、learned bandit/RL。
4. 交互建模：one-step swap、beam search、pairwise surrogate、learned reward。
5. 指标：PPL、task accuracy、memory、latency、policy overhead、router failure。

## 参考链接

- CCF AI 推荐目录：https://www.ccf.org.cn/Academic_Evaluation/AI/
- GPTQ：https://arxiv.org/abs/2210.17323
- AWQ：https://arxiv.org/abs/2306.00978
- SmoothQuant：https://arxiv.org/abs/2211.10438
- QuaRot：https://arxiv.org/abs/2404.00456
- SpinQuant：https://arxiv.org/abs/2405.16406
- QuIP#：https://arxiv.org/abs/2402.04396
- OmniQuant：https://arxiv.org/abs/2308.13137
- AQLM：https://arxiv.org/abs/2401.06118
- KIVI：https://arxiv.org/abs/2402.02750
- KVQuant：https://arxiv.org/abs/2401.18079
