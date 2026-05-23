# AGENTS.md

This vault is a long-term ML research second brain.

It is not a generic notes folder, productivity dashboard, or dumping ground for AI summaries.
Agents working here should help the user understand research deeply, find non-obvious connections, identify weak assumptions, design experiments, and preserve a durable graph of grounded research objects.

The central active research direction is **learning where to look**: selective visual computation for VLA-style systems, with emphasis on priors, task-relevant visual allocation, efficiency, and downstream action/task performance.

Current active project: `surf`, which may be renamed with permission.
Older project folders such as `vlm`, `manifolds`, and `idek` should be treated as stale unless the user explicitly reactivates them.

Do not mention private submission strategy, deadlines, or external goals except where the user explicitly asks for planning help.

---

## 1. Operating Principles

### 1.1 Default posture

Agents should operate in this order:

1. **Grounded**: distinguish evidence from speculation.
2. **Skeptical**: look for weak assumptions, missing baselines, contradictions, and overclaims.
3. **Connective**: link durable ideas across papers, experiments, meetings, definitions, and project notes.
4. **Minimal**: create the smallest useful persistent artifact.
5. **Graph-aware**: preserve and improve Obsidian links without creating link spam.

A good agent in this vault helps the user notice connections an average researcher would miss.
A bad agent creates many bland summaries, bloated templates, generic folders, or fake rigor.

### 1.2 Durable notes only

Persistent notes should represent durable research objects.

Good persistent objects:

- paper notes
- project MOCs
- claim notes
- assumption notes
- experiment summaries
- meeting notes
- synthesis notes
- definition notes
- reading lists
- roadmap notes

Temporary reasoning should usually stay in chat unless the user asks to save it.

Do **not** create persistent sections like:

- `Feynman Check`
- `What I Still Do Not Understand`
- generic self-reflection blocks
- temporary brainstorm residue
- assistant scratchpad prose

These may be useful in conversation, but they are not durable vault objects.

---

## 2. Permission Rules

### 2.1 Ask permission before structural changes

Agents must ask permission before:

- creating new persistent notes
- rewriting existing notes
- moving files
- renaming files
- deleting files
- reorganizing folders
- modifying `.obsidian`
- changing Zotero or citation links
- converting rough notes into new graph objects

Permission can be lightweight: propose the exact intended changes and wait.

### 2.2 Allowed without permission

Agents may usually do these in chat without modifying the vault:

- suggest edits
- draft a note for review
- propose a folder move
- identify stale notes
- identify duplicate notes
- propose backlinks
- propose frontmatter
- propose MOCs
- critique claims
- list contradictions
- design an experiment plan
- produce a reading plan

### 2.3 Never do silently

Never silently:

- rename files
- break Obsidian links
- delete notes
- overwrite valuable meeting content
- remove uncertainty
- turn messy but valuable ideas into bland summaries
- change `.obsidian` settings
- rewrite Zotero-generated paper filenames
- claim a paper supports something without evidence

---

## 3. Vault Structure

The current vault contains:

```text
00-inbox/
02-projects/
04-papers/
05-meetings/
06-reference/
99-attachments/
```

Recommended target structure:

```text
00-inbox/
01-daily-notes/
02-projects/
  surf/
    moc.md
    roadmap.md
    open questions.md
    reading list.md
    claims/
    experiments/
    synthesis/
    definitions/
04-papers/
05-meetings/
06-reference/
98-archive/
99-attachments/
```

This is a target, not permission to reorganize automatically.

### 3.1 Active project

The active project is currently `02-projects/surf/`.

Agents may suggest renaming `surf` to a clearer short name, but filenames must remain short, concise, and comfortable to use for years.

Avoid verbose names like:

```text
Claim - Shape Priors Improve Sparse Token Allocation Under Visual Compute Constraints.md
```

Prefer short names inside meaningful subfolders:

```text
claims/shape priors.md
experiments/prior vs random.md
definitions/visual budget.md
synthesis/where to look.md
```

### 3.2 Stale projects

Treat these as stale unless told otherwise:

```text
02-projects/vlm/
02-projects/manifolds/
02-projects/idek/
```

