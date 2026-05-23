---
type: concept
project: surf
---

# oracle map

## definition
An oracle map is an external spatial target used to evaluate whether a prior attends to relevant regions.

## gaze oracle
The proposed gaze evaluation uses human gaze points or heatmaps as an oracle for where humans looked during manipulation.

## metrics
- NSS samples normalized attention at gaze locations.
- AUC-Judd treats attention as a classifier for fixated pixels.
- Pearson correlation requires a continuous heatmap.

## caveat
Human gaze similarity is not equivalent to action relevance. Center bias is a serious confound.

## links
- [[eval/gaze]]
- [[eval/baselines]]
