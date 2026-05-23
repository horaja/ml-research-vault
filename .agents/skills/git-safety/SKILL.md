---
name: git-safety
description: Inspect changed vault files after applied edits before committing.
---

# Git Safety Check

Use after applied changes. Do not commit unless explicitly asked.

## procedure
1. Inspect changed files.
2. Summarize git status.
3. Identify risky changes.
4. Identify possible broken links.
5. Suggest a short commit message.
6. Ask before committing.

## commit message style
```text
process inbox notes
update surf moc
add paper note
summarize experiment e001
archive stale projects
```

## output
```md
## Git status
## Changed files
## Risky changes
## Possible broken links
## Suggested commit message
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
