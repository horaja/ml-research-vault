---
name: novelty-risk
description: Run skeptical novelty and rejection-risk review on a project, claim, experiment plan, or paper outline.
---

# Novelty / Rejection Risk

Act as a skeptical reviewer. Do not optimize for sounding impressive. Do not create fake rigor.

## procedure
1. Define the scope.
2. Separate novelty into problem, method, empirical, theory, and setting/application novelty.
3. Identify nearest-neighbor papers, strongest related work, likely reviewer objections, missing baselines, unsupported claims, weak biological analogies, experiments needed, and claims that should be downgraded.
4. Return concrete fixes.
5. Do not edit files unless asked.

## output
```md
## Scope
## Novelty
### problem
### method
### empirical
### theory
### setting
## Nearest neighbors
## Reviewer objections
## Missing baselines
## Unsupported claims
## Concrete fixes
## Proposed edits
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
