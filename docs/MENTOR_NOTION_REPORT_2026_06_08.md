# EigenSkill-Q 导师版阶段报告

Date: 2026-06-08
Public repository: <https://github.com/rui4399/eigenskill-research-pack>
Latest pushed commit for this report cycle: `6ff1d3c`

> 这份文档是 Notion-ready 版本：导师不需要访问本机，只需要打开 GitHub
> 链接即可看到当前研究定位、数学原理、实验进展、证据边界和后续工作。

## 1. 一句话定位

本项目当前已经从早期“跨介质/蜂群/微内核”的宏大设想，收敛为一个更清晰、
更可验证的技术问题：

```text
当混合精度 LLM 量化依赖很小的校准集时，模块敏感度排序会有多不稳定？
这种不稳定会如何影响 bit allocation？能否用跨校准集共识降低错误分配风险？
```

因此，当前项目不再声称“提出新的 SOTA 量化器”，而是聚焦：

1. 发现并形式化 **Calibration Split Instability, CSI**；
2. 给出校准噪声、秩翻转风险、bootstrap 置信区间和置换检验；
3. 用统一门锁式实验流水线对 fake-quant、native PTQ、任务保留率和运行时证据进行审计；
4. 在有限 GPU 条件下完成 Qwen2.5-1.5B 的全量 MMLU 本地匹配基线。

这个定位的优点是问题边界清楚、结果可复现、证据链容易检查；当前阶段更接近
“量化鲁棒性诊断与工具链”，还不是完整 production quantizer。

## 2. 为什么这个问题值得做

主流 LLM 量化方法通常需要一个校准集来估计不同层或模块对量化误差的敏感度。
常见流程是：

```text
选一小批校准文本 -> 估计每个模块量化后的 loss 增量 -> 对模块排序 ->
把高 bit 分给敏感模块，把低 bit 分给不敏感模块
```

问题在于，边缘设备或快速 PTQ 场景里，校准样本往往很少。如果校准集换一批样本，
敏感度排序发生大幅变化，那么后续 bit allocation 其实是在跟噪声走，而不是跟
模型真实结构走。这个问题会造成三类风险：

1. **排序风险**：两个模块真实敏感度很接近时，小样本噪声会把二者顺序排反。
2. **预算风险**：混合精度量化通常有平均 bit 预算，例如 4.5 bit；排序错误会把
   高 bit 预算浪费在不该保护的模块上。
3. **泛化风险**：只在 WikiText2 校准出来的敏感模块，不一定能迁移到 C4、MMLU、
   GSM8K 或真实用户任务。

CSI 的核心价值就是把“校准集不稳定”从一个经验担忧变成一个可测量、可统计检验、
可画曲线、可和 downstream retention 连接的问题。

## 3. 核心数学模型

### 3.1 模块敏感度估计

设模型有模块集合 \(\mathcal{M}=\{1,\ldots,L\}\)。对模块 \(i\)，真实敏感度定义为
该模块被量化后在目标分布 \(\mathcal{P}\) 上引起的期望损失增量：

\[
s_i^\star =
\mathbb{E}_{x\sim \mathcal{P}}
\left[
\ell(f_{\theta}^{(i,q)};x)-\ell(f_{\theta};x)
\right].
\]

实际实验中无法访问完整分布，只能从大小为 \(m\) 的校准集
\(D=\{x_1,\ldots,x_m\}\) 上估计：

\[
\hat{s}_i(D)=
\frac{1}{m}\sum_{k=1}^{m}
\left[
\ell(f_{\theta}^{(i,q)};x_k)-\ell(f_{\theta};x_k)
\right].
\]

这里 \(f_{\theta}^{(i,q)}\) 表示只把模块 \(i\) 量化后的模型；\(\ell\) 是语言模型
loss。直观上，\(\hat{s}_i(D)\) 越大，模块 \(i\) 越不适合低 bit。

### 3.2 校准噪声与估计误差

令单样本损失增量随机变量为

\[
Z_i(x)=\ell(f_{\theta}^{(i,q)};x)-\ell(f_{\theta};x),
\quad
\mathbb{E}[Z_i]=s_i^\star,\quad
\mathrm{Var}(Z_i)\le \sigma_i^2.
\]

在有界方差假设下，Chebyshev 不等式给出：

\[
\Pr\left(|\hat{s}_i(D)-s_i^\star|\ge \epsilon\right)
\le
\frac{\sigma_i^2}{m\epsilon^2}.
\]

这说明当校准样本数 \(m\) 很小时，敏感度估计误差会随 \(1/m\) 缩小得很慢；
如果不同模块的真实敏感度差距本来就小，那么排序很容易被噪声扰乱。

### 3.3 秩翻转风险

