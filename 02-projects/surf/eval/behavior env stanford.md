---
type: eval
project: surf
status: planned
---


## purpose
Evaluate selective visual computation on household manipulation tasks rather than classification.

## planned axes
- Task success.
- Compute per action / GFLOPs.
- Sample efficiency / demonstrations needed.
- Generalization.
- Human/model attention overlap.

## planned task types
Tasks targeted at the current Stanford BEHAVIOR environment (https://behavior.stanford.edu): single-object articulated tasks, multi-object pick-and-place, multi-step shifting relevance, fine manipulation, and complex multi-object goals.

## source context
An archived implementation note records a blocker where offline frame collection was segfaulting under the older OmniGibson setup; revisit under BEHAVIOR_ENV.

## links
- [[sources/behavior-1k]]
- [[experiments/vla adaptation]]
- [[eval/reconstruction]]
- [[concepts/task relevance]]
