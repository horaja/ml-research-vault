---
name: meeting
description: Prepare for meetings or convert meeting transcripts/rough notes into durable meeting notes.
---

# Meeting Workflow

Use for meeting prep, transcript processing, and post-meeting durable notes.

Do not automatically update project roadmaps or project notes. Suggest follow-up edits separately.

## meeting prep
Include current state, strongest current claim, weakest assumption, recent results, papers/evidence to mention, questions to ask, what not to overclaim, and decision points.

## transcript processor
1. Create or update a meeting note.
2. Preserve valuable nuance.
3. Do not delete important raw content unless explicitly asked.
4. Extract compact summary, action items, advice, decisions, unresolved questions, and links.
5. Categorize advice as instruction, suggestion, open question, warning, or possible direction.
6. Propose project/roadmap updates separately.

## template
```md
---
type: meeting
date: YYYY-MM-DD
---

# <short meeting title>

## summary
## actions
## advice
### instructions
### suggestions
### open questions
### warnings
### possible directions
## decisions
## questions
## links
## raw
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
