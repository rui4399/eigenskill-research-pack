# Paper Draft C - Algorithm/Theory Track

## Working Title

Eigen-Regularized Skill Subspaces for Language Model Routing: A Preliminary Study

## Target Venues

NeurIPS/ICLR workshop, TMLR after broader evidence, ML systems workshop.

## Abstract

We study whether skill-specific behavior in compact language models can be organized into low-dimensional invariant subspaces. The motivating idea is to regularize selected Transformer layers so that a skill vector or skill subspace remains stable under the layer map, enabling cheaper inference paths for bounded tasks. We formalize an eigen-regularization objective based on subspace leakage, discuss why nonlinear components such as LayerNorm, attention softmax, and SwiGLU prevent a naive eigenvector argument, and propose an explicit linear bypass channel as a more tractable alternative. A small empirical prototype over eight controlled skills demonstrates the practicality of hybrid skill routing, but does not yet prove nonlinear invariance.

## 1. Problem

The naive EigenSkill claim is:

```text
W e_s ≈ λ e_s
```

If this held through the network, skill inference could replace dense matrix multiplication with cheaper scalar or low-rank operations. However, a Transformer block is not a single linear map. It includes normalization, attention, nonlinear activation, residual mixing, and often gated FFN structures. Therefore, eigenvector alignment in one linear layer is insufficient.

## 2. Subspace Formulation

Let `E_s ∈ R^{d×k}` be a skill basis. Instead of constraining one vector, constrain the image of the subspace:

```text
W_l E_s ≈ E_s A_{l,s}
```

The leakage objective is:

```text
L_leak = Σ_l ||(I - E_s E_s^T) W_l E_s||_F^2
```

The orthogonality objective is:

```text
L_orth = ||E_s^T E_s - I||_F^2
```

The low-dimensional dynamics objective is:

```text
L_dyn = Σ_l ||E_s^T W_l E_s - A_{l,s}||_F^2
```

The full objective is:

```text
L = L_task + α L_leak + β L_orth + γ L_dyn + δ L_distill
```

## 3. Nonlinear Obstruction

LayerNorm changes direction based on mean and variance. SwiGLU gates dimensions multiplicatively. Attention softmax creates data-dependent mixing across tokens. Therefore, even if `W_l E_s` lies inside the skill subspace, the next nonlinear operation may rotate or destroy that subspace.

This implies two possible strategies:

1. Weaken the theorem: only claim approximate local invariance on observed activation distributions.
2. Change the architecture: introduce an explicit linear bypass channel whose dynamics are controlled.

## 4. Linear Bypass Channel

We propose maintaining a separate skill state:

```text
h_{s,l+1} = A_{l,s} h_{s,l}
h_{l+1} = F_l(h_l) + G_l(h_l,s) B_l h_{s,l+1}
```

Here `F_l` is the ordinary Transformer block. The skill state evolves linearly, while a gate `G_l` controls injection into the main hidden state. This converts the theory target from full-network invariance to subsystem invariance.

## 5. Empirical Starting Point

The current prototype does not yet train `L_leak`. It trains a LoRA model over eight skills and shows that a hybrid runtime reaches 99.93% exact match. This supports the system motivation but should be described as preliminary evidence, not as a proof of eigen-routing.

## 6. Required Experiments

- Collect hidden states for each skill prompt.
- Test whether skill clusters are linearly separable.
- Fit PCA/SVD/CCA subspaces per skill.
- Add `L_leak` in LoRA training.
- Compare no regularization vs vector regularization vs subspace regularization.
- Measure whether subspace leakage correlates with runtime bypass success.

## 7. Conclusion

The strict eigenvector version is mathematically fragile under Transformer nonlinearities. The more defensible route is subspace leakage regularization plus an explicit linear bypass channel.

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
