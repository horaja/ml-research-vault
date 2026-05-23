---
type: eval
project: surf
status: planned
---

# reconstruction

## question
Given selected patches, how much task-relevant visual information is preserved?

## metric
Use a task mask `W` over relevant pixels and compare original image `I` to reconstruction `I^R` from selected patches:

`Q(Task, Prior) = -D(W * I, W * I^R)`

Normalize by the all-patches reconstruction to reduce MAE capacity confounding.

## W mask
Planned source: BDDL task objects plus semantic segmentation from BEHAVIOR/OmniGibson.

## sanity metric
Patch coverage:

`sum(selected W_patch) / sum(all W_patch)`

Random should be near `k / 196` on a 14x14 grid.

## caveats
- MAE was trained with random masks; structured prior-selected masks may behave differently.
- Task-mentioned objects are imperfect proxies for action relevance.
- Poor segmentation can unfairly penalize or reward a prior.

## links
- [[concepts/task relevance]]
- [[eval/baselines]]
- [[eval/behavior]]
