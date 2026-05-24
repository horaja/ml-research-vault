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
1. Open the existing meeting note (the user pre-fills the minimal template below with raw pre/post-meeting thoughts; the agent runs on those + the transcript). If no note exists yet, create one at `05-meetings/<counterpart>/YYYY-MM-DD.md`.
2. Preserve `## context` and `## links` as-written. Preserve `## notes` content; when extracting structured advice, move the raw bullets verbatim to `## raw` rather than deleting them.
3. Append structured sections: `## summary` (3-6 sentences), `## advice` with the five sub-categories, `## decisions`. Merge user-written `## actions` and `## questions` with anything extracted from the transcript; do not overwrite.
4. Categorize advice as instruction, suggestion, open question, warning, or possible direction.
5. Flip `status: raw` → `status: processed` in the frontmatter when done.
6. Propose project/roadmap updates separately — never apply them silently.

## template (user-filled, minimal)
The minimal capture template the user pre-fills lives at `06-reference/templates/meeting.md`. Do not duplicate it here — read that file when you need to scaffold a new note.

## processed shape (agent-produced)
After the transcript processor runs, the note grows the structured sections below (on top of the user's original content):

```md
## summary
## advice
### instructions
### suggestions
### open questions
### warnings
### possible directions
## decisions
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
