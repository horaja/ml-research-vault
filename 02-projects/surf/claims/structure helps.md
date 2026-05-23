---
type: claim
project: surf
status: supported
---

# structure helps

## claim
Line drawings are a structural prior for patch selection. Preliminary line-guided patch selection results motivate using structure as part of the prior module.

## evidence
- Code/result: [[sources/repo]]
- Experiment: [[experiments/e001]]
- Paper context: [[Chan et al. (2022)]]

## assumptions
- Line drawings preserve useful object structure.
- Structural patches relevant for classification may overlap with patches relevant for manipulation.

## counterevidence
- Center bias and Canny edge-density baselines may explain part of the gain.

## baseline
- Random selection.
- Center bias.
- Canny edge density.
- All-patches compute-matched baseline.

## links
- [[concepts/line prior]]
- [[synthesis/shape and action]]
