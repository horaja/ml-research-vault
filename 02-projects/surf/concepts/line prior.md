---
type: concept
project: surf
---

# line prior

## definition
A line prior scores image patches using line-drawing structure, then selects patches with high structural content under a visual budget.

## current implementation
The repo computes line drawing patch scores by average pooling line intensity over line-drawing patches, normalizing scores with softmax, and combining them with a Gaussian spatial weighting around the line drawing center of gravity.

## role
- Current implemented prior.
- Task-agnostic.
- Structural, not semantic or language-conditioned.

## limitations
- May reward contours useful for classification rather than action.
- May be confounded by center bias.
- Does not use task language.

## links
- [[sources/repo]]
- [[claims/structure helps]]
- [[eval/baselines]]
