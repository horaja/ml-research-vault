---
type: experiment
project: surf
status: planned
---

# vla adaptation

## hypothesis
A selector that helps classification may also help action prediction if its selected patches preserve task-relevant object and affordance information.

## setup
- Dataset/task suite: Stanford BEHAVIOR environment (https://behavior.stanford.edu).
- Model: VLA-style policy with selective visual encoder.
- Prior/selector: line prior first, then language-conditioned or iterative variants.
- Metrics: task success, compute per action, sample efficiency, generalization.

## risks
- Older OmniGibson offline frame collection segfaulted; status under current BEHAVIOR_ENV unverified.
- Task-relevant masks may miss contact-specific regions.

## links
- [[behavior env stanford]]
- [[eval/reconstruction]]
- [[synthesis/shape and action]]
