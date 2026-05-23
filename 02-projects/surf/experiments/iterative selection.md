---
type: experiment
project: surf
status: planned
---

# iterative selection

## hypothesis
Iterative coarse-to-fine selection improves performance under matched compute by requesting additional patches only when uncertainty warrants it.

## setup
- Pass 1: cheap prior selection.
- Pass 2: image-refined posterior selection.
- Pass 3: add patches from high-uncertainty regions if needed.

## baselines
- One-shot top-k with the same total patch count.
- Fixed larger k.
- Random extra patches.

## metrics
- Accuracy or action success at matched GFLOPs.
- Additional patches requested per example.
- Failure cases where early selection omitted critical regions.

## links
- [[claims/iterative selection]]
- [[concepts/variational prior]]
- [[concepts/selector]]
