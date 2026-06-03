# EigenSkill v2 Delivery Status

更新时间：2026-06-03

## 已完成

- v2 targeted LoRA 训练完成。
- merged FP16 模型已导出。
- dynamic INT8 CPU 模型已导出。
- 纯模型评测完成：1391/1440 exact，overall exact = 96.60%。
- hybrid runtime 评测完成：1439/1440 exact，overall exact = 99.93%。
- 新增 `train_python/run_hybrid_skill.py` 单条技能调用 CLI。
- `unit_time_normalize` deterministic bypass CLI 已验证，启动约 0.12s。
- merged FP16 模型单条调用已验证：`intent_routing("打开客厅灯") -> device_control`。
- 新增 `train_python/verify_v2_package.py` 模型包完整性验证脚本。
- `python3 train_python/verify_v2_package.py` 已通过，输出 `package_ok=true`、`missing_files=[]`。
- GPU 当前无训练任务占用；WSL 中可见 RTX 5070 Laptop GPU，约 2855 MiB used / 5037 MiB free / 1% utilization。

## 模型包

- `models/eigenskill-smollm2-360m-lora-v2-fp16`
- `models/eigenskill-smollm2-360m-merged-v2-fp16`
- `models/eigenskill-smollm2-360m-int8-v2-dynamic`

## 报告与评测

- `outputs/EigenSkill-v2-Hybrid-Training-Report.md`
- `outputs/EigenSkill-v2-Notion-Summary.md`
- `outputs/eigenskill_v2_eval.json`
- `outputs/eigenskill_v2_hybrid_eval.json`
- `outputs/eigenskill_v2_hybrid_eval_recheck.json`
- `outputs/eigenskill_v2_package_manifest.json`
- `train_python/run_hybrid_skill.py`
- `train_python/verify_v2_package.py`

## 关键结论

- 纯 LLM 已能稳定处理大部分结构化技能。
- `unit_time_normalize` 纯模型仍是短板，exact = 73.33%。
- 将单位/时间换算放入 deterministic bypass micro-kernel 后，hybrid runtime 达到 99.93%。
- 这更符合 EigenSkill 的系统协同设计方向：LLM 负责语义技能，确定性技能走旁路内核。

## Notion 状态

- `codex mcp list` 已确认 Notion 为 `enabled / OAuth`。
- 当前 Codex 会话的 `tool_search notion` 返回 0，Notion 写入工具没有热加载进当前工具列表。
- 2026-06-03 再次检查：`tool_search notion-create-pages/notion-update-page` 仍未暴露 Notion 写入工具。
- 2026-06-03 第三轮检查：`codex mcp get notion` 显示 `enabled=true`、`transport=streamable_http`、`url=https://mcp.notion.com/mcp`；`codex mcp list` 显示 Notion `enabled / OAuth`；但 `tool_search notion notion-create-pages notion-update-page notion-search notion-fetch` 仍只返回 GitHub/Neon/Playwright/HeyGen 等无关工具，没有 Notion 命名空间。
- 重启后补充检查：本机已安装 Notion 桌面端，注册表显示 `Notion 7.19.0 / Notion Labs, Inc`；但桌面端安装不等于 Codex connector/API 写入工具可用。尝试安装 Notion connector 返回 `user_confirmed=true`、`completed=false`，当前工具列表仍未出现 Notion 写入工具。
- 因此本轮未能可靠创建/更新 Notion 页面。
- 下一次继续时，重启或刷新 Codex Desktop 后直接让 Codex 写入：
  - `outputs/EigenSkill-v2-Notion-Summary.md`
  - 可追加 `outputs/EigenSkill-v2-Hybrid-Training-Report.md`
