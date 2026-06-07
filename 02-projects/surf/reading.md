---
type: reading-list
project: surf
---

# reading

## prior — selection mechanism, what to attend to

**Skim**
- @jiangTRIPSEfficientVisionandLanguage2025 — nearest mechanism for text-guided patch selection; current blocker for [[experiments/contrastive alignment]].
- @sonSelectivePerceptionRobot2026 — view-level routing for task-relevance; scope check vs patch-level routing rejection.
- @yangLookZoomUnderstand2025 — language-guided active perception ("where to look and at what scale" under budget). Very similar to Tianqin's previous idea; read and send.
- Active vision — survey or canonical reference TBD.

**Deep**
- @huangNuwaMendingSpatial2026 — does global-semantic / attention-score pruning erode the positional-interaction spatial frame? Direct relevance to [[synthesis/architecture]].

## VLA / action — closed-loop policy, history integration

**Skim**
- @xiaoAVAVLAImprovingVisionLanguageAction2025 — POMDP framing, history-aware attention. Re-skim for composability with [[claims/iterative selection]].

## efficiency / adaptive compute — budget, iterative selection, when-to-stop

**Skim**
- @xuVisionPulseDynamicVisual2026 — high priority. Step-dependent visual sparsity in multimodal reasoning. If transfers to VLA closed-loop inference, escalates [[claims/iterative selection]] from speculative to load-bearing.
- AC²-VLA (Yu et al., arXiv Jan 2026; citekey TBD) — spatial / depth redundancy formulation. Completes four-formulation picture with ElegantVLA / VLA-ATTC / BRPO. See [[synthesis/adaptive compute]].

## eval — data, metrics, baselines

**Skim**
- @chuangLookFocusAct2025 — continuous human gaze + foveated ViT. Data-availability check for [[eval/gaze]]: candidate DAA complement/replacement.
- Eye-movement control — canonical reference TBD.
- Tianqin's ChatGPT-as-attention-baseline paper — citekey TBD.

## theory — formal frameworks

**Skim**
- @rajputMatchingPrincipleGeometric2026 — candidate framing for line/shape prior as nuisance suppression; treat skeptically.
- @korchinskiLearnYourOwn2026 — sample-complexity theory as analytical framework for surf's compute allocation. Skim for relevance.
- Hierarchical control / RL background
    - @frankMechanismsHierarchicalReinforcement2012
    - @badreMechanismsHierarchicalReinforcement2012

## used
- @chanLearningGenerateLine2022 — line-drawing generation paper backing [[concepts/line prior]]. *Note: `.bib` has both `@chanLearningGenerateLine2022` (article) and `@chanLearningGenerateLine2022a` (inproceedings) for the same work — dedupe in Zotero.*

## unkeyed — need citekey or drop
Wikilink-format entries that violate AGENTS.md §4.1. Resolve by importing to Zotero or dropping:
- [[Mees et al. (2023)]] — language-conditioned spatial grounding for manipulation. Track: **prior**.
- [[Bolya et al. (2023)]] — token efficiency baseline family (ToMe). Track: **efficiency**.
- [[Li et al. (2025)]] — adaptive pixel/visual operation selection in VLMs. Track: **prior** or **efficiency**.
