# Paper Claim Matrix

This matrix is the repository's claim firewall. A statement is paper-facing only
when it is tied to a runnable command, a committed artifact, and a narrow
interpretation. Anything outside these rows remains future work.

## Accepted Claims

| claim | evidence | command / artifact | boundary |
|---|---|---|---|
| Small calibration splits produce unstable module sensitivity rankings. | Split-stability reports and consensus allocation summaries. | `docs/consensus-allocation-method.md`, `docs/calibration_split_instability_position_2026_06_05.md` | Supports calibration robustness framing, not a new quantizer claim. |
| Calibration split instability appears across multiple small public model families. | Qwen3-0.6B, Qwen3-1.7B, and OLMo2-1B WikiText2-vs-C4 sensitivity benchmark. | `outputs/CALIBRATION_INSTABILITY_BENCHMARK_2026_06_06.md` | Establishes a measured problem setting; downstream PPL/task evidence is still needed for method superiority. |
| Consensus allocation can beat random mixed-precision allocations on current small-model PPL slices. | Qwen3-0.6B, Qwen3-1.7B, and OLMo2-1B WikiText2/C4 summaries. | README "Main Evidence" table and output summaries under `outputs/`. | PPL-slice evidence only; no MMLU/GSM8K/HumanEval claim. |
| ESMPQ001 is a real binary package format shared by C++ and Python readers. | C++ packer/reader, Python reader, format tests, inspector. | `ctest --test-dir build/cpp-wsl -R "mixed_precision|esmp"`; `python -m unittest train_python.test_esmp_format train_python.test_verify_esmp_package` | Matrix package format only; not a full model container. |
| Packed artifacts can be audited for manifest/header consistency. | `verify_esmp_package.py` verifies `pack_summary.json`, per-module manifest JSON, and ESMP binary headers. | `python train_python/verify_esmp_package.py --summary <pack_summary.json> --limit-modules 8 --min-checked 8 --max-missing 0` | Validates artifact integrity, not model quality. |
| A tuned Triton mixed INT4/INT8 kernel can beat torch FP16 for selected measured shapes. | Triton shape-family gate. | `outputs/real_system_packer_2026-06-05/TRITON_QWEN_SHAPE_FAMILY_GATE_2026_06_06.md` | Kernel-level only; no end-to-end speedup claim. |
| Selector wiring can choose measured kernel configs at runtime. | Selector smoke gate and config selector output. | `outputs/real_system_packer_2026-06-05/SELECTOR_RUNTIME_SMOKE_GATE_2026_06_06.md` | Runtime wiring evidence only; small decode cases remain launch-bound. |
| Selected-row routing can reduce module-level work when the active row set is small. | C++ runtime sweep and selected-row gate. | `outputs/real_system_packer_2026-06-05/CPP_RUNTIME_SWEEP_GATE_2026_06_06.md`, `SELECTED_ROW_BENCHMARK_GATE_2026_06_06.md` | Module-level selected-row evidence, not whole-LLM latency. |
| Shallow fused QKV replacement can run inside HF generation with bounded guard memory. | Fused QKV generation gate. | `outputs/real_system_packer_2026-06-05/FUSED_QKV_GENERATION_GATE_2026_06_06.md` | One-layer smoke result; generated text is not exact in the speed gate. |
| Conservative fused-QKV candidates can preserve a small prompt suite. | Fused QKV prompt-suite quality gate. | `outputs/real_system_packer_2026-06-05/FUSED_QKV_PROMPT_SUITE_GATE_2026_06_06.md` | Six-prompt suite only; not broad benchmark retention. |
| Current chat-task stress retention is measured rather than hidden. | 84-task stress gate. | `outputs/real_system_packer_2026-06-05/CHAT_TASK_STRESS_V3_84_GATE_2026_06_06.md` | Allows one known regression; does not prove production readiness. |
| Public-schema task evaluation is wired. | Streamed GSM8K and MMLU abstract-algebra smoke fixtures plus Qwen3-0.6B guarded baseline outputs. | `outputs/PUBLIC_TASK_SMOKE_MANIFEST_2026_06_06.md`, `outputs/PUBLIC_TASK_SMOKE_MMLU_QWEN3_0P6B.md`, `outputs/PUBLIC_TASK_SMOKE_GSM8K_QWEN3_0P6B.md` | Tiny negative smoke only: 0/4 on each slice; not broad task retention. |
| Public MMLU/GSM8K subset evaluation is guarded at 100 tasks. | Ollama qwen35-4B local API run on 50 MMLU abstract-algebra and 50 GSM8K rows. | `outputs/PUBLIC_TASK_BENCHMARK_OLLAMA_QWEN35_4B_GATE_2026_06_06.md` | Coverage and negative capability evidence only: 4/100 total passes; not leaderboard-scale or fused-retention evidence. |
| A Q-Palette-style allocation comparator proxy is executable. | Measured Qwen3-0.6B WikiText2/C4 sensitivity artifacts produce budget-satisfying rate-distortion allocations. | `outputs/Q_PALETTE_STYLE_ALLOCATION_FAMILY_GATE_2026_06_06.md` | Proxy comparator only; not a faithful official Q-Palette/IMPQ/WINDQuant reproduction. |
| A QuaRot/SpinQuant-style rotation-family proxy is executable. | Measured Qwen3-0.6B WikiText2/C4 sensitivity artifacts produce budgeted rotation/outlier-mitigation proxy summaries. | `outputs/QUAROT_SPINQUANT_ROTATION_FAMILY_GATE_2026_06_06.md` | Proxy comparator-family coverage only; not a faithful official QuaRot/SpinQuant implementation or activation/KV quality proof. |
| The current paper-facing evidence set passes as a ledger. | Top-level evidence ledger. | `outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md` | A ledger pass means listed gates passed, not that the paper is top-tier ready. |
| Missing baseline families are explicitly tracked. | Machine-readable baseline coverage manifest and generated gap dashboard. | `docs/BASELINE_COVERAGE_MANIFEST.json`, `outputs/BASELINE_GAP_DASHBOARD_2026_06_06.md` | Tracks readiness gaps; does not turn missing external baselines into evidence. |