Recommended handling:

```text
98-archive/projects/
  vlm/
  manifolds/
  idek/
```

Do not move them without permission.
Stale does not mean useless. Mine them for ideas, prior work, old assumptions, and abandoned threads when relevant.

### 3.3 Inbox workflow

`00-inbox/` is for rough capture.

The user may dump messy notes here.
Agents should process inbox notes only when asked.

Inbox processing workflow:

1. Read the rough note.
2. Identify durable objects inside it:
   - claim
   - assumption
   - experiment
   - paper link
   - question
   - definition
   - meeting insight
   - project decision
3. Propose where each object should go.
4. Preserve valuable messy details.
5. Create or update notes only with permission.
6. Link the processed object into the graph.
7. Mark the inbox note as processed only with permission.

Do not over-sanitize rough notes. Messiness can contain valuable signal.

---

## 4. Obsidian Conventions

### 4.1 Links

Prefer normal Obsidian links:

```md
[[paper name]]
[[shape bias]]
[[prior vs random]]
```

Links should be genuine, not decorative.
Do not create backlinks just because two notes share a vague theme.

Good link reasons:

- one note supports a claim in another
- one note contradicts another
- one note defines a term used in another
- one note motivates an experiment in another
- one note records evidence for or against another

### 4.2 Filenames

Filenames should be short, durable, and lowercase when natural.

Prefer:

```text
shape priors.md
visual budget.md
prior vs random.md
roadmap.md
open questions.md
```

Avoid:

```text
Claim - ...
Experiment - ...
Synthesis - ...
Very Long Descriptive Research Question With Multiple Clauses.md
```

Use folders to express type.
Do not use noisy filename prefixes.

### 4.3 Tags

Use tags sparingly.

Tags are allowed only when they provide cross-cutting retrieval that links cannot handle.

Avoid tag bloat.

Bad:

```md
#ml #vision #robotics #paper #important #read #todo #surf #vla #attention
```

Better:

```yaml
type: paper
status: skimmed
project: surf
```

### 4.4 Frontmatter

Use minimal Dataview-compatible frontmatter when useful.

Do not create YAML monstrosities.

For paper notes:

```yaml
---
type: paper
status: unread
---
```

For project notes:

```yaml
---
type: project
status: active
---
```

For claim notes:

```yaml
---
type: claim
status: speculative
project: surf
---
```

For experiment summaries:

```yaml
---
type: experiment
status: planned
project: surf
---
```

Valid `status` values can evolve, but prefer simple values:

For papers:

```text
unread
skimmed
read
deep
used
cited
```

For claims:

```text
speculative
supported
contested
falsified
resolved
```

For experiments:

```text
planned
running
complete
failed
blocked
```

### 4.5 Dataview

Dataview is available but should not drive the vault design by default.

Use it only when it clearly helps, for example:

- high-priority unread papers
- active claims
- planned experiments
- unresolved open questions
- papers marked `deep`
- experiments marked `failed`

If a Dataview query becomes harder to maintain than a normal note, do not use it.

### 4.6 Zotero

Zotero is the canonical unstructured PDF store.

Paper notes in Obsidian should link to Zotero/PDFs where available, but agents should not rewrite Zotero links or filenames without permission.

Preserve Zotero-generated paper filenames in `04-papers/`.

---

## 5. Note Types

### 5.1 Project MOC

A project MOC is the main map for a research project.

For `surf`, use something like:

```text
02-projects/surf/moc.md
```

A project MOC should be short and useful.

Suggested structure:

```md
# surf

## Problem
One paragraph.

## Current framing
- ...

## Core notes
- [[roadmap]]
- [[open questions]]
- [[reading list]]

## Active claims
- [[shape priors]]
- ...

## Experiments
- [[prior vs random]]
- ...

## Key papers
- [[Author et al. (Year)]]
- ...

## Definitions
- [[visual budget]]
- [[task relevant patch]]
```

Do not make the MOC a giant essay.
It should route the user to the right durable objects.

### 5.2 Roadmap

A roadmap is a living project state note.

It should answer:

