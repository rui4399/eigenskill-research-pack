# EigenSkill 阶段性科研报告：面向端侧 LLM 的技能化混合微内核推理框架

日期：2026-06-03

提交对象：导师预沟通材料

## 0. 一句话结论

EigenSkill 目前最稳妥的科研定位不应直接宣称“特征向量路由已经把 Transformer 推理从 O(d^2) 变为 O(d)”，而应收敛为：**面向端侧 LLM 的技能化混合推理框架**。它把低熵、可规则化、强契约输出的任务从大模型稠密路径中剥离出来，用确定性 micro-kernel 或低秩 skill path 旁路执行；小模型只负责语义路由、难以规则化的槽位抽取和上下文理解。这个定位更容易快速出结果，也更符合系统论文的证据要求。

当前可验证结果已经形成一个小型 proof-of-concept：

| 项目 | 结果 |
| --- | --- |
| 基座模型 | `HuggingFaceTB/SmolLM2-360M-Instruct` |
| 技能数 | 8 个低熵技能 |
| 训练样本 | 7200 |
| 评测样本 | 1440 |
| 纯 LoRA/merged FP16 生成评测 | 1391/1440 exact，96.60% |
| Hybrid runtime 评测 | 1439/1440 exact，99.93% |
| `unit_time_normalize` 纯模型 | 73.33% |
| `unit_time_normalize` 旁路后 | 100.00% |
| `intent_routing` v2 | 99.44% |

已生成模型与工程产物包括 LoRA adapter、merged FP16、dynamic INT8 CPU 导出、hybrid runtime CLI、C++ 低秩 microbenchmark。它们足以支撑一次导师讨论和一个 4-8 周的下一阶段实验计划，但还不足以直接支撑 ASPLOS/MLSys 主会级别的强结论。

## 1. 背景与问题定义

端侧 LLM 部署的核心约束不是单一的参数规模，而是“稠密计算图”和“硬件真实瓶颈”之间的错配。传统 Transformer 为了适配 GPU/TPU 的大块矩阵计算，维持了高度规则的结构：均分 attention heads、统一 FFN 宽度、统一量化策略和几乎全路径激活。这种结构在数据中心 GPU 上有利于吞吐，却在边缘设备、嵌入式开发板、国产 NPU 和跨介质 AIoT 设备上暴露出三个问题：

1. 许多端侧任务本身是低熵的，例如命令归一化、安全门控、JSON 修复、单位换算、传感器事件分级。这些任务并不需要每次都激活完整语言模型。
2. 端侧硬件的真实瓶颈常常是访存、cache miss、算子调度开销和框架负担，而不是峰值 FLOPS。让一个 0.5B 或 1B 模型反复执行稠密路径，可能比小型 deterministic kernel 更慢、更费电、更不稳定。
3. 跨介质或低带宽场景不能传高维张量。水下声学链路、低功耗无线链路和无人节点间的通信更适合传输 skill id、少量标量和状态摘要，而不是传输 hidden state。

因此，本课题的实际问题可以定义为：

> 在资源受限端侧设备上，如何把 LLM 的推理过程拆解为“语义理解/路由”和“技能微内核执行”两层，使可规则化任务绕过稠密大模型路径，同时保留小模型对自然语言输入的鲁棒理解能力？

## 2. 核心思想：从 EigenSkill 到 Hybrid Micro-Kernel

最初构想中的 EigenSkill 包含一个更激进的数学目标：给定某个 skill embedding `e_s`，通过谱正则约束使权重矩阵 `W` 满足：

```text
W e_s ≈ λ e_s
```

若该性质在多层网络中保持，则推理时可以用 `λ e_s` 替代部分矩阵乘，理论复杂度由 `O(d^2)` 降为 `O(d)`。这个方向有明显的数学吸引力，但它会立刻遇到 LayerNorm、SwiGLU、残差混合、attention softmax 等非线性结构。严格的不变子空间证明需要同时约束线性层、归一化层、激活函数和残差连接，目前还没有完成。

因此，本阶段把目标降维为更可落地的系统版本：

```text
输入文本
  -> skill router / prompt contract
  -> 若属于 deterministic skill: C++/parser/SIMD micro-kernel
  -> 若属于 semantic skill: 小模型 merged FP16 或 INT8 path
  -> 输出统一 schema 或 label
```

