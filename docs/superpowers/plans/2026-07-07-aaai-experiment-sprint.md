# AAAI Experiment Sprint Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the final AAAI evidence package that answers reviewer objections about downstream usefulness, stability, robustness, and trustworthy claim boundaries for the unified constraint-guided calibration framework.

**Architecture:** The sprint is organized as evidence gates rather than more one-off experiments. Existing scripts in `train_python/` remain the execution layer; new work should add thin orchestration, aggregation, and reporting scripts that produce reviewer-facing tables/figures under `outputs/aaai_sprint_2026_07_07/`.

**Tech Stack:** Python, existing `train_python/` gate scripts, RTX3090 guarded execution, JSON/Markdown outputs, MMLU/GSM8K task fixtures, official PTQ baselines where already supported by the repository.

---

## Scope Discipline

Do not add new theory, new model modules, or new loss terms during this sprint.
The target is reviewer-risk removal:

- CSI-guided allocation must be tied to downstream retention.
- Calibration size must be tied to both stability and accuracy.
- Seed robustness must show mean, standard deviation, and worst case.
- Heuristic comparison must show CSI is more predictive than simpler metrics.
- All tables must keep pending rows visibly pending until the experiment has run.

## Files

- Create: `outputs/aaai_sprint_2026_07_07/README.md`
  - Tracks the sprint status and artifact paths.
- Create: `outputs/aaai_sprint_2026_07_07/experiment_matrix.json`
  - Machine-readable list of methods, models, seeds, datasets, calibration sizes, and expected output files.
- Create: `train_python/build_aaai_sprint_matrix.py`
  - Generates the matrix and placeholder-free run manifest.
- Create: `train_python/summarize_aaai_sprint_results.py`
  - Aggregates completed JSON artifacts into win/loss, average rank, seed stability, and failure tables.
- Create: `train_python/test_build_aaai_sprint_matrix.py`
  - Tests matrix completeness and no accidental duplicate rows.
- Create: `train_python/test_summarize_aaai_sprint_results.py`
  - Tests aggregation on small synthetic records.
- Modify: `docs/AAAI_FINAL_SUBMISSION_CHECKLIST_2026_06_28.md`
  - Add priority mapping from this sprint plan to final submission artifacts.
- Modify: `paper_drafts/unified_constraint_guided_calibration_framework_2026_06_28.md`
  - Only after experiments complete, replace pending rows with verified results.

## Phase 0: Manifest and No-Result Aggregation

### Task 1: Create the AAAI Sprint Manifest

**Files:**
- Create: `train_python/build_aaai_sprint_matrix.py`
- Test: `train_python/test_build_aaai_sprint_matrix.py`
- Create: `outputs/aaai_sprint_2026_07_07/experiment_matrix.json`

- [ ] **Step 1: Write the matrix test**

Create `train_python/test_build_aaai_sprint_matrix.py` with tests that assert:

```python
import json
import subprocess
import sys
from pathlib import Path


def test_matrix_contains_p0_experiments(tmp_path: Path):
    out = tmp_path / "matrix.json"
    subprocess.run(
        [
            sys.executable,
            "train_python/build_aaai_sprint_matrix.py",
            "--output",
            str(out),
        ],
        check=True,
    )
    payload = json.loads(out.read_text(encoding="utf-8"))
    ids = {row["experiment_id"] for row in payload["experiments"]}
    assert "p0_csi_allocation_retention" in ids
    assert "p0_calibration_size_scaling" in ids
    assert "p0_seed_robustness" in ids
    assert "p1_csi_vs_heuristics" in ids


def test_matrix_has_no_duplicate_run_keys(tmp_path: Path):
    out = tmp_path / "matrix.json"
    subprocess.run(
        [
            sys.executable,
            "train_python/build_aaai_sprint_matrix.py",
            "--output",
            str(out),
        ],
        check=True,
    )
    payload = json.loads(out.read_text(encoding="utf-8"))
    keys = [tuple(row["run_key"]) for row in payload["runs"]]
    assert len(keys) == len(set(keys))
```

- [ ] **Step 2: Run the failing test**

