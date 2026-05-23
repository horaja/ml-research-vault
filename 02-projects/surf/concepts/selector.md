---
type: concept
project: surf
---

# selector

## definition
A selector maps an image, optional prior features, and optional instruction context to a patch score map, then chooses a subset of patches under a visual budget.

## interface
- input: visual evidence, prior features, and optional instruction context
- score: patch or region relevance
- select: patches or regions under a visual budget
- output: selected visual evidence for the VLA/action module

## implementation example
[[sources/repo]] contains a selector that scores line drawing density with spatial weighting and feeds selected ViT patch embeddings forward.

## variants
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
