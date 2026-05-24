# Cluster Agents

This file is for agents running on the remote cluster, where this vault is
checked out at `$VAULT_DIR` (default `$HOME/vault`) as a knowledge store
alongside the experiment repos.

## read first

- `AGENTS.md` — the durable vault rules. All of them still apply.
- `CLAUDE.md` / `GEMINI.md` — agent-specific pointers to `AGENTS.md`.
- `PROMPTS.md` — workflow registry.

## entry points for the active project

- `02-projects/surf/moc.md` — map of content.
- `02-projects/surf/roadmap.md` — current research state.
- `02-projects/surf/questions.md` — open questions.
- `02-projects/surf/reading.md` — reading list and status.

## write boundary

Cluster-side agents may **only** create or modify files under:

```text
00-inbox/cluster/<hostname>/<YYYY-MM-DD>/
```

Everything else in the vault is read-only from the cluster. The
`vault-sync` script (`.agents/skills/vault-sync/sync.sh`) enforces this:
it refuses to push if it sees any modification outside the drop folder.

Do not invoke `git` directly. Do not edit `.obsidian/`. Do not rename or
move files. Do not promote drops into durable notes — triage happens on the
laptop.

## what to drop

- experiment run summaries (hypothesis, command, result, interpretation —
  per `AGENTS.md` §5.9)
- log excerpts that surprised the agent
- failed-run notes that should not be repeated
- todo crumbs for the human-in-the-loop to triage

Keep filenames short. One file per run is fine.

## sync

Use the `/vault-sync` skill (`.agents/skills/vault-sync/SKILL.md`) to push
mid-session. Otherwise the cluster's `Stop` hook and cron timer handle pull
and push automatically.
