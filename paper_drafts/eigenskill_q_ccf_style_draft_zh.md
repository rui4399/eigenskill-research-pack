# EigenSkill-Q：面向受限推理的跨数据集一致性敏感度混合精度量化诊断

> CCF 风格论文初稿，2026-06-05。本文按正式学术论文结构组织，写法参考经典系统/模型论文的“问题清晰化、方法简洁化、实验证据驱动”范式，但不复用其原文表述。当前稿件是技术报告级草案，尚未满足正式投稿所需的完整基线、硬件与统计显著性要求。
>
> 状态更新，2026-06-07：本中文稿保留为中文读者版/历史草稿，不是当前投稿主稿。当前更接近投稿骨架的版本是 `paper_drafts/eigenskill_q_research_draft_en_2026_06_07.md`，它已纳入 33-gate evidence ledger、calibration robustness stress、sensitivity perturbation matrix、calibration seed stability、CSI-vs-n calibration-size curve、consensus transfer boundary、interaction-aware swap boundary、public-task model ladder、official PTQ task-execution smoke、official PTQ matched subset50/runtime profile、official PTQ deterministic IFEval-style execution/runtime profile、official PTQ matched baseline pack、AutoAWQ/GPTQModel aligned 16-prompt public PPL gates、official PTQ readiness matrix 和 paper-evidence alignment gate。若两者不一致，以新版英文稿和 `docs/PAPER_CLAIM_MATRIX.md` 为准。

## 摘要

大语言模型在资源受限环境中的部署受到显存、访存带宽和推理路径共同限制。后训练量化是降低成本的重要路径，但统一低比特量化往往在关键模块引入过大误差，而混合精度分配又依赖少量校准样本估计模块敏感度，容易受到校准分割噪声影响。本文将问题收敛为：在很小校准预算下，模块敏感度排序到底有多不稳定，以及跨分割一致性是否能降低错误位宽分配的风险。EigenSkill-Q 当前是一份可复现实验工件，而不是生产级量化器。它分别在 WikiText2/C4 等校准视图上估计线性模块的低比特损失增量，在固定平均位宽预算下构建 consensus allocation，并通过 claim matrix 与 evidence ledger 约束每一条可公开声明。当前英文主稿对应 30 个通过的 evidence gates，覆盖校准不稳定性、prompt-seed 稳定性、随机基线压力、跨分割迁移、交互式 swap 边界、Q-Palette 风格拉格朗日分配代理、AutoAWQ/GPTQModel Qwen2.5-0.5B W4/G128 对齐 16-prompt public PPL readiness，以及 PC 侧 subset50 runtime/VRAM 负结果。实验表明，跨数据集一致性能够把“有用但不稳定”的敏感度信号转化为更稳健的短切片 fake-quant 分配依据；同时，官方 PTQ readiness 结果只说明本地基线包可执行，并不支持 SOTA、生产 runtime、移动端部署或端到端加速声明。

**关键词**：大语言模型；后训练量化；混合精度；校准稳定性；模型压缩；C++ 审计工具

## 1 引言

大语言模型的推理成本主要由权重存储、激活访存、矩阵乘法和 KV cache 维护共同决定。对于边缘端或单卡本地环境，模型能否运行并不只取决于参数规模，还取决于低比特表示是否能在质量、显存和计算路径之间取得稳定平衡。统一 INT4 或更低比特量化可以显著降低权重存储，但不同层、不同投影矩阵和不同 MLP 分支对量化误差的容忍度并不一致。将所有模块压到同一精度通常会让少数关键模块成为主要质量瓶颈。

混合精度量化试图解决这一问题。其基本思路是把有限的高精度预算分配给更敏感的模块，其他模块保留低精度。问题在于，敏感度并不是一个直接可观测的固定常数。真实部署时关心的是目标分布上的损失或任务质量，而训练外的后训练量化只能依赖少量校准文本进行估计。当校准样本很少时，单个分割得到的模块排序可能具有明显噪声。本文将这一现象称为**校准退化问题**：位宽分配不是因为预算本身不足而退化，而是因为预算被不稳定的敏感度排序引导到错误模块上。

