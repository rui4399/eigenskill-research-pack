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

## 2026-06-04 追加：output reconstruction proxy 负结果

新增 `measure_module_output_sensitivity.py`，对每个 Linear 模块采样输入 `x`，
测量 group-wise INT4 后的局部输出扰动：

```text
E ||x(W - Q(W))^T||^2 / E ||xW^T||^2
```

结果：

```text
Linear modules:              225
sample rows per module:      128
output-sensitive allocation: 4-bit=135, 8-bit=90
protected output proxy:      54.50%
```

PPL：

| dataset | output-sensitive PPL | loss-sensitive PPL | swap-search PPL |
|---|---:|---:|---:|
| WikiText2-128 | 25.21 | 24.14 | 24.07 |
| C4-64 | 33.71 | 32.77 | 32.57 |

含义：output reconstruction proxy 优于 uniform INT4，但弱于 measured
loss-sensitive，也没有超过 activation-stat RD。这个负结果很关键：局部输出重构
误差不能直接替代全局 next-token loss，论文应强调 loss-aware 和
interaction-aware allocation。

新增证据：

```text
train_python/search_allocation_swaps.py
train_python/build_dataset_prompts.py
train_python/measure_module_output_sensitivity.py
data_eval/text_prompts/c4_en_validation_64.txt
outputs/smollm2_allocation_swap_search_group128_wikitext2_128_summary.json
outputs/smollm2_allocation_swap_search_group128_wikitext2_128_report.md
outputs/smollm2_loss_sensitive_swap_search_alloc_4to8_group128_summary.json
outputs/smollm2_fake_quant_ppl_compare_allocations_swap_group128_wikitext2_128_summary.json
outputs/smollm2_fake_quant_ppl_c4_validation_64_report.md
outputs/smollm2_fake_quant_ppl_compare_allocations_swap_group128_c4_en_validation_64_summary.json
outputs/smollm2_output_sensitivity_proxy_report.md
outputs/smollm2_module_output_sensitivity_limit4_group128.json
outputs/smollm2_output_sensitive_alloc_4to8_limit4_group128_summary.json
outputs/smollm2_fake_quant_ppl_compare_allocations_with_output_proxy_group128_wikitext2_128_summary.json
outputs/smollm2_fake_quant_ppl_compare_allocations_with_output_proxy_group128_c4_en_validation_64_summary.json
```

## 2026-06-04 深夜增补：Qwen2.5-1.5B 与 C++ low-bit kernel

本轮把实验从 SmolLM2-360M 推进到本地缓存的
`Qwen2.5-1.5B-Instruct`。模型权重不进入仓库，只记录路径、哈希和评估输出。

```text
local model path:        C:\Users\18042\models\Qwen2.5-1.5B-Instruct
WSL model path:          /mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct
model.safetensors bytes: 3,087,467,144
sha256:                  DD924A11B4C220F385B51FFA522DAEA7C9F3D850E31B162BB5661DF483C6D3EE
Linear modules:          197
group size:              128
```

### 1. 2p / 8p / consensus 分配

使用 measured per-module loss sensitivity 构造 `{4,8}` 混合精度分配：

| allocation | 4-bit | 8-bit | avg bits | protected positive delta |
|---|---:|---:|---:|---:|
| 2-prompt loss-sensitive | 137 | 60 | 4.4993 | 60.20% |
| 8-prompt loss-sensitive | 136 | 61 | 4.4953 | 54.45% |
| 2p/8p consensus | 132 | 65 | 4.4993 | 53.81% |

2p 与 8p 的 8-bit 模块 Jaccard 为 `0.6351`。这说明分配不是完全稳定，但也不是随机漂移；更长校准会改变 27/197 个 bit decision。

### 2. Qwen2.5-1.5B fake-quant PPL

64-prompt 双数据集结果：

| dataset | FP16 | uniform INT4 | uniform INT3 | 2p loss-sensitive | 8p loss-sensitive | consensus |
|---|---:|---:|---:|---:|---:|---:|
| WikiText2-64 | 12.8516 | 17.2441 | 273.9454 | 16.1788 | 15.7520 | 15.7966 |
| C4-64 | 18.1669 | 23.9949 | 293.8201 | 23.2682 | 22.3620 | 22.4891 |

更长 WikiText2-128 结果：

| dataset | FP16 | uniform INT4 | uniform INT3 | 2p loss-sensitive | 8p loss-sensitive | consensus |
|---|---:|---:|---:|---:|---:|---:|
| WikiText2-128 | 13.1290 | 17.4996 | 232.6215 | 16.6503 | 16.0781 | 16.1356 |

结论：在 Qwen2.5-1.5B 上，8-prompt loss-sensitive allocation 在 WikiText2-64、C4-64 和 WikiText2-128 上都优于 uniform INT4，也优于 2-prompt allocation。Consensus 更稳定，但在当前切片中略逊于直接 8p 分配。

限制：这仍是 fake weight quantization quality diagnostic，不是 packed INT4/INT3 runtime，也不代表显存、延迟或能耗收益。

### 3. C++ low-bit kernel 更新

C++ 侧新增通用 row-scaled signed low-bit API：

