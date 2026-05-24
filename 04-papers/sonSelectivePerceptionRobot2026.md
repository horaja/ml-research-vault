---
type: paper
status: unread
citekey: "sonSelectivePerceptionRobot2026"
year: "2026"
---

# Selective Perception for Robot: Task-Aware Attention in Multimodal VLA

**Authors:** Young-Chae Son, Jung-Woo Lee, Yoon-Ji Choi, Dae-Kwan Ko, Soo-Chul Lim
**Venue:** journalArticle
**Year:** 2026
**Zotero:** [open](zotero://select/library/items/CK3BLIWW) · [DOI](https://doi.org/10.48550/ARXIV.2602.15543)


## Abstract

In robotics, Vision-Language-Action (VLA) models that integrate diverse multimodal signals from multi-view inputs have emerged as an effective approach. However, most prior work adopts static fusion that processes all visual inputs uniformly, which incurs unnecessary computational overhead and allows task-irrelevant background information to act as noise. Inspired by the principles of human active perception, we propose a dynamic information fusion framework designed to maximize the efficiency and robustness of VLA models. Our approach introduces a lightweight adaptive routing architecture that analyzes the current text prompt and observations from a wrist-mounted camera in real-time to predict the task-relevance of multiple camera views. By conditionally attenuating computations for views with low informational utility and selectively providing only essential visual features to the policy network, Our framework achieves computation efficiency proportional to task relevance. Furthermore, to efficiently secure large-scale annotation data for router training, we established an automated labeling pipeline utilizing Vision-Language Models (VLMs) to minimize data collection and annotation costs. Experimental results in real-world robotic manipulation scenarios demonstrate that the proposed approach achieves significant improvements in both inference efficiency and control performance compared to existing VLA models, validating the effectiveness and practicality of dynamic information fusion in resource-constrained, real-time robot control environments.


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

## Links


