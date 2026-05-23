# Some topics
### [[Core Transformer Theory]]
1. **Self Attention** as a Kernel Method
	1. *Kernel Similarity Function*
	2. Reproducing Kernel Hilbert Spaces
	3. Connection between softmax and kernel functions
2. **Expressivity** and **Approximation** Theory of Transformers
	1. Universal approximation results for transformers
	2. Turing completeness arguments
	3. Circuit complexity of attention
3. **Positional Encoding** Theory
	1. Different types of Encodings
	2. Theoretical Limitations of Encodings
	3. RoPE and ALiBi Derivations
### [[Patch Selection and Sparsity Theory]]
1. **Information Bottleneck** Principle
	1. **Key Question**: How does patch selection approximate the [[Patch Selection and Sparsity Theory#^6befa3|IB Principle]]/[[Patch Selection and Sparsity Theory#^c8f935|Optimal IB Limit]]
2. **Rate-Distortion** Theory
	1. Related to impacts of sparsity
	2. Connection to Learned Representations
3. **Token Pruning Theory**, Approximation Bounds
	1. Importance scoring theory
	2. Top-k selection as optimization

### [[Self-Supervised Learning Theory|Self-Supervised Learning Theory]]
1. **Masked Autoencoder** Theory
	1. Reconstruction as pretext task
	2. Relationship to denoising autoencoders
	3. Implicit regularization from masking
2. **Contrastive Learning** & DINO
	1. InfoNCE loss derivation
	2. Mutual Information maximizing interpretation
	3. Self-distillation dynamics
	4. Centering and Sharpening in DINO

### Robustness and Generalization
1. Formalization of **Shape-Bias** vs **Texture-Bias** Theory
	1. Shortcut Learning Theory
	2. Spurious correlations
	3. Role of Inductive Bias in Generalization
2. **Domain Generalization** Theory
	1. Invariant risk minimization
	2. Domain-invariant representations
	3. PAC-Bayes bounds for domain adaptation ^7bb86f
3. **Causal** Representation Learning
	1. Independent Causal Mechanisms
	2. Interventions
	3. Identifiability of causal features

### Gaussian Processes & Spatial Kernels
1. **Gaussian Process** Fundamentals
	1. Kernel composition rules
	2. Anisotropic kernels
	3. Kernel hyperparameter interpretation
2. **Depth-Aware Kernel** Design
	1. Mercer's Theorem

### Depth and Geometry
1. **Monocular Depth Estimation** Theory
2. **Multi-view Geometry** Basics

### Multi-Stream and Fusion Theory
1. Multi-Modal **Fusion Architectures**
	1. Tensor fusion theory
	2. Gated fusion
	3. Attention-based fusion optimality conditions
2. **The Binding Problem**—Computational Neuroscience
	1. Temporal synchrony hypothesis
	2. Attention-based binding
	3. Population Codes

### Optimization and Training Dynamics
1. Transformer **Training Dynamics**
	1. Attention Entropy Dynamics
	2. Neural Tangent Kernel Regime vs feature learning
2. Grokking & **Generalization Timing**
	1. Double descent
	2. Grokking
	3. Implicit regularization in overparameterized models

### Computational Complexity
1. **Attention Complexity** & Efficient Architectures
	1. Linear Attention
	2. Sparse Attention Patterns