```text
PackedLowBitMatrix
PackedMixedBitMatrix
pack_lowbit_per_row(bits=2..8)
pack_mixed_lowbit_per_row(row_bits=2..8)
unpack_signed_bits
lowbit_dequant_gemv
mixed_lowbit_dequant_gemv
mixed_lowbit_selected_rows_gemv
```

旧的 `PackedInt4Matrix / pack_int4_per_row / int4_dequant_gemv` 保持兼容，并基于通用 low-bit 路径实现。`quant_kernel_verify` 现在同时检查 INT4 和 INT3 输出有限、AVX2 dense GEMV、selected-row GEMV、scalar bypass。

WSL/g++ 11.4 验证：

```text
cmake --build build/cpp-wsl -j2: passed
ctest --test-dir build/cpp-wsl: passed
quant_kernel_verify --dim 256 --active-rows 16: ok=true
```

benchmark smoke：

```text
d=256 rows=16
dense_ms=0.033150
davx_ms=0.003075
int4_ms=0.197147
int3_ms=0.167296
selected_avx2_ms=0.000231
scalar_ms=0.000019
```

解释：当前 scalar bit-unpack INT3/INT4 GEMV 慢于 AVX2 FP32 dense GEMV。这是有价值的负结果：低比特存储格式本身不等于速度收益，后续需要 vectorized unpack、low-bit dot product、NEON/AVX2 专门路径或直接接入成熟 runtime。

2026-06-04 追加 mixed-bit benchmark：

```text
d=2048, active_rows=16
dense_ms=2.554907
mixed_full_dequant_ms=11.888089
mixed_selected_ms=0.145753
mixed_selected speedup vs scalar dense=17.53x
mixed_selected rel_l2 vs mixed full output rows=0.0
mixed selected-row faster than dense: 7/9 cases
full mixed-bit dequant faster than dense: 0/9 cases
```

解释：这支持“mixed-bit representation + selected-row bypass”的系统闭环，但仍不支持“低比特完整 GEMV 更快”的说法。

### 4. GPU 资源边界

本机 GPU：NVIDIA GeForce RTX 5070 Laptop GPU，约 8.15 GiB 显存。

Qwen2.5-1.5B 的 WikiText2-128 `--reuse-model` 评估过程中曾短时达到：

```text
memory used: 7296 MiB / 8151 MiB
```

这约等于 89.5%，超过预设的 85% 上限。因此后续不宜继续扩大 1.5B 单进程多配置评估；更大切片应拆分 config、降低并行驻留、或改用更省显存的评估路径。

已新增 GPU guard 与低峰值 fake quant：

```text
train_python/run_with_gpu_guard.py
eval_weight_quant_ppl.py: in-place group-wise fake quantization
```

修复前，1.5B 五配置 baseline 对比被 guard 终止，采样峰值为 `7643/8151 MiB`。
修复后，同一 16-prompt Qwen2.5-1.5B baseline 对比成功完成：

```text
peak GPU memory: 4634 / 8151 MiB = 56.85%
max GPU utilization: 62%
guard killed: false
```

16-prompt WikiText2 budget baseline：

| method | PPL | mean NLL delta vs FP16 | avg bits |
|---|---:|---:|---:|
| FP16 | 10.76298 | 0.00000 | 16.0000 |
| uniform INT4 | 15.04498 | 0.33493 | 4.0000 |
| loss-sensitive {4,8} | 13.13882 | 0.19946 | 4.4953 |
| random budget-matched {4,8} | 14.18543 | 0.27610 | 4.4952 |
| category heuristic budget | 14.43989 | 0.29388 | 4.4709 |

64-prompt WikiText2 budget baseline：

| method | PPL | mean NLL delta vs FP16 | avg bits |
|---|---:|---:|---:|
| FP16 | 12.28746 | 0.00000 | 16.0000 |
| uniform INT4 | 16.41184 | 0.28942 | 4.0000 |
| loss-sensitive {4,8} | 14.98599 | 0.19854 | 4.4953 |
| random budget-matched {4,8} | 15.69645 | 0.24486 | 4.4952 |
| category heuristic budget | 15.72164 | 0.24646 | 4.4709 |

解释：loss-sensitive 在这两个短切片上不只优于 uniform INT4，也优于预算匹配的 random/heuristic mixed precision baseline。限制：这仍是 sanity slice，不能替代完整基准。

### 5. 最新 GitHub 提交

```text
13d9df8 Add Qwen2.5 1.5B WikiText2-128 evidence
8ab5f83 Add Qwen2.5 1.5B 64-prompt PPL evidence
9401a21 Add generic low-bit C++ quant kernels
126ddd6 Add Qwen2.5 1.5B calibration stability evidence
```

主要新增证据：

```text
data_eval/eval_configs/qwen25_1p5b_group128_compare_2p8p_consensus.json
outputs/qwen25_1p5b_loss_sensitive_compare_2p8p_consensus_ppl64_table.md
outputs/qwen25_1p5b_loss_sensitive_compare_2p8p_consensus_wikitext2_128_table.md
outputs/qwen25_1p5b_loss_sensitive_2p_vs_8p_stability_report.md
outputs/qwen25_1p5b_sensitivity_limit8_compact_summary.md
inference_cpp/include/eigenskill/quant_kernels.hpp
inference_cpp/src/quant_kernels.cpp
inference_cpp/src/quant_kernel_bench.cpp
inference_cpp/src/quant_kernel_verify.cpp
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
