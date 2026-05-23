> This document serves as an overview for Module 1 of the architecture, including any research questions answered with it.

## Research Questions

1. What, possibly learned, representation serves as the most effective prior for our case. 
	1. Why do we care—think big picture?
2. How can we evaluate and validate these representations?

## Evaluating Prior Representations

At a high level, **what is our prior doing**?
- Biasing the patch selector.

But what is a **good bias**, or an **ideal bias**?

**Two Options**:
1. Patch-level "Informative-ness"
	1. Provides **Information Sufficiency** Signals
2. Similarity to an Oracle Representation
	1. **Isolates** prior better
### Option A: Compare patch-level 'informative'-ness

From **Luo et. al. (2024)**, we get a **task-agnostic** reconstruction shift metric.
**Key Obstacle**: Task-agnostic. Thus we must create a **task-dependent reconstruction shift metric.**

#### Towards Creating a Task-dependent R.S. Metric
Instead of measuring reconstruction similarity between input image and reconstructed image, measure the reconstruction similarity of the task-dependent portions of the input image, and the task-dependent portions of the reconstructed image—i.e. $$Quality(Task, Prior) = -H(W \odot I, W \odot I^R)$$where $I^R = MAE(P_{selected})$ and some $W$.

Note 1: $W$ **cannot depend on the prior**, otherwise circular logic.
Note 2: To remove MAE-confounding, isolate the prior calculation by taking ratio of metric calculated when MAE receives all patches.

**Idea 2: $W$ can be derived from the task**:
$W$ is a *mask* over task-mentioned objects through a grounded segmentation model.
- **Note**: This creates a dependency/upper-bound via the accuracy of the segmentation model—poor segmentation results can unfairly penalize/reward the prior.
	- Mitigation: use Behavior's OmniGibson's in-built semantic and instance segmentation module as ground-truth.

### Option B: Measure Similarity to an Oracle Representation

From **Kim et. al. (2024)**, we obtain a dataset providing task-specific human attention maps.
Then, use **correlation methods** to measure similarity to our **spatial attention map**.
**Key Obstacle** - distribution of input data from DAA dataset may not match our intended evaluation set BEHAVIOR-1K.
- **Possible Future Solution** - create our own human attention maps.
- **Obstacle 2** - Dataset only provides one pixel containing current gaze location.

#### Some Approaches to Create 'Oracle' Heatmaps
1. Isotropic Gaussian Heatmap
	1. *Novel minor contribution*: Vergence-modulated $\sigma$
2. Semantic-Conditioned Expansion
3. Foveated Acuity Model
Key ==Flawed Assumption==: If $W$ derived from gaze, and we claim that prior is trained/designed to align with human attention, then conclusion is really: *"Our prior mimics human gaze"*, and less about capturing informationally rich regions.

#### Similarity Measures
1. Normalized Scanpath Saliency
2. AUC-Judd
3. Pearson Correlation Coefficient

## Candidate Representations

1. **Line Drawings** - Current, as implemented in preliminary results.
	1. Pros: Static, efficient
	2. Cons: non-task-specific, only relying on shape and not language/instruction input.
2. **Line Drawings + Language Embeddings**
	1. Pros: Task-specific, more context
	2. Cons: More complex, more params, learned, etc.

### Towards an Implementation...
#### Aside: Gist Selectors/Detectors
- What are they? Why are they relevant?
- Can Line Drawing be an effective gist detector?

#### Key Obstacle: Fusion Mechanism between LD and L.E.

~~**Idea 1**: [R. Yang, H. Xu, Y. Wu, and X. Wang. Multi-task reinforcement learning with soft modularization.|Routing Networks]~~
- Reframe problem as: "How does the language embedding/task/instruction **modulate** which spatial regions matter?"
	- Where spatial regions are patches of *line drawing*. Each layer is an iterative refinement of weights over patches.
- **Cons**: Routing may not be the correct abstraction for this problem, as it is designed for **functional abstraction**, not *spatial selection*.
	- Too many patches to map directly to computational modules, but then using some processing modules in their place adds unnecessary indirection and complexity
	- Don't have key problem that routing attempts to solve: **parameter interference**
	- Hierarchical and compositional inductive bias hurts spatial prior creation

**Possible Directions** *(simplest to most complex)*
1. [FiLM](https://arxiv.org/pdf/1709.07871)-Gated Patch Scorer
2. Contrastive alignment + top-k selection - [[Jiang et al. (2025)|TRIPS Patch Selection for VLMs]]
3. Cross-Attention Patch Prior
4. Energy-based cross-modal scoring - Similar Inspiration: [[Mees et al. (2023)|HULC++]]
5. Variational Attention Spatial Prior
	1. Incorporate a prior to (4), easily extensible to *Module 3's uncertainty prediction* via the posterior variance per patch.

**Key Note**: For any approach, pre-training of certain weights can be done with the DAA Gaze Prediction Data
- e.g. Pre-training of projection matrices of (2)
- e.g. Speed up convergence for (5)

#### Methods
- **Simpler PoC**: Contrastive Alignment
- **The Better Approach for rest of Architecture**: Variational Spatial Prior
	- Specifically for Module 3 and the iterative architecture
	- ==TODO==: Literature Review
## Theoretical Motivation
By finding an optimal prior that will help guide us toward the most ~~efficient~~ (relevant?) collection of patches. Note that since our current method of extracting line drawings are representative of human behavior and human attention, we can also hypothesize that <candidate representation 2> above is an approximation of **task-specific human attention**.

