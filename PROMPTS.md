# PROMPTS.md

Reusable workflow prompts for the ML research vault.

This file is a prompt library, not a replacement for `AGENTS.md`.
Agents must read and follow `AGENTS.md` first, then use the workflow prompt here that matches the task.

The vault is a long-term Obsidian research second brain.
The goal is durable research understanding, not AI-generated note volume.

---

## How to Use This File

### Recommended invocation pattern

Use this pattern in any agent CLI:

```text
Read AGENTS.md and PROMPTS.md.
Run the workflow: <workflow name>.
Inputs: <files/folders/transcript/result/etc.>
Mode: propose-only unless I explicitly say apply.
```

Default to **propose-only**.
A workflow should mutate files only when the user clearly asks it to apply changes.

### Agent compatibility

This file is intentionally vendor-neutral.
It should work with Codex CLI, Claude Code, Gemini CLI, or any local file-editing agent.

Recommended setup:

```text
AGENTS.md       = durable vault rules and operating principles
PROMPTS.md      = reusable workflow recipes
CLAUDE.md       = optional pointer to AGENTS.md + PROMPTS.md
GEMINI.md       = optional pointer to AGENTS.md + PROMPTS.md
```

Optional lightweight `CLAUDE.md` or `GEMINI.md` content:

```md
# Agent Context

Read `AGENTS.md` first.
Use `PROMPTS.md` for named workflows.
Default to propose-only before editing vault files.
```

For Claude Code, these workflows can later be split into custom slash commands under `.claude/commands/`.
For Gemini CLI, keep `GEMINI.md` short and point it here.
For Codex CLI, keep `AGENTS.md` as the main instruction file and invoke workflows from this file by name.

---

## Global Workflow Contract

Every workflow must follow this sequence unless the user explicitly overrides it.

### 1. Scout

Read the relevant files.
Identify the smallest set of notes needed for the task.
Do not scan the entire vault unless the workflow calls for it.

### 2. Classify

Classify information as one of:

- paper evidence
- experiment result
- meeting advice
- mathematical argument
- implementation fact
- hypothesis
- claim
- assumption
- conjecture
- design choice
- speculation
- open question
- stale idea

Never collapse these categories.

### 3. Propose

Before editing, propose:

- files to create
- files to modify
- files to move
- links to add
- frontmatter to add/update
- possible deletions or archive moves
- uncertainties

Keep the proposal compact.

### 4. Permission gate

Ask before persistent mutation unless the user already said to apply.

Permission is required for:

- creating notes
- rewriting notes
- moving files
- renaming files
- deleting files
- changing folder structure
- changing `.obsidian`
- changing Zotero links
- converting rough notes into durable graph objects

### 5. Apply

When applying edits:

- preserve Obsidian links
- preserve useful messiness
- keep filenames short
- avoid generic summaries
- distinguish result from interpretation
- use minimal frontmatter
- avoid tag bloat
- do not over-link

### 6. Verify

After editing, report:

- changed files
- new links added
- unresolved questions
- possible broken links
- suggested git commit message

If git is available, run `git diff --stat` or suggest that the user inspect it.
Do not commit unless the user explicitly asks.

---

## Universal Output Format

For propose-only workflows, use:

```md
## Summary

## Files read

## Proposed changes

## Questions / permission needed

## Risks

## Suggested next action
```

For applied workflows, use:

```md
## Done

## Files changed

## Important edits

## Links added

## Unresolved issues

## Suggested git commit
```

---

# Workflows

---

## 0. Router

Use when the user gives a vague task and the agent needs to choose a workflow.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Router workflow.

Task:
<USER TASK>

Choose the best workflow or combination of workflows.
Do not edit files yet.

Return:
- interpreted task
- workflow(s) to use
- files/folders likely needed
- whether permission is required
- suggested exact next prompt
```

### Output contract

```md
## Interpreted task

## Best workflow

## Needed context

## Permission needed

