# NotebookLM / Gemini 审稿人问题集

日期：2026-06-03

当前个人 NotebookLM 没有可直接调用的 API，Codex 无法真正和 NotebookLM 里的 Gemini 自动对话。因此这里写成可直接复制给 NotebookLM/Gemini 的问题集。目标不是让它夸 idea，而是模拟严厉审稿人，暴露 EigenSkill-Q 的数学、实验和创新缺口。

## 使用方式

把下面整段复制到 NotebookLM/Gemini：

```text
你现在扮演 NeurIPS/ICLR/MLSys/ASPLOS 或 IEEE TNNLS/Neural Networks/Information Sciences 的严厉审稿人。请基于我提供的 EigenSkill-Q 设想，从 LLM 量化数学、低比特推理系统、实验设计和论文创新性四个角度提出批判性意见。不要鼓励式回答，优先指出不可发表、证据不足、和已有工作重复的地方，并给出可执行修改建议。
```

---

## 10 个最核心问题

### 1. 当前 v2 skill 数据是否存在严重 train/eval leakage？

已知审计结果：

```text
train_n = 7200
eval_n = 1440
exact_train_eval_overlap = 1339
input_train_eval_overlap = 1339
unique_prompt_templates = 13
```

请判断：这种结果还能否作为论文主实验？如果不能，如何把它降级为 engineering PoC，同时重建无泄漏 benchmark？

### 2. EigenSkill-Q 和 GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant 的本质区别是什么？

请逐项比较：

- GPTQ 的 Hessian-aware weight quantization；
- AWQ 的 activation-aware salient weight protection；
- SmoothQuant 的 activation outlier migration；
- QuaRot/SpinQuant 的 orthogonal rotation；
- HARP/TORQ/ButterflyQuant 的 learned or structured rotation；
- EigenSkill-Q 的 sensitivity-rate-distortion bit allocation。

如果只是组合已有方法，怎样构造真正新的贡献？

### 3. “skill” 这个概念是否会被审稿人认为是包装词？

如果 skill 只是 layer policy、bit-width policy、rotation policy 的别名，是否需要改名？

请评估三种命名：

```text
EigenSkill-Q
Quantization Skill Router
Sensitivity-Aware Quantization Policy Router
```

哪一个更容易被国际审稿人接受？

### 4. 能否给出位宽分配的理论推导？

候选公式：

```text
b_{l,g}^* = clip_B( 1/2 log2( S_{l,g} sigma_{l,g}^2 / (lambda c_{l,g}) ) )
```

请检查它从 rate-distortion + Lagrangian 推导是否严谨。这里 $S_{l,g}$ 应该如何定义？用 Hessian trace、activation covariance、perplexity drop、还是 Fisher information？

### 5. 正交旋转的目标函数是否足够新？

候选目标：

```text
min_R tr( DeltaW_R R C R^T DeltaW_R^T ) + rho Cost(R)
s.t.  R^T R = I
```

请判断：这是否只是 QuaRot/SpinQuant/HARP 的重复？如果要创新，应该加入哪些硬件格式约束，例如 MXFP4 block scale、NVFP4 E4M3 scale、codebook occupancy、block variance balance？

### 6. 低秩残差补偿是否比原 eigen bypass 更可发表？

候选结构：

```text
y = Q_b(W)x + A(B^T x),  rank(AB^T)=r << d
```

请从数学和系统角度评价：

- 是否比 $W e_s \approx \lambda e_s$ 更稳？
- 是否和 LoRA / QA-LoRA / SERQ / ARHQ / pQuant 重复？
- 如何证明它服务任意输入而不是只服务模板 skill？

### 7. 混合精度实验如何避免过拟合校准集？

请设计严格划分：

```text
calibration set != validation set != test set
prompt templates disjoint
tasks disjoint
models optionally disjoint for transfer
```

尤其关注：如果用 128/256/512 条 calibration samples 调 bit-width，如何证明不是调到某个 benchmark？

### 8. 评估任务应该选哪些，才能证明量化方法真的强？

请评估下面任务组合是否足够：

