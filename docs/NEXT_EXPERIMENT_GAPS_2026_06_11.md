# Next Experiment Gaps 2026-06-11

This note turns the remaining open reviewer gaps into executable gate targets.
It is a planning artifact, not evidence by itself.

## 1. Downstream Retention

Current CSI gates prove ranking stability, not that better rankings improve
PPL or task retention.

Next gate target:

```text
FP16 vs native PTQ vs CSI-derived allocation
same model, same public calibration pool, same task fixture, same GPU guard
```

Recommended first run:

- model: `Qwen2.5-1.5B-Instruct`
- tasks: reuse existing full GSM8K and full MMLU fixtures only if time allows;
  otherwise start with Broad20x20 plus GSM8K500 as a cheaper matched gate.
- variants:
  - FP16
  - AutoAWQ W4/G128
  - GPTQModel W4/G128
  - CSI allocation derived from `n=8` or robust consensus across seed artifacts
- required output:
  - task matrix JSON/MD
  - runtime profile JSON/MD
  - paired bootstrap statistics JSON/MD

Claim boundary:

- Valid only if the CSI allocation is a real executed variant, not just a
  sensitivity artifact.
- Do not claim downstream retention from CSI-vs-n alone.

## 2. Baseline Family

Current official-package baseline coverage is strongest for AutoAWQ and
GPTQModel. SmoothQuant and rotation-family coverage remains incomplete.

Minimum acceptable next baseline:

- a clearly labeled SmoothQuant-style or rotation-family **proxy** if faithful
  package execution is unavailable;
- a faithful official implementation only if it can be installed, run, and
  guarded without changing the claim boundary.

Preferred order:

1. SmoothQuant-style activation-smoothing proxy over the same measured
   sensitivity records.
2. Rotation-family proxy scale-up from Qwen3-0.6B to Qwen2.5-1.5B sensitivity
   artifacts.
3. Faithful QuaRot/SpinQuant only if dependency and runtime risk is acceptable.

Claim boundary:

- Proxy coverage can answer reviewer breadth concerns only as related-family
  diagnostics.
- It cannot be described as official SmoothQuant, QuaRot, or SpinQuant.

## 3. Cross-Scale CSI Interpretation

The 0.5B-vs-1.5B cross-scale gate now shows:

- 1.5B is lower than 0.5B at every shared n and audited metric.
- Both scales improve from `n=2` to `n=8`.
- 1.5B has larger Spearman gain but smaller top-20 and positive-set Jaccard
  gains.

Paper wording should be conservative:

```text
In the current same-prompt-pool Qwen2.5 artifacts, the 1.5B curve is less
stable than the 0.5B curve at matched calibration sizes, while both improve
with additional calibration prompts.
```

Avoid:

```text
larger models are inherently less stable
```

until more model scales or repeated model-family evidence exists.
