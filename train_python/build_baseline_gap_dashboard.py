#!/usr/bin/env python3
from __future__ import annotations

"""Build a reviewer-facing dashboard for baseline and readiness gaps.

The dashboard is intentionally not a success gate. Its job is to keep missing
external baselines visible and machine-checkable, so the repository cannot drift
from "known gap" to accidental paper claim.
"""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_path(path: Path) -> str:
    return path.as_posix()


def package_availability(audit: dict[str, Any]) -> dict[str, dict[str, Any]]:
    packages: dict[str, dict[str, Any]] = {}
    for item in audit.get("packages", []) or []:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name", ""))
        if name:
            packages[name] = item
    return packages


def evidence_matches(root: Path, patterns: list[str]) -> list[str]:
    matches: set[str] = set()
    for pattern in patterns:
        for path in root.glob(pattern):
            if path.is_file():
                matches.add(normalize_path(path.relative_to(root)))
    return sorted(matches)


def task_count_from_payload(payload: dict[str, Any]) -> int:
    for key in ("task_count", "total", "tasks"):
        value = payload.get(key)
        if isinstance(value, int):
            return value
    for split in ("baseline", "fused"):
        aggregate = payload.get(split, {}).get("aggregate", {}) if isinstance(payload.get(split), dict) else {}
        value = aggregate.get("tasks")
        if isinstance(value, int):
            return value
    summary = payload.get("summary", {})
    if isinstance(summary, dict):
        value = summary.get("tasks")
        if isinstance(value, int):
            return value
    return 0


def total_task_count(root: Path, matches: list[str]) -> int:
    total = 0
    for match in matches:
        path = root / match
        if path.suffix.lower() != ".json":
            continue
        try:
            payload = load_json(path)
        except (OSError, json.JSONDecodeError):
            continue
        total += task_count_from_payload(payload)
    return total


def packages_ok(required: list[str], available: dict[str, dict[str, Any]], mode: str) -> bool:
    if not required:
        return True
    flags = [bool(available.get(name, {}).get("available")) for name in required]
    if mode == "all":
        return all(flags)
    if mode == "any":
        return any(flags)
    raise ValueError(f"unsupported package mode: {mode}")


def package_summary(required: list[str], available: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for name in required:
        item = available.get(name, {})
        rows.append(
            {
                "name": name,
                "available": bool(item.get("available")),
                "version": str(item.get("version", "")),
            }
        )
    return rows


def classify_item(
    item: dict[str, Any],
    matches: list[str],
    partial_matches: list[str],
    package_ok: bool,
    task_count: int = 0,
) -> str:
    min_total_tasks = int(item.get("min_total_tasks", 0) or 0)
    task_threshold_ok = not min_total_tasks or task_count >= min_total_tasks
    if matches and package_ok:
        return "covered" if task_threshold_ok else "partial"
    if matches and not package_ok:
        return "evidence_without_package_audit"
    if partial_matches and package_ok:
        return "partial"
    if partial_matches and not package_ok:
        return "partial_without_package_audit"
    if not matches and package_ok and item.get("required_packages"):
        return "package_only"
    return "missing"


def evaluate_manifest(root: Path, manifest: dict[str, Any], audit: dict[str, Any]) -> dict[str, Any]:
    available = package_availability(audit)
    items: list[dict[str, Any]] = []
    for item in manifest.get("items", []) or []:
        if not isinstance(item, dict):
            raise ValueError("manifest items must be objects")
        required_globs = [str(pattern) for pattern in item.get("required_evidence_globs", []) or []]
        partial_globs = [str(pattern) for pattern in item.get("partial_evidence_globs", []) or []]
        required_packages = [str(name) for name in item.get("required_packages", []) or []]
        mode = str(item.get("package_mode", "any"))
        matches = evidence_matches(root, required_globs)
        partial_matches = evidence_matches(root, partial_globs)
        task_count = total_task_count(root, matches)
        package_ok = packages_ok(required_packages, available, mode)
        status = classify_item(item, matches, partial_matches, package_ok, task_count)
        row = dict(item)
        row["status"] = status
        row["evidence_count"] = len(matches)
        row["evidence_task_count"] = task_count
        row["evidence_matches"] = matches[:20]
        row["evidence_truncated"] = len(matches) > 20
        row["partial_evidence_count"] = len(partial_matches)
        row["partial_evidence_matches"] = partial_matches[:20]
        row["partial_evidence_truncated"] = len(partial_matches) > 20
        row["package_ok"] = package_ok
        row["package_summary"] = package_summary(required_packages, available)
        items.append(row)

    status_counts: dict[str, int] = {}
    family_counts: dict[str, dict[str, int]] = {}
    blocker_missing: list[str] = []
    for item in items:
        status = str(item["status"])
        family = str(item.get("family", "unknown"))
        status_counts[status] = status_counts.get(status, 0) + 1
        family_counts.setdefault(family, {})
        family_counts[family][status] = family_counts[family].get(status, 0) + 1
        if item.get("paper_blocker") and status != "covered":
            blocker_missing.append(str(item.get("id")))

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "schema_version": manifest.get("schema_version"),
        "passed": not blocker_missing,
        "item_count": len(items),
        "status_counts": status_counts,
        "family_counts": family_counts,
        "paper_blocker_missing": blocker_missing,
        "items": items,
        "interpretation": {
            "covered": "At least one committed artifact matched the manifest evidence pattern and required packages are available or not needed.",
            "partial": "Only a narrower substitute artifact exists, or the matched task artifacts are below the configured task-count threshold.",
            "package_only": "A required package family is available, but no committed comparison artifact exists yet.",
            "evidence_without_package_audit": "A committed artifact exists, but the package audit does not show the expected package family.",
            "partial_without_package_audit": "A narrower substitute artifact exists, but the package audit does not show the expected package family.",
            "missing": "No committed artifact and no package-only readiness signal.",
        },
    }