这种问题在短周期研究中尤为明显。我们在早期 Qwen3-0.6B 实验中观察到：一个 4-prompt WikiText2 校准探针得到的 loss-sensitive 分配能显著优于 uniform INT4，也优于随机种子的平均水平，但在 WikiText2-64 len96 评估中仍输给 15 个随机同预算分配里的最佳种子。这一结果说明，单分割敏感度并非完全无效，却不足以支撑“稳定优于随机”的学术结论。如果隐藏这一负结果，方法看似更强，实则不可复现风险更高。

本文提出的 EigenSkill-Q 将研究问题收敛到一个可检验命题：在固定平均比特预算下，跨数据集一致性是否能提高敏感度引导混合精度分配的稳健性。具体地，我们在 WikiText2 与 C4 上分别估计每个线性模块被量化到 INT4 后的短文本 NLL 增量，先锁定两个分割共同选择的高精度模块，再用平均损失增量除以模块参数量形成的 score/cost 排序填充剩余预算。该策略保留了敏感度方法的可解释性，同时避免完全依赖单一校准分布。

本文贡献如下。

1. 提出并明确化了短校准混合精度量化中的校准分割噪声问题，保留单分割输给最佳随机分配的负结果作为方法动机。
2. 给出一种简单的跨数据集一致性位宽分配方法，在固定 4.5 average-bit 的 `{4,8}` 预算下优先保护稳定敏感模块。
3. 构建 C++ 分配、审计和汇总工具，覆盖 consensus allocation builder、random baseline audit、evidence matrix、split-stability audit、budget-curve summary 和 GPU guard summary。
4. 在 Qwen3-0.6B、Qwen3-1.7B、OLMo2-0425-1B-Instruct 与 SmolLM2-1.7B 的短切片 fake-quant 诊断中验证该路径，并保留 robust-LCB、swap search 等边界结果。
5. 将 AutoAWQ/GPTQModel 的 Qwen2.5-0.5B W4/G128 readiness 证据放入独立 claim boundary：它们用于补齐官方包可执行性与 PPL/任务/PC-runtime 观测，不用于宣称相对强基线的优势。

## 2 相关工作

**深层模型中的结构性绕路。** ResNet 通过残差映射缓解深层网络优化退化问题，提供了一个重要研究范式：先找到阻碍规模化的退化现象，再设计尽可能简单、可堆叠、可验证的结构修复。本文并不研究视觉残差结构，但借鉴这种论证方式，把量化中的问题从“低比特不够好”细化为“少样本敏感度排序不稳定”，再用一致性分配进行针对性修复。

**大语言模型后训练量化。** LLM.int8() 通过混合精度处理大模型中的离群特征，说明低比特路径必须关注异常通道和局部敏感性。GPTQ 使用近似二阶信息进行逐层权重量化，是 LLM PTQ 的代表性方法。SmoothQuant 通过平滑权重与激活之间的尺度难题支持 W8A8 推理。AWQ 进一步强调激活感知的权重量化保护。QuaRot 与 SpinQuant 等旋转方法则通过正交变换降低离群值对低比特表示的破坏。本文当前没有实现这些生产级基线，因此不与其竞争 SOTA，而是聚焦混合精度分配中的校准稳定性诊断。

**混合精度与敏感度分配。** 早期混合精度量化方法常用 Hessian、梯度或验证损失估计层级敏感度，再在给定 bit budget 下求解分配问题。本文采用更轻量的模块替换式 fake-quant 探针：每次只将一个线性模块替换为 INT4 fake quant 权重，记录短校准文本上的 NLL 增量。该方法计算代价高于纯统计启发式，但实现简单、解释直接，适合作为短周期研究基线。

**系统化可复现工具。** 量化论文常见问题是实验逻辑留在 Python glue code 中，审稿人难以区分方法、报告和偶然脚本状态。本文把分配构建、审计和结果汇总拆成独立 C++ 可执行工具。其目的不是宣称 C++ runtime 已经完成，而是把可复现实验的关键元数据路径固定下来，为后续 packed kernel 和硬件实验打基础。

