---
name: literature-search
description: Intake external literature search results when web access is available.
---

# External Literature Search Intake

Use only when external search is available and the user asks for it.

Prioritize primary sources, official proceedings, arXiv, author pages, and reputable conference/workshop pages.

## procedure
For each candidate, return title, authors, year, venue/source, URL, why it may matter, what claim/question it might inform, and confidence level.

Do not add papers to the vault automatically. Do not claim relevance beyond what the abstract/source supports.

## output
```md
## Search topic
## Candidates
### <paper/resource>
- authors:
- year:
- venue/source:
- url:
- why it may matter:
- informs:
- confidence:
## Suggested next reads
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
