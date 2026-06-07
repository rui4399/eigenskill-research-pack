#!/usr/bin/env python3
from __future__ import annotations

"""Gate paper-draft alignment with committed evidence artifacts."""

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


DEFAULT_REQUIRED_REFERENCES = (
    "outputs/real_system_packer_2026-06-05/EVIDENCE_LEDGER_2026_06_06.md",
    "outputs/CALIBRATION_INSTABILITY_BENCHMARK_2026_06_06.md",
    "outputs/SENSITIVITY_PERTURBATION_MATRIX_QWEN25_2026_06_07.md",
    "outputs/CALIBRATION_SEED_STABILITY_QWEN25_0P5B_2026_06_07.md",
    "outputs/CSI_VS_N_CURVE_QWEN25_0P5B_2026_06_07.md",
    "outputs/CSI_TREND_SIGNIFICANCE_QWEN25_0P5B_2026_06_07.md",
    "outputs/CSI_NULL_PERMUTATION_QWEN25_0P5B_2026_06_07.md",
    "outputs/RANK_INVERSION_THEORY_QWEN25_0P5B_2026_06_07.md",
    "outputs/CALIBRATION_ROBUSTNESS_STRESS_GATE_2026_06_07.md",
    "outputs/CONSENSUS_TRANSFER_BOUNDARY_GATE_2026_06_07.md",
    "outputs/INTERACTION_SWAP_BOUNDARY_GATE_2026_06_07.md",
    "outputs/Q_PALETTE_STYLE_ALLOCATION_FAMILY_GATE_2026_06_06.md",
    "outputs/PUBLIC_TASK_MODEL_LADDER_GATE_2026_06_07.md",
    "outputs/OFFICIAL_PTQ_TASK_RETENTION_SMOKE_MATRIX_2026_06_07.md",
    "outputs/OFFICIAL_PTQ_RUNTIME_PROFILE_2026_06_07.md",
    "outputs/OFFICIAL_PTQ_TASK_SUBSET50_MATRIX_2026_06_07.md",
    "outputs/OFFICIAL_PTQ_SUBSET50_RUNTIME_PROFILE_2026_06_07.md",
    "outputs/OFFICIAL_PTQ_TASK_SUBSET100_MATRIX_2026_06_07.md",
    "outputs/OFFICIAL_PTQ_SUBSET100_RUNTIME_PROFILE_2026_06_07.md",
    "outputs/OFFICIAL_PTQ_TASK_IFEVAL_V2_MATRIX_2026_06_07.md",
    "outputs/OFFICIAL_PTQ_RUNTIME_IFEVAL_V2_PROFILE_2026_06_07.md",
    "outputs/OFFICIAL_PTQ_MATCHED_BASELINE_PACK_QWEN25_0P5B_2026_06_07.md",
    "outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_0P5B_BUNDLE_16_GATE_2026_06_07.md",
    "outputs/OFFICIAL_AWQ_PUBLIC_CALIB_QWEN25_1P5B_BUNDLE_16_GATE_2026_06_07.md",
    "outputs/OFFICIAL_GPTQMODEL_PUBLIC_CALIB_QWEN25_0P5B_BUDGET8_16_GATE_2026_06_07.md",
    "outputs/BASELINE_GAP_DASHBOARD_2026_06_06.md",
    "docs/PAPER_CLAIM_MATRIX.md",
    "docs/SYSTEM_EVIDENCE_GATES.md",
)

FORBIDDEN_STALE_TOKENS = (
    "CODEX_RESUME",
    "RESUME_HANDOFF",
    "notion_ready_update_",
    "wake_up_summary_",
    "nightly_delivery_",
    "EigenSkill-Swarm",
    "EigenSkill-100-Resource",
)

UNSAFE_CLAIM_PATTERNS = (
    re.compile(r"\bSOTA\b", re.IGNORECASE),
    re.compile(r"\bstate[- ]of[- ]the[- ]art\b", re.IGNORECASE),
    re.compile(r"\bproduction\s+(?:Tensor\s+Core\s+)?(?:LLM\s+)?runtime\b", re.IGNORECASE),
    re.compile(r"\breal\s+Redmi\b", re.IGNORECASE),
    re.compile(r"\bboard[- ]level\b", re.IGNORECASE),
    re.compile(r"\bend[- ]to[- ]end\s+(?:TTFT|latency|tokens/s|speed)", re.IGNORECASE),
    re.compile(r"\bfaithful\s+official\s+(?:GPTQ|AWQ|SmoothQuant|QuaRot|SpinQuant)", re.IGNORECASE),
)

NEGATION_TOKENS = (
    "not",
    "no ",
    "non-claim",
    "does not",
    "do not",
    "not yet",
    "not claimed",
    "not a",
    "doesn't",
    "cannot",
    "would need",
    "needed",
    "future",
    "missing",
)

PATH_RE = re.compile(
    r"(?P<path>(?:outputs|docs|paper_drafts|train_python|inference_cpp|data_eval|mobile)/[A-Za-z0-9_./+\-=]+)"
)


def normalize_path(value: str) -> str:
    return value.replace("\\", "/").strip().strip("`'\"")


def clean_extracted_path(value: str) -> str:
    cleaned = normalize_path(value)
    while cleaned and cleaned[-1] in ".,;:)":
        cleaned = cleaned[:-1]
    while cleaned.endswith("\\"):
        cleaned = cleaned[:-1]
    return cleaned


def extract_repo_paths(text: str) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for match in PATH_RE.finditer(text):
        path = clean_extracted_path(match.group("path"))
        if path and path not in seen:
            seen.add(path)
            out.append(path)
    return out


def line_is_negated(line: str) -> bool:
    lower = line.lower()
    return any(token in lower for token in NEGATION_TOKENS)


