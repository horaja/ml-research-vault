---
type: concept
project: surf
---

# variational prior

## definition
A planned latent-variable selector with a language-conditioned prior `p(z | l)` and an image-conditioned posterior `q(z | x, l)` over patch relevance.

## purpose
- Produce a language-only first-pass attention map.
- Refine attention with image evidence.
- Use posterior uncertainty to drive iterative patch requests.

## training idea
Optimize action prediction while regularizing posterior attention toward the prior with a KL term. Optional gaze supervision can shape prior/posterior maps when gaze annotations exist.

## failure modes
- Posterior collapse if KL is too strong.
- Prior underfitting if KL is too weak or prior capacity is low.
- Attention mode collapse to fixed regions.
- Gaze-language decorrelation.
- Circular dependency if selector sees selected-patch downstream features.

## status
Design plan only. Not implemented in the current repo.

## links
- [[claims/iterative selection]]
- [[experiments/iterative selection]]
- [[synthesis/prior vs learned]]
