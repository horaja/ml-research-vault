---
type: synthesis
project: surf
---

# adaptive compute

## question
How should a VLA allocate compute adaptively, and how do the existing formulations differ?

## current view
Four distinct formulations of adaptive compute for VLA appear in the recent literature:
1. **Temporal mode switch** — when to think hard vs. shallow (ElegantVLA).
2. **Critic-based confidence gating** — gate on a learned confidence signal (VLA-ATTC).
3. **Budget-relative RL reward** — train a stopping policy with budget penalties (BRPO).
4. **Spatial / depth redundancy suppression** — suppress redundant computation per step using action context (AC²-VLA).

surf sits closest to (4) and potentially adds an iterative refinement axis on top — see [[claims/iterative selection]] and the @xuVisionPulseDynamicVisual2026 evidence captured in [[2026.06.02]].

## supporting evidence
- [[2026.06.01]] synthesises the four-formulation picture in prose.
- @xuVisionPulseDynamicVisual2026 (unread, 2026.06.02 digest): reportedly shows step-dependent visual sparsity in multimodal reasoning. If the finding transfers to VLA closed-loop inference, it pushes surf toward the iterative-selection axis as a load-bearing design choice. Not yet verified from the paper.

## tensions
- TBD.

## missing experiments
- TBD.

## links
- [[claims/iterative selection]]
- [[claims/efficiency without collapse]]
- [[roadmap]]
- [[2026.06.01]]
- [[2026.06.02]]
