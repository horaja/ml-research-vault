---
type: concept
project: surf
---

# selector

## definition
A selector maps an image, optional prior features, and optional instruction context to a patch score map, then chooses a subset of patches under a visual budget.

## current interface
Current repo:
- input: color image plus optional line drawing
- score: line drawing density and spatial weighting
- select: random or spatially biased sampled indices
- output: selected ViT patch embeddings plus positional embeddings

## planned variants
- Contrastive language-conditioned selector.
- Variational prior/posterior selector.
- Iterative coarse-to-fine selector.
- Summary-token variant that preserves some unselected context.

## hard rule
Avoid circular dependency: selector inputs should not depend on features computed from already-selected downstream patches within the same forward pass.

## links
- [[concepts/line prior]]
- [[concepts/variational prior]]
- [[experiments/language conditioning]]
- [[experiments/iterative selection]]
