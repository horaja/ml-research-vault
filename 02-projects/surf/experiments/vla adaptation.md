---
type: experiment
project: surf
status: planned
---

# vla adaptation

## hypothesis
A selector that helps classification may also help action prediction if its selected patches preserve task-relevant object and affordance information.

## setup
- Dataset/task suite: BEHAVIOR-style household manipulation.
- Model: VLA-style policy with selective visual encoder.
- Prior/selector: line prior first, then language-conditioned or iterative variants.
- Metrics: task success, compute per action, sample efficiency, generalization.

## risks
- BEHAVIOR/OmniGibson setup has a current blocker: offline frame collection was segfaulting in the old note.
- Task-relevant masks may miss contact-specific regions.

## links
- [[eval/behavior]]
- [[eval/reconstruction]]
- [[synthesis/shape and action]]
