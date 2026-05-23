---
type: eval
project: surf
status: planned
---

# gaze

## question
Does the prior attend to regions where humans look during manipulation?

## data
The old plan uses DAA gaze data: image frames, language descriptions, and left/right gaze coordinates. A durable DAA paper note is missing.

## metrics
- NSS: sample normalized attention at gaze locations.
- AUC-Judd: classify fixated vs non-fixated pixels.
- Pearson correlation: compare attention map to a Gaussian gaze heatmap.

## implementation details
- Resize DAA global images to the selector input size and remap gaze coordinates.
- Use the wide global image rather than foveated crops.
- Prefer upsampling the 14x14 attention map to image resolution for saliency metrics.

## caveats
- Center bias is a serious confound.
- Human gaze similarity is not equivalent to task success.
- DAA-to-BEHAVIOR domain shift can break transfer.

## links
- [[concepts/oracle map]]
- [[eval/baselines]]
- [[questions]]
