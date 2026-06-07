# EigenSkill Research Portfolio Split

Date: 2026-06-07

This note separates the current monolithic research pack into independent paper
tracks. The goal is not to multiply titles from the same evidence. A track is
split-worthy only when it has a distinct research question, non-overlapping
core claims, a separate artifact boundary, and its own reviewer-facing failure
mode.

## Split Rules

1. **No shared headline claims.** A result may support multiple introductions,
   but it cannot be the main contribution of two papers.
2. **No speculative material inside empirical papers.** Swarm, acoustic,
   morphology, and nonlinear eigen-routing vision text must stay outside the
   AAAI/ICLR quantization artifact unless a gate-backed experiment exists.
3. **One repo, one claim firewall.** Each public repository needs its own
   `CLAIMS.md`, `REPRODUCE.md`, and artifact policy. A reviewer should not have
   to infer which claims are active.
4. **Shared utilities are allowed, shared conclusions are not.** Dataset
   loaders, guards, and plotting scripts may be duplicated or extracted; paper
   conclusions must remain distinct.
5. **Negative results are publishable only when framed as a diagnostic.** A
   failed LoRA policy learner is not a method, but it can motivate deterministic
   routing or task-specific parsers if evaluated cleanly.

## Track A: CSI Quantization Robustness

**Working repo:** `eigenskill-q-calibration-robustness`

**Core question:** How unstable are module-sensitivity rankings under small
calibration splits, and can robust cross-split estimators reduce bad
mixed-precision allocation choices under a fixed bit budget?

**Current source repo material:**

- `docs/PAPER_CLAIM_MATRIX.md`
- `docs/SYSTEM_EVIDENCE_GATES.md`
- `docs/consensus-allocation-method.md`
- `docs/calibration_split_instability_position_2026_06_05.md`
- CSI, bootstrap, null-permutation, rank-inversion, allocation, and official PTQ
  task/PPL gates under `outputs/`
- `train_python/*calibration*`, `*allocation*`, `*official_awq*`,
  `*official_gptqmodel*`, `gate_official_ptq_*`, and task/PPL evaluation scripts
- `paper_drafts/eigenskill_q_research_draft_en_2026_06_07.md`

**Paper shape:** AAAI/IJCAI/TMLR-style empirical robustness paper.

**Do not include:** physical swarm, acoustic communication, nonlinear spectral
routing claims, mobile deployment claims, or production runtime claims.

**AAAI blockers:**

- Full or much larger MMLU/GSM8K/ARC/HellaSwag/PIQA/IFEval task coverage.
- Faithful SmoothQuant and at least one rotation-family baseline.
- Larger model row beyond the current Qwen2.5-1.5B AutoAWQ smoke.
- Clearer method delta beyond mean consensus, preferably robust estimator or
  interaction-aware allocation with confidence intervals.

## Track B: ESMP Packed Runtime And Kernels

**Working repo:** `eigenskill-esmp-runtime`

**Core question:** Can an explicit mixed-bit packed format plus selected-row and
Triton/CPU kernels provide reproducible, inspectable runtime evidence for
resource-constrained LLM modules?

**Current source repo material:**

- `inference_cpp/`
- `train_python/esmp_format.py`
- `train_python/pack_qwen3_consensus.py`
- `train_python/triton_mixed_gemm.py`
- `train_python/tune_triton_blocks.py`
- `train_python/benchmark_esmp_*`
- `train_python/measure_esmp_*`
- `outputs/real_system_packer_2026-06-05/`
- `mobile/redmi_k80_pro/` only as a harness, not as completed evidence

**Paper shape:** MLSys/ASPLOS workshop or systems artifact paper, later
MLSys/EuroSys/TC after end-to-end runtime closure.

**Do not include:** CSI theory as the main contribution, SOTA PTQ quality
claims, or broad task-retention claims unless the fused runtime gates provide
them.

**Hard blockers:**

- AVX2/NEON vectorized INT4 path that beats a strong FP32/FP16 baseline on
  relevant shapes.
- End-to-end TTFT/tokens/s/memory on a real model path, not only module probes.
- Kernel selection and fused decode scheduler stability.

## Track C: Hybrid Deterministic Skill Bypass

**Working repo:** `hybridskill-bypass-runtime`

