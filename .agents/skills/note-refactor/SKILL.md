---
name: note-refactor
description: Refactor long, messy, or non-graph-friendly notes into shorter durable Obsidian objects.
---

# Note Refactor

Refactor notes like code. The goal is durable structure, not bland summarization.

## procedure
1. Read the target note.
2. Identify core durable objects.
3. Identify sections that should stay.
4. Identify sections that should move.
5. Identify split candidates only if justified.
6. Identify possible backlinks.
7. Identify claims needing grounding.
8. Label speculation.
9. Preserve valuable messy details.
10. Propose a patch before applying.

## output
```md
## Refactor plan
## Keep
## Move
## Split candidates
## Links to add
## Claims to audit
## Proposed patch
## Permission needed
```

Create new notes only when the object is central, reusable, controversial, or experiment-driving.


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
