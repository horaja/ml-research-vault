---
name: definition
description: Create or update short definition notes only for terms central to the active project.
---

# Definition Note Builder

Do not create glossary bloat.

## procedure
1. Decide whether the term is central enough for a note.
2. If not, suggest a one-line definition inside an existing note.
3. If yes, propose a short filename in the definitions subfolder.
4. Define the term operationally, not just philosophically.
5. Link related claims, papers, experiments, or synthesis notes.
6. Include confusion/failure cases when useful.

## template
```md
---
type: definition
project: surf
---

# <term>

## definition
## operationalization
## why it matters
## confusions
## links
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
