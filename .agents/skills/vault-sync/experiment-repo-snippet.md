# Experiment-Repo Bootstrap Snippet

Paste the block below into each experiment repo's `CLAUDE.md` (and/or
`AGENTS.md`) on the cluster. It tells any agent launched in that repo to
land on the vault as a knowledge store before doing anything else.

This file is *not* a skill (no `SKILL.md`, no `/slash` invocation). It is
versioned here as the canonical source of the snippet so updates stay in
one place; the actual install is manual, per experiment repo.

---

## Snippet to paste

```md
## Cluster-side: vault knowledge store

This repo runs on the cluster. The research vault is checked out at
`$VAULT_DIR` (default `$HOME/vault`).

Before working on this repo:

1. Read `$VAULT_DIR/CLUSTER.md`.
2. Read `$VAULT_DIR/02-projects/surf/moc.md` and
   `$VAULT_DIR/02-projects/surf/roadmap.md` for active research framing.

You may **only** write under
`$VAULT_DIR/00-inbox/cluster/<hostname>/<YYYY-MM-DD>/`. Everything else
in the vault is read-only from here. The `vault-sync` script enforces
this on push.

Available vault skills (invoke via `/<name>`):

- `/vault-sync` — pull-rebase the vault and push the drop folder.
- `/code-notes-diff` — audit code vs vault state; report into the drop
  folder.
- `/run-summary` — summarize a single run into the drop folder.

Laptop-side triage promotes drops into durable notes via
`PROMPTS.md` §24 / §2 / §3. Do not attempt to promote from the cluster.
```

---

## When to update

- Add a new cluster-side skill → extend the "Available vault skills" list.
- Vault layout changes (e.g., active project renamed) → update the
  step-2 path.
- Drop-folder convention changes → update the write-boundary line.

After updating this file, paste the new block into each experiment repo's
agent config. Old copies will not auto-update.
