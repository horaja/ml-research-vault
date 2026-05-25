---
type: source
project: surf
---

# refactor map

Archive root: `98-archive/refactor/surf/2026-05-23/originals/`

## map

| original | archived path | new note(s) | preserved | omitted / downgraded | concerns |
|---|---|---|---|---|---|
| `moc.md` | `98-archive/refactor/surf/2026-05-23/originals/moc.md` | [[moc]] | routing intent | empty folder placeholders | none |
| `roadmap.md` | `98-archive/refactor/surf/2026-05-23/originals/roadmap.md` | [[roadmap]] | roadmap sections | empty shell | roadmap re-centered on three-module architecture |
| `open questions.md` | `98-archive/refactor/surf/2026-05-23/originals/open questions.md` | [[questions]] | durable question categories | empty shell | old links changed from `open questions` to `questions` |
| `reading list.md` | `98-archive/refactor/surf/2026-05-23/originals/reading list.md` | [[reading]] | reading categories | empty shell | old links changed from `reading list` to `reading` |
| `Project Formalization and Proposal.md` | `98-archive/refactor/surf/2026-05-23/originals/Project Formalization and Proposal.md` | [[sources/proposal]], [[claims/structure helps]], [[claims/v4 relevance]], [[synthesis/where to look]] | title, motivation, mechanisms, preliminary result, VLA plan, biological caution | empty proposal template sections | proposal claims are historical framing unless repo-supported |
| `Module 1/Overview.md` | `98-archive/refactor/surf/2026-05-23/originals/Module 1/Overview.md` | [[eval/reconstruction]], [[eval/gaze]], [[concepts/selector]], [[questions]], [[synthesis/prior vs learned]] | evaluation options, task relevance caveats, oracle caveats, candidate selectors | vague gist prose, repeated motivation | line-drawing-human-attention claim downgraded to speculation |
| `Module 1/Implementation Plans/Evaluation Metrics/Task-Dependant Reconstruction Shift Metric Integration.md` | `98-archive/refactor/surf/2026-05-23/originals/Module 1/Implementation Plans/Evaluation Metrics/Task-Dependant Reconstruction Shift Metric Integration.md` | [[eval/reconstruction]], [[eval/baselines]], [[behavior env stanford]], [[experiments/vla adaptation]] | metric, normalization, W mask, baselines, patch budgets, BEHAVIOR plan, segfault blocker | checklist verbosity, dependency table | expected baseline ordering is not a result |
| `Module 1/Implementation Plans/Evaluation Metrics/Oracle Similarity Metric Integration.md` | `98-archive/refactor/surf/2026-05-23/originals/Module 1/Implementation Plans/Evaluation Metrics/Oracle Similarity Metric Integration.md` | [[eval/gaze]], [[concepts/oracle map]], [[eval/baselines]], [[questions]] | NSS/AUC/CC, DAA fields, remapping, center-bias confound, DAA-BEHAVIOR gap | checklist verbosity | DAA paper note missing |
| `Module 1/Implementation Plans/Prior Design Algorithms/Contrastive Alignment.md` | `98-archive/refactor/surf/2026-05-23/originals/Module 1/Implementation Plans/Prior Design Algorithms/Contrastive Alignment.md` | [[experiments/language conditioning]], [[claims/language helps]], [[concepts/selector]], [[synthesis/prior vs learned]] | shared-space scoring, patch/language embedding options, DAA pretrain, BEHAVIOR finetune, TRIPS summary token, failure modes | long implementation prose and day-by-day plan | source inventory should include remote implementations |
| `Module 1/Implementation Plans/Prior Design Algorithms/Variational Spatial Prior.md` | `98-archive/refactor/surf/2026-05-23/originals/Module 1/Implementation Plans/Prior Design Algorithms/Variational Spatial Prior.md` | [[concepts/variational prior]], [[claims/iterative selection]], [[experiments/iterative selection]], [[synthesis/prior vs learned]] | prior/posterior split, ELBO, KL risks, gaze auxiliary loss, iterative loop, circular dependency rule | theorem-like exposition and timeline filler | source inventory should include remote implementations |

## unresolved
- Missing DAA paper note.
- Need clean center-bias and Canny baselines.
- Need source inventory for remote cluster implementations.
- Need repeated seeds or confidence intervals for current ImageNet-10 result.
