---
type: paper
status: unread
citekey: "jiangComputationalConstraintsUnderlying"
year: ""
---

# Computational constraints underlying shape and texture functional domain organization in macaque V4

**Authors:** Dunhan Jiang, Tainye Wang, Yingjue Bian, Shiming Tang, Tai Sing Lee
**Venue:** journalArticle
**Year:** 
**Zotero:** [open](zotero://select/library/items/YJXNF9Y4)


## Abstract

V4, an intermediate visual area in the ventral pathway of the primate visual system, is known to contain neurons selective to visual stimulus attributes of intermediate complexity. Recent studies have shown that macaque V4 is organized into neuronal columns, each tuned to specific natural image features, and topologically arranged across the cortical surface to form functionally specialized domains. Using digital twins of V4 constructed from a large-scale wide-field imaging dataset, we demonstrate that shape- and texture-preferring neurons — previously identified in single-unit studies — are spatially clustered into functional domains. The segregated spatial organization suggests the existence of parallel modules for surface and boundary processing. Unlike artificial neural networks trained for ImageNet classification, which exhibit a strong texture bias, we found that V4 cortical columns and functional domains are more evenly balanced between shape and texture preferences. Finally, we show that computational constraints of feature similarity and retinotopy constraints are necessary and sufficient to explain many observed properties of the organization of the V4 topological map of natural image feature preferences.


## TL;DR

## Problem

## Core idea

## Method

## Results

## Baselines / metrics

## Assumptions

## Limitations

## Math

## Follow-up questions

- What exactly is the "dispersity" measure — how is it computed, and can it be evaluated on an *arbitrary* input image via the digital twin, or only on the imaged stimulus set? (Gates whether dispersity can craft a selection prior.)
- Does the shape/texture domain segregation yield a *spatial* signal over an image (a per-location shape-vs-texture score), or only a per-column property? Is there a usable per-patch prior here at all?
- "Feature similarity + retinotopy" is necessary-and-sufficient for the map's *organization* — does that constrain *what to attend to* for a task, or only how features are laid out cortically? (Where-to-look link: real mechanism or analogy?)
- The "ImageNet ANNs are texture-biased, V4 is balanced shape/texture" result — what is the actual evidence, and does balanced shape preference predict better *task-relevant region selection*, or only better classification robustness?
- Is the digital twin / dataset available to compute a V4-derived prior, or would surf have to approximate it?

## Links


