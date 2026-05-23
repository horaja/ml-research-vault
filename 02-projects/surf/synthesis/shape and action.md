---
type: synthesis
project: surf
---

# shape and action

## question
Does shape or line structure identify regions that matter for action?

## possible mechanism
Manipulation may depend on object boundaries, affordance geometry, contact regions, and obstacles. Line drawings may preserve some of this structure while discarding texture/background.

## risks
- Contact surfaces may be too fine-grained for line-density scoring.
- Texture/color can be task-relevant.
- A structural prior can select visually salient contours that are irrelevant to the action.

## decisive tests
- [[eval/reconstruction]] on task masks.
- [[experiments/vla adaptation]] with task success under matched compute.
- Baselines in [[eval/baselines]].

## links
- [[synthesis/architecture]]
- [[claims/structure helps]]
- [[concepts/task relevance]]
- [[claims/v4 relevance]]
