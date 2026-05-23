---
name: inbox
description: Triage, process, and optionally apply approved transformations for rough notes in `00-inbox/`.
---

# Inbox Workflow

Convert rough notes into minimal, durable Obsidian graph objects. This is research-signal extraction, not cleanup for its own sake.

## triage procedure
1. Read the target inbox note or folder.
2. Identify durable objects: claim, assumption, result, experiment idea, paper connection, definition, open question, meeting insight, project decision, stale idea, or trash/no durable value.
3. Preserve messy but valuable details.
4. Prefer updating existing notes over creating new notes.
5. Create a new note only if the object is central, reusable, controversial, or experiment-driving.
6. Keep proposed filenames short.
7. Suggest links into the graph.
8. Ask permission before moving, rewriting, creating, archiving, marking processed, or deleting.

## apply procedure
Use only after the user approves a triage plan. Apply only the approved changes. Do not add extra restructuring.

## output
```md
## Inbox triage
### <inbox note>
- durable objects:
- proposed destination:
- proposed action:
- links:
- keep / move / archive / delete:
- permission needed:

## Batch proposal
## Questions
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
