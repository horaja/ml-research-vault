# code-notes diff — behavior_env@5748990

## scope
- repo: `/lab_data/leelab/VLA-Husain-Tianqin/behavior_env` (worktree `lucid-neumann-d581ef`)
- vault project: `02-projects/surf/`
- ran at: 2026-05-24T UTC

## experiments
### missing vault summaries (code exists, no note)
- `docs/contrastive_alignment.md` — see [[contrastive_alignment]] detailed design doc for contrastive alignment Module 1 (TRIPS-inspired cross-modal patch scoring, DAA gaze pre-training, BEHAVIOR-1K fine-tuning). No vault experiment note or synthesis note references this document. It contains architecture decisions, training recipes, and evaluation plans that are not captured in any vault note.
- `slurm_scripts/` pipeline (01–04, `run_behavior.sh`) — a multi-step BEHAVIOR-1K environment setup pipeline (SIF pull, dataset download, eval framework install, eval tests, behavior run). No vault note documents this infrastructure or its current status.

### ghost code refs (note exists, code absent)
- [[experiments/e001]] — note cites commit `0543ccf` from `line-biased-vision-encoder` repo; commit does not exist in this repo. This is expected: `e001` belongs to a different repo (`line-biased-vision-encoder` on laptop), not `behavior_env`. No ghost ref in the strict sense, but the two repos are not cross-linked.
- [[sources/repo]] — documents path `/Users/husain/Documents/cmu/research/line-biased-vision-encoder`, a laptop-local path. No code from that repo is present in `behavior_env`.

### hyperparameter / metric drift
- No configs or metric summaries found in this repo. The repo contains no `configs/`, `runs/`, `outputs/`, or `wandb/` directories. All metric claims in vault notes (Top-1 0.734/0.758, Top-5 0.964/0.968, GFLOPs 1.408/0.448) originate from `line-biased-vision-encoder`, not this repo.

## claims
### claims with no supporting code in this repo
- [[claims/structure helps]] — status=supported, grounded in [[experiments/e001]] and [[sources/repo]]. Neither the SelectiveMagnoViT implementation nor any line-prior code is present in `behavior_env`. The supporting code lives in the laptop `line-biased-vision-encoder` repo.
- [[claims/efficiency without collapse]] — status=supported, same grounding. Same situation.

### implementations with no claim/experiment link
- `docs/contrastive_alignment.md` — a substantial design document covering cross-modal patch scoring (Architecture B), contrastive pre-training with DAA gaze data, TRIPS-inspired summary tokens, and a 7-day implementation plan. This appears to be the planned next step for [[experiments/language conditioning]] and [[claims/language helps]], but no vault note links to it or records its existence.
- BEHAVIOR-1K eval framework (`slurm_scripts/03–04`, `eval_tests_inner.sh`, `eval_verify_inner.sh`) — implements reconstruction-based evaluation with MAE, patch selectors, and an evaluation pipeline. Maps to [[eval/reconstruction]] and [[eval/behavior]] conceptually, but those vault notes do not reference this codebase.
- `run_behavior.sh` — runs OmniGibson robot control example. Maps to [[experiments/vla adaptation]] and [[eval/behavior]], but neither vault note references this script or repo.

## roadmap
### stale entries
- (none confirmed stale from this repo's evidence alone)

### phantom entries
- "Strengthen [[experiments/e001]] with kill baselines from [[eval/baselines]]" — no baseline comparison code found in this repo. May exist in `line-biased-vision-encoder`.
- "Run [[experiments/language conditioning]]" — `docs/contrastive_alignment.md` is a detailed design doc for this, but no implementation code exists yet. Status: designed but not implemented.
- "Use [[eval/reconstruction]] and [[eval/behavior]]" — eval framework code exists in this repo (`slurm_scripts/03–04`) but eval tests are failing due to torch version incompatibility (CVE-2025-32434 requires torch ≥ 2.6; the container has an older version). The eval pipeline is blocked.
- "Use [[experiments/iterative selection]]" — no matching code in this repo.

## active blockers observed
1. **BEHAVIOR-1K env segfault**: `behavior_run_343227.log` shows OmniGibson crashing with `AssertionError: Category sink not found in average object specs!` followed by segfault. The vault note [[eval/behavior]] mentions a segfault blocker — this appears to be the same or a related issue, still unresolved as of this run (dated 2026-03-03).
2. **Eval framework torch version**: `eval_tests_385130.log` shows 4/5 tests failing because `transformers` refuses `torch.load` on torch < 2.6 (CVE-2025-32434). The MAE reconstructor cannot load pretrained weights.
3. **OmniGibson dependency resolution**: `eval_verify_385135.log` and `eval_verify_385137.log` show `pip` failing to resolve `bddl~=3.7.0` and `pymeshlab~=2022.2` — these packages are not available in the expected versions. The workaround (local bddl3 install) partially succeeds in 385137 but the pymeshlab blocker remains.

## proposed triage actions (laptop-side)
- promote: `docs/contrastive_alignment.md` → propose linking from [[experiments/language conditioning]] or a new vault note via PROMPTS.md §24. This is a substantial design artifact that should be visible in the vault graph.
- investigate: the two-repo split (laptop `line-biased-vision-encoder` vs. cluster `behavior_env`) means most claim-grounding code is not visible from the cluster. Consider whether [[sources/repo]] should note both repos, or whether a second source note is needed.
- update: [[eval/behavior]] should record the specific `Category sink not found` assertion error and torch version blocker, replacing the vague "segfaulting" note with concrete failure details.
- update: roadmap "next experiments" items referencing eval framework are currently blocked by dependency issues; this should be reflected in experiment status or the roadmap.

## confidence notes
- This scan can see: the `behavior_env` repo's git history, file structure, slurm scripts, log files, and docs. It can see the full vault project notes.
- This scan cannot see: the `line-biased-vision-encoder` repo (laptop-local, path `/Users/husain/Documents/cmu/research/line-biased-vision-encoder`), any wandb runs, any remote experiment results, the BEHAVIOR-1K source code (gitignored/submodule at `BEHAVIOR-1K/`), or the contents of `behavior_data/`.
- Per AGENTS.md §1.2: absence of code in this repo does not mean the code does not exist elsewhere. Findings are scoped narrowly to what is observable in `behavior_env`.
