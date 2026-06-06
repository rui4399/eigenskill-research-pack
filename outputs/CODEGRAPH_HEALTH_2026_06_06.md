# CodeGraph Health Check

Date: `2026-06-06`

## Result

CodeGraph CLI is usable for this repository after `codegraph sync .`.

Observed status after sync:

- files indexed: `139`
- nodes indexed: `2811`
- edges indexed: `5463`
- backend: `node:sqlite`
- journal: `wal`
- lock files: none observed in `.codegraph`

## Verification

Symbol queries against newly added files work:

- `codegraph query "take_records"` returns
  `train_python/build_public_task_smoke.py:37`
- `codegraph query "write_jsonl"` returns
  `train_python/build_public_task_smoke.py:43`
- `codegraph files` lists both
  `train_python/build_public_task_smoke.py` and
  `train_python/test_build_public_task_smoke.py`

The command `codegraph query "build_public_task_smoke"` did not return a match.
This appears to be expected behavior rather than an index failure: `query`
searches symbols more reliably than file stems. Use `codegraph files` for file
name checks.

## MCP Note

Codex configuration already contains an enabled codegraph MCP server. Verified
with `codex mcp list`:

- name: `codegraph`
- command: `C:\Users\18042\AppData\Roaming\npm\codegraph.cmd`
- args: `serve --mcp`
- status: `enabled`

The CLI can also print the generic Codex MCP snippet:

```toml
[mcp_servers.codegraph]
command = "codegraph"
args = ["serve", "--mcp"]
```

The current Codex Desktop session still does not expose codegraph as a callable
MCP tool through `tool_search` (`0` matching tools for `codegraph context search
trace callers callees mcp tools`). This appears to be a current-session tool
discovery/hot-load limitation rather than a repository index failure. The index
itself is healthy, and the practical fallback is to use the `codegraph` CLI until
the desktop session is restarted or MCP tools are refreshed.

`codex doctor` reports MCP configuration as healthy (`15` configured servers,
`0` disabled). Its provider reachability `404` is the local CC Switch `/v1`
probe behavior and is unrelated to codegraph.

Manual stdio MCP probing also succeeds: `initialize` returns server
`codegraph@0.9.9`, and `tools/list` returns the expected tool set:

- `codegraph_search`
- `codegraph_callers`
- `codegraph_callees`
- `codegraph_impact`
- `codegraph_node`
- `codegraph_explore`
- `codegraph_status`
- `codegraph_files`
