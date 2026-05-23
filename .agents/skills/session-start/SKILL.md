---
name: session-start
description: Read-only research dashboard. Surfaces the current state of the active project (MOC, roadmap, open questions, recent daily, open experiments, unread papers) at the start of a work session. Does not create or modify notes.
---

# Session Start

Use at the beginning of a work session to orient on the current research state. This is a read-only orientation pass, not a note-creation workflow. It does not replace `daily-opener` — run `daily-opener` afterward if you want to draft today's note.

## inputs
- active project from `AGENTS.md`
- active project `moc.md`, `roadmap.md`, `questions.md`, `reading.md`
- most recent file under `01-daily-notes/`
- recent experiment summaries under the active project's `experiments/`
- recent meeting notes under `05-meetings/`
- paper notes with `status: unread` or `status: reading` under `04-papers/`

## procedure
1. Identify the active project from `AGENTS.md`.
2. Read the project MOC, roadmap, and open questions. Note the project's stated current state and next experiments.
3. Find the most recent daily note (lexicographic max under `01-daily-notes/`). Read its priorities, experiments, and risks sections.
4. List experiment notes with `status: planned` or `status: running`.
5. List paper notes with `status: unread` or `status: reading`. Cap at 10.
6. List the 3 most recently modified meeting notes.
7. Surface anything in `00-inbox/` that has not been triaged.
8. Do not read the full vault. Do not summarize archived projects.
9. Do not create, rename, or modify notes. This skill is read-only.

## return
- one-sentence framing of what the active project is currently trying to do
- next experiments from the roadmap
- open experiments (planned or running) with their question
- top 3 open questions worth attacking next
- unread / in-progress papers, with one-line hooks
- recent meeting topics (titles only)
- inbox backlog count
- anything stale: experiments running for more than a week, papers reading for more than two weeks, roadmap items unchanged for more than a month
- nothing else — no advice, no synthesis, no proposed edits

## output
```md
## Active project
## Current direction
## Next experiments
## Open experiments
## Top open questions
## Papers in flight
## Recent meetings
## Inbox backlog
## Stale items
```

If the user wants synthesis, proposals, or planning, suggest the appropriate skill (`weekly-review`, `synthesis`, `roadmap-archive-graph`) rather than producing it inline.


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