对两个模块 \(i,j\)，真实敏感度间隔为：

\[
\Delta_{ij}=|s_i^\star-s_j^\star|.
\]

若估计噪声的成对方差代理为 \(\tau_{ij}^2\)，则可以写出一个保守的秩翻转风险界：

\[
\Pr\left(
\mathrm{sign}(\hat{s}_i(D)-\hat{s}_j(D))
\ne
\mathrm{sign}(s_i^\star-s_j^\star)
\right)
\le
\frac{4\tau_{ij}^2}{m\Delta_{ij}^2}.
\]

这个公式的系统含义很直接：

- \(m\) 越大，校准样本越多，排序越稳定；
- \(\tau_{ij}^2\) 越大，说明这对模块对输入分布更敏感，更容易排错；
- \(\Delta_{ij}\) 越小，说明两个模块真实敏感度接近，小样本下更容易互换顺序。

这就是 CSI-vs-n 曲线的理论基础。

### 3.4 CSI 指标

给定两个校准集 \(D_a,D_b\)，项目同时统计三类稳定性：

\[
\rho_{\mathrm{Spearman}}(D_a,D_b)
=
\mathrm{corr}_{\mathrm{rank}}
\left(\hat{s}(D_a),\hat{s}(D_b)\right),
\]

\[
J_k(D_a,D_b)
=
\frac{|\mathrm{TopK}(\hat{s}(D_a))\cap \mathrm{TopK}(\hat{s}(D_b))|}
{|\mathrm{TopK}(\hat{s}(D_a))\cup \mathrm{TopK}(\hat{s}(D_b))|},
\]

\[
J_+(D_a,D_b)
=
\frac{|P(D_a)\cap P(D_b)|}{|P(D_a)\cup P(D_b)|},
\]

其中 \(J_k\) 衡量 top-sensitive 模块集合是否一致，\(J_+\) 衡量正敏感模块集合是否
一致。报告中把这些指标作为 CSI 诊断的主体，而不是只看单个 PPL 数字。

### 3.5 共识分配思想

如果单一校准集的排序不稳定，那么直接用一个 split 的排序分配 bit 容易过拟合。
因此当前方法采用保守的 cross-split consensus：

\[
\bar{s}_i = \alpha \hat{s}_i(D_1) + (1-\alpha)\hat{s}_i(D_2),
\]

或使用 top set intersection / robust lower-confidence bound 等变体。目标不是声称
这就是新量化器，而是证明：

```text
校准噪声存在 -> 排序不稳定可测 -> 共识估计可以降低单 split 决策风险。
```

## 4. 当前实验进展

### 4.1 仓库与证据工程

公开仓库已经从“运行中的实验笔记”整理为可审计 artifact：

- root README 收敛为项目范围、非 claim 和证据入口；
- `docs/PAPER_CLAIM_MATRIX.md` 管理每条公开结论及其证据边界；
- `docs/SYSTEM_EVIDENCE_GATES.md` 管理实验 gate；
- `docs/SYSTEM_EVIDENCE_RUNBOOK.md` 管理可复现命令；
- `outputs/` 中的结果只有被 claim matrix 或 gate 引用时才算正式公开证据。

当前公开仓库主入口：

- README: <https://github.com/rui4399/eigenskill-research-pack/blob/main/README.md>
- Claim matrix: <https://github.com/rui4399/eigenskill-research-pack/blob/main/docs/PAPER_CLAIM_MATRIX.md>
- Artifact manifest: <https://github.com/rui4399/eigenskill-research-pack/blob/main/docs/ARTIFACT_MANIFEST.md>

### 4.2 CSI-vs-n 曲线

在 Qwen2.5-0.5B-Instruct 上，使用同一公共 WikiText2 prompt pool，分别抽取
\(n=2,4,8\) 条校准 prompt，并用 6 个 deterministic seeds 生成 seed-pair 稳定性。

核心结果：

| Calibration size | Mean Spearman | Top-20 Jaccard | Positive-set Jaccard |
|---:|---:|---:|---:|
| n=2 | 0.3725 | 0.3797 | 0.5485 |
| n=4 | 0.4324 | 0.4672 | 0.5734 |
| n=8 | 0.6645 | 0.6449 | 0.7282 |

对应解释：

- 随着校准样本从 2 增加到 8，敏感度排序稳定性明显提升；
- n=2 到 n=4 的提升并非所有指标都显著分离；
- n=4 到 n=8 的提升更加稳定；
- 这支持“校准集太小时排序噪声显著”的研究动机。

公开证据：

- <https://github.com/rui4399/eigenskill-research-pack/blob/main/outputs/CSI_VS_N_CURVE_QWEN25_0P5B_2026_06_07.md>

### 4.3 Bootstrap 趋势显著性

