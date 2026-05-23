## Phase 1: Classification
#### [[Dohare et al. (2024)|Loss of plasticity in deep continual learning]]
**Core Problem**: Standard deep learning gradually loses the ability to learn when training continues over time.

Define **Plasticity**: The ability to continually learning affectively from unseen data.

Researchers observed **Loss of Plasticity**:
- neurons become *dormant* (permanently inactive)
- weights grow very large
- loses diversity in its representations ("low *stable rank*")
- performance steadily degrades on new tasks

**Authors' Solution**: Continual Backpropogation

**Applications to our project**:
- Note that robotics tasks (rl or non-rl) are inherently continual
	- Proof?
- Claim that shape-biased patch selection combats loss of plasticity
	- What about shape-biased patch selection reducing the 'stable rank'.
## Phase 3: *Iterative*, *Conditional* VLM architecture for Patch Selection
#### [[Pang et al. (2025)|Next Patch Prediction for Autoregressive Visual Generation]]

#### [[Li et al. (2025)#^fae4c8|Look Less, Reason More: Rollout-Guided Adaptive Pixel-Space Reasoning]]
**Overview of Paper**
In modern VLM frameworks, the model is given a '*zoom*' tool, called Pixel-Space Reasoning. This paper attempts to train a model to **efficiently** use this tool. Two-stage training process:
1. Supervised Fine-Tuning with AND without tool usage, for 'baseline competence' in both options.
2. Rollout-Guided Reinforcement Learning — N rollouts over 2 groups:
	1. The *Teacher* Group:
		1. Sets the **Tool Necessity Value** via forced tool and no-tool usage and comparing accuracies.
	2. The *Student* Group:
		1. Decides Tool Necessity Value, rewarded if same as Teacher Group.
**Application to Paper**: Dataset Generation/patch-selection-strategy(shape vs no-bias) using Teacher RGRL Framework
*Key Question*: Why this over LD-selection module?
- Background and non-important areas may still have many LD marks, incorrectly indicating they are important.
- However, this framework only specified a patch as important if it actually leads to higher accuracy. Using RL, you can learn a dynamic sequence conditioned on **Semantic Intent of the Query** (and the current reasoning state), thus it is more robust than static selection
	- Nuance: Instead of forcing tool-usage vs non-tool-usage, force shape-bias vs non-shape-bias, selecting the shape-patches via LD-selection module
#### [[Chen et al. (2025)|Think Twice to See More: Iterative Visual Reasoning in Medical VLMs]]
**Research Gap**: VLM performance in medical applications is sub-par due to their *single-pass* nature.

**Core Innovation**: A cognitive chain called **Think-Act-Rethink-Answer**, to mimic expert diagnostic behavior.

**Training Strategy**: SFT + RL

**Dataset Curation**: Used Roboflow Datasets with Bounding Boxes and LLMS to generate QA dataset for RL Training. Used GPT-4o to develop cognitive chains for SFT training.

**Key Observation**: The 'round 2' act and rethink tells the model ***where*** to look. For medical applications, this ensures the VLM is concentrating on pathologically relavent sections.

**Potential Application**: For VLA models in robotics applications, we can influence the model by ensuring it attends to the ***shape*** of the surrounding objects more, as there is literature that this enhances grasping and other robotics capabilities. We can do this by using the same ViTAR framework, but curating the training dataset using shape-biased models, such as our [[Project Overview - DISCONTINUED|Selective-Magno-ViT]].
#### [[Kwok et al. (2025)|RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models]]