Run:

```powershell
python -m pytest train_python/test_build_aaai_sprint_matrix.py -q
```

Expected: fails because `train_python/build_aaai_sprint_matrix.py` does not exist.

- [ ] **Step 3: Implement the manifest generator**

Create `train_python/build_aaai_sprint_matrix.py` with:

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


MODELS = ["qwen25_0p5b", "qwen25_1p5b", "qwen25_3b", "qwen25_7b"]
PRIMARY_MODELS = ["qwen25_0p5b", "qwen25_1p5b"]
TASKS = ["mmlu", "gsm8k"]
SEEDS = [0, 1, 2, 3, 4]
CALIBRATION_SIZES = [32, 64, 128, 256, 512, 1024, 2048]
ALLOCATION_POLICIES = ["uniform", "sensitivity_only", "csi_guided"]
PTQ_BASELINES = ["fp16", "uniform_int4", "uniform_int3", "gptq_int4", "awq_int4", "smoothquant_int4"]
HEURISTICS = ["variance", "entropy", "layer_sensitivity", "random", "csi"]


def add_run(runs: list[dict], *, experiment_id: str, model: str, task: str, method: str, seed: int | None = None, calibration_size: int | None = None) -> None:
    run_key = [experiment_id, model, task, method, str(seed), str(calibration_size)]
    runs.append(
        {
            "experiment_id": experiment_id,
            "model": model,
            "task": task,
            "method": method,
            "seed": seed,
            "calibration_size": calibration_size,
            "run_key": run_key,
            "status": "pending",
            "expected_summary": f"outputs/aaai_sprint_2026_07_07/{'_'.join(run_key)}.json",
        }
    )


