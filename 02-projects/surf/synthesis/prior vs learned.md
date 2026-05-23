---
type: synthesis
project: surf
---

# prior vs learned

## question
When should selection use a handcrafted prior, a learned selector, or a variational prior/posterior?

## current view
Start with the line prior because it is implemented and has classification evidence. Use learned language conditioning as the next diagnostic. Treat the variational prior as a later architecture if language and uncertainty matter.

## comparison
- [[concepts/line prior]]: simple, implemented, task-agnostic.
- [[experiments/language conditioning]]: tests whether instruction context changes where to look.
- [[concepts/variational prior]]: adds language-only prior, image-refined posterior, and uncertainty, but increases training complexity.

## key diagnostic
If language-conditioned selection does not beat a zero-language ablation, do not invest in the variational architecture yet.

## links
- [[claims/language helps]]
- [[claims/iterative selection]]
- [[concepts/selector]]
