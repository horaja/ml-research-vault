---
type: synthesis
project: surf
---

# where to look

## question
What should guide selective visual computation for VLA-style systems?

## current view
The strongest current evidence supports a structural line prior for ImageNet-10 classification. The central research risk is whether classification-useful structure overlaps with action-relevant structure.

## supported
- [[experiments/e001]] supports lower-compute selective patch processing in the current classification repo.

## speculative
- Structural priors may help VLA action prediction.
- V4-inspired preferences may provide useful mid-level shape guidance.
- Iterative selection may reduce wasted visual compute.

## tensions
- Biological motivation is useful, but current evidence does not show biological faithfulness.
- Gaze alignment may not track action relevance.
- Strong baselines could explain much of the observed benefit.

## links
- [[claims/structure helps]]
- [[claims/efficiency without collapse]]
- [[experiments/vla adaptation]]
- [[eval/baselines]]
