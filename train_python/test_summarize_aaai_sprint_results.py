from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def write_result(path: Path, method: str, task: str, accuracy: float, seed: int | None = None):
    payload = {
        "method": method,
        "task": task,
        "accuracy": accuracy,
        "bits_per_weight": 4.0,
        "model_size_mb": 100.0,
        "csi": 0.7,
    }
    if seed is not None:
        payload["seed"] = seed
    path.write_text(json.dumps(payload), encoding="utf-8")


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


def test_summarizer_reports_seed_stability(tmp_path: Path):
    results = tmp_path / "results"
    results.mkdir()
    write_result(results / "seed0.json", "csi_guided", "mmlu", 0.70, seed=0)
    write_result(results / "seed1.json", "csi_guided", "mmlu", 0.74, seed=1)
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
    assert payload["seed_stability"]["csi_guided"]["worst"] == 0.70
    assert payload["seed_stability"]["csi_guided"]["seeds"] == 2.0
