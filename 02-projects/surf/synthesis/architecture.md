---
type: synthesis
project: surf
---

# architecture

## framing
surf is about learning where to look: allocating visual computation toward task-relevant information instead of processing the whole image uniformly.

The current project architecture has three interacting modules: prior, VLA/action, and efficiency/RL.

## modules

### prior
What guides where to look before or during action inference.

Examples:
- line / structure prior
- V4 / mid-level shape prior
- language-conditioned spatial prior
- learned or hand-designed task priors

### VLA/action
How selected visual information conditions action prediction.

This module represents the downstream embodied policy/action interface. It should not be reduced to any single vision-encoder artifact.

### efficiency/RL
How compute allocation becomes adaptive.

Examples:
- iterative selection
- uncertainty-conditioned refinement
- visual compute budget
- policy-learning or reinforcement-learning formulation for where to look next

## interaction
- The prior proposes or biases visual regions.
- The VLA/action module consumes selected visual evidence for task behavior.
- The efficiency/RL module controls adaptive allocation under budget.
- Experiments should test whether selection improves task success, compute efficiency, sample efficiency, or generalization.

## current evidence
- [[sources/repo]] contains the `line-biased-vision-encoder` source artifact for the line-prior vision path.
- [[experiments/e001]] records the preliminary line-guided patch selection result that motivates the prior module.
- [[sources/proposal]] preserves the high-level framing around biologically guided token selection for VLA-style systems.
- [[99-attachments/images/model_architecture.jpeg|model architecture sketch]] records the three-module architecture.

## open questions
- What makes a patch task-relevant for action?
- When should the selector refine rather than stop?
- Which baselines would kill the structural-prior claim?
- Does line structure help because of affordance relevance, shape invariance, or removal of nuisance detail?
- How should V4 alignment be operationalized for action tasks?
- What objective should train the efficiency/RL module to choose where to look next?

## links
- [[moc]]
- [[roadmap]]
- [[questions]]
- [[claims/structure helps]]
- [[claims/language helps]]
- [[claims/iterative selection]]
- [[claims/v4 relevance]]
- [[concepts/line prior]]
- [[concepts/v4 prior]]
- [[concepts/selector]]
- [[concepts/task relevance]]
- [[concepts/visual budget]]
- [[experiments/e001]]
- [[experiments/language conditioning]]
- [[experiments/iterative selection]]
- [[experiments/vla adaptation]]
- [[eval/baselines]]
- [[eval/reconstruction]]
- [[eval/gaze]]
- [[behavior env stanford]]
