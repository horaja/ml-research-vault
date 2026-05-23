---
name: paper
description: Intake, normalize, or deeply read paper notes while preserving project-agnostic paper notes.
---

# Paper Workflow

Paper notes live in `04-papers/` and remain project-agnostic. Project relevance belongs in project notes, claim notes, synthesis notes, and reading lists.

Never add sections named `Connection to My Work`, `Possible Use in Paper`, or `How this changes my project`.

## intake
Extract only what is supported by the note, PDF, or abstract:
- bibliographic metadata
- status
- problem
- core idea
- method
- key results
- assumptions
- limitations/failures
- baselines and metrics
- central math only if central
- durable follow-up questions
- links

If information is missing, mark it unknown.

## deep read
Return:
- exact problem statement
- method mechanism
- assumptions the method needs
- evidence supporting claims
- strongest baselines
- weakest baseline gap
- failure modes
- hidden dependencies
- central math variable-by-variable, only if central
- what would make the paper\'s claim fail
- project notes that should link to it

## template
```md
---
type: paper
status: unread
---

# <title>

## metadata
- authors:
- year:
- venue:
- zotero:

## summary
## problem
## method
## results
## assumptions
## limitations
## baselines
## math
## questions
## links
```

## status values
`unread`, `skimmed`, `read`, `deep`, `actionable`, `used`, `cited`.
Use `deep` only when genuinely understood, not merely summarized.


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
