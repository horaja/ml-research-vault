---
name: daily-opener
description: Create or update the daily research opener note for the active ML research vault. Use for today's opener, daily note, or day-start research orientation.
---

# Daily Opener

Create a compact daily note that orients the research day. It is a research launchpad, not a diary.

## inputs
- today\'s date
- recent daily notes if available
- active project MOC, roadmap, open questions, reading list, recent meetings, and experiment summaries when relevant

## procedure
1. Identify the active project from `AGENTS.md`.
2. Use the existing daily-notes convention if present.
3. If no daily path is clear, propose the path before creating it.
4. Create or update only today\'s daily note.
5. Do not create other durable notes from the opener.
6. Keep temporary planning separate from durable updates.

## template
```md
---
type: daily
project: surf
date: YYYY-MM-DD
---

# YYYY-MM-DD

## opener
## papers
## questions
## priorities
## experiments
## risks
## links
```

## include
- today\'s research focus
- 2-4 papers worth looking at
- open questions carried forward
- near-term priorities
- experiment/result follow-ups
- weak assumptions or contradictions to check
- deadline awareness when relevant
- news/external signals only if grounded and sourceable

If web access is unavailable, mark news as skipped.

## output
```md
## Daily focus
## Proposed note path
## Proposed opener
## Needs permission?
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
