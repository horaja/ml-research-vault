---
type: paper
status: unread
citekey: "liCogVLACognitionAlignedVisionLanguageAction2026a"
year: "2026"
---

# CogVLA: Cognition-Aligned Vision-Language-Action Model via Instruction-Driven Routing & Sparsification

**Authors:** Wei Li, Renshan Zhang, Rui Shao, Jie He, Liqiang Nie
**Venue:** preprint
**Year:** 2026
**Zotero:** [open](zotero://select/library/items/UIA3BWFE) · [DOI](https://doi.org/10.48550/arXiv.2508.21046)


## Abstract

Recent Vision-Language-Action (VLA) models built on pre-trained Vision-Language Models (VLMs) require extensive post-training, resulting in high computational overhead that limits scalability and deployment.We propose CogVLA, a Cognition-Aligned Vision-Language-Action framework that leverages instruction-driven routing and sparsification to improve both efficiency and performance. CogVLA draws inspiration from human multimodal coordination and introduces a 3-stage progressive architecture. 1) Encoder-FiLM based Aggregation Routing (EFA-Routing) injects instruction information into the vision encoder to selectively aggregate and compress dual-stream visual tokens, forming a instruction-aware latent representation. 2) Building upon this compact visual encoding, LLM-FiLM based Pruning Routing (LFP-Routing) introduces action intent into the language model by pruning instruction-irrelevant visually grounded tokens, thereby achieving token-level sparsity. 3) To ensure that compressed perception inputs can still support accurate and coherent action generation, we introduce V-L-A Coupled Attention (CAtten), which combines causal vision-language attention with bidirectional action parallel decoding. Extensive experiments on the LIBERO benchmark and real-world robotic tasks demonstrate that CogVLA achieves state-of-the-art performance with success rates of 97.4% and 70.0%, respectively, while reducing training costs by 2.5-fold and decreasing inference latency by 2.8-fold compared to OpenVLA. CogVLA is open-sourced and publicly available at https://github.com/JiuTian-VL/CogVLA.


## TL;DR
- Take OpenVLA, use **instruction** to throw away most of visual tokens. Do this at 2 different stages, then let the action tokens see each other so they decode in one pass.
	- What does that last part mean?

## Problem

## Core idea

## Method

## Results
- 98.6% on Libero-Spatial $>$ 76.5% OpenVLA
- 2.5x cheaper to train
- 2.8x faster to run

## Baselines / metrics

## Assumptions

## Limitations

## Math

## Follow-up questions

## Links


