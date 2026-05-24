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

## cluster-side skills

All three write only into the drop folder; `vault-sync`'s boundary check
enforces this on push.

- `/vault-sync` (`.agents/skills/vault-sync/SKILL.md`) — pull-rebase the
  vault and push the drop folder. Push mid-session if needed; otherwise
  the cluster's `Stop` hook and cron timer handle pull and push
  automatically.
- `/code-notes-diff` (`.agents/skills/code-notes-diff/SKILL.md`) — audit
  an experiment repo against vault experiments, claims, and roadmap.
  Writes one divergence report to the drop folder. Strictly descriptive;
  laptop-side triage decides what (if anything) becomes durable.
- `/run-summary` (`.agents/skills/run-summary/SKILL.md`) — summarize a
  single run's config + metrics + short logs into a structured draft in
  the drop folder. Uses `status: drop` so it is never mistaken for a
  durable experiment note; promoted laptop-side via `PROMPTS.md` §24.

## laptop-side triage

Drops are not durable until a laptop session triages them. Use existing
`PROMPTS.md` workflows: §2 / §3 (Inbox Triage / Apply) for general drops,
§24 (Code-to-Vault Experiment Sync) to promote run drafts and
missing-summary findings, §19 (Roadmap Update) for confirmed stale
roadmap entries, §20 (Archive Planner) for ghost refs.
