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

## links
- [[concepts/variational prior]]
- [[experiments/iterative selection]]
- [[concepts/selector]]
