# Executive Summary
This project develops a biologically-inspired dual-stream Vision-Language Model that mimics the human brain's parallel visual processing pathways—separating spatial/motion processing (dorsal/"where" stream) from object/texture recognition (ventral/"what" stream). The dorsal stream will utilize computationally efficient line drawings or magnocellular-style transforms for rapid spatial understanding, while the ventral stream processes detailed texture information for object identification. A sensor fusion pipeline will integrate outputs from both streams, with data containerization directing appropriate visual features to each pathway. This architecture aims to achieve significant computational efficiency gains while maintaining high accuracy for vision-language-action tasks, drawing on established neuroscience principles of how biological vision systems process information in parallel specialized pathways.
#### Key Research Question
How can we improve speed, robustness, and accuracy of VLA models?
**Hypothesis**: Using shape-biased patch selection and brain-inspired dual stream architecture, we can enhance efficiency, increase robustness, and maintain accuracy of VLA models.
**Goal**: Creating a 2-stage, *Plug-and-Play* framework.
#### Expected Contributions
1. Substantial reduction in token count driving lower inference times
2. Enhanced Model Robustness/Domain Invariance
3. Novel, Generalizable Framework for VLA architectures as a plug-n-play module

# Problem Statement
#### Motivation
Current Vision-Language-Action (VLA) models are too computationally expensive and fragile for real-world robotics, requiring high-end GPUs and failing under common conditions like motion blur, occlusions, or poor lighting. This prevents their deployment in critical applications—from disaster response and agricultural automation to assistive robotics—where real-time performance on edge devices and robustness to unpredictable environments are essential. By developing a biologically-inspired dual-stream architecture that separates spatial and object processing, we can reduce computational requirements while improving robustness, finally enabling VLA deployment in these untapped domains.
#### Research Gap
No existing VLA architecture systematically implements the brain's dual-stream processing strategy. 
#### Success Metrics
1. **Efficiency**:
	1. Inference Latency
	2. Throughput
	3. Memory Footprint (Tokens)
2. **Robustness**:
	1. Shape-Bias (SIN)
	2. Domain Shift
3. **Accuracy**:
	1. Task Completion
	2. Spatial Reasoning
	3. Object Manipulation

# Literature Review
#### VLA Models in Robotics
1. **RT-2** [[Brohan et al. ()]]
2. **OpenVLA** [[Kim et al. (2024)]]
3. **Octo** [[Team et al. (2024)]]
#### Biological Visual Dual-Stream Processing Theory
1. Existence of Dorsal and Ventral Streams 
2. Dorsal Inference Faster than Ventral Stream [[Maunsell et al. (1999)]]
#### Token Reduction
1. **DynamicViT** [[Rao et al. (2021)]]
2. **EfficientFormer** [[Li et al. (2022)]]
3. etc.
#### Masked Autoencoders (MAEs)
 - Similarity to our project: Process small amount of patches to get a representation equivalent to 100% of patches
#### Meta's Sam 3D
- 2 Stage Pipeline for creating 3D from 2D
	- First model is a Mixture of Transformers that predicts coarse shape and layout
	- Second model takes the predicted voxels and adds high-res details 
# Technical Approach
#### Methods
Our approach implements a **SelectiveMagnoViT** stream that leverages line drawings as an attention mechanism for selective patch processing in Vision Transformers. The system uses a dual-input strategy where magnocellular-like (Magno) images provide the main visual features while line drawings guide the selection of important patches, significantly reducing computational requirements. This creates the **Dorsal** Stream.

Furthermore, we also make the **Ventral** Stream, and implement **Stream Fusion**.