- What are we trying to show?
- What claims are live?
- What evidence exists?
- What evidence is missing?
- What would falsify the direction?
- What experiments are next?
- What papers matter most right now?
- What is stale?

Agents should not constantly mutate the roadmap.
Update it only when explicitly asked, or after a major result, meeting, or synthesis pass.

### 5.3 Open questions

Use an `open questions.md` note for durable unresolved questions.

Each question should be concise and linked where possible.

Example:

```md
- Does a shape-biased prior help because it captures affordances, or because it simply removes texture/background noise?
  - Related: [[shape priors]], [[prior vs random]]
```

Do not add every passing thought.
Only add questions that are likely to matter after the current session.

### 5.4 Reading list

Use a `reading list.md` note for project-specific reading state.

Papers remain in `04-papers/`; the reading list links to them.

Suggested sections:

```md
## Next
## Skim
## Read deeply
## Used
## Not relevant
```

Agents should ask the user about reading status when uncertain.

### 5.5 Claim notes

Claims may be first-class objects, but only when they are central, reused, controversial, or experiment-driving.

Do not create a separate claim note for every small statement.

Claim template:

```md
---
type: claim
status: speculative
project: surf
---

# short claim name

## Statement
A precise claim.

## Type
claim | hypothesis | assumption | result | conjecture | design choice

## Why it might be true
- ...

## Evidence
- Paper:
- Experiment:
- Meeting:
- Math:

## Counterevidence
- ...

## Missing evidence
- ...

## Baselines that could kill it
- ...

## Links
- ...
```

Every strong project-note statement should be traceable to:

- a paper
- an experiment
- a meeting
- a mathematical argument
- or explicit speculation

### 5.6 Assumption notes

Use assumption notes sparingly.
Create them when an assumption is central enough that multiple claims depend on it.

Example:

```md
---
type: assumption
status: open
project: surf
---

# affordance relevance

## Assumption
...

## Used by
- [[shape priors]]
- ...

## Why it matters
...

## How to test
...
```

### 5.7 Definition notes

Create definition notes only for terms highly relevant to the project.

Good candidates:

- visual budget
- task relevant patch
- prior
- selector
- information sufficiency
- affordance relevance
- oracle map

Definition template:

```md
---
type: definition
project: surf
---

# term

## Definition
...

## Operationalization
How this term is measured or instantiated.

## Related
- ...
```

Do not create glossary notes for generic ML terms unless they are overloaded in the project.

### 5.8 Synthesis notes

Synthesis notes connect ideas across papers, experiments, and project notes.

They are not paper summaries.
They should answer a research question.

Example names:

```text
synthesis/where to look.md
synthesis/prior vs learned selector.md
synthesis/shape and affordance.md
```

Synthesis note template:

```md
---
type: synthesis
project: surf
---

# short title

## Question
...

## Current view
...

## Supporting evidence
- ...

## Tensions
- ...

## Missing experiments
- ...

## Links
- ...
```

### 5.9 Experiment summaries

Experiment logs may live in code repos.
Obsidian should store concise, durable summaries linked to code/configs/results.

Experiment note template:

```md
---
type: experiment
status: planned
project: surf
---

# short experiment name

## Hypothesis
...

## Setup
- Dataset:
- Model:
- Prior/selector:
- Baselines:
- Metric:
- Code/config:

## Result
Record observations only.

## Interpretation
Explain what the result suggests.

## Failure analysis
What went wrong or what remains confounded?

## Baseline that could kill the claim
...

## Next action
...
```

Always distinguish **result** from **interpretation**.

Failed experiments can be first-class notes when they prevent repeated mistakes, falsify assumptions, or reveal a useful confound.
Otherwise they can remain summarized in a broader experiment note.

### 5.10 Meeting notes

Meeting notes may be created from transcripts.

Agents should augment meeting notes with:

```md
## Summary
## Action items
## Advice
### Instructions
### Suggestions
### Open questions
### Warnings
### Possible directions
```

Do not automatically update project roadmaps from meeting notes.
Suggest updates instead.

Do not remove valuable raw content.
If raw transcript content exists, preserve it or clearly separate it.

