# EigenSkill-Q 2026-06-05 公开仓库与阶段进展更新

## 公开仓库

- GitHub: https://github.com/rui4399/eigenskill-research-pack
- 当前公开状态: `PUBLIC`, `isPrivate=false`
- 当前远端 `main`: `4c933e28edc6c88733314d5d3b86705bbd34d436`
- 最新提交: `4c933e2 Add task eval smoke pipeline`
- 外部访问检查: unauthenticated HTTP `200 OK`

如果浏览器里仍显示不可见，优先排查 GitHub App/浏览器缓存、登录账号切换或移动端客户端缓存；仓库服务端状态已经是公开。

## 研究叙事收敛

当前版本不再把 EigenSkill-Q 包装成“新量化器”，而是收敛为:

```text
Calibration Split Instability (CSI)
+ conservative cross-dataset consensus allocation diagnostics
```

核心问题定义变为: 现有混合精度量化通常默认校准集可靠，但短校准切分会导致模块敏感度排序高度不稳定，从而使 bit allocation 在分布迁移下不可靠。因此，先测量校准分割不稳定性，再使用保守的跨数据集共识分配，比单一校准集排序更适合作为论文主线。

## 已完成的新证据

### 1. Qwen3-1.7B C4-128 random16 完成

在 85% 显存上限下，原始 `--reuse-model` 方案被杀在:

```text
6936 / 8151 MiB = 85.09%
```

后续改为低显存 chunked 运行，不复用模型进程，完成 16 个随机种子审计。峰值显存:

```text
batch0: 6884 / 8151 MiB = 84.46%
batch1: 5538 / 8151 MiB = 67.94%
batch2: 5546 / 8151 MiB = 68.04%
batch3: 5538 / 8151 MiB = 67.94%
```

结果:

| Dataset | FP16 | uniform INT4 | consensus | category | random min/mean/max |
|---|---:|---:|---:|---:|---:|
| C4-128 | 29.4065 | 35.7923 | 32.8806 | 34.1947 | 33.1374 / 34.3623 / 35.1416 |

边际:

- consensus vs uniform INT4: +2.9117 PPL
- consensus vs category: +1.3141 PPL
- consensus vs best random16: +0.2568 PPL
- consensus vs random16 mean: +1.4817 PPL
- random seed audit: 16 wins / 0 losses / 0 ties

### 2. CSI C++ 诊断工具完成

`quant_sensitivity_stability` 现在可以输出 Markdown/CSV/JSON，并包含 CSI 指标:

- positive-set instability
- sign instability
- score-rank instability
- mean top-k Jaccard
- top-k instability
- scalar CSI

OLMo2 WikiText2 vs C4 的当前 CSI:

```text
positive_set_instability: 0.5488
sign_instability:         0.3982
score_rank_instability:   0.4078
mean_topk_jaccard:        0.1640
topk_instability:         0.8360
CSI:                      0.5477
```

解释: top-k 共识很弱，单一校准集排序不能直接被当作可靠量化证据。这支持把论文主线从“提出一个简单平均策略”改成“校准分割不稳定性的系统诊断与鲁棒分配”。

### 3. 任务评估 smoke 管线完成

新增了 PPL 之外的最小任务评估接口:

```text
data_eval/task_prompts/quant_task_smoke.jsonl
train_python/eval_task_jsonl.py
inference_cpp/src/quant_task_eval_summary.cpp
inference_cpp/testdata/task_eval_fixture.json
```

Qwen3-0.6B smoke 结果:

```text
total: 5
exact: 3
accuracy: 0.6000
gsm8k_smoke: 1/2
mmlu_smoke: 2/2
ifeval_smoke: 0/1
GPU peak: 3048/8151 MiB = 37.39%
```

这不是正式 benchmark，只是验证评估链路能跑通。下一步必须把它接到真实 MMLU/GSM8K/IFEval 小子集，并比较 FP16、uniform INT4、consensus allocation 的能力保留。

## 目前短板

- 还没有 GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant 等 SOTA 对照。
- 任务评估仍是 smoke，不足以支撑 CCF-A/顶会主张。
- 最大模型仍停在 1.7B 级别，后续至少要补 3B/7B 级别的可行性或解释硬件边界。
- 当前贡献更像 calibration robustness paper，而不是 quantization algorithm paper。

## 下一步优先级

1. 不再继续堆随机种子，把精力转到真实任务子集。
2. 为 AWQ/GPTQ/QuaRot 类方法预留统一评估入口。
3. 把 CSI 写成正式定义: 排名方差、top-k 不稳定性、分布迁移下的 regret。
4. 用 3B 级别模型做显存受控试探，仍保持 85% 上限。
5. 论文目标从 NeurIPS/MLSys 的量化算法叙事，改为更清晰的模型压缩/鲁棒校准/AI 系统诊断方向。

## 本次验证命令

```text
ctest --test-dir build/cpp-wsl --output-on-failure
python3 -m py_compile train_python/eval_task_jsonl.py
gh repo view rui4399/eigenskill-research-pack --json nameWithOwner,visibility,url,isPrivate
curl -I -L https://github.com/rui4399/eigenskill-research-pack
```

已确认 C++ 测试通过、Python smoke evaluator 可编译、GitHub 仓库公开可访问。
