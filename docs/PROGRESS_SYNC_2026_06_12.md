# EigenSkill-Q Progress Sync 2026-06-12

This file is the current single-page progress map. It consolidates the latest
local search, codegraph status, evidence outputs, draft status, and next
experiment queue. It is a coordination artifact; paper claims still follow
`docs/PAPER_CLAIM_MATRIX.md`.

## Current Repository State

- branch: `codex/eigenskill-q-system-evidence`
- latest checked commits:
  - `38e7417` Add paper-ready CSI cross-scale artifacts
  - `0b766af` Add Qwen2.5 CSI cross-scale comparison
  - `f360176` Promote Qwen2.5 1.5B CSI gates to ledger
  - `18bc585` Add Qwen2.5 1.5B CSI calibration curve
- codegraph index: `231` files, `4276` nodes, `8416` edges
- current evidence ledger: `75 / 75` gates pass by
  `train_python/build_current_evidence_ledger.py`

## Tooling Health

Current local tooling status is healthy for repo work and experiment
coordination, with one bounded caveat about remote SaaS authentication.

| Surface | Current evidence | Boundary |
|---|---|---|
| Codex doctor | `codex doctor --json` completed with a warning only on the update probe (`403`); config, provider route, state DB, logs DB, goals DB, and memories DB were OK | update-check warning is not an experiment blocker |
| Local maintenance | `C:\Users\18042\.codex\maintenance\codex-local-maintenance-20260613-104518.log` reported `overall=ok fail=0 warn=0` | historical CC Switch provider degradation was informational; active local model-rewrite proxy remained usable |
| Skills registry | `C:\Users\18042\.codex\enabled-local-skills.json` was regenerated at `2026-06-12T19:13:00.8552465+08:00` with `996` scanned, `992` enabled files, `887` unique names, `4` excluded, and `0` invalid frontmatter files | force-enabled local skills still require reading the matching `SKILL.md` before use |
| Plugins/MCP | `C:\Users\18042\.codex\config.toml` contained `183` plugin blocks and `16` MCP servers: `blender`, `codegraph`, `feishu`, `node_repl`, `notebooklm`, `notion`, `obsidian-vault`, `openai-api-key-local-confirmation`, `playwright`, `steam-wallpaper-control`, `tripo-mcp`, `unity-mcp`, `unreal-mcp`, `windows-app-control`, `windows-mcp-safe`, and `word-document-server` | configured/enabled is not the same as logged-in SaaS OAuth health |
| Codegraph | live `codegraph_status` for this repo returned `231` files, `4276` nodes, `8416` edges, backend `node:sqlite`, WAL mode | use codegraph first for code intelligence; use direct file reads after edits or when checking generated markdown |

## Main Research Line

The strongest current line is CSI: calibration split instability in
mixed-precision LLM quantization. The supported claim is diagnostic and
bounded:

```text
Small calibration splits can produce unstable module-sensitivity rankings;
in the measured Qwen2.5 artifacts, increasing calibration prompt count improves
prompt-seed ranking stability.
```

Do not convert this into a universal scaling law, SOTA quantization claim,
downstream retention claim, production-runtime claim, or mobile-deployment
claim without additional evidence.

## Latest CSI Evidence

### Qwen2.5-1.5B same-model curve

| n | cases | pairs | mean Spearman | top-20 Jaccard | positive-set Jaccard | source |
|---:|---:|---:|---:|---:|---:|---|
| 2 | 6 | 15 | 0.1410 | 0.2604 | 0.4244 | `outputs/CALIBRATION_SEED_STABILITY_QWEN25_1P5B_N2_2026_06_10.md` |
| 4 | 6 | 15 | 0.2869 | 0.3313 | 0.5189 | `outputs/CALIBRATION_SEED_STABILITY_QWEN25_1P5B_N4_2026_06_11.md` |
| 8 | 6 | 15 | 0.4918 | 0.4401 | 0.5992 | `outputs/CALIBRATION_SEED_STABILITY_QWEN25_1P5B_N8_2026_06_11.md` |

Aggregated gates:

- `outputs/CSI_VS_N_CURVE_QWEN25_1P5B_2026_06_11.md`
- `outputs/CSI_TREND_SIGNIFICANCE_QWEN25_1P5B_2026_06_11.md`
- `outputs/CSI_NULL_PERMUTATION_QWEN25_1P5B_2026_06_11.md`

Summary:

- all three audited metrics improve monotonically from `n=2` to `n=8`;
- full-range bootstrap gain CIs are positive;
- permutation test max Holm-adjusted p-value is `0.000149993`;
- this is same-model local stability evidence, not downstream quality
  retention.

### Qwen2.5 0.5B vs 1.5B cross-scale comparison

Source artifacts:

- `outputs/CSI_CROSS_SCALE_QWEN25_0P5B_VS_1P5B_2026_06_11.md`
- `outputs/CSI_CROSS_SCALE_PAPER_ARTIFACTS_QWEN25_0P5B_VS_1P5B_2026_06_12.md`
- `outputs/CSI_CROSS_SCALE_DUAL_CURVE_QWEN25_0P5B_VS_1P5B_2026_06_12.svg`

Current conservative wording:

```text
In the current same-prompt-pool Qwen2.5 artifacts, the 1.5B curve is less
stable than the 0.5B curve at matched calibration sizes, while both improve
with additional calibration prompts.
```

Boundary:

- valid: cross-scale replication and comparison on the supplied artifacts;
- invalid: model size causality, universal scaling law, or downstream
  retention.

## Other Strong Evidence Blocks

| Block | Current state | Boundary |
|---|---|---|
| Official PTQ task evidence | Qwen2.5-1.5B FP16/AutoAWQ/GPTQModel has full GSM8K and complete 57-subject full-MMLU local task/runtime/statistics gates | local guarded execution only, not official leaderboard or SOTA |
| ESMP/W4A8 systems prototype | ESMP package, C++/Triton/W4A8 module-level gates exist | systems prototype, not end-to-end production runtime |
| Comparator/proxy coverage | AWQ/GPTQ proxy, rotation-family proxy, allocation-family proxy, robust-LCB gates exist | proxies are diagnostics, not faithful official baselines |

## Draft And Venue State

Committed drafts right now:

- `paper_drafts/eigenskill_q_research_draft_en_2026_06_07.md`
- `paper_drafts/eigenskill_q_ccf_style_draft_zh.md`

The five split tracks in `docs/PAPER_DRAFT_INDEX.md` are still planning routes,
not five completed committed drafts. The next writing pass should create or
update route-specific drafts only after deciding which evidence block each
venue is allowed to cite.

Recommended route mapping:

| Route | Best current thesis | Missing before strong submission |
|---|---|---|
| AAAI / IJCAI / TMLR | CSI as a reproducible calibration-instability diagnostic with conservative allocation implications | real downstream evaluation of CSI-derived allocation |
| NeurIPS / ICLR workshop | Robustness/measurement benchmark for calibration-induced ranking instability | broader model families, more prompt pools |
| ACL / EMNLP Findings | Language-model PTQ robustness and task-retention caveats | clearer NLP task link beyond MMLU/GSM8K local gates |
| MLSys / systems workshop | ESMP/W4A8 packed-kernel artifact and runtime diagnostics | end-to-end latency, memory, energy, and deployment measurements |
| Neural Networks / Information Sciences | extended journal version combining CSI, statistics, and baseline analysis | faithful SmoothQuant/rotation-family baselines and stronger ablations |

## Reviewer Gaps To Close Next

1. Downstream retention:
   run a real CSI-derived allocation variant against FP16, AutoAWQ, and
   GPTQModel on a matched public task fixture.
2. Baseline family breadth:
   add a clearly bounded SmoothQuant-style or rotation-family scale-up proxy;
   use faithful official implementations only if install/runtime risk is low.
3. Prompt-pool generality:
   repeat the Qwen2.5-1.5B `n=2/4/8` curve on a second public prompt pool,
   preferably C4, before claiming broader calibration robustness.
4. Draft split:
   create the route-specific CSI draft first; keep ESMP and benchmark-suite
   drafts separate.

## Immediate Execution Queue

1. Complete the matched Qwen2.5-1.5B IFEval row:
   `outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_IFEVAL_PARTIAL_2026_06_13.md`
   shows AutoAWQ and GPTQModel execute the 8-row deterministic IFEval fixture,
   but the FP16 row timed out while materializing/loading the incomplete local
   Hugging Face cache.
2. Run the cheapest downstream-retention gate:
   `Qwen2.5-1.5B`, CSI `n=8` or robust consensus allocation, Broad20x20 plus
   GSM8K500 if disk/GPU budget is acceptable.
3. Then decide whether to spend the next long run on second prompt pool or
   faithful baseline breadth.
