---
name: reading-list
description: Build or update project-specific reading lists grouped by research purpose.
---

# Reading List Workflow

Build reading lists that help decide what to read next. Papers remain in `04-papers/`; reading lists link to them.

## procedure
1. Identify scope: project, claim, theory direction, baseline threat, or paper set.
2. Group papers by purpose, not just topic.
3. Ask about reading status when uncertain.
4. Do not add random papers because they are thematically nearby.
5. If external search is used, cite or leave source URLs for review.
6. Suggest project links, but do not edit project notes without permission.

## groups
- must understand
- nearest neighbors
- baselines / threats
- theory tools
- experimental protocols
- background only
- probably stale / low priority

## per-paper fields
```md
- [[paper]]
  - why:
  - status:
  - answers:
  - should link from:
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
