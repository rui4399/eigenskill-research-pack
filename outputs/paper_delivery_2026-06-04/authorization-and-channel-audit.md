# Authorization And Channel Audit

Date: 2026-06-04

## Summary

The unfinished authorization work is not all the same state. Current strict
status:

| Channel | Status | Evidence / Missing Item |
|---|---|---|
| GitHub | Usable | `gh auth status` previously succeeded for `rui13181593055`; repo is public. Must still push current commit. |
| Notion | OAuth completed, write tools not visible in current session | `codex mcp login notion` previously returned successful login. Current `tool_search` still does not expose Notion create/update/fetch tools, so current session likely needs MCP/tool hot reload or Codex restart. |
| NotebookLM Enterprise | Not configured | Enterprise API check reported missing `NOTEBOOKLM_PROJECT_NUMBER` / location. Personal NotebookLM browser flow is separate and not a callable API here. |
| WeChat | Bridge likely usable; verify immediately before send | Prior maintenance showed live bridge/companion/worker PIDs and fresh poll heartbeat. Must run maintenance again before final file send. |

## What Is Still Missing

1. **Notion write capability inside this current Codex session.**
   OAuth is completed, but the callable Notion MCP tools are not exposed. The
   safe fallback is to generate a Notion-ready Markdown page now and write it
   after the session/tool layer refreshes.

2. **NotebookLM Enterprise configuration.**
   Missing project number and location. Unless the user provides/sets Google
   Cloud project configuration, NotebookLM Enterprise cannot be used through the
   API.

3. **Final WeChat file send evidence.**
   Sending the ZIP must be verified by the bridge tool output. If WeChat returns
   a stale-session error such as `sendmessage failed: ret=-2`, the user needs to
   send one fresh inbound message and the file send should be retried.

4. **GitHub update for this exact stage.**
   The repo was already public before this stage. The current C++ evaluator,
   report, and paper package still need to be committed and pushed.

## Current Safe Fallbacks

- Notion: use `outputs/paper_delivery_2026-06-04/notion_ready/EigenSkill-Q_Notion_Page.md`.
- NotebookLM: keep source links and paper references in the repo; do not claim
  NotebookLM Enterprise ingestion.
- WeChat: use
  `C:\Users\18042\Documents\Codex\2026-05-21\unlinearity-cli-wechat-bridge-codex\tools\wechat-send-file.mjs`.
- GitHub: commit and push through local `git` / `gh`.
