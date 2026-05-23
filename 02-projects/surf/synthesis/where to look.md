---
type: synthesis
project: surf
---

# where to look

## question
What should guide selective visual computation for VLA-style systems?

## current view
The project should be judged by whether selected visual evidence improves task behavior under a visual budget. The organizing architecture is [[synthesis/architecture]].

## mechanisms
- Structural priors can bias selection toward contours, shape, and object boundaries.
- Language-conditioned priors can make selection task-specific.
- V4 or mid-level shape priors may provide richer structural guidance.
- Efficiency/RL mechanisms can decide whether to stop or refine.

## tensions
- Gaze alignment may not track action relevance.
- Center bias and edge-density baselines can explain apparent attention quality.
- Biological motivation should guide inductive-bias design without becoming a biological-faithfulness claim.

## links
- [[synthesis/architecture]]
- [[claims/structure helps]]
- [[claims/efficiency without collapse]]
- [[experiments/vla adaptation]]
- [[eval/baselines]]