## 3 方法

### 3.1 问题定义

设预训练语言模型包含一组待量化线性模块：

```text
M = {1, 2, ..., n}
```

第 `i` 个模块权重为 `W_i`，参数量或存储成本记为 `c_i`。给定位宽集合 `{4,8}` 和平均位宽预算 `B=4.5`，我们需要决定每个模块的位宽：

```text
b_i in {4, 8}
sum_i c_i b_i <= B * sum_i c_i
```

目标是在预算约束下尽可能减少量化后的语言建模损失。由于完整搜索不可行，本文用校准数据上的模块敏感度估计进行近似。

### 3.2 单分割模块敏感度

给定校准数据集 `D`，基座模型在 `D` 上的平均负对数似然为：

```text
L(W; D)
```

将第 `i` 个模块临时替换为 INT4 fake quant 权重 `Q4(W_i)`，其余模块保持原精度，得到：

```text
L(W_{-i}, Q4(W_i); D)
```

模块的正向损失增量定义为：

```text
delta_i(D) = max(L(W_{-i}, Q4(W_i); D) - L(W; D), 0)
```

为了在不同参数量模块之间比较保护收益，定义单位成本分数：

```text
r_i(D) = delta_i(D) / c_i
```

单分割 loss-sensitive 分配等价于在固定预算下按 `r_i(D)` 降序选择模块升至 8-bit。该方法简单，但当 `D` 很小时，`r_i(D)` 的排序可能不稳定。

### 3.3 跨数据集一致性分配

本文使用两个校准分布：

```text
D_left  = WikiText2 calibration prompts
D_right = C4 calibration prompts
```

先分别生成两个单分割高精度集合：

```text
H_left, H_right
```

一致性分配包含两步。

第一步，优先锁定交集模块：

```text
I = H_left ∩ H_right
```

如果交集模块在预算内，则全部置为 8-bit。若预算不足，则按平均 score/cost 截断。

第二步，用平均敏感度填充剩余预算：

```text
r_i^cons = 0.5 * (delta_i(D_left) + delta_i(D_right)) / c_i
```

对尚未选择的模块按 `r_i^cons` 降序加入 8-bit 集合，直到达到预算。其余模块保持 4-bit。

该方法可视为一个保守的鲁棒目标近似：如果一个模块只在单一分割上表现敏感，它可能是分布噪声；如果它在两个分割上共同敏感，或平均损失/成本显著较高，则更可能值得保护。

### 3.4 C++ 审计工具

EigenSkill-Q 当前实现中，模型加载和 fake quant PPL 评估仍由 Python/PyTorch 完成。为了降低报告路径中的脚本偶然性，本文实现了以下 C++ 工具：

| 工具 | 作用 |
|---|---|
| `quant_consensus_builder` | 从两个 sensitivity JSON 构建 consensus allocation |
| `quant_random_baseline_audit` | 统计目标分配相对 `random_seed_*` 的 win/loss/tie 与边际 |
| `quant_evidence_matrix` | 合并多个 PPL summary 为跨数据集证据表 |
| `quant_sensitivity_stability` | 分析两个校准分割之间的 Jaccard、Spearman、Kendall 等稳定性 |
| `quant_budget_curve_summary` | 汇总不同平均位宽预算下的质量曲线 |
| `gpu_guard_summary` | 汇总受控 GPU 运行的显存峰值、利用率与 guard 状态 |

这些工具的设计目标是可审计性，而不是替代真实量化 runtime。它们保证论文表格可以由提交的 JSON 产物重新生成。

## 4 实验设计

### 4.1 模型与数据

当前质量诊断主要覆盖以下模型：

