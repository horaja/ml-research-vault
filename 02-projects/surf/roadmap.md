---
type: project
project: surf
status: active
---

# roadmap

## current framing
Selective visual computation should be evaluated as a way to preserve task-relevant information under a visual budget, not as a biological-faithfulness claim.

The current implemented system is a line-guided ViT for ImageNet-style classification. The project direction is to test whether similar priors help VLA-style action prediction.

## verified evidence
- [[experiments/e001]]: line-guided selective patch processing improves ImageNet-10 Top-1 in the checked-in repo while using lower reported GFLOPs.

## live claims
- [[claims/structure helps]]
- [[claims/efficiency without collapse]]
- [[claims/language helps]]
- [[claims/iterative selection]]
- [[claims/v4 relevance]]

## missing evidence
- VLA/action prediction evidence.
- A center-bias and Canny edge-density comparison for the current line prior.
- Evidence that line drawings select action-relevant regions, not just class-discriminative contours.
- Evidence that V4-derived preferences add useful information beyond generic shape/edge priors.

## falsifiers
- Center bias matches or beats line-guided selection at the same visual budget.
- Language-conditioned selectors do not beat a zero-language ablation.
- Selective processing improves classification but harms action prediction under matched compute.
- Gaze alignment improves while task success does not, showing biological-plausibility metrics are not measuring action relevance.

## next experiments
- Validate current ImageNet-10 result and baselines in [[experiments/e001]].
- Run the language-conditioning ablation in [[experiments/language conditioning]].
- Implement task-relevance metrics in [[eval/reconstruction]] before claiming VLA relevance.
- Treat [[experiments/vla adaptation]] as planned until repo support exists.

## central papers
- [[Chan et al. (2022)]]
- [[Jiang et al. (2025)]]
- [[Mees et al. (2023)]]
- [[He et al. (2021)]]
- [[Bolya et al. (2023)]]
- [[Rao et al. (2021)]]

## stale directions
- Routing networks for functional module selection are likely the wrong abstraction for spatial patch selection.
