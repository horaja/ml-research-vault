---
type: claim
project: surf
status: speculative
---

# language helps

## claim
Instruction-conditioned patch scoring may select more task-relevant patches than a task-agnostic line prior.

## why it might be true
- Manipulation instructions can disambiguate which object or region matters.
- A contrastive selector can score patch-language compatibility directly.

## missing evidence
- No language-conditioned selector exists in the current repo.
- No zero-language ablation.
- DAA gaze supervision may not teach action relevance if gaze and action-relevant regions diverge.

## baseline that could kill it
- Same architecture with language replaced by zeros.
- Line prior only.
- Learned visual scorer without language.

## links
- [[experiments/language conditioning]]
- [[synthesis/prior vs learned]]
- [[eval/gaze]]
