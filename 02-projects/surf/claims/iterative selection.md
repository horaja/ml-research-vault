---
type: claim
project: surf
status: speculative
---

# iterative selection

## claim
Coarse-to-fine selection may outperform one-shot top-k selection by using uncertainty or intermediate evidence to request additional patches.

## why it might be true
- A first pass can use a cheap prior.
- Later passes can refine with image evidence or posterior uncertainty.
- This matches the project goal of allocating visual compute only where needed.

## needed evidence
- Comparison against fixed one-shot top-k at equal compute.
- Stopping/refinement rule that improves task success, compute efficiency, sample efficiency, or generalization.

## baseline that could kill it
- One-shot top-k performs equally well at the same GFLOPs.
- Adaptive refinement spends extra compute without improving action success or classification accuracy.

## evidence
- @xuVisionPulseDynamicVisual2026 (unread, 2026.06.02 digest): reportedly shows that the critical visual-token set evolves across reasoning steps, and that redundant visual context steers the model toward query-irrelevant regions. If step-dependency transfers to VLA closed-loop inference, this directly supports iterative selection over one-shot top-k. Not yet verified from the paper.

## links
- [[concepts/variational prior]]
- [[experiments/iterative selection]]
- [[concepts/selector]]
- [[synthesis/adaptive compute]]