## Suggested prompt
```

---

## 1. Daily Opener

Use at the beginning of the day.
The daily note is a research launchpad, not a diary.

### Inputs

- today's date
- recent daily notes, if available
- `02-projects/surf/moc.md`, if available
- `02-projects/surf/roadmap.md`, if available
- `02-projects/surf/open questions.md`, if available
- recent meeting notes
- recent experiment summaries
- reading list

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Daily Opener workflow.

Date: <YYYY-MM-DD>
Mode: <propose-only | apply>

Create or update today's daily note as a compact research opener.
Use the existing daily-notes structure if present.
If no daily folder exists, propose the path before creating it.

Include:
- today's research focus
- 2-4 papers worth looking at
- open questions carried forward
- near-term priorities
- experiment/result follow-ups
- weak assumptions or contradictions to check
- ICLR countdown, if relevant
- relevant news only if grounded and worth checking

Rules:
- Keep it compact.
- Do not create other durable notes.
- Do not invent news, citations, or paper claims.
- If web access is unavailable, mark news as skipped.
- If web access is used, cite sources in the note or leave source URLs for review.
```

### Suggested daily note template

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

### Output contract

```md
## Daily focus

## Proposed note path

## Proposed opener

## Needs permission?
```

---

## 2. Inbox Triage

Use to process rough notes in `00-inbox/`.
This is one of the most important workflows.

### Inputs

- one inbox note, or the whole `00-inbox/` folder
- active project MOC/roadmap
- existing claims/experiments/definitions if relevant

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Inbox Triage workflow.

Input:
<INBOX FILE OR FOLDER>

Mode: propose-only.

For each inbox note:
1. Identify durable research objects inside it:
   - claim
   - assumption
   - result
   - experiment idea
   - paper connection
   - definition
   - question
   - meeting insight
   - stale idea
   - trash/no durable value
2. Preserve messy but valuable details.
3. Propose where each object should go.
4. Prefer updating existing notes over creating new notes.
5. Create a new note only if the object is central, reusable, controversial, or experiment-driving.
6. Keep proposed filenames short.
7. Suggest links into the graph.
8. Ask permission before moving, rewriting, creating, archiving, or deleting.

Do not apply changes yet.
```

### Output contract

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

---

## 3. Inbox Apply

Use after the user approves an inbox triage plan.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Inbox Apply workflow.

Approved plan:
<PASTE APPROVED PLAN>

Apply only the approved changes.
Do not add extra restructuring.
Preserve valuable original wording when it carries research signal.
After applying, report changed files and suggested git commit.
```

---

## 4. Paper Intake

Use when adding a paper note, usually linked from Zotero.
The paper note should stay project-agnostic.
Project relevance belongs in project notes, not in the paper note.

### Inputs

- paper note
- PDF text if available
- abstract if available
- Zotero link if available

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Paper Intake workflow.

Paper:
<PAPER NOTE OR PDF/TEXT>

Mode: <propose-only | apply>

Create or normalize a minimal paper note.
Use a consistent template.
Do not include sections named "Connection to My Work" or "Possible Use in Paper".
Do not claim the paper says something unless the note/PDF supports it.
If information is missing, mark it as unknown.

Extract:
- status
- bibliographic metadata if available
- problem
- core idea
- method
- assumptions
- limitations / failures
- baselines and metrics
- key results
- central math only if central to the paper
- follow-up questions
- links

After processing, suggest which project notes might link to this paper.
Do not edit project notes without permission.
```

### Paper note template

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

### Status values

Use one of:

```text
unread
skimmed
read
deep
actionable
used
cited
```

Use `deep` only when the paper is genuinely understood, not merely summarized.

---

## 5. Paper Deep Read

Use when a paper matters enough to understand deeply.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Paper Deep Read workflow.

Paper:
<PAPER NOTE/PDF>

Mode: propose-only unless explicitly told to apply.

Do a skeptical deep read.
Focus on what the paper actually proves or demonstrates.
Do not write generic summary prose.

Return:
- exact problem statement
- method mechanism
- assumptions the method needs
- what evidence supports the claims
- strongest baselines
- weakest baseline gap
- failure modes
- hidden dependencies
- central math, variable-by-variable, only if central
- what would make the paper's claim fail
- project notes that should link to it

Do not add "Connection to My Work" to the paper note.
If there are project implications, propose edits to project notes separately.
```

---

