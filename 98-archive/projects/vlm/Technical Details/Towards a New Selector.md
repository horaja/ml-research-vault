### Motivation
Current Architecture: A pre-ViT, fixed selector
Downsides:
1. Cannot retain valuable information from lost patches
2. Treats Shape-Biased auxiliary representation as "Ground Truth"
I hypothesize completely cutting out patches will have a very negative effect on VLA performance.

### Methodology
#### Learned
Task: *Information-Preserving Compression relative to a reference view*
**Inputs**:
- Auxiliary Representation
	- Can encode, analyze, etc.
- Post-attention token sequence, $Z$
- Attention Weights
	- With some engineering, attention logits, Q,K,V, etc.
**Outputs**:
- Binary Mask over $Z$.

For a **regularizing metric** for a loss function, analogous to **manifold alignment**, see [[Wang et al. ()]].
- Alternatively, look into Optimal Transport, Procrustes Transform

> TODO: Research model architecture. Why? Theory? Neuro-Abstractions?

##### Idea 1
Learning a **view-conditioned minimal sufficient subset** of color image tokens.
Thus, every selected token MUST explain the shape-bias representation.

![[Learned Selector Visualization]]
#### Iterative
##### Some Control Theory
Define an MDP as $(S, A, \delta, R, \pi)$. However, this has many intrinsic assumptions. See [Markov Decisions](https://stanford.edu/~cpiech/cs221/handouts/markovDecisions.html).

Thus, many methods have been created to abstract away from concrete assumptions to fit real-world parameters more accurately. One such method is **Proximal Policy Optimization (PPO)**.

> TODO: Define **Optimal Stopping**

##### Literature Review
###### PPO for Token Pruning
From [[Lu et al. (2025)]], we see the use of **Multi-Agent Proximal Policy Optimization (MAPPO)** in token pruning across layers, where each agent decides *keep or drop* for each token, optimizing for a compute-accuracy reward.

Applications to our setting: Although we have a similar setup, our *motivation is completely different.* We condition all of our decisions on the knowledge that an auxiliary representation gives us.
- learning robust representation/learning *quickly*

[This](https://openreview.net/pdf?id=vlOfFI9vWO) is a recent ICLR 2025 Submission Paper that did very poorly on trying to apply a similar MAPPO framework to Dynamic Token Selection.

###### POMDP for VLA Models
From [[Xiao et al. (2025)]], we see the reformation of VLA models into **Partially Observable Markov Decision Processes (POMDP)**, approximating the *intractable* Belief State using a recurrent state, and then a small discussion of this framework's extension into token pruning. Specifically, the POMDP can be used to **rank** each token conditioned on the previous timestep via the **AVA module**, thus providing a *scoring mechanism* that a simple Top-K operation can select for pruning.

Applications to our setting: This seems like a learned scoring mechanism conditioned on previous timesteps. A natural extension would be to incorporate the line drawing representation, motivated by a need for affordance-bias in action-based models, and possibly some neuroscience abstractions.

> TODO: Formalize this extension.

### Ablations

1. **WHY LINE DRAWING**
	1. Possible Answer: LD gives you  -> gives you 3D structures.
	2. For **affordance**, specifically, what are existing methods to **estimate** it?

>TODO: Affordance estimation methods research.