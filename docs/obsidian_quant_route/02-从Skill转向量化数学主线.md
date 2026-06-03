# 从 Skill 转向量化数学主线

日期：2026-06-03

## 为什么原 skill 路线不够

原 8 个 skill：

```text
intent_routing
json_repair
field_extraction
command_normalization
sensor_event_triage
packet_encode
safety_gate
unit_time_normalize
```

问题不只是数量少，而是它们和“模型量化”之间的学术耦合太弱：

1. 它们是低熵模板任务，很容易被规则或小模型记忆解决。
2. 它们不触及 LLM 量化的核心难点：outlier、Hessian 敏感度、activation distribution shift、KV cache 长上下文误差、低比特整数/浮点格式误差。
3. 它们的效果提升主要来自 deterministic parser，不是模型参数压缩或数学量化设计。
4. 很难说服国际期刊审稿人：为什么这个 skill set 能代表 LLM quantization 的普遍问题。

因此，skill 应该从“业务功能 skill”改成“量化决策 skill”。

## 新主线名称候选

### 方向 A：Spectral-Aware Mixed-Precision Quantization

中文：谱敏感混合精度量化。

核心问题：给定每层权重 $W_l$、激活协方差 $C_l = E[x_l x_l^T]$ 和 Hessian 近似 $H_l$，如何分配每层/每通道/每组 bit-width，使总误差在显存预算下最小？

目标函数：

```text
min_{b_l, Q_l, R_l}  Σ_l  E[ || (Q_{b_l}(R_l W_l) - R_l W_l) x_l ||_2^2 ]
s.t.                 Σ_l cost(b_l) <= B
                     R_l^T R_l = I
```

更精细可写成 Hessian 加权：

```text
ΔL ≈ 1/2 Σ_l vec(ΔW_l)^T H_l vec(ΔW_l)
```

其中：

```text
ΔW_l = R_l^T Q_b(R_l W_l) - W_l
```

这能连接 GPTQ 的二阶误差思想、AWQ 的 activation-aware 思想、QuaRot/SpinQuant 的旋转思想。

### 方向 B：Outlier Redistribution via Learnable Orthogonal Rotations

中文：可学习正交旋转的异常值重分布量化。

核心思想：量化损失大的根源不是均方误差本身，而是权重/激活/KV cache 中存在方向性 outlier。通过正交旋转 $R$ 保持函数不变或近似不变，同时让通道分布更均匀：

```text
x' = R x
W' = W R^T
W x = W' x'
```

如果 $R$ 设计得好，量化器面对的是更均匀、更低峰度的分布。

可优化目标：

```text
min_R  α · kurtosis(RX) + β · max_channel_energy(RX) + γ · QError(RW, RX)
s.t.   R^T R = I
```

可选约束：使用 Hadamard/Givens/Householder 结构降低旋转计算成本。

### 方向 C：Sensitivity-Guided Quantization Skill Router

中文：敏感度引导的量化技能路由。

这里保留 EigenSkill 的名字，但 skill 不再是“开灯/JSON 修复”，而是量化流程里的专家模块：

| Quant Skill | 输入 | 输出 | 数学作用 |
| --- | --- | --- | --- |
| outlier_detect | activation/weight statistics | outlier channels/groups | 找出量化高风险方向 |
| hessian_probe | calibration batch | layer sensitivity score | 近似二阶损失 |
| rotation_select | covariance + outlier map | rotation family / rank | 选择旋转策略 |
| bit_allocate | sensitivity + memory budget | bit-width per layer/group | 解 constrained optimization |
| kv_policy | context length + K/V stats | KV bit policy | 长上下文 cache 压缩 |
| residual_patch | quant error residual | low-rank correction | 低秩补偿量化误差 |

这才是和 AI 模型量化强相关的 EigenSkill。

## 推荐主贡献表述

不要写：

> 我们训练 skill token，使某些矩阵乘法从 O(d^2) 变成 O(d)。

更稳妥地写：

> We formulate LLM post-training quantization as a sensitivity-aware routing problem over layers, channels, and activation subspaces. EigenSkill learns or estimates compact quantization skills, including outlier redistribution, orthogonal rotation selection, and mixed-precision bit allocation, to minimize Hessian/activation-weighted distortion under memory and bandwidth constraints.

## 与主流工作的关系

- GPTQ：二阶/Hessian 近似误差补偿，是数学基础线。
- SmoothQuant：把 activation outlier 平滑迁移到 weight，是 outlier redistribution 基础线。
- AWQ：activation-aware 保护重要权重，是 sensitivity-aware 基础线。
- OmniQuant：学习量化参数，是 calibration optimization 基础线。
- QuaRot：通过旋转去除 hidden-state outlier，是 orthogonal invariance 基础线。
- SpinQuant：学习旋转矩阵，是 learnable rotation 基础线。
- KIVI/KVQuant：KV cache 量化，是长上下文内存瓶颈基础线。

## 更适合期刊的数学创新点

1. **统一目标函数**：把权重量化、激活量化、KV cache 量化写成统一的加权失真最小化问题。
2. **可证明误差界**：给出旋转后量化误差关于 covariance eigenvalue、outlier kurtosis、bit-width 的上界。
3. **混合精度分配算法**：用 Lagrangian / knapsack / differentiable relaxation 做 bit allocation。
4. **低秩残差补偿**：对最敏感层保留低秩 residual adapter，而不是全层高精度。
5. **硬件成本项**：目标函数加入 bandwidth、cache line、SIMD/NPU tile 约束，使数学与系统相连。

## 关键公式草案

### 量化失真

```text
D_l(b, R) = E_x || (Q_b(W_l R^T) - W_l R^T) R x ||_2^2
```

若 $C_l = E[x x^T]$，则：

```text
D_l(b, R) = tr( ΔW_l(R,b) R C_l R^T ΔW_l(R,b)^T )
```

### Hessian 加权损失

```text
ΔL_l ≈ 1/2 vec(ΔW_l)^T H_l vec(ΔW_l)
```

### 混合精度位宽分配

```text
min_{b_l ∈ {2,3,4,8}} Σ_l S_l · ε_l(b_l)
s.t.                  Σ_l n_l b_l <= B
```

其中 $S_l$ 是层敏感度，可由 Hessian trace、activation norm、outlier ratio 或 perplexity drop 估计。

### 低秩补偿

```text
W_l ≈ Q_b(W_l) + A_l B_l^T
rank(A_l B_l^T) = r << d
```

优化：

```text
min_{A,B} E_x || (W_l - Q_b(W_l) - A B^T)x ||_2^2
```

这比原来的 eigen-skill 线性旁路更容易落地，也更容易被期刊接受。

## 下一批 skill/任务应该怎么选

不要再选家居命令/JSON 修复作为主任务。应选择能暴露量化误差的问题：

1. long-context retrieval：KV cache 量化最敏感。
2. arithmetic and symbolic reasoning：低比特误差容易放大。
3. code generation：对 logits 排序和细节敏感。
4. multi-step tool planning：中间状态错误会级联。
5. mathematical QA：适合观察量化后推理退化。
6. calibration transfer：用少量校准数据泛化到未见任务。
7. adversarial outlier prompts：诱发 activation outliers。
8. multilingual mixed scripts：中文/英文/符号混合，测试 tokenizer 和激活分布变化。

最终 skill 应该是“量化场景/误差模式 skill”，不是“业务动作 skill”。
