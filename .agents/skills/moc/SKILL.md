---
name: moc
description: Build or maintain project maps of content.
---

# MOC Maintainer

MOCs are indexes with judgment, not giant directories.

## procedure
1. Identify the target project or scope.
2. Read only the notes needed to orient the map.
3. Surface central problem, claims, papers, experiments, definitions, synthesis notes, open questions, and relevant archive links.
4. Include only useful links.
5. Avoid link spam.
6. Keep section names short.
7. Do not turn the MOC into a giant essay.

## template
```md
---
type: moc
project: surf
---

# surf

## problem
## claims
## papers
## experiments
## concepts
## questions
## synthesis
## archive
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
