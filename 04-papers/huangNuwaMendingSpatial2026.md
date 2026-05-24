---
type: paper
status: unread
citekey: "huangNuwaMendingSpatial2026"
year: "2026"
---

# Nüwa: Mending the Spatial Integrity Torn by VLM Token Pruning

**Authors:** Yihong Huang, Fei Ma, Yihua Shao, Jingcai Guo, Zitong Yu, Laizhong Cui, Qi Tian
**Venue:** journalArticle
**Year:** 2026
**Zotero:** [open](zotero://select/library/items/8C39A2AP) · [DOI](https://doi.org/10.48550/ARXIV.2602.02951)


## Abstract

Vision token pruning has proven to be an effective acceleration technique for the efficient Vision Language Model (VLM). However, existing pruning methods demonstrate excellent performance preservation in visual question answering (VQA) and suffer substantial degradation on visual grounding (VG) tasks. Our analysis of the VLM's processing pipeline reveals that strategies utilizing global semantic similarity and attention scores lose the global spatial reference frame, which is derived from the interactions of tokens' positional information. Motivated by these findings, we propose $\text{Nüwa}$, a two-stage token pruning framework that enables efficient feature aggregation while maintaining spatial integrity. In the first stage, after the vision encoder, we apply three operations, namely separation, alignment, and aggregation, which are inspired by swarm intelligence algorithms to retain information-rich global spatial anchors. In the second stage, within the LLM, we perform text-guided pruning to retain task-relevant visual tokens. Extensive experiments demonstrate that $\text{Nüwa}$ achieves SOTA performance on multiple VQA benchmarks (from 94% to 95%) and yields substantial improvements on visual grounding tasks (from 7% to 47%).


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