## Rejected Or Not-Yet Claims

| claim | status | required next evidence |
|---|---|---|
| EigenSkill-Q is a SOTA quantizer. | Rejected. | GPTQ/AWQ/SmoothQuant and faithful QuaRot/SpinQuant comparisons on matched public benchmarks. |
| EigenSkill-Q is competitive with recent mixed-precision allocation papers. | Not yet. | Q-Palette/IMPQ/WINDQuant-style comparisons or faithful reimplementations under matched budgets. |
| EigenSkill-Q faithfully implements rotation-family PTQ. | Not yet. | Official or faithful QuaRot/SpinQuant transforms, activation/KV rotation kernels, and quality-retention evaluation. |
| The system has mobile/Redmi K80 Pro latency evidence. | Not yet. | On-device TTFT, tokens/s, peak memory, and thermal/power logs. |
| The packed runtime is a production Tensor Core LLM runtime. | Not yet. | Fused decode scheduler, stable multi-layer replacement, and broad quality retention. |
| Spectral/eigen routing survives nonlinear Transformer blocks. | Not yet. | Mathematical proof or controlled nonlinear-layer experiments. |
| The old leaked v2 routing result proves generalization. | Rejected. | It remains historical negative evidence only. |

## Current Paper Angle

The strongest defensible paper framing is:

```text
Calibration Split Instability in Mixed-Precision LLM Quantization:
Consensus Sensitivity Allocation with Gated Packed-System Evidence
```

This angle is narrower than the original EigenSkill idea, but it is much more
reviewable: it defines a measurable instability problem, gives a conservative
allocation response, and keeps systems claims behind executable gates.
