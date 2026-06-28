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
- @heModelKnowsWhich2026 — NTP-only token selection via noise gating, no auxiliary supervision. Critical read: does NTP gradient alone capture the structural/action-relevant signal that surf's contrastive prior is designed to inject?
- @palaciosVisualInstructionTuning2026 — probing + causal interventions show visual features embed into *intermediate* LLM layers; restricting fine-tuning to those layers preserves vision-centric performance. Anchor evidence for [[experiments/contrastive alignment]] layer selection.
- @liDepthCacheDepthGuidedTrainingFree2026 — depth-guided training-free VLA token merging; spatially differentiated merge ratios (near-field workspace preserved, far-field compressed). Competing structural-prior baseline for [[claims/structure helps]] — depth vs. line drawings as the structural signal.
- @jiangBetterYouLearn2025 — LightVLA: first differentiable token pruning for VLA (Gumbel-Softmax, no auxiliary parameters). Important baseline for [[experiments/contrastive alignment]]. Read to nail down what "differentiable" means here — Gumbel-ST gradient path, and whether it's the same design space as SparseLearn / DiffPrune.
- Active vision — survey or canonical reference TBD.

**Deep**
- @huangNuwaMendingSpatial2026 — does global-semantic / attention-score pruning erode the positional-interaction spatial frame? Direct relevance to [[synthesis/architecture]].
- @zhuActiveO3EmpoweringMultimodal2025 — GRPO-trained active perception (zoom/crop) for MLLMs. Direct candidate answer to [[questions]] selector-training-approach: RL policy with verifiable spatial rewards. Compare against contrastive objective before finalizing [[experiments/contrastive alignment]].
- @liCogVLACognitionAlignedVisionLanguageAction2026 — instruction-driven routing + sparsification in VLA (EFA-Routing, LFP-Routing, V-L-A Coupled Attention); SOTA on LIBERO; 56 cites. Closest existing instantiation of [[claims/language helps]] without geometric prior. Deep read before writing [[experiments/contrastive alignment]] spec — extract what's missing that surf's structural prior is positioned to supply.

## biological grounding — mid-level vision, V4 shape/texture organization

**Deep**
- @jiangComputationalConstraintsUnderlying — V4 columns cluster into shape vs. texture functional domains; a Kohonen SOM under feature-similarity + retinotopy constraints is necessary and sufficient to reproduce the map; ImageNet ANNs are texture-biased while V4 is balanced shape/texture. Grounding for [[claims/v4 relevance]] and [[claims/structure helps]]. Q: is the dispersity measure computable on arbitrary scene images via the digital twin, and does it yield a per-patch shape score usable as a selection prior?

**Skim**
- @wangLargescaleCalciumImaging2024 — wide-field calcium-imaging V4 map for natural scenes; the dataset behind the digital twin in @jiangComputationalConstraintsUnderlying. Q: what is measured per column, and what coverage/resolution would limit a prior derived from it?
- @wangManifoldTransformRecurrent2025 — recurrent cortical circuit / manifold transform for robust encoding of familiar stimuli. Decides whether [[claims/iterative selection]] × familiarity is real: does the mechanism change *where/how much* compute is spent, or only *how robustly* a stimulus is encoded?

## efficiency / adaptive compute — budget, iterative selection, when-to-stop

**Skim**
- @xuVisionPulseDynamicVisual2026 — high priority. Step-dependent visual sparsity in multimodal reasoning. If transfers to VLA closed-loop inference, escalates [[claims/iterative selection]] from speculative to load-bearing.
- AC²-VLA (Yu et al., arXiv Jan 2026; citekey TBD) — spatial / depth redundancy formulation. Completes four-formulation picture with ElegantVLA / VLA-ATTC / BRPO. See [[synthesis/adaptive compute]].
- @xiaoAVAVLAImprovingVisionLanguageAction2025 — POMDP framing, history-aware attention. Re-skim for composability with [[claims/iterative selection]].

## eval — data, metrics, baselines

**Skim**
- @chuangLookFocusAct2025 — continuous human gaze + foveated ViT. Data-availability check for [[eval/gaze]]: candidate DAA complement/replacement.
- Eye-movement control — canonical reference TBD.
- Tianqin's ChatGPT-as-attention-baseline paper — citekey TBD.
- biorxiv 2026.05.29.726887 — https://www.biorxiv.org/content/10.64898/2026.05.29.726887v1.full.pdf — neuroscience reference for 2026-06-13 meeting with Dr. Lee; citekey TBD after Zotero import.

## theory — formal frameworks

**Skim**
- @rajputMatchingPrincipleGeometric2026 — candidate framing for line/shape prior as nuisance suppression; treat skeptically.
- @korchinskiLearnYourOwn2026 — sample-complexity theory as analytical framework for surf's compute allocation. Skim for relevance.
- @yangTightSampleComplexity2026 — tight VC dimension Θ(LW log(TW)) for transformers; candidate framing for token-pruning-as-regularization via log(T) reduction. Use in theoretical analysis section.
- Hierarchical control / RL background
    - @frankMechanismsHierarchicalReinforcement2012
    - @badreMechanismsHierarchicalReinforcement2012

## used
- @chanLearningGenerateLine2022 — line-drawing generation paper backing [[concepts/line prior]]. *Note: `.bib` has both `@chanLearningGenerateLine2022` (article) and `@chanLearningGenerateLine2022a` (inproceedings) for the same work — dedupe in Zotero.*