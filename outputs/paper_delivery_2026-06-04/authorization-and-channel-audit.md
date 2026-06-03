# Authorization And Channel Audit

Date: 2026-06-04

## Summary

The unfinished authorization work is not all the same state. Current strict
status:

| Channel | Status | Evidence / Missing Item |
|---|---|---|
| GitHub | Usable | Repo is public at `https://github.com/rui4399/eigenskill-research-pack`; local `git`/`gh` remains the reliable update path for the current checkout. |
| Notion | OAuth completed, write tools not visible in current session | `codex mcp list` previously showed `notion https://mcp.notion.com/mcp enabled OAuth`, but current `tool_search` still does not expose Notion create/update/fetch tools, so current session likely needs MCP/tool hot reload or Codex restart. |
| NotebookLM Enterprise | Not configured | Enterprise API check reported missing `NOTEBOOKLM_PROJECT_NUMBER` / location. Personal NotebookLM browser flow is separate and not a callable API here. |
| WeChat | Currently blocked at final send step | Earlier ZIP delivery worked, but the current text send and DOCX send both fail with `sendmessage failed: ret=-2`. The DOCX upload itself succeeds; final send fails even after the file sender's context-refresh retry. |

## What Is Still Missing

1. **Notion write capability inside this current Codex session.**
   OAuth is completed, but the callable Notion MCP tools are not exposed. The
   safe fallback is to generate a Notion-ready Markdown page now and write it
   after the session/tool layer refreshes.

2. **WeChat fresh context for delivery.**
   Current send attempts fail with `ret=-2`. Local bridge guidance for this
   error is to ask the user to send any fresh WeChat message, then retry; relogin
   may be needed if a fresh message does not repair the target context.

3. **NotebookLM Enterprise configuration.**
   Missing project number and location. Unless the user provides/sets Google
   Cloud project configuration, NotebookLM Enterprise cannot be used through the
   API.

4. **NotebookLM Enterprise configuration.**
   The personal/browser NotebookLM source workflow is separate from Enterprise
   API access. Enterprise remains blocked until project number/location are
   configured.

5. **Submission-grade experiment evidence.**
   The current package is a stronger research draft plus artifacts. A real
   CCF-A attempt still needs quantized-model PPL/accuracy, latency/memory, and
   GPTQ/AWQ/SmoothQuant/rotation baselines.

## Current Safe Fallbacks

- Notion: use `outputs/paper_delivery_2026-06-04/notion_ready/EigenSkill-Q_Notion_Page.md`.
- NotebookLM: keep source links and paper references in the repo; do not claim
  NotebookLM Enterprise ingestion.
- WeChat: retry after a fresh inbound WeChat message from the user; the current
  DOCX path is
  `outputs/paper_delivery_2026-06-04/EigenSkill-Q_CCF-A_Draft_v2_Loss_Sensitive.docx`.
- GitHub: commit and push through local `git` / `gh`; verify the exact latest
  commit with `git rev-parse HEAD` after each push.