这样做的关键好处是：不需要先证明完整 Transformer 内部的不变子空间，也能验证“技能旁路能提高可靠性和降低端侧执行负担”这个系统假设。谱约束仍作为下一阶段算法线保留，用于学习低维 skill subspace；系统线则先用 deterministic bypass 和低秩 `U A U^T` microbenchmark 建立可测证据。

## 3. 已完成原型

### 3.1 技能集合

当前训练与评测覆盖 8 个低熵技能：

| Skill | 输出形态 | 端侧意义 |
| --- | --- | --- |
| `intent_routing` | label | 将自然语言路由到聊天、提醒、设备控制等任务 |
| `json_repair` | JSON | 修复工具调用或传输中的坏 JSON |
| `field_extraction` | JSON | 从短文本抽取时间、地点、金额、人物、药品等槽位 |
| `command_normalization` | JSON | 把自然语言命令归一成设备/工具指令 |
| `sensor_event_triage` | label | 对传感器状态做 normal/warning/emergency/ignore 分级 |
| `packet_encode` | JSON | 把 skill 调用封装成低带宽通信包 |
| `safety_gate` | label | 对危险或需要澄清的动作做 allow/block/clarify |
| `unit_time_normalize` | JSON | 对时间、时长和单位换算输出固定 schema |

这些 skill 的选择理由是：输出空间小、评价可自动化、端侧实用性强、容易映射到 micro-kernel，并且能覆盖 EigenSkill 中“路由、协议、执行、安全”的关键链路。

### 3.2 训练配置

- Base model: `HuggingFaceTB/SmolLM2-360M-Instruct`
- 训练方式：LoRA targeted fine-tuning
- LoRA rank: 16
- LoRA alpha: 32
- learning rate: 1.2e-4
- 训练轮数：1.5 epoch
- max length: 512
- gradient checkpointing: enabled
- 每个 skill：900 train + 180 eval
- 总训练样本：7200
- 总评测样本：1440

### 3.3 产物

| 产物 | 路径 | 定位 |
| --- | --- | --- |
| LoRA adapter | `models/eigenskill-smollm2-360m-lora-v2-fp16` | 可继续训练/复现实验 |
| Merged FP16 | `models/eigenskill-smollm2-360m-merged-v2-fp16` | 模型路径主交付物 |
| Dynamic INT8 CPU | `models/eigenskill-smollm2-360m-int8-v2-dynamic` | CPU/端侧初步量化版本 |
| Hybrid CLI | `train_python/run_hybrid_skill.py` | 单条 skill 请求执行 |
| Hybrid eval | `outputs/eigenskill_v2_hybrid_eval_recheck.json` | 旁路可靠性评测 |
| C++ microbenchmark | `inference_cpp/src/eigenskill_bench.cpp` | 低秩 skill path 系统证据 |

## 4. 评测结果与解释

### 4.1 总体结果

| Runtime | Exact | Accuracy | 解释 |
| --- | ---: | ---: | --- |
| 纯模型 v2 | 1391/1440 | 96.60% | LoRA 后大部分低熵 skill 已能稳定生成 |
| Hybrid v2 | 1439/1440 | 99.93% | `unit_time_normalize` 由 deterministic bypass 接管 |

最关键的现象是：纯模型在 7 个技能上接近或达到 100%，但在 `unit_time_normalize` 上只有 73.33%。失败样例包括输出 `1500g`、`2cm`、自然语言解释或不完整 JSON。这说明小模型即使被强 prompt 和 LoRA 约束，仍会把“单位换算”当成语言常识问答，而不是严格 schema 转换。对于端侧系统来说，这类任务不应继续依赖 LLM 生成，而应交给 deterministic micro-kernel。

### 4.2 Hybrid 的意义

Hybrid runtime 对 `unit_time_normalize` 做了 180 次旁路覆盖，使该 skill 从 73.33% 提升到 100.00%。这不是“模型能力突然变强”，而是系统设计把错误类型移出了模型路径。它说明 EigenSkill 的早期工程方向应该是：

1. 让 LLM 处理语义歧义、槽位抽取和路由；
2. 让 micro-kernel 处理可规则化、可枚举、可证明的转换；
3. 用统一 schema 把两种路径封装成同一推理接口；
4. 在端侧 runtime 中根据 skill id 做动态路径选择。

