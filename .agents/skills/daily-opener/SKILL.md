---
name: daily-opener
description: Create or update the daily research opener note for the active ML research vault. Use for today's opener, daily note, or day-start research orientation.
---

# Daily Opener

Create a compact daily note that orients the research day. It is a research launchpad, not a diary.

## inputs
- today's date
- recent daily notes if available
- active project MOC, roadmap, open questions, reading list, recent meetings, and experiment summaries when relevant

## procedure
1. Identify the active project from `AGENTS.md`.
2. Use the existing daily-notes convention if present.
3. If no daily path is clear, propose the path before creating it.
4. Create or update only today's daily note.
5. Run the research digest phase (see below).
6. Do not create other durable notes from the opener.
7. Keep temporary planning separate from durable updates.

## template
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
## news / external signals
## durable updates
```

## include
- today's research focus
- 2-4 papers worth looking at (manual picks, separate from digest)
- open questions carried forward
- near-term priorities
- experiment/result follow-ups
- weak assumptions or contradictions to check
- deadline awareness when relevant
- news/external signals only if grounded and sourceable

If web access is unavailable, mark news as skipped.

## output
```md
## Daily focus
## Proposed note path
## Proposed opener
## Needs permission?
```

---

## digest phase

The digest is an automated research paper discovery step. It fetches papers from Semantic Scholar, arXiv, and lab blog RSS feeds, then uses vault context to score and select a curated set for the daily note.

### steps

1. Install dependencies if needed:
   ```
   pip install -r .agents/skills/daily-opener/research-digest/requirements.txt
   ```

2. Fetch raw candidates:
   ```
   python .agents/skills/daily-opener/research-digest/fetch_papers.py .agents/skills/daily-opener/research-digest/config.yaml /tmp/raw_candidates.json
   ```

3. Deduplicate:
   ```
   python .agents/skills/daily-opener/research-digest/dedup.py /tmp/raw_candidates.json /tmp/candidates.json
   ```

4. Read `/tmp/candidates.json` to get the candidate pool.

5. Read vault context before scoring:
   - Last 3-5 daily notes from `01-daily-notes/`
   - `02-projects/surf/roadmap.md`
   - `02-projects/surf/questions.md`
   - `02-projects/surf/reading.md` — do not resurface papers already on this list
   - All files in `02-projects/surf/claims/`
   - Last 1-2 meeting notes from `05-meetings/Dr. Lee/`

6. Score and select 5-10 papers (hard ceiling: 10). Assign tiers:

   **Core (2-3):** Directly useful to the active project. Advances a specific open question, proposes a relevant method, introduces a benchmark worth evaluating on, or comes from a tracked author on a related topic.

   **Adjacent (2-3):** Trending or important in neighboring areas — vision transformer architectures, multimodal LLM reasoning, VLA / robot foundation models, efficient inference, image tokenization, embodied AI. Papers "everyone in the field is talking about."

   **Horizon (1-2):** Important ML ideas that are seemingly unrelated — optimization insights, scaling laws, representation learning breakthroughs, theoretical results. If a major conference just dropped proceedings, shift toward its best papers.

   The goal is a well-rounded morning briefing, not an echo chamber. Do NOT just surface papers matching the researcher's exact topic. Diversify.

7. Separate RSS blog posts from papers. Blog posts go in a different section.

8. Write the digest into the daily note (see format below).

9. Evaluate query health:
   - If a query produced zero results for 7+ consecutive days, retire it.
   - If multiple highly-scored papers share a theme not covered by existing queries, add a new query.
   - If a query is too broad, refine it.
   - Log any changes in the daily note.
   - Update `.agents/skills/daily-opener/research-digest/config.yaml` with changes and hit count shifts.

10. If fetching fails entirely (no web access), write `### digest (auto)\n*skipped — no web access*` and continue.

### output format

Papers go under `## papers` in a `### digest (auto)` sub-heading:

```md
### digest (auto)

**core**
- [Title](url) — First Author et al. · Venue
  Relevance note: 1-2 sentences on why this matters for this researcher specifically.

**adjacent**
- [Title](url) — First Author et al. · Venue
  Relevance note.

**horizon**
- [Title](url) — First Author et al. · Venue
  Relevance note.
```

Blog posts go under `## news / external signals` in a `### lab blogs (auto)` sub-heading:

```md
### lab blogs (auto)

- [Post title](url) — Lab Name
  One-line summary if relevant to the researcher's work. Skip if irrelevant.
```

If any query changes were made, append at the bottom of the digest section:

```md
**query health:** added "new query text" (reason). retired "old query" (0 hits, 7 days).
```

### style rules

- No bloat. No filler. No motivational framing.
- Dense with information, light on words.
- No decorative Obsidian links. Only link to vault notes when there is a genuine, specific connection (e.g., a paper provides evidence for `[[claims/structure helps]]`).
- No AI slop. No "this exciting paper," no "researchers have made a breakthrough." Say what the paper does and why it matters.
- Machine-generated sections are clearly marked with `(auto)` in the heading.

---

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
