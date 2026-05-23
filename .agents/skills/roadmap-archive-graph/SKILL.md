---
name: roadmap-archive-graph
description: Update roadmaps sparingly, plan archival of stale material, and run graph passes for genuine missing links.
---

# Roadmap / Archive / Graph Workflow

Structural maintenance. Default to propose-only.

## roadmap update
Update the active project roadmap only if the trigger materially changes research state: user request, major result, major meeting, literature synthesis, or stale direction archived.

Roadmap should answer what we are trying to understand/prove, live claims, evidence, missing evidence, falsification criteria, next experiments, central papers, and stale directions.

## archive planner
Classify stale material as stale but valuable, obsolete/archive, duplicate, active dependency, or unsafe to move. Do not delete or move files without permission.

## graph pass
Find genuine missing links: claim to evidence, experiment to claim, paper to method/baseline, meeting advice to open question, definition to project note, synthesis to related claims.

Do not add links just because words match.

## output
```md
## Maintenance scope
## Roadmap changes
## Archive candidates
## Graph links
## Unsafe moves / broken-link risk
## Proposed edits
## Permission needed
```


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
