---
type: project
project: surf
status: active
---

# roadmap

## current framing
surf is organized around a three-module architecture for learning where to look:
- prior module: proposes or biases spatial regions
- VLA/action module: consumes selected visual evidence for task behavior
- efficiency/RL module: controls adaptive allocation under a visual budget

See [[synthesis/architecture]].

## live claims
- [[claims/structure helps]]
- [[claims/efficiency without collapse]]
- [[claims/language helps]]
- [[claims/iterative selection]]
- [[claims/v4 relevance]]

## evidence
- [[experiments/e001]] (complete) is the line-guided patch selection result motivating the prior module.
- [[sources/proposal]] preserves the larger VLA/action and adaptive-computation framing.
- [[99-attachments/images/model_architecture.jpeg|model architecture sketch]] records the current three-module architecture.

## missing evidence
- Baselines that distinguish structure from center bias and generic edge density.
- Action-task evaluation showing whether selected visual evidence improves task behavior.
- Operational evidence for V4 alignment in action tasks.
- Training objective for adaptive where-to-look decisions under budget.

## falsifiers
- Center bias matches or beats structural priors under the same visual budget.
- Language-conditioned selection does not beat a zero-language ablation.
- Adaptive refinement spends extra compute without improving task success, compute efficiency, sample efficiency, or generalization.
- Gaze alignment improves while task performance does not.

## next experiments
- [ ] Use [[eval/reconstruction]] and [[behavior env stanford]] to connect selection with task relevance.
- [ ] Run [[experiments/contrastive alignment]] to test instruction-conditioned spatial selection.

## tooling
- [ ] Audit tracked S2 author IDs in the digest config — `s2_author` returned 0–1 papers for 10+ consecutive runs; Tai Sing Lee, Chelsea Finn, Sergey Levine known to publish frequently.
- [ ] Wire up `hit_count` tracking in `fetch_papers.py` so the 7-day retirement rule can apply to low-yield queries.
- [ ] Configure a Claude Code hook that sends host-computer notifications when Claude needs a permission prompt.

## central papers
- [[Chan et al. (2022)]]
- @jiangTRIPSEfficientVisionandLanguage2025
- [[Mees et al. (2023)]]
- [[He et al. (2021)]]
- [[Bolya et al. (2023)]]
- [[Rao et al. (2021)]]

## stale directions
- Routing networks for functional module selection are likely the wrong abstraction for spatial patch selection.
- SNNs
