---
type: synthesis
project: surf
---

# prior vs learned

## question
When should selection use a hand-designed prior, a learned selector, or a variational prior/posterior?

## current view
Use hand-designed priors as interpretable starting points and kill baselines. Use learned selectors when instruction or image context must change where to look. Use variational prior/posterior machinery when uncertainty and iterative refinement become central.

## comparison
- [[concepts/line prior]]: simple structural prior.
- [[experiments/language conditioning]]: tests whether instruction context changes where to look.
- [[concepts/variational prior]]: connects language-only prior, image-refined posterior, and uncertainty.

## key diagnostic
If language-conditioned selection does not beat a zero-language ablation, the next change should target task signal, scoring capacity, or supervision before adding more architecture.

## links
- [[synthesis/architecture]]
- [[claims/language helps]]
- [[claims/iterative selection]]
- [[concepts/selector]]
