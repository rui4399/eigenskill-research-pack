import pytest

from train_python.build_awq_activation_csi import (
    build_allocation,
    compare_splits,
    normalize_stats,
)


def test_normalize_stats_ranks_awq_modules_by_activation_scale_product():
    raw = [
        {"module": "b", "in_features": 4, "out_features": 8, "mean_abs_input": 2.0, "mean_abs_scale": 0.5},
        {"module": "a", "in_features": 4, "out_features": 4, "mean_abs_input": 1.0, "mean_abs_scale": 0.25},
    ]

    rows = normalize_stats(raw)

    assert [row["module"] for row in rows] == ["b", "a"]
    assert rows[0]["param_count"] == 32
    assert rows[0]["score"] == pytest.approx(1.0)
    assert rows[0]["rank"] == 1


def test_compare_splits_reports_topk_agreement_and_rank_correlation():
    left = normalize_stats(
        [
            {"module": "a", "in_features": 1, "out_features": 8, "mean_abs_input": 5, "mean_abs_scale": 1},
            {"module": "b", "in_features": 1, "out_features": 8, "mean_abs_input": 4, "mean_abs_scale": 1},
            {"module": "c", "in_features": 1, "out_features": 8, "mean_abs_input": 1, "mean_abs_scale": 1},
        ]
    )
    right = normalize_stats(
        [
            {"module": "b", "in_features": 1, "out_features": 8, "mean_abs_input": 6, "mean_abs_scale": 1},
            {"module": "a", "in_features": 1, "out_features": 8, "mean_abs_input": 4, "mean_abs_scale": 1},
            {"module": "c", "in_features": 1, "out_features": 8, "mean_abs_input": 1, "mean_abs_scale": 1},
        ]
    )

    summary = compare_splits(left, right, top_fraction=2 / 3)

    assert summary["shared_modules"] == 3
    assert summary["top_k"] == 2
    assert summary["top_jaccard"] == pytest.approx(1.0)
    assert summary["spearman"] == pytest.approx(0.5)


def test_build_allocation_respects_average_bit_budget():
    rows = normalize_stats(
        [
            {"module": "big", "in_features": 10, "out_features": 10, "mean_abs_input": 10, "mean_abs_scale": 1},
            {"module": "small", "in_features": 1, "out_features": 10, "mean_abs_input": 9, "mean_abs_scale": 1},
        ]
    )

    allocation = build_allocation(rows, base_bits=2, high_bits=4, budget_avg_bits=3)

    assert allocation["avg_bits"] == pytest.approx(2.1818181818)
    assert allocation["bit_hist"] == {"2": 1, "4": 1}
    assert allocation["bits_by_module"] == {"big": 2, "small": 4}