对 n=2 与 n=8 的 seed-pair 分布进行 bootstrap 检验：

| Metric | n=2 mean | n=8 mean | Mean gain | 95% bootstrap CI | Dominance |
|---|---:|---:|---:|---:|---:|
| Spearman | 0.3725 | 0.6645 | 0.2920 | [0.2039, 0.3775] | 0.9422 |
| Top-20 Jaccard | 0.3797 | 0.6449 | 0.2651 | [0.1961, 0.3369] | 0.9778 |
| Positive Jaccard | 0.5485 | 0.7282 | 0.1797 | [0.1352, 0.2195] | 0.9644 |

这说明 n=8 相比 n=2 的稳定性提升不仅是均值变化，也有统计置信区间支撑。

公开证据：

- <https://github.com/rui4399/eigenskill-research-pack/blob/main/outputs/CSI_TREND_SIGNIFICANCE_QWEN25_0P5B_2026_06_07.md>

### 4.4 置换检验与 Holm 校正

项目还做了 Monte-Carlo label-shuffle permutation null。三项指标的 observed gain
均通过 Holm-adjusted 显著性校正：

| Metric | Observed gain | Raw p | Holm-adjusted p |
|---|---:|---:|---:|
| Spearman | 0.2920 | 4.99975e-05 | 0.000149993 |
| Top-20 Jaccard | 0.2651 | 4.99975e-05 | 0.000149993 |
| Positive Jaccard | 0.1797 | 4.99975e-05 | 0.000149993 |

公开证据：

- <https://github.com/rui4399/eigenskill-research-pack/blob/main/outputs/CSI_NULL_PERMUTATION_QWEN25_0P5B_2026_06_07.md>

### 4.5 Native PTQ 全量 MMLU 进展

为了回应“不能只做 fake-quant / 小样本 smoke”的批评，项目已经完成
Qwen2.5-1.5B-Instruct 在 FP16、AutoAWQ、GPTQModel 三个变体上的本地全量
MMLU 匹配评测。该评测覆盖 57 个 MMLU subjects，共 14,042 行；三种变体使用
相同任务 fixture 和 GPU guard。

| Variant | Rows | Passes | Accuracy | Mean tok/s | Mean TTFT | Peak VRAM |
|---|---:|---:|---:|---:|---:|---:|
| FP16 | 14,042 | 8,234 | 0.5864 | 4.9773 | 0.396824 s | 7168 MiB |
| AutoAWQ | 14,042 | 7,931 | 0.5648 | 10.8232 | 0.153977 s | 6633 MiB |
| GPTQModel | 14,042 | 7,529 | 0.5362 | 9.1870 | 0.182449 s | 6167 MiB |

相对 FP16：

- AutoAWQ accuracy drop: 0.0216；
- GPTQModel accuracy drop: 0.0502；
- AutoAWQ 本地 guarded tokens/s ratio: 2.1745；
- GPTQModel 本地 guarded tokens/s ratio: 1.8458；
- AutoAWQ/GPTQModel 峰值 VRAM 均低于 FP16。

重要边界：

- 这是本地 PC-side、guarded、matched prompt 的 evidence；
- 可以作为 native PTQ baseline evidence；
- 不能声称 official leaderboard；
- 不能声称手机部署；
- 不能声称 energy improvement；
- 不能声称已经优于 AWQ/GPTQ 官方方法中的全部设置。

公开证据：

- Task matrix: <https://github.com/rui4399/eigenskill-research-pack/blob/main/outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_MMLU_FULL_PREFIX14042_FP16_AWQ_GPTQMODEL_MATRIX_2026_06_08.md>
- Runtime profile: <https://github.com/rui4399/eigenskill-research-pack/blob/main/outputs/OFFICIAL_PTQ_QWEN25_1P5B_MMLU_FULL_PREFIX14042_FP16_AWQ_GPTQMODEL_RUNTIME_PROFILE_2026_06_08.md>
- Statistics: <https://github.com/rui4399/eigenskill-research-pack/blob/main/outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_MMLU_FULL_PREFIX14042_FP16_AWQ_GPTQMODEL_STATISTICS_2026_06_08.md>

### 4.6 Full GSM8K 与 7B 覆盖

除 MMLU 外，项目已完成两条补充证据：

1. Qwen2.5-1.5B FP16/AutoAWQ/GPTQModel 在 GSM8K 全量 1,319 行上的 matched
   retention row；
2. Ollama Qwen2.5-abliterate-7B 的 public-task coverage row，包括 100 行
   MMLU abstract algebra + 200 行 GSM8K，以及完整 GSM8K 1,319 行。

这些结果的作用是缓解“只有 tiny subset”的批评，但目前 7B 证据还不是
quantized retention，因此不应作为主结论，只作为 scale coverage。