这比单纯继续增加 LoRA 数据更可解释、更稳定，也更适合写系统论文。

## 5. C++ 系统原型

当前 C++ 端已经实现一个独立 microbenchmark，不依赖 llama.cpp、RKNN、ExecuTorch 或 CUDA。它对比两条路径：

```text
dense path: y = W x
skill path: z = U^T x; z2 = A z; y = U z2
```

其中 dense path 复杂度为 `O(d^2)`，低秩 skill path 复杂度为 `O(dk + k^2 + dk)`，当 `k << d` 时近似为 `O(dk)`。当前 benchmark 使用合成矩阵 `W = U A U^T`，因此低秩路径在数学上等价于 dense path，误差主要来自浮点累积。这个实验测的是 best-case systems ceiling，不能直接代表任意 Transformer 权重都可以低秩替代。

下一步应把 Python parser 里的 `unit_time_normalize` 迁移到 C++，形成第一个真实 deterministic bypass micro-kernel；再把低秩 skill path 和实际 LoRA 权重/hidden activation 做拟合实验。

## 6. 数学路线：谱约束应如何收敛

完整 Eigen-Regularization 可以从单向量约束推广到子空间约束。设某一层权重为 `W_l`，skill 子空间基为 `E_s ∈ R^{d×k}`，列向量正交，即 `E_s^T E_s = I`。希望该层在 skill 子空间上近似闭合：

```text
W_l E_s ≈ E_s A_{l,s}
```

其中 `A_{l,s} ∈ R^{k×k}` 是低维 skill dynamics。对应正则项可以写成：

```text
L_eigen = Σ_{l∈L} ||(I - E_s E_s^T) W_l E_s||_F^2
```

它惩罚 `W_l E_s` 泄漏到 skill 子空间外。若希望同时控制子空间内的动力学，可加入：

```text
L_dyn = Σ_{l∈L} ||E_s^T W_l E_s - A_{l,s}||_F^2
```

训练目标为：

```text
L = L_task + α L_eigen + β L_orth + γ L_dyn + δ L_distill
```

其中：

- `L_task` 是原始监督损失；
- `L_orth = ||E_s^T E_s - I||_F^2` 保持 skill basis 正交；
- `L_distill` 可约束旁路输出与原模型/教师模型一致；
- `α, β, γ, δ` 通过消融实验决定。

非线性穿透问题不能被单层谱约束自动解决。更合理的办法是设计一条显式 linear bypass channel：在每个 block 的残差路径中维护一个 skill state `h_s`，只让它经过线性/低秩变换，并在 block 输出处与普通 hidden state 融合：

```text
h_{l+1} = TransformerBlock_l(h_l) + G_l(h_l, s) B_l h_s
h_{s,l+1} = A_{l,s} h_{s,l}
```

其中 `G_l` 是门控标量或小维向量，`B_l` 是把 skill state 注入主 hidden space 的投影。这样可以把数学证明对象从“整个 Transformer 非线性系统”收敛为“显式线性旁路子系统”，难度显著降低，也更符合系统实现。

## 7. 投稿定位

### 7.1 最适合的近期路线

当前最现实的路线不是主会冲顶，而是先形成“系统+实验”的 workshop/中文导师认可版本，再扩展为期刊或主会：

1. **近期 2-4 周**：技术报告 + arXiv/预印本 + GitHub artifact。目标是吸引合作者。
2. **近期 4-8 周**：补 C++ bypass latency、INT8/FP16 对比、llama.cpp/ONNX/ExecuTorch baseline、真实端侧设备测试。目标是 workshop 或系统短文。
3. **中期 2-4 个月**：扩展到多模型、多任务、多设备，补能耗和 memory bandwidth，形成 TECS/JSA/IoTJ 级别期刊稿。
4. **长期 6 个月以上**：若谱约束与低秩路径能在真实 Transformer 层中稳定工作，再考虑 ASPLOS/MLSys 主会。

### 7.2 候选 venues

