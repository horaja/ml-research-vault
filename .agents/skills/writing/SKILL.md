---
name: writing
description: Draft research-facing prose such as internal memos, problem formulations, related work sketches, abstracts, and reviewer objections.
---

# Writing Workflow

Writing should be direct, technical, and internal-lab-memo style by default.

Be ambitious but not inflated.

## use for
Research memos, problem formulations, experiment plans, related work sketches, abstract variants, contribution bullets, reviewer objection lists, novelty memos, and rejection-risk memos.

## rules
- Ground claims in notes, papers, and experiments.
- Mark unsupported claims.
- Do not invent citations.
- Do not overstate novelty.
- Do not overstate biological analogies.
- Do not optimize for sounding impressive over correctness.
- Draft in chat unless the user explicitly asks to create a note.

## output
```md
## Draft
## Claims needing evidence
## Citations / notes needed
## Likely objections
## Suggested next action
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