**Core question:** For low-entropy, numerically strict tasks, when should an LLM
delegate to a deterministic parser or micro-kernel instead of learning the task
through short LoRA fine-tuning?

**Current source repo material:**

- `data_eval/eigenskill_quant_v0/` as historical data only, clearly marked
  leaked if used in discussion
- `data_eval/chat_task_benchmark_v1.jsonl`
- `data_eval/chat_task_stress_v2.jsonl`
- `data_eval/chat_task_stress_v3_84.jsonl`
- `train_python/hybrid_eval_*`
- `train_python/generate_*skill*`
- C++ policy-bypass reports under `outputs/EigenSkill-Q-Cpp-Policy-Bypass-*`
- chat-task stress gates under `outputs/real_system_packer_2026-06-05/`

**Paper shape:** efficient AI / edge AI workshop, negative-results workshop, or
software engineering for AI systems paper.

**Do not include:** CSI as the main contribution, PTQ baseline claims, or swarm
vision.

**Hard blockers:**

- Leak-free datasets only.
- Honest LoRA failure analysis with completion-only or constrained decoding
  ablations.
- C++ parser latency/coverage/maintainability numbers versus model-only output.

## Track D: Calibration Benchmark Suite

**Working repo:** `csi-benchmark-suite`

**Core question:** Can the community standardize calibration split instability
metrics, prompt-seed robustness, and rank-inversion diagnostics for LLM
quantization?

**Current source repo material:**

- CSI metric builders and gates:
  `build_calibration_instability_benchmark.py`,
  `build_calibration_robustness_stress.py`,
  `gate_csi_vs_n_curve.py`,
  `gate_csi_trend_significance.py`,
  `gate_csi_null_permutation.py`,
  `gate_rank_inversion_theory.py`
- public prompt manifests and compact task fixtures
- plotting utilities and bootstrap/null-test JSON outputs

**Paper shape:** benchmark/dataset/tool paper, TMLR, ACL/EMNLP Findings, or
efficient-LLM workshop artifact.

**Do not include:** a new quantization algorithm claim. This track sells the
measurement protocol and reproducibility.

**Hard blockers:**

- More datasets and model families.
- Stable JSON schema and CLI.
- Baseline scripts that external users can run without private artifacts.

## Track E: Eigen-Swarm Vision

**Working repo:** `eigenswarm-vision`

**Core question:** What would a cross-medium distributed edge-intelligence
architecture require if low-dimensional skill IDs, deterministic bypass, and
physical topology changes were treated as first-class design constraints?

**Current source repo material:** none should be imported as completed evidence.
Only high-level diagrams, assumptions, and explicit non-claims should be used.

**Paper shape:** vision/position paper for edge AI, tinyML, IoT, robotics,
MLSys/ASPLOS workshops, or a future survey-style article.

**Do not include:** claims that the current EigenSkill-Q code implements swarm
coordination, acoustic communication, magnetic assembly, or nonlinear
eigen-routing.

**Hard blockers for a non-vision paper:**

- Physical communication prototype.
- Board-level power and latency.
- Safety and security threat model.
- Real multi-node experiment.

## Recommended Repository Layout

```text
github_publish/
  eigenskill-q-calibration-robustness/  # main AAAI/ICLR quantization track
  eigenskill-esmp-runtime/              # packed runtime/kernels track
  hybridskill-bypass-runtime/           # deterministic skill bypass track
  csi-benchmark-suite/                  # benchmark/protocol/tooling track
  eigenswarm-vision/                    # position paper only
```

The existing `eigenskill-research-pack` should remain the temporary integration
repo until each child repo has a clean README, claim firewall, and reproduction
path. After that, the integration repo can either become private lab history or
   be converted into a landing page that links to the child artifacts.

## Publication Order

1. **CSI Quantization Robustness** first: strongest current evidence and most
   coherent AAAI/TMLR story.
2. **ESMP Runtime** second: wait until AVX2/NEON/Triton claims are end-to-end
   enough to avoid "tooling only" rejection.
3. **CSI Benchmark Suite** can be spun out in parallel if schemas and examples
   are cleaned.
4. **HybridSkill Bypass** after leak-free task data and C++ parser evidence are
   strong enough.
5. **Eigen-Swarm Vision** last, as a deliberately separate vision paper.
