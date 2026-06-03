# EigenSkill-Q 阶段增补：逐模块 Loss-Sensitive 量化分配

日期：2026-06-04

## 一句话结论

本阶段已把 EigenSkill-Q 从“激活统计 proxy 的负结果”推进到“逐模块
loss sensitivity 的正结果”。在 SmolLM2-360M-Instruct 上，group-wise fake
quant 的 `{4,8}` 混合精度分配把 8-prompt PPL 从 uniform INT4 的 `272.18`
降到 `212.69`，并明显优于此前 activation-stat RD allocation 的 `292.01`。

这不是最终量化器，但它是目前最值得写进论文主线的实验证据。

## 实验设计

目标是验证一个更强的 bit allocation 信号：

```text
对每个 Linear 模块：
1. 保存原始权重；
2. 只把该模块权重量化为 group-wise INT4；
3. 在短 prompt 校准集上计算 next-token NLL；
4. 恢复原始权重；
5. 记录 delta NLL / parameter cost。
```

然后在 4.5 weighted average bits 预算下，把 8-bit 精度分配给最敏感的模块：

```text
base bits:          4
high bits:          8
Linear modules:     225
selected 8-bit:     53
remaining 4-bit:    172
weighted avg bits:  4.4993
```

对应实现：

```text
train_python/measure_module_quant_sensitivity.py
```

## 关键结果

逐模块敏感度探测：

```text
model:                       HuggingFaceTB/SmolLM2-360M-Instruct
probe prompts:               4
max length:                  128
group size:                  128
positive delta NLL total:    1.5635
protected positive delta:    0.9042
protected ratio:             57.83%
```

PPL 对比，8 prompts，max length 160，group size 128：

| method | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---|
| FP16 | 179.14 | 0.0000 | 16:225 |
| uniform INT4 | 272.18 | 0.4183 | 4:225 |
| activation-stat RD 4/8 | 292.01 | 0.4886 | 4:172, 8:53 |
| loss-sensitive 4/8 | 212.69 | 0.1717 | 4:172, 8:53 |

相对改进：

```text
vs uniform INT4:
PPL       272.18 -> 212.69
delta NLL 0.4183 -> 0.1717

vs activation-stat RD:
PPL       292.01 -> 212.69
delta NLL 0.4886 -> 0.1717
```

公共数据集切片补充，WikiText2 validation 32 prompts，max length 160，
group size 128：

| method | PPL | delta NLL vs FP16 | bit histogram |
|---|---:|---:|---|
| FP16 | 18.24 | 0.0000 | 16:225 |
| uniform INT4 | 30.26 | 0.5062 | 4:225 |
| uniform INT3 | 1678.70 | 4.5221 | 3:225 |
| loss-sensitive 4/8 | 25.92 | 0.3514 | 4:172, 8:53 |

这个结果说明正向趋势不仅存在于手写 prompt，在公开文本切片上也成立：

```text
PPL       30.26 -> 25.92
delta NLL 0.5062 -> 0.3514
```

## 对论文主线的意义

此前 activation-stat sensitivity proxy 在 group-wise quantization 下输给
uniform INT4，说明“只看激活统计”不足以支撑顶会/一区级别量化论文。

本次结果说明更可信的主线应改成：

```text
Measured perturbation sensitivity under resource-constrained mixed-precision
LLM quantization.
```

也就是把每层/每模块的量化选择视为受预算约束的组合优化问题，用实际
loss perturbation、Fisher/Hessian proxy 或 activation reconstruction error
估计 `D_l(b_l)`，再做 bit allocation。

当前证据支持的叙事是：

1. deterministic C++ policy kernel 能保证策略执行可验证；
2. naive activation proxy 会失败；
3. measured loss sensitivity 能显著改善 `{4,8}` 混合精度分配；
4. 后续用 Fisher/Hessian、GPTQ/AWQ/SmoothQuant/rotation baseline 补齐后，
   才有国际会议/期刊投稿的可信度。

## 不能夸大的地方

- 这仍然是 fake quant：权重量化后又 dequantize 回浮点运行。
- 不能声称已有真实显存、延迟或能耗下降。
- 不能声称超过 GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant。
- 不能把这个结果解释成 eigen-routing 或 `O(d)` Transformer 推理已经成立。
- 当前 PPL 集仍是 8 条手写 prompt，不是 WikiText2/C4 标准切片。

## 下一步

1. 用 WikiText2/C4 小切片替代 8 条 prompt。
2. 重复不同 calibration set，报告 variance。
3. 比较三种 sensitivity：
   - measured one-module loss delta；
   - Fisher/Hessian proxy；
   - activation reconstruction error after fake quantization。
4. 接入 GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant baseline。
5. 只有在真实压缩权重格式或 quantized runtime 里运行后，再报告内存和延迟。

## 证据文件

```text
outputs/smollm2_module_loss_sensitivity_limit4_group128.json
outputs/smollm2_module_loss_sensitivity_limit4_group128_report.md
outputs/smollm2_loss_sensitive_alloc_4to8_limit4_group128_summary.json
outputs/smollm2_fake_quant_ppl_loss_sensitive_4to8_group128_limit8_summary.json
data_eval/text_prompts/wikitext2_validation_32.txt
outputs/smollm2_fake_quant_ppl_loss_sensitive_4to8_group128_wikitext2_32_summary.json
outputs/smollm2_fake_quant_ppl_report.md
```