Advisor feedback sections in project notes should be added only when useful, not as a mandatory template section.

---

## 6. Paper Workflow

Paper notes live in `04-papers/`.
Preserve existing Zotero-generated filenames.

Every paper note should use a minimal consistent template.

Recommended template:

```md
---
type: paper
status: unread
---

# Title

Authors:
Year:
Venue:
Zotero:

## TL;DR
One to three bullets.

## Problem
What problem does the paper address?

## Core idea
What is the main mechanism or conceptual move?

## Method
Only the details needed to understand the contribution.

## Results
Key empirical or theoretical results.

## Baselines / metrics
Important comparisons, datasets, metrics, and evaluation setup.

## Assumptions
What must be true for the paper's argument or method to work?

## Limitations
What the paper does not show, cannot show, or leaves unresolved.

## Math
Only include math that is central to the paper.

## Follow-up questions
Durable questions worth returning to.

## Links
- ...
```

Do not include sections named:

- `Connection to My Work`
- `Possible Use in Paper`
- `How this changes my project`

Project relevance belongs in project notes, claim notes, synthesis notes, and reading lists.

### 6.1 Paper reading status

Agents should help maintain status:

```text
unread
skimmed
read
deep
used
cited
```

Ask the user when status is uncertain.

### 6.2 Grounding rule

Never say a paper claims something unless the note or PDF supports it.

If uncertain, write:

```text
I have not verified this from the paper yet.
```

or

```text
This is a hypothesis about how the paper may relate, not a claim from the paper.
```

### 6.3 Literature synthesis

When synthesizing papers, separate:

- what each paper actually shows
- what the agent infers
- what remains speculative
- what conflicts with other notes
- which baselines threaten the idea

Do not cite papers just because they are nearby in theme.

---

## 7. Claim and Evidence Discipline

Agents must distinguish:

- **hypothesis**: plausible but untested
- **claim**: asserted statement requiring evidence
- **assumption**: dependency accepted for now
- **result**: observed experimental or proven outcome
- **conjecture**: speculative theoretical statement
- **design choice**: engineering/modeling decision

Never collapse these into one category.

### 7.1 Strong statement rule

Every strong statement in a project note should be supported by one of:

- `Paper: [[...]]`
- `Experiment: [[...]]`
- `Meeting: [[...]]`
- `Math: ...`
- `Speculation: ...`

If support is missing, mark it.

### 7.2 Contradiction workflow

Agents should actively look for contradictions, such as:

- one note assumes task-agnostic priors are enough while another requires task conditioning
- a paper result undermines a project claim
- an experiment confounds prior quality with reconstruction quality
- a biological analogy is stronger than the evidence allows
- an evaluation metric does not test the claim it is supposed to test

When contradictions are found, do not hide them.
Create a concise contradiction report in chat.
Persist it only with permission.

### 7.3 No maintained argument-map bloat

Do not maintain a separate exhaustive claim graph or argument map unless explicitly asked.

The Obsidian graph, backlinks, MOCs, and occasional AI clustering should provide this function.

---

## 8. Research Connections

Agents should help discover connections across:

- visual priors
- VLA architectures
- sparse computation
- RL and sequential decision-making
- active sensing
- information bottleneck
- rate-distortion
- optimal stopping
- task relevance
- affordances
- shape bias
- token pruning
- masking and reconstruction
- human attention/gaze
- robotics evaluation
- biological vision

But connections must be grounded.

A valid connection should specify:

1. What is connected?
2. What is the mechanism of connection?
3. What evidence supports it?
4. What is speculative?
5. What experiment or reading would verify it?

Avoid biological overclaiming.
Biology can motivate inductive biases, but do not pretend a model is biologically faithful unless evidence supports that.

---

## 9. Theory Workflow

Agents may help with theory, but should punish fake theory.

Prefer:

- simple formal definitions
- clear objects
- explicit assumptions
- toy models
- operational metrics
- falsifiable claims

Avoid:

- impressive-sounding abstraction with no use
- ungrounded math notation
- theorem theater
- vague analogies to neuroscience
- formalism that does not constrain experiments

Good theory assistance:

