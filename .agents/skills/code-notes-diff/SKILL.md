---
name: code-notes-diff
description: Cluster-side audit. Compare an experiment repo's state against the vault's experiments, claims, and roadmap. Write a single divergence report into the drop folder. Strictly descriptive — no durable-note edits.
---

# Code-Notes Diff

Cluster-side audit skill. The cluster agent reads the vault and the local
experiment repo, then writes one structured divergence report into the
drop folder. Triage and any durable-note updates happen on the laptop via
existing workflows (`PROMPTS.md` §24, §19, §20, §2/§3).

## when to invoke

- Mid-project, when the agent suspects the repo has moved past the notes
  (or vice versa).
- Before a meeting, to surface "what does the vault still claim that the
  code no longer supports?"
- After a refactor, to find ghost references and missing summaries.

## inputs

- `$VAULT_DIR` (default `$HOME/vault`).
- Experiment repo path — default: current working directory.
- Optional scope: `experiments`, `claims`, `roadmap`, or `all` (default).

## procedure

1. Read vault entry points: `AGENTS.md`, `CLUSTER.md`,
   `02-projects/surf/moc.md`, `roadmap.md`, all files under
   `02-projects/surf/experiments/`, `02-projects/surf/claims/`, and the
   run-relevant subset of `02-projects/surf/sources/` when referenced.
2. Scan the experiment repo: `git log -50 --oneline`, presence of
   `configs/`, `runs/` / `outputs/` / `wandb/` (whichever conventions
   the repo uses), the most recent metric summaries if findable, and the
   current `HEAD` commit.
3. For each vault experiment note:
   - If it cites a commit hash, check the commit exists in the repo.
   - If it lists hyperparameters, compare against the latest matching
     config.
   - If it records a metric, compare against the most recent run log.
     Flag discrepancies; do not reinterpret.
4. For each runs/configs artifact in the repo: surface as "missing
   summary" if no vault note references it.
5. For each claim with status `supported` / `weakened` / `falsified`:
   identify the grounding experiment and check the supporting code is
   present.
6. For roadmap "next experiments" entries: classify as
   *stale* (appears done in code) or *phantom* (no matching code).
7. Write a single report to
   `$VAULT_DIR/00-inbox/cluster/<hostname>/<YYYY-MM-DD>/code-notes-diff.md`
   using the format below. Never write anywhere else in the vault.

## discipline

`AGENTS.md` §1.2 ("Source authority and project state") forbids using
local-repo absence as evidence against project-wide claims. Phrase
findings narrowly: "no run dir matching e003 under `<repo>/runs/`" — not
"e003 was never run". This report is a *temporary audit artifact*, not a
durable note; the laptop-side triage decides what (if anything) survives.

Do not invoke `git` against the vault directly. `vault-sync` is the only
thing that touches the vault remote.

## output format

```md
# code-notes diff — <repo>@<commit-short>

## scope
- repo:
- vault project:
- ran at: <UTC timestamp>

## experiments
### missing vault summaries (code exists, no note)
- <run path> — config: <path>, metric: <value if found>

### ghost code refs (note exists, code absent)
- [[experiments/eXXX]] — note cites <commit>, not in repo

### hyperparameter / metric drift
- [[experiments/eXXX]] — note: lr=1e-4; latest config: lr=3e-4

## claims
### claims with no supporting code
- [[claims/foo]] — status=supported, grounded in [[experiments/eXXX]],
  no matching run dir in repo

### implementations with no claim/experiment link
- <module/path> — appears central; no vault claim or experiment cites it

## roadmap
### stale entries
- "<text from roadmap>" — appears done at <run path>

### phantom entries
- "<text>" — no matching configs/runs found

## proposed triage actions (laptop-side)
- promote: <run path> → propose new experiments/eYYY via PROMPTS.md §24
- investigate: <ghost ref> may need archival via §20
- update: roadmap "next experiments" via §19 if stale entries confirmed

## confidence notes
- what this scan could see and what it could not
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
