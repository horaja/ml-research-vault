---
type: experiment
project: surf
status: planned
---

# vla adaptation

## hypothesis
A selector that helps classification may also help action prediction if its selected patches preserve task-relevant object and affordance information.

## setup
- Dataset/task suite: BEHAVIOR-style household manipulation is planned, not implemented.
- Model: VLA-style policy with selective visual encoder.
- Prior/selector: line prior first, then language-conditioned or iterative variants.
- Metrics: task success, compute per action, sample efficiency, generalization.

## result
Not run. Current repo is classification-only.

## risks
- Classification evidence may not transfer to action prediction.
- BEHAVIOR/OmniGibson setup has a current blocker: offline frame collection was segfaulting in the old note.
- Task-relevant masks may miss contact-specific regions.

## links
- [[eval/behavior]]
- [[eval/reconstruction]]
- [[synthesis/shape and action]]