| 模型 | 角色 |
|---|---|
| Qwen/Qwen3-0.6B | 最新补充的轻量模型，验证 consensus 是否修复单分割失败 |
| Qwen/Qwen3-1.7B | 更强 Qwen3 家族模型，已有 consensus 与 budget curve |
| allenai/OLMo-2-0425-1B-Instruct | 非 Qwen 家族模型，用于检查方法是否只依赖单一架构 |
| HuggingFaceTB/SmolLM2-1.7B-Instruct | interaction-aware swap boundary 与局部/全局分配反例 |

评估数据为 WikiText2 与 C4 的公开文本短切片。本文报告的主要 PPL 来自 PyTorch fake quant 诊断，不代表 packed INT4 runtime 的真实延迟或显存收益。

官方 PTQ readiness 另行覆盖 `Qwen/Qwen2.5-0.5B-Instruct` 上的 AutoAWQ 与 GPTQModel W4/G128 本地包。该部分用于说明公开校准、加载、短 PPL、subset50 任务执行和 PC 侧 runtime/VRAM 路径已经接通；它仍不是完整 AWQ/GPTQ 竞争基线。

### 4.2 评价指标

本文使用以下指标：

1. `PPL`：量化后语言建模困惑度，越低越好。
2. `target vs uniform`：目标分配相对 uniform INT4 的 PPL 改善。
3. `target vs best random`：目标分配相对同预算随机分配最佳种子的 PPL 边际。
4. `win/loss/tie`：目标分配对多个随机种子的逐一比较。
5. `GPU guard peak`：运行期间显存峰值是否低于 85% 上限。

### 4.3 基线

本文当前包含以下内部基线：

- FP16：未量化模型质量参考。
- uniform INT4：所有线性模块统一 4-bit fake quant。
- category heuristic：C++ 结构类别启发式分配。
- random budget：同平均位宽预算的随机分配。
- single-split loss-sensitive：单一校准分布的敏感度分配。
- WikiText2+C4 consensus：本文主方法。

正式投稿前仍需加入更完整的 GPTQ、AWQ、SmoothQuant、QuaRot/SpinQuant 等公开基线。当前仓库已有 Qwen2.5-0.5B 上的局部 AutoAWQ/GPTQModel readiness、aligned 16-prompt public PPL gates 与 matched-pack 证据，但它们只能支持“本地官方包路径已接通”的边界声明，不能支持相对这些方法的优势声明。

## 5 实验结果

### 5.1 Qwen3-0.6B：从单分割失败到 consensus 修复

Qwen3-0.6B 含 197 个被测线性模块。单 WikiText2 分割分配 44 个 8-bit 模块，C4 分割分配 41 个 8-bit 模块，WikiText2+C4 consensus 分配 46 个 8-bit 模块，平均位宽均约为 4.4997。

| 分配 | 4-bit 模块 | 8-bit 模块 | 平均位宽 |
|---|---:|---:|---:|
| WikiText2 single split | 153 | 44 | 4.4997 |
| C4 single split | 156 | 41 | 4.4997 |
| WikiText2+C4 consensus | 151 | 46 | 4.4997 |

单分割结果显示了本文的核心问题。WikiText2 单分割在 C4 上击败全部 15 个随机种子，但在 WikiText2-64 len96 上输给最佳随机种子。

| 数据集 | FP16 | uniform INT4 | WikiText2 split | random min/mean/max | vs best random |
|---|---:|---:|---:|---:|---:|
| WikiText2-64 len96 | 33.9865 | 54.6542 | 49.5352 | 48.5030 / 50.4787 / 52.6347 | -1.0322 |
| C4-64 | 36.1380 | 52.9352 | 47.5872 | 48.3840 / 49.4427 / 50.7971 | +0.7969 |

引入 consensus 后，同一预算下两个数据集均击败所有随机种子。

| 数据集 | FP16 | uniform INT4 | consensus | category | random min/mean/max | vs uniform | vs best random |
|---|---:|---:|---:|---:|---:|---:|---:|
| WikiText2-64 len96 | 33.9865 | 54.6542 | 45.6559 | 50.4746 | 48.5030 / 50.4787 / 52.6347 | +8.9983 | +2.8471 |
| C4-64 | 36.1380 | 52.9352 | 44.9290 | 48.6222 | 48.3840 / 49.4427 / 50.7971 | +8.0062 | +3.4551 |

