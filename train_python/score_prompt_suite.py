#!/usr/bin/env python3
"""Rule-score prompt-suite outputs beyond dense-vs-fused exact text match."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Callable


@dataclass(frozen=True)
class ScoreResult:
    passed: bool
    detail: str


@dataclass(frozen=True)
class Rule:
    name: str
    expected: str
    score: Callable[[str], ScoreResult]


def _clean(text: str) -> str:
    return " ".join((text or "").strip().split())


def _sentence_count(text: str) -> int:
    stripped = _clean(text)
    if not stripped:
        return 0
    parts = [part for part in re.split(r"[.!?]+", stripped) if part.strip()]
    return len(parts)


def _json_objects(text: str) -> list[dict[str, Any]]:
    objects: list[dict[str, Any]] = []
    for match in re.finditer(r"\{.*?\}", text or "", flags=re.DOTALL):
        try:
            value = json.loads(match.group(0))
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            objects.append(value)
    return objects


def _keys_from_prompt(prompt: str) -> list[str]:
    lower = prompt.lower()
    match = re.search(r"keys? ([a-z0-9_, and-]+?)(?: for|\.|$)", lower)
    if not match:
        return []
    raw = match.group(1).replace(" and ", ",")
    return [part.strip().replace("-", "_") for part in raw.split(",") if part.strip()]


def _fields_from_prompt(prompt: str) -> list[str]:
    lower = prompt.lower()
    match = re.search(r"fields? ([a-z0-9_, and-]+?)(?:\.|$)", lower)
    if not match:
        return []
    raw = match.group(1).replace(" and ", ",")
    return [part.strip().replace("-", "_") for part in raw.split(",") if part.strip()]


def _json_key_rule(keys: list[str]) -> Rule:
    required = set(keys)

    def score(text: str) -> ScoreResult:
        for obj in _json_objects(text):
            normalized = {str(key).lower().replace("-", "_") for key in obj}
            if required.issubset(normalized):
                return ScoreResult(True, f"found keys {sorted(required)}")
        return ScoreResult(False, f"missing JSON keys {sorted(required)}")

    return Rule("json_keys", ",".join(keys), score)


def _yaml_field_rule(fields: list[str]) -> Rule:
    required = set(fields)

    def score(text: str) -> ScoreResult:
        found = {m.group(1).lower().replace("-", "_") for m in re.finditer(r"^\s*([A-Za-z0-9_-]+)\s*:", text or "", re.MULTILINE)}
        if required.issubset(found):
            return ScoreResult(True, f"found fields {sorted(required)}")
        return ScoreResult(False, f"missing YAML fields {sorted(required - found)}")

    return Rule("yaml_fields", ",".join(fields), score)


def _int4_byte_rule(values: int) -> Rule:
    expected = values * 4 // 8
    pattern = re.compile(rf"(?<!\d){expected:,}|(?<!\d){expected}(?!\d)")

    def score(text: str) -> ScoreResult:
        normalized = (text or "").replace(",", "")
        ok = bool(re.search(rf"(?<!\d){expected}(?!\d)", normalized)) and bool(re.search(r"\b(byte|bytes|b)\b", normalized, re.I))
        return ScoreResult(ok, f"expected {expected} bytes")

    return Rule(f"byte_count_{values}_int4", f"{expected} bytes", score)


def _average_bit_rule() -> Rule:
    def score(text: str) -> ScoreResult:
        ok = bool(re.search(r"(?<!\d)5(?:\.0+)?(?!\d)", text or ""))
        return ScoreResult(ok, "expected 5 bits")

    return Rule("average_bits_75p4_25p8", "5 bits", score)


def _sentence_rule(expected: int) -> Rule:
    def score(text: str) -> ScoreResult:
        count = _sentence_count(text)
        return ScoreResult(count == expected, f"sentence_count={count}, expected={expected}")

    return Rule(f"sentence_count_{expected}", f"{expected} sentences", score)


def _cpp_signature_rule() -> Rule:
    def score(text: str) -> ScoreResult:
        raw = text or ""
        has_sig = "(" in raw and ")" in raw and (";" in raw or "{" in raw)
        has_cppish = bool(re.search(r"\b(void|int|float|double|size_t|uint8_t|std::|const)\b", raw))
        return ScoreResult(has_sig and has_cppish, "expected C/C++ function-like signature")

    return Rule("cpp_signature", "C++ signature", score)


def _keyword_rule(name: str, keywords: list[str], min_hits: int = 2) -> Rule:
    expected = ",".join(keywords)

    def score(text: str) -> ScoreResult:
        lower = (text or "").lower()
        hits = [kw for kw in keywords if kw in lower]
        return ScoreResult(len(hits) >= min_hits, f"hits={hits}, expected at least {min_hits}")

    return Rule(name, expected, score)


def _contains_all_rule(keywords: list[str]) -> Rule:
    expected = ",".join(keywords)

    def score(text: str) -> ScoreResult:
        lower = (text or "").lower()
        missing = [kw for kw in keywords if kw.lower() not in lower]
        return ScoreResult(not missing, f"missing={missing}")

    return Rule("contains_all", expected, score)


def _regex_rule(pattern: str, expected: str = "") -> Rule:
    compiled = re.compile(pattern, re.I | re.MULTILINE | re.DOTALL)

    def score(text: str) -> ScoreResult:
        return ScoreResult(bool(compiled.search(text or "")), f"pattern={pattern}")

    return Rule("regex", expected or pattern, score)


def _nonempty_rule() -> Rule:
    def score(text: str) -> ScoreResult:
        cleaned = _clean(text)
        ok = len(cleaned) >= 24 and "i cannot" not in cleaned.lower()
        return ScoreResult(ok, f"chars={len(cleaned)}")

    return Rule("nonempty_answer", "non-empty answer", score)


def _expected_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value]
    if isinstance(value, str):
        return [part.strip() for part in value.split(",") if part.strip()]
    return []


def rule_from_spec(spec: dict[str, Any], prompt: str) -> Rule:
    name = str(spec.get("rule", "")).strip()
    expected = spec.get("expected")
    if name == "json_keys":
        return _json_key_rule(_expected_list(expected if expected is not None else spec.get("keys", [])))
    if name == "yaml_fields":
        return _yaml_field_rule(_expected_list(expected if expected is not None else spec.get("fields", [])))
    if name == "contains_all":
        return _contains_all_rule(_expected_list(expected if expected is not None else spec.get("keywords", [])))
    if name == "keyword_min_hits":
        keywords = _expected_list(expected if expected is not None else spec.get("keywords", []))
        min_hits = int(spec.get("min_hits", 2))
        return _keyword_rule("keyword_min_hits", keywords, min_hits)
    if name == "regex":
        pattern = str(spec.get("pattern", expected or ""))
        return _regex_rule(pattern, str(spec.get("expected_label", expected or pattern)))
    if name == "int4_bytes":
        values = int(spec.get("values", 0) or 0)
        if values:
            return _int4_byte_rule(values)
        return _regex_rule(str(spec.get("pattern", r"\b\d+\s*bytes?\b")), str(expected or "packed byte count"))
    if name == "average_bits_75p4_25p8":
        return _average_bit_rule()
    if name == "sentence_count":
        return _sentence_rule(int(expected))
    if name == "cpp_signature":
        return _cpp_signature_rule()
    if name == "nonempty_answer":
        return _nonempty_rule()
    return rule_for_prompt(prompt)


def load_expected_specs(path: Path) -> dict[str, dict[Any, dict[str, Any]]]:
    by_id: dict[Any, dict[str, Any]] = {}
    by_prompt: dict[str, dict[str, Any]] = {}
    if not path:
        return {"by_id": by_id, "by_prompt": by_prompt}
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        try:
            spec = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSONL at {path}:{line_no}: {exc}") from exc
        if "id" in spec:
            by_id[spec["id"]] = spec
        if "prompt" in spec:
            by_prompt[str(spec["prompt"])] = spec
    return {"by_id": by_id, "by_prompt": by_prompt}


def spec_for_row(row: dict[str, Any], specs: dict[str, dict[Any, dict[str, Any]]] | None) -> dict[str, Any] | None:
    if not specs:
        return None
    row_id = row.get("id")
    if row_id in specs["by_id"]:
        return specs["by_id"][row_id]
    prompt = str(row.get("prompt", ""))
    return specs["by_prompt"].get(prompt)


def rule_for_prompt(prompt: str) -> Rule:
    lower = prompt.lower()
    keys = _keys_from_prompt(prompt)
    if "json" in lower and keys:
        return _json_key_rule(keys)
    fields = _fields_from_prompt(prompt)
    if "yaml" in lower and fields:
        return _yaml_field_rule(fields)
    int4_match = re.search(r"(\d+)\s+(?:signed\s+)?(?:4-bit|four-bit|int4)", lower)
    if int4_match and ("byte" in lower or "packed" in lower):
        return _int4_byte_rule(int(int4_match.group(1)))
    if "average bit width" in lower and "75 percent" in lower and "25 percent" in lower:
        return _average_bit_rule()
    if "exactly one sentence" in lower or lower.startswith("in exactly one sentence"):
        return _sentence_rule(1)
    if "exactly two sentences" in lower or "two sentences" in lower:
        return _sentence_rule(2)
    if "c++" in lower and ("signature" in lower or "declaration" in lower or "prototype" in lower):
        return _cpp_signature_rule()
    if "prompt-split instability" in lower:
        return _keyword_rule("prompt_split_instability", ["prompt", "split", "instabil"], 3)
    if "kv-cache drift" in lower or "hidden-state drift" in lower:
        return _keyword_rule("drift_proxy", ["drift", "proxy", "state", "cache"], 2)
    if "speed evidence" in lower and "quality evidence" in lower:
        return _keyword_rule("speed_quality_plan", ["speed", "quality", "experiment"], 2)
    if "readme" in lower or "warning" in lower or "caveat" in lower:
        return _keyword_rule("claim_caveat", ["not", "claim", "speed", "latency", "compression"], 2)
    if "selected-row kernel" in lower:
        return _keyword_rule("selected_row_kernel", ["selected", "row", "kernel", "benchmark", "decode"], 2)
    if "reconstruction error" in lower:
        return _keyword_rule("reconstruction_vs_generation", ["reconstruction", "generation", "attention", "row"], 2)
    if "layer 0" in lower:
        return _keyword_rule("layer0_policy", ["layer", "0", "qkv", "quality", "fallback"], 2)
    if "triton" in lower and "dense gemm" in lower:
        return _keyword_rule("triton_dense_shape", ["triton", "dense", "gemm", "batch", "launch"], 2)
    if "baseline, full-v8, and rowguard" in lower:
        return _keyword_rule("candidate_choice", ["baseline", "full", "rowguard"], 2)
    return _nonempty_rule()


def _score_text(rule: Rule, text: str) -> dict[str, Any]:
    result = rule.score(text or "")
    return {"passed": result.passed, "detail": result.detail}


def score_file(path: Path, expected_specs: dict[str, dict[Any, dict[str, Any]]] | None = None) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for row in payload.get("rows", []):
        spec = spec_for_row(row, expected_specs)
        rule = rule_from_spec(spec, str(row.get("prompt", ""))) if spec else rule_for_prompt(str(row.get("prompt", "")))
        baseline_text = str(row.get("baseline", {}).get("generated_text", ""))
        fused_text = str(row.get("fused", {}).get("generated_text", ""))
        baseline_score = _score_text(rule, baseline_text)
        fused_score = _score_text(rule, fused_text)
        rows.append(
            {
                "id": row.get("id"),
                "prompt": row.get("prompt", ""),
                "rule": rule.name,
                "expected": rule.expected,
                "expected_spec_id": spec.get("id") if spec else None,
                "baseline": baseline_score,
                "fused": fused_score,
                "preserved": bool(baseline_score["passed"] and fused_score["passed"]),
                "regressed": bool(baseline_score["passed"] and not fused_score["passed"]),
                "improved": bool((not baseline_score["passed"]) and fused_score["passed"]),
            }
        )
    prompts = len(rows)
    baseline_passes = sum(1 for row in rows if row["baseline"]["passed"])
    fused_passes = sum(1 for row in rows if row["fused"]["passed"])
    aggregate = {
        "prompts": prompts,
        "baseline_passes": baseline_passes,
        "fused_passes": fused_passes,
        "baseline_pass_rate": baseline_passes / max(prompts, 1),
        "fused_pass_rate": fused_passes / max(prompts, 1),
        "preserved_passes": sum(1 for row in rows if row["preserved"]),
        "regressions": sum(1 for row in rows if row["regressed"]),
        "improvements": sum(1 for row in rows if row["improved"]),
        "rule_count": len({row["rule"] for row in rows}),
    }
    return {"source": str(path), "aggregate": aggregate, "rows": rows}


def render_markdown(result: dict[str, Any]) -> str:
    agg = result["aggregate"]
    lines = [
        "# Scored Prompt Suite",
        "",
        f"Source: `{result['source']}`",
        "",
        "## Aggregate",
        "",
        "| metric | value |",
        "|---|---:|",
        f"| prompts | {agg['prompts']} |",
        f"| baseline passes | {agg['baseline_passes']} / {agg['prompts']} |",
        f"| fused passes | {agg['fused_passes']} / {agg['prompts']} |",
        f"| baseline pass rate | {agg['baseline_pass_rate']:.4f} |",
        f"| fused pass rate | {agg['fused_pass_rate']:.4f} |",
        f"| preserved passes | {agg['preserved_passes']} |",
        f"| regressions | {agg['regressions']} |",
        f"| improvements | {agg['improvements']} |",
        f"| rules used | {agg['rule_count']} |",
        "",
        "## Rows",
        "",
        "| id | rule | baseline | fused | status | expected |",
        "|---:|---|---:|---:|---|---|",
    ]
    for row in result["rows"]:
        status = "preserved" if row["preserved"] else "regressed" if row["regressed"] else "improved" if row["improved"] else "same_fail"
        lines.append(
            f"| {row['id']} | `{row['rule']}` | {str(row['baseline']['passed']).lower()} | "
            f"{str(row['fused']['passed']).lower()} | {status} | {row['expected']} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Rule-score a fused QKV prompt-suite JSON.")
    parser.add_argument("--input-json", required=True)
    parser.add_argument("--expected-jsonl", default="")
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()

    expected_specs = load_expected_specs(Path(args.expected_jsonl)) if args.expected_jsonl else None
    result = score_file(Path(args.input_json), expected_specs=expected_specs)
    out_json = Path(args.out_json)
    out_md = Path(args.out_md)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    out_md.write_text(render_markdown(result), encoding="utf-8")
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md), "aggregate": result["aggregate"]}, indent=2))


if __name__ == "__main__":
    main()
