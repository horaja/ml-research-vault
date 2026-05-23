---
type: project
project: surf
---

# questions

## action relevance
- Does a line prior select regions needed for action prediction, or only regions useful for classification?
- Are affordance/contact regions recoverable from structural cues alone?

## priors
- Does language conditioning improve spatial selection beyond a learned visual scorer with language removed?
- Is a V4-derived prior meaningfully different from generic line/edge density?

## evaluation
- Can [[eval/reconstruction]] avoid measuring MAE reconstruction artifacts instead of prior quality?
- Does [[eval/gaze]] measure task relevance, or only similarity to human gaze?
- How much of the apparent signal is explained by center bias?

## implementation
- The current repo implements classification only. What is the minimal VLA/action setup that tests the core claim?
- Can selector inputs stay independent of selected-patch downstream features and avoid circular dependency?

## contradictions
- The project motivation leans on biological vision, but current evidence is ImageNet-10 classification.
- Human gaze alignment may be useful but does not by itself establish action relevance.
