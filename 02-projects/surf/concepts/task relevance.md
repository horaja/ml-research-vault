---
type: concept
project: surf
---

# task relevance

## definition
A region is task-relevant if preserving or processing it changes the ability to perform the current task or predict the correct action.

## operationalization
The proposed reconstruction metric approximates task relevance with a mask over task-mentioned objects from BDDL and semantic segmentation.

## caveats
- Task-mentioned objects are not always the same as action-critical regions.
- Contact surfaces, tools, obstacles, and phase-specific targets may be missed.
- A mask must not depend on the prior being evaluated.

## links
- [[eval/reconstruction]]
- [[eval/behavior]]
- [[questions]]
