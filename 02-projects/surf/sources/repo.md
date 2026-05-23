---
type: source
project: surf
---

# repo

## source
- Path: `/Users/husain/Documents/cmu/research/line-biased-vision-encoder`
- Commit inspected: `0543ccf`
- Read-only inspection date: 2026-05-23

## role
This repo is one source artifact for the line-prior vision path. It should constrain statements about that artifact, not the full surf project state.

## implementation facts
- Implements `SelectiveMagnoViT`.
- Scores line drawing patches by average pooled line intensity.
- Computes a line drawing center of gravity.
- Selects patches with a spatial selector using patch scores and Gaussian weighting, or random fallback.
- Feeds selected color-image patch embeddings into a timm ViT.

## reported result
Repo README/docs report ImageNet-10 validation:
- full patch budget: Top-1 `0.734`, Top-5 `0.964`, `1.408` GFLOPs
- line-guided selective low compute: Top-1 `0.758`, Top-5 `0.968`, `0.448` GFLOPs

## links
- [[experiments/e001]]
- [[concepts/line prior]]
- [[claims/structure helps]]
- [[synthesis/architecture]]