## 6. Reading List Builder

Use to create or update the active reading list.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Reading List Builder workflow.

Scope:
<surf / a specific claim / a specific theory direction / a set of papers>

Mode: propose-only.

Build or update a reading list that helps the user decide what to read next.
Group papers by purpose, not by topic only.

Possible groups:
- must understand
- nearest neighbors
- baselines / threats
- theory tools
- experimental protocols
- background only
- probably stale / low priority

For each paper, include:
- why read it
- current status
- what question it answers
- what project note should link to it

Do not add random papers because they are thematically nearby.
If web search is used, cite sources or leave URLs.
```

---

## 7. Claim Audit

Use to prevent overclaiming and fake rigor.

### Inputs

- project note
- claim note
- synthesis note
- paper note set
- experiment summaries

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Claim Audit workflow.

Input:
<NOTE OR FOLDER>

Mode: propose-only.

Audit strong statements.
For each strong statement, classify it as:
- hypothesis
- claim
- assumption
- result
- conjecture
- design choice
- speculation

For each, identify grounding:
- paper
- experiment
- meeting
- math
- code/config
- none

Flag:
- unsupported claims
- biological analogies that are too strong
- fake mathematical rigor
- missing baselines
- contradictions with other notes
- claims that should be downgraded to speculation
- claims that deserve their own note

Do not rewrite yet.
```

### Output contract

```md
## Claim audit

| statement | type | grounding | issue | proposed fix |
|---|---|---|---|---|

## Contradictions

## Missing evidence

## Claims worth promoting

## Suggested edits
```

---

## 8. Claim Note Builder

Use only for central, reusable, controversial, or experiment-driving claims.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Claim Note Builder workflow.

Claim:
<CLAIM>

Mode: propose-only unless explicitly told to apply.

Create a short durable claim note only if justified.
If the claim is too minor, suggest embedding it in an existing note instead.

The note should distinguish:
- claim
- status
- evidence
- assumptions
- counterevidence
- missing baseline
- experiment needed
- links

Keep filename short.
Do not use a "Claim -" prefix.
Use the claims subfolder if present.
```

### Claim note template

```md
---
type: claim
project: surf
status: speculative
---

# <short claim name>

## claim

## status

## evidence

## assumptions

## counterevidence

## baseline

## experiment

## links
```

Status values:

```text
speculative
plausible
supported
weakened
falsified
retired
```

---

## 9. Experiment Plan

Use before running experiments.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Experiment Plan workflow.

Research question / claim:
<QUESTION OR CLAIM>

Code repo context:
<PATHS OR DESCRIPTION>

Mode: propose-only.

Design a minimal experiment that tests the claim.
Include:
- hypothesis
- what result would support it
- what result would weaken or kill it
- dataset
- model
- baselines
- metric
- ablations
- controls
- expected failure modes
- command/config plan if code context is available
- artifact paths to save
- Obsidian summary note path

Be skeptical.
Prioritize clean baselines over impressive experiments.
```

### Output contract

```md
## Hypothesis

## Minimal test

## Baselines

## Metrics

## Kill criterion

## Setup

## Commands/configs

## Failure modes

## Expected Obsidian summary
```

---

## 10. Experiment Summary

Use after a run.
Raw logs stay in the code repo.
Obsidian stores compact interpretation.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Experiment Summary workflow.

Inputs:
- result/log/config: <PATH OR PASTE>
- related claim: <CLAIM OR NOTE>
- code repo commit, if available: <COMMIT>

Mode: <propose-only | apply>

Create or update a compact Obsidian experiment summary.
Do not copy raw logs into Obsidian.
Distinguish result from interpretation.
Include:
- hypothesis
- setup
- dataset
- model
- baselines
- metric
- command/config link
- result
- interpretation
- failure analysis
- next action
- what baseline would kill the claim

If the run is inconclusive, say so.
Do not make it sound successful just because work was done.
```

### Experiment note template

```md
---
type: experiment
project: surf
status: planned
---

# e001

## hypothesis

## setup

## baselines

## metric

## result

## interpretation

## failure

## next

