# Revised Publication Targets

This note replaces the earlier broad venue list with targets that match the
current evidence level. NeurIPS/MLSys are intentionally not the primary route.

## Current Evidence Level

The repository currently supports a narrow claim:

```text
For short-slice fake weight quantization, noisy one-split module sensitivity
can fail against random allocation, and a cross-dataset consensus allocation
can repair an observed best-random failure case on OLMo2-0425-1B while staying
positive on Qwen3-1.7B and Qwen3-0.6B diagnostics.
```

The evidence is not yet enough for a broad systems or hardware paper because
there is no board-level latency, energy, packed runtime, or NPU/NEON result.

## Best-Fit Near-Term Route

### 1. ACL Findings / EMNLP Findings / COLING Main or Findings

Fit:

```text
LLM compression diagnostic
robust calibration-set selection
mixed-precision bit allocation analysis
negative evidence plus repair heuristic
```

What must be added:

```text
real baseline comparison or a clearly scoped diagnostic framing
larger prompt slices
at least one additional model family if possible
clean ablation: one-split vs consensus vs random16 vs category
```

### 2. AAAI / IJCAI

Fit:

```text
algorithmic heuristic with clear empirical validation
calibration-noise robustness
resource-aware model compression
```

Risk:

```text
current evaluator is fake-quant only
baselines such as GPTQ/AWQ/SmoothQuant/QuaRot are not implemented
```

### 3. CIKM / DASFAA / KDD Workshop

Fit:

```text
practical efficient-LLM compression evidence
short-cycle empirical system artifact
```

This is more realistic if public baseline packages remain unavailable.

## Journal Route

### Neural Networks

Possible only if the paper is reframed as:

```text
robust calibration and allocation diagnostics for mixed-precision LLM
fake-quantization under noisy sensitivity estimates
```

Needed:

```text
more models
more prompt slices
baseline implementations
statistical tests across random seeds
```

### IEEE Transactions on Artificial Intelligence

Possible if the contribution is positioned as an applied compression framework
with conservative claims. Needs stronger baselines and clearer novelty.

### IEEE Access

Realistic fallback for a complete engineering report, but less selective. Use
only if the goal is publication speed rather than prestige.

## Not Ready Yet

Avoid targeting these with the current artifact:

```text
ASPLOS / ISCA / MICRO: no hardware or runtime evidence
TNNLS / TPAMI: not enough theoretical or empirical depth
DAC / ICCAD: no hardware design flow
RTAS / EMSOFT: no real-time or embedded board evaluation
```

## Next Evidence Needed

Highest value work:

```text
1. Implement or install at least one public quantization baseline.
2. Increase evaluation slices beyond 64 prompts for the strongest rows.
3. Add an interaction-aware swap/search stage initialized from consensus.
4. Add exact scripts for every table in the draft.
5. Keep negative results visible; they are central to the consensus argument.
```

