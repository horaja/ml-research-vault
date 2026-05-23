---
name: claim-note
description: Build short durable claim notes only for central, reusable, controversial, or experiment-driving claims.
---

# Claim Note Builder

Do not create a claim note for every small statement.

A claim deserves its own note only if it is central, reusable, controversial, or experiment-driving.

## procedure
1. State the candidate claim precisely.
2. Decide whether it deserves a note.
3. If too minor, suggest embedding it in an existing note.
4. If justified, propose a short filename in the claims subfolder.
5. Do not use `Claim -` prefixes.
6. Separate claim, hypothesis, assumption, result, conjecture, and design choice.

## template
```md
---
type: claim
project: surf
status: speculative
---

# <short claim name>

## claim
## status
## evidence
## assumptions
## counterevidence
## baseline
## experiment
## links
```

## status values
`speculative`, `plausible`, `supported`, `weakened`, `falsified`, `retired`.


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