## links
```

Status values:

```text
planned
running
done
inconclusive
failed
superseded
```

Experiment IDs should be short and stable:

```text
e001
e002
e003
```

Use the note title or first line to carry meaning if needed.

---

## 11. Meeting Prep

Use before meetings.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Meeting Prep workflow.

Meeting:
<PERSON/GROUP + DATE>

Scope:
<surf / experiment / paper / general research>

Mode: propose-only.

Prepare a compact meeting brief.
Include:
- current state
- strongest current claim
- weakest assumption
- recent results
- papers or evidence to mention
- questions to ask
- what not to overclaim
- decision points

Do not update vault files unless asked.
```

---

## 12. Meeting Transcript Processor

Use when the user provides a transcript or rough meeting notes.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Meeting Transcript Processor workflow.

Transcript/source:
<TRANSCRIPT OR FILE>

Meeting metadata:
- date:
- attendees:
- context:

Mode: <propose-only | apply>

Create or update a meeting note.
Preserve valuable nuance.
Do not delete important raw content unless explicitly asked.

Extract:
- compact summary
- action items
- advice categorized as instruction / suggestion / open question / warning / possible direction
- decisions
- unresolved questions
- links to relevant project/paper/experiment notes

Do not update roadmap or project notes unless explicitly asked.
If follow-up project edits are warranted, propose them separately.
```

### Meeting note template

```md
---
type: meeting
date: YYYY-MM-DD
---

# <short meeting title>

## summary

## actions

## advice

## decisions

## questions

## links

## raw
```

---

## 13. MOC Builder / Maintainer

Use to maintain project maps of content.
MOCs are indexes with judgment, not giant directories.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the MOC Maintainer workflow.

MOC:
<MOC NOTE OR PROJECT>

Mode: propose-only unless explicitly told to apply.

Update or propose a project MOC that helps the user navigate the research graph.
Include only useful links.
Do not turn it into a table of contents for the whole vault.

A good MOC should surface:
- central problem
- active claims
- key papers
- experiments
- definitions
- synthesis notes
- open questions
- stale/archived directions if relevant

Avoid link spam.
Prefer short section names.
```

### MOC template

```md
---
type: moc
project: surf
---

# surf

## problem

## claims

## papers

## experiments

## concepts

## questions

## synthesis

## archive
```

---

## 14. Note Refactor

Use when a note is too long, messy, or not graph-friendly.
This is analogous to refactoring code.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Note Refactor workflow.

Note:
<NOTE PATH>

Mode: propose-only.

Refactor this note for durable Obsidian use.
Do not flatten valuable messiness into generic summary.

Identify:
- core durable objects
- sections that should stay
- sections that should move
- possible backlinks
- possible new notes, only if justified
- claims needing grounding
- speculation needing labels
- stale material

Keep filenames short.
Do not apply edits yet.
```

### Output contract

```md
## Refactor plan

## Keep

## Move

## Split candidates

## Links to add

## Claims to audit

## Proposed patch
```

---

## 15. Definition Note Builder

Use only for definitions central to the active project.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Definition Note Builder workflow.

Term:
<TERM>

Mode: propose-only unless explicitly told to apply.

Create a definition note only if the term is central to surf.
The note should be short and useful.
Do not create glossary bloat.

Include:
- working definition
- why it matters
- formal version, if needed
- related claims
- related papers
- failure/confusion cases

If the term is not central, suggest adding a one-line definition to an existing note instead.
```

---

## 16. Synthesis Builder

Use to connect papers, claims, experiments, and theory.
This is where non-obvious connections should be made, but grounded.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Synthesis Builder workflow.

Topic:
<TOPIC>

Inputs:
<NOTES/PAPERS/EXPERIMENTS>

Mode: propose-only unless explicitly told to apply.

Build a concise synthesis note.
Prioritize non-obvious but grounded connections.
Separate:
- what is supported
- what is plausible
- what is speculative
- what contradicts what
- what experiment would decide it

Do not cite a paper just because it is thematically nearby.
Do not overstate biological analogies.
Do not create a claim graph or argument map.
Let Obsidian links and MOCs carry the graph.
```

### Synthesis template

```md
---
type: synthesis
project: surf
---

# <short topic>

## thesis

