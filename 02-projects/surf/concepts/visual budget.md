---
type: concept
project: surf
---

# visual budget

## definition
The amount of visual input processed by the expensive model path, usually measured as selected patches, selected-token ratio, GFLOPs, or compute per action.

## current operationalization
In the repo, `patch_percentage` determines the fraction of ViT patches selected. GFLOPs are measured for a single forward pass.

## planned operationalization
For VLA systems, visual budget should include compute per action and task success under fixed or adaptive patch budgets.

## links
- [[claims/efficiency without collapse]]
- [[experiments/e001]]
- [[eval/behavior]]
