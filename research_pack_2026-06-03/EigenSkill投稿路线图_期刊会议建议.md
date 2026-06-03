# EigenSkill 投稿路线图与期刊/会议建议

日期：2026-06-03

## 总体判断

EigenSkill 当前更像一个“有初步模型包和系统原型的研究方向”，还不是完整主会论文。最强证据是 hybrid runtime 在 8-skill controlled evaluation 上达到 99.93% exact，并且明确暴露了 LLM 不适合处理 deterministic unit/time normalization 的系统性失败。最弱证据是谱约束理论和跨介质 swarm 架构尚未实证。

因此路线应分层：

| 层级 | 目标 | 适合 venue |
| --- | --- | --- |
| 快速展示 | 技术报告、预印本、workshop、导师组会 | arXiv、MLSys/NeurIPS workshop、AIMLSystems workshop/track |
| 稳妥投稿 | 端侧系统、嵌入式 runtime、IoT 技能执行 | JSA、ACM TECS、IEEE IoTJ、Elsevier Internet of Things |
| 长期冲顶 | 算法-系统-硬件协同、runtime/compiler/architecture | MLSys、ASPLOS、ISCA/MLArchSys、TACO |

## 推荐优先级

### 1. Journal of Systems Architecture

匹配度：高。

理由：JSA 明确覆盖 embedded systems、system software、programming languages、mobile systems、parallel/distributed architectures 等方向。EigenSkill 的 C++ micro-kernel、端侧 runtime、INT8/FP16 导出和低秩 path 都可以组织成系统架构论文。

建议题目：

> EigenSkill: A Hybrid Micro-Kernel Runtime for Skill-Specialized Edge Language Model Inference

需要补的实验：

- CPU/GPU/ARM latency；
- parser bypass vs LLM generation latency；
- dynamic INT8 vs FP16；
- memory footprint；
- 至少一个端侧板卡；
- 与 llama.cpp/ONNX Runtime/ExecuTorch 的 baseline 对比。

### 2. ACM Transactions on Embedded Computing Systems

匹配度：高。

理由：TECS 关注嵌入式计算系统。若把论文主线收敛为“嵌入式设备上的技能微内核 + 小模型路由 + 混合精度执行”，它比纯算法 venue 更合适。

建议题目：

> Skill-Specialized Hybrid Inference for Embedded Language Models

需要补的实验：

- 嵌入式平台：RK3588、Jetson、RISC-V/ARM CPU 至少一类；
- 功耗或 energy proxy；
- cold start / warm start；
- micro-kernel branch overhead；
- 真实 AIoT 命令样本。

### 3. IEEE Internet of Things Journal

匹配度：中高。

理由：如果强调 AIoT、低带宽 packet encode、安全门控、传感器事件分级、边缘节点协作，IoTJ 会比较自然。它要求应用场景和网络/设备证据更强，而不是只展示模型精度。

建议题目：

> Hybrid Skill Micro-Kernels for Reliable and Low-Bandwidth LLM Inference in Edge IoT

需要补的实验：

- IoT 场景：传感器异常、智能家居/无人节点命令、低带宽通信；
- 通信负载：JSON/skill packet 的字节数对比；
- 安全门控误判/漏判；
- 多节点模拟或真实节点实验。

### 4. Elsevier Internet of Things

匹配度：中高。

理由：适合把“跨介质分布式微内核群体大模型”作为 IoT/CPS 架构论文展开。该版本应弱化顶会算法口吻，强调工程架构、协议、边缘智能和应用边界。

风险：如果没有真实跨介质硬件实验，就只能作为 architecture/position 或 concept paper，不能写成完整系统验证。

### 5. ACM TCPS / ACM TOSN

匹配度：中。

理由：TCPS/TOSN 适合 cyber-physical systems、sensor networks、多节点协作、物理世界反馈闭环。但当前 EigenSkill 的硬件和通信实验还没完成。

适合版本：

> Morphological Skill Swarms: A Cyber-Physical Architecture for Low-Bandwidth Edge LLM Coordination

需要补：

- 传感器网络模拟；
- 低带宽链路；
- 拓扑变化；
- 故障恢复；
- 安全鉴权；
- 至少一个 physical-in-the-loop demo。

### 6. MLSys

匹配度：中，作为中长期目标。

理由：MLSys 关注 ML 与系统交叉。EigenSkill 如果补齐 runtime、artifact、端到端 benchmark 和严谨 baseline，可以投。当前证据还偏小。

必须补：

- 不止一个基座模型；
- 不止一个数据集；
- 与现有 inference framework 的公平对比；
- 训练成本、推理成本、可复现 artifact；
- ablation：无 bypass、规则全接管、LLM-only、hybrid、低秩 path。

### 7. ASPLOS

匹配度：中低但可作为长期冲顶。

理由：ASPLOS 官方 scope 覆盖 architecture、programming languages、operating systems 及其交叉，也覆盖 mobile/edge systems、ML systems、embedded/real-time systems。EigenSkill 的长期版本如果能变成 runtime/compiler/hardware co-design，会有想象空间。

当前不建议直接投主会，因为缺少：

- 真正硬件/编译器/OS 层贡献；
- 大规模系统评测；
- 和现有框架的强 baseline；
- 对 irregular skill path 的调度、cache、branch、tiling 的实测；
- artifact evaluation 级别复现。

## 国内中文期刊路线

如果目标是先获得导师认可和国内学术输出，可考虑：

| 期刊 | 适合角度 | 难度 |
| --- | --- | --- |
| 《软件学报》 | 端侧 LLM 推理框架、系统软件、模型压缩与运行时 | 高 |
| 《计算机研究与发展》 | 算法-系统协同、边缘智能、体系结构 | 高 |
| 《计算机学报》 | 更偏完整理论或系统创新 | 高 |
| 《电子学报》 | 嵌入式系统、边缘 AI、硬件协同 | 中高 |
| 《通信学报》 | 跨介质/低带宽群体智能通信协议 | 中高 |
| 《小型微型计算机系统》 | 原型系统与工程验证 | 中 |

国内路线的优势是导师沟通和中文论证更顺；劣势是需要按期刊格式、参考文献和实验完整性重新组织。

## 建议发文拆分

### Paper A：系统主线

核心：Hybrid skill micro-kernel runtime。

投向：JSA / TECS / MLSys workshop。

当前最成熟，应该优先推进。

### Paper B：IoT 应用线

核心：低带宽 AIoT skill packet、sensor triage、safety gate。

投向：IEEE IoTJ / Elsevier Internet of Things。

需要补通信和设备实验。

### Paper C：算法理论线

核心：Eigen-Regularization、skill subspace、linear bypass channel。

投向：NeurIPS/ICLR workshop、TMLR 后续。

需要补数学和消融，不要现在强投正刊。

### Paper D：群体架构线

核心：cross-medium distributed micro-kernel swarm。

投向：TCPS/TOSN/IoT architecture special issue。

只能作为 vision/architecture paper，不能把未完成硬件写成已完成结果。

## 近期最优行动

1. 先给导师发“阶段性科研报告 + 投稿路线图”。
2. 让导师帮忙确定：系统期刊先行，还是 workshop 快速曝光。
3. 两周内补 C++ deterministic bypass latency。
4. 一个月内补端侧设备或至少 CPU/GPU baseline。
5. 三个月内把 Paper A 做成可投稿稿。

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