def write_markdown(path: Path, dashboard: dict[str, Any]) -> None:
    lines = [
        "# Baseline Gap Dashboard",
        "",
        f"Date: `{dashboard['date']}`",
        f"Status: **{'READY' if dashboard['passed'] else 'NOT READY'}** for paper claims that require external baselines",
        f"Items: `{dashboard['item_count']}`",
        "",
        "## Status Counts",
        "",
        "| status | count |",
        "|---|---:|",
    ]
    for status, count in sorted(dashboard["status_counts"].items()):
        lines.append(f"| `{status}` | {count} |")

    lines.extend(["", "## Missing Paper Blockers", ""])
    if dashboard["paper_blocker_missing"]:
        for item_id in dashboard["paper_blocker_missing"]:
            lines.append(f"- `{item_id}`")
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Baseline Items",
            "",
            "| id | family | priority | blocker | status | evidence | tasks | partial | packages | boundary |",
            "|---|---|---|---:|---|---:|---:|---:|---|---|",
        ]
    )
    for item in dashboard["items"]:
        packages = ", ".join(
            f"{pkg['name']}={'yes' if pkg['available'] else 'no'}"
            for pkg in item.get("package_summary", [])
        )
        if not packages:
            packages = "n/a"
        boundary = str(item.get("claim_boundary", "")).replace("|", "\\|")
        lines.append(
            f"| `{item.get('id')}` | {item.get('family')} | {item.get('priority')} | "
            f"{bool(item.get('paper_blocker'))} | **{item.get('status')}** | "
            f"{item.get('evidence_count')} | {item.get('evidence_task_count', 0)} | "
            f"{item.get('partial_evidence_count', 0)} | {packages} | {boundary} |"
        )

    lines.extend(
        [
            "",
            "## Claim Boundary",
            "",
            "- This dashboard is a gap index, not an evidence ledger.",
            "- `NOT READY` means at least one paper-blocking external baseline, public task benchmark, or deployment claim is still missing.",
            "- A missing row should be reported as future work unless a committed artifact is added and the dashboard is regenerated.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build baseline/readiness gap dashboard.")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--baseline-audit", type=Path, default=Path("outputs/baseline_environment_audit.json"))
    parser.add_argument("--out-json", type=Path, default=Path("outputs/baseline_gap_dashboard.json"))
    parser.add_argument("--out-md", type=Path, default=Path("outputs/BASELINE_GAP_DASHBOARD.md"))
    parser.add_argument("--strict", action="store_true", help="Exit nonzero when paper-blocking items are missing.")
    args = parser.parse_args()

    root = args.root.resolve()
    manifest = load_json(args.manifest)
    audit = load_json(args.baseline_audit) if args.baseline_audit.exists() else {"packages": []}
    dashboard = evaluate_manifest(root, manifest, audit)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(dashboard, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, dashboard)
    print(
        json.dumps(
            {
                "passed": dashboard["passed"],
                "item_count": dashboard["item_count"],
                "status_counts": dashboard["status_counts"],
                "paper_blocker_missing": dashboard["paper_blocker_missing"],
                "out_json": str(args.out_json),
                "out_md": str(args.out_md),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    raise SystemExit(1 if args.strict and not dashboard["passed"] else 0)


if __name__ == "__main__":
    main()
