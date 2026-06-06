# Redmi K80 Pro Mobile Benchmark Runbook

This runbook converts the current mobile blocker into a reproducible evidence
path. It is not mobile evidence by itself. Do not rename this file to
`*_report.md` and do not create `*summary.json` artifacts until a real device is
connected and measured.

## Claim Boundary

- Valid claim after this runbook: the repository has a harness for collecting
  Redmi K80 Pro device identity, TTFT, tokens/s, peak memory, and thermal logs.
- Invalid claim before a real run: Redmi K80 Pro deployment, phone-side speedup,
  energy reduction, or thermal stability.

## 1. Connect Device

Enable USB debugging on the Redmi K80 Pro, connect it by USB, then verify:

```powershell
adb devices -l
```

The target row must have state `device`. Rows marked `offline` or
`unauthorized` are blockers, not evidence.

## 2. Build The NEON Probe

The current C++ probe is a decode/GEMV microbenchmark, not a full LLM runtime.
Build it with Android NDK or a device-side compiler. Example shape:

```powershell
adb push mobile\redmi_k80_pro\neon_mixed_decode.cpp /data/local/tmp/neon_mixed_decode.cpp
adb shell "cd /data/local/tmp && clang++ -O3 -std=c++17 -march=armv8.2-a+dotprod neon_mixed_decode.cpp -o neon_mixed_decode"
```

If `clang++` is not available on-device, build with the Android NDK on the host
and push the binary instead.

## 3. Collect Device Metrics

Run the collector with a benchmark command that prints one JSON object to
stdout. The JSON must include TTFT, tokens/s, peak memory, and generated token
count. Accepted metric names include:

- `ttft_seconds`, `ttft_s`, or `time_to_first_token_seconds`
- `tokens_per_second`, `tok_s`, or `tps`
- `peak_memory_mb`, `peak_rss_mb`, `peak_pss_mb`, `peak_memory_kb`,
  `peak_rss_kb`, `peak_pss_kb`, `peak_memory_bytes`, `peak_rss_bytes`, or
  `peak_pss_bytes`
- `generated_tokens` or `tokens`

Example:

```powershell
python mobile\redmi_k80_pro\collect_adb_metrics.py `
  --benchmark-command "cd /data/local/tmp && ./neon_mixed_decode --rows 512 --cols 1024 --iters 100" `
  --out-json outputs\redmi_k80_pro_real_device_metrics_YYYY_MM_DD.json `
  --out-md outputs\REDMI_K80_PRO_REAL_DEVICE_METRICS_YYYY_MM_DD.md
```

## 4. Gate Real Evidence

Only after the collector reports `real_device_connected=true`, run:

```powershell
python train_python\gate_mobile_device_metrics.py `
  --input-json outputs\redmi_k80_pro_real_device_metrics_YYYY_MM_DD.json `
  --max-ttft-seconds 30 `
  --min-tokens-per-second 0.1 `
  --min-generated-tokens 1 `
  --out-json outputs\redmi_k80_pro_real_device_metrics_summary.json `
  --out-md mobile\redmi_k80_pro\REDMI_K80_PRO_REAL_DEVICE_METRICS_report.md
```

Those final two paths intentionally match the dashboard evidence globs. Use
them only for real device results.

## 5. Rebuild Readiness Dashboard

```powershell
python train_python\build_baseline_gap_dashboard.py `
  --manifest docs\BASELINE_COVERAGE_MANIFEST.json `
  --baseline-audit outputs\baseline_environment_audit.json `
  --out-json outputs\baseline_gap_dashboard_YYYY_MM_DD.json `
  --out-md outputs\BASELINE_GAP_DASHBOARD_YYYY_MM_DD.md
```

If the dashboard still marks `mobile_redmi_k80_pro` as missing, the paper must
say mobile evidence is not complete yet.
