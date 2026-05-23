---
type: claim
project: surf
status: supported
---

# structure helps

## claim
Line drawings are a structural prior for patch selection. Current support is classification-only: the repo reports improved ImageNet-10 accuracy at lower compute when line-guided selection is used.

## evidence
- Code/result: [[sources/repo]]
- Experiment: [[experiments/e001]]
- Paper context: [[Chan et al. (2022)]]

## assumptions
- Line drawings preserve useful object structure rather than only class-discriminative contours.
- Structural patches relevant for classification may overlap with patches relevant for manipulation.

## counterevidence
- No current VLA/action result.
- Center bias and Canny edge-density baselines may explain part of the gain.

## baseline
- Random selection.
- Center bias.
- Canny edge density.
- All-patches compute-matched baseline.

## links
- [[concepts/line prior]]
- [[synthesis/shape and action]]
