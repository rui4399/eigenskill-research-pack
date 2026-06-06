# Historical Artifacts

This repository used to track generated delivery bundles, private Obsidian and
NotebookLM exports, and early speculative research packs. They were removed
from the public tree because they are not part of the current reproducible
artifact boundary.

The current public repository should contain:

- source code for C++ and Python checks;
- small synthetic fixtures and no-leak evaluation data;
- selected evidence JSON/Markdown reports;
- format specifications, claim boundaries, and paper-readiness notes.

It should not contain:

- generated `.docx`, `.pdf`, or `.zip` delivery bundles;
- private NotebookLM or Obsidian exports;
- Codex resume handoff files, wake-up summaries, Notion-ready update snippets,
  or nightly delivery notes;
- old speculative paper packs about acoustic communication, physical swarm
  assembly, or unvalidated eigen-routing claims.

The removed files remain recoverable from Git history if needed, but they
should not be treated as current project evidence.

The hygiene gate intentionally rejects these process artifacts so the public
branch stays focused on source code, fixtures, evidence gates, and claim
boundaries.
