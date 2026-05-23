---
type: eval
project: surf
---

# baselines

## selector baselines
- Random selection.
- Center bias.
- Canny edge density.
- Line drawing overlap.
- Oracle upper bound.

## language baselines
- Language-conditioned selector.
- Zero-language ablation.
- Learned visual scorer without language.

## compute controls
- All patches.
- Equal patch budget.
- Equal GFLOPs or latency where possible.

## kill criteria
- Center bias matches or beats the proposed prior.
- Canny edge density matches or beats line drawings.
- Zero-language matches language-conditioned selection.
- Equal-compute dense or random baselines erase the advantage.

## links
- [[claims/structure helps]]
- [[claims/language helps]]
- [[eval/reconstruction]]
- [[eval/gaze]]