def find_unsafe_claims(lines: Iterable[str]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for lineno, line in enumerate(lines, start=1):
        for pattern in UNSAFE_CLAIM_PATTERNS:
            if pattern.search(line) and not line_is_negated(line):
                findings.append({"line": lineno, "pattern": pattern.pattern, "text": line.strip()})
    return findings


def load_ledger_gate_count(path: Path | None) -> int | None:
    if path is None:
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    value = payload.get("gate_count")
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def text_mentions_gate_count(text: str, gate_count: int) -> bool:
    slash = re.compile(rf"\b{gate_count}\s*/\s*{gate_count}\b")
    words = re.compile(rf"\b{gate_count}\s+(?:executable\s+)?gates\b", re.IGNORECASE)
    return bool(slash.search(text) or words.search(text))


def build_report(
    root: Path,
    paper: Path,
    *,
    required_references: tuple[str, ...] = DEFAULT_REQUIRED_REFERENCES,
    ledger_json: Path | None = None,
    expected_gate_count: int | None = None,
) -> dict[str, Any]:
    paper_path = root / paper
    text = paper_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    extracted_paths = extract_repo_paths(text)
    missing_references = [ref for ref in required_references if ref not in text]
    missing_paths = [path for path in extracted_paths if not (root / path).exists()]
    stale_tokens = [
        {"token": token, "count": text.count(token)}
        for token in FORBIDDEN_STALE_TOKENS
        if token in text
    ]
    unsafe_claims = find_unsafe_claims(lines)
    gate_count = expected_gate_count if expected_gate_count is not None else load_ledger_gate_count(root / ledger_json if ledger_json else None)
    gate_count_mentioned = True if gate_count is None else text_mentions_gate_count(text, gate_count)

    failures: list[str] = []
    if missing_references:
        failures.append(f"missing required evidence references: {len(missing_references)}")
    if missing_paths:
        failures.append(f"referenced repo paths missing: {len(missing_paths)}")
    if stale_tokens:
        failures.append(f"stale forbidden tokens: {len(stale_tokens)}")
    if unsafe_claims:
        failures.append(f"unsafe non-negated claim lines: {len(unsafe_claims)}")
    if not gate_count_mentioned:
        failures.append(f"paper does not mention current ledger gate count: {gate_count}")

    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "paper": str(paper),
            "required_reference_count": len(required_references),
            "missing_required_reference_count": len(missing_references),
            "referenced_repo_path_count": len(extracted_paths),
            "missing_referenced_path_count": len(missing_paths),
            "stale_token_count": len(stale_tokens),
            "unsafe_claim_count": len(unsafe_claims),
            "ledger_gate_count": gate_count,
            "ledger_gate_count_mentioned": gate_count_mentioned,
        },
        "failures": failures,
        "missing_required_references": missing_references,
        "missing_referenced_paths": missing_paths,
        "stale_tokens": stale_tokens,
        "unsafe_claims": unsafe_claims,
        "referenced_paths": extracted_paths,
        "interpretation": (
            "This gate verifies that the paper draft cites committed evidence artifacts, "
            "does not reference removed process files, and keeps high-risk claims inside "
            "explicit non-claim or limitation language."
        ),
    }


def write_markdown(path: Path, report: dict[str, Any]) -> None:
    summary = report["summary"]
    lines = [
        "# Paper Evidence Alignment Gate",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{'PASS' if report['passed'] else 'FAIL'}**",
        "",
        "## Summary",
        "",
        f"- paper: `{summary['paper']}`",
        f"- required evidence references: `{summary['required_reference_count']}`",
        f"- missing required references: `{summary['missing_required_reference_count']}`",
        f"- referenced repo paths: `{summary['referenced_repo_path_count']}`",
        f"- missing referenced paths: `{summary['missing_referenced_path_count']}`",
        f"- stale forbidden tokens: `{summary['stale_token_count']}`",
        f"- unsafe claim lines: `{summary['unsafe_claim_count']}`",
        f"- ledger gate count: `{summary['ledger_gate_count']}`",
        f"- ledger gate count mentioned: `{summary['ledger_gate_count_mentioned']}`",
        "",
        "## Missing Required References",
        "",
    ]
    if report["missing_required_references"]:
        lines.extend(f"- `{path}`" for path in report["missing_required_references"])
    else:
        lines.append("- none")
    lines.extend(["", "## Missing Referenced Paths", ""])
    if report["missing_referenced_paths"]:
        lines.extend(f"- `{path}`" for path in report["missing_referenced_paths"])
    else:
        lines.append("- none")
    lines.extend(["", "## Unsafe Claim Lines", ""])
    if report["unsafe_claims"]:
        for item in report["unsafe_claims"]:
            lines.append(f"- line `{item['line']}`: {item['text']}")
    else:
        lines.append("- none")
    lines.extend(["", "## Failures", ""])
    if report["failures"]:
        lines.extend(f"- {failure}" for failure in report["failures"])
    else:
        lines.append("- none")
    lines.extend(["", "## Interpretation", "", report["interpretation"]])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate paper/evidence alignment.")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--paper", type=Path, required=True)
    parser.add_argument("--ledger-json", type=Path)
    parser.add_argument("--expected-gate-count", type=int)
    parser.add_argument("--required-reference", action="append", default=[])
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    required = tuple(args.required_reference) if args.required_reference else DEFAULT_REQUIRED_REFERENCES
    root = args.root.resolve()
    report = build_report(
        root,
        args.paper,
        required_references=required,
        ledger_json=args.ledger_json,
        expected_gate_count=args.expected_gate_count,
    )
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, report)
    print(json.dumps({"passed": report["passed"], "summary": report["summary"], "failures": report["failures"]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
