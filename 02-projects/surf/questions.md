---
type: project
project: surf
---

# questions

## architecture
- How should the prior, VLA/action, and efficiency/RL modules exchange information?
- Which outputs from the VLA/action module should trigger refinement?
- Should adaptive compute be trained as a policy, a threshold rule, or a value-of-information objective?

## action relevance
- What makes a patch task-relevant for action?
- Are affordance/contact regions recoverable from structural cues alone?
- Does line structure help because of affordance relevance, shape invariance, or removal of nuisance detail?

## priors
- Does language conditioning improve spatial selection beyond a learned visual scorer with language removed?
- How should V4 alignment be operationalized for action tasks?
- When should the selector refine rather than stop?

## evaluation
- Which baselines would kill the structural-prior claim?
- Can [[eval/reconstruction]] avoid measuring MAE reconstruction artifacts instead of prior quality?
- Does [[eval/gaze]] measure task relevance, or similarity to human gaze?
- How much of the apparent signal is explained by center bias?

## implementation
- Can selector inputs stay independent of selected-patch downstream features and avoid circular dependency?
