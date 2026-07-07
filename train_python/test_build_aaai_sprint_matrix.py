import json
import subprocess
import sys
from pathlib import Path


def test_matrix_contains_priority_experiments(tmp_path: Path):
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
    assert "p0_csi_vs_heuristics" in ids
    assert "p1_bit_width_sweep" in ids
    assert "p1_scale_support" in ids


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


def test_matrix_uses_final_sprint_ranges(tmp_path: Path):
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
    calibration_sizes = {row["calibration_size"] for row in payload["runs"] if row["experiment_id"] == "p0_calibration_size_scaling"}
    assert 16 in calibration_sizes
    assert 4096 in calibration_sizes
    heuristics = {row["method"] for row in payload["runs"] if row["experiment_id"] == "p0_csi_vs_heuristics"}
    assert {"rank_variance", "entropy", "layer_sensitivity", "calibration_loss", "random", "csi"} <= heuristics


def test_matrix_covers_decision_allocation_requirements(tmp_path: Path):
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
    rows = [row for row in payload["runs"] if row["experiment_id"] == "p0_csi_allocation_retention"]
    methods = {row["method"] for row in rows}
    budgets = {row["bit_width"] for row in rows}
    models = {row["model"] for row in rows}
    assert {"uniform", "single_split", "sensitivity_only", "activation_magnitude", "hessian_trace_proxy", "weight_sensitivity", "random", "csi_guided"} <= methods
    assert {2, 3, 4} <= budgets
    assert {"qwen25_1p5b", "qwen25_3b", "qwen25_7b"} <= models


def test_matrix_covers_scale_support(tmp_path: Path):
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
    rows = [row for row in payload["runs"] if row["experiment_id"] == "p1_scale_support"]
    models = {row["model"] for row in rows}
    methods = {row["method"] for row in rows}
    assert {"qwen25_7b", "qwen25_14b_awq"} <= models
    assert {"uniform", "single_split", "csi_guided"} <= methods


def test_matrix_runs_scale_models_through_calibration_and_seed_curves(tmp_path: Path):
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
    scaling_models = {
        row["model"]
        for row in payload["runs"]
        if row["experiment_id"] == "p0_calibration_size_scaling"
    }
    seed_models = {
        row["model"]
        for row in payload["runs"]
        if row["experiment_id"] == "p0_seed_robustness"
    }
    assert {"qwen25_7b", "qwen25_14b_awq"} <= scaling_models
    assert {"qwen25_7b", "qwen25_14b_awq"} <= seed_models