随机审计进一步确认，consensus 对 15 个随机种子的 win/loss/tie 均为 `15/0/0`。

| 数据集 | consensus PPL | 随机种子数 | win/loss/tie | 最佳随机种子 | vs best seed | vs seed mean |
|---|---:|---:|---:|---|---:|---:|
| WikiText2-64 len96 | 45.6559 | 15 | 15/0/0 | `random_seed_20260609` | +2.8471 | +4.8229 |
| C4-64 | 44.9290 | 15 | 15/0/0 | `random_seed_20260609` | +3.4551 | +4.5138 |

这组结果支持本文主张：单分割敏感度信号有价值但不稳，跨数据集一致性可以把该信号转化为更可靠的分配策略。

### 5.2 Qwen3-1.7B 与 OLMo2：第二层模型证据

在 Qwen3-1.7B 与 OLMo2-0425-1B-Instruct 上，WikiText2+C4 consensus 同样在两个 64-prompt 短切片上优于最佳随机种子。

| 模型 | 数据集 | FP16 | uniform INT4 | consensus | random min/mean/max | vs best random |
|---|---|---:|---:|---:|---:|---:|
| Qwen3-1.7B | WikiText2-64 | 21.6552 | 31.1885 | 26.3260 | 27.6685 / 28.2905 / 29.9682 | +1.3425 |
| Qwen3-1.7B | C4-64 | 25.5510 | 30.7410 | 28.3303 | 28.4562 / 29.4357 / 30.0408 | +0.1259 |
| OLMo2-1B | WikiText2-64 | 18.8573 | 22.4888 | 21.0349 | 21.4637 / 21.6140 / 21.7550 | +0.4288 |
| OLMo2-1B | C4-64 | 32.2736 | 36.8334 | 35.4726 | 35.8512 / 36.0334 / 36.3837 | +0.3785 |

其中 Qwen3-1.7B 的 C4 边际较小，说明方法仍是短切片诊断而非强泛化保证。尽管如此，它和 OLMo2 的负例修复共同说明 consensus 不是只在 Qwen3-0.6B 上偶然有效。

### 5.3 校准分割稳定性

分割稳定性审计显示，WikiText2 与 C4 的短校准探针存在明显排序差异。

| 模型 | 共享模块数 | positive-set Jaccard | score/cost Spearman | top-20 score Jaccard |
|---|---:|---:|---:|---:|
| Qwen3-1.7B | 197 | 0.4512 | 0.0734 | 0.1429 |
| OLMo2-1B | 113 | 0.4512 | 0.1845 | 0.1111 |

这些低相关性解释了为什么单分割分配可能输给随机种子。它也说明本文的 consensus 不是额外复杂化，而是对可观测噪声的直接响应。

### 5.4 Budget Curve

如果分配策略有效，释放更多 8-bit 预算应当总体降低 fake-quant PPL。当前 Qwen3-1.7B 与 OLMo2 的 budget curve 在 4.25、4.50、4.75 平均位宽上呈单调改善。

| 模型 | 数据集 | 4.25 bits | 4.50 bits | 4.75 bits |
|---|---|---:|---:|---:|
| Qwen3-1.7B | WikiText2-64 | 28.0753 | 27.3180 | 26.6163 |
| Qwen3-1.7B | WikiText2-128 | 27.7279 | 27.4054 | 26.5665 |
| Qwen3-1.7B | C4-64 | 30.4752 | 29.9230 | 29.2500 |
| OLMo2-1B | WikiText2-64 | 23.2779 | 22.5113 | 22.1464 |
| OLMo2-1B | WikiText2-128 | 25.7774 | 25.0435 | 24.6993 |
| OLMo2-1B | C4-64 | 37.9817 | 37.2835 | 37.1610 |

该结果不是质量绝对值上的 SOTA 证据，但验证了位宽预算与 fake-quant 质量之间的方向性关系。

### 5.5 GPU Guard

