---
name: weekly-review
description: Run a weekly research review over recent daily notes, meetings, experiments, active MOC, roadmap, open questions, and recent paper notes.
---

# Weekly Review

Use once per week or when the user asks for a research state review. Do not scan the whole vault unless needed.

## inputs
Recent daily notes, recent meeting notes, recent experiment summaries, active project MOC, roadmap, open questions, and recently edited paper notes.

## return
- what changed this week
- strongest current claim
- weakest current assumption
- most important missing baseline
- contradictions found
- papers to read next
- experiments to prioritize
- stale notes or ideas
- notes that should be refactored
- proposed edits only

## output
```md
## Weekly state
## Strongest claim
## Weakest assumption
## Missing baseline
## Contradictions
## Reading
## Experiments
## Refactors
## Proposed edits
```

Persist weekly reviews only if the user asks.


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