## evidence

## tensions

## open questions

## experiments

## links
```

---

## 17. Weekly Review

Use once per week.
This is the compounding workflow.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Weekly Review workflow.

Week ending: <YYYY-MM-DD>

Mode: propose-only.

Read recent daily notes, meeting notes, experiment summaries, active project MOC, roadmap, open questions, and recently edited paper notes.
Do not scan the whole vault unless needed.

Return:
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
```

### Output contract

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

---

## 18. Novelty / Rejection Risk

Use for serious skeptical review.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Novelty / Rejection Risk workflow.

Scope:
<surf / claim / experiment plan / paper outline>

Mode: propose-only.

Act as a skeptical reviewer.
Do not optimize for sounding impressive.
Do not create fake rigor.

Separate novelty into:
- problem novelty
- method novelty
- empirical novelty
- theory novelty
- setting/application novelty

Identify:
- nearest-neighbor papers
- strongest related work
- likely reviewer objections
- missing baselines
- unsupported claims
- weak biological analogies
- experiments needed
- claims that should be downgraded

Return concrete fixes.
Do not edit files unless asked.
```

---

## 19. Roadmap Update

Use sparingly.
Roadmaps should not be constantly rewritten.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Roadmap Update workflow.

Trigger:
<major result / meeting / literature synthesis / user request>

Mode: propose-only unless explicitly told to apply.

Update the active project roadmap only if the trigger materially changes the research state.
Do not turn the roadmap into a task dump.

Roadmap should answer:
- what are we trying to understand or prove?
- what are the live claims?
- what evidence exists?
- what is missing?
- what would falsify the direction?
- what experiments are next?
- what papers are central now?
- what is stale?
```

---

## 20. Archive Planner

Use when stale folders or notes need cleanup.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Archive Planner workflow.

Scope:
<FOLDER OR NOTES>

Mode: propose-only.

Identify stale material and propose archive moves.
Do not delete anything.
Do not move files yet.

For each item, classify:
- stale but valuable
- obsolete and probably archive
- duplicate
- active dependency
- unsafe to move because links may break

Propose short archive paths.
List links that may need updating.
```

---

## 21. Graph Pass

Use occasionally to improve Obsidian graph connectivity.
This should not create link spam.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Graph Pass workflow.

Scope:
<PROJECT/FOLDER/NOTE SET>

Mode: propose-only.

Look for genuine missing links between notes.
Prioritize links that improve research reasoning:
- claim to evidence
- experiment to claim
- paper to method/baseline
- meeting advice to open question
- definition to project note
- synthesis to related claims

Do not add links just because words match.
Do not over-link common terms.
Return proposed link edits only.
```

---

## 22. Writing Memo

Use when turning research state into prose.
This is not a persistent paper draft unless explicitly requested.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Writing Memo workflow.

Target:
<abstract / related work / problem formulation / advisor memo / paper outline>

Inputs:
<NOTES>

Mode: draft-in-chat unless explicitly told to create a note.

Use a direct technical or internal lab memo style.
Be ambitious but not inflated.
Ground claims in notes.
Mark unsupported claims.
Do not invent citations.
Do not overstate novelty.

Return:
- draft
- claims needing evidence
- citations/notes needed
- likely objections
```

---

## 23. External Literature Search Intake

Use only when the agent has web access and the user asks for external search.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the External Literature Search Intake workflow.

Search topic:
<TOPIC>

Mode: propose-only.

Find papers or resources relevant to the active research direction.
Prioritize primary sources, official proceedings, arXiv, authors' pages, and reputable conference/workshop pages.

For each candidate:
- title
- authors
- year
- venue/source
- URL
- why it may matter
- what claim/question it might inform
- confidence level

Do not add papers to the vault automatically.
Do not claim relevance beyond what the abstract/source supports.
```

---

## 24. Code-to-Vault Experiment Sync

Use when code repo experiments need compact Obsidian summaries.

### Prompt

