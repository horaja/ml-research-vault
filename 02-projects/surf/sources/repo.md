---
type: source
project: surf
---

# repo

## source
- Path: `/Users/husain/Documents/cmu/research/line-biased-vision-encoder`
- Commit inspected: `0543ccf`
- Read-only inspection date: 2026-05-23

## current implementation facts
- Implements `SelectiveMagnoViT`.
- Scores line drawing patches by average pooled line intensity.
- Computes a line drawing center of gravity.
- Selects patches with a spatial selector using patch scores and Gaussian weighting, or random fallback.
- Feeds selected color-image patch embeddings into a timm ViT.
- Current task is ImageNet-style classification, not VLA/action prediction.

## reported result
Repo README/docs report ImageNet-10 validation:
- full patch budget: Top-1 `0.734`, Top-5 `0.964`, `1.408` GFLOPs
- line-guided selective low compute: Top-1 `0.758`, Top-5 `0.968`, `0.448` GFLOPs

## not currently implemented
- VLA/action prediction.
- BEHAVIOR/OmniGibson evaluation.
- DAA gaze evaluation.
- Contrastive language-conditioned selector.
- Variational prior/posterior selector.
- Iterative coarse-to-fine patch selection.

## links
- [[experiments/e001]]
- [[concepts/line prior]]
- [[claims/structure helps]]
