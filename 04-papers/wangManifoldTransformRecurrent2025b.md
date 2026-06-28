---
type: paper
status: unread
citekey: "wangManifoldTransformRecurrent2025b"
year: "2025"
---

# Manifold Transform by Recurrent Cortical Circuit Enhances Robust Encoding of Familiar Stimuli

**Authors:** Weifan Wang, Xueyan Niu, Liyuan Liang, Tai-Sing Lee
**Venue:** preprint
**Year:** 2025
**Zotero:** [open](zotero://select/library/items/NR64WBG7) · [DOI](https://doi.org/10.1101/2025.03.02.641067)


## Abstract

A ubiquitous phenomenon observed along the ventral stream of the primate hierarchical visual system is the suppression of neural responses to familiar stimuli at the population level. The observation of the suppression of the neural response in the early visual cortex (V1 and V2) to familiar stimuli that are multiple times larger in size than the receptive fields of individual neurons implicates the plausible development of recurrent circuits for encoding these global stimuli. In this work, we investigated the neural mechanisms of familiarity suppression and showed that an recurrent neural circuit based on Hebbian learning, consisting of neurons with small and local receptive fields, can develop to encode specific global familiar stimuli robustly as a result of familiarity training. We proposed that the learned recurrent circuit implements a manifold transform. The recurrent circuit compresses the dimensions of irrelevant variations of a familiar image in the neural response manifold relative to the dimensions for discriminating different familiar stimuli, resulting in increased robustness of the global stimulus representation against noise and other irrelevant perturbations. We demonstrate that a recurrent circuit implements the manifold transform using a mixed strategy of locally linear and globally nonlinear computations, where the local linear computation selectively redistributes recurrent gain to enhance concept discrimination. These results provide testable predictions for neurophysiological experiments.


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

- Does familiarity training change *where / how much* capacity the circuit allocates, or only *how robustly* a fixed representation encodes the stimulus? (The decider for [[claims/iterative selection]] × familiarity.)
- The manifold transform "compresses irrelevant variation" — is that an allocation/selection mechanism (fewer dims spent on familiar input, mapping onto a visual budget), or purely an encoding-robustness story?
- Is "familiarity" here per-whole-image (global stimulus) or per-region? Could it support *region-level* cheap-vs-expensive selection, which is what surf's efficiency module needs?
- Is there any *inference-time compute* gain for familiar inputs, or only representational robustness? (If no compute saving, the familiarity ↔ selection bridge dies.)
- Which testable prediction here, if any, could be operationalized as a surf experiment?

## Links