- WikiText2 / C4 perplexity；
- ARC / PIQA / HellaSwag；
- GSM8K 或 MATH-mini；
- HumanEval / MBPP small subset；
- Long-context retrieval / Needle-in-a-Haystack；
- 中文/英文/符号混合输入。

还缺什么？是否需要 TruthfulQA、MMLU、BBH、LongBench？

### 9. 系统论文需要哪些真实硬件证据？

如果目标是 ASPLOS/MLSys，只有 PyTorch fake quant 是否不够？

请列出最低系统证据：

- latency；
- throughput；
- VRAM / RAM；
- dequant overhead；
- kernel fusion；
- CPU/GPU/ARM/RK3588/手机端；
- energy proxy。

哪些必须真实测，哪些可以先用 emulator/proxy？

### 10. 最可能被拒稿的原因是什么？

请站在审稿人角度，列出 top 10 rejection risks，例如：

- novelty insufficient；
- too many existing baselines missing；
- no proof；
- toy data leakage；
- no real kernel；
- only small models；
- no ablation；
- no long-context/KV；
- unclear skill terminology；
- hardware claims overclaimed。

并给每个风险对应一个修复动作。

---

## 额外 8 个针对数学主线的问题

### 11. Hessian 近似如何低成本估计？

请比较：

```text
Hessian diagonal
Hessian trace
Fisher diagonal
activation covariance C = E[xx^T]
GPTQ-style block Hessian X X^T
perplexity sensitivity probing
```

哪种最适合 0.5B-3B 小模型快速实验？

### 12. Rate-distortion 假设是否成立？

如果权重/激活不是 Gaussian，且有 heavy-tail/outlier，公式：

```text
D \approx sigma^2 2^{-2b}
```

会不会失效？是否需要用 generalized Gaussian、kurtosis correction 或 empirical distortion table？

### 13. MXFP4/NVFP4 的误差模型怎么写？

请给出 block floating point 的理论模型：

```text
hat z_i = s_B c_i
```

并分析 scale quantization、block size、codebook occupancy、outlier 对误差的影响。

### 14. 正交旋转是否总能降低量化误差？

请给出反例或条件：什么情况下旋转无效甚至变差？

比如：

- covariance 已经接近 isotropic；
- block scale 分组和旋转结构不匹配；
- 旋转开销超过收益；
- 激活分布校准集外漂移。

### 15. 低秩残差分支的 rank 如何分配？

是否可以和 bit allocation 统一：

```text
min_{b_l,r_l} Σ_l S_l ε_l(b_l,r_l)
s.t. Σ_l memory(b_l,r_l) <= B
```

如何选择 $r_l$？

### 16. KV cache 量化是否应该进入第一篇论文？

KV cache 会显著增强系统意义，但会扩大战线。请判断：第一篇主攻 weight-only mixed precision，还是直接做 weight+activation+KV？

### 17. 如何证明方法跨模型泛化？

需要测试：

```text
Qwen2.5-0.5B -> Qwen2.5-1.5B
SmolLM2 -> Qwen
Llama-3.2 -> Qwen
English -> Chinese/multilingual
short context -> long context
```

哪些最有说服力？

### 18. 最终论文应投哪里？

请根据当前阶段判断：

```text
AAAI-27
ASPLOS'27 Sep cycle
MLSys/NeurIPS/ICLR/ICML 2027
TNNLS
Neural Networks
Information Sciences
Pattern Recognition
Journal of Systems Architecture
ACM TECS
```

如果只有算法和小模型，投哪里？如果有 C++ kernel 和硬件测量，投哪里？如果理论更强但实验一般，投哪里？

---

## 让 Gemini 输出的格式要求

```text
请按以下格式输出：
1. 结论：当前是否可投，能投什么级别。
2. 最大硬伤：最多 5 条。
3. 和已有工作的重复点：逐项对比。
4. 最应该保留的创新点：最多 3 条。
5. 必做实验清单：按 2 周、4 周、8 周排序。
6. 最适合投稿 venue：按会议/期刊排序。
7. 你会给这篇论文的初始审稿分数和理由。
```