def build_payload() -> dict:
    experiments = [
        {
            "experiment_id": "p0_csi_allocation_retention",
            "reviewer_objection": "CSI is only an observation, not an allocation decision.",
            "required_outputs": ["pareto_curve", "task_retention_table", "bits_per_weight", "model_size", "rank_agreement", "csi_variance"],
        },
        {
            "experiment_id": "p0_calibration_size_scaling",
            "reviewer_objection": "Calibration stability does not necessarily scale into downstream retention.",
            "required_outputs": ["dual_axis_csi_accuracy_curve", "split_agreement", "rank_correlation", "topk_overlap"],
        },
        {
            "experiment_id": "p0_seed_robustness",
            "reviewer_objection": "The result may be a lucky seed.",
            "required_outputs": ["mean_std_worst_case", "seed_rank_correlation", "seed_accuracy"],
        },
        {
            "experiment_id": "p1_csi_vs_heuristics",
            "reviewer_objection": "A simpler variance or sensitivity heuristic may be enough.",
            "required_outputs": ["pearson_correlation", "spearman_correlation", "future_accuracy_drop_prediction"],
        },
    ]
    runs: list[dict] = []
    for model in PRIMARY_MODELS:
        for task in TASKS:
            for method in PTQ_BASELINES + ALLOCATION_POLICIES:
                add_run(runs, experiment_id="p0_csi_allocation_retention", model=model, task=task, method=method)
            for n in CALIBRATION_SIZES:
                add_run(runs, experiment_id="p0_calibration_size_scaling", model=model, task=task, method="csi_guided", calibration_size=n)
            for method in ["uniform", "gptq_int4", "awq_int4", "csi_guided"]:
                for seed in SEEDS:
                    add_run(runs, experiment_id="p0_seed_robustness", model=model, task=task, method=method, seed=seed)
            for heuristic in HEURISTICS:
                add_run(runs, experiment_id="p1_csi_vs_heuristics", model=model, task=task, method=heuristic)
    return {
        "schema_version": 1,
        "created_for": "AAAI experiment sprint 2026-07-07",
        "experiments": experiments,
        "runs": runs,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(build_payload(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the matrix test**

Run:

```powershell
python -m pytest train_python/test_build_aaai_sprint_matrix.py -q
```

Expected: `2 passed`.

- [ ] **Step 5: Generate the sprint matrix**

Run:

```powershell
python train_python/build_aaai_sprint_matrix.py --output outputs/aaai_sprint_2026_07_07/experiment_matrix.json
```

Expected: `outputs/aaai_sprint_2026_07_07/experiment_matrix.json` exists and contains pending rows only.

### Task 2: Add No-Result Summarization

**Files:**
- Create: `train_python/summarize_aaai_sprint_results.py`
- Test: `train_python/test_summarize_aaai_sprint_results.py`

- [ ] **Step 1: Write summarizer tests**

Create `train_python/test_summarize_aaai_sprint_results.py` with tests for a tiny synthetic result set:

```python
import json
import subprocess
import sys
from pathlib import Path


def write_result(path: Path, method: str, task: str, accuracy: float, seed: int = 0):
    path.write_text(
        json.dumps(
            {
                "method": method,
                "task": task,
                "seed": seed,
                "accuracy": accuracy,
                "bits_per_weight": 4.0,
                "model_size_mb": 100.0,
                "csi": 0.7,
            }
        ),
        encoding="utf-8",
    )


def test_summarizer_builds_win_loss_and_rank(tmp_path: Path):
    results = tmp_path / "results"
    results.mkdir()
    write_result(results / "ours_mmlu.json", "csi_guided", "mmlu", 0.72)
    write_result(results / "base_mmlu.json", "awq_int4", "mmlu", 0.70)
    out = tmp_path / "summary.json"
    subprocess.run(
        [
            sys.executable,
            "train_python/summarize_aaai_sprint_results.py",
            "--input-dir",
            str(results),
            "--output",
            str(out),
        ],
        check=True,
    )
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["win_loss"]["csi_guided_vs_awq_int4"]["wins"] == 1
    assert payload["average_rank"]["csi_guided"] == 1.0
```

- [ ] **Step 2: Run the failing summarizer test**

Run:

```powershell
python -m pytest train_python/test_summarize_aaai_sprint_results.py -q
```

Expected: fails because the summarizer does not exist.

- [ ] **Step 3: Implement the summarizer**

Create `train_python/summarize_aaai_sprint_results.py` with:

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from statistics import mean, pstdev
from typing import Any


def finite_float(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(number) or math.isinf(number):
        return None
    return number


def load_records(input_dir: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(input_dir.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        method = payload.get("method")
        task = payload.get("task")
        accuracy = finite_float(payload.get("accuracy"))
        if not method or not task or accuracy is None:
            continue
        record = dict(payload)
        record["method"] = str(method)
        record["task"] = str(task)
        record["accuracy"] = accuracy
        record["source_path"] = str(path)
        records.append(record)
    return records


def build_win_loss(records: list[dict[str, Any]], proposed: str = "csi_guided") -> dict[str, dict[str, int]]:
    by_task_method: dict[tuple[str, str], list[float]] = defaultdict(list)
    for record in records:
        by_task_method[(record["task"], record["method"])].append(float(record["accuracy"]))
    tasks = sorted({record["task"] for record in records})
    methods = sorted({record["method"] for record in records if record["method"] != proposed})
    output: dict[str, dict[str, int]] = {}
    for method in methods:
        row = {"wins": 0, "losses": 0, "ties": 0}
        for task in tasks:
            ours = by_task_method.get((task, proposed), [])
            theirs = by_task_method.get((task, method), [])
            if not ours or not theirs:
                continue
            ours_mean = mean(ours)
            theirs_mean = mean(theirs)
            if abs(ours_mean - theirs_mean) < 1.0e-12:
                row["ties"] += 1
            elif ours_mean > theirs_mean:
                row["wins"] += 1
            else:
                row["losses"] += 1
        output[f"{proposed}_vs_{method}"] = row
    return output


def build_average_rank(records: list[dict[str, Any]]) -> dict[str, float]:
    by_task: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for record in records:
        by_task[record["task"]][record["method"]].append(float(record["accuracy"]))
    ranks: dict[str, list[float]] = defaultdict(list)
    for methods in by_task.values():
        ordered = sorted(
            ((method, mean(values)) for method, values in methods.items()),
            key=lambda item: item[1],
            reverse=True,
        )
        for index, (method, _score) in enumerate(ordered, start=1):
            ranks[method].append(float(index))
    return {method: mean(values) for method, values in sorted(ranks.items())}


def build_seed_stability(records: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
    grouped: dict[str, list[float]] = defaultdict(list)
    for record in records:
        if record.get("seed") is None:
            continue
        grouped[record["method"]].append(float(record["accuracy"]))
    return {
        method: {
            "mean": mean(values),
            "std": pstdev(values) if len(values) > 1 else 0.0,
            "worst": min(values),
            "seeds": float(len(values)),
        }
        for method, values in sorted(grouped.items())
    }


def summarize(input_dir: Path) -> dict[str, Any]:
    records = load_records(input_dir)
    return {
        "record_count": len(records),
        "win_loss": build_win_loss(records),
        "average_rank": build_average_rank(records),
        "seed_stability": build_seed_stability(records),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(summarize(Path(args.input_dir)), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run summarizer tests**

Run:

```powershell
python -m pytest train_python/test_summarize_aaai_sprint_results.py -q
```

Expected: tests pass.

## Phase 1: P0 Experiments

### Task 3: CSI-Guided Allocation Downstream Retention

**Files:**
- Use: `train_python/build_consensus_allocation.py`
- Use: `train_python/gate_official_ptq_task_retention.py`
- Use: `train_python/gate_official_ptq_runtime_profile.py`
- Output: `outputs/aaai_sprint_2026_07_07/p0_csi_allocation_retention_*.json`

- [ ] **Step 1: Freeze the baseline list**

Use exactly these baselines for the first pass:

```text
fp16
uniform_int4
uniform_int3
gptq_int4
awq_int4
smoothquant_int4
uniform_allocation
sensitivity_only_allocation
csi_guided_allocation
```

Do not add OmniQuant until the above table has at least one complete model-task pair.

- [ ] **Step 2: Generate or locate allocation JSONs**

Produce one allocation summary for each policy:

```text
uniform_allocation
sensitivity_only_allocation
csi_guided_allocation
```

Expected output fields per allocation:

```json
{
  "method": "csi_guided_allocation",
  "model": "qwen25_1p5b",
  "bits_per_weight": 4.0,
  "model_size_mb": 0.0,
  "rank_agreement": 0.0,
  "csi_variance": 0.0,
  "allocation_path": "outputs/aaai_sprint_2026_07_07/allocation.json"
}
```

Replace zero values only after the real run completes.

- [ ] **Step 3: Evaluate retention on MMLU and GSM8K**

Use existing task-retention tooling with guarded execution:

```powershell
python train_python/gate_official_ptq_task_retention.py --help
python train_python/gate_official_ptq_runtime_profile.py --help
```

Record the exact commands used in `outputs/aaai_sprint_2026_07_07/README.md`.

- [ ] **Step 4: Build the Pareto figure data**

Create a JSON table with:

```json
{
  "method": "csi_guided_allocation",
  "task": "mmlu",
  "accuracy": 0.0,
  "bits_per_weight": 0.0,
  "model_size_mb": 0.0,
  "rank_agreement": 0.0,
  "csi_variance": 0.0
}
```

The figure is x-axis `bits_per_weight` or `model_size_mb`, y-axis `accuracy`, series `uniform`, `sensitivity_only`, `csi_guided`.

### Task 4: Calibration Size Scaling

**Files:**
- Use: `train_python/gate_calibration_seed_stability.py`
- Use: `train_python/gate_csi_vs_n_curve.py`
- Use: `train_python/gate_csi_trend_significance.py`
- Use: `train_python/gate_csi_null_permutation.py`
- Output: `outputs/aaai_sprint_2026_07_07/p0_calibration_size_scaling_*.json`

- [ ] **Step 1: Use the fixed calibration sizes**

Run sizes:

```text
32
64
128
256
512
1024
2048
```

- [ ] **Step 2: Compute CSI metrics for each size**

For each size, report:

```text
split agreement
rank correlation
top-k overlap
positive-set overlap
```

- [ ] **Step 3: Evaluate downstream retention for each size**

For each size, evaluate:

```text
MMLU
GSM8K
```

- [ ] **Step 4: Build dual-axis figure data**

Output table columns:

```text
model, task, calibration_size, csi_score, rank_correlation, topk_overlap, accuracy
```

The figure has left y-axis `CSI / rank agreement` and right y-axis `accuracy`.

### Task 5: Seed Robustness

**Files:**
- Use: `train_python/gate_calibration_seed_stability.py`
- Use: `train_python/gate_official_ptq_task_statistics.py`
- Output: `outputs/aaai_sprint_2026_07_07/p0_seed_robustness_*.json`

- [ ] **Step 1: Use fixed seeds**

Run:

```text
0
1
2
3
4
```

- [ ] **Step 2: Report stable statistics**

For each method, report:

```text
mean accuracy
standard deviation
worst-case accuracy
mean CSI
standard deviation CSI
rank-correlation mean
rank-correlation standard deviation
```

- [ ] **Step 3: Add reviewer table**

Use table columns:

```text
method, accuracy_mean, accuracy_std, accuracy_worst, csi_mean, csi_std, rank_corr_mean, rank_corr_std
```

## Phase 2: P1 Experiments

### Task 6: CSI vs Simple Heuristics

**Files:**
- Use: `train_python/gate_sensitivity_perturbation_matrix.py`
- Use: `train_python/gate_rank_inversion_theory.py`
- Output: `outputs/aaai_sprint_2026_07_07/p1_csi_vs_heuristics_*.json`

- [ ] **Step 1: Compare these predictors**

```text
variance
entropy
layer_sensitivity
random
csi
```

- [ ] **Step 2: Predict future accuracy drop**

For each predictor, compute:

```text
Pearson correlation with future accuracy drop
Spearman correlation with future accuracy drop
```

- [ ] **Step 3: Pass criterion**

The CSI predictor must be best or statistically tied for best. If it is not,
the final paper must weaken the claim from "CSI-guided allocation" to
"CSI-assisted audit".

### Task 7: Objective-Aligned Ablation

**Files:**
- Use: `train_python/build_consensus_allocation.py`
- Use: `train_python/gate_robust_lcb_consensus.py`
- Output: `outputs/aaai_sprint_2026_07_07/p1_objective_ablation_*.json`

- [ ] **Step 1: Run the four ablations**

```text
no_calibration_split
no_rank_component
no_stability_component
no_allocation_policy
```

- [ ] **Step 2: Report two columns**

```text
CSI
accuracy
```

- [ ] **Step 3: Interpret failure**

If an ablation does not degrade either CSI or accuracy, the method section must
explain why that term is redundant or remove that term from the core claim.

## Phase 3: P2/P3 Backlog

### Task 8: Generalization and Efficiency Backlog

Run only after P0 and P1 are closed:

```text
bit_width_sweep: INT2, INT3, INT4, INT8, FP16 on Qwen2.5-1.5B
model_scale: Qwen2.5-3B and Qwen2.5-7B
extra_family: one of Llama-3.2, Phi-3, Mistral
dataset_shift: calibration WikiText/C4, evaluation MMLU/GSM8K
failure_recovery: 2048 -> 128 calibration reduction with CSI reject/audit
efficiency: calibration time, CSI time, memory, inference time
layer_visualization: layer id vs CSI score
cross_quantizer_generalization: GPTQ-derived CSI predicts AWQ/SmoothQuant risk
case_study: one stable layer and one unstable layer with activation/rank evidence
pareto_frontier: memory vs accuracy across all complete methods
```

## Completion Gate

The sprint is complete only when:

- `outputs/aaai_sprint_2026_07_07/experiment_matrix.json` exists.
- P0 retention, calibration scaling, and seed robustness have result JSON files.
- `train_python/summarize_aaai_sprint_results.py` produces win/loss and average-rank summaries.
- The paper draft contains verified numbers instead of pending rows.
- `docs/AAAI_FINAL_SUBMISSION_CHECKLIST_2026_06_28.md` marks every must-do item with an artifact path.
