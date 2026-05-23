---
type: experiment
project: surf
status: planned
---

# language conditioning

## hypothesis
Instruction-conditioned patch scoring selects more task-relevant patches than task-agnostic line scoring.

## setup
- Visual features: start with line drawing patch features.
- Language features: frozen sentence or vision-language text encoder.
- Scoring: shared-space similarity or richer MLP score.
- Selection: top-k or soft selection during training.

## baselines
- Line prior only.
- Same architecture with language vector zeroed.
- Learned visual scorer without language.
- Random and center bias.

## metrics
- Gaze alignment from [[eval/gaze]].
- Task-relevant reconstruction from [[eval/reconstruction]].
- Downstream action success when VLA setup exists.

## result
Not run.

## risks
- Language may not contain useful spatial information.
- DAA gaze supervision may not transfer to BEHAVIOR-style scenes.
- Cosine similarity may be too weak; failure should not immediately falsify language conditioning.

## links
- [[claims/language helps]]
- [[synthesis/prior vs learned]]
- [[concepts/selector]]
