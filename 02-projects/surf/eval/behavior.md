---
type: eval
project: surf
status: planned
---

# behavior

## purpose
Evaluate selective visual computation on household manipulation tasks rather than classification.

## planned axes
- Task success.
- Compute per action / GFLOPs.
- Sample efficiency / demonstrations needed.
- Generalization.
- Human/model attention overlap.

## planned task types
Old note proposed BEHAVIOR-1K-style tasks such as single-object articulated tasks, multi-object pick-and-place, multi-step shifting relevance, fine manipulation, and complex multi-object goals.

## current blocker
Old note says offline frame collection was segfaulting. Treat BEHAVIOR evaluation as planned until the implementation repo supports it.

## links
- [[experiments/vla adaptation]]
- [[eval/reconstruction]]
- [[concepts/task relevance]]
