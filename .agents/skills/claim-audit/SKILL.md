---
name: claim-audit
description: Audit strong statements for evidence, overclaiming, speculation, contradictions, missing baselines, and fake rigor.
---

# Claim Audit

Prevent overclaiming and fake rigor.

## procedure
1. Read the target note or folder.
2. Identify strong statements.
3. Classify each as hypothesis, claim, assumption, result, conjecture, design choice, or speculation.
4. Identify grounding: paper, experiment, meeting, math, code/config, or none.
5. Flag unsupported claims, overstrong biological analogies, fake mathematical rigor, missing baselines, contradictions, claims to downgrade, and claims worth promoting.
6. Do not rewrite unless explicitly asked.

## output
```md
## Claim audit
| statement | type | grounding | issue | proposed fix |
|---|---|---|---|---|

## Contradictions
## Missing evidence
## Claims worth promoting
## Suggested edits
```

## strong statement rule
Every strong project-note statement should be supported by `Paper`, `Experiment`, `Meeting`, `Math`, `Code/config`, or `Speculation`.


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
