---
name: run-summary
description: Cluster-side. Summarize a single experiment run from its config + logs + metrics into a structured draft in the drop folder. Mirrors PROMPTS.md §10 but constrained to what the cluster agent can verify.
---

# Run Summary

Cluster-side skill. Reads one run directory and writes a structured
experiment-summary draft into the drop folder. The draft uses
`status: drop` so it is unambiguously not yet durable; promotion to a
real `experiments/eYYY.md` happens laptop-side via `PROMPTS.md` §24
(Code-to-Vault Experiment Sync).

## when to invoke

- A run just finished and the agent should record observations before
  context is lost.
- A surprising/failed run that should not be repeated.
- An ablation result that warrants a note before the runs directory gets
  cleaned up.

## inputs

- `$VAULT_DIR` (default `$HOME/vault`).
- Run directory: `--run <path>` or auto-detect the most recent under
  `runs/` / `outputs/` / `wandb/`.
- Optional: `--claim <vault path>` or `--experiment <vault path>` for
  hypothesis context.

## procedure

1. Read the run's config, metric summary, and any short log files in the
   run dir. Do not copy raw logs into the summary.
2. If a related vault claim or experiment note was provided, read it for
   hypothesis context.
3. If no related note was provided, *cautiously* infer hypothesis from
   config naming and mark it explicitly as inferred.
4. Distinguish *result* (what the logs/metrics actually show) from
   *interpretation* (cautious one-liner). Per `AGENTS.md` §10.2, the
   logs/configs are higher-trust than any narrative.
5. Use a short stable run-id for the filename: prefer the run dir's own
   ID/timestamp when present.
6. Write to
   `$VAULT_DIR/00-inbox/cluster/<hostname>/<YYYY-MM-DD>/run-<run-id>.md`
   using the template below. Never write anywhere else in the vault.

## discipline

- `status: drop` is a non-standard sentinel — explicitly *not* one of the
  durable experiment statuses (`planned` / `running` / `done` /
  `inconclusive` / `failed` / `superseded`). The laptop triage converts
  `drop` to a real status during promotion.
- Do not fabricate metrics, commands, or commits. If a value cannot be
  read from the run dir, leave the field blank or write `unknown`.
- Do not edit the source claim/experiment note. The summary lives only
  in the drop folder until laptop-side promotion.
- Do not invoke `git` against the vault directly.

## template

```md
---
type: experiment-draft
project: surf
status: drop
source-run: <repo>@<commit>:<run path>
---

# run-<id>

## hypothesis

## setup
- dataset:
- model:
- baselines:
- metric:
- command/config:

## result

## interpretation

## failure

## next

## links
- related claim: [[claims/...]]
- related experiment: [[experiments/...]]
```

## output

```md
## Run summarized
## Source run path
## Drop file written
## Inferred fields (if any)
## Unknown fields (if any)
```

## shared rules

- Read `AGENTS.md` first. Use `PROMPTS.md` as the workflow registry.
- Default to propose-only unless the user explicitly asks to apply.
- Ask permission before creating, rewriting, moving, renaming, deleting,
  or reorganizing persistent notes — none of which this skill should ever
  do; the drop folder is the only valid write target.
- Preserve Obsidian links and valuable messy details.
- Keep filenames short. Use folders, not noisy filename prefixes.
- Use minimal frontmatter only when it helps retrieval.
- Do not invent citations, paper claims, commands, metrics, or results.
- Separate evidence from inference and speculation.
- Never create persistent AI-slop sections such as `Feynman Check` or
  `What I Still Do Not Understand`.
