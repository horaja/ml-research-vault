---
name: vault-sync
description: Pull-rebase the vault and push only changes under 00-inbox/cluster/. Used on the remote cluster; refuses to push edits outside the drop folder.
---

# Vault Sync

Cluster-side sync skill. The vault is read-only on the cluster except for the
drop folder `00-inbox/cluster/<hostname>/<YYYY-MM-DD>/`. This skill (and the
backing `sync.sh` script) is the only thing on the cluster that touches the
git remote.

## when to invoke

- Manually via `/vault-sync` to push mid-session.
- Automatically via a Claude Code `Stop` hook at end of session (see
  `hook.json.example`).
- On a cron timer for the pull cadence (see `cron.example`).

All three call the same script. The boundary check lives in one place.

## inputs

- `$VAULT_DIR` (defaults to `$HOME/vault` on the cluster) — the vault checkout.

## procedure

1. Run `.agents/skills/vault-sync/sync.sh`.
2. Read its output. If it refused (exit 2), it printed the out-of-bounds
   paths — these are edits outside `00-inbox/cluster/` that must be reverted
   or moved into the drop folder before sync can proceed.
3. Do not invoke `git` directly. Do not attempt to push from agent code.

## write boundary contract

Cluster-side agents may **only** create or modify files under
`00-inbox/cluster/<hostname>/<YYYY-MM-DD>/`. Everything else in the vault is
read-only from the cluster.

Suggested drop contents:

- experiment run summaries (hypothesis, command, result, interpretation)
- log excerpts that surprised the agent
- failed-run notes that should not be repeated
- todo crumbs for the human-in-the-loop to triage

One file per run is fine. Keep filenames short. The laptop-side inbox
workflow (`AGENTS.md` §3.3) promotes drops into durable notes; do not try to
write durable notes from the cluster.

## output

```md
## Sync result
## Pulled commits (if any)
## Pushed drop (host + timestamp, if any)
## Out-of-bounds edits (if refused)
```

## shared rules

- Read `AGENTS.md` first. Use `PROMPTS.md` as the workflow registry if present.
- Default to propose-only unless the user explicitly asks to apply.
- Ask permission before creating, rewriting, moving, renaming, deleting, or
  reorganizing persistent notes.
- Preserve Obsidian links and valuable messy details.
- Keep filenames short. Use folders, not noisy filename prefixes.
- Use minimal frontmatter only when it helps retrieval.
- Do not invent citations, paper claims, commands, metrics, or results.
- Separate evidence from inference and speculation.
- Never create persistent AI-slop sections such as `Feynman Check` or
  `What I Still Do Not Understand`.