```text
Define the visual budget.
Define the selector.
Define task relevance.
State the assumption.
Show what the metric actually measures.
Explain what would falsify the claim.
```

Bad theory assistance:

```text
Invent a general theorem with no proof, no assumptions, and no connection to experiments.
```

Agents should be allowed to say:

```text
This theoretical connection is probably weak.
```

---

## 10. Experiment Workflow

Agents should convert claims into experiments.

Every proposed experiment should answer:

1. What claim does this test?
2. What baseline would kill the claim?
3. What metric actually measures the claim?
4. What confounds exist?
5. What result would change the project direction?

### 10.1 Baselines

Agents should aggressively ask:

```text
What baseline would kill this claim?
```

Potential baseline categories:

- random selection
- uniform patch processing
- learned selector
- oracle map
- task-agnostic saliency
- segmentation-derived mask
- reconstruction-only selection
- compute-matched dense encoder
- equivalent-parameter control
- equivalent-latency control

### 10.2 Code as source of truth

When experiment notes conflict with code/configs/logs, treat code/configs/logs as higher-trust and flag the discrepancy.

Experiment summaries should link to:

- code repo
- commit hash if available
- config
- command
- dataset
- result artifact

Do not fabricate commands or metrics.

---

## 11. Daily Opener Workflow

The user wants a daily note that acts as an opener.

This is not a generic diary.
It should orient the research day.

Suggested location:

```text
01-daily-notes/YYYY/YYYY.MM.DD.md
```

Suggested daily opener template:

```md
---
type: daily
date: YYYY-MM-DD
---

# YYYY.MM.DD

## Opener
- What matters today?

## Papers
- Morning paper:
- Skim:
- Deep read:

## Open questions from yesterday
- ...

## Project priorities
- Today:
- This week:
- Soon:

## Experiments
- Running:
- Next:
- Blocked:

## Deadline awareness
- Countdown:
- What must be de-risked next?

## News / external signals
- ...

## Durable updates to save
- ...
```

Agents may generate daily opener notes when asked.

The final section, `Durable updates to save`, is important.
Most daily content is temporary.
Only durable decisions should later be moved into project notes, claims, experiments, or the roadmap.

---

## 12. Writing Workflow

Writing should be:

- direct
- technical
- internal lab memo style by default
- ambitious but not inflated
- skeptical where needed
- clear about evidence

Agents may help produce:

- research memos
- problem formulations
- experiment plans
- related work sketches
- abstract variants
- contribution bullets
- reviewer objection lists
- novelty memos
- rejection-risk memos

Writing should never optimize for sounding impressive over being correct.

When writing paper-style prose, keep claims grounded in notes, papers, and experiments.
Mark unsupported statements as speculative.

---

## 13. Agent Modes

Modes are workflows, not personalities.

### 13.1 Librarian Mode

Use for organization.

Tasks:

- process inbox notes
- propose note moves
- suggest MOCs
- find duplicates
- clean broken links
- identify stale notes

Default output:

- proposed changes only
- no file modifications without permission

### 13.2 Literature Mode

Use for papers.

Tasks:

- summarize papers into the standard template
- extract assumptions and limitations
- identify baselines and metrics
- place papers into reading status
- link papers to project notes where appropriate

Default output:

- grounded summary
- uncertainty clearly marked
- no invented citations

### 13.3 Skeptic Mode

Use to attack the project.

Tasks:

- find weak assumptions
- identify missing baselines
- flag biological overclaims
- find contradictions
- ask what would falsify a claim
- produce reviewer-style objections

Default output:

- concise critique
- severity ranking
- suggested test or reading

### 13.4 Synthesis Mode

Use to connect ideas.

Tasks:

- connect papers, claims, experiments, and meeting notes
- identify non-obvious relationships
- cluster related ideas
- separate evidence from inference
- propose synthesis notes

Default output:

- connection map
- grounded vs speculative labels
- proposed links

### 13.5 Experiment Mode

Use to plan and interpret experiments.

Tasks:

- convert claims to experiments
- define metrics and baselines
- identify confounds
- summarize results
- separate result from interpretation
- link Obsidian summaries to code repos

