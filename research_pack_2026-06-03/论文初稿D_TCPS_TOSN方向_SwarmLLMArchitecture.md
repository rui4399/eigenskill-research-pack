# Paper Draft D - Swarm/CPS Architecture Track

## Working Title

Cross-Medium Distributed Micro-Kernel Swarm LLMs: A Vision for Low-Bandwidth Cyber-Physical Skill Assembly

## Target Venues

ACM TCPS, ACM TOSN, Elsevier Internet of Things, IoT/CPS workshops.

## Abstract

Future AIoT systems may span air, ground, and underwater environments where radio links are intermittent, acoustic communication is low bandwidth, and physical docking may be required for high-bandwidth exchange. We propose a cross-medium distributed micro-kernel swarm architecture in which each node stores a small skill dictionary and executes bounded LLM-derived skills locally. Instead of transmitting hidden states or model parameters, nodes exchange compact skill identifiers, scalar parameters, safety states, and authentication tags. When high-bandwidth coordination is required, nodes can physically assemble through a wired or magnetic bus. This paper frames the architecture, threat model, and research agenda. The current EigenSkill prototype validates only the skill-runtime layer on controlled data; the cross-medium physical swarm remains future work.

## 1. Vision

The central vision is to replace a monolithic edge model with a swarm of small skill executors. Each node owns:

- a local skill dictionary;
- a small semantic router or command interface;
- deterministic micro-kernels for bounded tasks;
- a compact packet encoder;
- a safety gate;
- optional physical docking interface.

## 2. Cross-Medium Communication

In underwater or low-power links, bandwidth is too limited for tensor exchange. The proposed protocol transmits:

```text
{Skill ID, arguments, precision policy, auth tag, timestamp}
```

The receiving node reconstructs the operation using its local skill dictionary. This is closer to distributed procedure calls than tensor parallelism.

## 3. Morphological Assembly

When the system requires high-bandwidth coordination, nodes may physically dock and switch from wireless/acoustic links to SPI/CAN/UART-like buses. This part is speculative and requires mechanical, electrical, and control-system validation.

## 4. Security

The system should authenticate skill packets before executing physical actions. A lightweight construction can include:

```text
auth = MAC(timestamp || skill_id || args || nonce)
```

ChaCha20-Poly1305 is a reasonable candidate for authenticated encryption on constrained devices, but the exact security implementation must be validated against platform constraints.

## 5. Current Evidence

Current EigenSkill evidence covers:

- eight skill definitions;
- LoRA fine-tuning over a 360M model;
- 96.60% pure-model exact match;
- 99.93% hybrid exact match;
- deterministic bypass for `unit_time_normalize`;
- C++ low-rank microbenchmark.

It does not yet cover:

- water acoustic communication;
- magnetic docking;
- multi-node physical assembly;
- real swarm coordination;
- power/energy measurements.

## 6. Research Plan

1. Simulate 10-50 nodes with low-bandwidth packet exchange.
2. Implement packet authentication.
3. Deploy two or three physical nodes with sensor triage and safety gate.
4. Measure communication savings against text/tool-call baselines.
5. Add physical docking only after software protocol stabilizes.

## 7. Positioning

This paper should be written as a vision or architecture proposal, not as a completed systems paper. The honest contribution is the architecture and the path from skill micro-kernels to distributed cyber-physical execution.

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
