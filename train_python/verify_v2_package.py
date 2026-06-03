import argparse
import json
import subprocess
import sys
from pathlib import Path


DEFAULT_REQUIRED_PATHS = [
    "models/eigenskill-smollm2-360m-lora-v2-fp16/adapter_model.safetensors",
    "models/eigenskill-smollm2-360m-merged-v2-fp16/model.safetensors",
    "models/eigenskill-smollm2-360m-int8-v2-dynamic/pytorch_model_int8_dynamic_state_dict.pt",
    "outputs/eigenskill_v2_eval.json",
    "outputs/eigenskill_v2_hybrid_eval.json",
    "outputs/eigenskill_v2_hybrid_eval_recheck.json",
    "outputs/EigenSkill-v2-Hybrid-Training-Report.md",
    "outputs/EigenSkill-v2-Notion-Summary.md",
    "train_python/run_hybrid_skill.py",
]


def rel(root, path):
    return str(Path(path).resolve().relative_to(root.resolve())).replace("\\", "/")


def file_record(root, path):
    full = root / path
    exists = full.exists()
    record = {
        "path": str(path).replace("\\", "/"),
        "exists": exists,
        "bytes": full.stat().st_size if exists and full.is_file() else None,
    }
    if exists and full.is_file():
        record["last_write_time"] = full.stat().st_mtime
    return record


def summarize_eval(path):
    result = json.loads(path.read_text(encoding="utf-8"))
    total = 0
    exact = 0
    overrides = 0
    by_skill = {}
    for skill, value in result["summary"].items():
        n = int(value["n"])
        skill_exact = int(round(float(value["exact"]) * n))
        total += n
        exact += skill_exact
        overrides += int(value.get("hybrid_overrides", 0))
        by_skill[skill] = {
            "n": n,
            "exact": skill_exact,
            "accuracy": float(value["exact"]),
            "hybrid_overrides": int(value.get("hybrid_overrides", 0)),
        }
    return {
        "total": total,
        "exact": exact,
        "accuracy": exact / total if total else 0.0,
        "hybrid_overrides": overrides,
        "by_skill": by_skill,
    }


def run_command(root, command):
    proc = subprocess.run(
        command,
        cwd=root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
    )
    return {
        "command": command,
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }


def verify(root, out_path):
    records = [file_record(root, Path(path)) for path in DEFAULT_REQUIRED_PATHS]
    missing = [item["path"] for item in records if not item["exists"]]

    pure_eval = summarize_eval(root / "outputs/eigenskill_v2_eval.json")
    hybrid_eval = summarize_eval(root / "outputs/eigenskill_v2_hybrid_eval.json")
    recheck_eval = summarize_eval(root / "outputs/eigenskill_v2_hybrid_eval_recheck.json")

    bypass_check = run_command(
        root,
        [
            sys.executable,
            "train_python/run_hybrid_skill.py",
            "--skill",
            "unit_time_normalize",
            "--input",
            "750克是多少千克，只输出JSON",
            "--deterministic-only",
        ],
    )

    package_ok = (
        not missing
        and pure_eval["exact"] == 1391
        and pure_eval["total"] == 1440
        and hybrid_eval["exact"] == 1439
        and hybrid_eval["total"] == 1440
        and recheck_eval["exact"] == 1439
        and recheck_eval["total"] == 1440
        and hybrid_eval["hybrid_overrides"] == 180
        and bypass_check["returncode"] == 0
    )

    manifest = {
        "package": "eigenskill-smollm2-360m-v2-hybrid",
        "package_ok": package_ok,
        "required_files": records,
        "missing_files": missing,
        "eval": {
            "pure_v2": pure_eval,
            "hybrid_v2": hybrid_eval,
            "hybrid_v2_recheck": recheck_eval,
        },
        "checks": {
            "deterministic_bypass_cli": bypass_check,
        },
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def main():
    parser = argparse.ArgumentParser(description="Verify EigenSkill v2 package artifacts and eval metrics.")
    parser.add_argument("--root", default=".")
    parser.add_argument("--out", default="outputs/eigenskill_v2_package_manifest.json")
    args = parser.parse_args()

    manifest = verify(Path(args.root).resolve(), Path(args.out))
    print(json.dumps({"package_ok": manifest["package_ok"], "missing_files": manifest["missing_files"]}, ensure_ascii=False))
    raise SystemExit(0 if manifest["package_ok"] else 1)


if __name__ == "__main__":
    main()
