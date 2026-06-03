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
outputs/paper_delivery_2026-06-04/导师速览.md
outputs/paper_delivery_2026-06-04/authorization-and-channel-audit.md
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
4. 指标：PPL、task accuracy、memory、latency、policy overhead、router failure。

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
