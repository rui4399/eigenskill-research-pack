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


def test_normalize_task_row_supports_gsm8k_question_answer_schema():
    row = {
        "question": "A duck lays 16 eggs and 7 are used. How many remain?",
        "answer": "16 - 7 = <<16-7=9>>9\n#### 9",
    }

    normalized = task_eval.normalize_task_row(row)

    assert "A duck lays" in normalized["prompt"]
    assert normalized["answer"] == "9"
    assert normalized["answer_type"] == "number"


def test_normalize_task_row_supports_mmlu_choice_schema():
    row = {
        "question": "Find the degree for the given field extension.",
        "subject": "abstract_algebra",
        "choices": ["0", "4", "2", "6"],
        "answer": 1,
    }

    normalized = task_eval.normalize_task_row(row)

    assert "A. 0" in normalized["prompt"]
    assert "D. 6" in normalized["prompt"]
    assert normalized["task"] == "abstract_algebra"
    assert normalized["answer"] == "B"
    assert normalized["answer_type"] == "choice"
