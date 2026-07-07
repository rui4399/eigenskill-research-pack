from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import eval_task_jsonl as task_eval


def test_load_allocation_reads_module_bit_map(tmp_path: Path):
    allocation = tmp_path / "allocation.json"
    allocation.write_text(
        json.dumps(
            {
                "groups": [
                    {"module": "layer.0"},
                    {"module": "layer.1"},
                ],
                "allocations": {"csi_guided": [3, 4]},
            }
        ),
        encoding="utf-8",
    )

    module_bits, payload = task_eval.load_allocation(str(allocation), "csi_guided")

    assert module_bits == {"layer.0": 3, "layer.1": 4}
    assert "allocations" in payload


def test_apply_fake_quant_reports_uniform_bit_histogram():
    torch = pytest.importorskip("torch")
    model = torch.nn.Sequential(torch.nn.Linear(2, 2), torch.nn.ReLU(), torch.nn.Linear(2, 1))

    meta = task_eval.apply_fake_quant(model, "uniform_int3")

    assert meta["linear_modules_touched"] == 2
    assert meta["bit_hist"] == {"3": 2}