| Venue | 当前匹配度 | 适合版本 | 缺口 |
| --- | --- | --- | --- |
| Journal of Systems Architecture | 高 | 端侧 skill runtime + C++ micro-kernel | 需要真实设备 latency/energy |
| ACM TECS | 高 | 嵌入式 LLM 技能微内核 | 需要嵌入式平台评测 |
| IEEE Internet of Things Journal | 中高 | AIoT skill runtime + 协议/安全 | 需要 IoT 场景和网络实验 |
| Elsevier Internet of Things | 中高 | 跨介质/AIoT 架构扩展 | 需要系统场景和应用验证 |
| ACM TCPS/TOSN | 中 | swarm/cyber-physical 架构 | 需要真实传感器/通信实验 |
| MLSys | 中 | ML + system co-design | 需要更强 baseline 和端到端系统 |
| ASPLOS | 中低但可作为长期目标 | runtime/compiler/architecture 交叉强稿 | 需要硬件、OS、编译器层实质贡献 |
| NeurIPS/ICLR workshop or TMLR | 中 | 谱约束/路由算法 | 需要数学消融和泛化实验 |

## 8. 当前局限

1. 数据集是可控合成/半合成任务，还没有真实用户日志或公开 benchmark。
2. 评测指标主要是 exact match，缺少 latency、energy、memory bandwidth 和 tail latency。
3. C++ benchmark 目前是合成低秩 best-case，尚未和真实模型权重打通。
4. 谱约束理论仍停留在设计阶段，没有完成跨 LayerNorm/SwiGLU 的证明。
5. 跨介质 swarm、水声通信、磁吸总线等是远景架构，没有硬件实验，论文中必须作为 future work 或 architecture proposal。

## 9. 下一阶段实验计划

### 第 1 周：把当前结果整理成可展示 artifact

- 产出可运行 CLI：`eigenskill run --skill unit_time_normalize --input ...`
- 固化模型包 manifest 和 eval report。
- 把 deterministic parser 迁移到 C++，最少支持时间、时长、质量、长度换算。
- 在 Windows/WSL CPU 上跑 latency 对比：LLM path vs parser path。

### 第 2-3 周：端侧系统证据

- 选择 2-3 个 baseline：纯 merged FP16、dynamic INT8、规则 parser、hybrid runtime。
- 指标：平均延迟、P95/P99、峰值内存、模型加载时间、吞吐、失败率。
- 若硬件可用，优先测试 RK3588 / ARM CPU；如果暂时不可用，先用本机 CPU + NVIDIA GPU 做模拟。

### 第 4-6 周：算法线补强

- 对 `intent_routing` 做 hard-negative patch，解决最后 1 个误判。
- 在 hidden states 上拟合 skill subspace，尝试 PCA/SVD/CCA，验证 skill prompt 是否形成可分子空间。
- 加入 `L_eigen` 的小规模训练消融：无正则、单向量正则、子空间正则、distill 正则。

### 第 7-8 周：论文线

- 写系统短文：Hybrid micro-kernel runtime。
- 写架构报告：Cross-medium distributed skill swarm 作为 vision。
- 准备开源最小包：数据生成脚本、评测脚本、模型 manifest、C++ benchmark。

## 10. 对导师可说的核心贡献

1. 提出端侧 LLM 技能化混合推理框架，把低熵任务从稠密模型路径中旁路出去。
2. 构建 8-skill 小模型训练与评测管线，完成 LoRA、merged FP16、dynamic INT8 导出。
3. 证明在当前 controlled dataset 上，hybrid runtime 能将 exact accuracy 从 96.60% 提升到 99.93%。
4. 识别出小模型在单位/时间标准化上的系统性失败模式，并用 deterministic micro-kernel 给出工程解决方案。
5. 搭建 C++ 低秩 skill path microbenchmark，为后续系统性能论文提供第一块证据。
6. 给出谱约束与线性旁路通道的后续数学路线，避免直接陷入完整非线性 Transformer 证明。

## 11. 建议导师反馈点

请导师重点判断三件事：

1. 论文主线是否应该先走系统工程，即 hybrid micro-kernel runtime，而不是先走谱约束理论。
2. 目标 venue 应先投 embedded/IoT/systems 期刊，还是先投 workshop/预印本吸引合作者。
3. 下一阶段是否能提供或借用端侧硬件平台，例如 RK3588、Jetson、ARM 开发板或国产 NPU。

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
