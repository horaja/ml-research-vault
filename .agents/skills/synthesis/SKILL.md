---
name: synthesis
description: Build concise synthesis notes that connect papers, claims, experiments, and theory.
---

# Synthesis Builder

Synthesis notes answer research questions. They are not paper summaries.

## procedure
1. Identify the topic or research question.
2. Read relevant notes only.
3. Separate supported, plausible, speculative, contradicted, and unresolved points.
4. Make non-obvious connections only when grounded.
5. Specify the mechanism of connection.
6. Identify what experiment or reading would decide the issue.
7. Do not cite papers just because they are thematically nearby.
8. Do not overstate biological analogies.
9. Do not create a separate argument map.

## template
```md
---
type: synthesis
project: surf
---

# <short topic>

## thesis
## evidence
## tensions
## open questions
## experiments
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