所有纳入本稿的 Qwen3-0.6B consensus 新实验均低于用户设定的 85% 显存上限。

| 运行 | 峰值显存 | 峰值比例 | 峰值 GPU 利用率 | 状态 |
|---|---:|---:|---:|---|
| C4 sensitivity | 4589 / 8151 MiB | 56.30% | 36% | pass |
| consensus WikiText2 eval | 4867 / 8151 MiB | 59.71% | 57% | pass |
| consensus C4 eval | 4893 / 8151 MiB | 60.03% | 55% | pass |

Qwen3-1.7B 和 OLMo2 的相关 guarded runs 也低于 85%，其中 Qwen3 peaked at `5071/8151 MiB`，OLMo2 peaked at `4376/8151 MiB`。GPU guard 是实验有效性的必要条件：超出上限被 kill 的运行不纳入结果。

### 5.6 官方 PTQ readiness 与系统证据边界

当前仓库已把 AutoAWQ 与 GPTQModel 的 Qwen2.5-0.5B W4/G128 本地包纳入统一 readiness matrix。两者均使用公开校准提示，均扩展到 WikiText2/C4 各 16 个 public PPL prompts；两个包合计覆盖 5714 个 PPL eval tokens，最大 package-vs-FP16 PPL ratio 为 1.2570。

同一 matched baseline pack 还合并了 300 次 subset50 public task executions 与 PC 侧 runtime/VRAM profile。随后新增的 deterministic IFEval-style gate 覆盖 FP16、AutoAWQ、GPTQModel 三种 Qwen2.5-0.5B 变体共 24 次指令格式执行，并记录单独 runtime profile；由于 FP16 baseline 为 0/8，这部分只能作为执行路径证据，而不是任务保持率证据。这个结果最重要的含义是边界清晰：量化包在本地 Transformers/GPTQModel 路径下降低了部分 guarded VRAM，但 tokens/s 慢于 FP16。因此它是 readiness 与负结果记录，不是加速结果。

## 6 讨论

### 6.1 为什么不是单纯增加校准样本

增加校准样本可以降低估计方差，但在本地资源受限和短周期迭代下，校准预算本身也是约束。本文选择跨分布一致性，是因为它能在很少样本条件下暴露“只对一个分割敏感”的不稳定模块。未来更完整版本应同时研究样本数、分割数和分布差异三者的关系。

### 6.2 与随机基线的关系

随机基线不是强生产基线，但它是检验启发式分配是否有真实信息量的最低门槛。如果一个敏感度分配不能稳定击败同预算随机分配，则很难证明其排序信号可靠。本文保留 best-random 负结果，目的是防止把 uniform INT4 改善误报为稳健算法优势。

### 6.3 与真实量化器的关系

EigenSkill-Q 当前是 fake-quant 诊断框架，而不是 GPTQ/AWQ/SmoothQuant/QuaRot 的替代品。更合理的发展方向是把 consensus sensitivity 作为混合精度 bit allocation 或 baseline initialization 的上层策略，再接入真实量化器和 packed runtime。

## 7 局限性

1. 当前评估仍是 PyTorch fake quant，不能支持真实延迟、显存占用或能耗结论。
2. 数据切片较短，PPL 结果应视为诊断信号，而非完整 benchmark。
3. 尚未完整纳入 GPTQ、AWQ、SmoothQuant、QuaRot、SpinQuant 等公开强基线；现有 AutoAWQ/GPTQModel 证据仅覆盖 Qwen2.5-0.5B 的 public-calibrated readiness、16-prompt PPL、subset50 任务执行与 PC 侧 runtime/VRAM 观测。
4. 当前只覆盖少数模型家族，尚不足以证明跨架构普适性。
5. 位宽集合仅为 `{4,8}`，未覆盖 INT3、INT2、FP4、NF4、MXFP4 等格式。
6. C++ 工具主要负责 allocation/report/audit，模型执行仍依赖 Python/PyTorch。
7. 尚无 ARM NEON、RKNN、Ascend、Qualcomm NPU 或 llama.cpp/ExecuTorch 集成。