See [[Implementation Notes]] for implementation-level specifics.
#### Model Architecture
1. **Dorsal Stream**
	1. *Patch Importance Scorer*
		1. Non-learnable *(for now...?)*, analytical scoring mechanism
		2. Utilizes edge detection via Line Drawing Generation
			1. Uses *contour-style*
				1. Most biologically-accurate, no outside biases, cleanest
	2. *Spatial Threshold Selector*
		1. Intakes Magno-style Images
			1. Sensitive to *rapid* motion/temporal changes
				1. Depth Perception through motion parallax
			2. large receptive fields -> low spatial resolution *(blurry)*
			3. Sensitive to low-contrast stimuli
			4. Gray-scale
		2. Uses COG $\mapsto$ Gaussian Spatial Weights and Scores
		3. Selects $k$ patches
	3. *Vision Transformer Backbone*
		1. Base ViT
		2. Custom Patch Embedding
		3. Adaptive Positional Encoding
		4. Modified Attention
		![[Dorsal Stream Architecture]]
2. **Ventral Stream**
	1. *(TBD)*
3. **Stream Fusion**
	1. *(TBD)*
#### Key Innovations
1. **Spatially-Aware** Patch Selection
	1. *Using COG, Guassians*
2. etc.
#### Assumptions/Limitations

# Experiments

# Progress Timeline
See [[Tasks]] for current progress and ToDos.
# Results & Findings

#### Preliminary Results
#### Key Insights

# Resources
*Insert code repository, dataset source, compute specifications, etc*

# Open Questions
1. Replacing **Edge Detection/Shape-biased Scoring Module** with non-LD generation
	1. Depth Map/Foreground-Background Segmentation
		1. Focus on reducing token count/model size here
2. Dorsal Stream focuses on **detecting *action***, incorporate via...
	1. GRU as an element of scoring module
3. **Ventral Stream**
	1. Dual Stream? Or single stream with ventral property incorporation?
4. If dual stream, **stream fusion**?
5. *Theoretical Bounds* on sparsity impacts of task performance.

# Communication
#### Paper Submission Targets
1. **Arxiv**
2. **NeurIPS 2026**
	1. Abstract Deadline: 01/23/26
	2. Paper Deadline: 01/28/26
#### Presentation Materials

## ITERATIVE VLA
#### Literature Review
##### [[Bai et al. (2025)]]
- Created an iterative VLM architecture
- Things to note: verifier head
- Things to ignore: MDP, DPO
##### [[Graves et al. (2017)]]
- Stochastic verifier head for early stopping
- Canonically for RNNS, applied to VLA/VLMs
- Potential for novel use and contribution
##### [[Qiao et al. (2025)]]
- Reasoning steps can actively trigger new visual queries.
#### Notes
Main Idea: Given that static selection is performant across domains, can the selection process itself become **conditional** and **iterative**?

**Key Concept: Test-time scaling**:
- Definition: ML paradigm where Model performance is improved by increasing the computational budget allocated to the _inference_ phase, rather than the _training_ phase.

**SIMPLER, different Idea**: Create a dataset using line-drawing-selection, use that to train/SFT/etc. a NN for shape-biased patch selection.

**Arguments to make for ICML submission**:
1. Idea must be algorithmically novel (e.g. one of these)
	1. A **new stopping rule** that is task-conditional and evidence-dependent
	2. *A **new selection policy** over visual tokens / patches / actions with provable properties*
	3. *A **new objective** implicitly optimized by the iterative process*
	4. A **new decomposition** of perception vs reasoning at test time
2. Neuroscience angle must a theoretical justification for a formal abstraction
	1. Examples of theory angles:
		1. **Optimal stopping**: when should the model stop gathering more visual evidence?
		2. **Submodularity / diminishing returns**: each iteration yields less marginal information
		3. ***PAC-style guarantees**: how many iterations are needed to reach ε-confidence?*
			1. Similar to question seen in 10-701: How much *data* is needed...
		4. ***Information-theoretic framing**: maximize mutual information per unit compute*
3. Use classification results as **validation of the principle**, not the main result.
	1. Ensure VLA results show generalization of the principle, and embodied consequences.
4. Focus on very strong results in at-least one of:
	1. Clear regime change
	2. Compute-performance frontier shift
	3. Failure-mode elimination

