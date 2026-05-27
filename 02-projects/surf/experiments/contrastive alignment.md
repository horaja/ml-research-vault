---
type: experiment
status: planned
project: surf
---

# contrastive alignment

## hypothesis
A learned cross-modal scorer — projecting patch embeddings and the language embedding into a shared space and selecting top-$k$ patches by cosine similarity — produces more task-relevant selections than the task-agnostic line prior.

## setup
- Source: [[sources/line-biased-vision-encoder]] (line-prior backbone) + new repo (URL TBD).
- Visual features: patch embeddings from the line-prior ViT backbone.
- Language features: frozen text encoder.
- Scoring: shared-space cosine similarity with learnable temperature $\tau$; top-$k$ selection at inference (softmax over scores for training).
- Pre-train (optional): contrastive objective using DAA gaze as soft positives.
- Fine-tune: end-to-end on the Stanford BEHAVIOR environment (https://behavior.stanford.edu).
- Baseline: line prior only; same architecture with language vector zeroed; learned visual scorer without language; random; center-bias.
- Metrics: gaze alignment ([[eval/gaze]]), task-relevant reconstruction ([[eval/reconstruction]]), task success on BEHAVIOR_ENV, GFLOPs per action.

## result
TBD — experiment in progress.

## interpretation
Pending.

## failure analysis
Pending.

## baseline that could kill the claim
Learned visual scorer with language zeroed matching this method — would imply language carries no spatial information for the task and the gain is from the learned scorer alone.

## next action
Run gaze-pretrain → BEHAVIOR_ENV fine-tune; log per-baseline numbers; record commit hash and config.

## links
- [[claims/language helps]]
- [[concepts/selector]]
- [[synthesis/prior vs learned]]
- [[eval/gaze]]
- [[behavior env stanford]]