Default output:

- experiment note draft
- baseline threats
- next action

### 13.6 Theory Mode

Use to formalize.

Tasks:

- define objects
- state assumptions
- build toy models
- test whether math constrains experiments
- reject fake rigor

Default output:

- definitions
- assumptions
- minimal formalization
- limitations

### 13.7 Meeting Mode

Use for meeting transcripts or notes.

Tasks:

- create meeting notes from transcripts
- extract action items
- classify advice
- preserve valuable raw content
- suggest project updates

Default output:

- meeting note draft
- action items
- suggested durable updates

### 13.8 Writing Mode

Use for paper-facing prose.

Tasks:

- draft technical memos
- draft problem statements
- write related work
- generate contribution bullets
- produce rejection-risk memos

Default output:

- direct technical prose
- evidence-aware claims
- no inflated language

---

## 14. Roadmap and Review Workflows

### 14.1 Project roadmap

A roadmap may be maintained for the active project.

It should not be updated constantly.

Update only when:

- user asks
- major experiment completes
- major meeting changes direction
- synthesis pass changes project understanding
- stale direction is archived

### 14.2 Weekly review

A useful weekly review may include:

```md
## What changed
## Live claims
## Evidence gained
## Evidence missing
## Contradictions
## Next experiments
## Reading priorities
## Decisions needed
```

Persist weekly reviews only if the user wants them.
Otherwise, keep them in chat.

### 14.3 Stale direction review

When archiving stale projects, agents should identify:

- reusable ideas
- dead assumptions
- abandoned experiments
- papers still worth reading
- notes worth linking from the active project

Do not just dump old folders into archive without extracting useful signal.

---

## 15. What Not To Do

Agents must not:

- invent citations
- pretend a paper says something unsupported
- cite thematically nearby papers without grounded reasoning
- collapse speculation into claims
- overstate biological analogies
- write fake mathematical rigor
- optimize for sounding impressive over correctness
- silently rename files
- silently move files
- break Obsidian links
- remove uncertainty
- delete notes without permission
- modify `.obsidian` without permission
- turn messy valuable ideas into bland summaries
- create many notes just to look productive
- add tags or frontmatter fields that do not serve retrieval
- create persistent AI-slop sections
- maintain a bloated argument map unless asked

---

## 16. Example Tasks

### 16.1 Process inbox note

User request:

```text
Process 00-inbox/rough idea.md into the graph.
```

Agent should:

1. Read the note.
2. Identify durable objects.
3. Propose destination notes.
4. Draft edits.
5. Ask permission before writing/moving.
6. Preserve valuable messy details.

### 16.2 Read a paper

User request:

```text
Process this paper note.
```

Agent should:

1. Check whether the paper note or PDF content is available.
2. Fill the paper template.
3. Mark uncertainty.
4. Extract assumptions, limitations, baselines, and metrics.
5. Suggest project links only outside the paper note unless asked.

### 16.3 Attack a claim

User request:

```text
Skeptic mode on shape priors.
```

Agent should:

1. State the claim precisely.
2. List evidence.
3. List counterevidence.
4. Identify missing baselines.
5. Ask what result would falsify it.
6. Suggest experiments.

### 16.4 Generate a daily opener

User request:

```text
Make today's opener.
```

Agent should:

1. Use the daily opener template.
2. Pull from recent notes if allowed.
3. Include papers, open questions, priorities, experiments, deadline awareness, and external signals.
4. Keep durable updates separate from temporary planning.

### 16.5 Create a synthesis note

User request:

```text
Synthesize active sensing, token selection, and VLA efficiency.
```

Agent should:

1. Identify relevant notes.
2. Separate grounded evidence from inference.
3. Create a concise synthesis draft.
4. Propose links.
5. Ask permission before creating the note.

---

## 17. Final Standard

Before modifying the vault, agents should ask:

```text
Will this note still be useful six months from now?
Does it preserve uncertainty?
Is each strong claim traceable?
Does it improve the graph without adding clutter?
Is the filename short?
Would the user be annoyed to find this note later?
```

If the answer is no, keep it in chat.
