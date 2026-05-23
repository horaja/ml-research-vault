# Roadmap for ICML/NeurIPS Submission

## Theory Extensions (Pick 1-2)

### 1. [[Patch Selection and Sparsity Theory#^281ba6|Formal IB Analysis]]
- Derive a variational upper bound on $I(Z;X)$ given your selection mechanism
- Prove that under assumptions about line-drawing quality (e.g., edge preservation), your selector minimizes $I(Z;X)$ subject to $I(Z;Y) ≥ I(Y;Y) - ε$
- Connect patch budget $k$ to rate-distortion curves

### 2. [[Background Overview#^7bb86f|PAC-Bayes / Generalization Bounds]]
- Show that the structural bottleneck (fewer tokens) provides tighter generalization guarantees
- Bound the **Rademacher complexity** of your hypothesis class vs. full ViT
- Prove sample efficiency gains when the true task only depends on shape

### 3. Online/Adaptive Selection Theory
- Frame patch selection as a sequential decision problem (bandits/active sensing)
- Prove regret bounds for iterative refinement of the selector
- Connect to attention mechanisms—show your method approximates learned attention with explicit geometric priors
### 4. Mathematical Models of Neuroscience Abstractions
- Use results derived from these mathematical models to motivate shape-biased patch selection.
	- Create a mathematical model for shape-bias

## Empirical Extensions (Do Most of These)

### 1. Scale Up Classification
- Move to ImageNet-1K; compare against ToMe, DynamicViT, EfficientFormer
- Add out-of-distribution benchmarks (ImageNet-A, ImageNet-R) to validate shape-bias robustness claims

### 2. Complete VLA Experiments
- Run SmolVLA on ≥3 LeRobot tasks (pick-place, cabinet, drawer)
- Measure success rate, latency, and robustness under occlusion/clutter
- Compare to: (a) full encoder, (b) random patch drop, (c) uniform downsampling

### 3. Ablate Selection Mechanism
- Show learned scorer (train on reconstruction loss) vs. your line-drawing scorer
- Iterative selection (select k₁ patches, refine to k₂) vs. one-shot
- Test different line-drawing generators (sketch RNN, ControlNet edges, etc.)

### 4. Real-World Transfer
- Deploy on physical robot or use domain-randomized sim
- Show your method degrades less than baselines when cameras shift or lighting changes


### Minimum Viable Contribution for ICML/NeurIPS

- **Theory:** Add one formal result—either IB variational bound OR PAC-style generalization guarantee
- **Experiments:** ImageNet-1K results + at least 2 VLA tasks with ablations showing your method beats random selection AND one other non-trivial adaptive selection method at the same compute budget
- **Novelty hook:** Position this as "the first principled fusion of shape-prior selection with IB-driven token budgets in VLAs"

### Higher-Impact Version (if I have 4-6 months)

- Make the selector **[[Towards a New Selector|learnable and iterative]]** (this addresses your intuition)
	- Iterative can mean control-theoretic feedback loop, or iterative through layers of backbone.
- Prove convergence/approximation guarantees for the learned selector - THEORY
- Show it discovers better patches than line-drawing heuristics on complex scenes - occlusion, affordance-biased, etc.
	- Can turn this into full generalization theory section, with strong empirical results.
- Demonstrate 3-5× speedup on real robot with maintained success rates - actual latency needed.

## Concrete Next Steps (Prioritized)

1. Run ImageNet-1K experiments to see if your method scales (if accuracy drops >2% @ 40% PP, the approach may need rethinking)
2. Finish ≥2 VLA tasks and generate preliminary success/latency plots
	1. Real World latency necessary - test on standard edge compute
3. Draft one formal theorem (I'd start with a PAC-style bound—easier than full IB analysis)
	1. How does this apply though? For motivation—Rather use shape-bias/mixed selection/gaze prediction neuroscience topics.
4. **Week 5-6:** Implement learned scorer variant and compare to line-drawing baseline
	1. Why? What am I trying to show here? Is this unnecessarily overcomplicating?
5. **Week 7-8:** Write paper, iterate on framing

## Key Insight

**Novelty at top venues requires either breakthrough theory OR breakthrough empirical gains**—incremental improvements on both won't suffice. Your best bet is to lean into the VLA angle (fewer papers do robotics) and add *just enough* theory to justify the design, rather than trying to compete with pure theory papers.