```text
Read AGENTS.md and PROMPTS.md.
Run the Code-to-Vault Experiment Sync workflow.

Code repo path:
<PATH>

Experiment/results path:
<PATH>

Mode: propose-only unless explicitly told to apply.

Inspect the code/config/results needed to summarize the experiment.
Treat code/config/results as source of truth for what was run.
Treat Obsidian as source of truth for interpretation.

Return:
- runs found
- config/command
- metric/results
- matching claim or project note
- proposed experiment summary note
- discrepancies between code and notes
```

---

## 25. Git Safety Check

Use after any applied changes.

### Prompt

```text
Run the Git Safety Check workflow.

Inspect changed files.
Do not commit unless explicitly asked.

Return:
- git status summary
- changed files
- risky changes
- possible broken links
- suggested commit message
```

Suggested commit message style:

```text
process inbox notes
update surf moc
add paper notes
summarize experiment e001
archive stale projects
```

---

## 26. Code-Notes Disparity

Use cluster-side. Audit an experiment repo against the vault's experiments, claims, and roadmap. Strictly descriptive — write the report into the drop folder; do not edit durable notes.

### Inputs

- `$VAULT_DIR` on the cluster (default `$HOME/vault`)
- experiment repo path (default: current working directory)
- optional scope: `experiments` | `claims` | `roadmap` | `all` (default)

### Prompt

```text
Read AGENTS.md, CLUSTER.md, and PROMPTS.md.
Run the Code-Notes Disparity workflow.

Repo:
<REPO PATH or .>

Scope: <experiments | claims | roadmap | all>

Mode: apply (write to drop folder only).

Read the active project notes (MOC, roadmap, experiments/, claims/) and
scan the repo (git log, configs, runs/outputs/wandb if present, HEAD
commit). For each vault experiment, check whether cited commits exist,
whether hyperparameters and metrics match the latest config/log, and
whether ungrounded references remain. For each repo run/config artifact,
surface missing vault summaries. For each supported/weakened/falsified
claim, check that the grounding experiment's code is present. For
roadmap "next experiments" entries, classify as stale (done in code) or
phantom (no matching code).

Phrase findings narrowly per AGENTS.md §1.2 — local-repo absence does
not constrain project-wide claims. Do not invoke git against the vault
directly.

Write one report to:
$VAULT_DIR/00-inbox/cluster/<hostname>/<YYYY-MM-DD>/code-notes-diff.md

Do not write anywhere else in the vault.
```

### Output contract

```md
# code-notes diff — <repo>@<commit-short>

## scope
## experiments
### missing vault summaries
### ghost code refs
### hyperparameter / metric drift
## claims
### claims with no supporting code
### implementations with no claim/experiment link
## roadmap
### stale entries
### phantom entries
## proposed triage actions (laptop-side)
## confidence notes
```

Laptop-side promotion uses §24 (missing summaries), §19 (confirmed stale roadmap entries), §20 (ghost refs to archive), and §2/§3 (general drop triage).

---

## 27. Run Summary

Use cluster-side after a run. Summarize one run's config + metrics + short logs into a structured draft in the drop folder. Promotion to a durable `experiments/eYYY.md` happens laptop-side via §24.

### Inputs

- `$VAULT_DIR` on the cluster
- run directory (default: most recent under `runs/` / `outputs/` / `wandb/`)
- optional related claim or experiment note for hypothesis context

### Prompt

```text
Read AGENTS.md, CLUSTER.md, and PROMPTS.md.
Run the Run Summary workflow.

Run directory:
<RUN PATH or auto-detect latest>

Related vault note (optional):
<CLAIM OR EXPERIMENT PATH>

Mode: apply (write to drop folder only).

Read the run's config, metric summary, and short log files. Do not copy
raw logs. Distinguish result (from logs) from interpretation (cautious
one-liner). If hypothesis is not provided, infer cautiously from config
naming and mark it inferred. Leave unknown fields blank or "unknown" —
do not fabricate.

Write to:
$VAULT_DIR/00-inbox/cluster/<hostname>/<YYYY-MM-DD>/run-<run-id>.md

Use frontmatter `status: drop` (non-standard sentinel — explicitly not a
durable status). The laptop triage converts `drop` to a real status
during §24 promotion.

Do not write anywhere else in the vault.
```

### Output contract

