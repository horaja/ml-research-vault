---
type: experiment
project: surf
status: blocked
---

# vla adaptation

## hypothesis
A selector that helps classification may also help action prediction if its selected patches preserve task-relevant object and affordance information.

## setup
- Model: VLA-style policy with selective visual encoder.
- Prior/selector: line prior first, then language-conditioned or iterative variants.
- Eval substrate: [[behavior env stanford]] — see that note for axes, task taxonomy, and environment blockers.

## risks
- Task-relevant masks may miss contact-specific regions.

## links
- [[behavior env stanford]]
- [[eval/reconstruction]]
- [[synthesis/shape and action]]
