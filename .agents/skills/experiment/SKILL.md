---
name: experiment
description: Plan experiments before running them and summarize experiment results afterward.
---

# Experiment Workflow

Code repos are the source of truth for runs, logs, configs, and exact results. Obsidian stores compact interpretation linked to code/config/result artifacts.

Always distinguish result from interpretation.

## plan
Include hypothesis, supporting result, weakening/kill result, dataset, model, baselines, metric, ablations, controls, failure modes, command/config plan when available, artifacts, and proposed Obsidian summary path.

Prioritize clean baselines over impressive experiments.

## summary
Do not copy raw logs into Obsidian. Include hypothesis, setup, dataset, model, baselines, metric, command/config link, result, interpretation, failure analysis, next action, and baseline that would kill the claim.

If the run is inconclusive, say so.

## template
```md
---
type: experiment
project: surf
status: planned
---

# e001

## hypothesis
## setup
## baselines
## metric
## result
## interpretation
## failure
## next
## links
```

## status values
`planned`, `running`, `done`, `inconclusive`, `failed`, `superseded`.

## id convention
Use short stable IDs: `e001`, `e002`, `e003`.


## shared rules
- Read `AGENTS.md` first. Use `PROMPTS.md` as the workflow registry if present.
- Default to propose-only unless the user explicitly asks to apply.
- Ask permission before creating, rewriting, moving, renaming, deleting, or reorganizing persistent notes.
- Preserve Obsidian links and valuable messy details.
- Keep filenames short. Use folders, not noisy filename prefixes.
- Use minimal frontmatter only when it helps retrieval.
- Do not invent citations, paper claims, commands, metrics, or results.
- Separate evidence from inference and speculation.
- Never create persistent AI-slop sections such as `Feynman Check` or `What I Still Do Not Understand`.
