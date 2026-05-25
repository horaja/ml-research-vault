---
type: concept
project: surf
---

# line prior

## definition
A line prior scores image patches using line-drawing structure, then selects patches with high structural content under a visual budget.

## implementation example
[[sources/repo]] contains a line-prior vision artifact that computes line drawing patch scores by average pooling line intensity over line-drawing patches, normalizing scores with softmax, and combining them with a Gaussian spatial weighting around the line drawing center of gravity.

## role
- Task-agnostic.
- Structural, not semantic or language-conditioned.

## limitations
- May reward contours useful for classification rather than action.
- May be confounded by center bias.
- Needs comparison against language-conditioned variants.

## theory
- Possible theoretical reading as a nuisance-suppression loss (texture/background as nuisance) — see @rajputMatchingPrincipleGeometric2026. Speculative; not verified.

## links
- [[sources/repo]]
- [[claims/structure helps]]
- [[eval/baselines]]