这些限制决定了本文当前更适合作为技术报告、workshop 草稿或后续正式论文的实验骨架，而不是直接投递系统或硬件顶会。

## 8 结论

本文提出 EigenSkill-Q，将资源受限大语言模型量化研究从早期宽泛的“技能路由”叙事收敛到一个更可验证的问题：少样本校准下，敏感度引导混合精度分配如何避免被单一分割噪声误导。通过 WikiText2+C4 跨数据集一致性分配，本文在 Qwen3-0.6B 上修复了单分割输给最佳随机分配的失败行，并在 Qwen3-1.7B 与 OLMo2 上得到第二层支持。配套 C++ 审计工具进一步增强了结果可追溯性。后续工作应优先补齐公开量化基线、更大评估切片、多校准种子统计检验，以及真实 packed runtime 和硬件测量。

## 致谢

本文实验和仓库整理围绕 Rui 的 EigenSkill/EigenSkill-Q 研究方向展开。当前稿件强调诚实边界：可证明的部分写成结果，未完成的边缘硬件、谱路由和物理群体智能仅保留为未来方向。

## 参考文献

[1] K. He, X. Zhang, S. Ren, and J. Sun. Deep Residual Learning for Image Recognition. arXiv:1512.03385, 2015. https://arxiv.org/abs/1512.03385

[2] T. Dettmers, M. Lewis, Y. Belkada, and L. Zettlemoyer. LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale. arXiv:2208.07339, 2022. https://arxiv.org/abs/2208.07339

[3] E. Frantar, S. Ashkboos, T. Hoefler, and D. Alistarh. GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers. arXiv:2210.17323, 2022. https://arxiv.org/abs/2210.17323

[4] G. Xiao, J. Lin, M. Seznec, H. Wu, J. Demouth, and S. Han. SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models. arXiv:2211.10438, 2022. https://arxiv.org/abs/2211.10438

[5] J. Lin, J. Tang, H. Tang, S. Yang, X. Dang, and S. Han. AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration. arXiv:2306.00978, 2023. https://arxiv.org/abs/2306.00978

[6] Z. Dong, Z. Yao, A. Gholami, M. Mahoney, and K. Keutzer. HAWQ: Hessian AWare Quantization of Neural Networks with Mixed-Precision. arXiv:1905.03696, 2019. https://arxiv.org/abs/1905.03696

[7] S. Ashkboos et al. QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs. arXiv:2404.00456, 2024. https://arxiv.org/abs/2404.00456

[8] Z. Liu et al. SpinQuant: LLM quantization with learned rotations. arXiv:2405.16406, 2024. https://arxiv.org/abs/2405.16406

## 附录 A：仓库证据索引

本文主要数值来自以下提交后的仓库产物：

```text
outputs/qwen3_0p6b_lowmem_consensus_random16_evidence_matrix.md
outputs/qwen3_0p6b_lowmem_consensus_random16_random_seed_audit.md
outputs/qwen3_0p6b_lowmem_consensus_random16_gpu_guard_summary.md
outputs/qwen3_0p6b_wikitext2_c4_consensus_alloc_4to8_limit4_group128_report.md
outputs/INTERACTION_SWAP_BOUNDARY_GATE_2026_06_07.md
outputs/OFFICIAL_PTQ_MATCHED_BASELINE_PACK_QWEN25_0P5B_2026_06_07.md
outputs/OFFICIAL_PTQ_READINESS_MATRIX_QWEN25_0P5B_2026_06_07.md
outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_0P5B_BUNDLE_16_GATE_2026_06_07.md
outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_0P5B_BUDGET8_16_GATE_2026_06_07.md
outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md
docs/consensus-allocation-method.md
docs/PAPER_CLAIM_MATRIX.md
```

旧稿对应早期 Git commit：

```text
f0cadb7adc0a660c4945ffb542b2fc5ea0f55fc9
```

新版英文稿对应后续公开分支提交，详见 GitHub PR commit history。
