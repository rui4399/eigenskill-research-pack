# Wake-up Summary: Qwen3-1.7B C4-128 GPU-Filling Run

瑞，按你说的“多用 GPU，但显存别超过 85%”，我做了一个更贴近上限的实验。

## What Worked

Qwen3-1.7B 在 C4-128 上跑通了一个轻量 random4 对比：

```text
FP16              29.4065
uniform INT4      35.7923
consensus         32.8806
category          34.1947
random4 min/mean/max 33.2734 / 34.5656 / 35.1416
```

Consensus 胜出：

- vs uniform INT4: +2.9117 PPL
- vs category: +1.3141 PPL
- vs best random4: +0.3928 PPL
- random win/loss/tie: 4 / 0 / 0

## GPU

有效 run 峰值：

```text
6884 / 8151 MiB = 84.46%
max GPU util = 74%
guard = pass
```

这基本已经贴着 85% 显存线跑了。

## What Failed Usefully

完整 random16 的 C4-128 两次被 guard 杀掉：

- max_length 128: 86.28%
- max_length 96: 86.31%

所以后面要做 C4-128 random16，不能直接一口气跑完整配置，应该改成分批 sequential config 或 chunked evaluator。

## Code Fix

C++ `quant_random_baseline_audit` 已修，能同时识别：

- `random_seed_*`
- `random_budget_seed_*`

这避免为了结果命名重复浪费 GPU。