```md
---
type: experiment-draft
project: surf
status: drop
source-run: <repo>@<commit>:<run path>
---

# run-<id>

## hypothesis
## setup
## baselines
## metric
## result
## interpretation
## failure
## next
## links
```

---

# Common Invocation Examples

## Daily opener

```text
Read AGENTS.md and PROMPTS.md. Run Daily Opener for today. Mode: apply if the daily note already exists, otherwise propose the path first.
```

## Inbox processing

```text
Read AGENTS.md and PROMPTS.md. Run Inbox Triage on 00-inbox/. Propose-only. Keep filenames short and avoid new notes unless justified.
```

## Paper processing

```text
Read AGENTS.md and PROMPTS.md. Run Paper Intake on 04-papers/<paper>. Mode: apply. Do not add project relevance to the paper note; suggest project links separately.
```

## Claim audit

```text
Read AGENTS.md and PROMPTS.md. Run Claim Audit on 02-projects/surf/. Propose-only. Focus on unsupported claims, missing baselines, and speculation disguised as results.
```

## Experiment summary

```text
Read AGENTS.md and PROMPTS.md. Run Experiment Summary using <result path> and related claim <claim note>. Propose-only. Distinguish result from interpretation.
```

## Meeting transcript

```text
Read AGENTS.md and PROMPTS.md. Run Meeting Transcript Processor on this transcript. Mode: apply to a new meeting note only after proposing the path.
```

## Weekly review

```text
Read AGENTS.md and PROMPTS.md. Run Weekly Review for week ending <date>. Propose-only. Do not edit files.
```

## Novelty audit

```text
Read AGENTS.md and PROMPTS.md. Run Novelty / Rejection Risk on 02-projects/surf/moc.md and roadmap.md. Propose-only.
```

---

# Tool-Specific Notes

## Codex CLI

Use Codex for applying file edits after the plan is clear.
Good default:

```text
Read AGENTS.md and PROMPTS.md. Run <workflow>. Mode: propose-only.
```

Then, after approving:

```text
Apply the approved plan exactly. Then run Git Safety Check. Do not commit.
```

## Claude Code

Use Claude Code for skeptical review, literature synthesis, and note refactoring.
If desired, convert major workflows into custom slash commands later.
Good defaults:

```text
Run the Novelty / Rejection Risk workflow from PROMPTS.md on <scope>. Do not edit files.
```

or:

```text
Run the Note Refactor workflow from PROMPTS.md on <note>. Propose-only.
```

## Gemini CLI

Use Gemini for alternative perspectives, broad connection search, or cross-checking.
Keep `GEMINI.md` short and point it to `AGENTS.md` and `PROMPTS.md`.
Good default:

```text
Read GEMINI.md, AGENTS.md, and PROMPTS.md. Run Synthesis Builder on <topic>. Propose-only.
```

---

# Anti-Bloat Rules

Before creating any persistent note, ask:

1. Will this note be useful months from now?
2. Is this better as a section in an existing note?
3. Is this central, reusable, controversial, or experiment-driving?
4. Does it improve the graph, or just create more files?
5. Is the filename short enough to actually use?

If the answer is unclear, propose instead of creating.

---

# Grounding Rules

Never write a strong project statement unless it is grounded in one of:

- paper
- experiment
- meeting
- code/config
- math
- explicitly marked speculation

Never invent citations.
Never pretend a paper says something unsupported.
Never cite a paper only because it is thematically nearby.
Never hide uncertainty.
Never inflate biological analogies.
Never write fake theory.

---

# Preferred Minimal Frontmatter

Use only when useful.
Do not add frontmatter to every old note unless the user asks.

## Paper

```yaml
type: paper
status: unread
```

## Claim

```yaml
type: claim
project: surf
status: speculative
```

## Experiment

```yaml
type: experiment
project: surf
status: planned
```

## Meeting

```yaml
type: meeting
date: YYYY-MM-DD
```

## Daily

```yaml
type: daily
project: surf
date: YYYY-MM-DD
```

## MOC

```yaml
type: moc
project: surf
```

---

# Final Rule

The agent is not here to make the vault look impressive.
The agent is here to make the research harder to fool, easier to connect, and easier to build into real results.
