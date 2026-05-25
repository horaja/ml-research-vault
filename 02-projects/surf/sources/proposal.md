---
type: source
project: surf
---

# proposal

## status
Historical and high-level framing.

## title
Biologically-Guided Token Selection for Efficient Vision-Language-Action Models.

## direction
Learning where to look through selective visual computation for VLA-style systems.

## mechanisms
- Line-drawing / structural prior for patch scoring.
- V4-derived feature preference / mid-level shape prior.
- Iterative coarse-to-fine token selection.
- Eventual evaluation on simulated robotic manipulation tasks.

## motivation
- VLA models often process full images uniformly.
- Human/biological vision selectively allocates resources to behaviorally relevant regions.
- Structure/shape may be more invariant and task-relevant than texture/background.

## preliminary reported result
The proposal reports line-drawing guided selective attention at `75.8%` ImageNet-10 accuracy while processing `40%` of patches, reducing computation from `1.408` GFLOPs to `0.448` GFLOPs.

## planned evaluation axes
- Task success.
- Compute per action / GFLOPs.
- Sample efficiency / demonstrations needed.
- Generalization.
- Human/model attention overlap.

## planned VLA direction
- Adapt line-drawing selection to action prediction.
- Implement iterative token selection.
- Integrate V4-derived guidance.
- Evaluate on realistic household manipulation tasks in the Stanford BEHAVIOR environment (https://behavior.stanford.edu).

## caution
Biological motivation is allowed, but do not overclaim biological faithfulness.

## links
- [[sources/repo]]
- [[roadmap]]
- [[synthesis/architecture]]
- [[claims/v4 relevance]]
- [[synthesis/where to look]]