### 4.7 系统与 runtime 证据现状

系统侧已经有 C++/ESMP/Triton 的原型证据，包括：

- C++ allocation planner；
- ESMP packed format；
- Triton shape-family kernel gates；
- W4A8 selected-module reconstruction gate；
- Redmi K80 Pro harness skeleton。

但系统侧目前还不能作为端到端系统结论，原因是：

- 还没有完整 minimal runtime 的端到端 text generation；
- mobile/Redmi K80 Pro 没有完整 TTFT/tokens/s/peak memory log；
- kernel-level 快不等于 end-to-end 快；
- 完整系统结论需要报告物理文件大小、真实显存、TTFT、tokens/s、能耗或至少端侧延迟。

因此本阶段把工作拆成两条线：

```text
算法与统计线 = CSI + native PTQ + statistical robustness
系统与工程线 = ESMP/Triton/minimal runtime，等端到端证据补齐后再提升权重
```

## 5. 当前完成的核心工作

### 5.1 Calibration Split Instability

提出并测量 LLM mixed-precision quantization 中的校准分割不稳定性。区别于只报告
PPL，本项目报告 rank correlation、top-k overlap、positive-set overlap 和
CSI-vs-n 曲线。

### 5.2 Statistical testing pipeline

将敏感度估计误差与秩翻转风险写成统计模型，并使用 bootstrap confidence intervals、
permutation null test、Holm adjustment 对趋势进行消解。

### 5.3 Conservative consensus allocation

用 cross-split consensus 减少单校准集排序噪声带来的错误 bit allocation 风险。
当前更适合描述为 diagnostic allocation framework，而不是新的 production quantizer。

### 5.4 Gated artifact discipline

每条 claim 都要求同时具备：

1. JSON artifact；
2. Markdown gate report；
3. runbook command；
4. claim boundary row。

这种 evidence gate 能保证公开结果都有可追溯证据，避免阶段成果被误读。

### 5.5 Native PTQ baseline row

已经补上 Qwen2.5-1.5B FP16/AutoAWQ/GPTQModel 的全量 MMLU 14,042 行 matched row，
这是目前最重要的“非 fake-quant”证据。

## 6. 当前边界

当前证据还不支持以下结论：

- 不能说我们提出了 SOTA quantizer；
- 不能说 consensus allocation 全面优于 AWQ/GPTQ/SmoothQuant/QuaRot；
- 不能说已经有 production runtime；
- 不能说移动端部署已完成；
- 不能说 W4A8/Triton kernel speedup 等价于端到端生成加速；
- 不能把 Eigen-Swarm、acoustic communication、physical swarm assembly 当作当前已完成结果。

这些内容可以作为长期方向，但不应和当前已完成的 CSI/量化鲁棒性证据混在一起。

## 7. 下一阶段最小闭环

### P0: 理论 section 固化

把以下内容压成 1.5 页以内：

1. sensitivity estimator；
2. Chebyshev/Hoeffding-style error bound；
3. pairwise rank inversion；
4. bootstrap CI；
5. permutation null；
6. Holm-adjusted p-value。

目标：把当前经验观察解释为 calibration noise 下的 robust ranking 问题，而不是
简单的 score averaging 技巧。

### P1: 补一个更强 baseline 或 ablation

在时间允许时优先补：

- SmoothQuant 或 rotation-family 一行；
- 更完整 IFEval；
- 3B/7B quantized retention；
- CSI allocation 与 native PTQ 的更清晰对齐。

### P2: 系统备线继续推进

系统侧继续做，但不要阻塞当前 CSI/量化鲁棒性主线：

- 导出真实 `.eqm` / ESMP packed 文件并报告物理大小；
- 写 minimal runtime，避开 PyTorch hook overhead；
- 报告 TTFT、tokens/s、peak VRAM；
- 如果端到端仍慢，诚实写成 integration-risk finding。

## 8. 给导师看的当前结论

项目目前已经从“想法很大但容易发散”的状态，收敛成一个可复现、有统计支撑、
可以持续推进的研究问题。最关键的进展不是又写了一份草稿，而是已经补上了：

1. CSI-vs-n 的统计趋势；
2. bootstrap 和 permutation 显著性；
3. Qwen2.5-1.5B full-MMLU 14,042 行 native PTQ matched evidence；
4. 明确的 claim firewall 和 public artifact discipline。

当前工作的核心不是宣称“我们造了一个更强量化器”，而是证明并系统化一个容易被
忽略的问题：小校准集会让敏感度排序本身不可靠，从而影响混合精度量化决策。围绕
这个问题，项目已经形成了数学定义、统计检验、实验流水线和公开证据仓库。
