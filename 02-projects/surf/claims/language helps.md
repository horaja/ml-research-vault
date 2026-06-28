---
type: claim
project: surf
status: speculative
---

# language helps

## claim
Instruction-conditioned patch scoring may select more task-relevant patches than a task-agnostic line prior.

## why it might be true
- Manipulation instructions can disambiguate which object or region matters.
- A contrastive selector can score patch-language compatibility directly.
- @caiFlashVLMTextGuidedVisual2025 reports beyond-lossless compression on LLaVA 1.5 under language-conditioned token selection — language conditioning may not just reduce compute but select *better* tokens than the unpruned baseline. Robustness across instruction types (esp. short spatial-reference manipulation instructions) not yet verified.
- @liCogVLACognitionAlignedVisionLanguageAction2026 instantiates instruction-driven routing + sparsification directly in VLA (EFA-Routing + LFP-Routing + V-L-A Coupled Attention); SOTA on LIBERO with 2.5× training and 2.8× latency reduction vs. OpenVLA. 56 cites. This is the strongest empirical instantiation of the claim — without any geometric prior. Threat: if pure language routing already achieves SOTA, the additional contribution from structural priors needs to be isolated. Demands explicit "language routing without structural prior" baseline in [[experiments/contrastive alignment]].

## needed evidence
- Zero-language ablation.
- Learned visual scorer without language.
- DAA gaze supervision may not teach action relevance if gaze and action-relevant regions diverge.

## baseline that could kill it
- Same architecture with language replaced by zeros.
- Line prior only.
- Learned visual scorer without language.

## links
- [[experiments/language conditioning]]
- [[synthesis/prior vs learned]]
- [[eval/gaze]]
