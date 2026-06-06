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
| The current paper-facing evidence set passes as a ledger. | Top-level evidence ledger. | `outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md` | A ledger pass means listed gates passed, not that the paper is top-tier ready. |

## Rejected Or Not-Yet Claims

| claim | status | required next evidence |
|---|---|---|
| EigenSkill-Q is a SOTA quantizer. | Rejected. | GPTQ/AWQ/SmoothQuant/QuaRot/SpinQuant comparisons on public benchmarks. |
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
